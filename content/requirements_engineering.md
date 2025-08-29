---
title: requirements_engineering
description: Conteúdo sobre Engenharia de Requisitos
pubDate: Jul 24 2025
tags:
  - MVP
  - Design
  - Documentação Técnica
---
<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=f2c438&height=120&section=header"/>

# Sumário
- [Requisitos](#requisitos)
- [MVP - Mínimo Produto Viável](#mvp---mínimo-produto-viável)
- [Documentação Técnica](#documentação-técnica-️)

# Requisitos

# MVP - Mínimo Produto Viável
- Ele surge num contexto de grande risco e cujas chances de insucesso são altíssimas.
- Um MVP precisa atestar a capacidade da empresa de atrair clientes dispostos a pagar pelo produto ou serviço. 
- [x] Existem clientes dispostos a pagar por uma solução X para um problema Y?
- Como o custo de desenvolver um sistema, mesmo que mínimo, pode ser alto, então geralmente uma startup faz MVPs com sketches, vídeos ou apenas uma landing page. Seria algo que pode ser feito em poucos dias (na Cento é 1 semana).
- **No MVP, você decide se o produto é mínimo, mas é o cliente quem decide se o produto é viável.** *Viável* significa um produto que atrai clientes.
- Se for pra fazer um sistema, devemos focar em *early adopters*, criando algo bem genérico para um amplo público.
- Por enquanto, você não precisa automatizar nada.
- Use serviços e bibliotecas de terceiros, como de autenticação e cobranças por cartões de crédito.
- **Requisitos não-funcionais mais adequados:** desempenho, usabilidade, segurança e privacidade.
- **Otimização prematura** deve ser evitada.

> **_Ame o problema e não a solução ou tecnologia que você está usando._**

- **Escalabilidade** não é importante agora. NÃO É. Assim como cobertura de testes e arquitetura extensível.
- Se o sistema...
	- Já tem requisitos e escopo claros,
	- A equipe já tem competência e experiência para desenvolvê-lo, e
	- O sistema já tem um cliente garantido que vai pagar por ele...
	- Então esse sistema não é um MVP.
- O MVP teste se vale a pena construir e vender algo.

> **_O MVP não é um produto. Ele é um processo._**

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

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=f2c438&height=120&section=footer"/>