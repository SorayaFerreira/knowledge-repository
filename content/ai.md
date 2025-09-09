---
title: ai
description: Conteúdo sobre Inteligência Artificial
pubDate: May 05 2025
tags:
  - Prompt
  - Redes Neurais
  - IA
---
<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=800080&height=120&section=header"/>

# Sumário
- [Engenharia de Prompt](#engenharia-de-prompt)
- [Artigo: Júniors 🆚 LLMs](#artigo-júniors--llms)
- [Redes Neurais – Overview](#redes-neurais--overview)

# Engenharia de Prompt 👾

- https://platform.openai.com/docs/guides/text?api-mode=responses

- IA Responsável e Segurança: É fundamental "criar com responsabilidade", utilizando um "Kit de ferramentas de IA generativa responsável" e um "Framework seguro de IA". As "Configurações de segurança", "Orientações de segurança", "Políticas" e "Termos de Serviço" são pilares para garantir o alinhamento do uso da IA com as diretrizes da B3.
- Instruções Claras e Específicas: Para personalizar o comportamento do modelo de forma eficaz e eficiente, forneça instruções claras e específicas. Isso minimiza a ambiguidade, ajuda o modelo a produzir os resultados esperados e é vital para a conformidade e auditoria. Você pode usar restrições para guiar o modelo sobre o que fazer e o que não fazer, como especificar a duração de um resumo.
- Formato da Resposta Definido: É possível dar instruções que especifiquem o formato da resposta, como tabela, lista com marcadores, JSON, frase ou parágrafo. Isso é essencial para a integração de dados nos sistemas de governança e para a padronização de relatórios. A estratégia de conclusão parcial pode ser usada para formatar respostas, iniciando um formato e deixando o modelo concluí-lo.
- Prompting de Poucas Imagens (Few-Shot Prompting): Para garantir consistência no formato, fraseado e escopo das respostas, é altamente recomendado incluir exemplos (few-shot examples) nos comandos. Isso ajuda o modelo a identificar padrões e aplicá-los, garantindo a padronização necessária para a governança. A consistência no formato dos exemplos é crucial, prestando atenção a tags XML, espaços em branco e novas linhas.
- Adição de Contexto: Inclua informações e contexto que o modelo precisa para resolver um problema, em vez de presumir que ele tem todo o conhecimento necessário. Isso garante que o modelo utilize dados e regras aprovadas pela B3, reduzindo "alucinações" e assegurando a veracidade das informações, o que é vital para a governança de dados.
- Prefixos: A adição de prefixos (como "JSON:" para sinalizar o formato de saída ou "Texto:" para demarcar a entrada) ajuda a demarcar partes semanticamente significativas da entrada ou a indicar o formato esperado da saída, auxiliando na estruturação controlada dos dados gerados.
- Divisão de Comandos em Componentes: Para casos de uso complexos, você pode dividir as instruções em componentes mais simples ou usar comandos encadeados, onde a saída de um comando se torna a entrada do próximo. Isso pode melhorar a rastreabilidade e a capacidade de depuração, facilitando a governança do processo de IA.
- O que Evitar: É crucial evitar depender dos modelos para gerar informações factuais sem verificação e usá-los com cuidado em problemas matemáticos e lógicos.
- Instruções Claras para Tonalidade e Interatividade: As instruções podem ser usadas para mapear a experiência e a mentalidade de um usuário, o que é útil para criar interações com uma "vibe" específica (ex: formal, informal, analítica). Uma instrução de sistema pode informar ao modelo para ser mais interativo ou responder de forma mais abrangente.
- Formato da Resposta para Estilo: A capacidade de pedir que a resposta seja formatada como um "argumento rápido de venda" ou "palavras-chave" permite direcionar o estilo e a concisão da saída, moldando a "vibe" da comunicação para diferentes públicos (ex: investidores, startups, equipes internas de inovação).
- Few-Shot Prompting para Consistência de Estilo: Ao fornecer exemplos, você pode guiar o modelo a dar preferência a respostas concisas ou detalhadas, garantindo que a "vibe" das suas comunicações seja consistente.
- Estratégias de Iteração de Prompt para Refinamento: O design de comandos é um processo iterativo.
    - Usar frases diferentes no comando pode gerar respostas distintas, permitindo refinar a linguagem e o tom para alcançar a "vibe" desejada.
    - Mudar para uma tarefa análoga pode ajudar a encontrar uma estrutura de prompt que naturalmente elicita a "vibe" desejada (e.g., reformular como pergunta de múltipla escolha para uma resposta mais direta).
    - Mudar a ordem do conteúdo do comando também pode afetar a resposta e deve ser testado para otimizar a "vibe".

## Passos para Escrever um Bom Prompt:
1. Defina um papel: estimule a ferramenta a assumir um papel.
2. Forneça o contexto;
3. Zero-Shot: consiste em prover uma descrição da tarefa no promptsem fornecer nenhum.
4. One-shot ou few-shot: consiste em fornecer exemplos para receber uma resposta que segue o mesmo padrão. 
5. Estimule o raciocínio passo a passo (chain-of-thought)
6. Para tarefas mais complexas, peça uma reflexão (step-back prompting)

# Redes Neurais – Overview
> Livro: An Introduction to Neural Networks, by Kevin Gurney

- Uma **rede neural** é um conjunto interconectado de simples elementos de processamento, unidades ou nós, cujas funcionalidades vagamente se baseiam no fucionamento do neurônio biológico. A habilidade de processamento da rede está armazenada nas forças de conexão interunidade, ou pesos, obtidos num processo de adaptação, ou aprendizado, a um conjunto de padrões de treinamento.

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=800080&height=120&section=footer"/> 