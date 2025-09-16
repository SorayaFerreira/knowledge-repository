---
title: maintenance
description: Conteúdo sobre Manutenção de Software
pubDate: Set 14 2025
tags:
  - Manutenção de Software
---
<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=5f161c&height=120&section=header"/>

# Sumário
- [Conceitos Fundamentais](#conceitos-fundamentais)
- [Tipos de Manutenção](#tipos-de-manutenção)
- [Leis de Lehman](#leis-de-lehman)
- [Técnicas da Manutenção](#técnicas-da-manutenção)
- [Modelos de Manutenção](#modelos-de-manutenção)
- [Fatores de Compreensão](#fatores-de-compreensão)
- [Métricas](#métricas)

# Conceitos Fundamentais
- Manutenção: manter, sustentar, consertar, conservar, refatorar e evoluir.
- Na manutenção, precisamos de muito teste de regressão.
- A partir do momento que o cilente já está usando algo que você já implementou, então o que for feito em cima disso já é manutenção de software.
- A manutenção representa 90% dos custos do desenvolvimento e constitui a fase mais longa do ciclo de software.
- **Manutenção é responsável por tratar das mudanças relacionadas ao software após sua entrega para o cliente. Dessa forma, ela o mantém em bom estado de reparo, eficiência e validade, evitando falhas e obsolescência.**
- Software é código mais todos os artefatos relacionados a ele, como requisitos, decisões, projeto e manuais.

# Tipos de Manutenção
- **Corretiva**: corrige defeitos.
- **Adaptativa**: adapta a mudanças externas.
- **Perpectiva/Evolutiva**: fornece melhorias para os usuários.
- **Preventiva**: previne problemas. Aqui entra refatoração de código, atualização de documentação e reestruturações.

# Leis de Lehman
- São as Leis da Evoulção de Software. 
- Sistemas de software envelhecem assim como seres vivos. 
- O processo de manutenção vai até o ponto em que se torna menos custoso realiza a substituição completa do sistema. São elas:
- **Crescimento Contínuo:** funcionalidades adicionais devem ser acrescentadas aos poucos para atender as necessidades dos usuários e otimizar sua experiência de utilização.
- **Declínio da qualidade:** se o software não sofre adaptações para atender mudanças externas, ele entra em declínio.
- **Complexidade Crescente:** se a complexidade não for reduzida, ela só vai crescer cada vez mais.
- **Mudança Contínua:** se o software não é continuamente adaptado, ele se torna inútil em algum momento.
- **Auto Regulação;**
- **Conservação da estabilidade organizacional;**
- **Conservação de familiaridade;**
- **Sistema de feedback;**

# Técnicas da Manutenção
- **Reengenharia**: reconstrução de um software já existente, igual foi o caso do SigFap.
- **Engenharia Reversa**: descobrir os princípios tecnológicos e fundamentos de um software, analisando sua estrutura, função e operação. Ou seja, é quando você tenta extrair diagramas e modelos mentais de coisa que foram implementadas sem documentação.
- **Migração**: traduzir um programa para outra linguagem de programação, por exemplo. Ou migrar o banco de dados, ou o sistema operacional também.

# Modelos de Manutenção
- **Modelo Quick-fix:** abordagem ad hoc. Espera-se pela ocorrência do problema para que ele seja resolvido da forma mais rápida possível. Essas mudanças são feitas sem análises detalhadas.
- **Modelo Melhoria/Iterativa:** foca em melhorar o sistema de forma iterativa. É muito parecido com a metodologia de desenvolvimento, mas que foi adaptado para a manutenção especificamente. Tem atividades como **Análise, Caracterização da proposta de modificação, novo projeto e implementação**.
- **Modelo de Taute:** change request -> estimate -> schedule -> programming -> test -> documentation -> release -> operation ↺.

# Fatores de Compreensão
Atividades e técnicas específicas da manutenção:
- Compreensão do programa: isso aqui é aquilo de "ler código é mais difícil do que escrever". Envolve toda a complexidade de gastar seu tempo entendendo o que foi feito por outra pessoa.
- Transição: passagem do software para a fase de manutenção ou entre equipes de manutenção.
- Gerenciamento de Solicitações: gestão do fluxo de todas as solicitações de mudança.
- Análise de Impacto: avaliar as consequências de uma mudança proposta no sistema.
- Acompanhamento de Níveis SLA (Service Level Agreement): monitorar se os acordos de nível de serviço para a manutenção estão sendo cumpridos.
- Aceitação/rejeição da solicitação de mudança: processo de avaliar e decidir se uma solicitação de mudança será implementada ou não.
- VVT e GCS são atividades de suporte à manutenção.

# Métricas
- Fan-in: número de funções que chamam um dada função, ou número de módulos externos que dependem de determinado módulo.
- Fan-out: número de funções chamadas por uma dada função, ou número de módulos dos quais um determinado módulo depende.
- Tamanho de código: LOC - Linhas de Código.
- Complexidade Ciclomática: complexidade do c ódigo através da quantidade de caminhos de execução.
- Profundidade de aninhamento: número de estruturas internas, como `for`, `while` e `if` aninhados.
- Métricas de Chidamber-Kemerer (CK) – Específicas para Sistemas Orientados a Objetos: profundidade de herança (DIT), número de filhos (NOC), Acoplamento entre objetos (CBO), Falta de coesão em métodos (LCOM), Métodos ponderados por classes (WMC), Resposta para classe (RFC).



<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=5f161c&height=120&section=footer"/>