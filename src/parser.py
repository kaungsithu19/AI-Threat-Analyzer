import re
from typing import List, Dict

def parse_auth_log(file_path: str) -> List[Dict]:
    """
    Very simple parser for Linux auth-style logs.
    Extracts timestamp (raw), username, source_ip, and message.
    """
    events = []
    pattern = re.compile(
        r'^(?P<ts>\w+\s+\d+\s[\d:]+)\s+\S+\s+\S+\[\d+\]:\s+(?P<msg>.*)$'
    )

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            m = pattern.match(line)
            if not m:
                continue

            msg = m.group("msg")

            # extract IP address
            ip_match = re.search(r'from\s+(\d+\.\d+\.\d+\.\d+)', msg)
            source_ip = ip_match.group(1) if ip_match else None

            # extract username
            user_match = re.search(r'for\s+(invalid user\s+)?(\w+)', msg)
            username = user_match.group(2) if user_match else None

            events.append({
                "timestamp": m.group("ts"),
                "username": username,
                "source_ip": source_ip,
                "message": msg
            })

    return events


if __name__ == "__main__":
    logs = parse_auth_log("../data/sample_logs.log")
    print(logs)
