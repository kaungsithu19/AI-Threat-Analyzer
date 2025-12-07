# 🛡️ AI-Powered Threat Log Analyzer & Incident Report Generator

An AI-assisted **Blue Team tool** that automatically analyzes security logs, detects suspicious activity (e.g., brute-force, privilege escalation), maps them to **MITRE ATT&CK**, and generates a human-readable **incident report** with recommended actions.

---

## 🎯 Project Goal

To automate log review and reporting using AI reasoning.  
The system ingests Windows/Linux/SIEM logs, detects anomalies, and outputs structured findings that help security analysts focus on what matters.

---

## 🧠 Key Features

✅ Parse and normalize log files (Linux auth logs supported)  
✅ Use OpenAI GPT model for threat reasoning and pattern recognition  
✅ Auto-map detected attacks to **MITRE ATT&CK** techniques  
✅ Generate Markdown-based **Incident Reports**  
✅ Optional **Streamlit Dashboard** for real-time visualization  

---

## ⚙️ Tech Stack

| Component | Tool |
|------------|------|
| Language | Python 3.10+ |
| AI Model | OpenAI GPT (e.g., `gpt-4.1-mini`) |
| Data Processing | pandas, regex |
| Report Generation | Markdown / tabulate |
| Dashboard | Streamlit |
| Threat Mapping | MITRE ATT&CK JSON rules |
| Environment | VS Code (Windows) |

---

## 🧩 Folder Structure

```

ai-threat-analyzer/
├── data/                 # Input logs
├── outputs/              # Generated reports
├── src/                  # Source modules
│    ├── parser.py        # Log ingestion and parsing
│    ├── ai_analyzer.py   # AI-driven threat analysis
│    ├── mitre_mapper.py  # MITRE ATT&CK mapping
│    └── report_generator.py # Report creation
├── app.py                # Streamlit dashboard
├── main.py               # CLI runner
├── config.yaml           # Model config
├── requirements.txt      # Dependencies
├── .env                  # API key (DO NOT COMMIT)
└── README.md

````

## 🚀 Setup Instructions

### 1️⃣ Clone this Repository

```bash
git clone https://github.com/<your-username>/ai-threat-analyzer.git
cd ai-threat-analyzer

