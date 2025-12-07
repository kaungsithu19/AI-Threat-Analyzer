import sys
from src.parser import parse_auth_log
from src.ai_analyzer import analyze_logs_with_ai
from src.report_generator import generate_markdown_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_log_file>")
        sys.exit(1)

    log_path = sys.argv[1]
    print(f"[+] Parsing logs from {log_path}...")
    logs = parse_auth_log(log_path)

    if not logs:
        print("[-] No logs parsed. Check file path/format.")
        sys.exit(1)

    print(f"[+] {len(logs)} log entries parsed. Sending to AI for analysis...")
    findings = analyze_logs_with_ai(logs)

    print("[+] Generating incident report...")
    output_path = "outputs/incident_report.md"
    generate_markdown_report(findings, output_path)

    print(f"[+] Done. Report saved to {output_path}")

if __name__ == "__main__":
    main()
