#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
qa.py — verificação obrigatória antes de qualquer entrega do curitibaortopedia.

Falha quando:
  1. sobrar marcador {{...}} não substituído
  2. houver id duplicado na página
  3. houver link ou src interno para arquivo inexistente
  4. houver âncora #alguma-coisa sem elemento correspondente (na página ou na página alvo)
  5. algum bloco JSON-LD for inválido
  6. alguma imagem estiver sem alt, ou SVG de figura sem aria-labelledby e role
  7. a nav estiver ausente ou duplicada
  8. o canonical divergir do nome do arquivo
  9. a página estiver fora do sitemap
 10. o bloco de contato estiver ausente
 11. o title passar de 65 caracteres ou a description passar de 160
 12. faltar BreadcrumbList ou dateModified no JSON-LD
 13. houver mais de um h1 ou nenhum
 14. o FAQPage não espelhar exatamente as perguntas visíveis

Uso: python3 qa.py
"""

import html
import json
import os
import re
import sys
from html.parser import HTMLParser

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

erros = []
avisos = []


def erro(pagina, msg):
    erros.append("%s: %s" % (pagina, msg))


def aviso(pagina, msg):
    avisos.append("%s: %s" % (pagina, msg))


class Pagina(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []           # href
        self.srcs = []            # src
        self.h1 = 0
        self.navs_main = 0
        self.headers = 0
        self.title = None
        self.description = None
        self.canonical = None
        self.imgs_sem_alt = 0
        self.jsonld = []
        self.faq_perguntas = []
        self.tem_contato = False
        self.svgs_figura = []     # (tem_role, tem_labelledby)
        self._pilha = []
        self._captura = None
        self._buffer = []
        self._em_style_script = None
        self._svg_attrs = None
        self._svg_depth = 0

    # --- utilidades ---
    def _classes(self, attrs):
        d = dict(attrs)
        return (d.get("class") or "").split(), d

    def handle_starttag(self, tag, attrs):
        classes, d = self._classes(attrs)
        self._pilha.append((tag, classes))

        if tag in ("style", "script") and not d.get("type", "").endswith("ld+json"):
            self._em_style_script = tag
        if d.get("id"):
            self.ids.append(d["id"])
        if tag == "a" and d.get("href"):
            self.links.append(d["href"])
        if tag in ("img", "source", "iframe") and d.get("src"):
            self.srcs.append(d["src"])
        if tag == "link" and d.get("href"):
            if d.get("rel") == "canonical":
                self.canonical = d["href"]
            elif d.get("rel") in ("icon", "apple-touch-icon", "stylesheet"):
                self.srcs.append(d["href"])
        if tag == "img" and not d.get("alt"):
            self.imgs_sem_alt += 1
        if tag == "h1":
            self.h1 += 1
        if tag == "nav" and "mainnav" in classes:
            self.navs_main += 1
        if tag == "header" and "site-header" in classes:
            self.headers += 1
        if tag == "section" and "contact-block" in classes:
            self.tem_contato = True
        if tag == "meta":
            if d.get("name") == "description":
                self.description = d.get("content", "")
        if tag == "script" and d.get("type") == "application/ld+json":
            self._captura = "jsonld"
            self._buffer = []
        if tag == "title":
            self._captura = "title"
            self._buffer = []
        if tag == "summary" and self._dentro_de("faq"):
            self._captura = "summary"
            self._buffer = []
        if tag == "svg":
            if self._svg_depth == 0 and self._dentro_de_tag("figure"):
                self._svg_attrs = d
            self._svg_depth += 1

    def _dentro_de(self, classe):
        return any(classe in cs for (_, cs) in self._pilha)

    def _dentro_de_tag(self, tag):
        return any(t == tag for (t, _) in self._pilha)

    def handle_endtag(self, tag):
        if self._captura and tag in ("script", "title", "summary"):
            texto = "".join(self._buffer)
            if self._captura == "jsonld":
                self.jsonld.append(texto)
            elif self._captura == "title":
                self.title = texto.strip()
            elif self._captura == "summary":
                self.faq_perguntas.append(" ".join(texto.split()))
            self._captura = None
            self._buffer = []
        if tag in ("style", "script"):
            self._em_style_script = None
        if tag == "svg":
            self._svg_depth -= 1
            if self._svg_depth == 0 and self._svg_attrs is not None:
                self.svgs_figura.append(self._svg_attrs)
                self._svg_attrs = None
        for i in range(len(self._pilha) - 1, -1, -1):
            if self._pilha[i][0] == tag:
                del self._pilha[i:]
                break

    def handle_data(self, data):
        if self._captura:
            self._buffer.append(data)


def coletar_ids(caminho):
    p = Pagina()
    with open(caminho, "r", encoding="utf-8") as f:
        p.feed(f.read())
    return p


def main():
    paginas = sorted(x for x in os.listdir(SITE) if x.endswith(".html"))
    arquivos = set(os.listdir(SITE))
    analisadas = {}

    for nome in paginas:
        analisadas[nome] = coletar_ids(os.path.join(SITE, nome))

    # sitemap
    sitemap_path = os.path.join(SITE, "sitemap.xml")
    sitemap_locs = set()
    if not os.path.exists(sitemap_path):
        erros.append("sitemap.xml: arquivo ausente")
    else:
        with open(sitemap_path, "r", encoding="utf-8") as f:
            sitemap_locs = set(re.findall(r"<loc>(.*?)</loc>", f.read()))

    for nome, p in analisadas.items():
        bruto = open(os.path.join(SITE, nome), "r", encoding="utf-8").read()

        # 1. marcadores
        for m in set(re.findall(r"\{\{[A-Z_]+\}\}", bruto)):
            erro(nome, "marcador não substituído %s" % m)

        # 2. ids duplicados
        vistos, dup = set(), set()
        for i in p.ids:
            if i in vistos:
                dup.add(i)
            vistos.add(i)
        for i in sorted(dup):
            erro(nome, "id duplicado: %s" % i)

        # 3. links e src internos
        alvos = [l for l in p.links + p.srcs
                 if not l.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:", "//"))]
        for alvo in alvos:
            arquivo = alvo.split("#")[0].split("?")[0]
            if arquivo and arquivo not in arquivos:
                erro(nome, "link interno inexistente: %s" % alvo)

        # 4. âncoras
        for l in p.links:
            if l.startswith("#"):
                if l[1:] and l[1:] not in p.ids:
                    erro(nome, "âncora sem destino: %s" % l)
            elif "#" in l and not l.startswith(("http", "mailto:", "tel:")):
                arquivo, anc = l.split("#", 1)
                if arquivo in analisadas and anc not in analisadas[arquivo].ids:
                    erro(nome, "âncora sem destino em %s: #%s" % (arquivo, anc))

        # 5. JSON-LD válido
        blocos = []
        for bloco in p.jsonld:
            try:
                blocos.append(json.loads(bloco))
            except Exception as e:
                erro(nome, "JSON-LD inválido: %s" % e)

        # 6. imagens e svg
        if p.imgs_sem_alt:
            erro(nome, "%d imagem(ns) sem alt" % p.imgs_sem_alt)
        for attrs in p.svgs_figura:
            if attrs.get("role") != "img" or not attrs.get("aria-labelledby"):
                erro(nome, "SVG de figura sem role=img e aria-labelledby")
            else:
                for ref in attrs["aria-labelledby"].split():
                    if ref not in p.ids:
                        erro(nome, "aria-labelledby aponta para id inexistente: %s" % ref)

        # 7. nav
        if p.navs_main != 1:
            erro(nome, "nav principal ausente ou duplicada (%d)" % p.navs_main)
        if p.headers != 1:
            erro(nome, "cabeçalho ausente ou duplicado (%d)" % p.headers)

        # 8. canonical
        esperado = BASE if nome == "index.html" else BASE + nome
        if p.canonical != esperado:
            erro(nome, "canonical divergente: %s (esperado %s)" % (p.canonical, esperado))

        # 9. sitemap
        if esperado not in sitemap_locs:
            erro(nome, "página fora do sitemap")

        # 10. contato
        if not p.tem_contato:
            erro(nome, "bloco de contato ausente")

        # 11. title e description
        if not p.title:
            erro(nome, "title ausente")
        elif len(p.title) > 65:
            erro(nome, "title com %d caracteres (máximo 65)" % len(p.title))
        if not p.description:
            erro(nome, "meta description ausente")
        elif len(p.description) > 160:
            erro(nome, "description com %d caracteres (máximo 160)" % len(p.description))

        # 12. BreadcrumbList e dateModified
        texto_ld = json.dumps(blocos, ensure_ascii=False)
        if '"BreadcrumbList"' not in texto_ld:
            erro(nome, "sem BreadcrumbList no JSON-LD")
        if '"dateModified"' not in texto_ld:
            erro(nome, "sem dateModified no JSON-LD")

        # 13. h1
        if p.h1 != 1:
            erro(nome, "%d elementos h1 (esperado exatamente 1)" % p.h1)

        # 14. FAQ espelhado
        faq_schema = []
        for bloco in blocos:
            nos = bloco.get("@graph", [bloco]) if isinstance(bloco, dict) else []
            for no in nos:
                if isinstance(no, dict) and no.get("@type") == "FAQPage":
                    for q in no.get("mainEntity", []):
                        faq_schema.append(" ".join(q.get("name", "").split()))
        if p.faq_perguntas or faq_schema:
            if p.faq_perguntas != faq_schema:
                erro(nome, "FAQPage não espelha as perguntas visíveis")
                for a, b in zip(p.faq_perguntas, faq_schema):
                    if a != b:
                        erro(nome, "  visível: %s" % a)
                        erro(nome, "  schema : %s" % b)
                if len(p.faq_perguntas) != len(faq_schema):
                    erro(nome, "  contagem: %d visíveis contra %d no schema"
                         % (len(p.faq_perguntas), len(faq_schema)))

        # extras informativos
        if "revdate" not in bruto:
            aviso(nome, "sem data de revisão visível")

    # arquivos obrigatórios
    for obrigatorio in ("CNAME", ".nojekyll", "robots.txt", "sitemap.xml",
                        "favicon.ico", "favicon.svg", "og-image.png",
                        "styles.css", "main.js"):
        if obrigatorio not in arquivos:
            erros.append("repositório: arquivo obrigatório ausente: %s" % obrigatorio)

    # relatório
    print("Páginas verificadas: %d" % len(paginas))
    if avisos:
        print("\nAvisos:")
        for a in avisos:
            print("  - " + a)
    if erros:
        print("\nERROS (%d):" % len(erros))
        for e in erros:
            print("  - " + e)
        print("\nQA reprovado.")
        sys.exit(1)
    print("\nTudo certo.")


if __name__ == "__main__":
    main()
