from typing import List, Dict
from tabulate import tabulate
from .mitre_mapper import map_attack_to_mitre

def generate_markdown_report(findings: List[Dict], output_path: str):
    if not findings:
        content = "# Incident Report\n\nNo suspicious activity detected.\n"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        return

    content = "# Incident Report\n\n"

    for i, fnd in enumerate(findings, start=1):
        attack_type = fnd.get("attack_type", "")
        mitre_info = fnd.get("MITRE_Technique") or map_attack_to_mitre(attack_type)

        content += f"## Finding {i}\n"
        content += f"**Attack Type:** {attack_type}\n\n"

        if mitre_info:
            if isinstance(mitre_info, dict):
                content += f"**MITRE ATT&CK:** {mitre_info.get('id')} – {mitre_info.get('name')}\n\n"
            else:
                content += f"**MITRE ATT&CK (from AI):** {mitre_info}\n\n"

        content += f"**Confidence:** {fnd.get('confidence_score', 'N/A')}\n\n"
        content += "### Suspicious Events\n"

        events = fnd.get("suspicious_events", [])
        if events:
            headers = events[0].keys()
            rows = [e.values() for e in events]
            table = tabulate(rows, headers=headers, tablefmt="github")
            content += table + "\n\n"
        else:
            content += "_No detailed events returned._\n\n"

        content += "### Recommendations\n"
        content += f"{fnd.get('recommendations', 'No specific recommendations provided.')}\n\n"
        content += "---\n\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
