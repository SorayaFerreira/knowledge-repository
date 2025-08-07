---
title: ui_ux
description: Conteúdos Interação Humano-Computador 
pubDate: Mar 18 2025
tags:
  - IHC
  - UI
  - UX
  - Interfaces
  - Design
  - Atômico
---
<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=054f77&height=120&section=header"/>

# Sumário
- [Heurísticas de Nielsen](#heurísticas-de-nielsen---comprasbrasil)
- [Atomic Design](#atomic-design)

# Heurísticas de Nielsen - ComprasBrasil
- Visibility of System Status: indicar ao usuário onde ele está, de onde veio e para onde vai. Ex.: nossa área de controle do andamento.
- Match between the system and the real world: o sistema deve "falar o mesmo idioma" que o usuário, isto é, utilizar convenções, termos comuns a ele. Ex.: utilização de jargões conhecidos pelos futuros usuários, como `homologação` e `adjudicação`.
- User control and freedom: permitir que o usuário corrija seus próprios erros ou mudem de ideia de forma fácil. Ex.: botões de saída (X), a Desistência.
-  Consistency and Standards: seguir padrões da indústria e da plataforma, pois situações, termos e ações muito parecidos devem significar as mesmas coisas ao longo da navegação. Ex.: nossa preocupação em padronizar as representações de UI a partir de um modelo.
- Error Prevention: prevenir erros por desatenção e erros por discrepância entre o modelo mental do design e do usuário. Ex.: 
- Recognition rather than recall: aprensentar opções de imediato, minimizando a quantidade de passos a memorizar para executar uma ação. Ex.: utilização do layout com `Visão Geral`, `Detalhes`, `Comunicação`, `Controle de Andamento` e `Controle de Processo/Lotes`.
- Flexibility and efficiency of use: utilizar atalhos proveitosos tanto para usuários experientes quanto iniciantes e permitir personalização de ações frequentes. Ex.: nossa dinâmica para o dashboard.
- Aesthetic and Minimalist Design: a interface não deve conter informação pouco necessária.
- Help users recognize, diagnose, and recover from errors: ajudar o usuário a compreender erros e sugerir soluções.
- Help and Documentation: pode ser necessário fornecer documentações para ajudar os usuários a entender como completar suas tarefas. Ex.: nosso [Portal de Ajuda](https://ajuda.portaldecomprasbrasil.com.br/).

- **O que é microdata? E para quê serve?** R.: É um conjunto de atributos que serve para especificar melhor o assunto dos conteúdos inseridos numa página com HTML.

- **Como escrever microdata nos pitches? Passo a passo.** R.: 

- **Atributos "itemtype" e "itemscope", "itemprop"? R**.: 
	- O "itemscope" limita o "assunto", de um conjunto de tags (as aninhadas dentro do elemento que recebeu o itemscope). 
	- Já o "itemtype" recebe uma URL (`https://schema.org/TipoDoConteudo`, ou `itemprop="url"`para sites de terceiros), indicando o tipo contido na tag raiz (com o itemscope). 
	- O "itemprop" serve para definir propriedades do conteúdo (itemscope) que está incluso no conjunto de tags em questão, "Então aí ele tá mostrando que o tipo `BlogPosting` possui os atributos `headline`, `datePublished`, `url`, e `discussionUrl`. Tipo no nosso caso, onde o tipo `Processo` possui os atributos (derivados) `solicitacoes` e `propostas`. Tipo no nosso caso, onde o tipo `Processo` possui os atributos (derivados) `solicitacoes` e `propostas`".
 
- **O que é design token-based UI architecture?** R.: dá pra usar para geração de código automático. São decisões de design representadas como dados, sendo blocos de fundação para o design de sistemas. _São variáveis JSON  ou YAML que vão guardar padrões de design para diferentes elementos_.

# Atomic Design
Atomos combinados juntos formam molécular. Moléculas combinadas podem se combinar e formar organismos complexos.
Atomos são os blocos fundamentais de composição de toda matéria. Cada átomo tem suas propriedades, suas partes, e se ele for despedaçado, ele perde sua essência principal.
- Atoms: labels, inputs, buttons etc
- Molecules: form label, search input etc. 
- Organism: diferentes tipos de moléculas unidas, ou uma mesma molécula repetida várias vezes dentro de um conjunto.
- Templates: objetos de nível de página que colocam componentes em um layout e articulam a estrutura de conteúdo subjacente do design.
![templates](https://atomicdesign.bradfrost.com/images/content/template.png)

- Pages: instâncias de modelos que mostram a aparência de uma interface de usuário com conteúdo representativo real.

# React ⚛✨
- [React learn](https://react.dev/learn) é muito legal.
- O React é uma `lib` que fornece componentes sem estilo. Ele faz uso de uma técnica chamada VDOM (Virtual DOM) que faz com que ele seja mais efiente do que os demais frameworks de UI. Sempre que algo muda no DOM virtual, ele faz uma comparação com o novo estado, calcula a menor atualização possível e a aplica ao DOM real. Resumindo, o VDOM atualiza somente aquele pedacinho que foi alterado, e não o DOM inteiro. Só que o React tem alguns problemas, como o JSX mesmo. O JSX unifica o HTML com o JavaScript e isso fez algumas pessoas detestarem o React.
- Para dar estilo, podemos utilizar bibliotecas como Bootstrap, Tailwind, entre outras;
- Alguns termos ainda me geram dúvida sobre sua função e relação entre as ferramentas supracitadas: Radix UI, shadcn/ui, Tailwind, Origin UI;
- O [Origin UI](https://originui.com/) e o [Kibo UI](https://originui.com/) são _projetos_ que utilizam componentes primitivos do **shadcn/ui** em seus próprios componentes.
- O shadcn/ui é equivalente ao bootstrap e ao tailwind, a diferença é que nele você faz um "download" do componente para seu projeto e, então, você tem total controle sobre os componentes, podem fazer as alterações que quiser.
- Radix IU é uma biblioteca de componentes React que te ajuda a construir coisas como dropdowns, dialogs, entre outras coisas. Ele não vem com estilização, apenas com o comportamento. Então é você quem estiliza e, para isso, você pode usar outras bibliotecas.
- O shadcn/ui é rápido de utilizar, flexível, leve, simples e feito especificamente para o React. Um dos diferenciais dele é que os componentes são customizáveis, ao contrário do Tailwind e do Material UI
- Atualmente, a forma mais recomendada de se construir interfaces com React é utilizando o Radix UI e o shadcn/ui.
- Libs que o shadcn recomenda como alternativas: [ariakit](https://ariakit.org/), [React Aria](https://react-spectrum.adobe.com/react-aria/index.html).
- Quando você for importar um componente, é interessante investigar de quais outras libs ele depende e se elas são confiáveis.
- **Renderizar** significa que o react vai recalcular todo o conteúdo de um componente. Isso acontece quando: um hook muda; uma propriedade do componente muda; um elemento pai do componente é al terado; é preenchido um novo estado.
- **Cuidado🚨**: há um tipo de erro muito comum no react é a criação de _estados derivados_, gerando renderização desnecessária. Não cometa isso. Para resolver, tente criar uma variável para armazenar, ao invés de usar um state.

- **Componente**: é um pedaço da UI que tem sua própria lógica e aparência. Ele pode ser tão grande quanto uma página da web, ou tão pequeno quanto um botão.
- Os componentes são como tags HTML, e, assim como tags HTML possuem propriedades (`<img src="./alguma_coisaqueatagrecebeu">`), os componentes possuem propriedades. Dentro dos componentes há funções javascript que recebem como parâmetro as `props`, isto é, as propriedades passadas lá entre </> (colchetes).
- Lá dentro da função javascript, você pode acessar as `props` ou pode acessar o `children` dessas `props`, que pode ser um texto entre as tags, tipo `<div>Eu sou o children.</div>`.
- Mano, achei loko isso. Um componente react é uma função javascript que retorna um _markup_ um HTML. Daí você pega e chama essa função dentro de tags (`< />`) como se fosse um elemento HTML mesmo.
- O nome dos componentes têm que começar com letra maiúscula.
- [Detalhes do JSX](https://react.dev/learn#writing-markup-with-jsx).
- O atributo `class` do react é o `className`, mas funciona do mesmo jeito.
- Você pode usar `{}` no meio dos elementos html para colocar coisa em javascript.
- Ou também dá pra fazer o contrário e colocar HTML  no meio das função js.
- Aqui também funciona o `map()`. Use para transformar um array de qualquer coisa, tipo `produtos`, num array de itens `<li>`, porém todos precisam do atributo `key={}` preenchido.
- Não é necessário colocar `()` ao final para chamar uma função, o próprio React chama o handler de evento quando o usuário o executar.
- Tem como armazenar o número de vezes que um evento ocorreu, tipo o clique de um botão, por meio do `{ useState }`, tu importa e daí tem que adicionar a variável no seu componente. Mesmo que você tenha mais de uma instância do mesmo componente, a contagem de cada um será diferente.
- **Hooks**: o que é um hook? Então. Hooks são funções que o nome delas começa com `use`, tipo a `useState` mesmo. Você pode criar seus próprios hooks combinando os hooks embutidos existentes. Os hooks são restritivos. Eles só podem ser chamados no topo dos seus componentes ou de outros hooks. 

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=054f77&height=120&section=footer"/>