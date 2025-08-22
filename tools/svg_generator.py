#!/usr/bin/env python3
# svg_generator.py - Gera SVGs animados para o README

import random
import math
from datetime import datetime
from xml.sax.saxutils import escape

def generate_glitch_svg(width=800, height=200):
    """Gera um SVG com efeito glitch animado"""
    
    # Cores cyberpunk
    colors = ['#00ff00', '#ff0040', '#00ffff', '#ffff00', '#ff8000']
    bg_color = '#0a0a0a'
    
    svg_content = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="{bg_color}"/>'''

    # Gera linhas de "código" com glitch - usando apenas caracteres seguros
    for i in range(8):
        y = 25 + i * 22
        line_length = random.randint(40, 70)
        # Apenas caracteres alfanuméricos e símbolos seguros
        charset = '0123456789ABCDEF|+-=[]{}()/*~^_'
        chars = ''.join(random.choices(charset, k=line_length))
        
        color = random.choice(colors)
        delay = i * 0.2  # Stagger animation

        svg_content += f'''
  <text x="20" y="{y}" font-family="monospace" font-size="14" fill="{color}">
    {chars}
    <animate attributeName="opacity" values="1;0.3;1;0.7;1" dur="1.5s" begin="{delay}s" repeatCount="indefinite"/>
  </text>'''
    
    # Scan line animada
    svg_content += f'''
  
  <rect x="0" y="0" width="100%" height="2" fill="#00ff00" opacity="0.8">
    <animate attributeName="y" values="0;{height-2};0" dur="3s" repeatCount="indefinite"/>
  </rect>
  
  <rect x="0" y="{height//2}" width="100%" height="1" fill="#ff0040" opacity="0.5">
    <animate attributeName="opacity" values="0;1;0" dur="0.5s" repeatCount="indefinite"/>
  </rect>
  
</svg>'''
    
    return svg_content

def generate_matrix_svg(width=800, height=150):
    """Gera SVG estilo Matrix"""
    
    chars = '0123456789ABCDEF'
    
    svg_content = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#000000"/>'''
    
    # Gera colunas de caracteres Matrix
    for col in range(0, width, 15):
        for row in range(0, height, 20):
            char = random.choice(chars)
            delay = random.uniform(0, 4)
            duration = random.uniform(1, 3)
            
            svg_content += f'''
  <text x="{col}" y="{row}" font-family="monospace" font-size="12" fill="#00ff00">
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
  <rect width="100%" height="100%" fill="#1a1a1a" stroke="{color}" stroke-width="2" rx="5"/>
  
  <text x="100" y="25" text-anchor="middle" font-family="monospace" font-size="12" fill="{color}">
    CYBERDECK
  </text>
  
  <text x="100" y="45" text-anchor="middle" font-family="monospace" font-size="14" fill="{color}" font-weight="bold">
    {status}
    <animate attributeName="opacity" values="1;0.5;1" dur="2s" repeatCount="indefinite"/>
  </text>
  
  <text x="100" y="65" text-anchor="middle" font-family="monospace" font-size="10" fill="#888">
    {timestamp}
  </text>
</svg>'''
    
    return svg_content

def generate_progress_bar(label="SYSTEM LOAD", value=None):
    """Gera barra de progresso animada"""
    
    if value is None:
        value = random.randint(20, 95)
    
    color = "#00ff00" if value < 50 else "#ffff00" if value < 80 else "#ff0040"
    bar_width = value * 2.8
    
    svg_content = f'''<svg width="300" height="60" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#0a0a0a" rx="3"/>
  
  <text x="10" y="20" font-family="monospace" font-size="12" fill="#00ffff">
    {label}
  </text>
  
  <rect x="10" y="25" width="280" height="10" fill="#333" rx="2"/>
  <rect x="10" y="25" width="0" height="10" fill="{color}" rx="2">
    <animate attributeName="width" values="0;{bar_width}" dur="2s" fill="freeze"/>
  </rect>
  
  <text x="10" y="50" font-family="monospace" font-size="10" fill="{color}">
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
