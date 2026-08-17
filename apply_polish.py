#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_polish.py — propaga CSS, JavaScript, marca, navegação, bloco de contato
e rodapé para todas as páginas do diretório site/.

Fonte única da verdade:
    design.css  -> bloco <style> de todas as páginas e site/styles.css
    newjs.txt   -> bloco <script> de todas as páginas e site/main.js
    este arquivo -> marca, nav, contato e rodapé

Uso:
    python3 apply_polish.py            (propaga para todas as páginas)
    python3 apply_polish.py --check    (só relata o que mudaria)
"""

import os
import re
import sys

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
CSS_FILE = os.path.join(ROOT, "design.css")
JS_FILE = os.path.join(ROOT, "newjs.txt")

# ---------------------------------------------------------------------------
# 1. Navegação. Adicione aqui toda página nova.
#    tipo: "link" | "group" | "cta"
#    soon=True mostra o item como "em breve" e sem href (não quebra o QA).
# ---------------------------------------------------------------------------

NAV_NEW = [
    {"tipo": "link", "label": "Início", "href": "index.html"},
    {"tipo": "link", "label": "Ortopedistas", "href": "ortopedistas-em-curitiba.html"},
    {
        "tipo": "group",
        "label": "Por região do corpo",
        "id": "menu-regioes",
        "itens": [
            {"grupo": "Membro inferior"},
            {"label": "Joelho", "href": "ortopedista-joelho-curitiba.html",
             "sub": "Dor, menisco, ligamentos, artrose"},
            {"label": "Quadril", "soon": True, "sub": "Conteúdo no site irmão"},
            {"label": "Pé e tornozelo", "soon": True},
            {"grupo": "Membro superior e coluna"},
            {"label": "Ombro", "href": "ortopedista-ombro-curitiba.html",
             "sub": "Manguito rotador, tendinite, luxação"},
            {"label": "Coluna", "href": "ortopedista-coluna-curitiba.html",
             "sub": "Lombalgia, hérnia de disco, ciática"},
            {"label": "Mão e punho", "soon": True},
            {"grupo": "Outras áreas"},
            {"label": "Ortopedia infantil", "soon": True},
            {"label": "Medicina esportiva", "soon": True},
        ],
    },
    {
        "tipo": "group",
        "label": "Guias",
        "id": "menu-guias",
        "itens": [
            {"label": "Qual médico procurar para cada dor", "href": "qual-medico-procurar-para-cada-dor.html",
             "sub": "Tabela de sintoma por especialidade"},
            {"label": "CRM, RQE e como verificar", "href": "crm-rqe-como-verificar-ortopedista.html",
             "sub": "Confira o registro antes da consulta"},
            {"label": "Sobre o projeto", "href": "sobre.html"},
        ],
    },
    {"tipo": "cta", "label": "Cadastre-se", "href": "cadastre-se.html"},
]

# Colunas de links do rodapé.
FOOTER_TEMAS_NEW = [
    ("Ortopedista em Curitiba", "ortopedistas-em-curitiba.html", False),
    ("Ortopedista de joelho", "ortopedista-joelho-curitiba.html", False),
    ("Ortopedista de coluna", "ortopedista-coluna-curitiba.html", False),
    ("Ortopedista de ombro", "ortopedista-ombro-curitiba.html", False),
    ("Qual médico procurar", "qual-medico-procurar-para-cada-dor.html", False),
    ("CRM, RQE e verificação", "crm-rqe-como-verificar-ortopedista.html", False),
]

FOOTER_SITE_NEW = [
    ("Sobre o projeto", "sobre.html"),
    ("Cadastre-se na lista", "cadastre-se.html"),
    ("Privacidade e LGPD", "privacidade.html"),
]

# ---------------------------------------------------------------------------
# 2. Marca
# ---------------------------------------------------------------------------

MARK_SVG = (
    '<svg class="mark" viewBox="0 0 32 32" role="img" aria-label="Curitiba Ortopedia" '
    'xmlns="http://www.w3.org/2000/svg" focusable="false">'
    '<path d="M24.05 23.02 A10.5 10.5 0 1 1 24.05 8.98" fill="none" stroke="currentColor" '
    'stroke-width="4.2" stroke-linecap="round"/>'
    '<circle cx="26.6" cy="16" r="3.3" fill="#B25E36"/>'
    "</svg>"
)

BRAND_BLOCK = (
    '<a class="brand" href="index.html" aria-label="Curitiba Ortopedia, página inicial">'
    + MARK_SVG
    + '<span class="wordmark"><span class="wm-1">Curitiba Ortopedia</span>'
    '<span class="wm-2">Guia de ortopedistas</span></span></a>'
)

# ---------------------------------------------------------------------------
# 3. Construtores de HTML
# ---------------------------------------------------------------------------


def _item_html(it, mobile=False):
    if "grupo" in it:
        return '<div class="grp">%s</div>' % it["grupo"]
    sub = it.get("sub")
    if it.get("soon"):
        txt = it["label"]
        if mobile:
            return '<a class="soon" aria-disabled="true">%s</a>' % txt
        inner = txt if not sub else "%s<small>%s</small>" % (txt, sub)
        return '<a class="soon" aria-disabled="true">%s</a>' % inner
    inner = it["label"]
    if sub and not mobile:
        inner = "%s<small>%s</small>" % (it["label"], sub)
    return '<a href="%s">%s</a>' % (it["href"], inner)


def build_nav():
    out = ['<nav class="mainnav" aria-label="Navegação principal">']
    for e in NAV_NEW:
        if e["tipo"] == "link":
            out.append('<a class="nav-link" href="%s">%s</a>' % (e["href"], e["label"]))
        elif e["tipo"] == "cta":
            out.append('<a class="nav-link cta" href="%s">%s</a>' % (e["href"], e["label"]))
        else:
            out.append('<div class="nav-group" data-open="false">')
            out.append(
                '<button class="nav-btn" type="button" aria-expanded="false" aria-controls="%s">'
                '%s<span class="chev" aria-hidden="true"></span></button>' % (e["id"], e["label"])
            )
            out.append('<div class="nav-menu" id="%s">' % e["id"])
            for it in e["itens"]:
                out.append(_item_html(it))
            out.append("</div></div>")
    out.append("</nav>")
    return "".join(out)


def build_mobile_panel():
    out = ['<div class="mobile-panel" id="menu-mobile"><div class="inner">']
    for e in NAV_NEW:
        if e["tipo"] == "link":
            out.append('<a href="%s">%s</a>' % (e["href"], e["label"]))
        elif e["tipo"] == "cta":
            out.append('<a class="cta" href="%s">%s</a>' % (e["href"], e["label"]))
        else:
            out.append('<div class="grp">%s</div>' % e["label"])
            for it in e["itens"]:
                if "grupo" in it:
                    continue
                out.append(_item_html(it, mobile=True))
    out.append("</div></div>")
    return "".join(out)


def build_header():
    return (
        '<header class="site-header">'
        '<div class="bar">'
        + BRAND_BLOCK
        + build_nav()
        + '<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="menu-mobile">'
        '<span class="bars" aria-hidden="true"><i></i><i></i><i></i></span>Menu</button>'
        "</div>"
        + build_mobile_panel()
        + "</header>"
    )


CONTACT_BLOCK = (
    '<section class="contact-block reveal" aria-labelledby="contato-titulo">'
    '<h2 id="contato-titulo">Fale com o projeto</h2>'
    "<p>O Curitiba Ortopedia é um projeto informativo independente e gratuito, sem vínculo com "
    "clínicas, hospitais, planos de saúde ou fabricantes. Não realizamos atendimento, não marcamos "
    "consultas e não damos orientação clínica individual por mensagem.</p>"
    "<p>Se você é ortopedista e quer aparecer na lista, se encontrou um erro em alguma página, se "
    "quer sugerir um tema ou se precisa corrigir ou remover os seus dados, escreva para o e-mail "
    "abaixo. Pedidos de correção e de remoção são atendidos sem custo.</p>"
    '<p class="mailrow">'
    '<a class="btn" href="mailto:contato@curitibaortopedia.com.br">contato@curitibaortopedia.com.br</a>'
    '<a class="btn ghost" href="cadastre-se.html">Entrar para a lista</a>'
    "</p>"
    "</section>"
)


def build_footer():
    temas = "".join(
        ('<li><span class="muted">%s</span></li>' % t) if soon else ('<li><a href="%s">%s</a></li>' % (h, t))
        for (t, h, soon) in FOOTER_TEMAS_NEW
    )
    site = "".join('<li><a href="%s">%s</a></li>' % (h, t) for (t, h) in FOOTER_SITE_NEW)
    return (
        '<footer class="site-footer">'
        '<div class="wrap"><div class="cols">'
        '<div><div class="fbrand">' + MARK_SVG + "<span>Curitiba Ortopedia</span></div>"
        "<p>Guia informativo e gratuito sobre ortopedia para pacientes de Curitiba e região "
        "metropolitana, com uma lista de ortopedistas organizada por área de atuação.</p>"
        "<p>Conteúdo educativo, escrito em linguagem de paciente e revisado periodicamente. "
        "Nada aqui substitui a consulta com um médico.</p></div>"
        "<div><h3>Temas</h3><ul>" + temas + "</ul></div>"
        "<div><h3>O projeto</h3><ul>" + site + "</ul></div>"
        "</div>"
        '<div class="legal">'
        "<p>Este site não indica, não classifica e não recomenda um profissional em detrimento de "
        "outro. A lista é publicada em ordem alfabética, apenas com dados fornecidos e autorizados "
        "pelo próprio médico. Cada profissional é o único responsável pela sua publicidade médica "
        "perante o Conselho Federal de Medicina.</p>"
        "<p>© 2026 Curitiba Ortopedia · curitibaortopedia.com.br · Curitiba, Paraná · "
        '<a href="privacidade.html">Privacidade e LGPD</a></p>'
        "</div></div></footer>"
    )


# ---------------------------------------------------------------------------
# 4. Blocos com sentinelas
# ---------------------------------------------------------------------------

def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def wrapped(name, content):
    return "<!--%s:S-->%s<!--%s:E-->" % (name, content, name)


def blocks():
    css = read(CSS_FILE).strip()
    js = read(JS_FILE).strip()
    return {
        "CSS": wrapped("CSS", '\n<style>\n%s\n</style>\n'
                              '<noscript><style>.reveal{opacity:1;transform:none}</style></noscript>\n' % css),
        "JS": wrapped("JS", '\n<script>\n%s\n</script>\n' % js),
        "MARK": wrapped("MARK", MARK_SVG),
        "HEADER": wrapped("HEADER", build_header()),
        "CONTACT": wrapped("CONTACT", CONTACT_BLOCK),
        "FOOTER": wrapped("FOOTER", build_footer()),
    }


def apply_to_html(html, bl):
    for name, block in bl.items():
        pattern = re.compile(r"<!--%s:S-->.*?<!--%s:E-->" % (name, name), re.S)
        html = pattern.sub(lambda m, b=block: b, html)
        html = html.replace("{{%s}}" % name, block)
    return html


def main():
    check = "--check" in sys.argv
    bl = blocks()
    pages = sorted(p for p in os.listdir(SITE) if p.endswith(".html"))
    changed = []
    for name in pages:
        path = os.path.join(SITE, name)
        original = read(path)
        new = apply_to_html(original, bl)
        if new != original:
            changed.append(name)
            if not check:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new)
    # sincroniza os arquivos soltos de referência
    if not check:
        with open(os.path.join(SITE, "styles.css"), "w", encoding="utf-8") as f:
            f.write(read(CSS_FILE))
        with open(os.path.join(SITE, "main.js"), "w", encoding="utf-8") as f:
            f.write(read(JS_FILE))
    verbo = "mudariam" if check else "atualizadas"
    print("%d/%d páginas %s%s" % (len(changed), len(pages), verbo,
                                  (": " + ", ".join(changed)) if changed else ""))
    if not check:
        print("styles.css e main.js sincronizados com design.css e newjs.txt")


if __name__ == "__main__":
    main()
