#!/usr/bin/env python3
# Visual scan simulator for README demos
import sys, time, random

BANNER = "[>] CYBERDECK :: SCAN ENGINE v0.7 <]>"
LINES = [
    "Initializing modules",
    "Loading core modules.list",
    "Decrypting payload header",
    "Checking integrity",
    "Mapping network nodes",
    "Extracting artifacts",
    "Finalizing"
]

# Nova função para retornar a saída como texto
def get_scan_output():
    output = []
    output.append(BANNER)
    
    max_len = max(len(line) for line in LINES)
    
    for line in LINES:
        status = random.choice(["OK", "OK", "OK", "WARN", "ERR"])
        padding = "." * (max_len - len(line) + 3)
        output.append(f"{line}{padding}[{status}]")
        
    output.append("\n > SCAN COMPLETE - all systems nominally")
    return "\n".join(output)


def main():
    """Função original para rodar no terminal, se quiser."""
    print("+" + "-"* (len(BANNER)+2) + "+")
    print("| " + BANNER + " |")
    print("+" + "-"* (len(BANNER)+2) + "+")
    
    for i, line in enumerate(LINES):
        sys.stdout.write(f"{line: <35}")
        sys.stdout.flush()
        time.sleep(0.1)
        for _ in range(random.randint(5, 15)):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(random.random()*0.1)

        status = random.choice(["OK", "OK", "WARN", "ERR"])
        print(f"[{status}]")
        time.sleep(0.45 + random.random()*0.3)
        
    print("\n > SCAN COMPLETE - all systems nominally")

if __name__ == "__main__":
    main() # Quando executado diretamente, roda a simulação visual