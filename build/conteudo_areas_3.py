#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ortopedia geral e traumatologia: a área que cuida de tudo."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from page_builder import escrever
from conteudo_areas_1 import alerta, CRUMB

escrever(
    "ortopedia-geral-curitiba.html",
    title="Ortopedista geral em Curitiba: cuida de tudo",
    description="O ortopedista geral trata a maior parte das queixas do aparelho locomotor em Curitiba: dores, tendinites, entorses, fraturas e artrose inicial.",
    h1="Ortopedista geral e traumatologia em Curitiba",
    lead="Se você não sabe qual é a sua área, comece por aqui. Abaixo estão as fichas dos ortopedistas gerais de Curitiba, que resolvem a maior parte das queixas do dia a dia, e depois o guia da área.",
    crumbs=CRUMB,
    lista={"titulo": "Ortopedistas gerais em Curitiba",
           "texto": "Ortopedia e traumatologia é a especialidade completa, com três anos de residência médica depois da faculdade.",
           "area": "Ortopedia geral e traumatologia", "n": 6},
    banda={"titulo": "Prefere procurar pela parte do corpo?",
           "texto": "A busca por área mostra qual ortopedista cuida de cada região, com a página explicando o problema."},
    secoes=[
        {"id": "quem-e", "titulo": "Quem é o ortopedista geral", "html": """
    <p>É o médico que concluiu a residência em ortopedia e traumatologia, três anos depois dos seis de faculdade, e que atua no aparelho locomotor inteiro: ossos, articulações, músculos, tendões, ligamentos, nervos periféricos e as consequências do trauma sobre tudo isso.</p>
    <p>Existe uma confusão comum que vale desfazer de uma vez: <strong>ortopedista geral não é um ortopedista incompleto</strong>. A subespecialidade é uma formação adicional que aprofunda uma região, e ela pesa em casos cirúrgicos complexos. Mas o volume do dia a dia, aquilo que faz a pessoa procurar um médico, é justamente o território do ortopedista geral, e ele foi treinado exatamente para isso, inclusive em plantão de trauma.</p>
    <p>Na prática, para a maior parte das queixas, começar pelo ortopedista geral é mais rápido, mais barato e igualmente correto. E quando o caso pede um subespecialista, é ele quem identifica isso e encaminha, o que evita você adivinhar sozinho e bater na porta errada.</p>
"""},
        {"id": "o-que-trata", "titulo": "O que ele resolve no dia a dia", "html": """
    <div class="table-scroll">
      <table>
        <caption class="sr-only">Queixas atendidas pelo ortopedista geral</caption>
        <thead><tr><th scope="col">Grupo</th><th scope="col">Exemplos frequentes</th></tr></thead>
        <tbody>
          <tr><th scope="row">Trauma</th><td>Fraturas, entorses, luxações, contusões, ferimentos e imobilizações</td></tr>
          <tr><th scope="row">Tendinopatias</th><td>Tendinite do ombro, epicondilite do cotovelo, tendinite do Aquiles, fascite plantar</td></tr>
          <tr><th scope="row">Dores da coluna</th><td>Lombalgia e cervicalgia sem sinais de alarme, com ou sem irradiação leve</td></tr>
          <tr><th scope="row">Artrose inicial</th><td>Joelho, quadril, mãos e coluna, na fase em que o tratamento é conservador</td></tr>
          <tr><th scope="row">Dores por sobrecarga</th><td>Dor femoropatelar, canelite, bursites, dores de quem mudou de rotina de treino</td></tr>
          <tr><th scope="row">Nervos periféricos</th><td>Suspeita de túnel do carpo e outras compressões, com encaminhamento quando necessário</td></tr>
          <tr><th scope="row">Osteoporose</th><td>Investigação após fratura por queda simples e prevenção de novas fraturas</td></tr>
          <tr><th scope="row">Avaliações</th><td>Aptidão para atividade física, laudos, segunda opinião e acompanhamento pós-operatório</td></tr>
        </tbody>
      </table>
    </div>
    <p>Repare em uma coisa: quase nada nessa lista termina em cirurgia. A maior parte se resolve com diagnóstico correto, ajuste de carga, reabilitação e tempo, que é exatamente o que um bom ortopedista geral faz.</p>
"""},
        {"id": "quando-basta", "titulo": "Quando o geral basta e quando encaminhar", "html": """
    <p><strong>O ortopedista geral costuma bastar quando</strong> a queixa é recente, tem relação clara com esforço, treino ou uma torção, quando não há sinal de alarme, quando é a primeira avaliação daquele problema, ou quando o tratamento provável é medicação e fisioterapia.</p>
    <p><strong>A subespecialidade passa a pesar em três situações</strong>, e um bom ortopedista geral identifica todas elas:</p>
    <ol class="steps">
      <li><b>Quando o caso é cirúrgico</b><span>Cirurgias de ligamento, artroplastias, artroscopias e cirurgias de coluna têm curva de aprendizado longa, e volume faz diferença no resultado.</span></li>
      <li><b>Quando o problema se arrasta</b><span>Se você já fez fisioterapia, já tomou medicação e já esperou de três a seis meses sem melhora, existe algo fora do óbvio.</span></li>
      <li><b>Quando o diagnóstico não fecha</b><span>Dor no ombro que vem do pescoço, dor no joelho que vem do quadril, dor no pé que é neurológica. Quem olha aquela região o dia inteiro conhece as armadilhas.</span></li>
    </ol>
    <p>Se você quiser ir direto ao subespecialista, use a <a href="encontre-um-ortopedista.html">busca por área</a>. Se estiver em dúvida, comece pelo geral: perder tempo procurando o especialista perfeito costuma custar mais do que uma primeira consulta bem feita.</p>
"""},
        {"id": "trauma", "titulo": "A parte de traumatologia", "html": """
    <p>O nome completo da especialidade é ortopedia e traumatologia, e a segunda metade explica boa parte da rotina. Traumatologia cuida do que acontece depois de uma queda, de um acidente, de um choque no esporte ou de um tombo em casa.</p>
    <p>Alguns pontos práticos que evitam erro:</p>
    <ul>
      <li><strong>Nem toda dor após trauma precisa de radiografia</strong>, mas algumas situações precisam sempre: impossibilidade de apoiar o peso, deformidade, dor sobre pontos ósseos específicos e trauma de alta energia.</li>
      <li><strong>Gesso ou imobilização não é tratamento neutro.</strong> Imobilizar demais gera rigidez e perda de músculo, e por isso a tendência atual é imobilizar o necessário e mobilizar o quanto antes for seguro.</li>
      <li><strong>Fratura em pessoa acima de 50 anos, após queda da própria altura, é um alerta de osteoporose</strong> e merece investigação, porque a próxima fratura costuma ser pior.</li>
      <li><strong>Inchaço que aparece em minutos</strong> depois de uma torção sugere sangue dentro da articulação e merece avaliação rápida.</li>
    </ul>
"""},
        {"id": "consulta", "titulo": "Como é a consulta", "html": """
    <p>Conversa, exame físico e, quando necessário, exame de imagem, nessa ordem. A conversa é a parte mais longa e a que mais fecha diagnóstico. O exame físico inclui a região vizinha, porque dores referidas são comuns. A imagem entra depois da hipótese, e não antes dela.</p>
    <p>O guia <a href="primeira-consulta-ortopedista.html">primeira consulta com o ortopedista</a> traz a lista do que levar, como descrever a dor em trinta segundos e sete perguntas que valem a consulta. Vale ler antes de ir, porque consulta bem aproveitada economiza retorno.</p>
    <div class="callout info">
      <h3>Uma dica que vale para qualquer área</h3>
      <p>Leve os exames antigos, mesmo os que você acha irrelevantes. Uma radiografia de três anos atrás mostrando o mesmo joelho é uma informação que nenhum exame novo entrega: ela mostra a velocidade da mudança.</p>
    </div>
"""},
        {"id": "quando-procurar", "titulo": "Quando procurar", "html": """
    <p>Marque consulta quando a dor dura mais de quatro a seis semanas, quando ela limita o que você precisa fazer, quando existe inchaço recorrente, quando a articulação trava ou falseia, quando houve trauma e a dor não melhora, ou simplesmente quando você não sabe a quem recorrer e precisa de uma avaliação inicial confiável.</p>
""" + alerta("Procure pronto atendimento sem esperar se houver", [
            "Deformidade do membro, osso exposto ou incapacidade de apoiar o peso depois de trauma.",
            "Articulação quente, vermelha e muito dolorida, com febre ou inchaço em poucas horas.",
            "Perda de força progressiva, dormência em sela, ou perda de controle da urina ou das fezes.",
            "Membro frio, pálido ou roxo, com ou sem dormência.",
            "Dor forte que aparece à noite, não alivia com repouso, com perda de peso ou história de câncer.",
            "Criança que se recusa a andar, principalmente com febre."])},
    ],
    faq=[
        ("Ortopedista geral é menos qualificado que o subespecialista?",
         "Não. O ortopedista geral concluiu a residência completa em ortopedia e traumatologia e foi treinado no aparelho locomotor inteiro, incluindo trauma. A subespecialidade é uma formação adicional que aprofunda uma região e pesa principalmente em casos cirúrgicos complexos. Para a maior parte das queixas do dia a dia, o ortopedista geral resolve muito bem e encaminha quando o caso pede."),
        ("Devo procurar o ortopedista geral ou já ir direto ao especialista da região?",
         "Se o seu caso é recente, tem relação clara com esforço ou torção e não tem sinais de alarme, começar pelo ortopedista geral costuma ser mais rápido e mais barato. Vá direto ao subespecialista quando o caso já é cirúrgico, quando o problema se arrasta há meses sem melhora ou quando o diagnóstico ficou indefinido em uma avaliação anterior."),
        ("O ortopedista geral trata fratura?",
         "Trata, e essa é uma parte central da formação dele, já que a especialidade se chama ortopedia e traumatologia. Fraturas simples são conduzidas com imobilização e acompanhamento, e fraturas complexas ou com desvio importante podem ser encaminhadas conforme a região e a necessidade cirúrgica. Trauma agudo, no entanto, deve ser atendido na urgência, e não em consulta eletiva."),
        ("Ortopedista geral pede ressonância?",
         "Pede quando o resultado pode mudar a conduta. O exame inicial da maior parte dos problemas ósseos e articulares é a radiografia, muitas vezes com carga. Ressonância entra em suspeitas específicas de lesão de partes moles, quando se cogita cirurgia ou quando o quadro não melhora como esperado. Pedir imagem sem hipótese clínica costuma gerar achados que confundem."),
        ("Quanto tempo até melhorar de uma dor tratada pelo ortopedista geral?",
         "Depende do problema, mas alguns prazos ajudam a calibrar expectativa: entorses leves melhoram em semanas, tendinopatias respondem a fortalecimento em cerca de três meses, e lombalgia aguda melhora bastante em quatro a seis semanas quando a pessoa se mantém ativa. Melhora que não vem dentro do prazo esperado é motivo para reavaliar, e não para insistir no mesmo tratamento."),
    ],
    takeaways=[
        "Ortopedista geral é o especialista completo do aparelho locomotor, e resolve a maior parte das queixas.",
        "A subespecialidade pesa no caso cirúrgico, no caso arrastado e no diagnóstico indefinido.",
        "Quase nada do que o ortopedista geral trata no dia a dia termina em cirurgia.",
        "Imobilizar demais gera rigidez, e a tendência atual é mobilizar assim que for seguro.",
        "Fratura por queda simples depois dos 50 anos é um alerta de osteoporose.",
        "Trauma agudo é caso de urgência, não de consulta eletiva.",
        "Levar exames antigos mostra a velocidade da mudança, coisa que exame novo não mostra.",
    ],
    refs=[
        "Sociedade Brasileira de Ortopedia e Traumatologia. Formação em ortopedia e traumatologia e áreas de atuação. sbot.org.br.",
        "Conselho Federal de Medicina. Registro de qualificação de especialista e áreas de atuação.",
        "National Institute for Health and Care Excellence. Low back pain and sciatica in over 16s, NG59.",
        "Bannuru RR et al. OARSI guidelines for the non-surgical management of knee, hip, and polyarticular osteoarthritis. Osteoarthritis and Cartilage, 2019.",
        "Stiell IG et al. Decision rules for the use of radiography in acute ankle injuries. JAMA, 1993.",
        "Compston J et al. Osteoporosis. The Lancet, 2019.",
    ],
)

print("página gerada: ortopedia geral")
