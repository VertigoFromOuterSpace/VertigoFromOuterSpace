#!/usr/bin/env python3
# svg2gif.py - Gera GIF animado a partir de SVG animado

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import imageio

def svg_to_gif(svg_path, gif_path, width=800, height=200, duration=2.5, fps=15):
    """
    Renderiza um SVG animado em frames PNG usando Chrome headless e converte em GIF animado.
    Requer: Chrome, chromedriver, selenium, pillow, imageio
    """
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument(f'--window-size={width},{height}')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=chrome_options)

    # Carrega SVG localmente
    svg_url = 'file://' + os.path.abspath(svg_path)
    driver.get(svg_url)
    time.sleep(0.5)  # Espera carregar

    frames = []
    total_frames = int(duration * fps)
    for i in range(total_frames):
        png = driver.get_screenshot_as_png()
        img = Image.open(BytesIO(png)).crop((0, 0, width, height))
        frames.append(img.convert('RGB'))
        driver.execute_script(f"document.documentElement.setCurrentTime({i/fps})")
        time.sleep(1/fps)

    driver.quit()
    imageio.mimsave(gif_path, frames, duration=1/fps)
    print(f"✅ GIF salvo em {gif_path}")

if __name__ == "__main__":
    from io import BytesIO
    import sys
    if len(sys.argv) < 3:
        print("Uso: python tools/svg2gif.py .assets/cyber_glitch.svg .assets/cyber_glitch.gif")
        sys.exit(1)
    svg_to_gif(sys.argv[1], sys.argv[2])
