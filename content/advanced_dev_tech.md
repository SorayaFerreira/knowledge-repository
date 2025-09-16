---
title: advanced_dev_tech
description: Conteúdo sobre Técnicas Avançadas de Desenvolvimento de Software
pubDate: Mar 17 2025
tags:
  - Virtualização
  - Containers
  - Docker
  - Variáveis de Ambiente
---
<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=ff4000&height=120&section=header"/>

# Sumário
- [Virtualização 🆚 Containers](#virtualização--containers)
- [Docker 🐳🐋](#docker-)
- [Paradimas de Programação](#paradigmas-de-programação-️️)
- [Programação Funcional](#programação-funcional)

# Virtualização 🆚 Containers
Ambos são tecnologias que auxiliam a configuração de servidores.

![Imagem comparando virtualização e containers](https://miro.medium.com/v2/resize:fit:1400/1*LxvdF6TuBXec4AWhApdLBg.png)

## Virtualização 👩‍💻🖥
A virtualização é uma técnica que consiste num fracionamento abstrato, feito pelo Hypervisor, da camada de hardware da máquina host (servidor, computador pessoal etc) que possibilita a execução de sistemas operacionais, dependências e programas de modo individual e independente dentro do sistema operacional original, **_dividindo_** componentes físicos. Essa técnica é ótima para separar a execução de várias aplicações, que podem demandar sistemas operacionais diferentes, em um mesmo computador, sem que um sistema interfira no outro.

No entanto, tal tática pode requerer muito dos recursos da máquina e maior trabalho de manutenção, logo, em alguns casos, pode ocasionar desperdício. Foi em razão disso que surgiu a virtualização em containers, serviço oferecido por softwares como Docker, Podman e LXC.

## Containers
Na técnica de virtualização utilizando containers, há uma entidade, como o **_engine_** no caso do docker, que cria containers com base no sistema operacional host, e tais containers fazem uso dos mesmos componentes físicos, de modo "simultâneo". Isso é mais

Os **containers** empacotam software de forma que seja  possível executá-lo nas máquinas destino mesmo que elas tenhas sistemas operacionais diferentes. Eles são formados por imagens, e **_imagens_** são pacotes executáveis mais leves que oferecem as instruções para criar os containers. O [Docker Hub](https://hub.docker.com) é uma comunidade que disponibiliza várias imagens para criação de containers de alguns sistemas de código aberto.

# Docker 🐳🐋
O Docker é uma plataforma que viabiliza a virtualização em containers. Nele, os containers são ambientes de [runtime](../programming_languages/backend_javascript.md) com tudo que é preciso para rodar o código da aplicação de forma independente. Ele apresenta a **Engine**, entidade responsável por criar, executar e gerenciar os containers.

![Logo Docker Compose](https://miro.medium.com/v2/resize:fit:1400/0*yKUZfT6P10SAIWNy.jpg)

**Docker Compose** é uma ferramenta utilizada para configurar o gerenciamento de multiplos containers, cada um executando um serviço diferente e que "conversam" entre si. Tal configuração é feita em um arquivo **YAML**, com extensão `.yml`. Uma vez escrito o documento de configuração, basta executar apenas um comando para iniciar todos os serviços nos containers.

Já o **Dockerfile** é um arquivo de texto com instruções detalhadas para criação de uma imagem, que será utilizada pelo docker com o comando de build para criar o container. É um arquivo sem extensão, porém seu nome ser exatamente `Dockerfile`.

## Concorrentes do Docker
- **Podman**: o nome é abreviação de `gerenciador pod`. Trata-se de uma plataforma que, assim como o docker, tem o objetivo de executar e gerenciar containers. Ele foi criado por colaboradores da Red Hat com a comunidade open-source e faz uso da biblioteca `libpod`. Sua principal diferença é não ter _daemon_, ou seja, não apresenta um processo com privilégios de administrador sendo executado no background, o que torna o Podman mais seguro.
- **LXC**: `LinuX Containers` é um projeto de aplicações em container, também de código aberto. Ele não tem uma interface gráfica, mas de linha de comando. Além disso, seus containers se comportam como máquinas virtuais mais leves e possibilita maior controle da configuração.

### YAML
Esta é uma linguagem de serialização de dados, mas geralmente utilizada para arquivos de configuração, assim como JSON e XML. A sigla significa "Yet Another Markup Language" e ela é usada para escrever o documento Docker Compose. 

Principais características:
- Arquivos com tal linguagem podem ter extensão `.yml` ou `.yaml`;
- Utiliza identação para indicar aninhamento, tal qual o Python.
- Exemplo:
```yaml
#Comment: This is a supermarket list using YAML
#Note that - character represents the list
---
food: 
  - vegetables: tomatoes #first list item
  - fruits: #second list item
      citrics: oranges 
      tropical: bananas
      nuts: peanuts
      sweets: raisins
...
```
- Visite este [guia](https://www.redhat.com/en/blog/yaml-beginners).

### Variáveis de Ambiente
São cadeias de caracteres (strings) que usualmente guardam dados de configuração de aplicações, sendo utilizadas pela própria aplicação durante o funcionamento. Elas podem ser aplicadas em containers do Docker, quando é preciso realizar uma configuração dinâmica, ou para registrar dados sensíveis, como senhas. Para tanto, arquivos com extensão `.env` são definidos para que o Docker leia com prioridade, contudo essas variáveis podem ser descritas em outros documentos como o dockerfile.

# Paradigmas de Programação 🖱️⌨️
*Sobre Paradigmas de Programação*, [vídeo](https://youtu.be/sqKnYS-ZXsQ?si=Ep64J9IPRHdxeoTl).

- Imperativos: Programação Procedural, Programação Orientada a Objetos.
- Declarativos: Programação Funcional, Programação Lógica.

* Eles são divididos em dois tipos: **imperativos e declarativos.**  
* Pode-se dizer que a programação funcional é um dos **últimos estágios da evolução** natural das linguagens de programação.  
* Dicionário: exemplo que serve como modelo; padrão.  
* Paradigmas: modelo, padrão ou estilo de programação suportado pelas linguagens.  
* Os projetistas de cada linguagem são quem projetam as linguagens para certos paradigmas.  
* Os paradigmas de programação são classificados conforme decisões de projeto, isto é, a forma como cada problema será abordado em sua solução.  
* Quando a gente conhece vários paradigmas, a gente sabe várias formas diferentes de resolver um mesmo problema e isso **é poderoso**.  
* Alguns paradigmas: orientado a objetos, orientado a eventos, lógico, declarativo, imperativo, estruturado, funcional, procedural, orientado a fluxos, orientado a aspectos.  
* A linguagem precisa seguir todos os princípios daquele paradigma para ela ser considerada “puramente \[nome do paradigma\]”.  
* **Paradigma Estruturado:** surge logo após o imperativo e agrupa instruções em blocos de condicionais e loops.  
* **Paradigma Procedural:** estrutura o código por procedimentos, como rotinas, métodos e funções.  
* **Paradigma Orientado a Objetos:** tem a lógica mais próxima do mundo real. Tudo é objeto. Tem classes, métodos, atributos etc.  
* **Paradigma Orientado a Eventos:** aguarda um evento para realizar uma ação. É ideal para sistemas, drivers e interfaces de usuário. Exemplos de eventos: cliques, teclas, alertas.  
* **Orientado a Aspectos:** realiza melhorias para a orientação a objetos por separação de interesses transversais. Ex.: login, autenticação, controle de acesso.  
* **Paradigma Lógico:** baseado em conhecimento (fatos e regras). Inferência lógica de informações. O Prolog é um exemplo de linguagem desse paradigma.

## **Paradigma Imperativo**
* É o mais antigo que temos. Ele segue o conceito de estado e ações que manipulam esse estado. Ele surgiu com a arquitetura de Von Neumann.     
* Variáveis não são simples.  
* **O que é uma variável**: é um elemento de código que possui *nome, endereço (de memória), valor (aquilo que será armazenado), tipo (do dado que ela armazena), tempo de vida e escopo.*  
* Expressões têm efeitos colaterais, isto é, resultados não esperados, porém linguagens funcionais não têm efeitos colaterais. Eles ocorrem sobretudo quando uma função é capaz de alterar o valor de uma variável global.  
* As expressões são influenciadas por regras de precedência, associatividade, sobrecarga de operadores e misturas de tipos.

## **Paradigma Declarativo**
* O dev define aquilo que ele deseja, e não como obter.   
* Executor/interpretador é o responsável pelos resultados.  
* A responsabilidade de executar ou interpretar o código fica para o sistema, sem que o dev precise se preocupar com a maneira pela qual esses resultados são obtidos.

## Programação Funcional
* Linguagens puramente funcionais: Elixir, OCaml, Clojure, Haskell, Scala, Erlang.  
* Uma função é algo exato. Ela sempre produz os mesmos resultados esperados, dado o dado de entrada. A programação funcional busca mimetizar as funções matemáticas o máximo possível.

Conceitos e diretrizes de programação funcional:
- Imutabilidade: nenhuma variável pode ser modificada durante a execução. As variáveis são salvas como _somente leitura_, de modo que a depuração fica mais simples. 
- Funções de Primeira Classe: as funções não tês restrições ou limitações e podem ser passadas como argumento a qualquer momento.
- Funções puras: a função tem apenas um resultado possível, com base numa entrada.
- Composição de Funções: isola lógicas em muitas funções pequenas, o que aumenta a facilidade de testar e dasacoplar lógicas.
- Expressões: essa metodologia não aprova a criação de funções void, com procedimentos muito complexos.
- Recursões: não usam laços, mas recursões, a fim de evitar bugs envolvendo laços de iteração.

```shell
iex> 1
iex> Ox1F
iex> 1.0
iex> true
iex> :atom
iex> "elixir"
iex> [1, 2, 3]
iex> {1, 2, 3}
<> # concatenação de strings
and, or, not # lógicos
= # é uma equivalência. Não estamos fazendo atribuição de memória. 
iex> {a, b, c} = {:hello, "world", 42}
iex> nil # é o null
```

* Átomo: carrega um significado igual ao longo de todo o código. É muito parecido com uma constante (*const*). Ex.: *:num \= Numero*  
* Em Elixir não temos atribuição; temos a equivalência. A atribuição coloca um valor dentro de uma variável, que pode mudar ao longo do código. Já na equivalência, o que está à esquerda e o que está à direita devem ser compatíveis. A “variável” da esquerda assume o valor da direita e isso nunca muda, por conta da imutabilidade.  Ao fazer a definição de uma equivalência, você diz “De agora em diante, considere que X é o mesmo que 10”. 

```elixir
// Gera incompatibilidade
{a, b} = {1, 2, 3}
** (MatchError) no match of right hand side value: {1, 2, 3}

// Esse é equivalente
{:ok, value} = {:ok, 42}
```

* Função Pura: é aquela que age sobre os próprios parâmetros.  Se elas não retornam nada, elas são ineficientes. Sempre produzem as mesmas saídas (sem efeitos colaterais). É inevitável ter funções impuras, porém elas devem ser evitadas.  
* Imutabilidade: tudo é considerado constante.  
* Função de 1ª Ordem: é aquela que permite atribuir uma função a uma variável.  
* Função de 2ª Ordem: é aquela que permite passar uma função como parâmetro de outra função.  
* Função Lambda: são as funções anônimas, isto é, funções sem nome. Você usa de forma muito específica. Geralmente são curtas, utilizadas em expressões. No javascript podemos criar funções lambda de duas formas: atribuindo a uma variável (com *function*), ou declarando uma arrow function.  
* Há vários métodos para construção de loops na programação funcional além da técnica recursiva. 
* Imutabilidade faz com que os dados sejam mais consistentes. As variáveis não são variáveis.  
* Records: as entidades são imutáveis. O Record é equivalente a uma classe e os atributos dele são imutáveis.  
* É possível fazer funções anônimas também.
* Uma **função callback** é uma função passada a outra função como argumento, que é então invocado dentro da função externa para completar algum tipo de rotina ou ação.  
* A gente usa muito as callback functions em funções assíncronas, mas isso deve ser bem planejado, se não, criamos o chamado “callback hell”.

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=ff4000&height=120&section=footer"/>