import re
import os
from divider_gen import make_divider
from scanner_sim import get_scan_output # Precisaremos modificar um pouco o scanner_sim.py

def update_readme(readme_path="README.md"):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Gera o novo conteúdo
    divider_output = "```\n" + make_divider(width=70) + "\n```"
    scanner_output = "```\n" + get_scan_output() + "\n```"

    # Substitui o conteúdo entre os marcadores
    content = re.sub(r".*", 
                     f"\n{divider_output}\n", 
                     content, flags=re.DOTALL)
    
    content = re.sub(r".*",
                     f"\n{scanner_output}\n",
                     content, flags=re.DOTALL)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    # Garante que estamos no diretório raiz do projeto
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    update_readme()