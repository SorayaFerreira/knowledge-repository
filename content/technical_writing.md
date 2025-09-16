---
title: technical_writing
description: Conteúdos sobre Escrita Técnica
pubDate: Mar 18 2025
tags:
  - Escrita Técnica

---

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=ff5733&height=120&section=header"/>

# Sumário
- [Documentação Técnica](#documentação-técnica-️)
- [Writing Code Is Easy. Reading It Isn’t.](#writing-code-is-easy-reading-it-isnt)

# Documentação Técnica 👩‍💻📋️
> Link de referência: https://grantslatton.com/how-to-design-document

- Todas as decisões tomadas dentro duma empresa DEVEM ter objetivo de fazer a empresa crescer. Elas devem contribuir para o negócio.
- O objetivo maior de uma documentação de design é informar ao leitor que aquele design é o melhor dadas as circunstâncias que o cercam.
- **Você não deve escrever uma documentação esperando que o leitor complete e conecte todas as coisas na cabeça dele sozinho.**
- É interessante que o leitor pense que cada sentença soa óbvia a partir das anteriores, de modo que seja uma leitura muito fácil, simples de compreender e autocompleta.
- A documentação deve apresentar os modelos mentais que levaram a uma solução de maneira inteligível, mesmo que tenha levado semanas para ser pensado.
- **Você precisa prever todas as alternativas e todos os argumentos que o leitor possa pensar para contrapor suas ideias. Então, garanta que tudo isso seja previamente invalidado.**
- Seja muito sucinto porque a atenção do seu leitor é algo escasso. Utilize notas de rodapé para ajudar.
- Ordem utilizada: `Definition -> Goal -> Organization -> Editing -> Volume -> Concrete tips`;
- Ordem de tópico com base nas docs do Golang: 
    1. **Introduction**
    2. **Problem**
    3. **Goals**
    4. **Draft Design:** This section quickly summarizes the draft design, as a basis for high-level discussion and comparison with other approaches.
    5. **Discussion and Open Questions:** These draft designs are meant only as a starting point for community discussion. This section outlines some of the questions that remain to be answered.
    6. **Design in Other Languages**: Alternativas à solução proposta.

# Writing Code Is Easy. Reading It Isn’t.
_https://idiallo.com/blog/writing-code-is-easy-reading-is-hard_

- Escrever código fica fácil depois que você já domina a sintaxe e já tem a ideia da solução em mente. E com LLMs fica mais fácil ainda.
-  É muito mais difícil ler código do que escrever, em razão da dificuldade em formar o modelo mental do sistema em sua mente. E é impossível ler código sem esse modelo mental na cabeça.
- Ler código é como refazer os passos de alguém, o que implica em consultar diferentes arquivos, encontrar chamadas de funções, deduzir side effects e decifrar intenções que não estão explícitas. 
- Quanto maior a quantidade de código para analisar, mais demorado é para construir o modelo mental.
- É mais conveniente utilizar LLMs para entender código do que para gerar um monte de código pra você entender sozinha depois.

> [!QUOTE]
Say you need to understand a simple function like `getUserPreferences(userId)`. To build your mental model, you need to trace:
> - Where is this function defined?
> - What does it return? Is it a Promise? What's the shape of the data?
> - Does it hit a database directly or go through an API?
> - Are there caching layers involved?
> - What happens if the user doesn't exist?
> - Who else calls this function and in what contexts?
> - Are there side effects?

> The future of programming might not be about generating more code faster. It might be about generating understanding faster. And that's a much harder problem to solve.

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=ff5733&height=120&section=footer"/>