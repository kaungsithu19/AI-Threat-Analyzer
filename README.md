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
| AI Model | OpenAI GPT |
| Data Processing | pandas, regex |
| Report Generation | Markdown / tabulate |
| Dashboard | Streamlit |
| Threat Mapping | MITRE ATT&CK rules |
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
```

---

## 🚀 Setup Instructions

### 1️⃣ Clone this Repository

```bash
git clone https://github.com/<your-username>/ai-threat-analyzer.git
cd ai-threat-analyzer
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
venv\Scriptsctivate    # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Key

Create a `.env` file:

```
OPENAI_API_KEY=sk-yourapikeyhere
```

---

## ▶️ How to Run

### Option A: CLI

```bash
python main.py data/sample_logs.log
```

Output:

```
outputs/incident_report.md
```

### Option B: Streamlit UI

```bash
streamlit run app.py
```

---

## 🧾 Example Output

**Incident Summary:**

Detected multiple SSH failures from `45.118.22.13` targeting `admin`.

**MITRE:** `T1110 – Brute Force`  
**Severity:** Medium  
**Recommendations:**
- Block IP  
- Enable 2FA  
- Review authentication policy  

---

## 🧠 Workflow Overview

1. **Input Phase:** Read log files  
2. **Preprocessing:** Extract fields  
3. **AI Analysis:** GPT interprets log patterns  
4. **MITRE Mapping:** Assign ATT&CK techniques  
5. **Report Generation:** Markdown incident report  
6. **Visualization:** Real-time Streamlit dashboard  

---

## 🔐 Security Note

- Do **NOT** upload `.env` to GitHub.  
- Remove sensitive IPs/usernames when sharing logs.

---

## 🚀 Future Enhancements

- Windows Event Log parser  
- Anomaly detection using ML  
- SOAR auto-blocking actions  
- Local LLM support (offline)  

---

## 🧑‍💻 Author

**Your Name**  
GitHub: <your-username>

---

## 📝 License

MIT License.
