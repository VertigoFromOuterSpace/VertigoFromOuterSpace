#!/usr/bin/env python3
# divider_gen.py — ASCII art generator for cyberpunk aesthetics

def make_divider(w=70, style="glitch"):
    """
    Gera divisores ASCII em diferentes estilos
    
    Args:
        w (int): Largura do divisor
        style (str): Estilo - "glitch", "matrix", "waves", "blocks"
    """
    import random
    
    if style == "glitch":
        chars = [" ", "/", "\\", "_", "^", "|", "-", "~"]
        weights = [30, 15, 15, 10, 8, 8, 8, 6]  # Mais espaços, menos ruído
    elif style == "matrix":
        chars = ["0", "1", " ", "|", "-", "+"]
        weights = [20, 20, 30, 10, 10, 10]
    elif style == "waves":
        chars = ["~", "^", "v", "-", "_", " "]
        weights = [25, 20, 20, 15, 10, 10]
    elif style == "blocks":
        chars = ["█", "▓", "▒", "░", " "]
        weights = [15, 20, 25, 25, 15]
    else:
        # Default glitch
        chars = [" ", "/", "\\", "_", "^"]
        weights = [40, 15, 15, 15, 15]
    
    out = []
    for r in range(6):
        line = ""
        for c in range(w):
            line += random.choices(chars, weights=weights)[0]
        out.append(line)
    return "\n".join(out)

def make_banner(text, width=70):
    """Cria um banner ASCII com texto"""
    padding = (width - len(text) - 4) // 2
    border = "=" * width
    
    return f"{border}\n{' ' * padding}[ {text} ]{' ' * padding}\n{border}"

def cyber_frame(content, width=70):
    """Emoldura conteúdo com estética cyberpunk"""
    lines = content.split('\n')
    top = f"╔{'═' * (width-2)}╗"
    bottom = f"╚{'═' * (width-2)}╝"
    
    framed = [top]
    for line in lines:
        # Trunca ou padroniza linha para caber na moldura
        if len(line) > width - 4:
            line = line[:width-4]
        padded = f"║ {line:<{width-4}} ║"
        framed.append(padded)
    framed.append(bottom)
    
    return "\n".join(framed)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        style = sys.argv[1]
        print(make_divider(70, style))
    else:
        print("=== CYBERDECK ASCII GENERATOR ===\n")
        
        styles = ["glitch", "matrix", "waves", "blocks"]
        for style in styles:
            print(f"{style.upper()} STYLE:")
            print(make_divider(60, style))
            print()
        
        print("BANNER EXAMPLE:")
        print(make_banner("VERTIGO FROM OUTER SPACE", 60))
        print()
        
        print("FRAMED CONTENT:")
        sample = "SYSTEM STATUS: ONLINE\nCONNECTION: SECURE\nACCESS LEVEL: ROOT"
        print(cyber_frame(sample, 50))
