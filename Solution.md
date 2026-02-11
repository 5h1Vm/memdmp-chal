# Shadow Dump - Solution

## Quick Solution Steps

### Step 1: Find Suspicious Process
```bash
vol3 -f memdump.mem windows.pslist
Look for: python.exe (Note the PID, e.g., 2600)
```
### Step 2: Extract Command Line
```bash
vol3 -f memdump.mem windows.cmdline --pid 2600
Output: python shadow_agent.py --job=CTF{v0latility_n3wbi3 --mode=stealth
```

## Flag Part 1: CTF{v0latility_n3wbi3

### Step 3: Dump Process Memory
```bash
vol3 -f memdump.mem windows.memmap --pid 2600 --dump
Creates: pid.2600.dmp
```
### Step 4: Find Encoded Data
```bash
strings pid.2600.dmp | grep "SECRET" -A1
Output: SECRET_CREDENTIAL_BASE64_FLAG_NEARBY WHpSdU5sOWphRFJzZlE9PQ==
````
### Step 5: Double Decode Base64
```bash
echo "WHpSdU5sOWphRFJzZlE9PQ==" | base64 -d | base64 -d
Output: _4n6_ch4l}
```
### Step 6: Assemble Flag
```bash
Part 1: CTF{v0latility_n3wbi3
Part 2: _4n6_ch4l}
```
## Flag:   CTF{v0latility_n3wbi3 _4n6_ch4l}