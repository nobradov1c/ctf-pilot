# Cyber Defence Frameworks

- **Security Analyst** role, you will be a Triage Specialist, SOC (Security Operations Center), monitoring 24/7

  - IPS - Intrusion Prevention System
  - IDS - Intrusion Detection System
  - open-source intelligence

- IP reputation and location check:

  - [AbuseIPDB](https://www.abuseipdb.com/)

## Pyramid of Pain

- Hash Values
- IP Address
  - **Fast Flux** - Fast Flux is a DNS technique used by botnets to hide phishing, web proxying, malware delivery, and malware communication activities behind compromised hosts acting as proxies. The purpose of using the Fast Flux network is to make the communication between malware and its command and control server (C&C) challenging to be discovered by security professionals. [read more](https://unit42.paloaltonetworks.com/fast-flux-101/)
- Domain Names
  - **Punycode attack** - a way of converting words that cannot be written in ASCII, into a Unicode ASCII encoding
  - URL Shorteners
    - You can see the actual website the shortened link is redirecting you to by appending "+" to it like `tinyurl.com/aaaaa+`
    - or just `curl` it without redirection (by default)
- Host Artifacts
  - traces or observables that attackers leave on the system, such as registry values, suspicious process execution, attack patterns or IOCs (Indicators of Compromise), files dropped by malicious applications, or anything exclusive to the current threat
- Network Artifacts
  - user-agent string, C2 information, or URI patterns followed by the HTTP POST requests
  - [snort](https://www.snort.org/)
- Tools
  - [MalwareBazaar](https://bazaar.abuse.ch/)
  - [MalShare](https://malshare.com/)
  - [SOC Prime Threat Detection Marketplace](https://tdm.socprime.com/)
  - [fuzzy hashing](https://ssdeep-project.github.io/ssdeep/index.html)
- TTPs - Tactics, Techniques & Procedures
  - [MITRE ATT&CK](https://attack.mitre.org/)

## Cyber kill chain - framework

The Cyber Kill Chain framework is designed for identification and prevention of the network intrusions. You will learn what the adversaries need to do in order to achieve their goals.

- Reconnaissance

  - discovering and collecting information on the system and the victim
    - [the Harvester](https://github.com/laramies/theHarvester)
    - [hunter.io](https://hunter.io/)
    - [OSING framework](https://osintframework.com/)
    - social media

- Weaponization
  - creating payload from malware and exploit
- Delivery
  - phishing email, infected USB, watering hole attack (drive-by download)
- Exploitation
- Installation
- Command & Control
- Actions on Objectives
