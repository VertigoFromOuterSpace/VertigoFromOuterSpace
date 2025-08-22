#!/usr/bin/env python3
# Visual scan simulator for README demos
import sys, time, random
from datetime import datetime

BANNER = "[>] CYBERDECK :: SCAN ENGINE v0.7 <]>"

SCAN_PROFILES = {
    "system": [
        "Initializing kernel modules",
        "Loading system drivers",
        "Checking hardware integrity",
        "Validating memory banks",
        "Testing network interfaces",
        "Mounting file systems",
        "Starting background services"
    ],
    "network": [
        "Scanning network topology",
        "Probing active hosts",
        "Analyzing traffic patterns", 
        "Checking firewall rules",
        "Testing port accessibility",
        "Validating SSL certificates",
        "Mapping route tables"
    ],
    "security": [
        "Analyzing threat vectors",
        "Scanning for vulnerabilities",
        "Checking access permissions",
        "Validating encryption keys",
        "Testing intrusion detection",
        "Auditing user privileges",
        "Verifying security policies"
    ]
}

def get_scan_output(profile="system", show_timestamp=True):
    """
    Retorna saída de scan como texto
    
    Args:
        profile (str): Tipo de scan - "system", "network", "security"
        show_timestamp (bool): Se deve incluir timestamp
    """
    output = []
    
    if show_timestamp:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output.append(f"[{timestamp}] {BANNER}")
    else:
        output.append(BANNER)
    
    lines = SCAN_PROFILES.get(profile, SCAN_PROFILES["system"])
    max_len = max(len(line) for line in lines)
    
    for line in lines:
        # Simula diferentes probabilidades de status
        status_weights = [70, 20, 8, 2]  # OK mais provável
        status = random.choices(["OK", "WARN", "ERR", "SKIP"], weights=status_weights)[0]
        
        padding = "." * (max_len - len(line) + 3)
        output.append(f"{line}{padding}[{status}]")
        
    output.append(f"\n > SCAN COMPLETE [{profile.upper()}] - all systems nominally")
    return "\n".join(output)

def animated_scan(profile="system", delay=0.1):
    """Versão animada para terminal (original)"""
    print("+" + "-"* (len(BANNER)+2) + "+")
    print("| " + BANNER + " |")
    print("+" + "-"* (len(BANNER)+2) + "+")
    
    lines = SCAN_PROFILES.get(profile, SCAN_PROFILES["system"])
    
    for i, line in enumerate(lines):
        sys.stdout.write(f"{line: <35}")
        sys.stdout.flush()
        time.sleep(delay)
        
        for _ in range(random.randint(5, 15)):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(random.random()*0.1)

        status_weights = [70, 20, 8, 2]
        status = random.choices(["OK", "WARN", "ERR", "SKIP"], weights=status_weights)[0]
        print(f"[{status}]")
        time.sleep(0.2 + random.random()*0.3)
        
    print(f"\n > SCAN COMPLETE [{profile.upper()}] - all systems nominally")

def cyber_status():
    """Gera um status board cyberpunk"""
    status_items = [
        ("CPU LOAD", f"{random.randint(15, 85)}%"),
        ("MEM USAGE", f"{random.randint(40, 90)}%"),
        ("NET TRAFFIC", f"{random.randint(1, 999)} KB/s"),
        ("THREAT LEVEL", random.choice(["LOW", "MEDIUM", "HIGH"])),
        ("ENCRYPTION", "AES-256"),
        ("FIREWALL", "ACTIVE"),
    ]
    
    output = ["=== SYSTEM STATUS ==="]
    for item, value in status_items:
        output.append(f"{item:<12}: {value}")
    
    return "\n".join(output)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        profile = sys.argv[1]
        if profile == "--status":
            print(cyber_status())
        elif profile in SCAN_PROFILES:
            animated_scan(profile)
        else:
            print(f"Profiles disponíveis: {', '.join(SCAN_PROFILES.keys())}")
            print("Ou use --status para status board")
    else:
        print("=== CYBERDECK SCANNER DEMO ===\n")
        
        for profile in SCAN_PROFILES:
            print(f"{profile.upper()} SCAN:")
            print(get_scan_output(profile, show_timestamp=False))
            print()
        
        print("SYSTEM STATUS:")
        print(cyber_status())