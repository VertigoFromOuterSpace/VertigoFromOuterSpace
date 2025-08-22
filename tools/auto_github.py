#!/usr/bin/env python3
# auto_github.py - Script para automação completa do GitHub

import os
import sys
import subprocess
import time
from datetime import datetime
from cyberdeck import ascii_logo, loading_animation
from update_readme import update_readme

def run_command(command, description=""):
    """Executa comando e retorna True se sucesso"""
    try:
        if description:
            print(f"🔄 {description}...")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - SUCCESS")
            return True
        else:
            print(f"❌ {description} - ERROR: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ {description} - EXCEPTION: {e}")
        return False

def git_status():
    """Verifica status do git"""
    print("\n📊 CHECKING GIT STATUS...")
    run_command("git status", "Git Status Check")
    print()

def update_and_commit():
    """Atualiza README e faz commit"""
    print("🚀 STARTING AUTOMATED GITHUB UPDATE...\n")
    
    # 1. Atualizar README
    print("1️⃣ UPDATING README.md...")
    try:
        update_readme()
        print("✅ README.md updated with fresh animations!")
    except Exception as e:
        print(f"❌ Failed to update README: {e}")
        return False
    
    # 2. Git add
    if not run_command("git add .", "Adding changes to git"):
        return False
    
    # 3. Verificar se há mudanças
    result = subprocess.run("git diff --staged --quiet", shell=True)
    if result.returncode == 0:
        print("ℹ️  No changes to commit")
        return True
    
    # 4. Commit
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"🤖 Auto-update: Cyberdeck animations refresh - {timestamp}"
    
    if not run_command(f'git commit -m "{commit_msg}"', "Committing changes"):
        return False
    
    # 5. Push
    if not run_command("git push", "Pushing to GitHub"):
        return False
    
    print("\n🎉 GITHUB UPDATE COMPLETE!")
    return True

def setup_git_automation():
    """Configura automação do git"""
    print("⚙️  SETTING UP GIT AUTOMATION...\n")
    
    # Verifica se estamos em um repositório git
    if not os.path.exists(".git"):
        print("❌ Not a git repository. Run 'git init' first.")
        return False
    
    # Verifica configuração do git
    commands = [
        ("git config user.name", "Checking git user name"),
        ("git config user.email", "Checking git user email"),
        ("git remote -v", "Checking git remote")
    ]
    
    for cmd, desc in commands:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            print(f"✅ {desc}: {result.stdout.strip()}")
        else:
            print(f"⚠️  {desc}: Not configured")
    
    return True

def interactive_mode():
    """Modo interativo"""
    print(ascii_logo())
    loading_animation("INITIALIZING AUTO-GITHUB", 2)
    
    while True:
        print("\n" + "="*60)
        print("🤖 CYBERDECK AUTO-GITHUB MENU")
        print("="*60)
        print("[1] Update README & Push to GitHub")
        print("[2] Check Git Status")
        print("[3] Setup Git Configuration Check")
        print("[4] Force Update (no commit)")
        print("[Q] Quit")
        print("="*60)
        
        choice = input("\nSelect option [1-4/Q]: ").upper()
        
        if choice == "1":
            if update_and_commit():
                print("\n🎊 GitHub successfully updated!")
            else:
                print("\n💥 Update failed!")
            input("\nPress ENTER to continue...")
            
        elif choice == "2":
            git_status()
            input("\nPress ENTER to continue...")
            
        elif choice == "3":
            setup_git_automation()
            input("\nPress ENTER to continue...")
            
        elif choice == "4":
            try:
                update_readme()
                print("✅ README.md force updated!")
            except Exception as e:
                print(f"❌ Force update failed: {e}")
            input("\nPress ENTER to continue...")
            
        elif choice == "Q":
            print("\n👾 AUTO-GITHUB DISCONNECTED 👾")
            break
        else:
            print("❌ Invalid choice!")
            time.sleep(1)

def scheduled_update():
    """Atualização agendada (para usar com cron/task scheduler)"""
    print(f"[{datetime.now()}] 🤖 SCHEDULED UPDATE STARTING...")
    
    if update_and_commit():
        print(f"[{datetime.now()}] ✅ SCHEDULED UPDATE COMPLETE")
        return True
    else:
        print(f"[{datetime.now()}] ❌ SCHEDULED UPDATE FAILED")
        return False

if __name__ == "__main__":
    # Garante que estamos no diretório correto
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    os.chdir(project_dir)
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "--update":
            update_and_commit()
        elif command == "--schedule":
            scheduled_update()
        elif command == "--status":
            git_status()
        elif command == "--setup":
            setup_git_automation()
        else:
            print("Usage: python auto_github.py [--update|--schedule|--status|--setup]")
            print("  --update   : Update README and push to GitHub")
            print("  --schedule : For scheduled/automated runs")
            print("  --status   : Check git status")
            print("  --setup    : Setup git configuration check")
    else:
        interactive_mode()
