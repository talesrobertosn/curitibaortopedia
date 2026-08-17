#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valida o layout em navegador real: mede a nav e tira capturas."""
import asyncio, os
from playwright.async_api import async_playwright

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
SHOTS = os.path.join(ROOT, "capturas")
LARGURAS = [1221, 1280, 1440, 1920]
PAGINAS = ["index.html", "ortopedistas-em-curitiba.html", "ortopedista-joelho-curitiba.html"]

MEDIDA = """() => {
  const bar = document.querySelector('.site-header .bar');
  const nav = document.querySelector('nav.mainnav');
  const brand = document.querySelector('.site-header .brand');
  const cs = getComputedStyle(bar);
  const a11y = bar.querySelector('.a11y');
  const extra = a11y ? a11y.offsetWidth + 18 : 0;
  const disponivel = bar.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
  return {
    disponivel: Math.round(disponivel),
    necessario: Math.round(nav.scrollWidth + brand.offsetWidth + extra + 18),
    navVisivel: getComputedStyle(nav).display !== 'none',
    mobile: document.body.classList.contains('nav-mobile'),
    overflow: document.documentElement.scrollWidth - document.documentElement.clientWidth
  };
}"""


async def main():
    os.makedirs(SHOTS, exist_ok=True)
    falhas = []
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for largura in LARGURAS:
            page = await b.new_page(viewport={"width": largura, "height": 900})
            await page.goto("file://" + os.path.join(SITE, "index.html"))
            await page.wait_for_timeout(700)
            m = await page.evaluate(MEDIDA)
            estado = "nav completa" if m["navVisivel"] else "menu mobile"
            print("%5dpx | disponível %4d | necessário %4d | %s | overflow %d"
                  % (largura, m["disponivel"], m["necessario"], estado, m["overflow"]))
            if m["navVisivel"] and m["necessario"] > m["disponivel"]:
                falhas.append("nav estoura o container em %dpx" % largura)
            if largura >= 1280 and m["mobile"]:
                falhas.append("nav caiu para mobile em %dpx" % largura)
            if m["overflow"] > 0:
                falhas.append("overflow horizontal em %dpx" % largura)
            await page.close()

        for largura, alt in ((390, 900), (1280, 980)):
            for nome in PAGINAS:
                page = await b.new_page(viewport={"width": largura, "height": alt})
                await page.goto("file://" + os.path.join(SITE, nome))
                await page.wait_for_timeout(900)
                m = await page.evaluate(MEDIDA)
                if m["overflow"] > 0:
                    falhas.append("overflow horizontal em %s a %dpx" % (nome, largura))
                await page.screenshot(
                    path=os.path.join(SHOTS, "%s-%d.png" % (nome.replace(".html", ""), largura)),
                    full_page=False)
                await page.close()

        # interação: menu mobile
        page = await b.new_page(viewport={"width": 390, "height": 844})
        await page.goto("file://" + os.path.join(SITE, "index.html"))
        await page.wait_for_timeout(600)
        if not await page.is_visible(".menu-toggle"):
            falhas.append("botão de menu não aparece em 390px")
        else:
            await page.click(".menu-toggle")
            await page.wait_for_timeout(400)
            if not await page.is_visible(".mobile-panel"):
                falhas.append("painel mobile não abre")
            await page.screenshot(path=os.path.join(SHOTS, "menu-mobile-390.png"))
            await page.click(".menu-toggle")
            await page.wait_for_timeout(300)
            if await page.is_visible(".mobile-panel"):
                falhas.append("painel mobile não fecha")
        await page.close()

        # interação: menu suspenso no desktop
        page = await b.new_page(viewport={"width": 1280, "height": 900})
        await page.goto("file://" + os.path.join(SITE, "index.html"))
        await page.wait_for_timeout(600)
        await page.click("nav.mainnav .nav-group .nav-btn")
        await page.wait_for_timeout(400)
        if not await page.is_visible("nav.mainnav .nav-menu"):
            falhas.append("menu suspenso não abre no desktop")
        await page.screenshot(path=os.path.join(SHOTS, "menu-desktop-1280.png"))
        await page.close()
        await b.close()

    if falhas:
        print("\nFALHAS:")
        for f in falhas:
            print("  - " + f)
        raise SystemExit(1)
    print("\nLayout validado, capturas em capturas/")


asyncio.run(main())
