#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera og-image.png e favicon.ico renderizando HTML no Chromium via Playwright."""
import asyncio, os, io
from playwright.async_api import async_playwright
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
def _resolver_site(root):
    """Aceita duas disposições: build/ ao lado de site/, ou build/ dentro do repositório."""
    cand = os.path.join(root, "site")
    if os.path.isdir(cand):
        return cand
    pai = os.path.dirname(root)
    if os.path.exists(os.path.join(pai, "index.html")):
        return pai
    return root

SITE = _resolver_site(ROOT)

OG_HTML = """
<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,600&family=Public+Sans:wght@400;600;700&display=swap">
<style>
 *{margin:0;padding:0;box-sizing:border-box}
 body{width:1200px;height:630px;background:#FAF8F5;font-family:"Public Sans",sans-serif;
      position:relative;overflow:hidden}
 .bg{position:absolute;inset:0;
     background:radial-gradient(760px 420px at 8% -10%, rgba(51,80,108,.16), transparent 62%),
                radial-gradient(620px 420px at 96% 8%, rgba(178,94,54,.16), transparent 60%)}
 .inner{position:relative;padding:78px 84px;height:100%;display:flex;flex-direction:column;justify-content:space-between}
 .brand{display:flex;align-items:center;gap:16px}
 .brand svg{width:52px;height:52px;color:#22384E}
 .wm1{font-family:"Newsreader",serif;font-size:31px;font-weight:600;color:#1A2C3D;line-height:1}
 .wm2{font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:#5E6E7B;font-weight:600;margin-top:6px}
 h1{font-family:"Newsreader",serif;font-size:69px;line-height:1.06;color:#1A2C3D;font-weight:600;
    letter-spacing:-.02em;max-width:19ch}
 p{font-size:25px;color:#33424F;margin-top:22px;max-width:34ch;line-height:1.45}
 .foot{display:flex;align-items:center;justify-content:space-between;border-top:1px solid #E5DFD6;padding-top:26px}
 .foot span{font-size:19px;color:#5E6E7B}
 .foot .tag{background:#22384E;color:#FFFFFF;font-size:17px;font-weight:600;padding:10px 22px;border-radius:999px}
 .rule{position:absolute;right:-120px;bottom:-160px;width:520px;height:520px;border-radius:50%;
       border:44px solid rgba(34,56,78,.06)}
</style></head><body>
<div class="bg"></div><div class="rule"></div>
<div class="inner">
  <div class="brand">
    <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
      <path d="M24.05 23.02 A10.5 10.5 0 1 1 24.05 8.98" fill="none" stroke="currentColor" stroke-width="4.2" stroke-linecap="round"/>
      <circle cx="26.6" cy="16" r="3.3" fill="#B25E36"/></svg>
    <div><div class="wm1">Curitiba Ortopedia</div><div class="wm2">Guia de ortopedistas</div></div>
  </div>
  <div>
    <h1>Ortopedista em Curitiba, sem propaganda</h1>
    <p>Guia por área de atuação e explicação honesta sobre o que a evidência mostra.</p>
  </div>
  <div class="foot"><span>curitibaortopedia.com.br</span><span class="tag">Projeto informativo gratuito</span></div>
</div></body></html>
"""

ICON_HTML = """
<!doctype html><html><head><meta charset="utf-8"><style>
 *{margin:0;padding:0}html,body{width:256px;height:256px;background:transparent}
</style></head><body>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="256" height="256">
  <rect width="32" height="32" rx="7" fill="#22384E"/>
  <path d="M22.9 21.7 A8.6 8.6 0 1 1 22.9 10.3" fill="none" stroke="#FFFFFF" stroke-width="3.6" stroke-linecap="round"/>
  <circle cx="24.7" cy="16" r="2.9" fill="#B25E36"/>
</svg></body></html>
"""


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1200, "height": 630},
                                      device_scale_factor=1)
        await page.set_content(OG_HTML, wait_until="networkidle")
        await page.wait_for_timeout(900)
        await page.screenshot(path=os.path.join(SITE, "og-image.png"))

        icon = await browser.new_page(viewport={"width": 256, "height": 256})
        await icon.set_content(ICON_HTML, wait_until="networkidle")
        png = await icon.screenshot(omit_background=True)
        await browser.close()

    img = Image.open(io.BytesIO(png)).convert("RGBA")
    img.save(os.path.join(SITE, "favicon.ico"),
             sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    img.resize((180, 180), Image.LANCZOS).save(os.path.join(SITE, "apple-touch-icon.png"))
    print("og-image.png, favicon.ico e apple-touch-icon.png gerados")


asyncio.run(main())
