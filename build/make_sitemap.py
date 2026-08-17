#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera site/sitemap.xml com lastmod real, a partir da data de modificação de cada página."""
import os, time

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
BASE = "https://curitibaortopedia.com.br/"

PRIORIDADE = {
    "index.html": ("1.0", "weekly"),
    "ortopedistas-em-curitiba.html": ("0.9", "weekly"),
    "crm-rqe-como-verificar-ortopedista.html": ("0.8", "monthly"),
    "qual-medico-procurar-para-cada-dor.html": ("0.8", "monthly"),
    "cadastre-se.html": ("0.7", "monthly"),
    "sobre.html": ("0.4", "yearly"),
    "privacidade.html": ("0.3", "yearly"),
}
PADRAO = ("0.8", "monthly")


def main():
    paginas = sorted(p for p in os.listdir(SITE) if p.endswith(".html"))
    linhas = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for nome in paginas:
        caminho = os.path.join(SITE, nome)
        lastmod = time.strftime("%Y-%m-%d", time.localtime(os.path.getmtime(caminho)))
        loc = BASE if nome == "index.html" else BASE + nome
        prio, freq = PRIORIDADE.get(nome, PADRAO)
        linhas += ["  <url>",
                   "    <loc>%s</loc>" % loc,
                   "    <lastmod>%s</lastmod>" % lastmod,
                   "    <changefreq>%s</changefreq>" % freq,
                   "    <priority>%s</priority>" % prio,
                   "  </url>"]
    linhas.append("</urlset>")
    with open(os.path.join(SITE, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(linhas) + "\n")
    print("sitemap.xml gerado com %d páginas" % len(paginas))


if __name__ == "__main__":
    main()
