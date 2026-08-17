#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Artigos de captura: custo, SUS, primeira consulta, especialidades e escolha do profissional."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from page_builder import escrever

BANDA = {"titulo": "Já sabe qual área você precisa?",
         "texto": "A busca por área mostra qual ortopedista cuida da parte do corpo que está doendo."}

# ---------------------------------------------------------------------------
# 1. Quanto custa
# ---------------------------------------------------------------------------
escrever(
    "quanto-custa-consulta-ortopedista-curitiba.html",
    title="Quanto custa consulta com ortopedista em Curitiba",
    description="Como funcionam os custos da ortopedia em Curitiba pelo SUS, pelo convênio e no particular, o que perguntar antes de marcar e como evitar surpresas.",
    h1="Quanto custa uma consulta com ortopedista em Curitiba",
    lead="Não existe tabela única, e qualquer site que anuncie um valor exato está chutando ou fazendo propaganda. O que existe é uma lógica de formação de preço, um conjunto de perguntas que evita surpresa e alguns direitos que pouca gente usa. É disso que trata esta página.",
    pill="Guia de acesso",
    tipo="WebPage",
    banda=BANDA,
    secoes=[
        {"id": "tres-caminhos", "titulo": "Os três caminhos e o que cada um custa", "html": """
    <p><strong>Pelo SUS, o custo é zero.</strong> Consulta, exames e cirurgia são gratuitos, incluindo material. O preço que se paga é tempo de espera, e o caminho começa na unidade básica de saúde do seu endereço. O passo a passo está no guia sobre <a href="ortopedista-sus-curitiba.html">ortopedista pelo SUS em Curitiba</a>.</p>
    <p><strong>Pelo convênio, o custo é a coparticipação, quando o seu plano tem.</strong> Ela varia conforme o contrato e costuma ser um valor fixo por consulta ou um percentual. Vale conferir no aplicativo do plano antes de marcar, porque a coparticipação de consulta e a de exame são diferentes.</p>
    <p><strong>No particular, o valor é livre.</strong> Cada consultório define o seu, e a variação dentro de Curitiba é grande. Ela depende da região da cidade, da estrutura, do tempo reservado por paciente, da subespecialidade e de o profissional atender ou não convênios. Por isso não publicamos uma faixa fechada: qualquer número aqui envelheceria rápido e induziria você a comparar coisas diferentes.</p>
    <div class="callout info">
      <h3>Existe tabela de referência?</h3>
      <p>Existe uma tabela de referência de honorários publicada por entidades médicas, usada principalmente em negociação com planos de saúde e como parâmetro de reembolso. Ela não obriga nenhum consultório particular a cobrar aquele valor, e não serve como tabela de preço ao público. Serve para você entender que o valor tem uma referência técnica por trás, e não é arbitrário.</p>
    </div>
"""},
        {"id": "o-que-perguntar", "titulo": "O que perguntar antes de marcar", "html": """
    <p>Esta lista resolve quase todos os problemas de expectativa. Faça as perguntas por telefone ou mensagem, nesta ordem.</p>
    <ol class="steps">
      <li><b>Qual o valor da consulta e a forma de pagamento</b><span>Pergunte também se há diferença de valor entre primeira consulta e retorno.</span></li>
      <li><b>Qual o prazo de retorno sem custo</b><span>Esta é a pergunta que mais economiza dinheiro em ortopedia. É comum a consulta terminar com pedido de exame, e o retorno para avaliar o resultado é parte do mesmo atendimento. Prazos de 15 a 30 dias são comuns, mas variam bastante.</span></li>
      <li><b>Se procedimentos de consultório são cobrados à parte</b><span>Infiltração, punção, imobilização e retirada de pontos podem ter cobrança própria.</span></li>
      <li><b>Se o consultório emite recibo e relatório para reembolso</b><span>Se você tem plano com reembolso, peça o documento com CRM, CPF, código do procedimento e data. Sem isso, o reembolso trava.</span></li>
      <li><b>Se o profissional atende o seu convênio naquele endereço</b><span>Muitos médicos atendem determinado plano em um consultório e não em outro. Confirme com a clínica, e não apenas no buscador do plano, que costuma estar desatualizado.</span></li>
    </ol>
"""},
        {"id": "exames-e-cirurgia", "titulo": "Exames, procedimentos e cirurgia", "html": """
    <p><strong>Exames.</strong> Radiografia é o exame mais barato e resolve boa parte das dúvidas iniciais. Ultrassonografia é intermediária. Ressonância é o exame caro do grupo, e por isso vale lembrar que ela raramente deve ser feita antes da consulta: pedida sem hipótese clínica, costuma gerar achados que assustam e não mudam a conduta.</p>
    <p><strong>Procedimentos de consultório.</strong> Infiltrações e punções têm custo próprio, que muda conforme o material usado. Vale perguntar se o valor inclui o medicamento.</p>
    <p><strong>Cirurgia.</strong> No particular, o orçamento tem quatro componentes que costumam ser cotados separadamente: honorário da equipe cirúrgica, honorário do anestesista, taxas hospitalares e materiais e implantes. Peça o orçamento discriminado, com validade e com previsão de dias de internação. No convênio, a cobertura segue o rol da ANS e a autorização é solicitada pelo médico, com prazos regulados. Se houver negativa, ela deve ser fundamentada e por escrito, e pode ser questionada.</p>
    <div class="callout accent">
      <h3>Uma regra simples contra surpresa</h3>
      <p>Nunca aceite orçamento cirúrgico apenas verbal, e desconfie de proposta com desconto por decisão imediata. Em medicina, pressa comercial e boa indicação raramente andam juntas.</p>
    </div>
"""},
        {"id": "reembolso", "titulo": "Reembolso, imposto de renda e coparticipação", "html": """
    <p><strong>Reembolso.</strong> Planos com essa modalidade devolvem parte do valor pago, conforme o contrato. O cálculo raramente é integral. Guarde recibo, relatório e comprovante de pagamento, e envie pelo aplicativo do plano, que costuma ser mais rápido que outros canais.</p>
    <p><strong>Imposto de renda.</strong> Despesas médicas com você e com dependentes são dedutíveis na declaração completa, desde que comprovadas por documento com nome e CPF do prestador e do paciente. Guardar recibo tem valor prático de verdade.</p>
    <p><strong>Coparticipação.</strong> Ela existe para reduzir a mensalidade e é cobrada por uso. Se o seu plano tem, o custo de acompanhar um tratamento longo com muitos retornos deixa de ser desprezível, e isso deve entrar na conta ao escolher entre convênio e particular.</p>
"""},
        {"id": "vale-a-pena", "titulo": "Como decidir entre SUS, convênio e particular", "html": """
    <p>Não existe resposta única, mas existem critérios objetivos.</p>
    <ul>
      <li><strong>Urgência do quadro.</strong> Trauma e sinais de alarme não escolhem via: vão para a urgência, que é gratuita no SUS e disponível em qualquer porta.</li>
      <li><strong>Necessidade de continuidade.</strong> Problemas crônicos exigem vários retornos. Aí o valor do retorno pesa mais que o da primeira consulta.</li>
      <li><strong>Necessidade de cirurgia.</strong> Se a cirurgia é provável, entender desde já como ela será custeada evita começar um caminho e ter que recomeçar em outro.</li>
      <li><strong>Tempo.</strong> Pelo SUS, a espera para consulta eletiva pode ser longa. Para quem tem dor incapacitante e alguma reserva financeira, uma consulta particular inicial pode acelerar o diagnóstico, e o tratamento pode seguir pela rede pública.</li>
    </ul>
    <p>Uma combinação usada com frequência e perfeitamente legítima é fazer a avaliação inicial no particular, entender o problema, e conduzir exames e tratamento pelo SUS ou pelo convênio, levando o relatório do médico.</p>
"""},
    ],
    faq=[
        ("Qual o valor médio de uma consulta particular de ortopedia em Curitiba?",
         "Não publicamos um valor porque não existe tabela única e a variação é grande dentro da própria cidade, conforme região, estrutura do consultório, subespecialidade e tempo de consulta. Qualquer número divulgado como média envelhece rápido e faz você comparar serviços diferentes. O caminho confiável é perguntar diretamente ao consultório, junto com a política de retorno."),
        ("O retorno com o ortopedista é cobrado?",
         "Depende do consultório. É comum haver um prazo em que o retorno para avaliação de exames está incluído na consulta inicial, com valores e prazos que variam bastante. Como em ortopedia o retorno é quase sempre necessário, essa informação muda o custo real do tratamento e deve ser perguntada antes de marcar."),
        ("Plano de saúde é obrigado a cobrir cirurgia ortopédica e o material?",
         "Procedimentos previstos na cobertura obrigatória definida pela ANS devem ser cobertos, incluindo materiais necessários à sua realização, conforme as regras vigentes e o contrato. Negativas devem ser fundamentadas e informadas por escrito quando solicitadas, e podem ser questionadas junto à operadora, à ANS e, se necessário, pela via judicial."),
        ("Consulta pelo SUS é gratuita mesmo?",
         "Sim. Consulta, exames, cirurgia, materiais e internação pelo SUS são gratuitos. Não existe cobrança legítima por atendimento no sistema público, e qualquer cobrança nesse contexto deve ser denunciada à ouvidoria."),
        ("Posso deduzir a consulta no imposto de renda?",
         "Despesas médicas com o contribuinte e com seus dependentes são dedutíveis na declaração completa, desde que comprovadas com documento contendo nome, CPF e CRM do profissional, além dos dados do paciente. Guarde recibos e relatórios, inclusive os de fisioterapia e exames."),
    ],
    takeaways=[
        "Pelo SUS o custo é zero, e o que se paga é tempo de espera.",
        "No particular o valor é livre e varia muito dentro de Curitiba, por isso não existe média confiável.",
        "A pergunta que mais economiza é a do prazo de retorno sem custo.",
        "Ressonância pedida antes da consulta costuma custar caro e mudar pouco.",
        "Orçamento cirúrgico deve ser discriminado e por escrito.",
        "Negativa de cobertura pelo plano deve ser fundamentada e pode ser contestada.",
        "Avaliar no particular e tratar pelo SUS ou pelo convênio é uma combinação legítima e comum.",
    ],
    refs=[
        "Agência Nacional de Saúde Suplementar. Cobertura assistencial, rol de procedimentos e prazos máximos de atendimento. gov.br/ans.",
        "Associação Médica Brasileira. Classificação Brasileira Hierarquizada de Procedimentos Médicos, referência de honorários.",
        "Ministério da Saúde. Princípios do SUS e gratuidade do atendimento.",
        "Receita Federal do Brasil. Perguntas e respostas sobre dedução de despesas médicas no imposto de renda.",
        "Conselho Federal de Medicina. Resolução CFM nº 2.336/2023, sobre publicidade e divulgação de preços.",
    ],
)

# ---------------------------------------------------------------------------
# 2. SUS
# ---------------------------------------------------------------------------
escrever(
    "ortopedista-sus-curitiba.html",
    title="Ortopedista pelo SUS em Curitiba: como conseguir",
    description="O caminho para conseguir consulta com ortopedista pelo SUS em Curitiba, o que levar na unidade de saúde, como acompanhar a fila e o que fazer em urgência.",
    h1="Ortopedista pelo SUS em Curitiba: o caminho completo",
    lead="Muita gente perde meses porque tenta entrar pela porta errada. O acesso ao ortopedista na rede pública tem um caminho definido, alguns atalhos legítimos e vários pontos onde a fila trava por motivos evitáveis, como telefone desatualizado. Este guia mostra tudo isso em ordem.",
    pill="Guia de acesso",
    tipo="WebPage",
    banda=BANDA,
    secoes=[
        {"id": "caminho", "titulo": "O caminho, passo a passo", "html": """
    <ol class="steps">
      <li><b>Procure a unidade básica de saúde do seu endereço</b><span>É a porta de entrada do sistema. Leve documento com foto, comprovante de residência e o Cartão Nacional de Saúde. Se ainda não tiver o cartão, ele é feito na própria unidade.</span></li>
      <li><b>Passe pela avaliação</b><span>O profissional examina, trata o que pode ser tratado ali, solicita exames iniciais quando necessário e decide se há indicação de encaminhamento. Boa parte das queixas ortopédicas comuns é resolvida nessa etapa, com medicação e fisioterapia.</span></li>
      <li><b>O encaminhamento entra no sistema de regulação</b><span>Não é a unidade que marca diretamente com o especialista. O pedido entra em um sistema que organiza a fila conforme critérios clínicos de prioridade e ordem de espera.</span></li>
      <li><b>Aguarde a convocação e mantenha o contato atualizado</b><span>O aviso costuma vir pela própria unidade, por telefone ou por convocação. Telefone desatualizado é uma das maiores causas de perda de vaga.</span></li>
      <li><b>Compareça, e avise se não puder ir</b><span>Falta sem aviso desperdiça a vaga e joga você para o fim do processo. Se não puder comparecer, avise com antecedência para remarcar.</span></li>
    </ol>
"""},
        {"id": "acelerar", "titulo": "O que ajuda a andar mais rápido, de forma legítima", "html": """
    <ul>
      <li><strong>Chegar com a história organizada.</strong> Anote quando começou, o que piora, o que já tentou, quais medicamentos usa e quais exames já fez. Encaminhamento bem preenchido, com descrição clínica e exames anexados, é classificado com mais precisão.</li>
      <li><strong>Levar exames anteriores.</strong> Radiografias antigas, laudos e relatórios evitam repetição e podem elevar a prioridade quando mostram algo relevante.</li>
      <li><strong>Manter cadastro e telefone atualizados</strong> na unidade, inclusive um segundo número de contato.</li>
      <li><strong>Perguntar sobre a fisioterapia enquanto espera.</strong> Em muitos casos ortopédicos, a fisioterapia é o tratamento principal e não depende do especialista para começar.</li>
      <li><strong>Acompanhar a posição na fila.</strong> A Secretaria de Estado da Saúde do Paraná disponibiliza consulta on-line de posição na fila para procedimentos regulados pelo estado.</li>
      <li><strong>Usar a ouvidoria quando algo travar.</strong> A ouvidoria do SUS atende pelo telefone 136 e também há canais municipais. Registrar demanda é um direito e costuma destravar situações paradas.</li>
    </ul>
    <div class="callout info">
      <h3>O que não ajuda</h3>
      <p>Ir direto a um hospital para tentar consulta eletiva, procurar pronto atendimento por queixa crônica sem sinal de alarme, ou tentar marcar diretamente com o especialista sem encaminhamento. Nenhum desses caminhos encurta a fila e todos consomem seu tempo e o do serviço.</p>
    </div>
"""},
        {"id": "urgencia", "titulo": "Quando não é fila, é urgência", "html": """
    <p>Situações agudas não passam pela regulação eletiva. Vão para a rede de urgência, que em Curitiba inclui unidades de pronto atendimento e serviços hospitalares de referência em trauma, entre eles o Complexo Hospitalar do Trabalhador, referência estadual em urgência e trauma.</p>
    <div class="callout alert">
      <h3>Procure a urgência, e não a fila, se houver</h3>
      <ul>
        <li>Fratura suspeita, deformidade do membro, ou impossibilidade de apoiar o peso depois de trauma.</li>
        <li>Articulação quente, vermelha e muito dolorida, com febre.</li>
        <li>Perda de força progressiva, dormência em sela, ou perda de controle da urina ou das fezes.</li>
        <li>Membro frio, pálido ou roxo.</li>
        <li>Ferimento profundo, osso exposto ou perda de movimento de um dedo após corte.</li>
        <li>Criança que se recusa a andar, principalmente com febre.</li>
      </ul>
      <p>Em emergência, ligue 192.</p>
    </div>
"""},
        {"id": "direitos", "titulo": "Seus direitos, em linguagem simples", "html": """
    <ul>
      <li><strong>Atendimento gratuito.</strong> Não existe cobrança legítima por consulta, exame, cirurgia ou material no SUS.</li>
      <li><strong>Informação.</strong> Você tem direito a saber o seu diagnóstico, as alternativas de tratamento e os riscos, em linguagem que entenda, e a receber relatório e cópia de exames.</li>
      <li><strong>Acompanhante.</strong> Idosos, crianças, adolescentes e pessoas com deficiência têm direito a acompanhante.</li>
      <li><strong>Prioridade.</strong> Pessoas com 60 anos ou mais, gestantes, lactantes, pessoas com crianças de colo e pessoas com deficiência têm atendimento prioritário, e a prioridade é maior a partir dos 80 anos.</li>
      <li><strong>Reclamar sem prejuízo.</strong> Registrar demanda na ouvidoria é um direito e não pode gerar retaliação.</li>
    </ul>
"""},
        {"id": "enquanto-espera", "titulo": "O que fazer enquanto espera", "html": """
    <p>Esperar não significa ficar parado, e em ortopedia isso é literal. Na maior parte das dores crônicas do aparelho locomotor, o que muda o rumo é movimento orientado, e não a consulta em si.</p>
    <ul>
      <li>Pergunte na unidade sobre fisioterapia, grupos de atividade física e programas de exercício.</li>
      <li>Mantenha atividade dentro do que a dor permite. Repouso prolongado piora dor lombar e piora artrose.</li>
      <li>Controle peso, sono e outras doenças, como diabetes, que influenciam diretamente a evolução.</li>
      <li>Leia sobre o seu problema para chegar à consulta com perguntas objetivas. Cada área tem uma página aqui, e você chega nelas pela <a href="encontre-um-ortopedista.html">busca por área</a>.</li>
      <li>Volte à unidade se algo mudar. Piora significativa muda a classificação de prioridade.</li>
    </ul>
"""},
    ],
    faq=[
        ("Posso marcar direto com o ortopedista pelo SUS?",
         "Não. O acesso à ortopedia eletiva passa pela unidade básica de saúde do seu endereço, que avalia e insere o encaminhamento no sistema de regulação. Esse fluxo existe para que os casos mais graves sejam vistos primeiro e para que problemas resolvíveis na atenção primária não ocupem a fila do especialista."),
        ("Quanto tempo demora a fila da ortopedia em Curitiba?",
         "Varia conforme a prioridade clínica e a demanda do momento, e a ortopedia está entre as especialidades mais procuradas, com esperas que podem se estender por meses nos casos eletivos. Casos classificados como mais graves são atendidos antes, e situações agudas não entram nessa fila, porque vão para a rede de urgência."),
        ("Como sei em que posição estou na fila?",
         "A Secretaria de Estado da Saúde do Paraná mantém um serviço on-line de consulta de posição na fila para procedimentos regulados pelo estado. Também é possível perguntar na unidade de saúde onde o encaminhamento foi feito e registrar demanda na ouvidoria do SUS, pelo telefone 136."),
        ("Perdi a consulta que marcaram para mim. Volto para o fim da fila?",
         "Faltar sem avisar costuma significar perder a vaga e precisar de nova solicitação, o que atrasa bastante. Se você não puder comparecer, avise a unidade com antecedência para remarcar. É por isso também que manter o telefone atualizado é tão importante: muita convocação se perde por contato desatualizado."),
        ("Fiz consulta particular. Posso fazer a cirurgia pelo SUS?",
         "Sim. Você pode levar o relatório do médico particular à unidade de saúde e seguir o fluxo público. A avaliação e a indicação serão refeitas pelo serviço que vai operar, o que é normal, mas o relatório e os exames ajudam a organizar o encaminhamento e evitam repetir etapas."),
        ("Preciso pagar alguma coisa em atendimento pelo SUS?",
         "Não. Consulta, exames, cirurgia, materiais e internação são gratuitos no SUS. Qualquer cobrança nesse contexto é irregular e deve ser comunicada à ouvidoria."),
    ],
    takeaways=[
        "A porta de entrada é a unidade básica de saúde do seu endereço, não o hospital.",
        "O encaminhamento entra em um sistema de regulação com classificação por prioridade.",
        "Telefone desatualizado é uma das maiores causas de perda de vaga.",
        "Dá para consultar a posição na fila e registrar demanda na ouvidoria pelo 136.",
        "Trauma e sinais de alarme não entram na fila eletiva: vão para a urgência.",
        "Fisioterapia e exercício frequentemente podem começar antes da consulta com o especialista.",
        "Atendimento pelo SUS é gratuito em todas as etapas.",
    ],
    refs=[
        "Prefeitura Municipal de Curitiba, Secretaria Municipal da Saúde. Rede de serviços do SUS e fluxo de consultas e exames especializados.",
        "Secretaria de Estado da Saúde do Paraná. Consulta de posição na fila do SUS.",
        "Ministério da Saúde. Política Nacional de Atenção Básica e Carta dos Direitos dos Usuários da Saúde.",
        "Ouvidoria Geral do SUS. Canal 136.",
        "Complexo Hospitalar do Trabalhador. Pronto-socorro de trauma.",
        "Brasil. Lei nº 10.741/2003, Estatuto da Pessoa Idosa, sobre prioridade de atendimento.",
    ],
)

# ---------------------------------------------------------------------------
# 3. Primeira consulta
# ---------------------------------------------------------------------------
escrever(
    "primeira-consulta-ortopedista.html",
    title="Primeira consulta com ortopedista: o que levar",
    description="Como se preparar para a consulta com o ortopedista: o que levar, como descrever a dor, quais perguntas fazer e o que esperar do exame físico e dos exames.",
    h1="Primeira consulta com o ortopedista: como se preparar",
    lead="Uma consulta de ortopedia dura em média entre vinte e quarenta minutos, e a maior parte do diagnóstico sai da conversa. Chegar preparado não é preciosismo: é a diferença entre sair com um plano claro e sair com mais um pedido de exame.",
    pill="Guia de acesso",
    tipo="WebPage",
    banda=BANDA,
    secoes=[
        {"id": "o-que-levar", "titulo": "O que levar", "html": """
    <ul>
      <li><strong>Documento com foto e carteirinha do convênio</strong>, ou o Cartão Nacional de Saúde no atendimento público.</li>
      <li><strong>Lista dos medicamentos que você usa</strong>, com doses. Vale fotografar as caixas.</li>
      <li><strong>Exames anteriores da região</strong>, com laudo e, se possível, as imagens. Radiografias antigas valem ouro para comparação.</li>
      <li><strong>Relatórios de cirurgias prévias</strong>, principalmente na mesma região.</li>
      <li><strong>Uma anotação curta da história</strong>, do jeito que está descrito na seção seguinte.</li>
      <li><strong>Roupa que permita examinar a região.</strong> Para joelho, short. Para ombro, blusa que descubra o ombro. Examinar por cima da calça jeans não funciona.</li>
      <li><strong>O calçado que você mais usa</strong>, se a queixa é no pé, no joelho ou no quadril. O desgaste da sola conta bastante.</li>
      <li><strong>Acompanhante</strong>, se você é idoso, tem dificuldade de audição ou acha que vai esquecer as orientações. É um direito no caso de pessoas com 60 anos ou mais.</li>
    </ul>
"""},
        {"id": "descrever-a-dor", "titulo": "Como descrever a sua dor em trinta segundos", "html": """
    <p>Existe uma sequência que médicos usam para organizar a história. Se você chegar com ela pronta, ganha tempo de consulta para o que interessa.</p>
    <div class="table-scroll">
      <table>
        <caption class="sr-only">Roteiro para descrever a dor</caption>
        <thead><tr><th scope="col">Pergunta</th><th scope="col">Exemplo de resposta útil</th></tr></thead>
        <tbody>
          <tr><td>Onde exatamente dói?</td><td>Aponte com um dedo, se conseguir. Dor apontada com a mão inteira e dor apontada com um dedo têm significados diferentes.</td></tr>
          <tr><td>Quando começou e como?</td><td>Há três meses, depois de uma torção jogando bola, ou sem motivo aparente.</td></tr>
          <tr><td>O que piora?</td><td>Descer escada, levantar da cadeira, dormir sobre o lado, correr acima de vinte minutos.</td></tr>
          <tr><td>O que melhora?</td><td>Repouso, calor, anti-inflamatório, mudar de posição.</td></tr>
          <tr><td>Como é a dor à noite?</td><td>Dor que acorda a pessoa é um dado importante e muda a investigação.</td></tr>
          <tr><td>Trava, falseia ou incha?</td><td>Esses três verbos são muito informativos em joelho e ombro.</td></tr>
          <tr><td>O que você já tentou?</td><td>Medicações, fisioterapia por quanto tempo, infiltração, repouso.</td></tr>
          <tr><td>O que você precisa voltar a fazer?</td><td>Subir escada em casa, trabalhar em pé oito horas, correr dez quilômetros. Isso muda a indicação.</td></tr>
        </tbody>
      </table>
    </div>
"""},
        {"id": "exame-fisico", "titulo": "O que acontece na consulta", "html": """
    <p><strong>Conversa.</strong> É a parte mais longa e a mais decisiva. A maior parte dos diagnósticos ortopédicos se forma aqui.</p>
    <p><strong>Exame físico.</strong> O médico observa a região, palpa pontos específicos, mede a amplitude de movimento, testa força e faz manobras próprias de cada articulação. Também examina a região vizinha, porque dor no joelho pode vir do quadril e dor no ombro pode vir do pescoço.</p>
    <p><strong>Exames complementares, quando necessários.</strong> Eles entram para confirmar ou descartar uma hipótese que já foi formulada. Não se assuste se a consulta terminar sem pedido de ressonância: em muitos casos ela não mudaria nada, e imagem pedida sem hipótese clínica costuma gerar achados que confundem.</p>
    <p><strong>Plano.</strong> Ao final, você deve sair sabendo o que provavelmente tem, o que vai fazer nas próximas semanas, o que fazer se piorar e quando retornar. Se isso não ficou claro, pergunte antes de sair da sala.</p>
"""},
        {"id": "perguntas-ao-medico", "titulo": "Sete perguntas que valem a consulta", "html": """
    <ol>
      <li>Qual é a hipótese mais provável para o meu caso?</li>
      <li>Esse exame que o senhor está pedindo vai mudar a conduta? De que forma?</li>
      <li>Quais são as alternativas de tratamento, incluindo as que não envolvem cirurgia?</li>
      <li>O que acontece se eu não fizer nada por alguns meses?</li>
      <li>Quanto tempo até eu sentir melhora, e qual melhora é realista?</li>
      <li>Quais sinais devem me fazer procurar atendimento antes do retorno?</li>
      <li>Se for cirurgia, quantas dessas o senhor faz por ano e como é a reabilitação?</li>
    </ol>
    <div class="callout info">
      <h3>Sobre a pergunta número quatro</h3>
      <p>Ela é a mais reveladora de todas. Todo tratamento tem uma alternativa, que é não tratar agora, e um bom médico sabe descrever o que acontece nesse cenário. Quem responde apenas que vai piorar, sem detalhar, está economizando uma informação que é sua.</p>
    </div>
"""},
        {"id": "depois", "titulo": "Depois da consulta", "html": """
    <ul>
      <li>Guarde o relatório, a receita e os pedidos de exame. Fotografe tudo, porque papel se perde.</li>
      <li>Anote a data do retorno e confirme se ele é sem custo dentro de algum prazo.</li>
      <li>Comece o que foi orientado, principalmente a fisioterapia. Tratamento que não é feito não é tratamento.</li>
      <li>Registre a evolução em poucas linhas por semana. No retorno, isso vale mais do que a memória.</li>
      <li>Se a orientação não fez sentido, ou se a proposta é cirúrgica e você ficou em dúvida, buscar uma segunda opinião é legítimo e não ofende ninguém.</li>
    </ul>
"""},
    ],
    faq=[
        ("Preciso levar exame de imagem já feito na primeira consulta?",
         "Se você já tem exames da região, sim, leve com laudo e imagens. Se ainda não tem, não faça por conta própria antes da consulta. O médico decide qual exame realmente responde à dúvida, e exame feito sem hipótese clínica costuma custar caro e mostrar achados que não têm relação com a sua dor."),
        ("Como devo me vestir para a consulta?",
         "Com roupa que permita expor a região a ser examinada. Short para joelho e quadril, blusa que descubra o ombro para queixas do membro superior, e evite roupas justas difíceis de levantar. Se a queixa é no pé ou no joelho, leve o calçado que você mais usa, porque o desgaste da sola dá informação."),
        ("Posso levar acompanhante?",
         "Sim, e em muitos casos é recomendável. Pessoas com 60 anos ou mais têm direito a acompanhante, e para qualquer paciente ter alguém que ajude a lembrar as orientações melhora a adesão ao tratamento. Se for menor de idade, a presença de responsável é necessária."),
        ("O médico não pediu nenhum exame. Isso é normal?",
         "É normal e frequentemente é sinal de boa prática. Grande parte dos diagnósticos ortopédicos se faz com história e exame físico, e nem todo caso precisa de imagem. O exame é indicado quando o resultado pode mudar a conduta, e não como confirmação automática do que já está claro."),
        ("Quanto tempo dura uma consulta de ortopedia?",
         "Costuma variar entre vinte e quarenta minutos na primeira avaliação, dependendo da complexidade e do serviço. Chegar com a história organizada e com os exames em mãos aumenta bastante o aproveitamento desse tempo."),
    ],
    takeaways=[
        "A maior parte do diagnóstico sai da conversa, não da imagem.",
        "Leve documentos, lista de medicamentos, exames com laudo e uma anotação curta da história.",
        "Roupa adequada e o calçado de uso diário mudam a qualidade do exame físico.",
        "Descreva onde dói, o que piora, o que melhora e o que você precisa voltar a fazer.",
        "Pergunte sempre o que acontece se você não fizer nada agora.",
        "Sair da consulta sem pedido de exame pode ser sinal de boa prática.",
        "Segunda opinião antes de cirurgia é legítima e recomendável quando há dúvida.",
    ],
    refs=[
        "Ministério da Saúde. Carta dos Direitos dos Usuários da Saúde.",
        "Brasil. Lei nº 10.741/2003, Estatuto da Pessoa Idosa.",
        "Conselho Federal de Medicina. Código de Ética Médica, Resolução CFM nº 2.217/2018, sobre informação ao paciente.",
        "Culvenor AG et al. Prevalence of knee osteoarthritis features on MRI in asymptomatic uninjured adults. British Journal of Sports Medicine, 2019.",
        "Brinjikji W et al. Imaging features of spinal degeneration in asymptomatic populations. American Journal of Neuroradiology, 2015.",
    ],
)

# ---------------------------------------------------------------------------
# 4. Ortopedista, reumatologista, fisiatra
# ---------------------------------------------------------------------------
escrever(
    "ortopedista-reumatologista-fisiatra.html",
    title="Ortopedista, reumatologista ou fisiatra: quem procurar",
    description="As diferenças entre ortopedista, reumatologista, fisiatra e fisioterapeuta, com uma tabela de sintomas para saber qual profissional procurar primeiro.",
    h1="Ortopedista, reumatologista, fisiatra ou fisioterapeuta",
    lead="Quatro profissionais cuidam de dor no corpo, com formações diferentes e ferramentas diferentes. Escolher errado custa meses. Esta página separa as funções com clareza e mostra, por sintoma, quem tende a resolver o seu caso.",
    pill="Guia de acesso",
    tipo="WebPage",
    banda=BANDA,
    secoes=[
        {"id": "quem-e-quem", "titulo": "Quem é quem", "html": """
    <div class="table-scroll">
      <table>
        <caption class="sr-only">Comparação entre as especialidades que tratam dor musculoesquelética</caption>
        <thead><tr><th scope="col">Profissional</th><th scope="col">Formação</th><th scope="col">Cuida principalmente de</th><th scope="col">Ferramentas</th></tr></thead>
        <tbody>
          <tr>
            <th scope="row">Ortopedista</th>
            <td>Médico, residência em ortopedia e traumatologia</td>
            <td>Problemas mecânicos e estruturais: fraturas, lesões de tendões e ligamentos, artrose, deformidades</td>
            <td>Diagnóstico, medicação, infiltração, imobilização, cirurgia</td>
          </tr>
          <tr>
            <th scope="row">Reumatologista</th>
            <td>Médico, residência em reumatologia</td>
            <td>Doenças inflamatórias e autoimunes: artrite reumatoide, lúpus, espondiloartrites, gota, além de osteoporose e fibromialgia</td>
            <td>Diagnóstico, exames laboratoriais, medicações que modificam a doença, imunobiológicos</td>
          </tr>
          <tr>
            <th scope="row">Fisiatra</th>
            <td>Médico, residência em medicina física e reabilitação</td>
            <td>Função e reabilitação: dor crônica, sequelas de AVC e de trauma, espasticidade, próteses e órteses</td>
            <td>Programas de reabilitação, medicação, procedimentos guiados, coordenação de equipe</td>
          </tr>
          <tr>
            <th scope="row">Fisioterapeuta</th>
            <td>Graduação em fisioterapia, não é médico</td>
            <td>Tratamento por exercício e recursos físicos, reabilitação funcional</td>
            <td>Avaliação funcional, exercício terapêutico, terapia manual, recursos físicos</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p>Existe sobreposição legítima entre eles, e os melhores desfechos costumam vir de trabalho conjunto. Uma pessoa com artrose de joelho, por exemplo, pode ser acompanhada pelo ortopedista, tratar com fisioterapia e, se houver componente inflamatório sistêmico, precisar de avaliação reumatológica.</p>
"""},
        {"id": "por-sintoma", "titulo": "Por sintoma, quem procurar primeiro", "html": """
    <div class="table-scroll">
      <table>
        <caption class="sr-only">Sintomas e profissional indicado</caption>
        <thead><tr><th scope="col">O que você sente</th><th scope="col">Comece por</th></tr></thead>
        <tbody>
          <tr><td>Dor em uma articulação só, ligada a esforço, trauma ou uso</td><td>Ortopedista</td></tr>
          <tr><td>Fratura, entorse, luxação, corte com perda de movimento</td><td>Ortopedista, e em urgência se for agudo</td></tr>
          <tr><td>Dor em várias articulações, com rigidez matinal longa</td><td>Reumatologista</td></tr>
          <tr><td>Inchaço simétrico em mãos e punhos, com cansaço</td><td>Reumatologista</td></tr>
          <tr><td>Crise aguda de dor intensa no dedão do pé, com vermelhidão</td><td>Reumatologista ou clínico, pensando em gota</td></tr>
          <tr><td>Dor difusa pelo corpo, sono ruim, cansaço crônico</td><td>Reumatologista ou clínico</td></tr>
          <tr><td>Dor crônica com perda de função, depois de cirurgia ou AVC</td><td>Fisiatra</td></tr>
          <tr><td>Necessidade de reabilitar movimento e força após diagnóstico feito</td><td>Fisioterapeuta</td></tr>
          <tr><td>Osteoporose e prevenção de fraturas</td><td>Reumatologista, endocrinologista ou clínico, com ortopedista se houver fratura</td></tr>
          <tr><td>Dor nas costas com formigamento na perna</td><td>Ortopedista de coluna, e neurologista se houver déficit progressivo</td></tr>
        </tbody>
      </table>
    </div>
"""},
        {"id": "regra-pratica", "titulo": "Uma regra prática que acerta bastante", "html": """
    <div class="callout accent">
      <h3>Mecânica ou inflamatória?</h3>
      <p><strong>Dor mecânica</strong> piora com o uso e melhora com o repouso, costuma ser de uma articulação, tem relação com movimento específico e rigidez matinal curta, de poucos minutos. Perfil ortopédico.</p>
      <p><strong>Dor inflamatória</strong> é pior de manhã ou depois do repouso, melhora ao se movimentar, tem rigidez matinal prolongada, pode acordar a pessoa na segunda metade da noite e atinge várias articulações. Perfil reumatológico.</p>
    </div>
    <p>Essa distinção não é perfeita, e existem casos que misturam os dois padrões. Mas ela resolve bem a dúvida inicial e evita passar meses na especialidade errada.</p>
"""},
        {"id": "fisioterapia", "titulo": "Sobre ir direto ao fisioterapeuta", "html": """
    <p>O fisioterapeuta é um profissional autônomo, com formação própria, e pode avaliar e tratar sem encaminhamento médico. Em muitas dores musculoesqueléticas comuns, ele é um excelente ponto de partida, e a reabilitação é frequentemente o tratamento principal.</p>
    <p>Ainda assim, vale passar antes pelo médico quando houver trauma importante, febre, perda de força, dormência progressiva, dor que acorda à noite, perda de peso sem explicação, história de câncer, ou quando a dor não melhora depois de algumas semanas de tratamento bem conduzido. Nesses casos, existe algo a descartar antes de tratar apenas os sintomas.</p>
"""},
        {"id": "outros", "titulo": "Outros profissionais que entram na história", "html": """
    <ul>
      <li><strong>Neurologista</strong>, quando há fraqueza progressiva, alteração de sensibilidade que se espalha, alteração de marcha sem dor ou suspeita de doença do sistema nervoso.</li>
      <li><strong>Cirurgião vascular</strong>, quando a dor na perna aparece ao caminhar sempre na mesma distância e melhora ao parar, ou quando há inchaço e dor em uma perna só, de início rápido.</li>
      <li><strong>Médico do esporte</strong>, para lesões ligadas a treino, planejamento de carga e retorno seguro à atividade. Há uma página específica sobre <a href="medicina-esportiva-curitiba.html">medicina esportiva</a>.</li>
      <li><strong>Clínico geral ou médico de família</strong>, que é a melhor porta de entrada quando a queixa é difusa, quando há muitas doenças associadas ou quando você não sabe por onde começar. No SUS, é sempre a primeira parada.</li>
      <li><strong>Terapeuta ocupacional</strong>, importante na reabilitação da mão e nas atividades de vida diária.</li>
    </ul>
"""},
    ],
    faq=[
        ("Qual a diferença entre ortopedista e reumatologista?",
         "O ortopedista é o médico do aparelho locomotor do ponto de vista mecânico e estrutural, e é quem opera quando é necessário: fraturas, lesões de ligamentos e tendões, artrose avançada e deformidades. O reumatologista cuida das doenças inflamatórias e autoimunes que afetam articulações e tecidos conjuntivos, como artrite reumatoide, lúpus, espondiloartrites e gota, e também acompanha osteoporose e fibromialgia."),
        ("O fisiatra opera?",
         "Não. O fisiatra é o médico da reabilitação e trabalha com função, dor e recuperação, usando programas de tratamento, medicação e procedimentos não cirúrgicos, muitas vezes guiados por imagem. Ele coordena equipes com fisioterapia, terapia ocupacional e fonoaudiologia, e é peça central na recuperação de lesões neurológicas e de dor crônica."),
        ("Posso ir ao fisioterapeuta sem passar por médico?",
         "Pode, porque o fisioterapeuta é profissional autônomo e faz sua própria avaliação. O cuidado necessário é com os sinais de alarme: trauma importante, febre, perda de força, dormência progressiva, dor noturna que não alivia, perda de peso ou história de câncer pedem avaliação médica antes, porque existem causas que não são musculoesqueléticas."),
        ("Fibromialgia é caso de ortopedia?",
         "Em geral não. A fibromialgia é uma síndrome de dor difusa crônica, com distúrbio do sono e fadiga, acompanhada tipicamente por reumatologia ou clínica médica, com tratamento que combina exercício, educação, sono e medicação quando indicada. O ortopedista entra apenas se houver um problema estrutural associado."),
        ("Tenho dor em várias articulações. Devo procurar ortopedista?",
         "Provavelmente o reumatologista resolve melhor. Dor em várias articulações ao mesmo tempo, com rigidez matinal prolongada, inchaço simétrico, febre, manchas na pele ou cansaço importante sugere causa inflamatória ou autoimune. O ortopedista costuma ser o caminho quando a dor é de uma articulação só e tem relação clara com uso, esforço ou trauma."),
    ],
    takeaways=[
        "Dor mecânica piora com uso e melhora com repouso: perfil ortopédico.",
        "Dor inflamatória é pior de manhã, melhora ao se mover e atinge várias articulações: perfil reumatológico.",
        "Fisiatra é o médico da reabilitação e da função, e não opera.",
        "Fisioterapeuta pode avaliar sem encaminhamento, com atenção aos sinais de alarme.",
        "Dor na perna ao caminhar sempre na mesma distância pede avaliação vascular.",
        "No SUS, o clínico ou médico de família é sempre a primeira parada.",
    ],
    refs=[
        "Aletaha D, Smolen JS. Diagnosis and management of rheumatoid arthritis: a review. JAMA, 2018.",
        "Sociedade Brasileira de Reumatologia. Informações ao público sobre doenças reumáticas.",
        "Associação Brasileira de Medicina Física e Reabilitação. Atuação do médico fisiatra.",
        "Conselho Federal de Fisioterapia e Terapia Ocupacional. Atribuições do fisioterapeuta.",
        "National Institute for Health and Care Excellence. Low back pain and sciatica in over 16s, NG59.",
    ],
)

# ---------------------------------------------------------------------------
# 5. Como escolher o melhor ortopedista
# ---------------------------------------------------------------------------
escrever(
    "melhor-ortopedista-curitiba.html",
    title="Melhor ortopedista de Curitiba: como escolher bem",
    description="Por que listas de melhores médicos não servem e quais critérios objetivos usar para escolher um bom ortopedista em Curitiba, com um checklist prático.",
    h1="Melhor ortopedista de Curitiba: por que a pergunta certa é outra",
    lead="Digitar melhor ortopedista de Curitiba é o instinto de quem está com dor e quer segurança. O problema é que nenhuma lista de melhores médicos mede o que importa, e ranquear profissionais é vedado pela ética médica. Este guia troca a busca pelo melhor por algo que funciona: critérios objetivos para escolher bem.",
    pill="Guia de escolha",
    tipo="WebPage",
    banda=BANDA,
    secoes=[
        {"id": "por-que-nao", "titulo": "Por que rankings de médicos não servem", "html": """
    <p>Três motivos, e nenhum deles é opinião.</p>
    <ol>
      <li><strong>São vedados.</strong> As normas de publicidade médica do Conselho Federal de Medicina proíbem publicidade comparativa e autopromoção com sugestão de superioridade. Um site que elege o melhor coloca o médico listado em situação delicada perante o conselho.</li>
      <li><strong>Medem a coisa errada.</strong> Notas em plataformas medem simpatia, pontualidade, sala de espera e facilidade de agendamento. Tudo isso importa para a experiência, e nada disso mede indicação cirúrgica correta, técnica ou honestidade sobre alternativas.</li>
      <li><strong>Costumam refletir dinheiro.</strong> Em boa parte dos diretórios comerciais, a posição depende de plano contratado ou de volume de avaliações incentivadas, e não de qualidade técnica.</li>
    </ol>
    <p>Existe ainda um problema de fundo: não existe um melhor ortopedista para todo mundo. Existe o especialista adequado para o seu problema, com registro em dia, acesso viável e comunicação que funciona com você.</p>
"""},
        {"id": "criterios", "titulo": "Os critérios que realmente ajudam", "html": """
    <h3>1. Registro e formação, que dá para verificar de graça</h3>
    <p>Confira o CRM e o RQE na consulta pública do Conselho Federal de Medicina. Leva menos de um minuto e responde se o médico existe, se o registro está ativo e se ele tem especialidade e área de atuação registradas. O passo a passo está no guia sobre <a href="crm-rqe-como-verificar-ortopedista.html">CRM, RQE e como verificar</a>.</p>

    <h3>2. Área de atuação compatível com o seu problema</h3>
    <p>Para queixas comuns, o ortopedista geral resolve muito bem. Quando o caso é cirúrgico, quando já se arrasta há meses ou quando o diagnóstico não fechou, a subespecialidade pesa. Encontre a área certa pela <a href="encontre-um-ortopedista.html">busca por área</a>.</p>

    <h3>3. Volume em cirurgias complexas</h3>
    <p>Para procedimentos de maior porte, existe relação entre volume e desfecho em diversas áreas da cirurgia. Perguntar quantas cirurgias como a sua o profissional faz por ano é legítimo, e um bom cirurgião responde com naturalidade.</p>

    <h3>4. Como ele explica as alternativas</h3>
    <p>Este é o critério mais subestimado, e talvez o mais preditivo de boa prática. Um bom ortopedista descreve o que acontece sem tratar, apresenta a alternativa não cirúrgica com sinceridade, informa taxas de sucesso realistas e não promete resultado. Quem apresenta apenas um caminho está te dando informação incompleta.</p>

    <h3>5. Estrutura e continuidade</h3>
    <p>Onde ele opera, quem faz a reabilitação, como funciona o acompanhamento pós-operatório e como você fala com a equipe se algo der errado. Cirurgia sem plano de reabilitação rende bem menos do que poderia.</p>

    <h3>6. Acesso viável</h3>
    <p>O melhor plano de tratamento é o que você consegue cumprir. Distância, horário, custo do retorno e convênio aceito não são detalhes: são o que determina se você vai completar o tratamento.</p>
"""},
        {"id": "sinais-de-alerta", "titulo": "Sinais de alerta na divulgação", "html": """
    <div class="callout alert">
      <h3>Desconfie quando encontrar</h3>
      <ul>
        <li>Promessa de resultado, cura garantida ou expressões como sem dor desde o primeiro dia.</li>
        <li>Fotos de antes e depois e depoimentos de pacientes usados como propaganda, que são vedados.</li>
        <li>Técnica anunciada como exclusiva, revolucionária ou disponível só naquele consultório.</li>
        <li>Autopromoção comparativa, como o melhor da cidade, o número um ou o mais indicado.</li>
        <li>Preço usado como chamariz, com desconto por decisão imediata.</li>
        <li>Indicação cirúrgica na primeira consulta, sem exame físico cuidadoso e sem discussão de alternativas.</li>
        <li>Diagnóstico fechado apenas pelo laudo, sem examinar você.</li>
      </ul>
    </div>
    <p>Nenhum desses sinais prova má prática isoladamente, mas todos indicam que a comunicação está orientada a vender, e não a informar.</p>
"""},
        {"id": "segunda-opiniao", "titulo": "Segunda opinião: quando e como pedir", "html": """
    <p>Peça segunda opinião sempre que a proposta for uma cirurgia eletiva de porte, quando o tratamento proposto for caro e não coberto, quando você não entendeu o motivo da indicação, ou quando a explicação recebida não bateu com o que você sente.</p>
    <p>Como fazer sem constrangimento: peça cópia do relatório e dos exames, que são seus por direito, e leve tudo ao segundo profissional. Se possível, não conte de saída qual foi a conduta proposta, para não induzir a resposta. Divergência entre dois médicos não significa que um deles seja ruim: em ortopedia existem zonas cinzentas legítimas, e entender por que eles divergem costuma esclarecer mais do que a conduta em si.</p>
    <div class="callout info">
      <h3>Uma pergunta que organiza tudo</h3>
      <p>Se fosse o senhor, ou alguém da sua família, com este exame e esta idade, o que faria e por quê? A resposta mostra raciocínio, e raciocínio é o que você está comprando em uma consulta.</p>
    </div>
"""},
        {"id": "checklist", "titulo": "Checklist final", "html": """
    <div class="callout accent">
      <h3>Antes de marcar</h3>
      <ul>
        <li>CRM ativo, verificado na consulta pública do CFM.</li>
        <li>RQE em ortopedia e traumatologia.</li>
        <li>Área de atuação compatível, se o caso for cirúrgico ou arrastado.</li>
        <li>Convênio e endereço confirmados diretamente com o consultório.</li>
        <li>Política de retorno conhecida.</li>
        <li>Nenhuma promessa de resultado na divulgação.</li>
      </ul>
      <h3>Depois da consulta</h3>
      <ul>
        <li>Você entendeu a hipótese diagnóstica e sabe explicá-la com suas palavras.</li>
        <li>As alternativas não cirúrgicas foram apresentadas.</li>
        <li>Você sabe o que acontece se não tratar agora.</li>
        <li>Você sabe quais sinais exigem atendimento antes do retorno.</li>
        <li>Se houve indicação cirúrgica, você sabe como será a reabilitação.</li>
      </ul>
    </div>
"""},
    ],
    faq=[
        ("Existe um ranking oficial dos melhores ortopedistas de Curitiba?",
         "Não existe, e não poderia existir. As normas de publicidade médica do Conselho Federal de Medicina vedam publicidade comparativa e autopromoção com sugestão de superioridade. Listas de melhores publicadas por sites comerciais costumam refletir plano contratado ou volume de avaliações, e não qualidade técnica."),
        ("Como saber se um ortopedista é bom antes de consultar?",
         "Dá para verificar objetivamente registro ativo, especialidade e área de atuação na consulta pública do Conselho Federal de Medicina, além de confirmar onde ele atende e quais convênios aceita. O restante, que é a qualidade da avaliação, aparece na consulta: um bom profissional examina você, explica as alternativas, informa o que acontece sem tratar e não promete resultado."),
        ("Avaliações de pacientes em sites de agendamento servem para alguma coisa?",
         "Servem para medir experiência, como pontualidade, atendimento da secretaria e clareza percebida. Não servem para medir indicação correta, técnica cirúrgica ou desfecho, que são justamente os fatores mais importantes. Use como informação complementar, nunca como critério principal."),
        ("É correto perguntar ao cirurgião quantas cirurgias como a minha ele faz?",
         "É correto e recomendável. Em procedimentos de maior porte, há relação entre volume e desfecho em diversas áreas da cirurgia, e profissionais experientes respondem essa pergunta com naturalidade. Desconforto com a pergunta já é, por si só, uma informação."),
        ("Pedir segunda opinião ofende o médico?",
         "Não deve ofender, e é prática comum em qualquer sistema de saúde maduro, especialmente antes de cirurgia eletiva. Você tem direito a cópia do relatório e dos exames. Divergência entre dois profissionais costuma refletir zonas cinzentas reais da ortopedia, e entender o motivo da divergência ajuda a decidir melhor."),
    ],
    takeaways=[
        "Não existe melhor ortopedista para todo mundo, existe o adequado para o seu problema.",
        "Rankings de médicos são vedados pela ética médica e medem experiência, não técnica.",
        "CRM e RQE são verificáveis de graça em menos de um minuto.",
        "Volume importa em cirurgias complexas, e perguntar sobre isso é legítimo.",
        "O melhor sinal de boa prática é explicar as alternativas e o cenário sem tratamento.",
        "Promessa de resultado, antes e depois e técnica exclusiva são sinais de alerta.",
        "Segunda opinião antes de cirurgia eletiva é direito seu e prática saudável.",
    ],
    refs=[
        "Conselho Federal de Medicina. Código de Ética Médica, Resolução CFM nº 2.217/2018.",
        "Conselho Federal de Medicina. Resolução CFM nº 2.336/2023, sobre publicidade e propaganda médicas.",
        "Conselho Federal de Medicina. Busca pública de médicos e registro de qualificação de especialista.",
        "Birkmeyer JD et al. Surgeon volume and operative mortality in the United States. New England Journal of Medicine, 2003.",
        "Sociedade Brasileira de Ortopedia e Traumatologia. Título de especialista e áreas de atuação.",
    ],
)

print("artigos gerados: custo, SUS, primeira consulta, especialidades, escolha")
