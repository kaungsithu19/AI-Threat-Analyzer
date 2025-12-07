# Incident Report

## Finding 1
**Attack Type:** Brute Force Attack

**MITRE ATT&CK (from AI):** T1110 - Brute Force

**Confidence:** High

### Suspicious Events
| timestamp       | username   | source_ip    | message                                                                  |
|-----------------|------------|--------------|--------------------------------------------------------------------------|
| Nov 11 10:01:01 | admin      | 45.118.22.13 | Failed password for invalid user admin from 45.118.22.13 port 51234 ssh2 |
| Nov 11 10:01:05 | admin      | 45.118.22.13 | Failed password for invalid user admin from 45.118.22.13 port 51235 ssh2 |
| Nov 11 10:01:10 | admin      | 45.118.22.13 | Failed password for invalid user admin from 45.118.22.13 port 51236 ssh2 |
| Nov 11 10:01:15 | admin      | 45.118.22.13 | Failed password for invalid user admin from 45.118.22.13 port 51237 ssh2 |
| Nov 11 10:01:20 | admin      | 45.118.22.13 | Failed password for invalid user admin from 45.118.22.13 port 51238 ssh2 |

### Recommendations
Implement account lockout policies, enable multi-factor authentication, monitor and block suspicious IP addresses, and consider using fail2ban or similar intrusion prevention tools to limit repeated failed login attempts.

---

