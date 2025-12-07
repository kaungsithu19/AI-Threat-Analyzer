import os
import io
import json
import pandas as pd
import streamlit as st

from src.parser import parse_auth_log
from src.ai_analyzer import analyze_logs_with_ai
from src.report_generator import generate_markdown_report

st.set_page_config(page_title="AI Threat Log Analyzer", page_icon="🛡️", layout="wide")

# ---- Sidebar / Header
st.title("🛡️ AI-Powered Threat Log Analyzer")
st.caption("Upload a security log → AI analysis → MITRE mapping → Incident report")

with st.sidebar:
    st.header("⚙️ Settings")
    st.markdown("Make sure your `.env` has `OPENAI_API_KEY`.")
    chunk_size = st.number_input("Max logs per chunk", min_value=10, max_value=200, value=30, step=10)
    st.markdown("---")
    st.info("Supported now: Linux `/var/log/auth.log`-style lines.\n\nWindows CSV support can be added later.")

# ---- File upload
uploaded = st.file_uploader("🔼 Upload a log file (e.g., `auth.log` or `.log` text)", type=["log", "txt", "csv", "json"], accept_multiple_files=False)

if uploaded:
    # Save uploaded file to a temp buffer / memory
    bytes_data = uploaded.read()

    # Try to detect simple text vs others
    # We built parser for auth-style text logs, so handle text first
    try:
        text_preview = bytes_data.decode("utf-8", errors="ignore")
    except Exception:
        text_preview = None

    st.subheader("👀 Preview (first 15 lines)")
    if text_preview:
        preview_lines = "\n".join(text_preview.splitlines()[:15])
        st.code(preview_lines or "(empty file)", language="text")
    else:
        st.warning("Could not preview text. If this is CSV/JSON, try opening in another tool or add a CSV/JSON parser later.")

    # ---- Parse logs
    parsed_events = []
    parse_error = None

    # If CSV/JSON were needed, you could branch here; for now, we do text parsing:
    try:
        # streamlit uploaded file is in memory; write to a tmp file so our parser can read path
        tmp_path = os.path.join("data", f"_uploaded_{uploaded.name}")
        with open(tmp_path, "wb") as f:
            f.write(bytes_data)

        parsed_events = parse_auth_log(tmp_path)
    except Exception as e:
        parse_error = str(e)

    if parse_error:
        st.error(f"Parse error: {parse_error}")
    elif not parsed_events:
        st.warning("No events parsed. Make sure this looks like Linux auth logs.")
    else:
        st.success(f"Parsed {len(parsed_events)} events ✅")

        # Show a small table sample
        df = pd.DataFrame(parsed_events)
        st.dataframe(df.head(20), use_container_width=True)

        # ---- Quick visuals
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🔢 Top Source IPs")
            if "source_ip" in df.columns:
                top_ips = df["source_ip"].value_counts().head(10)
                if not top_ips.empty:
                    st.bar_chart(top_ips)
                else:
                    st.info("No IP addresses detected.")
            else:
                st.info("No IP column available.")

        with col2:
            st.markdown("#### 👤 Top Usernames")
            if "username" in df.columns:
                top_users = df["username"].value_counts().head(10)
                if not top_users.empty:
                    st.bar_chart(top_users)
                else:
                    st.info("No usernames detected.")
            else:
                st.info("No username column available.")

        st.markdown("---")

        # ---- Analyze button
        if st.button("🤖 Analyze with AI"):
            with st.spinner("Sending to AI…"):
                findings = analyze_logs_with_ai(parsed_events)

            st.subheader("🧠 AI Findings")
            if not findings:
                st.info("No findings returned.")
            else:
                # Show raw JSON + pretty summary
                exp = st.expander("Show raw JSON from AI")
                with exp:
                    st.code(json.dumps(findings, indent=2), language="json")

                # Pretty cards
                for i, fnd in enumerate(findings, start=1):
                    st.markdown(f"### Finding {i}")
                    st.write(f"**Attack Type:** {fnd.get('attack_type','')}")
                    st.write(f"**MITRE Technique:** {fnd.get('MITRE_Technique','(not provided by AI)')}")
                    st.write(f"**Confidence:** {fnd.get('confidence_score','')}")
                    st.write("**Recommendations:**")
                    st.write(fnd.get('recommendations','-'))

                    events = fnd.get("suspicious_events", [])
                    if events:
                        st.markdown("**Suspicious Events (sample):**")
                        st.dataframe(pd.DataFrame(events).head(50), use_container_width=True)
                    st.markdown("---")

                # ---- Generate report
                out_path = os.path.join("outputs", "incident_report.md")
                generate_markdown_report(findings, out_path)
                st.success("Incident report generated ✅")

                # Let user download the report content directly
                try:
                    with open(out_path, "r", encoding="utf-8") as f:
                        report_text = f.read()
                    st.download_button(
                        "⬇️ Download Incident Report (Markdown)",
                        data=report_text,
                        file_name="incident_report.md",
                        mime="text/markdown",
                    )
                    st.markdown("Preview:")
                    st.code(report_text[:3000] if report_text else "(empty)", language="markdown")
                except Exception as e:
                    st.error(f"Could not open generated report: {e}")
