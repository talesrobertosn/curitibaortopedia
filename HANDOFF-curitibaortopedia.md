# HANDOFF — curitibaortopedia.com.br

Documento de continuidade. Quem abrir um chat novo deve ler este arquivo inteiro antes de produzir qualquer coisa.

Última atualização: 17 de agosto de 2026 (sessão 1, entrega inicial).

---

## 1. Estado atual

Site estático de SEO local, em português do Brasil, para GitHub Pages, no domínio `curitibaortopedia.com.br`. Gratuito, sem fins comerciais, voltado a pacientes leigos. Duas funções: hub de indicação de ortopedistas por subespecialidade e artigos informativos que capturam a busca de sintoma.

Objetivo declarado: primeira posição do Google para "ortopedista em Curitiba" e variações por subespecialidade.

Etapa 1 (atual): o nome do dono não aparece em lugar nenhum do site. O projeto se apresenta como informativo independente, com autoria institucional. A Etapa 2, com nome, RQE e schema de médico, só acontece quando houver título de especialista, e não deve ser antecipada.

### Páginas publicadas (10)

| Arquivo | Termo-alvo | Situação |
|---|---|---|
| `index.html` | ortopedista em Curitiba (hub) | pronta |
| `ortopedistas-em-curitiba.html` | ortopedista em Curitiba, pilar | pronta, diretório vazio por enquanto |
| `ortopedista-joelho-curitiba.html` | ortopedista de joelho Curitiba | pronta |
| `ortopedista-coluna-curitiba.html` | ortopedista de coluna Curitiba | pronta |
| `ortopedista-ombro-curitiba.html` | ortopedista de ombro Curitiba | pronta |
| `crm-rqe-como-verificar-ortopedista.html` | CRM, RQE, verificar ortopedista | pronta, artigo-assinatura |
| `qual-medico-procurar-para-cada-dor.html` | qual médico procurar para cada dor | pronta, peça central de linkagem interna |
| `cadastre-se.html` | cadastro de médicos | pronta |
| `sobre.html` | institucional | pronta |
| `privacidade.html` | LGPD | pronta |

### Arquivos de infraestrutura no repositório

`CNAME`, `.nojekyll`, `robots.txt`, `sitemap.xml`, `favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `og-image.png`, `styles.css`, `main.js`. Nenhum deles pode ser apagado.

### O que ficou para a próxima sessão

1. `ortopedista-mao-curitiba.html`
2. `ortopedista-pe-tornozelo-curitiba.html`
3. `ortopedista-quadril-curitiba.html` (curta, porta de entrada, aponta para quadrilcuritiba.com.br)
4. `ortopedista-infantil-curitiba.html`
5. `medicina-esportiva-curitiba.html`
6. Artigos: quanto custa a consulta, ortopedista pelo SUS em Curitiba, ortopedista contra reumatologista contra fisiatra, como se preparar para a primeira consulta, pronto atendimento ortopédico, o que é RQE e título pela SBOT, e depois os artigos de sintoma por região.

Enquanto essas páginas não existem, elas aparecem no menu e nos cards como "em breve", sem `href`, para não quebrar o QA.

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
    design.css   sistema de design, fonte única da verdade
    newjs.txt    JavaScript compartilhado
    inject.py    substitui os marcadores numa página nova
    apply_polish.py  propaga CSS, JS, marca, nav, contato e rodapé
    qa.py        verificação obrigatória
    make_sitemap.py  gera sitemap.xml com lastmod real
    make_assets.py   gera og-image.png, favicon.ico e apple-touch-icon.png
    check_layout.py  mede a nav e tira capturas com Playwright
```

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

### Componentes disponíveis

`.wrap` `.read` `.prose` `.lead` `.eyebrow` `.pill` `.crumbs` `.toc` `.cards` `.card` `.callout` (info, alert, accent) `.stat-row` `.stat` `.post-fig` `.faq` `.takeaways` `.refs` `.paths` `.path` `.btn` `.reveal` `.readbar` `.revdate` `.table-scroll` `.doc-list` `.doc-card` `.doc-empty` `.doc-note` `.section-band` `.divider`.

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

Existem exatamente dois links para `quadrilcuritiba.com.br` no site inteiro: o card de quadril na home e a seção de quadril em `qual-medico-procurar-para-cada-dor.html`. Não foi colocado link no rodapé, justamente para não criar uma rede de links entre os dois domínios. Se a página `ortopedista-quadril-curitiba.html` for criada, ela deve substituir um desses dois links, e não somar um terceiro.

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

## 8. Lições do site irmão, que continuam valendo

1. CSS solto que se descola do CSS embutido é bomba armada. Aqui `apply_polish.py` sincroniza `styles.css` e `main.js` em toda propagação, automaticamente.
2. A nav estoura o container ao ganhar itens. Meça sempre com `check_layout.py`.
3. Imagem em `assets/` pode não chegar ao servidor. Por isso todo diagrama é SVG inline.
4. Schema de FAQ que não espelha as perguntas visíveis. O QA verifica isso agora.
5. Rich results de FAQ não existem mais. Não prometa esse ganho.
