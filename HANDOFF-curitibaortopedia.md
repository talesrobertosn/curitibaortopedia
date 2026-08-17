# HANDOFF — curitibaortopedia.com.br

Documento de continuidade. Quem abrir um chat novo deve ler este arquivo inteiro antes de produzir qualquer coisa.

Última atualização: 17 de agosto de 2026 (sessão 1, com três rodadas: entrega inicial, revisão de navegação e busca, conclusão do site e a vitrine de ortopedistas, com 22 páginas).

---

## 1. Estado atual

Site estático de SEO local, em português do Brasil, para GitHub Pages, no domínio `curitibaortopedia.com.br`. Gratuito, sem fins comerciais, voltado a pacientes leigos. Duas funções: hub de indicação de ortopedistas por subespecialidade e artigos informativos que capturam a busca de sintoma.

Objetivo declarado: primeira posição do Google para "ortopedista em Curitiba" e variações por subespecialidade.

Etapa 1 (atual): o nome do dono não aparece em lugar nenhum do site. O projeto se apresenta como informativo independente, com autoria institucional. A Etapa 2, com nome, RQE e schema de médico, só acontece quando houver título de especialista, e não deve ser antecipada.

E-mail de contato do projeto, usado em todas as páginas e no schema: `curitibaquadril@gmail.com`, o mesmo do site irmão.

### Páginas publicadas (22)

Camada 1, indicação e áreas:

| Arquivo | Termo-alvo |
|---|---|
| `index.html` | ortopedista em Curitiba, hub com a busca no topo |
| `encontre-um-ortopedista.html` | buscar ortopedista por área |
| `ortopedistas-em-curitiba.html` | ortopedista em Curitiba, pilar com o diretório |
| `ortopedia-geral-curitiba.html` | ortopedista geral Curitiba, a área que cuida de tudo |
| `ortopedista-joelho-curitiba.html` | ortopedista de joelho Curitiba |
| `ortopedista-coluna-curitiba.html` | ortopedista de coluna Curitiba |
| `ortopedista-ombro-curitiba.html` | ortopedista de ombro Curitiba |
| `ortopedista-quadril-curitiba.html` | ortopedista de quadril Curitiba, curta, aponta para o site irmão |
| `ortopedista-mao-curitiba.html` | ortopedista de mão Curitiba |
| `ortopedista-pe-tornozelo-curitiba.html` | ortopedista de pé e tornozelo Curitiba |
| `ortopedista-infantil-curitiba.html` | ortopedista infantil Curitiba |
| `medicina-esportiva-curitiba.html` | médico do esporte Curitiba |

Camada 2, guias que capturam a dúvida:

| Arquivo | Termo-alvo |
|---|---|
| `crm-rqe-como-verificar-ortopedista.html` | CRM, RQE, verificar ortopedista, artigo-assinatura |
| `qual-medico-procurar-para-cada-dor.html` | qual médico procurar para cada dor |
| `melhor-ortopedista-curitiba.html` | melhor ortopedista de Curitiba, atacado pela via honesta |
| `ortopedista-sus-curitiba.html` | ortopedista pelo SUS em Curitiba |
| `quanto-custa-consulta-ortopedista-curitiba.html` | quanto custa consulta com ortopedista |
| `primeira-consulta-ortopedista.html` | o que levar na primeira consulta |
| `ortopedista-reumatologista-fisiatra.html` | diferença entre ortopedista, reumatologista e fisiatra |

Institucionais: `cadastre-se.html`, `sobre.html`, `privacidade.html`.

### Arquivos de infraestrutura no repositório

`CNAME`, `.nojekyll`, `robots.txt`, `sitemap.xml`, `favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `og-image.png`, `styles.css`, `main.js`. Nenhum deles pode ser apagado.

### Fila de conteúdo para as próximas sessões

Não existe mais nenhum item marcado como "em breve": menu, busca e rodapé estão completos. A fila agora é de artigos de sintoma, que servem para pescar busca de cauda longa e empurrar o leitor para a página de área correspondente:

1. Dor no joelho ao descer escada, joelho que estala, joelho inchado.
2. Dor lombar que desce pela perna, dor lombar ao levantar da cama.
3. Dor no ombro ao levantar o braço, dor no ombro ao dormir.
4. Formigamento na mão à noite, dedo que trava.
5. Dor no calcanhar ao levantar, o que fazer depois de torcer o tornozelo.
6. Pronto atendimento ortopédico em Curitiba, quando ir ao pronto-socorro.
7. O que é RQE, residência médica e título de especialista pela SBOT.

Cada artigo novo deve ser criado pelo gerador `page_builder.py`, receber link contextual na página de área correspondente e entrar em `FOOTER_GUIAS_NEW` ou no menu Guias, dentro de `apply_polish.py`.

### A vitrine de ortopedistas, que é o coração do site

Esta é a parte mais importante do projeto e a que mais deve aparecer. A vitrine é uma grade de fichas de profissional, no formato de diretório, que existe mesmo antes de haver qualquer médico cadastrado. Cada ficha em branco mostra a estrutura do que será publicado, com espaço para foto, nome, CRM e RQE, endereço, convênios e contato, e traz o botão "É ortopedista? Apareça aqui".

Onde a vitrine aparece hoje:

- **Home**, logo abaixo dos botões de especialidade, com seis fichas de ortopedia geral. É o bloco `#ortopedistas`.
- **Páginas de área**, imediatamente depois do hero, antes do índice e antes de qualquer texto longo. Essa ordem é deliberada: quem clica em uma especialidade quer ver os profissionais, não ler. O texto da área vem depois das fichas.
- **Página de busca**, abaixo da lista de áreas, com seis fichas.
- **Página pilar**, com seis fichas.
- Cada página de área usa três fichas, já rotuladas com a especialidade daquela página, na seção `#lista`. A página de ortopedia geral e a pilar usam seis.

Como o código funciona:

- `vitrine(area, n, titulo, intro, rodape)` em `page_builder.py` gera a grade inteira. As páginas geradas recebem isso automaticamente pelo parâmetro `lista={"titulo":..., "area":..., "n":...}`.
- `ficha(nome, registro, area, endereco, contato, convenios, site)` gera a ficha de um profissional real, no mesmo componente visual. Para publicar um médico, basta substituir uma das fichas em branco pela saída de `ficha(...)` e rodar o QA.
- O CSS dos dois estados é o mesmo bloco `.vcard`, com a variante `.preenchida`.

Gratuidade: ela precisa estar visível em todo lugar onde a vitrine aparece. Hoje aparece no selo verde-cobre ao lado do título, na frase de abertura, no rodapé de cada ficha e na faixa laranja com o botão. Não remova nenhum desses pontos.

Regras que não mudam ao preencher:

1. Só entra com autorização expressa registrada por e-mail, e apenas os campos previstos em `cadastre-se.html`.
2. A ordem é alfabética dentro de cada área. Nenhuma ficha recebe destaque, nota, estrela ou posição paga.
3. Antes de publicar, confira CRM e RQE na consulta pública do CFM.
4. Só depois de existirem profissionais reais e autorizados é que se pode adicionar `ItemList` com itens `Physician` no JSON-LD daquela página. Nunca marque schema de médico com dado de exemplo.
5. O rodapé da vitrine, com o aviso de que a lista não recomenda ninguém e de que cada profissional responde pela própria publicidade, precisa continuar visível.

---

## 2. Arquitetura técnica

Regra crítica, herdada do site irmão: **cada página HTML é autossuficiente**. O CSS inteiro fica inline em `<style>`, o JavaScript inteiro em `<script>`, e os diagramas são `<svg>` inline. `styles.css` e `main.js` na raiz existem apenas como referência e são sincronizados a cada entrega. Todos os caminhos são relativos.

### Disposição dos arquivos

```
repositório/                  (é o que o GitHub Pages publica)
  index.html, ortopedista-*.html, ...
  CNAME  .nojekyll  robots.txt  sitemap.xml
  favicon.ico  favicon.svg  apple-touch-icon.png  og-image.png
  styles.css  main.js
  HANDOFF-curitibaortopedia.md
  build/                      (ferramentas, não fazem parte do site)
    design.css       sistema de design, fonte única da verdade
    newjs.txt        JavaScript compartilhado
    inject.py        substitui os marcadores numa página nova
    apply_polish.py  propaga CSS, JS, marca, nav, contato e rodapé
    page_builder.py  gera uma página inteira a partir do conteúdo
    conteudo_areas_1.py, conteudo_areas_2.py, conteudo_areas_3.py,
    conteudo_artigos.py
                     o conteúdo das páginas geradas, em Python
    qa.py            verificação obrigatória
    make_sitemap.py  gera sitemap.xml com lastmod real
    make_assets.py   gera og-image.png, favicon.ico e apple-touch-icon.png
    check_layout.py  mede a nav e tira capturas com Playwright
```

### O gerador de páginas

`page_builder.py` monta head, Open Graph, favicon, os blocos JSON-LD, o hero, o índice navegável, o corpo, a FAQ visível, os takeaways, as referências e os marcadores, tudo a partir de um dicionário de conteúdo. Ele valida o tamanho do title e da description e, o mais importante, **gera o FAQPage a partir da mesma lista que desenha a FAQ visível**, o que torna impossível a divergência que custou caro no site irmão.

Para criar uma página nova, o caminho mais rápido é escrever o conteúdo em um arquivo no estilo de `conteudo_artigos.py` e rodar:

```
python3 build/conteudo_artigos.py
python3 build/inject.py nova-pagina.html
python3 build/apply_polish.py && python3 build/make_sitemap.py
python3 build/qa.py && python3 build/check_layout.py
```

As páginas antigas continuam escritas à mão, e as duas formas convivem sem problema, porque o resultado final tem a mesma estrutura.

Os scripts detectam sozinhos as duas disposições possíveis: `build/` ao lado de uma pasta `site/`, ou `build/` dentro do próprio repositório. Não é preciso ajustar caminho.

### Sentinelas

`inject.py` troca os marcadores `{{CSS}}`, `{{JS}}`, `{{MARK}}`, `{{HEADER}}`, `{{CONTACT}}` e `{{FOOTER}}` por blocos envolvidos em sentinelas de comentário, por exemplo `<!--CSS:S--> ... <!--CSS:E-->`. `apply_polish.py` reescreve o conteúdo entre as sentinelas em todas as páginas de uma vez. É por isso que uma mudança de design se propaga com um comando só, e é por isso que **nunca se deve editar CSS, nav, rodapé ou bloco de contato dentro do HTML**: a edição seria sobrescrita na próxima propagação.

### Sequência para criar uma página nova

1. Escrever o HTML completo usando `{{CSS}}`, `{{JS}}`, `{{HEADER}}`, `{{CONTACT}}` e `{{FOOTER}}`.
2. `python3 build/inject.py nova-pagina.html`
3. Adicionar a página em `NAV_NEW` e em `FOOTER_TEMAS_NEW`, dentro de `build/apply_polish.py`, e remover o item "em breve" correspondente.
4. `python3 build/apply_polish.py`
5. `python3 build/make_sitemap.py`
6. Adicionar links contextuais nas páginas relacionadas e o card na home.
7. `python3 build/qa.py` e `python3 build/check_layout.py`
8. Zipar e entregar.

O passo 4 já sincroniza `styles.css` e `main.js` com `design.css` e `newjs.txt`, o que resolve a lição número 1 do site irmão de forma definitiva.

---

## 3. Identidade visual

Estética: calma clínica premium, clara. Identidade deliberadamente diferente do quadrilcuritiba, que usa verde-petróleo com âmbar e a dupla Fraunces com Inter. Aqui nada disso aparece.

### Tokens de cor

| Token | Valor | Uso |
|---|---|---|
| `--brand` | `#22384E` | azul-ardósia profundo, cor principal |
| `--brand-700` | `#1A2C3D` | títulos, rodapé |
| `--brand-500` | `#33506C` | links |
| `--brand-300` | `#7C93A9` | traços de diagrama, bordas em foco |
| `--brand-soft` | `#EDF2F6` | pílulas, fundos suaves |
| `--brand-softer` | `#F5F8FA` | cabeçalho de tabela |
| `--accent` | `#B25E36` | cobre, destaque usado com parcimônia |
| `--accent-700` | `#8E4926` | texto de destaque, hover de link |
| `--accent-soft` | `#FBF0E9` | fundo de callout accent |
| `--alert` | `#9C2B2B` | callout de alerta |
| `--alert-soft` | `#FBEDEB` | fundo do alerta |
| `--ink` | `#141C24` | texto |
| `--ink-2` | `#33424F` | texto secundário |
| `--muted` | `#5E6E7B` | legendas |
| `--bg` | `#FAF8F5` | fundo da página |
| `--surface` | `#FFFFFF` | cards |
| `--line` | `#E5DFD6` | bordas |

Medidas: `--wrap` 1120px, `--wrap-head` 1240px, `--read` 760px, `--head-h` 66px.

### Tipografia

Newsreader nos títulos, Public Sans no corpo, carregadas do Google Fonts com preconnect. Corpo em 17.5px, altura de linha 1.72.

### Marca

Anel aberto à direita com um ponto de cobre no vão, sugerindo articulação. Definido uma única vez em `MARK_SVG`, dentro de `apply_polish.py`, e propagado para cabeçalho e rodapé. O anel usa `currentColor`, então funciona em fundo claro e escuro. O favicon é o mesmo símbolo em um quadrado arredondado azul-ardósia, legível a 16px.

### Navegação e busca, revisadas na sessão 1

A barra de navegação é: Início, Por região do corpo (menu suspenso), Guias (menu suspenso), Para médicos e, no fim, o botão de destaque em cobre "Buscar ortopedista", que leva para `encontre-um-ortopedista.html`. No celular, esse botão aparece como faixa laranja no topo do painel, antes de qualquer outro item.

A página de busca funciona como um diretório: campo de busca grande, três filtros por região e uma lista de cartões `.area-card` de 58 pixels de ícone e botão próprio. A filtragem é feita no próprio navegador, sem servidor, comparando o texto digitado com o atributo `data-chaves` de cada cartão, já normalizado sem acento. Para acrescentar uma área nova basta criar o `<li>` com `data-chaves` (palavras que o paciente usaria, incluindo sintomas) e `data-grupo` (`inferior`, `superior` ou `geral`). O contador em `#busca-status` é atualizado sozinho e é anunciado por leitor de tela.

Correção importante desta revisão: o menu suspenso fechava antes de o usuário conseguir clicar. A causa era o vão de 14 pixels entre o botão e o painel, que disparava `mouseleave` na descida do mouse. A solução tem duas partes, e as duas precisam existir: uma ponte invisível em `.nav-group::after`, que cobre o vão, e um atraso de 520 milissegundos antes de fechar, com o cronômetro cancelado se o mouse voltar. Itens do menu têm 12 pixels de altura interna e fonte de 1rem, para clique fácil.

### Acessibilidade, pensada para leitor mais velho

O site foi ajustado com a premissa explícita de que uma pessoa idosa precisa achar o ortopedista sem dificuldade:

- **Busca no topo da home.** O campo de busca é a primeira coisa depois do título, e abaixo dele vêm nove botões grandes, um por área, com ícone e descrição curta. A pessoa pode digitar ou apenas clicar.
- **Controle de tamanho da letra.** No canto direito do cabeçalho, e também dentro do menu no celular, há um controle com A menor e A maior. Ele altera a variável `--escala`, que multiplica a base de 16 pixels em `html`, e a preferência fica salva no navegador. A faixa vai de 90% a 140%.
- **Botão flutuante no celular.** Depois que a busca sai da tela, aparece uma barra laranja fixa na parte de baixo com "Buscar ortopedista". Ela não aparece na própria página de busca, controlada por `data-pagina="busca"` no `body`.
- **Alvos grandes.** Botões com no mínimo 50 pixels de altura, 60 na variante `lg`, itens de menu com fonte de 1rem, tiles com 82 pixels de altura mínima.
- **Sempre um caminho de volta.** A faixa `.cta-band` repete o convite de busca na home, no pilar, no guia por sintoma e em todas as páginas geradas.

### Componentes disponíveis

`.wrap` `.read` `.prose` `.lead` `.eyebrow` `.pill` `.crumbs` `.toc` `.cards` `.card` `.callout` (info, alert, accent) `.stat-row` `.stat` `.post-fig` `.faq` `.takeaways` `.refs` `.paths` `.path` `.btn` (variantes ghost, accent e lg) `.reveal` `.readbar` `.revdate` `.table-scroll` `.doc-list` `.doc-card` `.doc-empty` `.doc-note` `.section-band` `.divider` `.finder` `.finder-field` `.chips` `.chip` `.area-list` `.area-card` `.tile-grid` `.tile` `.cta-band` `.steps` `.vitrine` `.vcard` (variante preenchida) `.vfoto` `.vtag` `.vficha` `.vitrine-rodape` `.a11y` `.fab`.

Acessibilidade para leitor mais velho: corpo em 18 pixels, botões com 50 pixels de altura mínima e 60 na variante `lg`, itens de menu grandes, contraste alto e foco visível em cobre. A faixa `.cta-band` repete a chamada de busca na home, no pilar e no guia por sintoma, para que a pessoa nunca fique a mais de um clique da lista de ortopedistas.

O `.doc-card` é o componente central do projeto: avatar com iniciais, nome, CRM e RQE, etiquetas de área, lista de definição com endereço, contato e convênios, e rodapé com a origem do dado. Ele já está desenhado e demonstrado com dados fictícios em `cadastre-se.html`.

### Comportamento

Barra de progresso de leitura, entrada por IntersectionObserver com fallback em `<noscript>`, menu mobile cujo ponto de quebra é calculado a partir da largura real da nav medida no navegador, menus suspensos agrupados por região do corpo com suporte a mouse, teclado e Escape, `prefers-reduced-motion` respeitado e folha de estilos de impressão.

---

## 4. Regras de conteúdo, ética e dados

- Nunca citar o nome do dono enquanto estivermos na Etapa 1.
- Nunca ranquear, comparar ou eleger profissionais. A lista é alfabética e isso está escrito na página.
- Nunca publicar depoimento de paciente, foto de antes e depois ou promessa de resultado.
- Cada página que lista médicos traz, em letra pequena, que cada profissional é responsável pela própria publicidade perante o CFM.
- Só publicar dados de médicos com autorização expressa registrada por e-mail, e apenas os campos previstos em `cadastre-se.html`.
- Nunca marcar `Physician` ou `ItemList` com dado inventado ou de exemplo. O schema de médico só entra quando houver médicos reais e autorizados.
- Benefício e risco sempre juntos. Quando a evidência é fraca, o texto diz que é fraca. Quando o efeito médio fica abaixo do limiar clínico percebido, isso aparece escrito. Essa honestidade com os números é a marca registrada dos dois sites.
- Valores monetários entram como referência de mercado, nunca como orçamento. Nas páginas atuais optamos por não citar números fechados, porque envelheceriam rápido.
- Toda página de conteúdo termina com referências, callout de alerta com sinais que exigem médico e data visível de revisão.
- Toda imagem é ilustrativa e a legenda diz isso.
- A palavra-chave "melhor ortopedista de Curitiba" pode ser atacada por um artigo que ensina a escolher com critérios objetivos, sem eleger ninguém. Ainda não foi escrito.

---

## 5. SEO técnico já implementado

- `BreadcrumbList` em todas as páginas, inclusive na home.
- `MedicalWebPage` nas páginas de conteúdo, `WebPage` nas institucionais, `WebSite` e `Organization` na home, tudo com `inLanguage` pt-BR, `dateModified` e `publisher`.
- `FAQPage` gerado a partir das perguntas visíveis, com espelhamento verificado pelo QA. Lembrete: rich results de FAQ não existem mais desde 2026, o schema fica por consistência e por assistentes de IA. Não prometa caixa expandida a ninguém.
- Title com no máximo 65 caracteres e description com no máximo 160, ambos únicos e verificados pelo QA.
- Exatamente um `<h1>` por página, cada `<h2>` correspondendo a uma pergunta real de busca.
- `sitemap.xml` com `lastmod` real, gerado a partir da data de modificação do arquivo.
- `robots.txt` liberando tudo e apontando o sitemap.
- Open Graph completo com `og-image.png` de 1200 por 630.
- SVG de conteúdo com `role="img"` e `aria-labelledby` apontando para `title` e `desc`.

### Cross-link com o site irmão

Por decisão do dono, o quadril é tratado como uma área do guia que vive no outro domínio, e não como um link escondido. Os pontos de saída para `quadrilcuritiba.com.br` são: o item Quadril no menu por região do corpo, o cartão de quadril na página de busca, o card na home, a seção de quadril no guia por sintoma e um link no rodapé. Nenhuma página do curitibaortopedia repete conteúdo profundo de quadril, para não canibalizar o site irmão. Se um dia existir `ortopedista-quadril-curitiba.html`, ela deve ser curta, funcionar como porta de entrada e continuar mandando o leitor para lá.

### Próximas alavancas de autoridade

1. Pedir a cada médico cadastrado um link no site dele ou no perfil profissional. É a maior alavanca do projeto e já está pedida, com educação e sem obrigação, em `cadastre-se.html`.
2. Cadastrar no Google Search Console e no Bing Webmaster Tools, que importa a verificação do Google em um clique.
3. Depois que houver dados, olhar no Search Console as consultas em posição 8 a 25 filtrando por página, e não a média geral. São as brigas ganháveis.

---

## 6. QA obrigatório

`python3 build/qa.py` precisa terminar com "Tudo certo" antes de qualquer entrega. Ele reprova quando:

1. sobra marcador `{{...}}` não substituído;
2. há id duplicado na página;
3. há link ou src interno para arquivo inexistente;
4. há âncora sem elemento correspondente, inclusive âncoras entre páginas;
5. algum bloco JSON-LD é inválido;
6. alguma imagem está sem `alt`, ou algum SVG de figura está sem `role="img"` e `aria-labelledby` válido;
7. a nav ou o cabeçalho estão ausentes ou duplicados;
8. o canonical diverge do nome do arquivo;
9. a página está fora do sitemap;
10. o bloco de contato está ausente;
11. o title passa de 65 caracteres ou a description passa de 160;
12. falta `BreadcrumbList` ou `dateModified` no JSON-LD;
13. há mais de um `h1` ou nenhum;
14. o `FAQPage` não espelha exatamente as perguntas visíveis;
15. falta algum arquivo obrigatório do repositório.

Além do script, validar no navegador com `python3 build/check_layout.py`, que mede a nav em 1221, 1280, 1440 e 1920 pixels, checa overflow horizontal, testa a abertura do menu mobile e do menu suspenso, e salva capturas em 390 e 1280 pixels. **Olhe as capturas de verdade.**

Medição atual da nav: precisa de 700px e tem 1177px disponíveis a 1221 pixels de tela. Há folga para vários itens novos, mas a medição deve ser refeita a cada item adicionado.

Observação da sessão 1: o ambiente de desenvolvimento estava sem acesso ao Google Fonts, então as capturas foram feitas com as fontes de fallback. O layout foi validado nessa condição, que é a mais desfavorável. Em produção, com Newsreader e Public Sans carregadas, a nav fica ligeiramente mais estreita.

---

## 7. Decisões desta sessão que valem manter

- A lista de médicos nasceu vazia e assumida como vazia, em vez de preenchida com nomes copiados sem autorização. Cada página de área se sustenta pelo conteúdo enquanto a lista cresce.
- O card de médico foi desenhado e demonstrado com dados fictícios explicitamente rotulados, em `cadastre-se.html`, para que o médico veja como a ficha vai aparecer antes de enviar os dados.
- A nav foi montada agrupada por região do corpo desde o início, com menu suspenso, exatamente para evitar a fileira plana que estourou o container no site irmão.
- Itens ainda não escritos aparecem como "em breve" sem `href`, o que mantém o QA verde e sinaliza crescimento ao leitor.
- O artigo de CRM e RQE ensina o leitor a verificar o registro no CFM, inclusive explicando que ausência de RQE não é irregularidade em si. É o tipo de honestidade que gera link espontâneo e que nenhum diretório comercial escreve.
- Não citamos faixas de preço fechadas: em vez disso, ensinamos exatamente o que perguntar por telefone. Envelhece menos e ajuda mais.
- A porta de entrada do site passou a ser a busca por área, no formato de diretório, com botão de destaque em cobre presente em todas as páginas. O caminho do paciente é: onde dói, área, página da área, lista de profissionais. Quem chega sem saber nada tem sempre três alternativas visíveis: a busca, os atalhos por região na home e o guia por sintoma.

## 8. Lições do site irmão, que continuam valendo

1. CSS solto que se descola do CSS embutido é bomba armada. Aqui `apply_polish.py` sincroniza `styles.css` e `main.js` em toda propagação, automaticamente.
2. A nav estoura o container ao ganhar itens. Meça sempre com `check_layout.py`.
3. Imagem em `assets/` pode não chegar ao servidor. Por isso todo diagrama é SVG inline.
4. Schema de FAQ que não espelha as perguntas visíveis. O QA verifica isso agora.
5. Rich results de FAQ não existem mais. Não prometa esse ganho.
6. Lição nova, desta sessão: menu suspenso com vão entre botão e painel fecha na cara do usuário. Sempre que mexer no `top` do `.nav-menu`, confira a ponte `.nav-group::after` e o atraso de fechamento, e teste no navegador movendo o mouse do botão até o último item da lista.
7. Regra de especificidade que já mordeu uma vez: `nav.mainnav a.nav-link` vence `nav.mainnav .cta` no cascade. Botões de destaque na nav precisam ser escritos como `nav.mainnav a.nav-link.cta-accent`, senão o fundo simplesmente não aparece. Confira o `background` computado no navegador, não só o CSS.
8. Componente com número de filhos variável não pode depender de `display:grid` com colunas fixas. O `.steps` quebrou exatamente assim: o contador entrava na primeira célula, o título na segunda e o texto voltava para a primeira coluna da linha seguinte. A correção é posicionar o contador em `position:absolute` e deixar o conteúdo fluir. Quando criar componente novo, teste com dois e com três filhos.
9. Elemento com `.reveal` fica invisível até o JavaScript rodar. Existe um `<noscript>` que corrige isso, mas na hora de tirar captura de um componente é preciso rolar até ele antes, senão você fotografa um retângulo vazio e acha que o componente sumiu.
10. Nunca use a forma curta `margin` em um bloco que também tem a classe `.wrap`. Foi assim que a vitrine da home saiu descentralizada: `margin:34px 0 10px` zerou o `margin-inline:auto` do `.wrap` e jogou a seção para a esquerda. A regra da casa é usar `margin-block` nesses casos, e conferir a centralização em 1920 pixels, que é onde o erro aparece.
11. Nos textos de literal com `%` dentro de gerador em Python, escreva `100%%`. O `100% gratuito` do card quebrou o gerador inteiro com "not enough arguments for format string".
