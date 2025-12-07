import json
import os
import re  
from typing import List, Dict
from dotenv import load_dotenv
import yaml
from openai import OpenAI

load_dotenv()

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def chunk_logs(logs: List[Dict], chunk_size: int = 30) -> List[List[Dict]]:
    for i in range(0, len(logs), chunk_size):
        yield logs[i:i+chunk_size]

def analyze_logs_with_ai(logs: List[Dict]) -> List[Dict]:
    """
    Sends log chunks to the AI model and returns a list of findings.
    Each finding should match the JSON schema from the prompt.
    """
    config = load_config()
    client = OpenAI()

    all_findings = []

    for chunk in chunk_logs(logs, config.get("max_logs_per_chunk", 30)):
        logs_text = json.dumps(chunk, indent=2)

        prompt = f"""
You are a cybersecurity analyst. Analyze the following logs and identify any suspicious or malicious activity.

Return ONLY valid JSON in exactly this format:

{{
  "suspicious_events": [],
  "attack_type": "",
  "MITRE_Technique": "",
  "confidence_score": "",
  "recommendations": ""
}}

Logs:
{logs_text}
"""

        response = client.responses.create(
            model=config["openai_model"],
            input=prompt,
        )

        # Extract text output (Responses API structure may vary)
        ai_text = response.output[0].content[0].text
        print("=== RAW AI OUTPUT ===")
        print(ai_text)
        print("=====================")

        def clean_ai_json(ai_text: str) -> str:
            """
            Remove Markdown ```json ... ``` fences if the model includes them.
            Returns the cleaned JSON string.
            """
            text = ai_text.strip()

            # If it starts with ``` then strip the code fences
            if text.startswith("```"):
                # Remove the starting ```json or ``` or ``` something
                text = re.sub(r"^```[a-zA-Z0-9]*\s*", "", text)
                # Remove the trailing ```
                text = re.sub(r"\s*```$", "", text)

            return text.strip()

        ai_text = response.output[0].content[0].text
        print("=== RAW AI OUTPUT ===")
        print(ai_text)
        print("=====================")

        try:
            clean_text = clean_ai_json(ai_text)
            finding = json.loads(clean_text)
            all_findings.append(finding)
        except json.JSONDecodeError:
            all_findings.append({
                "suspicious_events": [],
                "attack_type": "analysis_error",
                "MITRE_Technique": "",
                "confidence_score": "0",
                "recommendations": "Model returned invalid JSON."
            })


    return all_findings
