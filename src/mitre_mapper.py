from typing import Dict

MITRE_MAP = {
    "brute force": {
        "id": "T1110",
        "name": "Brute Force"
    },
    "ssh password guessing": {
        "id": "T1110",
        "name": "Brute Force"
    },
    "privilege escalation": {
        "id": "T1068",
        "name": "Exploitation for Privilege Escalation"
    }
}

def map_attack_to_mitre(attack_type: str) -> Dict:
    if not attack_type:
        return {}
    attack_type_l = attack_type.lower()
    for keyword, mitre_info in MITRE_MAP.items():
        if keyword in attack_type_l:
            return mitre_info
    return {}
