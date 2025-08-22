import re
import os
import random
from datetime import datetime
from divider_gen import make_divider, make_banner
from scanner_sim import get_scan_output, cyber_status

def generate_dynamic_content():
    """Gera conteúdo que muda a cada atualização"""
    
    # Lista de frases cyberpunk
    cyber_quotes = [
        "The matrix has you...",
        "Wake up, Neo...", 
        "Follow the white rabbit",
        "There is no spoon",
        "Welcome to the desert of the real",
        "Ignorance is bliss",
        "The red pill or the blue pill?",
        "Free your mind",
        "What is real?",
        "Buckle your seatbelt, Dorothy"
    ]
    
    # Status systems variados
    system_status = [
        ("FIREWALL", random.choice(["ACTIVE", "UPDATING", "SCANNING"])),
        ("ENCRYPTION", random.choice(["AES-256", "RSA-4096", "QUANTUM"])),
        ("NEURAL LINK", random.choice(["STABLE", "SYNCING", "OPTIMIZING"])),
        ("THREAT LEVEL", random.choice(["LOW", "MEDIUM", "ELEVATED", "HIGH"])),
        ("DATA STREAM", random.choice(["FLOWING", "ENCRYPTED", "SECURE"])),
    ]
    
    # Monta o status
    status_display = []
    selected_systems = random.sample(system_status, 3)
    for system, status in selected_systems:
        status_display.append(f"║ {system:<12} : {status:<10} ║")
    
    # Badge estilo cyberpunk
    timestamp = datetime.now()
    quote = random.choice(cyber_quotes)
    
    dynamic_content = f"""
╔══════════════════════════════════════╗
║        CYBERDECK STATUS BOARD        ║
╠══════════════════════════════════════╣
{"".join(chr(10) + line for line in status_display)}
╠══════════════════════════════════════╣
║ UPTIME: {timestamp.strftime('%H:%M:%S'):<15} UTC: {timestamp.strftime('%d/%m')} ║
║ QUOTE: "{quote[:25]:<25}" ║
╚══════════════════════════════════════╝
"""
    
    return dynamic_content.strip()

def generate_github_badges():
    """Gera badges dinâmicos para o GitHub"""
    
    # Cores que mudam baseado na hora
    hour = datetime.now().hour
    if 6 <= hour < 12:
        color = "brightgreen"
        status = "Morning_Hack"
    elif 12 <= hour < 18:
        color = "yellow"
        status = "Afternoon_Code"
    elif 18 <= hour < 22:
        color = "orange"
        status = "Evening_Build"
    else:
        color = "red"
        status = "Night_Owl"
    
    # Badge que muda com base no timestamp
    commit_count = random.randint(100, 999)
    
    badges = f"""
![Status](https://img.shields.io/badge/Status-{status}-{color}?style=for-the-badge&logo=hackaday)
![Commits](https://img.shields.io/badge/Commits-{commit_count}-blue?style=for-the-badge&logo=git)
![Last_Update](https://img.shields.io/badge/Last_Update-{datetime.now().strftime('%H:%M:%S')}-purple?style=for-the-badge&logo=clockify)
"""
    
    return badges.strip()

def update_readme(readme_path="README.md"):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Gera conteúdo dinâmico
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Escolhe estilo aleatório para o divider
    styles = ["glitch", "matrix", "waves", "blocks"]
    chosen_style = random.choice(styles)
    
    # Escolhe perfil aleatório para o scanner
    profiles = ["system", "network", "security"]
    chosen_profile = random.choice(profiles)
    
    divider_output = f"```\n{make_divider(w=70, style=chosen_style)}\n```"
    scanner_output = f"```\n{get_scan_output(chosen_profile)}\n```"
    
    # Conteúdo dinâmico extra
    dynamic_board = f"```\n{generate_dynamic_content()}\n```"
    github_badges = generate_github_badges()

    # Substitui seções específicas se os marcadores existirem
    # Marcador para divider ASCII
    divider_pattern = r"(<!-- DIVIDER_START -->)(.*?)(<!-- DIVIDER_END -->)"
    if re.search(divider_pattern, content, re.DOTALL):
        content = re.sub(divider_pattern, 
                        f"<!-- DIVIDER_START -->\n**🎮 {chosen_style.upper()} STYLE ACTIVE**\n{divider_output}\n<!-- DIVIDER_END -->", 
                        content, flags=re.DOTALL)
    
    # Marcador para scanner output
    scanner_pattern = r"(<!-- SCANNER_START -->)(.*?)(<!-- SCANNER_END -->)"
    if re.search(scanner_pattern, content, re.DOTALL):
        content = re.sub(scanner_pattern,
                        f"<!-- SCANNER_START -->\n**📡 {chosen_profile.upper()} SCAN RESULTS**\n{scanner_output}\n<!-- SCANNER_END -->",
                        content, flags=re.DOTALL)
    
    # Adiciona status board dinâmico
    status_pattern = r"(<!-- STATUS_START -->)(.*?)(<!-- STATUS_END -->)"
    if re.search(status_pattern, content, re.DOTALL):
        content = re.sub(status_pattern,
                        f"<!-- STATUS_START -->\n**⚡ REAL-TIME STATUS**\n{dynamic_board}\n<!-- STATUS_END -->",
                        content, flags=re.DOTALL)
    
    # Adiciona badges dinâmicos
    badges_pattern = r"(<!-- BADGES_START -->)(.*?)(<!-- BADGES_END -->)"
    if re.search(badges_pattern, content, re.DOTALL):
        content = re.sub(badges_pattern,
                        f"<!-- BADGES_START -->\n{github_badges}\n<!-- BADGES_END -->",
                        content, flags=re.DOTALL)
    
    # Adiciona SVG animado
    svg_pattern = r"(<!-- SVG_START -->)(.*?)(<!-- SVG_END -->)"
    if re.search(svg_pattern, content, re.DOTALL):
        # Gera novos SVGs a cada atualização
        from svg_generator import save_svg_files
        save_svg_files()
        cache_bust = int(datetime.now().timestamp())
        
        svg_content = f"""
**🎨 LIVE CYBERDECK VISUAL**

<div align="center">
  <img src="https://raw.githubusercontent.com/VertigoFromOuterSpace/VertigoFromOuterSpace/main/.assets/cyber_glitch.svg?v={cache_bust}" alt="Cyber Glitch Animation"/>
</div>

**📊 SYSTEM METRICS**

<div align="center">
  <img src="https://raw.githubusercontent.com/VertigoFromOuterSpace/VertigoFromOuterSpace/main/.assets/progress_cpu_load.svg?v={cache_bust}" alt="CPU Load"/>
  <img src="https://raw.githubusercontent.com/VertigoFromOuterSpace/VertigoFromOuterSpace/main/.assets/progress_mem_usage.svg?v={cache_bust}" alt="Memory Usage"/>
</div>

**🔐 STATUS BADGE**

<div align="center">
  <img src="https://raw.githubusercontent.com/VertigoFromOuterSpace/VertigoFromOuterSpace/main/.assets/status_badge.svg?v={cache_bust}" alt="Status Badge"/>
</div>
"""
        
        content = re.sub(svg_pattern,
                        f"<!-- SVG_START -->{svg_content}<!-- SVG_END -->",
                        content, flags=re.DOTALL)
    
    # Atualiza o timestamp de última atualização
    timestamp_pattern = r"(<!-- LAST_UPDATE -->)(.*?)(<!-- /LAST_UPDATE -->)"
    if re.search(timestamp_pattern, content, re.DOTALL):
        content = re.sub(timestamp_pattern,
                        f"<!-- LAST_UPDATE -->🕒 Last updated: {timestamp} | Style: {chosen_style} | Scan: {chosen_profile}<!-- /LAST_UPDATE -->",
                        content, flags=re.DOTALL)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

def add_markers_to_readme(readme_path="README.md"):
    """Adiciona marcadores ao README se eles não existirem"""
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Adiciona marcadores no final do arquivo se não existirem
    if "<!-- DIVIDER_START -->" not in content:
        content += "\n\n<!-- DIVIDER_START -->\n```\n(Divider será gerado aqui)\n```\n<!-- DIVIDER_END -->"
    
    if "<!-- SCANNER_START -->" not in content:
        content += "\n\n<!-- SCANNER_START -->\n```\n(Scanner output será gerado aqui)\n```\n<!-- SCANNER_END -->"
    
    if "<!-- STATUS_START -->" not in content:
        content += "\n\n<!-- STATUS_START -->\n```\n(Status board será gerado aqui)\n```\n<!-- STATUS_END -->"
    
    if "<!-- BADGES_START -->" not in content:
        content += "\n\n<!-- BADGES_START -->\n(Badges dinâmicos serão gerados aqui)\n<!-- BADGES_END -->"
    
    if "<!-- SVG_START -->" not in content:
        content += "\n\n<!-- SVG_START -->\n(SVGs animados serão gerados aqui)\n<!-- SVG_END -->"
    
    if "<!-- LAST_UPDATE -->" not in content:
        content += "\n\n<!-- LAST_UPDATE -->Last updated: Never<!-- /LAST_UPDATE -->"
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Marcadores expandidos adicionados ao README.md")

def demo():
    """Função de demonstração que mostra as animações"""
    print("=== DEMO: CYBERDECK ANIMATION TOOLS ===\n")
    
    print("1. ASCII Divider Generator:")
    print(make_divider(w=60))
    print("\n" + "="*50 + "\n")
    
    print("2. Scanner Simulation:")
    print(get_scan_output())
    print("\n" + "="*50 + "\n")
    
    print("3. Combined output for README:")
    divider_output = f"```\n{make_divider(w=70)}\n```"
    scanner_output = f"```\n{get_scan_output()}\n```"
    print("DIVIDER SECTION:")
    print(divider_output)
    print("\nSCANNER SECTION:")
    print(scanner_output)

if __name__ == "__main__":
    import sys
    
    # Garante que estamos no diretório raiz do projeto
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--demo":
            demo()
        elif sys.argv[1] == "--add-markers":
            add_markers_to_readme()
        elif sys.argv[1] == "--update":
            update_readme()
            print("README.md atualizado com sucesso!")
        else:
            print("Uso: python update_readme.py [--demo|--add-markers|--update]")
    else:
        print("Escolha uma opção:")
        print("--demo: Mostra uma demonstração das animações")
        print("--add-markers: Adiciona marcadores ao README.md")
        print("--update: Atualiza o README.md com novo conteúdo")
        print("\nExemplo: python update_readme.py --demo")