#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conteúdo das páginas de mão e punho, pé e tornozelo, e quadril."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from page_builder import escrever

CRUMB = [("Ortopedistas em Curitiba", "ortopedistas-em-curitiba.html")]

ALERTA_GERAL = """
    <div class="callout alert">
      <h3>%(titulo)s</h3>
      <ul>
%(itens)s
      </ul>
      <p>Nesses casos, procure um pronto atendimento. Em emergência, ligue 192.</p>
    </div>
"""


def alerta(titulo, itens):
    return ALERTA_GERAL % {"titulo": titulo,
                           "itens": "\n".join("        <li>%s</li>" % i for i in itens)}


# ---------------------------------------------------------------------------
# Mão e punho
# ---------------------------------------------------------------------------
escrever(
    "ortopedista-mao-curitiba.html",
    title="Ortopedista de mão em Curitiba: quando procurar",
    description="Cirurgia da mão em Curitiba: túnel do carpo, dedo em gatilho, De Quervain, rizartrose e fraturas do punho, com o que funciona em cada caso.",
    h1="Ortopedista de mão e punho em Curitiba",
    lead="Aqui estão as fichas dos cirurgiões de mão e punho de Curitiba. Logo abaixo delas vem o guia da área: o que cada padrão de formigamento significa, o que melhora sem cirurgia e o que não pode esperar.",
    crumbs=CRUMB,
    lista={"titulo": "Ortopedistas de mão em Curitiba",
           "texto": "Cirurgia da mão é uma área de atuação com formação específica depois da residência em ortopedia.", "area": "Cirurgia da mão e do punho", "n": 3},
    banda={"titulo": "Não é isso que você está sentindo?",
           "texto": "A busca por área encontra o especialista certo a partir da parte do corpo que dói."},
    secoes=[
        {"id": "o-que-trata", "titulo": "O que o cirurgião de mão trata", "html": """
    <p>A cirurgia da mão cuida da mão, do punho, do antebraço e dos nervos periféricos do membro superior. É uma das áreas mais cirúrgicas da ortopedia e também uma das que mais resolvem com procedimentos pequenos, feitos com anestesia local, em poucos minutos.</p>
    <ul>
      <li><strong>Compressões de nervo</strong>, principalmente a síndrome do túnel do carpo e a compressão do nervo ulnar no cotovelo.</li>
      <li><strong>Tendinopatias</strong>, como o dedo em gatilho e a tenossinovite de De Quervain.</li>
      <li><strong>Artroses da mão</strong>, com destaque para a rizartrose, na base do polegar.</li>
      <li><strong>Cistos e tumores benignos</strong>, sendo o cisto sinovial de punho o mais comum de todos.</li>
      <li><strong>Fraturas e luxações</strong> do punho e dos dedos, incluindo a fratura do escafoide, que engana com facilidade.</li>
      <li><strong>Lesões de tendão e de nervo</strong> por corte, que são urgência e mudam de prognóstico com o tempo.</li>
      <li><strong>Contratura de Dupuytren</strong>, o dedo que vai fechando aos poucos por um espessamento na palma.</li>
      <li><strong>Sequelas de trauma</strong>, rigidez e deformidades.</li>
    </ul>
"""},
        {"id": "formigamento", "titulo": "O que o padrão do formigamento revela", "html": """
    <p>Formigamento na mão não é tudo igual, e o dedo afetado diz muito sobre onde está o problema. Este é um daqueles casos em que uma observação simples, feita em casa, orienta o médico melhor do que um exame caro.</p>
    <div class="table-scroll">
      <table>
        <caption class="sr-only">Padrões de formigamento na mão e nervos correspondentes</caption>
        <thead><tr><th scope="col">Onde formiga</th><th scope="col">Nervo provável</th><th scope="col">Costuma ser</th></tr></thead>
        <tbody>
          <tr><td>Polegar, indicador, médio e metade do anelar</td><td>Mediano, no punho</td><td>Síndrome do túnel do carpo</td></tr>
          <tr><td>Mínimo e a outra metade do anelar</td><td>Ulnar, no cotovelo</td><td>Compressão no túnel cubital</td></tr>
          <tr><td>Dorso da mão, lado do polegar</td><td>Radial superficial</td><td>Compressão por pulseira, gesso ou relógio apertado</td></tr>
          <tr><td>Mão inteira, com dor no pescoço</td><td>Raiz cervical</td><td>Origem na coluna, e não na mão</td></tr>
          <tr><td>As duas mãos, com os pés também</td><td>Nervos periféricos em geral</td><td>Investigação clínica, como diabetes ou deficiência de vitamina B12</td></tr>
        </tbody>
      </table>
    </div>
    <p>Um detalhe clássico do túnel do carpo: o formigamento acorda a pessoa de madrugada e melhora ao sacudir a mão para fora da cama. Quem descreve exatamente isso já entrou com meio diagnóstico pronto.</p>
"""},
        {"id": "tunel-do-carpo", "titulo": "Síndrome do túnel do carpo", "html": """
    <p>O nervo mediano passa por um túnel estreito no punho, entre ossos e um ligamento espesso. Quando a pressão nesse túnel aumenta, aparecem formigamento, dormência e, em casos avançados, perda de força e atrofia da região do polegar.</p>
    <p><strong>Como se confirma.</strong> O diagnóstico é clínico, com testes de exame físico. A eletroneuromiografia ajuda a graduar a gravidade e a esclarecer casos duvidosos, e costuma ser pedida quando a cirurgia entra na conversa. Ela não é obrigatória para dar o diagnóstico.</p>
    <p><strong>O que funciona.</strong> Em quadros leves e moderados, a tala noturna que mantém o punho em posição neutra tem efeito real e é barata. A infiltração com corticoide alivia bem, mas o efeito tende a diminuir com o tempo em boa parte dos pacientes. Em quadros moderados a graves, a cirurgia de liberação do túnel se mostrou superior ao tratamento conservador em ensaios clínicos, com resultados duradouros e um procedimento curto, feito com anestesia local.</p>
    <p><strong>O que não muda o rumo.</strong> Vitaminas isoladas, ultrassom terapêutico e laser têm evidência fraca. E existe um ponto que costuma ser mal explicado: quando já há atrofia da musculatura do polegar, parte do dano é permanente, e adiar a cirurgia nessa fase custa função que não volta.</p>
"""},
        {"id": "gatilho-quervain", "titulo": "Dedo em gatilho e De Quervain", "html": """
    <p><strong>Dedo em gatilho.</strong> O tendão engrossa e passa a travar dentro da polia que o segura, e o dedo trava dobrado, destravando com um estalo, muitas vezes doloroso. É mais comum em mulheres, em quem tem diabetes e depois dos 40 anos. A infiltração com corticoide resolve a maioria dos casos, com taxas de sucesso altas em pacientes sem diabetes e menores em diabéticos. Quando a infiltração falha depois de uma ou duas tentativas, a cirurgia de abertura da polia é rápida, feita com anestesia local, e tem índice de resolução muito alto.</p>
    <p><strong>Tenossinovite de De Quervain.</strong> Dor na lateral do punho, do lado do polegar, que piora ao segurar peso com a mão em desvio, ao torcer pano e ao levantar bebê. É frequente no pós-parto, o que rendeu o apelido de punho da mãe. Tratamento com ajuste de carga, órtese que inclui o polegar e, quando necessário, infiltração, que tem bons resultados. A cirurgia fica para os casos resistentes.</p>
    <div class="callout info">
      <h3>Por que tanta infiltração nesta página</h3>
      <p>Na mão, ao contrário do joelho, várias infiltrações têm evidência boa, porque o alvo é pequeno, superficial e bem definido, e o problema é local. Isso mostra uma coisa importante: não existe tratamento bom ou ruim em abstrato, existe tratamento certo para o problema certo.</p>
    </div>
"""},
        {"id": "rizartrose-cistos", "titulo": "Rizartrose, cistos e Dupuytren", "html": """
    <p><strong>Rizartrose</strong> é a artrose da articulação na base do polegar. Dói ao pinçar, ao abrir potes, ao girar chave. O tratamento começa com órtese, ajuste de atividade e analgesia, e boa parte das pessoas segue bem assim por anos. Quando a dor limita muito, existem cirurgias com bons resultados de alívio.</p>
    <p><strong>Cisto sinovial</strong> é o caroço mais comum do punho. Não é câncer, e uma parcela grande desaparece sozinha com o tempo. A punção alivia, mas recidiva com frequência. A cirurgia é reservada a cistos que doem, limitam ou crescem, e também pode recidivar. Assustar-se com o tamanho não ajuda: cisto grande e indolor incomoda menos do que cisto pequeno em ponto de atrito.</p>
    <p><strong>Contratura de Dupuytren</strong> é um espessamento da fáscia da palma que puxa os dedos para dentro, com progressão lenta e história familiar frequente. O tratamento é indicado quando o dedo já não estica o suficiente para apoiar a mão em uma mesa, e envolve procedimentos que vão de agulha a cirurgia aberta, com taxas diferentes de recidiva.</p>
"""},
        {"id": "fraturas", "titulo": "Fraturas que enganam", "html": """
    <p>Duas fraturas de punho merecem atenção especial porque são frequentemente subestimadas.</p>
    <p><strong>Escafoide.</strong> Depois de uma queda com a mão espalmada, dor na base do polegar, naquela depressão que aparece quando você abre a mão, é escafoide até prova em contrário. O problema é que a radiografia inicial pode parecer normal em uma parte dos casos. Tratar como se fosse fratura e reavaliar é a conduta segura, porque um escafoide não consolidado leva a artrose precoce do punho e a uma cirurgia bem maior lá na frente.</p>
    <p><strong>Rádio distal.</strong> A fratura mais comum do membro superior, típica de queda ao ar livre e de fragilidade óssea depois dos 60 anos. Muitas são tratadas com imobilização, outras precisam de cirurgia, e a decisão depende de desvio, estabilidade, idade e demanda funcional. Em pessoas acima de 50 anos, uma fratura por queda da própria altura é também um alerta de osteoporose e merece investigação.</p>
"""},
        {"id": "quando-procurar", "titulo": "Quando procurar", "html": """
    <p>Vale marcar consulta quando houver formigamento que acorda à noite, dedo que trava, dor que impede segurar objetos, caroço que cresce, perda de força para abrir garrafa ou girar chave, ou dor que persiste depois de uma queda, mesmo com radiografia dita normal.</p>
""" + alerta("Procure atendimento imediato se houver", [
            "Corte profundo com perda de movimento de um dedo, o que sugere lesão de tendão.",
            "Dedo ou mão dormentes e pálidos, ou muito inchados depois de trauma ou de gesso apertado.",
            "Infecção com vermelhidão que avança, febre, ou dor forte após ferimento com prego, mordida de animal ou espinho.",
            "Dedo em posição anormal, ou incapacidade de mover uma articulação depois de trauma.",
            "Perda de força súbita associada a formigamento em toda a mão."])},
    ],
    faq=[
        ("Túnel do carpo tem cura sem cirurgia?",
         "Em quadros leves e moderados, muita gente melhora bem com tala noturna, ajuste das atividades que forçam o punho e, quando necessário, infiltração. Nos quadros moderados a graves, a cirurgia de liberação se mostrou superior ao tratamento conservador em ensaios clínicos e tem resultado duradouro. Quando já existe perda de força e atrofia na base do polegar, adiar custa função que pode não voltar."),
        ("Quanto tempo demora para voltar a trabalhar depois da cirurgia de mão?",
         "Depende do procedimento e do trabalho. Em cirurgias pequenas, como dedo em gatilho e túnel do carpo, muitas pessoas com trabalho leve voltam em uma a duas semanas, enquanto atividades com esforço e vibração exigem mais tempo. Cirurgias de fratura e de tendão têm reabilitação bem mais longa, com terapia da mão."),
        ("Dedo em gatilho volta depois da infiltração?",
         "Pode voltar. A infiltração com corticoide resolve a maior parte dos casos, com taxas de sucesso mais altas em pessoas sem diabetes. Quando o dedo volta a travar depois de uma ou duas infiltrações, a cirurgia de abertura da polia é rápida, feita com anestesia local, e tem índice muito alto de resolução definitiva."),
        ("Cisto no punho precisa operar?",
         "Na maioria das vezes não. Uma parcela grande dos cistos sinoviais desaparece sozinha, e o tamanho não indica gravidade. A cirurgia entra quando o cisto dói, limita o movimento, comprime alguma estrutura ou cresce de forma atípica. Bater com objeto para estourar o cisto é uma prática antiga que não deve ser feita, porque machuca tecidos vizinhos e não impede a recidiva."),
        ("Caí com a mão espalmada e a radiografia deu normal, mas ainda dói. É normal?",
         "Merece reavaliação. A fratura do escafoide pode não aparecer na radiografia inicial e, quando é ignorada, evolui para falta de consolidação e artrose precoce do punho. Se a dor está naquela depressão na base do polegar, a conduta segura é imobilizar, reavaliar em alguns dias e, se preciso, complementar com outro exame de imagem."),
    ],
    takeaways=[
        "O dedo onde formiga aponta o nervo comprometido e orienta o diagnóstico.",
        "Formigamento que acorda à noite e melhora ao sacudir a mão é o padrão do túnel do carpo.",
        "Na mão, várias infiltrações têm evidência boa, ao contrário do que acontece em articulações grandes.",
        "Dedo em gatilho responde bem a infiltração, e a cirurgia é pequena quando ela falha.",
        "Cisto de punho costuma sumir sozinho e não é câncer.",
        "Dor na base do polegar depois de queda com a mão espalmada é escafoide até prova em contrário.",
        "Atrofia da musculatura do polegar significa que o nervo já sofreu, e aí o tempo importa.",
    ],
    refs=[
        "Padua L et al. Carpal tunnel syndrome: clinical features, diagnosis, and management. The Lancet Neurology, 2016.",
        "American Academy of Orthopaedic Surgeons. Management of carpal tunnel syndrome, clinical practice guideline.",
        "Verdugo RJ et al. Surgical versus non-surgical treatment for carpal tunnel syndrome. Cochrane Database of Systematic Reviews.",
        "Fiorini HJ et al. Surgery for trigger finger. Cochrane Database of Systematic Reviews, 2018.",
        "Huisstede BM et al. Effectiveness of interventions for de Quervain disease: a systematic review. Physical Therapy.",
        "Clementson M et al. Acute scaphoid fractures: guidelines for diagnosis and treatment. EFORT Open Reviews, 2020.",
    ],
)

# ---------------------------------------------------------------------------
# Pé e tornozelo
# ---------------------------------------------------------------------------
escrever(
    "ortopedista-pe-tornozelo-curitiba.html",
    title="Ortopedista de pé e tornozelo em Curitiba",
    description="Pé e tornozelo em Curitiba: fascite plantar, entorse, tendão de Aquiles e joanete, com o que a evidência mostra e quando o raio-x é necessário.",
    h1="Ortopedista de pé e tornozelo em Curitiba",
    lead="Aqui estão as fichas dos especialistas em pé e tornozelo de Curitiba. Logo abaixo delas vem o guia: dor no calcanhar, entorse, quando o raio-x é necessário e o que funciona de verdade.",
    crumbs=CRUMB,
    lista={"titulo": "Ortopedistas de pé e tornozelo em Curitiba",
           "texto": "Cirurgia do pé e tornozelo é uma área de atuação com formação adicional depois da residência.", "area": "Cirurgia do pé e tornozelo", "n": 3},
    banda={"titulo": "Procurando outra área?",
           "texto": "Digite onde dói e a busca mostra qual ortopedista cuida daquela parte do corpo."},
    secoes=[
        {"id": "o-que-trata", "titulo": "O que o especialista em pé e tornozelo trata", "html": """
    <ul>
      <li><strong>Dor no calcanhar</strong>, principalmente a fascite plantar, e o famoso esporão.</li>
      <li><strong>Entorses de tornozelo</strong> e a instabilidade que sobra depois de entorses repetidas.</li>
      <li><strong>Tendinopatia do Aquiles</strong> e as demais tendinopatias do tornozelo.</li>
      <li><strong>Deformidades</strong>, como joanete, dedo em garra e pé plano do adulto.</li>
      <li><strong>Metatarsalgia e neuroma de Morton</strong>, a dor na planta, perto dos dedos.</li>
      <li><strong>Artrose do tornozelo e do médio pé.</strong></li>
      <li><strong>Fraturas</strong> do tornozelo, do calcâneo e do médio pé, incluindo as fraturas por estresse de corredores.</li>
      <li><strong>Pé do paciente com diabetes</strong>, que é um capítulo à parte e exige acompanhamento conjunto.</li>
    </ul>
"""},
        {"id": "calcanhar", "titulo": "Dor no calcanhar e fascite plantar", "html": """
    <p>O padrão é inconfundível: os primeiros passos da manhã doem muito, melhoram depois de alguns minutos caminhando e voltam no fim do dia ou depois de ficar muito tempo em pé. A dor fica na parte de baixo do calcanhar, mais para dentro.</p>
    <p><strong>Sobre o esporão.</strong> Ele aparece em muita gente sem dor nenhuma, e não é a causa do problema. O esporão é consequência da tração crônica, e não a origem. Retirar esporão não é o tratamento da fascite.</p>
    <p><strong>O que funciona, em ordem de evidência.</strong> Alongamento específico da fáscia plantar e da panturrilha, feito diariamente, é a base e tem bom respaldo. Ajuste de carga e de calçado ajuda. Palmilhas dão alívio de curto prazo, com benefício menos claro no longo prazo. Terapia por ondas de choque tem evidência razoável em casos que não melhoram depois de alguns meses. A infiltração com corticoide alivia rápido, mas o efeito dura pouco e existe risco de ruptura da fáscia e de atrofia do coxim de gordura do calcanhar, então não é para repetir sem critério.</p>
    <p><strong>O dado mais importante para a sua expectativa:</strong> a fascite plantar é autolimitada na grande maioria dos casos. Algo em torno de nove em cada dez pessoas melhora dentro de aproximadamente um ano com tratamento conservador bem feito. Saber disso muda a decisão sobre procedimentos caros e agressivos oferecidos no terceiro mês.</p>
"""},
        {"id": "entorse", "titulo": "Entorse de tornozelo: quando o raio-x é necessário", "html": """
    <p>A maior parte das entorses não precisa de radiografia. Existe uma regra clínica validada, usada no mundo inteiro, que ajuda a decidir e evita exame desnecessário sem deixar passar fratura.</p>
    <div class="callout info">
      <h3>Sinais que indicam radiografia depois de uma entorse</h3>
      <ul>
        <li>Dor à palpação na borda posterior ou na ponta do maléolo lateral, aquele osso saliente do lado de fora.</li>
        <li>Dor à palpação na borda posterior ou na ponta do maléolo medial, do lado de dentro.</li>
        <li>Incapacidade de dar quatro passos, tanto logo após o trauma quanto no atendimento.</li>
        <li>No pé, dor na base do quinto metatarso ou no osso navicular.</li>
      </ul>
      <p>Sem nenhum desses sinais, a chance de fratura é muito baixa. Com qualquer um deles, a radiografia está indicada.</p>
    </div>
    <p><strong>Tratamento.</strong> A reabilitação funcional, com movimento precoce dentro do tolerável, apoio conforme a dor permitir e exercícios de equilíbrio, dá melhor resultado do que imobilização prolongada nas entorses simples. O treino proprioceptivo, aquele de equilíbrio em apoio de um pé só, reduz de forma consistente o risco de novas entorses, e é a parte que quase todo mundo pula.</p>
    <p><strong>Quando vira caso de especialista.</strong> Tornozelo que continua falhando meses depois, dor persistente na frente do tornozelo, sensação de travamento, ou entorses que se repetem várias vezes ao ano. Aí entra a investigação de instabilidade crônica e de lesões associadas da cartilagem.</p>
"""},
        {"id": "aquiles", "titulo": "Tendão de Aquiles", "html": """
    <p>A tendinopatia do Aquiles dá dor e rigidez atrás do calcanhar, pior ao levantar da cama e ao iniciar a corrida, às vezes com espessamento visível do tendão. O tratamento com melhor evidência é o exercício de fortalecimento progressivo, com ênfase na fase excêntrica, mantido por pelo menos três meses. É chato, é lento e funciona. Infiltração de corticoide dentro do tendão não deve ser feita, pelo risco de ruptura.</p>
    <p>A ruptura completa do Aquiles é outra história: acontece tipicamente em quem volta a jogar depois de anos parado, com a sensação de uma pedrada atrás do tornozelo, estalo audível e dificuldade de ficar na ponta do pé. É urgência ortopédica, e o tratamento pode ser cirúrgico ou funcional com imobilização, com resultados próximos em protocolos modernos de reabilitação.</p>
"""},
        {"id": "joanete", "titulo": "Joanete e dor na planta do pé", "html": """
    <p><strong>Joanete</strong>, ou hálux valgo, é o desvio do dedão com proeminência na borda interna do pé. Palmilhas, separadores e calçado adequado aliviam sintomas, mas não corrigem o desvio, e nenhum exercício desentorta o dedo. A cirurgia é indicada por dor e limitação, e não por aparência: operar joanete que não dói costuma trocar um problema estético por um problema real. Quando bem indicada, a correção tem bons resultados, com recuperação que leva semanas a meses.</p>
    <p><strong>Metatarsalgia</strong> é a dor na planta, logo atrás dos dedos, comum em quem usa salto, em quem aumentou a corrida rápido demais e em pés com deformidade. <strong>Neuroma de Morton</strong> é a dor com queimação e formigamento entre o terceiro e o quarto dedos, com sensação de pedra no sapato. Ambos começam com ajuste de calçado e palmilha, e têm opções de infiltração e cirurgia nos casos resistentes.</p>
"""},
        {"id": "diabetes", "titulo": "Pé de quem tem diabetes", "html": """
    <p>Esta seção existe porque salva pé. Quem tem diabetes há anos pode perder sensibilidade nos pés e deixar de sentir uma bolha, um corte ou um prego. A lesão evolui em silêncio e infecciona.</p>
    <div class="callout alert">
      <h3>Se você tem diabetes, procure atendimento no mesmo dia se aparecer</h3>
      <ul>
        <li>Qualquer ferida, bolha ou rachadura que não fecha, mesmo sem dor.</li>
        <li>Vermelhidão, calor, inchaço ou cheiro forte no pé.</li>
        <li>Mudança de formato do pé, com inchaço e calor sem ferida, o que pode ser pé de Charcot.</li>
        <li>Unha encravada com pus.</li>
      </ul>
      <p>Ferida em pé de pessoa com diabetes não espera a semana que vem, e a ausência de dor não significa que seja leve.</p>
    </div>
"""},
        {"id": "quando-procurar", "titulo": "Quando procurar o especialista", "html": """
    <p>Marque consulta quando a dor no pé dura mais de quatro a seis semanas, quando o tornozelo continua falhando, quando entorses se repetem, quando aparece deformidade nova, quando a dor aparece à noite em repouso, ou quando você teve trauma e continua sem conseguir apoiar direito.</p>
""" + alerta("Procure atendimento imediato se houver", [
            "Impossibilidade de apoiar o peso depois de trauma, ou deformidade visível do tornozelo.",
            "Estalo atrás do tornozelo com dificuldade de ficar na ponta do pé, o que sugere ruptura do Aquiles.",
            "Pé frio, pálido ou roxo, com ou sem dormência.",
            "Vermelhidão que avança pelo pé, com febre.",
            "Dor desproporcional depois de trauma ou de gesso, com inchaço tenso.",
            "Ferida em pé de pessoa com diabetes, com ou sem dor."])},
    ],
    faq=[
        ("Toda entorse de tornozelo precisa de raio-x?",
         "Não. Existe uma regra clínica validada que indica radiografia quando há dor à palpação das bordas ou pontas dos maléolos, dor na base do quinto metatarso ou no navicular, ou incapacidade de dar quatro passos. Sem esses sinais, a chance de fratura é muito baixa e o exame costuma ser dispensável."),
        ("Esporão de calcâneo é a causa da minha dor no calcanhar?",
         "Quase nunca. O esporão aparece em muitas pessoas sem dor nenhuma e é consequência da tração crônica na região, não a causa. A dor típica vem da fascite plantar, e o tratamento é dirigido a ela, com alongamento, ajuste de carga e calçado, não à retirada do esporão."),
        ("Quanto tempo dura uma fascite plantar?",
         "Costuma ser longo e costuma passar. A grande maioria das pessoas melhora dentro de cerca de um ano com tratamento conservador bem feito, e a parte que mais ajuda é o alongamento diário da fáscia e da panturrilha. Saber disso evita aceitar procedimentos caros e agressivos cedo demais."),
        ("Palmilha corrige joanete?",
         "Não. Palmilhas, separadores e calçados largos aliviam sintomas e distribuem melhor a carga, o que já é bastante útil, mas não corrigem o desvio do dedão nem impedem a progressão. A correção do desvio é cirúrgica, e a indicação deve ser por dor e limitação, não por estética."),
        ("Posso continuar correndo com dor no tendão de Aquiles?",
         "Em geral é possível manter alguma corrida, com volume reduzido, desde que a dor durante a atividade seja tolerável e não piore no dia seguinte. O que muda o quadro é o programa de fortalecimento progressivo, mantido por pelo menos três meses. Parar completamente e voltar sem fortalecer costuma levar de volta ao mesmo ponto."),
    ],
    takeaways=[
        "A dor no primeiro passo da manhã é a assinatura da fascite plantar.",
        "Esporão não é a causa da dor, é consequência da tração.",
        "A maioria das fascites melhora em cerca de um ano com alongamento e ajuste de carga.",
        "Entorse sem dor nos maléolos e com capacidade de caminhar raramente precisa de raio-x.",
        "Treino de equilíbrio reduz o risco de nova entorse, e é a parte que todo mundo pula.",
        "No Aquiles, o tratamento com melhor evidência é fortalecimento progressivo, não infiltração.",
        "Ferida em pé de pessoa com diabetes é urgência, mesmo sem dor.",
    ],
    refs=[
        "Stiell IG et al. Decision rules for the use of radiography in acute ankle injuries. JAMA, 1993.",
        "Bachmann LM et al. Accuracy of Ottawa ankle rules to exclude fractures of the ankle and mid-foot: systematic review. BMJ, 2003.",
        "Vuurberg G et al. Diagnosis, treatment and prevention of ankle sprains: update of an evidence-based clinical guideline. British Journal of Sports Medicine, 2018.",
        "Trojian T, Tucker AK. Plantar fasciitis. American Family Physician, 2019.",
        "Babatunde OO et al. Comparative effectiveness of treatment options for plantar heel pain: a systematic review and network meta-analysis. British Journal of Sports Medicine, 2019.",
        "Malliaras P et al. Achilles and patellar tendinopathy loading programmes: a systematic review. Sports Medicine.",
        "Sociedade Brasileira de Diabetes. Diretrizes sobre prevenção e cuidado do pé diabético.",
    ],
)

# ---------------------------------------------------------------------------
# Quadril, página curta que aponta para o site irmão
# ---------------------------------------------------------------------------
escrever(
    "ortopedista-quadril-curitiba.html",
    title="Ortopedista de quadril em Curitiba: por onde começar",
    description="Dor no quadril em Curitiba: o que é dor de quadril de verdade, o que costuma ser dor lateral e onde ler o conteúdo completo sobre artrose, bursite e prótese.",
    h1="Ortopedista de quadril em Curitiba",
    lead="Aqui estão as fichas dos ortopedistas de quadril de Curitiba. Logo abaixo delas vem o essencial: por que a dor de quadril é sentida na virilha, e não na lateral, e onde está o conteúdo aprofundado.",
    crumbs=CRUMB,
    lista={"titulo": "Ortopedistas de quadril em Curitiba",
           "texto": "Cirurgia do quadril é uma área de atuação com formação específica depois da residência.", "area": "Cirurgia do quadril", "n": 3},
    secoes=[
        {"id": "onde-doi", "titulo": "Dor de quadril dói na virilha, não na lateral", "html": """
    <p>Esta é a informação mais útil desta página. A articulação do quadril fica funda, no meio da virilha. Por isso, o problema articular verdadeiro, como a artrose, costuma doer na virilha, às vezes irradiando para a frente da coxa e até para o joelho.</p>
    <p>Já a dor bem na lateral, sobre aquela proeminência óssea onde você apoia a mão, com dor ao deitar daquele lado à noite, quase sempre não vem da articulação. Vem dos tendões dos glúteos e da bursa daquela região. São problemas diferentes, com tratamentos diferentes, e confundi-los leva a exame errado e a expectativa errada.</p>
    <div class="table-scroll">
      <table>
        <caption class="sr-only">Onde dói e o que costuma ser no quadril</caption>
        <thead><tr><th scope="col">Onde dói</th><th scope="col">Costuma ser</th></tr></thead>
        <tbody>
          <tr><td>Virilha, com dificuldade de calçar meia e de entrar no carro</td><td>Artrose ou impacto femoroacetabular</td></tr>
          <tr><td>Lateral, com dor ao deitar daquele lado</td><td>Tendinopatia dos glúteos e bursite trocantérica</td></tr>
          <tr><td>Nádega, com dor que desce pela perna</td><td>Origem na coluna lombar, e não no quadril</td></tr>
          <tr><td>Virilha em atleta jovem, ao girar</td><td>Impacto femoroacetabular e lesão labral</td></tr>
        </tbody>
      </table>
    </div>
"""},
        {"id": "site-irmao", "titulo": "O conteúdo completo fica no Quadril Curitiba", "html": """
    <p>Manter dois textos profundos sobre o mesmo assunto, em dois endereços diferentes, é ruim para o leitor e ruim para os dois sites. Por isso o conteúdo aprofundado de quadril vive em um projeto próprio, com a mesma filosofia editorial deste aqui: linguagem de paciente, referências citadas e honestidade sobre a força da evidência.</p>
    <p>Lá você encontra, entre outros temas, artrose de quadril e coxartrose, prótese de quadril e o que esperar da recuperação, bursite trocantérica e tendinopatia dos glúteos, impacto femoroacetabular, e fratura de quadril no idoso.</p>
    <div class="cta-band reveal">
      <div>
        <h2>Conteúdo completo sobre quadril</h2>
        <p>Artrose, prótese, bursite, impacto femoroacetabular e fratura no idoso, explicados em detalhe no nosso site dedicado ao tema.</p>
      </div>
      <a class="btn lg" href="https://quadrilcuritiba.com.br/" rel="noopener">Ir para quadrilcuritiba.com.br</a>
    </div>
"""},
        {"id": "quando-procurar", "titulo": "Quando procurar um ortopedista de quadril", "html": """
    <p>Vale marcar consulta quando a dor na virilha persiste por semanas, quando calçar meia ou cortar a unha do pé ficou difícil, quando você começou a mancar, quando a dor limita caminhar distâncias que antes eram tranquilas, ou quando a dor lateral atrapalha o sono há mais de um mês.</p>
""" + alerta("Procure atendimento imediato se houver", [
            "Impossibilidade de apoiar o peso depois de uma queda, principalmente em pessoa idosa: fratura de quadril é urgência.",
            "Perna que ficou visivelmente mais curta ou rodada para fora depois de trauma.",
            "Dor forte com febre e dificuldade de mover o quadril.",
            "Dor intensa que começou de repente, sem trauma, em quem faz uso prolongado de corticoide.",
            "Criança que se recusa a andar ou manca com febre."])},
    ],
    faq=[
        ("Dor na lateral do quadril é bursite?",
         "Frequentemente sim, embora hoje se entenda que o problema costuma envolver principalmente os tendões dos glúteos, e não apenas a bursa. O padrão típico é dor sobre a proeminência óssea lateral, que piora ao deitar daquele lado, ao subir escada e ao ficar muito tempo em pé apoiado em uma perna só. O tratamento começa com ajuste de carga e fortalecimento, e não com cirurgia."),
        ("Dor no quadril pode ser problema de coluna?",
         "Pode, e essa é uma das confusões mais comuns. Dor que começa na nádega e desce pela perna, com formigamento, costuma vir da coluna lombar. Já a dor de origem articular do quadril é sentida na virilha e piora com movimentos de rotação, como entrar no carro. Muitas vezes as duas coisas coexistem em pessoas mais velhas, e o exame físico separa uma da outra."),
        ("Artrose de quadril tem tratamento sem cirurgia?",
         "Tem, e ele deve ser tentado antes. Exercício supervisionado, controle de peso quando há sobrepeso, ajuste de atividades e analgesia adequada melhoram dor e função em boa parte dos pacientes. A prótese entra quando a dor limita o dia a dia e o sono e o tratamento conservador bem feito já não sustenta a qualidade de vida."),
        ("Por que o conteúdo detalhado de quadril está em outro site?",
         "Porque já existe um projeto nosso dedicado só a esse tema, com páginas aprofundadas sobre artrose, prótese, bursite e impacto femoroacetabular. Repetir o mesmo conteúdo em dois endereços prejudica o leitor, que se perde, e prejudica os dois sites na busca. Aqui ficam a orientação inicial e a lista de profissionais."),
    ],
    takeaways=[
        "Dor de quadril verdadeira costuma ser sentida na virilha, não na lateral.",
        "Dor lateral com dificuldade de deitar daquele lado costuma ser tendinopatia dos glúteos e bursite.",
        "Dor na nádega que desce pela perna costuma vir da coluna lombar.",
        "Artrose de quadril tem tratamento conservador que deve ser tentado antes da prótese.",
        "Queda em pessoa idosa com incapacidade de apoiar o peso é emergência.",
        "O conteúdo aprofundado de quadril está em quadrilcuritiba.com.br.",
    ],
    refs=[
        "Bannuru RR et al. OARSI guidelines for the non-surgical management of knee, hip, and polyarticular osteoarthritis. Osteoarthritis and Cartilage, 2019.",
        "National Institute for Health and Care Excellence. Osteoarthritis in over 16s: diagnosis and management, NG226, 2022.",
        "Grimaldi A et al. Gluteal tendinopathy: a review of mechanisms, assessment and management. Sports Medicine, 2015.",
        "Griffin DR et al. The Warwick agreement on femoroacetabular impingement syndrome. British Journal of Sports Medicine, 2016.",
    ],
)

print("páginas de área geradas: mão, pé e tornozelo, quadril")
