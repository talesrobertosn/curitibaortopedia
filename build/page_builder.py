#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
page_builder.py — gera uma página completa a partir do conteúdo.

Cuida sozinho de: head, Open Graph, favicon, blocos JSON-LD (página, breadcrumb
e FAQ), hero, índice navegável, corpo, FAQ visível, takeaways, referências e
marcadores {{CSS}} {{HEADER}} {{CONTACT}} {{FOOTER}} {{JS}}.

O FAQPage é gerado a partir da mesma lista que desenha a FAQ visível, então é
impossível os dois divergirem. Essa era a lição número 4 do site irmão.
"""

import html
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))


def _resolver_site(root):
    cand = os.path.join(root, "site")
    if os.path.isdir(cand):
        return cand
    pai = os.path.dirname(root)
    if os.path.exists(os.path.join(pai, "index.html")):
        return pai
    return root


SITE = _resolver_site(ROOT)
BASE = "https://curitibaortopedia.com.br/"
DATA = "2026-08-17"
DATA_EXTENSO = "17 de agosto de 2026"

ICONE_PESSOA = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
                'stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="8.5" r="4"/>'
                '<path d="M4.5 20.5c1.6-3.6 4.3-5.4 7.5-5.4s5.9 1.8 7.5 5.4"/></svg>')

ICONES_VITRINE = {
    "registro": '<circle cx="12" cy="12" r="9"/><path d="M8.5 12.5l2.4 2.4 4.6-5"/>',
    "local": '<path d="M12 21s7-5.6 7-11a7 7 0 1 0-14 0c0 5.4 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/>',
    "convenio": '<path d="M4 7h16v11H4z"/><path d="M4 11h16"/><path d="M8 15h4"/>',
    "contato": '<path d="M6.5 4.5h3l1.5 4-2 1.4a12 12 0 0 0 5.1 5.1l1.4-2 4 1.5v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 4.5 6.7 2 2 0 0 1 6.5 4.5z"/>',
}


def _linha(icone, rotulo, largura):
    return (
        '        <div class="vlinha">'
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>'
        '<div><span class="vrotulo">%s</span><span class="vbarra %s"></span></div>'
        "</div>" % (ICONES_VITRINE[icone], rotulo, largura)
    )


def vitrine(area="Ortopedia geral e traumatologia", n=6, titulo=None, intro=None, rodape=True):
    """Grade de fichas de ortopedista ainda sem nome, prontas para serem preenchidas."""
    cartoes = []
    for i in range(n):
        cartoes.append(
            '      <li class="vcard">\n'
            '        <div class="vtopo">\n'
            '          <span class="vfoto" aria-hidden="true">%s</span>\n'
            "          <div>\n"
            '            <h3 class="vnome">Ficha disponível</h3>\n'
            '            <p class="vesp">%s</p>\n'
            '            <span class="vtag">Aguardando cadastro</span>\n'
            "          </div>\n"
            "        </div>\n"
            '        <div class="vdados">\n'
            "%s\n%s\n%s\n%s\n"
            "        </div>\n"
            '        <div class="vfoot">\n'
            '          <a class="btn accent" href="cadastre-se.html">É ortopedista? Apareça aqui</a>\n'
            '          <p class="vnota"><strong>100%% gratuito</strong>, sem ranking e sem cobrança</p>\n'
            "        </div>\n"
            "      </li>" % (
                ICONE_PESSOA, area,
                _linha("registro", "Nome, CRM e RQE", "media"),
                _linha("local", "Endereço de atendimento", ""),
                _linha("convenio", "Convênios aceitos", "curta"),
                _linha("contato", "Telefone ou site do consultório", "media"),
            )
        )
    intro = intro or (
        "Estas fichas serão preenchidas com os profissionais de %s que autorizarem a publicação. "
        "Aparecer aqui é <strong>totalmente gratuito</strong>, em ordem alfabética, sem nota, sem estrela "
        "e sem posição paga." % area.lower()
    )
    fim = (
        '  <p class="vitrine-rodape">A lista está em formação e é publicada em ordem alfabética, apenas com '
        "dados fornecidos e autorizados pelo próprio médico. Não há cobrança de nenhum tipo, não há destaque "
        "comprado e não existe classificação por qualidade. Cada profissional é o único responsável pela sua "
        "publicidade médica perante o Conselho Federal de Medicina, e a presença nesta lista não constitui "
        "recomendação ou aval de qualidade por parte deste site.</p>\n" if rodape else ""
    )
    return (
        '  <p class="vitrine-intro">%s</p>\n'
        '  <ul class="vitrine">\n%s\n  </ul>\n%s' % (intro, "\n".join(cartoes), fim)
    )


SELO_GRATIS = ('<span class="selo-gratis"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
               'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
               '<path d="M4 12.5l5.5 5.5L20 6.5"/></svg>Cadastro 100% gratuito</span>')

FAIXA_GRATIS = """  <div class="faixa-gratis">
    <p><strong>Para o médico, aparecer aqui é totalmente gratuito, sempre.</strong> Não existe plano pago, não existe destaque comprado, não cobramos comissão por consulta e não vamos cobrar no futuro. O projeto é informativo e sem fins comerciais.</p>
    <a class="btn accent" href="cadastre-se.html">Quero minha ficha</a>
  </div>
"""


def bloco_vitrine(titulo, area, n=3, intro=None, id_secao="lista", rodape=True, faixa=True):
    """Seção completa da vitrine, já centralizada e com o selo de gratuidade."""
    return (
        '\n<section class="wrap vitrine-bloco" id="%s" aria-labelledby="%s-titulo">\n'
        '  <div class="vitrine-topo">\n'
        '    <h2 id="%s-titulo">%s</h2>\n'
        "    %s\n"
        "  </div>\n"
        "%s"
        "%s"
        "</section>\n" % (id_secao, id_secao, id_secao, titulo, SELO_GRATIS,
                          vitrine(area=area, n=n, intro=intro, rodape=rodape),
                          FAIXA_GRATIS if faixa else "")
    )


def ficha(nome, registro, area, endereco, contato, convenios, site=None, subtitulo=None):
    """Ficha de um profissional real, para substituir uma das fichas em branco.

    Use apenas com dados autorizados por escrito pelo próprio médico, e confira
    o registro na consulta pública do CFM antes de publicar. A ordem da lista é
    alfabética, e nenhuma ficha recebe destaque sobre outra.
    """
    iniciais = "".join(parte[0] for parte in nome.replace("Dr. ", "").replace("Dra. ", "").split()[:2]).upper()
    link = ('<a class="btn ghost" href="%s" rel="noopener nofollow">Site do consultório</a>' % site) if site else ""
    return (
        '      <li class="vcard preenchida">\n'
        '        <div class="vtopo">\n'
        '          <span class="vfoto preenchida" aria-hidden="true">%s</span>\n'
        "          <div>\n"
        '            <h3 class="vnome">%s</h3>\n'
        '            <p class="vesp">%s</p>\n'
        '            <span class="vtag registro">%s</span>\n'
        "          </div>\n"
        "        </div>\n"
        '        <dl class="vficha">\n'
        "          <dt>Atende</dt><dd>%s</dd>\n"
        "          <dt>Contato</dt><dd>%s</dd>\n"
        "          <dt>Convênios</dt><dd>%s</dd>\n"
        "        </dl>\n"
        '        <div class="vfoot">%s\n'
        '          <p class="vnota">Dados fornecidos e autorizados pelo próprio profissional</p>\n'
        "        </div>\n"
        "      </li>" % (iniciais, nome, subtitulo or area, registro, endereco, contato, convenios, link)
    )


LISTA_TEMPLATE = """
    <div class="doc-empty reveal">
      <h3>Lista em formação</h3>
      <p>%(texto)s Os profissionais que autorizarem a publicação aparecem aqui, em ordem alfabética, com CRM, RQE, endereços de atendimento e convênios aceitos.</p>
      <p class="mailrow"><a class="btn ghost" href="cadastre-se.html">Sou ortopedista e quero me cadastrar</a></p>
      <p class="doc-note">Esta lista não classifica, não compara e não recomenda profissionais. Cada médico é o único responsável pela sua publicidade perante o Conselho Federal de Medicina.</p>
    </div>
"""

BANDA_CTA = """
    <div class="cta-band reveal">
      <div>
        <h2>%(titulo)s</h2>
        <p>%(texto)s</p>
      </div>
      <a class="btn lg" href="encontre-um-ortopedista.html">Buscar ortopedista por área</a>
    </div>
"""


def gerar(slug, title, description, h1, lead, secoes, faq, takeaways, refs,
          pill="Área de atuação", crumbs=None, tipo="MedicalWebPage",
          lista=None, banda=None, og_desc=None, data=DATA):
    """Devolve o HTML completo da página, ainda com os marcadores por substituir."""
    if len(title) > 65:
        raise ValueError("title com %d caracteres em %s" % (len(title), slug))
    if len(description) > 160:
        raise ValueError("description com %d caracteres em %s" % (len(description), slug))

    url = BASE + slug
    crumbs = crumbs or []
    trilha = [("Início", "index.html")] + crumbs

    # --- JSON-LD -----------------------------------------------------------
    breadcrumb = []
    for i, (nome, href) in enumerate(trilha, start=1):
        item = BASE if href == "index.html" else BASE + href
        breadcrumb.append({"@type": "ListItem", "position": i, "name": nome, "item": item})
    breadcrumb.append({"@type": "ListItem", "position": len(trilha) + 1,
                       "name": h1, "item": url})

    grafo = [
        {
            "@type": tipo,
            "@id": url + "#webpage",
            "url": url,
            "name": title,
            "description": description,
            "inLanguage": "pt-BR",
            "dateModified": data,
            "isPartOf": {"@id": BASE + "#website"},
            "publisher": {"@type": "Organization", "name": "Curitiba Ortopedia", "url": BASE},
        },
        {
            "@type": "BreadcrumbList",
            "@id": url + "#breadcrumb",
            "itemListElement": breadcrumb,
        },
    ]
    if tipo == "MedicalWebPage":
        grafo[0]["about"] = {"@type": "MedicalSpecialty", "name": "Ortopedia e Traumatologia"}
        grafo[0]["audience"] = {"@type": "Patient"}
    if faq:
        grafo.append({
            "@type": "FAQPage",
            "@id": url + "#faq",
            "inLanguage": "pt-BR",
            "mainEntity": [
                {"@type": "Question", "name": p,
                 "acceptedAnswer": {"@type": "Answer", "text": r}}
                for (p, r) in faq
            ],
        })
    jsonld = json.dumps({"@context": "https://schema.org", "@graph": grafo},
                        ensure_ascii=False, indent=2)

    # --- trilha visível ----------------------------------------------------
    crumb_html = []
    for nome, href in trilha:
        crumb_html.append('<a href="%s">%s</a><span aria-hidden="true">/</span>' % (href, nome))
    crumb_html.append("<span>%s</span>" % (crumbs[-1][0] if crumbs else h1))
    crumb_html = "\n      ".join(crumb_html)

    # --- índice ------------------------------------------------------------
    itens_toc = []
    if lista:
        itens_toc.append(("lista", lista["titulo"]))
    itens_toc += [(s["id"], s["titulo"]) for s in secoes]
    if faq:
        itens_toc.append(("perguntas", "Perguntas frequentes"))
    toc = "\n      ".join('<li><a href="#%s">%s</a></li>' % (i, t) for (i, t) in itens_toc)

    # --- corpo -------------------------------------------------------------
    corpo = []
    for s in secoes:
        corpo.append('    <h2 id="%s">%s</h2>' % (s["id"], s["titulo"]))
        corpo.append(s["html"].rstrip())
    bloco_lista = ""
    if lista:
        intro = lista.get("intro")
        if not intro:
            intro = ("%s As fichas abaixo aguardam cadastro e serão preenchidas com os profissionais que "
                     "autorizarem a publicação. Aparecer aqui é <strong>totalmente gratuito</strong>, "
                     "em ordem alfabética, sem nota e sem posição paga." % lista.get("texto", ""))
        bloco_lista = bloco_vitrine(lista["titulo"], lista.get("area", "Ortopedia e traumatologia"),
                                    n=lista.get("n", 3), intro=intro.strip())
    if banda:
        corpo.append(BANDA_CTA % banda)
    if faq:
        corpo.append('    <h2 id="perguntas">Perguntas frequentes</h2>')
        corpo.append('    <div class="faq">')
        for p, r in faq:
            corpo.append(
                '      <details>\n'
                '        <summary>%s</summary>\n'
                '        <div class="answer"><p>%s</p></div>\n'
                '      </details>' % (p, r)
            )
        corpo.append("    </div>")
    if takeaways:
        corpo.append('    <div class="takeaways reveal">\n      <h2>Para levar daqui</h2>\n      <ul>')
        for t in takeaways:
            corpo.append("        <li>%s</li>" % t)
        corpo.append("      </ul>\n    </div>")
    if refs:
        corpo.append('    <div class="refs">\n      <h2>Referências</h2>\n      <ol>')
        for r in refs:
            corpo.append("        <li>%s</li>" % r)
        corpo.append("      </ol>\n    </div>")
    corpo = "\n\n".join(corpo)

    og = og_desc or description

    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(description)s">
<link rel="canonical" href="%(url)s">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta property="og:type" content="article">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Curitiba Ortopedia">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(og)s">
<meta property="og:url" content="%(url)s">
<meta property="og:image" content="%(base)sog-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#22384E">
<link rel="icon" href="favicon.ico" sizes="32x32">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,600;6..72,700&family=Public+Sans:wght@400;500;600;700&display=swap">
{{CSS}}
<script type="application/ld+json">
%(jsonld)s
</script>
</head>
<body>
<div class="readbar" aria-hidden="true"></div>
<a class="skip" href="#conteudo">Ir para o conteúdo</a>
{{HEADER}}
<main id="conteudo">

<section class="hero">
  <div class="wrap read">
    <nav class="crumbs" aria-label="Trilha de navegação">
      %(crumbs)s
    </nav>
    <p class="pill">%(pill)s</p>
    <h1>%(h1)s</h1>
    <p class="lead">%(lead)s</p>
    <p class="revdate">Última revisão: %(data_extenso)s</p>
  </div>
</section>
%(bloco_lista)s
<div class="wrap read">
  <nav class="toc" aria-label="Índice da página">
    <h2>Nesta página</h2>
    <ol>
      %(toc)s
    </ol>
  </nav>

  <div class="prose">

%(corpo)s

    {{CONTACT}}
  </div>
</div>

</main>
{{FOOTER}}
{{JS}}
</body>
</html>
""" % {
        "title": html.escape(title, quote=True),
        "description": html.escape(description, quote=True),
        "og": html.escape(og, quote=True),
        "url": url,
        "base": BASE,
        "jsonld": jsonld,
        "crumbs": crumb_html,
        "pill": pill,
        "h1": h1,
        "lead": lead,
        "data_extenso": DATA_EXTENSO,
        "toc": toc,
        "corpo": corpo,
        "bloco_lista": bloco_lista,
    }


def escrever(slug, **kwargs):
    caminho = os.path.join(SITE, slug)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(gerar(slug, **kwargs))
    return caminho
