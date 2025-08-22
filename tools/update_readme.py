import re
import os
from datetime import datetime
from divider_gen import make_divider
from scanner_sim import get_scan_output

def update_readme(readme_path="README.md"):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Gera o novo conteúdo com timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    divider_output = f"```\n{make_divider(w=70)}\n```"
    scanner_output = f"```\n{get_scan_output()}\n```"

    # Substitui seções específicas se os marcadores existirem
    # Marcador para divider ASCII
    divider_pattern = r"(<!-- DIVIDER_START -->)(.*?)(<!-- DIVIDER_END -->)"
    if re.search(divider_pattern, content, re.DOTALL):
        content = re.sub(divider_pattern, 
                        f"<!-- DIVIDER_START -->\n{divider_output}\n<!-- DIVIDER_END -->", 
                        content, flags=re.DOTALL)
    
    # Marcador para scanner output
    scanner_pattern = r"(<!-- SCANNER_START -->)(.*?)(<!-- SCANNER_END -->)"
    if re.search(scanner_pattern, content, re.DOTALL):
        content = re.sub(scanner_pattern,
                        f"<!-- SCANNER_START -->\n{scanner_output}\n<!-- SCANNER_END -->",
                        content, flags=re.DOTALL)
    
    # Atualiza o timestamp de última atualização
    timestamp_pattern = r"(<!-- LAST_UPDATE -->)(.*?)(<!-- /LAST_UPDATE -->)"
    if re.search(timestamp_pattern, content, re.DOTALL):
        content = re.sub(timestamp_pattern,
                        f"<!-- LAST_UPDATE -->Last updated: {timestamp}<!-- /LAST_UPDATE -->",
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
    
    if "<!-- LAST_UPDATE -->" not in content:
        content += "\n\n<!-- LAST_UPDATE -->Last updated: Never<!-- /LAST_UPDATE -->"
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Marcadores adicionados ao README.md")

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