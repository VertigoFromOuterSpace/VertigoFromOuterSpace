#!/usr/bin/env python3
# divider_gen.py — quick ascii generator
def make_divider(w=70, waves=6):
    import random
    out = []
    for r in range(6):
        line = ""
        for c in range(w):
            line += random.choice([" ", "/", "\\", "_", "^"])
        out.append(line)
    return "\n".join(out)

if __name__ == "__main__":
    print(make_divider(70))
