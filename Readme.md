# Shadow Dump – Memory Forensics Challenge

## Description

FinTech Solutions' SOC received an alert at 03:47 AM for unusual database activity originating from workstation `WKSTN-2847`. The endpoint detection system flagged an interactive login and the execution of unfamiliar scripts outside normal business hours. Preliminary investigation revealed a Python process running with elevated privileges, attempting connections outside the infrastructure. The analyst contained the workstation and captured volatile memory before terminating the process. The forensic image is now with your team for analysis.

As the Incident Response Analyst, your objective is to examine the memory dump and determine what credentials or sensitive data were accessed. Process configuration data, memory regions, and heap allocations may contain evidence of the intended exfiltration. Your goal is to recover the complete secret credential string.

---

## Challenge Information

- **Category:** Memory Forensics
- **Difficulty:** Medium
- **Estimated Time:** 30–45 minutes
- **Flag Format:** `CTF{...}`

---

## Learning Outcomes

- Volatile memory analysis: process enumeration and inspection using a modern memory forensics framework
- Memory forensics: locating and reconstructing data from process memory allocations
- Basic cryptanalysis/encoding recognition in memory artifacts

---

## Download

- **Memory Dump:** `memdump.mem` (≈1 GB)

---

## Setup

### Install Volatility 3

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install volatility3
```

**Linux (Arch):**
```bash
sudo pacman -S volatility3
```

**macOS (Homebrew):**
```bash
brew install volatility
```

**Windows:** Download the latest Volatility 3 release from the official project repository.

---

## Hints

Use only if you are stuck.

- **Hint 1:** Start by identifying unusual or short‑lived processes and their command lines.
- **Hint 2:** Pay attention to processes running with elevated privileges or unusual parent–child relationships.
- **Hint 3:** If you only recover part of the flag, investigate adjacent memory regions and related allocations.
- **Hint 4:** If the data looks random but structured, consider common encodings before assuming it is encrypted.

---

## Tools Required

- Volatility 3 – memory forensics framework
- strings – extract printable text from binaries (standard on most systems)
- grep – pattern searching utility
- base64, xor,etc  – encoding/decoding utility

---

## Flag Format

All flags must be submitted in the format:  

```text
CTF{...}
```

---

**Good luck, Analyst.**