#!/usr/bin/env python3
# scanner_sim.py — visual scan simulator for README demos
import sys, time, random

BANNER = "[> CYBERDECK :: SCAN ENGINE v0.7 <]"
LINES = [
    "Initializing modules",
    "Loading core_modules.list",
    "Decrypting payload header",
    "Checking integrity",
    "Mapping network nodes",
    "Extracting artifacts",
    "Finalizing"
]

def rnd_dots():
    return "." * random.randint(1,5)

def main():
    print("\n" + BANNER + "\n")
    for i, line in enumerate(LINES, 1):
        sys.stdout.write(f" {i:02d} | {line}{rnd_dots():<6}")
        sys.stdout.flush()
        time.sleep(0.45 + random.random()*0.3)
        status = random.choice(["OK", "WARN", "ERR"])
        print(f"  [{status}]")
    print("\n > SCAN COMPLETE — all systems nominal\n")

if __name__ == "__main__":
    main()
