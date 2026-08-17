#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conteúdo das páginas de ortopedia infantil e medicina esportiva."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from page_builder import escrever
from conteudo_areas_1 import alerta, CRUMB

# ---------------------------------------------------------------------------
# Ortopedia infantil
# ---------------------------------------------------------------------------
escrever(
    "ortopedista-infantil-curitiba.html",
    title="Ortopedista infantil em Curitiba: quando levar",
    description="Ortopedia pediátrica em Curitiba: o que é normal no crescimento, dores de crescimento, criança que manca, displasia do quadril, pé torto e escoliose.",
    h1="Ortopedista infantil em Curitiba",
    lead="Aqui estão as fichas dos ortopedistas infantis de Curitiba. Logo abaixo delas vem o guia: o que é normal no crescimento, dores de crescimento, criança que manca e os sinais que não esperam.",
    crumbs=CRUMB,
    lista={"titulo": "Ortopedistas infantis em Curitiba",
           "texto": "Ortopedia pediátrica é uma área de atuação com formação específica depois da residência em ortopedia.", "area": "Ortopedia pediátrica", "n": 3},
    banda={"titulo": "Procurando outra área?",
           "texto": "A busca por área mostra qual ortopedista cuida de cada parte do corpo, em poucos segundos."},
    secoes=[
        {"id": "o-que-trata", "titulo": "O que o ortopedista pediátrico trata", "html": """
    <p>O esqueleto da criança não é um esqueleto de adulto em miniatura. Ele cresce a partir de cartilagens específicas, as placas de crescimento, que são mais frágeis que os ligamentos e que respondem de um jeito próprio a trauma, infecção e sobrecarga. Isso cria um grupo de doenças que só existem nessa faixa etária.</p>
    <ul>
      <li><strong>Displasia do desenvolvimento do quadril</strong>, detectada nos primeiros meses de vida.</li>
      <li><strong>Pé torto congênito</strong>, tratado desde as primeiras semanas.</li>
      <li><strong>Desvios de eixo e de marcha</strong>, como pernas arqueadas, joelhos para dentro, pé chato e andar com os pés virados.</li>
      <li><strong>Dores de crescimento</strong> e dores por sobrecarga esportiva, como as apofisites.</li>
      <li><strong>Criança que manca</strong>, com ou sem febre, que sempre merece avaliação.</li>
      <li><strong>Escoliose do adolescente</strong> e outras deformidades da coluna.</li>
      <li><strong>Fraturas na criança</strong>, incluindo as que envolvem a placa de crescimento.</li>
      <li><strong>Doenças específicas do quadril infantil</strong>, como Perthes e epifisiólise.</li>
    </ul>
"""},
        {"id": "o-que-e-normal", "titulo": "O que é normal e assusta os pais", "html": """
    <p>Muita consulta de ortopedia infantil termina com a melhor notícia possível: não é nada, é o crescimento. Vale conhecer os padrões normais.</p>
    <div class="table-scroll">
      <table>
        <caption class="sr-only">Variações normais do crescimento por idade</caption>
        <thead><tr><th scope="col">O que os pais notam</th><th scope="col">Costuma ser normal</th><th scope="col">Preocupa quando</th></tr></thead>
        <tbody>
          <tr><td>Pernas arqueadas, em formato de O</td><td>Até cerca dos 2 anos</td><td>Persiste depois dos 3 anos, é só de um lado ou está piorando</td></tr>
          <tr><td>Joelhos para dentro, em formato de X</td><td>Entre 3 e 6 anos, com correção espontânea</td><td>Assimétrico, muito acentuado ou associado a baixa estatura</td></tr>
          <tr><td>Pé chato flexível</td><td>Muito comum, o arco costuma se formar até 6 a 8 anos</td><td>Rígido, doloroso ou só de um lado</td></tr>
          <tr><td>Andar com os pés virados para dentro</td><td>Comum e melhora com o crescimento</td><td>Causa quedas frequentes ou piora com a idade</td></tr>
          <tr><td>Andar na ponta dos pés</td><td>Fase transitória em crianças pequenas</td><td>Persiste, é só de um lado, ou vem com atraso do desenvolvimento</td></tr>
        </tbody>
      </table>
    </div>
    <div class="callout info">
      <h3>Três mitos que custam dinheiro</h3>
      <p>Palmilha não cria arco em pé chato flexível de criança, e a evidência disso é consistente. Botinha ortopédica não corrige desvio de marcha. Mochila pesada não causa escoliose, embora possa causar dor nas costas por sobrecarga.</p>
    </div>
"""},
        {"id": "dores-de-crescimento", "titulo": "Dores de crescimento", "html": """
    <p>Existem de verdade, são comuns entre 3 e 12 anos e têm um padrão bem definido: dor nas duas pernas, principalmente na coxa, na panturrilha ou atrás dos joelhos, no fim da tarde ou à noite, às vezes acordando a criança, que melhora com massagem, calor e colo, e some completamente pela manhã. A criança corre e brinca normalmente no dia seguinte.</p>
    <p>Esse padrão é tranquilizador. O que não combina com dor de crescimento, e por isso merece avaliação, é dor em um lado só, dor em um ponto específico, inchaço, manqueira, febre, perda de peso, cansaço fora do normal ou dor que atrapalha a criança durante o dia.</p>
"""},
        {"id": "crianca-que-manca", "titulo": "Criança que manca", "html": """
    <p>Manqueira em criança nunca é normal, e a lista de causas vai do banal ao grave. As mais frequentes:</p>
    <ul>
      <li><strong>Sinovite transitória do quadril.</strong> Inflamação passageira, muitas vezes depois de uma virose, com dor e limitação que melhoram em dias.</li>
      <li><strong>Artrite séptica.</strong> Infecção dentro da articulação. É emergência: a criança tem febre, dor intensa, recusa completa de mover o membro e piora rápido. Cada hora conta.</li>
      <li><strong>Doença de Legg-Calvé-Perthes.</strong> Alteração da irrigação da cabeça do fêmur, mais comum em meninos entre 4 e 8 anos, com manqueira e dor que pode ser sentida no joelho.</li>
      <li><strong>Epifisiólise proximal do fêmur.</strong> Escorregamento da placa de crescimento do quadril, típico de adolescentes, com maior frequência em quem tem sobrepeso. Também costuma doer no joelho ou na coxa.</li>
      <li><strong>Fraturas ocultas</strong>, incluindo a fratura em criança pequena que começou a mancar depois de uma queda banal.</li>
    </ul>
    <div class="callout accent">
      <h3>A regra que evita um erro clássico</h3>
      <p>Toda criança ou adolescente com dor no joelho precisa ter o quadril examinado. Perthes e epifisiólise se manifestam com dor referida no joelho, e são diagnósticos em que a demora custa caro. Se o exame do joelho é normal e a dor persiste, o problema pode estar acima.</p>
    </div>
"""},
        {"id": "quadril-do-bebe", "titulo": "Quadril do bebê e pé torto", "html": """
    <p><strong>Displasia do desenvolvimento do quadril.</strong> É a formação inadequada da articulação, que pode ir de uma leve imaturidade até a luxação. O exame físico do recém-nascido faz parte da rotina, e a ultrassonografia é o exame de escolha nos primeiros meses, indicada especialmente quando há fatores de risco, como parto pélvico, história familiar e sexo feminino. Quanto mais cedo se trata, mais simples é o tratamento: nos primeiros meses costuma bastar um suspensório específico, enquanto o diagnóstico tardio pode levar a cirurgia.</p>
    <p>Um detalhe prático que os pais podem controlar: o bebê deve ser enrolado de forma que as pernas fiquem livres para dobrar e abrir. Enrolar apertado com as pernas esticadas e juntas está associado a maior risco de displasia.</p>
    <p><strong>Pé torto congênito.</strong> O tratamento moderno começa nas primeiras semanas de vida com trocas seriadas de gesso, seguidas de um pequeno procedimento no tendão de Aquiles quando necessário e de uso de órtese por alguns anos. Os resultados são bons, e o ponto crítico é a adesão à órtese, porque é ela que evita a recidiva.</p>
"""},
        {"id": "escoliose", "titulo": "Escoliose do adolescente", "html": """
    <p>A escoliose idiopática do adolescente costuma aparecer na fase de estirão, é mais frequente em meninas e geralmente não dói. Ela é notada por assimetria dos ombros, da cintura ou das escápulas, e fica mais evidente quando a pessoa se inclina para a frente.</p>
    <p><strong>O que muda o rumo.</strong> Em curvas que ainda estão em risco de progressão, durante o crescimento, o colete tem evidência de reduzir a chance de a curva chegar ao ponto de indicação cirúrgica, e o benefício aumenta com as horas de uso por dia. Isso foi demonstrado em um ensaio clínico que precisou ser interrompido antes do previsto porque o resultado a favor do colete já era claro. Fisioterapia específica ajuda em sintomas e postura, mas não substitui o colete quando ele está indicado.</p>
    <p>Curvas grandes, com progressão importante, podem chegar a indicação cirúrgica. O acompanhamento durante o crescimento é o que permite decidir na hora certa, e é por isso que a avaliação precoce importa mesmo quando não dói nada.</p>
"""},
        {"id": "fraturas", "titulo": "Fraturas na criança", "html": """
    <p>Osso de criança quebra diferente e cola diferente. Ele é mais elástico, o que produz fraturas em galho verde, e tem uma capacidade de remodelação que permite aceitar desvios que seriam inaceitáveis em adultos, principalmente em crianças pequenas e em desvios no mesmo plano de movimento da articulação.</p>
    <p>Isso é uma boa notícia, com uma exceção importante: fraturas que atravessam a placa de crescimento exigem atenção especial, porque podem alterar o crescimento daquele osso e gerar diferença de comprimento ou desvio de eixo com o tempo. Por isso o acompanhamento depois da consolidação faz parte do tratamento.</p>
    <p>Cotovelo merece um parágrafo próprio: a fratura supracondiliana do úmero, típica de queda do trampolim ou do escorregador, pode comprometer nervos e vasos e é uma das poucas fraturas pediátricas que costumam exigir cirurgia com urgência.</p>
"""},
        {"id": "quando-procurar", "titulo": "Quando levar ao ortopedista", "html": """
    <p>Vale marcar consulta quando houver assimetria entre os lados, quando o desvio piora em vez de melhorar com a idade, quando existe dor que atrapalha brincar, quando a criança evita usar um braço ou uma perna, quando há história familiar de doença ortopédica, ou quando a escola aponta assimetria de ombros no adolescente.</p>
""" + alerta("Procure atendimento imediato se a criança apresentar", [
            "Febre com dor intensa em uma articulação e recusa de mover o membro.",
            "Recusa de andar ou de apoiar o peso, sem explicação clara.",
            "Deformidade visível, dor forte ou inchaço rápido depois de queda.",
            "Dor que acorda a criança à noite de forma persistente, com perda de peso ou palidez.",
            "Perda de força, dormência ou mão e pé frios depois de trauma ou de gesso.",
            "Inchaço de uma articulação que aparece em poucas horas."])},
    ],
    faq=[
        ("Meu filho tem pé chato, precisa de palmilha?",
         "Na grande maioria dos casos, não. O pé chato flexível é comum na infância e o arco tende a se formar até por volta dos 6 a 8 anos. Estudos mostram que palmilhas não moldam o arco nem alteram o resultado final nesses casos. A avaliação é indicada quando o pé é rígido, dói, é assimétrico ou vem acompanhado de outros achados."),
        ("Dores de crescimento existem mesmo?",
         "Existem e são comuns entre 3 e 12 anos. O padrão típico é dor nas duas pernas, no fim do dia ou à noite, que melhora com massagem e some pela manhã, sem manqueira e sem inchaço. O que não é dor de crescimento é dor de um lado só, dor em um ponto específico, febre, inchaço, manqueira ou dor que atrapalha durante o dia."),
        ("Criança que manca precisa ir ao médico no mesmo dia?",
         "Se houver febre, recusa de mover o membro ou dor intensa, sim, e sem esperar, porque artrite séptica é emergência. Manqueira sem febre e sem sinais de gravidade merece avaliação em poucos dias. Manqueira nunca deve ser tratada como coisa passageira apenas porque a criança está brincando entre as crises."),
        ("Mochila pesada causa escoliose?",
         "Não. A escoliose idiopática do adolescente não é causada por mochila, por postura sentada nem por dormir de lado. Mochila muito pesada pode causar dor nas costas por sobrecarga, o que é motivo suficiente para ajustar o peso, mas não altera a formação da curva."),
        ("Meu filho reclama do joelho e o exame do joelho deu normal. E agora?",
         "O quadril precisa ser examinado. Em crianças e adolescentes, doenças do quadril como Perthes e epifisiólise se manifestam frequentemente com dor referida no joelho ou na coxa. Essa é uma das armadilhas clássicas da ortopedia pediátrica, e o atraso no diagnóstico tem consequências."),
        ("Colete funciona na escoliose?",
         "Sim, quando indicado corretamente durante o crescimento. Um ensaio clínico importante mostrou redução significativa da progressão até o limiar cirúrgico com o uso do colete, com benefício maior quanto mais horas por dia ele era usado. Não é confortável, mas é uma das intervenções ortopédicas com evidência mais clara na adolescência."),
    ],
    takeaways=[
        "Boa parte dos desvios de perna e de marcha na infância é variação normal e se corrige com o crescimento.",
        "Palmilha não cria arco em pé chato flexível de criança.",
        "Dor de crescimento é bilateral, noturna e some de manhã; fora desse padrão, investigue.",
        "Criança que manca com febre é emergência até prova em contrário.",
        "Dor no joelho de criança e adolescente exige exame do quadril.",
        "Colete tem evidência de reduzir a progressão da escoliose durante o crescimento.",
        "Fratura que envolve a placa de crescimento precisa de acompanhamento depois de consolidar.",
    ],
    refs=[
        "Weinstein SL et al. Effects of bracing in adolescents with idiopathic scoliosis, BrAIST. New England Journal of Medicine, 2013.",
        "Evans AM, Rome K. A review of the evidence for non-surgical interventions for flexible pediatric flat feet. European Journal of Physical and Rehabilitation Medicine.",
        "American Academy of Pediatrics. Clinical report on the evaluation and referral for developmental dysplasia of the hip in infants.",
        "Kocher MS et al. Differentiating between septic arthritis and transient synovitis of the hip in children. Journal of Bone and Joint Surgery.",
        "Dobbs MB, Gurnett CA. Update on clubfoot: etiology and treatment. Clinical Orthopaedics and Related Research.",
        "Sociedade Brasileira de Ortopedia e Traumatologia. Informações ao público sobre ortopedia pediátrica.",
    ],
)

# ---------------------------------------------------------------------------
# Medicina esportiva
# ---------------------------------------------------------------------------
escrever(
    "medicina-esportiva-curitiba.html",
    title="Médico do esporte em Curitiba: quando procurar",
    description="Medicina esportiva em Curitiba: lesões por sobrecarga, lesão muscular, retorno seguro ao esporte e o que a evidência mostra sobre prevenção de lesões.",
    h1="Medicina esportiva e lesões do esporte em Curitiba",
    lead="Aqui estão as fichas dos médicos do esporte de Curitiba. Logo abaixo delas vem o guia: lesão por sobrecarga, o que realmente previne e por que o retorno ao esporte se decide por teste, não por calendário.",
    crumbs=CRUMB,
    lista={"titulo": "Médicos do esporte em Curitiba",
           "texto": "Medicina do esporte é uma especialidade própria e também uma área de atuação de outras especialidades, incluindo a ortopedia.", "area": "Medicina do esporte", "n": 3},
    banda={"titulo": "Quer achar o especialista da sua lesão?",
           "texto": "A busca por área leva direto para a página do joelho, do ombro, do tornozelo ou da coluna."},
    secoes=[
        {"id": "quem-e", "titulo": "Médico do esporte e ortopedista do esporte", "html": """
    <p>Duas figuras diferentes que se sobrepõem bastante. O <strong>médico do esporte</strong> tem formação voltada ao atleta como um todo: avaliação pré-participação, carga de treino, saúde cardiovascular no exercício, nutrição esportiva em conjunto com outros profissionais, e o tratamento não cirúrgico das lesões. O <strong>ortopedista com atuação em esporte</strong> vem da ortopedia e concentra a prática nas lesões do aparelho locomotor, incluindo as cirúrgicas, como ligamento cruzado, menisco, instabilidade de ombro e lesões de tornozelo.</p>
    <p>Na prática, a escolha depende da queixa. Lesão aguda com estalo, inchaço rápido e falseio tende a ser caso do ortopedista. Dor recorrente ligada a treino, retorno mal planejado e cansaço que não passa tendem a ser caso do médico do esporte. Os dois conversam com fisioterapia e preparação física, e o resultado depende muito dessa conversa.</p>
"""},
        {"id": "sobrecarga", "titulo": "Lesão por sobrecarga: a matemática da dose", "html": """
    <p>A maior parte das lesões de quem pratica esporte por prazer não vem de uma pancada. Vem de um aumento de carga que o tecido não teve tempo de acompanhar. Tendão, osso e músculo se adaptam ao estímulo, mas em velocidades diferentes, e o tendão é lento.</p>
    <p>Isso explica um padrão que se repete no consultório: a pessoa passa meses sem treinar, se anima em janeiro, dobra o volume em duas semanas e aparece com dor no joelho, no Aquiles ou na canela. O tecido não falhou por fraqueza, falhou por pressa.</p>
    <p>A recomendação prática mais conhecida é aumentar o volume de treino de forma gradual, na casa de cerca de 10% por semana. É importante dizer com honestidade que essa regra é um guia prático, e não uma lei com respaldo forte de ensaios clínicos: revisões que testaram a regra dos 10% não confirmaram um limiar mágico. O princípio que sobrevive é outro, e esse tem respaldo: mudanças bruscas de carga, principalmente depois de períodos parados, aumentam o risco, e progressão gradual com semanas mais leves espalhadas ao longo do plano reduz problemas.</p>
    <div class="callout info">
      <h3>Sinais de que a dose passou do ponto</h3>
      <ul>
        <li>Dor que aparece mais cedo a cada treino.</li>
        <li>Dor que continua no dia seguinte, ou que piora à noite.</li>
        <li>Rigidez matinal na região que treina.</li>
        <li>Queda de desempenho com sono ruim e irritabilidade.</li>
      </ul>
      <p>Dor leve que melhora durante o aquecimento e não piora no dia seguinte costuma permitir continuar treinando com carga ajustada, sob orientação.</p>
    </div>
"""},
        {"id": "lesao-muscular", "titulo": "Lesão muscular e o que fazer nas primeiras horas", "html": """
    <p>A lesão muscular clássica acontece em movimentos rápidos, com o músculo sendo alongado sob tensão, como no sprint e na finalização. O posterior da coxa é o campeão, seguido de panturrilha, adutor e reto femoral.</p>
    <p>O antigo protocolo de gelo, repouso, compressão e elevação foi revisto. As recomendações atuais enfatizam <strong>proteger sem imobilizar, evitar repouso prolongado, carregar o tecido progressivamente e retomar movimento cedo</strong>, dentro do tolerável. O gelo pode aliviar a dor, mas não existe boa evidência de que acelere a recuperação, e o uso prolongado de anti-inflamatórios logo após a lesão é questionado justamente porque a inflamação faz parte do reparo.</p>
    <p>Sobre prazos, honestidade: o tempo de retorno varia muito conforme o músculo, a extensão e a localização da lesão, sendo que lesões próximas ao tendão costumam demorar mais e recidivar mais. Prometer prazo exato na primeira semana é chute.</p>
"""},
        {"id": "prevencao", "titulo": "O que realmente previne lesão", "html": """
    <p>Aqui a evidência é boa, e as intervenções são baratas.</p>
    <ul>
      <li><strong>Programas neuromusculares de aquecimento</strong>, com fortalecimento, equilíbrio, controle de aterrissagem e mudança de direção, reduzem lesões de forma consistente em esportes coletivos, com efeitos relevantes sobre lesões de joelho e de tornozelo.</li>
      <li><strong>Exercício nórdico para posteriores de coxa.</strong> Programas que incluem esse exercício reduzem de forma expressiva as lesões de isquiotibiais em jogadores de futebol, com uma das melhores relações entre esforço e retorno em toda a medicina esportiva.</li>
      <li><strong>Treino de equilíbrio</strong> reduz recidiva de entorse de tornozelo.</li>
      <li><strong>Força.</strong> Musculatura mais forte tolera mais carga, e treino de força é fator protetor amplo, inclusive para lesões por sobrecarga.</li>
      <li><strong>Sono e recuperação.</strong> Sono insuficiente está associado a maior risco de lesão, e é a variável mais negligenciada por quem treina.</li>
    </ul>
    <p>E o que não sustenta o que promete: alongamento estático imediatamente antes do exercício não reduz risco de lesão de forma consistente, e pode reduzir desempenho de força se feito por tempo prolongado. Kinesio tape tem efeito modesto e provavelmente ligado à percepção. Suplementos que prometem proteger articulação não têm respaldo à altura da propaganda.</p>
"""},
        {"id": "retorno", "titulo": "Retorno ao esporte se decide por teste, não por calendário", "html": """
    <p>Perguntar quando volto é natural, mas a pergunta certa é o que preciso mostrar para voltar. Depois de lesões importantes, principalmente ligamento cruzado anterior, os critérios funcionais mudaram o jogo: força simétrica entre os lados, testes de salto com desempenho próximo ao do lado saudável, controle de movimento adequado e confiança psicológica para a modalidade.</p>
    <p>Voltar antes de atingir esses critérios aumenta o risco de nova lesão, e isso está bem documentado em atletas jovens. É também por isso que a reabilitação depois de reconstrução ligamentar não termina quando a dor acaba: ela termina quando o desempenho volta.</p>
    <p>Uma consequência prática para quem joga por prazer: se você não fizer a reabilitação, o resultado da cirurgia fica abaixo do que ela poderia entregar. Cirurgia é uma parte do tratamento, e não o tratamento inteiro.</p>
"""},
        {"id": "quando-procurar", "titulo": "Quando procurar atendimento", "html": """
    <p>Marque consulta quando a dor persiste por mais de duas a três semanas apesar do ajuste de carga, quando a mesma lesão se repete, quando existe inchaço depois dos treinos, quando o membro falha ou trava, ou quando você quer voltar a treinar depois de uma lesão importante e não sabe como progredir com segurança.</p>
""" + alerta("Interrompa e procure atendimento imediato se houver", [
            "Estalo audível com inchaço imediato e incapacidade de continuar.",
            "Impossibilidade de apoiar o peso, deformidade ou articulação fora do lugar.",
            "Dor no peito, falta de ar desproporcional, tontura ou desmaio durante o exercício.",
            "Dor muscular intensa com urina escura depois de treino extenuante, o que pode indicar rabdomiólise.",
            "Dor em uma perna com inchaço e vermelhidão em repouso, principalmente após viagem longa ou imobilização.",
            "Confusão, dor de cabeça persistente ou perda de memória depois de pancada na cabeça."])},
    ],
    faq=[
        ("Posso treinar sentindo dor?",
         "Depende do tipo de dor. Dor leve, que melhora durante o aquecimento, não piora no dia seguinte e não vem acompanhada de inchaço, costuma permitir treino com carga ajustada e acompanhamento. Dor que aumenta ao longo do treino, que persiste no dia seguinte, que causa manqueira ou que vem com inchaço pede pausa e avaliação."),
        ("Alongar antes do treino previne lesão?",
         "O alongamento estático feito imediatamente antes do exercício não mostrou redução consistente de lesões e, quando prolongado, pode reduzir desempenho de força. O que tem evidência é o aquecimento ativo com componente neuromuscular, incluindo força, equilíbrio e controle de movimento, feito de forma regular ao longo da temporada."),
        ("Qual o melhor exercício para evitar lesão de posterior de coxa?",
         "Programas que incluem o exercício nórdico para isquiotibiais reduzem de forma expressiva essas lesões em jogadores de futebol. É um exercício simples, feito em dupla ou com apoio, que exige poucos minutos por sessão e algumas sessões por semana. A dificuldade é adesão, e não custo."),
        ("Preciso fazer ressonância antes de voltar a correr?",
         "Quase nunca. A decisão de retorno se baseia em avaliação clínica, evolução da dor e desempenho em testes funcionais. Imagem entra quando há suspeita de lesão estrutural que muda a conduta, como fratura por estresse, lesão ligamentar ou lesão tendínea importante. Pedir exame por ansiedade costuma gerar achados que confundem."),
        ("Quanto tempo até voltar ao esporte depois de reconstruir o ligamento cruzado?",
         "Não existe um número que sirva para todo mundo, e prazo isolado é um critério ruim. O retorno a esportes com giro e mudança de direção costuma levar vários meses e depende de recuperar força simétrica, desempenho em testes de salto, controle de movimento e confiança. Voltar sem cumprir esses critérios aumenta o risco de nova lesão."),
    ],
    takeaways=[
        "A maior parte das lesões recreativas é erro de dose, não falta de preparo.",
        "A regra dos 10% é um guia prático, não uma lei, mas evitar saltos bruscos de carga tem respaldo.",
        "O protocolo antigo de gelo e repouso deu lugar a carga progressiva e movimento precoce.",
        "Programas neuromusculares de aquecimento reduzem lesões de forma consistente.",
        "O exercício nórdico reduz muito as lesões de posterior de coxa.",
        "Retorno ao esporte se decide por testes funcionais, não por calendário.",
        "Sono ruim aumenta risco de lesão, e quase ninguém trata isso como treino.",
    ],
    refs=[
        "Dubois B, Esculier JF. Soft tissue injuries simply need PEACE and LOVE. British Journal of Sports Medicine, 2020.",
        "Lauersen JB et al. The effectiveness of exercise interventions to prevent sports injuries: systematic review and meta-analysis. British Journal of Sports Medicine, 2014.",
        "van Dyk N et al. Including the Nordic hamstring exercise in injury prevention programmes halves the rate of hamstring injuries. British Journal of Sports Medicine, 2019.",
        "Nielsen RO et al. Training load and running-related injury: a systematic review. Journal of Orthopaedic and Sports Physical Therapy.",
        "Grindem H et al. Simple decision rules can reduce reinjury risk by 84% after ACL reconstruction. British Journal of Sports Medicine, 2016.",
        "Vuurberg G et al. Diagnosis, treatment and prevention of ankle sprains. British Journal of Sports Medicine, 2018.",
    ],
)

print("páginas geradas: ortopedia infantil, medicina esportiva")
