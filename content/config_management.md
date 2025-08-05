---
title: config_management
description: Conteúdo sobre Gerência e Configuração de Software
pubDate: Mar 17 2025
tags:
  - Git Flow
  - Semantic Versioning
  - Git
  - GitHub
  - Conventional Commits
  - GCS
  - CI/CD
---
<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=8a0303&height=120&section=header"/>

# Sumário
- [Git Flow](#git-flow-)
- [GCS - Anotações de Aula](#gcs---anotações-de-aula-️)

# Git Flow 🔴🠒🟢
Foi criado em 2010 pelo holandês Vincent Driessen. Trata-se de uma estratégia de workflow utilizada para organizar o versionamento de código no repositório, mantendo a segurança. Para compreendê-lo mais  facilmente, é possível visualizá-lo como uma árvore e seu ramos, isto é, um grafo.

A branch master é a faz o intermédio entre o repositório e o servidor de produção. Como não é recomendado fazer commit de correção de bugs diretamente na master, são criadas algumas branches. Nessa perspectiva, o intuito do Git Flow é evitar conflitos quando há vários programadores trabalhando no mesmo projeto. Então, sempre que é necessário adicionar uma feature ou corrigir um bug, cria-se uma branch (ramificação).

Depois que as alterações nas branches são totalment testadas, é feito merge com a master. O Git Flow prevê dois tipos de branches: a principal (master e develop) e as de suporte (feat, release e hotfix). A branch master fica para envio de todas as novas features. Então a develop é criada a partir da Master e ela precisa ter todas as features estáveis uma branch de release. Já as branches de features são criadas a partir da Develop.

Sobre a nomenclartura, é importante anotar que quase todas as estratégias de branching usam uma padronização do tipo `feature/nome-da-feature`. A branch release vai acumulando as features até que se possa lançar uma nova versão para a master com merge. A partir disso, a master recebe uma nova tag de versão.

Há ainda a branch hotfix, também feita a partir da master. O propósito dela é corrigir bugs. Após testado, o merge dela é feito diretamente na master, estreando também uma nova tag. Ao término de tal procedimento, a brach hotfix deve ser removida. Enquanto isso, a branch develop deve estar sempre atualizada com a master.

Algumas críticas ao Git Flow mencionam complexidade e burocracia. Além disso, defendem que é insustentável, ineficaz, que o próprio criador não recomenda o Git Flow atualmente e que o git Flow gera merges automáticos com resolução de conflitos e commits inúteis.

A seguir, uma ilustração que ajuda a compreender o Git Flow.

```mermaid
gitGraph TB:
    commit
    commit
    branch develop
    commit
    branch feature
    commit
    commit
    commit
    checkout develop
    merge feature
    commit
    branch release
    commit
    checkout main
    commit
    checkout release
    merge main
    checkout develop
    merge main
```

# Padrões de Versionamento 🏗
Os padrões de versionamentos visam gerenciar mudanças significativas nas aplicações, seguindo certa hierarquia.
A seguir, são apresentados alguns padrões e comparações entre eles.

## Semantic Versioning
Esta é a padronização mais utilizada, visto que é de fato sucinta, clara e abrangente, sendo capaz de representar a maioria dos projetos, na minha opinião.

Funciona da seguinte forma, segundo a própria especiaficação:
>" Dado um número de versão MAJOR.MINOR.PATCH, incremente a:
> - versão Maior(MAJOR): quando fizer mudanças incompatíveis na API,
> - versão Menor(MINOR): quando adicionar funcionalidades mantendo compatibilidade, e
> - versão de Correção(PATCH): quando corrigir falhas mantendo compatibilidade.
Rótulos adicionais para pré-lançamento(pre-release) e metadados de construção(build) estão disponíveis como extensão ao formato MAJOR.MINOR.PATCH."

[TEXTO COMPLETO AQUI](https://semver.org/lang/pt-BR/)

## CalVer 📆
O CalVer baseia-se em datas para realizar o versionamento, prevendo versões com data específica (formato AAAA.MM.DD), versões mensais (formato AAAA.MM) e versões semanais (formato AAAA.SS). Tal padrão atende necessidades muito específicas em contextos que têm as datas como algo significativo.

É comparado ao SemVer por prever números inteiros separados por ponto.

## Sentimental Versioning
Ao contrário do SemVer, este não tem especificação formal, apenas um guia com sugestões. Segundo ele, o padrão criado deve ser original, com números apreciáveis ao autor, e explicado se for algo belo, caso contrário, as novas versões são improvisadas conforme o humor momentâneo.

## FloatVer 
Este é um esquema de versionamento que utiliza números de ponto flutuante não negativos com tamanho IEEE754 32-bit. O formato é `breaking.nonbreaking`:
- breaking: incrementa 1 quando a mudança torna a versão incompatível com as anteriores.
- nonbreaking: incrementa 1 quando a mundança não afeta a compatibilidade com versões anteriores, isto é, não demanda mais RAM, cores do processador ou tempo de execução, nem altera a semântica da versão anterior.

É um padrão menos específico que o SemVer e utiliza números float, ao invés de inteiros.

# Conventional Commits
Alguns tipos de commits:
- feat: that add or remove a new feature to the API or UI
- fix: that fix a API or UI bug of a preceded feat commit
- ref: that rewrite/restructure your code, however do not change any API or UI behaviour
- perf: are special refactor commits, that improve performance
- style: that do not affect the meaning (white-space, formatting, missing semi-colons, etc)
- test: that add missing tests or correcting existing tests
- docs: that affect documentation only
- build: that affect build components like build tool, ci pipeline, dependencies, project version, ...
- ops: that affect operational components like infrastructure, deployment, backup, recovery, ...
- chore: commits e.g. modifying .gitignore

# Anotações sobre Git e GitHub 😼🐙
Git é uma técnica de versionamento de código criada por Linus torvalds. Ela permite que os desenvolvedores acompanhem as mudanças no código fonte ao longo do tempo, mantendo um histórico de todas as mudanças, versões criadas, ramificações, entre outros dados. É necessário, para utilizar localmente, instalar e configurar o Git Bach na máquina.
Já o Github é uma plataforma hospedada em nuvem que permite a manipulação com Git de maneira remota e compartilhada.

Para criar uma conta no github é necessário clicar em “Sign up”, inserir e-mail, criar nome de usuário e senha. Então, após validação do e-mail é preciso realizar o login e preencher os formulários que surgem informando seus interesses com a plataforma. Em seguida, a fim de garantir uma boa experiência no sistema, é importante personalizar a interface e as preferências nas configurações.

Durante a utilização, é possível deparar-se com o Markdown, que é uma linguagem simples de marcação capaz de converter um texto em HTML válido. É uma forma mais simples de se escrever um HTML, e um arquivo com tal linguagem tem extensão `.md`.

> Consulte a página disponível na [âncora](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) para saber mais sobre Markdown.

GIST: são repositórios Git. São muito parecidos com o Github, porém ele permitem o compartilhamento de arquivos e trechos de código com outros desenvolvedores, mesmo que o usuário não seja o autor original do código. É possível criar um GIST por meio do próprio Github.

![Git e GitHub](https://arquivo.devmedia.com.br/marketing/img/guia-git-e-github-37585.png)

## Principais Comandos
A seguir, anotações sobre certos comandos iniciais para utilizar no terminal do Git Bash.

```mermaid
flowchart TB
    A(Diretório de Trabalho)-->|add|B("Index (ou Stage)")
    B-->|commit|C(Repositório local)
    C-->|merge|A
    C-->|push|D(Respositório remoto)
    style A stroke:#fff,fill:#d71b09
    style B stroke:#fff,fill:#d71b09
    style C stroke:#fff,fill:#d71b09
    style D stroke:#fff,fill:#d71b09
```
----

- `git commit -am ""` para fazer add e commit em apenas uma linha de comando. O “add” coloca a alteração dentro do contêiner antes de adicionar à master. 
- `git log` mostra todos os commits realizados, detalhadamente.
- `git log --oneline` mostra todos os commits com apenas os nós e a mensagem.
- `git diff` serve para visualizar todas as mudanças, o que foi removido e o que foi acrescentado.
- `git reset --hard endereçoDeMemória` serve para remover o último commit e voltar à versão anterior, indicando o hash dela.
- `git status`  mostra o que tem no contêiner ou indica o comando para descartar mudanças e voltar à versão anterior.
- `git log --graph` mostra os nós.
- `git checkout master` retorna à última versão do projeto.
- `git log - -oneline  --graph` mostra tudo organizado e resumido.
- `git log --oneline  --graph  --all` mostra informações de todos os ramos.
- `q` para quando o terminal trava o cursor.
- `git merge nomeDoRamo` serve para fundir um ramo em outro.
- `git --abort` serve para abortar processo de fusão dos ramos.
- `git remote` verifica a existência de um repositório remoto.
- `git remote -v` para detalhes sobre o repositório remoto.
- `git clone linkDoRepositório` quando é criado um repositório, marcando a opção de adicionar README, e deseja-se clonar no windows, após selecionar git Bash here em alguma pasta.
- `ls -a` serve para visualizar pastas ocultas.
- `touch pastaCaminho/nomeArquivo.extensao` cria um arquivo dentro de uma pasta.
- `git push` para enviar alterações (commit) feitas no repositório de forma local para o repositório remoto, no GitHub.
- Para criar uma nova pasta no git hub, é preciso digitar o nome da pasta e uma barra “/”, então eve-se escrever o nome do arquivo que queira colocar.
- `git pull` serve para atualizar as mudanças feitas dentro do Git Hub no repositório local (a pasta no computador). Mostra possíveis conflitos entre branchs para consertar depois. Basta clicar na âncora do menu para escolher a versão, isso ocorre no vscode.
- `git fetch` serve para fazer download das alterações feitas no repositório remoto (alterações já feitas em outro repositório local, mas que não foram atualizadas neste outro repositório local aberto).
- `git config --global core.editor code` para configurar o VSCode como IDE padrão.
- `Fork`: é quando um projeto é clonado para o github, para fazer qualquer tipo de alteração no projeto clonado, sem alterar o projeto original.
- `Pull Request`: é uma forma de contribuir com os projetos da comunidade. Nele, é possível sugerir alguma alteração no projeto original, para o dono do projeto aprovar ou não.
- `git checkout hashDoCommit` retorna o código para a versão escolhida.
- `git branch` mostra o hash anterior da master e para onde foi apontado. Mostra qual o ramo atual.
- `git checkout -b nomeDoRamo` serve para criar uma nova ramificação do projeto (branch), a partir da branch atual, e já mudar para ela. A master é o ramo criado automaticamente pelo GIT. O novo ramo herda todos os commits de master.
- Para commitar na minha branch: faz o git add ` normal, depois o commit normal também, em seguida roda o git push origin soraya. 
- `git pull origin nomeDaBranch` para atualizar as alterações feitas na minha própria branch para o repositório local.
- `git branch nomeDaBranch`: apenas cria uma nova branch. É aconselhável criar sempre a partir da main/master.
- `git branch -d nomeDaBranch`: serve para deletar uma determinada branch.
- `git checkout nomeDaBranch`: serve para mudar de branch. Obs.: leva junto os arquivos em commit para o novo branch.
- O `git stash` salvará suas mudanças locais em uma pilha de alterações temporárias. Após o pull, pode-se trazer essas mudanças de volta com git stash pop. Commit: Se as mudanças estão prontas para serem salvas permanentemente, é possívle comitar as alterações e, em seguida, puxar as mudanças remotas:
```bash
git add .
git commit -m "Salvando mudanças locais"
git pull
```
- Forçar o pull (sobrescrever mudanças locais): Se não precisa das alterações locais e deseja sobrescrevê-las com as mudanças remotas, pode-se forçar o pull com a flag --hard:  O comando git reset --hard HEAD irá descartar todas as alterações locais não comitadas.
```bash
git reset --hard HEAD
git pull
```
- `rm arquivo.txt` remove um arquivo apenas no meu sistema de arquivos
- `git rm --cached arquivo.txt` remove um arquivo apenas na representação do sistema de arquivos do git
- `git rm arquivo.txt` remove um arquivo tanto no meu sistema de arquivos quanto na representação do sistema de arquivos do git
- `git rebase origin/feat/authn` serve para reaplicar commits, isto é, pegar commits de um branch e aplicá-los em outro branch como se fossem novos commits, evitando commits de merge. Além disso, ele serve para sincronizar um brach de trabalho seu com a base atual de um branch alvo.
- **Resolvendo conflitos**: 
> Eu gravei um vídeozinho resolvendo um conflito no git manualmente.

> ![vídeo](../media/Solve_Conlict_GIT.mp4)

> Mas o processo é basicamente rodar `git pull origin [branch de origem da PR]` na branch que você tá tentando realizar a PR com conflito.
> Nesse caso eu estava na `feat/centobank-transacao`, então foi `git pull origin dev`. Por que a dev é a "branch de origem" da minha branch. 1. Daí quando você faz isso o git exibe no terminal o processo de tentar realizar o merge automático das alterações. Mas em alguns casos ele não vai conseguir, e vai reclamar com "CONFLICT". Então você vai passando por cada um desses arquivos, onde você vai encontrar trechos de código marcados com [1] a versão que você estava trabalhando (current) e [2] a versão que está vindo da atualização que você está tentando fazer (incoming). O seu papel é decidir qual das duas vai manter. No VSCode tem uma extensão muito boa pra dar uma força nessas coisas, que é o [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) mas é legal que você saiba fazer manualmente também. Finalizado tudo, é só dar o `git add` de sempre e um `git commit` sem `-m` mesmo, que o próprio git já vai preencher a mensagem com a mensagem padrão de merge ("Merge branch 'dev' github.com:cento-software/bufunfa into ..."). Daí quando você faz isso o git exibe no terminal o processo de tentar realizar o merge automático das alterações. Mas em alguns casos ele não vai conseguir, e vai reclamar com "CONFLICT". A chave é acompanhar cada um dos CONFLICTs direitinho pra não deixar nada passar. O ideal é sempre testar depois de um merge desse pra garantir que você não deixou nenhum conflito pra resolver. Quando você já sabe o que precisa manter e o que não, fica bem mais fácil. Nesse caso aí, eu sabia que a maioria das novidades era por causa do merge da parte de authn na dev. Então foi só aceitar as alterações nos repositories e nas páginas/endpoints de autenticação e reorganizar os scripts do banco.

# GCS - Anotações de Aula 🏭️👩‍💼

* Em Gerência e Configuração de Software, nós não gerenciamos apenas o código, mas também o protótipo, os requisitos, etc.  
* Pra além do código do modelo, temos que versionar também o registro do modelo, e o código do modelo.   
* **Configurar**: atribuir formas diferentes a uma representação que entrega valor para um caso específico. Atribuir forma a algo para dar representatividade a alguém.  
* **Release**: uma representação que tem valor para algo ou para alguém.  
* **Gerência**: planejamento, organização, controle e aplicação de princípios com o intuito de maximizar a utilização dos recursos.  
* **Processos** em métodos ágeis são **abordagens.**  
* **Engenharia de Software:** é a aplicação de uma abordagem sistemática, disciplinada e quantificável, para o desenvolvimento, operação e manutenção do software.  
* Segundo a norma, **Gerência de Configuração é** um conjunto de atividades de apoio que lida com as mudanças inerentes ao desenvolvimento de software, mantendo a integridade e a estabilidade durante a evolução do projeto. “Processos que suportam a identificação única, o armazenamento controlado, versões controladas e relato de produtos de trabalho, componentes, durante a vida de um sistema de software”. Gerência de Configuração é um processo de gerência da tecnologia da informação que rastreia itens individuais de configuração de um sistema de informação.  
* **Build != Release.** Ninguém manda build pra produção, o que se manda é release.  
* **Versão:** forma ou variação de algo. É diferente de apresentação ou edição de um texto, filme, software etc. Refere-se a uma identificação específica.  
* **Hand-off:** nós temos uma equipe que precisa desenvolver logo… É fazer uma parte da equipe caminhar mais rápido para que a outra parte possa fazer a parte dela, por é dependente. Vc tem que caminhar a frente porque alguém precisa da sua entrega, e se vc não fizer isso, a outra parte da equipe fica bloqueada. Sendo assim, uma parte da equipe ficará altamente sobrecarregada por um tempo.  
* **Principais tarefas:** definir e implementar processo; identificar configuração; controlar configuração; relatos da situação da configuração; avaliação de subcontratos e fornecedores; controlar terceiros, fornecedores.  
* **Itens de Configuração (IC):** são itens (contendo informação) selecionados para controle das versões. É como se fosse um quebra-cabeça, precisa ser controlada a mudança, esse é um item de configuração. É um artefato de software que precisa ser gerido a fim de entregar um produto ou serviço de software.  
* **Barrier Artefact:** é um artefato que permite a transmissão de informação entre equipes diferentes.  
* **Item de Configuração:** é um artefato de software que precisa ser gerido a fim de entregar um produto ou serviço de software. Se eu sei que um artefato vai sofrer muitas mudanças que precisam ser controladas, então esse artefato é um item de configuração.  
* **Artefato:** é um elemento artificial que concretiza a visão que temos do minimundo (o nosso domínio). Ex.: issues, modelo, protótipos, modelo arquitetural, um README, especificações, templates etc.  
* Em GSC, queremos que nossos desenvolvedores estejam trabalhando no mesmo momento, ou que possam escolher em que momento vão trabalhar.  
* **Device Farming:** é um tipo de teste para sistemas mobile.  
* **SRE \- Site Reliability Engineering:** serve para sistemas de altíssimo alcance e alta confiabilidade.  
* **Release Engineering:** você deve conseguir gerar uma release em menos de duas horas.  
* **Spike:** é uma história de usuário de estudo (coisas que a equipe precisa estudar).  
* **Rollback:** é quando você volta uma versão.  
* **Commit:** é submeter contribuição, não alteração simplesmente.  
* Uma versão do tipo **Revisão** substitui a versão anterior. Já uma **Variante** não substitui, ela pode coexistir. O windows 11 é uma revisão, diante das versões anteriores.  
* **Repositório**: local onde os itens de configuração são armazenados.  
* **Baseline:** forma (configuração) que precisa ser revisada e aprovada para que eu possa iniciar uma etapa no projeto. Configuração revisada e aprovada que serve como base para uma próxima etapa de engenharia e que somente pode ser modificada via processo formal de GCS. São estabelecidas ao final de cada fase de desenvolvimento: análise (funcional), projeto (allocated) e implementação (product).  
*  Um elemento mais básico da baseline de um protótipo pode ser o **Design System**.   
* **Building:** é um processo de compilação e transpilação de geração de pacotes, configurações alvo. P. ex., é uma confirmação da configuração, para que ela seja uma versão executável: pom.xml. Confirma que o processo de configuração funciona. Utiliza arquivo de comandos que descreve como deve ocorrer a construção.  
* **Release:** versão disponibilizada para um propósito específico. *Ela tem representação para alguém, que não necessariamente o usuário, mas talvez algum stakeholder.* Toda liberação é uma versão, mas nem toda versão é uma liberação. *Nem toda versão é um release.*  
* **Engenharia de Plataforma:** aplicação de princípios do DevOps para melhorar segurança, compliance, custos e tempo de entrega, por meio de autoatendimento e melhor experiência para desenvolvedores.  
* As avaliações de apps, como as da app store, são **solicitações**.

## Atividades da GCS:
  * Planejar o gerenciamento de configuração;  
  * Executar a identificação da configuração;  
  * Gerenciar alterações de configuração;  
  * Executar controle de liberação;  
  * Executar a contabilidade do status da configuração;  
  * Realizar avaliação de configuração (auditorias)

## CONTROLE DE VERSÃO E CONTROLE DE MUDANÇA

* **Controle de Versão:** é importante porque apoia o desenvolvimento de diversas maneiras; permite colaboração concorrente; Registro de histórico; variação no projeto; apoia atividades de controle de mudança e integração/entrega/implantação contínua.  
* **Mudança** é uma modificação planejada, que estudamos, analisamos e trazemos para nosso projeto.  
* Perguntas importantes: Por que o sistema mudou **(controle de mudanças)**? Quais foram as mudanças **(controle de versão)**? O sistema continua funcionando depois das mudanças **(integração contínua)**?  
* **Gerenciamento de mudanças** é um processo utilizado para identificar, avaliar, aprovar, implementar e acompanhar modificações em itens de configuração ao longo do ciclo de vida do software. Identificação, registro, avaliação, aprovação, implementação e acompanhamento de todas as alterações realizadas nos artefatos de software ao longo do ciclo de vida do projeto e nos processos.  
* Se foi pra produção, está na fase de manutenção e evolução, se não, está na fase de desenvolvimento. Nós devemos controlar as mudanças ATÉ NA FASE DE MANUTENÇÃO E EVOLUÇÃO.  
* CICLO DE VIDA DO DESENVOLVIMENTO DE SOFTWARE (SDLC): planejamento \> análise de requisitos \> projeto \> implementação \> teste \> implantação \> manutenção e evolução.  
* A Descoberta de Produto, Lean Inceptions são abordagens da engenharia de requisitos que têm muita **divergência e convergência.** Eles buscam pontos de divergência.  
* Um elemento que ajuda no **paradoxo da escolha** é ter uma estratégia básica que é ter rotular as issues, isto é, colocar labels nas issues.  
* **Auditoria de Gerência de Configuração:** garantir a conformidade com os padrões e práticas estabelecidos; Identificar áreas de melhoria nos processos de gerência de configuração; assegurar a integridade e rastreabilidade das configurações de software; aspectos avaliados (conformidade com os processos estabelecidos, integridade e rastreabilidade das configurações; adequação da documentação de configuração; eficácia dos controles de versão e mudança).  
* **issue:** acompanhar o trabalho, dar ou receber feedback, colaborar com ideias ou tarefas e se comunicar eficientemente com outras pessoas. Usadas para relatar bugs e sugerir novas funcionalidades. Muitas equipes organizam o desenvolvimento associando issues e pull requests. Tornaram-se elemento central on controle do ciclo de vida do software. **Estrutura básica:** contexto, problema, solução ou próximo passo. Descrição clara, mudança é auto-contida, limites de habilidades necessárias para resolução, carga de trabalho baixa.

## SEVERIDADE E PRIORIDADE

* **Prioridade** é sempre *agendamento*, algo merece atenção prévia. Significa algo que merece atenção prévia.  
* **Severidade** é sobre *padrõe*s, se um padrão é rigoroso, ele não pode ser abandonado. Severidades: crítico, major, minor, enhancement. É o estado ou qualidade de ser severo; severo implica adesão a padrões rigorosos ou princípios elevados e frequentemente sugere aspereza.  
* Prioridades: alta, média e baixa.  
* **issue tossing** é quando a gente tem que ficar trocando o responsável por resolver a issue, normalmente porque você não conhece bem as pessoas e as capacidades das pessoas na equipe.

## CONTROLE DE VERSÃO

* O **controle de versão** é composto de duas partes: repositório e área de trabalho.  
* O **repositório** tem os itens de configuração \+ o histórico de versões dos itens. A área de trabalho não armazena o histórico. O repositório contém os arquivos versionados e os commits.  
* A **área de trabalho** é onde você edita o código, por exemplo, na IDE.  
* **Commit** é o registro permanente de um conjunto de alterações feitas em arquivos, criando uma nova revisão no repositório. A esfera do desenho representa um conjunto de commit. Representa o encerramento de uma unidade lógica de trabalho, permitindo rastreabilidade, reversão e colaboração no desenvolvimento de software. É algo que ocorre apenas no repositório local, e não no remoto.  
* **Update:** é o processo de atualizar a cópia de trabalho local com as alterações mais recentes que foram committadas no repositório central por outros devs.  
* **hook:** é algo que está no .git.  
* Há tipos de repositórios:  
  * Controle centralizado: há um único repositório central armazenado em um servidor, e os desenvolvedores acessam esse servidor para obter a versão mais recente dos arquivos. É muito rigoroso, cheio de regras, depende de conexão de rede, tem um único repositório, o histórico das alterações ficam só no rep central, é uma fonte autoritária. Desvantagens: dependência do rep central, ponto único de falha. Vantagens: controle de acesso, cópia de segurança, controle de qualidade.  
  * Controle distribuído: cada dev tem a área de trabalho e um **repositório local**, atua com arquitetura peer-to-peer. Permite que os devs trabalhem de forma independente e offline, realizando commits localmente e sincronizando com os reps dos outros. Vantagens: rapidez, autonomia, confiabilidade, redução de custos com servidor.  
* **git fetch:** atualiza apenas o histórico de versão e não gera conflito nenhum.  
* A identificação das coisas são chaves **hash**. Quando você faz commit é gerado um idenficador, que é colocado em algum lugar da tabela hash,   
* Uma branch que tem commits demais pode ser um **átomo de confusão.** Não faça ramificações de longa duração. Isso pode gerar: perda de contexto, diminuição de colaboração, risco de regressões, dificuldade de teste, conflitos complexos.


## MODELO DE RAMIFICAÇÕES

* **Ramificação:** é um ponteiro para um conjunto de alterações feitas. É um ponteiro móvel para um commit.  
* O sistema de versionamento não leva em consideração a estrutura do código, apenas o texto.  
* O snapshot é uma “fotografia” de um determinado estado do código.  
* Vantagens: modificar os IC sem alterar a master; “desligar” facilmente funcionalidades etc; permite várias pessoas trabalhando ao mesmo tempo; evita conflitos;  
* Quando a gente a lida com mesclagem é importante saber lidar com a dívida técnica  
* HEAD significa que qualquer coisa que for commitada a partir de agora será feito a partir desse head.  
* O \* do \`git branch\` indica onde está o head.  
* O \`git switch\` permite troca entre branches e criação de branches. Ele faz uma espécie de stash.  
* O pull request é uma solicitação de contribuição.   
* É uma boa prática sempre realmente aprovar uma PR, realizando comentários.  
* **O que é feature?** não é apenas a funcionalidade, pode ser algo que precisamos trabalhar numa ramificação para que outro colega possa terminar a parte dele. Existe um artigo discutindo o conceito de feature.  
* **Feature Branch Workflow:** a partir do ramo principal são criadas branches para as features que precisam ser criadas. Esse modelo é pouco sofisticado e exige alta maturidade e entendimento da equipe. Quanto mais próximo o modelo estiver da branch principal, mais ele exige maturidade e  conhecimento da equipe.  
* A gente pode estabelecer uma política de exigência ou não de PRs para determinadas branches.  
* **Git flow:** Feature branch \> Develop \> Release Branch \> Hotfix \> Main  
* No git hub flow é obrigatório haver uma estratégia de implantação contínua, é um critério do modelo.  
* **Git lab flow:** tem as branches de ambiente. Ele é uma plataforma, o git lab.   
* **Trunk-based:** exige altíssima maturidade da equipe, pois as branches das extremidades estão bem próximas do usuário. É preciso garantir que as entregas mantêm a estabilidade. Demanda critérios muito bem definidos.   
* Crie o hábito de utilizar o **git status**. **Conteúdo imutável**: uma vez criado, o conteúdo de um **blob** não pode ser alterado. Cada blob é identificado pelo hash.   
* O padrão de commits semânticos do Angular é o mais utilizado, mas dá pra usar o da microsoft também ou criar o seu próprio.  
* Quando você está num projeto com muitas pessoas, não é recomendado utilizar o rebase.

## CI/CD - Continuos Integration & Continuos Delivery

* CD envolve tanto delivered e deploy.  
* A **build** é quando a olha para os elementos de configuração. Está mais ligada à CI.   
* CI: não lida com nenhum aspecto de release. Ajuda o time a ver logo o formato do produto. A release é algo que entrega valor para alguém.   
* A medida que você faz uma contribuição é interessante que haja mecanismos de análise da sua contribuição.  
* Não existe entrega contínua sem implantação contínua.  
* Se você fizer um commit e ele passar no CI, ele será implantado automaticamente.  
* Você só vai implantar aquilo que estiver na branch principal.  
* Integração contínua é uma cultura. Se nem todo mundo da equipe tiver essa cultura, não adianta fazer esteira. Ela prega que cada desenvolvedor deve integrar código em um repositório compartilhado várias vezes ao dia.  
* Se você não souber pensar de forma atômica, você não é um engenheiro eficiente. A gente tem que ter visão do todo: do time, do negócio.  
* O quanto o teu time entrega valor rapidamente.  
* É um antipadrão haver um evento, uma cerimônia para integrar código.  
* Você só pode ter CD se você rodar a esteira de CI.  
* 


<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=008000&height=120&section=footer"/>