---
title: abstraction
description: Conteúdo sobre abstração de conceitos ou objetos
pubDate: Feb 02 2025
tags:
  - Modelo Mental
  - Abstração
  - Hipótese
---

# Modelo Mental 🧠🧮

<div align="center"><img alt="'El 'Toro' de Picasso" src="https://ferd.ca/static/img/picasso-bulls.jpg" width="400px"></div>

>  "[A complexidade precisa estar em algum lugar](https://ferd.ca/complexity-has-to-live-somewhere.html)",  "[mas não em _todo_ lugar](https://v5.chriskrycho.com/journal/essence-of-successful-abstractions/)". 

> Apenas complexidade pode gerir complexidade.

Modelos Mentais têm relação com os conceitos de _abstração_ e _hipótese_, que juntos visam gerenciar níveis de complexidade de uma ideia.

Observando a imagem acima ("El Toro" de Picasso), _abstração_ seria representada pelos desenhos da linha mais inferior, que são os mais simples. Um indivíduo tem algo em mente e cria uma representação simplificada disso, realçando apenas o que lhe interessa e aponta para seu objetivo. Uma planta de uma casa, por exemplo, também é uma abstração, todavia a planta direcionada para o encanador e a planta para o eletricista têm objetivos difentes, logo, são distintas entre si. Em outras palavras, de um mesmo _conceito_ podem surgir diferentes abstrações.

Já _hipótese_ é uma suposição, uma etapa que surge, no início do método científico, após a observação e elaboração de um problema. 

[![Representação do Método Científico](https://i.pinimg.com/736x/13/e2/b5/13e2b5f64d00dab5e5b487d765f7730b.jpg)](https://www.nerdcursos.com.br/metodo-cientifico)

Com base nisso, segue dois sites para auxílio na criação de modelos mentais para soluções de problemas de software: 
- [Refactoring.Guru](https://refactoring.guru/pt-br) com foco em padrões de código.
- [Patterns for API Design](https://microservice-api-patterns.org/) com destaque para padrões arquiteturais.

### Exemplo de Modelo Mental by Lucas

Então vamos ao meu modelo mental para o problema que está acontecendo:

> Descrição do problema > hipótese de qual pode ser a causa desse problema > solução.

##### Abstração

- Existe um `sistema de arquivos` na minha máquina local -- meus arquivos e pastas. 
- Existe uma `representação de um sistema de arquivos` da cópia local do meu repositório -- onde o Git, de alguma forma mágica (e que não convém pra gente no momento), armazena o histórico de alterações da parte do meu `sistema de arquivos` que está sendo controlada pelo git.
- Não está havendo uma `sincronização` entre ambos. Estou removendo um arquivo/pasta no meu `sistema de arquivos`, mas essa alteração não está refletindo na `representação de um sistema de arquivos` do Git.

##### Hipótese

> Agora, vou criar uma descrição do que eu acredito que está acontecendo, com base nos conceitos que eu modelei na minha abstração. Se algo ficar faltando, é sinal de que falta modelar mais algum conceito, ou propor uma nova modelagem que faça mais sentido.

- Quando removo um arquivo no GitHub, de alguma forma ele sincroniza as alterações realizadas no `sistema de arquivos` e na `representação do sistema de arquivos` do git
- Preciso encontrar uma forma de `sincronizar` meu `sistema de arquivos` e a `representação do sistema de arquivos` do git

##### Solução 

- `rm arquivo.txt` remove um arquivo apenas no meu `sistema de arquivos`
- `git rm --cached arquivo.txt` remove um arquivo apenas na `representação do sistema de arquivos` do git
- `git rm arquivo.txt` remove um arquivo tanto no meu `sistema de arquivos` quanto na `representação do sistema de arquivos` do git


Em um corpo, cada parte serve pra alguma coisa. Existe uma lógica natural por trás
Nós temos duas pernas com pés e dedos porque essa é uma maneira eficiente de equilibrar todo o resto 
E liberar os braços pra manipulação de objetos
Ao mesmo tempo, lá na outra ponta, o peso da cabeça influencia na questão do equilibrio. Então ela não pode ser subdesenvolvida, pra não prejudicar as capacidades, mas também não pode ser superdesenvolvida, porque daí o individuo teria dificuldade pra ficar em pé
Então todas as coisas estão conectadas, e mesmo que as responsabilidades sejam separadas entre si, as partes influenciam umas nas outras
Agora deixando a analogia da anatomia de lado
Outra coisa que eu quero que você visualize é a interface como uma representação da modelagem dos dados
No seguinte sentido, por exemplo: um processo aquisitivo pode ser de diferentes modalidades, e possui lotes que por sua ver possuem itens

Uma interface bem modelada vai representar esses detalhes de maneira semelhante a como eles foram modelados conceitualmente
No nosso caso, a mudança da modalidade não muda o processo como um todo. Apenas aplica algumas pequenas variações na sua apresentação (assim como pessoas de etnias diferentes continuam sendo pessoas, mas com algumas características físicas e culturais diferentes)
Já os lotes e os itens são coisas que o processo possui. Então elas são representadas como estando "dentro do processo"
lotes dentro do processo, e itens dentro dos lotes

Então existe uma justificativa conceitual para as escolhas visuais que a gente toma
Por que é importante que você pense dessa maneira: porque dessa forma você se torna mais conciente na hora de pensar e participar da modelagem dos pitchs. Não que você não esteja apresentando um bom entendimento dos pitchs. Você está. Mas pra chegarmos no próximo nível, é importante que você consiga ver além dessa forma
Daí você vai conseguir participar mais de igual pra igual, sugerindo mudanças na UX/UI talvez, inclusive

Por isso que acredito que você dominar os detalhes da legislação do processo ou de cada cabelinho de requisito que ele possui não é a nossa maior necessidade, e por isso comentei que isso poderia ser usado como combustível.Se tivermos um modelo bem definido, voltando a pensar na analogia do corpo, cada detalhe vai ser atendido no seu momento devido, sem que isso prejudique a nossa compreensão do todo. 

Por exemplo, até hoje o ser humano não entendeu muito bem como a própria cabeça funciona. Mas isso não o impede de criar abstrações do que é essa mente (vulgo psicologia) ou de realizar suas tarefas utilizando essa cabeça 
Aqui vai ser a mesma coisa. A gente precisa ter um bom andamento da nossa modelagem mesmo sem entender completamente os detalhes de determinado requisito de antemão. Daí o Richard entra apoiando a gente com esse lado da coisa, enquanto a gente garante que o nosso modelo (tanto visual quanto conceitual) está suportando esses detalhes novos que vão surgindo




