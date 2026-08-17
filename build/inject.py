#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
inject.py — injeta os blocos compartilhados numa página nova.

Uso:
    python3 inject.py site/nova-pagina.html [outra-pagina.html ...]

Substitui os marcadores {{CSS}}, {{JS}}, {{MARK}}, {{HEADER}}, {{CONTACT}} e
{{FOOTER}} pelos blocos definidos em apply_polish.py, já envolvidos pelas
sentinelas que permitem a propagação posterior.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from apply_polish import blocks, apply_to_html  # noqa: E402


def main():
    alvos = sys.argv[1:]
    if not alvos:
        print("uso: python3 inject.py site/pagina.html")
        raise SystemExit(1)
    bl = blocks()
    for alvo in alvos:
        with open(alvo, "r", encoding="utf-8") as f:
            html = f.read()
        novo = apply_to_html(html, bl)
        with open(alvo, "w", encoding="utf-8") as f:
            f.write(novo)
        restantes = [m for m in ("{{CSS}}", "{{JS}}", "{{MARK}}", "{{HEADER}}",
                                 "{{CONTACT}}", "{{FOOTER}}") if m in novo]
        print("%s injetado%s" % (alvo, "" if not restantes else " (sobrou: %s)" % restantes))


if __name__ == "__main__":
    main()
