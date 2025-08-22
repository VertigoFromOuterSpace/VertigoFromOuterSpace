#!/usr/bin/env python3
# svg_generator.py - Gera SVGs animados para o README

import random
import math
from datetime import datetime

def generate_glitch_svg(width=800, height=200):
    """Gera um SVG com efeito glitch animado"""
    
    # Cores cyberpunk
    colors = ['#00ff00', '#ff0040', '#00ffff', '#ffff00', '#ff8000']
    bg_color = '#0a0a0a'
    
    svg_content = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="glitch">
      <feColorMatrix type="matrix" values="1 0 0 0 0  0 0 0 0 0  0 0 1 0 0  0 0 0 1 0">
        <animateTransform attributeName="values" 
          values="1 0 0 0 0  0 0 0 0 0  0 0 1 0 0  0 0 0 1 0;
                  1 0 0 0 0.1  0 0 0 0 0  0 0 1 0 0  0 0 0 1 0;
                  1 0 0 0 0  0 0 0 0 0  0 0 1 0 0  0 0 0 1 0"
          dur="0.3s" repeatCount="indefinite"/>
      </feColorMatrix>
    </filter>
    
    <filter id="staticNoise">
      <feTurbulence baseFrequency="0.9" numOctaves="1" result="noise"/>
      <feColorMatrix in="noise" type="saturate" values="0"/>
      <feComponentTransfer result="monoNoise">
        <feFuncA type="discrete" tableValues="0.2 0.4 0.6 0.8"/>
      </feComponentTransfer>
      <feBlend in="SourceGraphic" in2="monoNoise" mode="multiply"/>
    </filter>
  </defs>
  
  <rect width="100%" height="100%" fill="{bg_color}"/>
  
  <!-- Linhas de código glitchadas -->'''
    
    # Gera linhas de "código" com glitch
    for i in range(8):
        y = 25 + i * 22
        line_length = random.randint(40, 70)
        chars = ''.join(random.choices('01010101||-+=[]{}()<>/\\~^_', k=line_length))
        
        color = random.choice(colors)
        
        svg_content += f'''
  <text x="20" y="{y}" font-family="Courier, monospace" font-size="14" fill="{color}" filter="url(#glitch)">
    {chars}
    <animate attributeName="opacity" values="1;0.7;1;0.9;1" dur="2s" repeatCount="indefinite"/>
  </text>'''
    
    # Efeito de scan line
    svg_content += f'''
  
  <!-- Scan line -->
  <rect width="100%" height="2" fill="#00ff00" opacity="0.6">
    <animateTransform attributeName="transform" type="translate" 
      values="0,-10; 0,{height}; 0,-10" dur="3s" repeatCount="indefinite"/>
  </rect>
  
  <!-- Static overlay -->
  <rect width="100%" height="100%" fill="url(#staticPattern)" opacity="0.1" filter="url(#staticNoise)"/>
  
</svg>'''
    
    return svg_content

def generate_matrix_svg(width=800, height=150):
    """Gera SVG estilo Matrix"""
    
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    svg_content = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#000000"/>
  
  <!-- Matrix rain effect -->'''
    
    for i in range(0, width, 20):
        # Cada coluna de caracteres
        for j in range(0, height, 16):
            char = random.choice(chars)
            delay = random.uniform(0, 3)
            duration = random.uniform(2, 5)
            
            svg_content += f'''
  <text x="{i}" y="{j}" font-family="Courier, monospace" font-size="12" fill="#00ff00" opacity="0.8">
    {char}
    <animate attributeName="opacity" values="0;1;0" dur="{duration}s" begin="{delay}s" repeatCount="indefinite"/>
  </text>'''
    
    svg_content += '\n</svg>'
    return svg_content

def generate_cyber_badge():
    """Gera badge SVG com informações dinâmicas"""
    
    status_options = [
        ("ONLINE", "#00ff00"),
        ("SECURE", "#00ffff"), 
        ("ENCRYPTED", "#ff6600"),
        ("SCANNING", "#ffff00")
    ]
    
    status, color = random.choice(status_options)
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    svg_content = f'''<svg width="200" height="80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a1a1a;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#2a2a2a;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <rect width="100%" height="100%" fill="url(#bgGrad)" stroke="{color}" stroke-width="2" rx="5"/>
  
  <text x="100" y="25" text-anchor="middle" font-family="Courier, monospace" font-size="12" fill="{color}">
    CYBERDECK
  </text>
  
  <text x="100" y="45" text-anchor="middle" font-family="Courier, monospace" font-size="14" fill="{color}" font-weight="bold">
    {status}
    <animate attributeName="opacity" values="1;0.5;1" dur="2s" repeatCount="indefinite"/>
  </text>
  
  <text x="100" y="65" text-anchor="middle" font-family="Courier, monospace" font-size="10" fill="#888">
    {timestamp}
  </text>
</svg>'''
    
    return svg_content

def generate_progress_bar(label="SYSTEM LOAD", value=None):
    """Gera barra de progresso animada"""
    
    if value is None:
        value = random.randint(20, 95)
    
    color = "#00ff00" if value < 50 else "#ffff00" if value < 80 else "#ff0040"
    
    svg_content = f'''<svg width="300" height="60" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#0a0a0a" rx="3"/>
  
  <text x="10" y="20" font-family="Courier, monospace" font-size="12" fill="#00ffff">
    {label}
  </text>
  
  <rect x="10" y="25" width="280" height="10" fill="#333" rx="2"/>
  <rect x="10" y="25" width="{value * 2.8}" height="10" fill="{color}" rx="2">
    <animate attributeName="width" values="0;{value * 2.8}" dur="2s" fill="freeze"/>
  </rect>
  
  <text x="10" y="50" font-family="Courier, monospace" font-size="10" fill="{color}">
    {value}%
  </text>
</svg>'''
    
    return svg_content

def save_svg_files():
    """Salva os SVGs na pasta .assets"""
    import os
    
    assets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.assets')
    os.makedirs(assets_dir, exist_ok=True)
    
    # Glitch banner
    with open(os.path.join(assets_dir, 'cyber_glitch.svg'), 'w', encoding='utf-8') as f:
        f.write(generate_glitch_svg())
    
    # Matrix effect
    with open(os.path.join(assets_dir, 'matrix_rain.svg'), 'w', encoding='utf-8') as f:
        f.write(generate_matrix_svg())
    
    # Status badge
    with open(os.path.join(assets_dir, 'status_badge.svg'), 'w', encoding='utf-8') as f:
        f.write(generate_cyber_badge())
    
    # Progress bars
    progress_types = [
        ("CPU LOAD", random.randint(15, 85)),
        ("MEM USAGE", random.randint(40, 90)), 
        ("NET TRAFFIC", random.randint(5, 70))
    ]
    
    for i, (label, value) in enumerate(progress_types):
        filename = f'progress_{label.lower().replace(" ", "_")}.svg'
        with open(os.path.join(assets_dir, filename), 'w', encoding='utf-8') as f:
            f.write(generate_progress_bar(label, value))
    
    print("✅ SVG files generated in .assets/")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--generate":
            save_svg_files()
        elif sys.argv[1] == "--glitch":
            print(generate_glitch_svg())
        elif sys.argv[1] == "--matrix":
            print(generate_matrix_svg())
        elif sys.argv[1] == "--badge":
            print(generate_cyber_badge())
        elif sys.argv[1] == "--progress":
            print(generate_progress_bar())
    else:
        print("SVG Generator - Cyberpunk Animations")
        print("Usage:")
        print("  --generate  : Save all SVGs to .assets/")
        print("  --glitch    : Show glitch SVG")
        print("  --matrix    : Show matrix SVG") 
        print("  --badge     : Show status badge")
        print("  --progress  : Show progress bar")
