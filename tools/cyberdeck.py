#!/usr/bin/env python3
# cyberdeck.py - Master control script for all animations

import os
import sys
import time
import random
from datetime import datetime
from divider_gen import make_divider, make_banner, cyber_frame
from scanner_sim import get_scan_output, cyber_status, animated_scan
from update_readme import update_readme, add_markers_to_readme

def ascii_logo():
    """Logo ASCII do projeto"""
    logo = """
  ╔═══════════════════════════════════════════════════════════════╗
  ║  ██╗   ██╗███████╗██████╗ ████████╗██╗ ██████╗  ██████╗       ║
  ║  ██║   ██║██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝ ██╔═══██╗      ║
  ║  ██║   ██║█████╗  ██████╔╝   ██║   ██║██║  ███╗██║   ██║      ║
  ║  ╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██║██║   ██║██║   ██║      ║
  ║   ╚████╔╝ ███████╗██║  ██║   ██║   ██║╚██████╔╝╚██████╔╝      ║
  ║    ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝  ╚═════╝       ║
  ║                                                               ║
  ║            FROM OUTER SPACE :: CYBERDECK v3.14               ║
  ╚═══════════════════════════════════════════════════════════════╝
    """
    return logo

def loading_animation(text="LOADING", duration=3):
    """Animação de loading"""
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    
    while time.time() < end_time:
        for char in chars:
            sys.stdout.write(f"\r{char} {text}...")
            sys.stdout.flush()
            time.sleep(0.1)
    
    sys.stdout.write(f"\r✓ {text} COMPLETE!\n")

def cyberdeck_dashboard():
    """Dashboard principal do cyberdeck"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(ascii_logo())
    loading_animation("INITIALIZING CYBERDECK", 2)
    
    print("\n" + "="*70)
    print("SYSTEM STATUS:")
    print(cyber_status())
    
    print("\n" + "="*70)
    print("AVAILABLE MODULES:")
    print("[1] ASCII Divider Generator")
    print("[2] Scanner Simulation")
    print("[3] Update README.md")
    print("[4] Full Demo")
    print("[5] Setup README Markers")
    print("[Q] Quit")
    print("="*70)

def demo_all():
    """Demonstração completa de todas as funcionalidades"""
    print("\n🚀 CYBERDECK FULL DEMO 🚀\n")
    
    # 1. ASCII Art
    print("1. ASCII DIVIDER STYLES:")
    styles = ["glitch", "matrix", "waves", "blocks"]
    for style in styles:
        print(f"\n{style.upper()}:")
        print(make_divider(60, style))
    
    print("\n" + "="*60)
    
    # 2. Banner
    print("\n2. BANNER GENERATION:")
    print(make_banner("VERTIGO FROM OUTER SPACE", 60))
    
    print("\n" + "="*60)
    
    # 3. Scanner simulations
    print("\n3. SCANNER SIMULATIONS:")
    profiles = ["system", "network", "security"]
    for profile in profiles:
        print(f"\n{profile.upper()} SCAN:")
        print(get_scan_output(profile, show_timestamp=False))
    
    print("\n" + "="*60)
    
    # 4. Framed content
    print("\n4. CYBER FRAME:")
    sample = f"CYBERDECK STATUS: ONLINE\nTIMESTAMP: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\nACCESS LEVEL: ROOT\nENCRYption: ACTIVE"
    print(cyber_frame(sample, 50))

def interactive_menu():
    """Menu interativo"""
    while True:
        cyberdeck_dashboard()
        
        choice = input("\nSelect module [1-5/Q]: ").upper()
        
        if choice == "1":
            print("\n=== ASCII DIVIDER GENERATOR ===")
            style = input("Choose style [glitch/matrix/waves/blocks]: ").lower()
            if style in ["glitch", "matrix", "waves", "blocks"]:
                print(f"\n{style.upper()} DIVIDER:")
                print(make_divider(70, style))
            else:
                print("\nDefault GLITCH style:")
                print(make_divider(70))
            input("\nPress ENTER to continue...")
            
        elif choice == "2":
            print("\n=== SCANNER SIMULATION ===")
            profile = input("Choose scan [system/network/security] or ENTER for animated: ").lower()
            if profile in ["system", "network", "security"]:
                print(f"\n{profile.upper()} SCAN:")
                print(get_scan_output(profile))
            else:
                print("\nRUNNING ANIMATED SYSTEM SCAN...")
                animated_scan("system", delay=0.05)
            input("\nPress ENTER to continue...")
            
        elif choice == "3":
            print("\n=== UPDATING README.md ===")
            try:
                os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
                update_readme()
                print("✓ README.md updated successfully!")
            except Exception as e:
                print(f"❌ Error: {e}")
            input("\nPress ENTER to continue...")
            
        elif choice == "4":
            demo_all()
            input("\nPress ENTER to continue...")
            
        elif choice == "5":
            print("\n=== SETTING UP README MARKERS ===")
            try:
                os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
                add_markers_to_readme()
            except Exception as e:
                print(f"❌ Error: {e}")
            input("\nPress ENTER to continue...")
            
        elif choice == "Q":
            print("\n👾 CYBERDECK DISCONNECTED 👾")
            break
        else:
            print("❌ Invalid choice!")
            time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == "--demo":
            demo_all()
        elif command == "--update":
            os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            update_readme()
            print("README updated!")
        elif command == "--setup":
            os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            add_markers_to_readme()
        else:
            print("Usage: python cyberdeck.py [--demo|--update|--setup]")
    else:
        interactive_menu()
