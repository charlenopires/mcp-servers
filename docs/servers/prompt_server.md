# Servidor de Engenharia de Prompts

## 📋 Visão Geral

O Servidor de Engenharia de Prompts é uma implementação MCP (Model Context Protocol) especializada em técnicas avançadas para otimização, análise e geração de prompts de alta qualidade. O servidor fornece ferramentas para melhorar a eficácia dos prompts para diferentes tarefas e modelos.

![Engenharia de Prompts](../assets/prompt_engineering.png)

## 🎯 Propósito

Este servidor foi desenvolvido para ajudar usuários a criar prompts mais eficazes através da aplicação de técnicas de engenharia de prompts. O servidor analisa a estrutura dos prompts, identifica oportunidades de melhoria e aplica estratégias específicas para diferentes tipos de tarefas, como geração de texto, código ou imagens.

## 🛠️ Ferramentas Disponíveis

### 1. `otimizar_prompt`

**Descrição:** Otimiza um prompt aplicando técnicas específicas de engenharia de prompts baseadas no tipo de tarefa.

**Entradas:**

- `prompt` (string): O texto do prompt a ser otimizado
- `tipo_tarefa` (string): Tipo de tarefa (text_generation, code_generation, image_generation)
- `modelo_alvo` (string, opcional): Modelo específico para o qual otimizar
- `nivel_detalhe` (string, opcional): Nível de detalhe desejado na saída

**Saídas:**

- `prompt_otimizado` (string): Versão otimizada do prompt
- `tecnicas_aplicadas` (list): Lista de técnicas aplicadas
- `explicacoes` (dict): Explicações para cada modificação
- `metricas` (dict): Métricas de melhoria estimadas

**Exemplo de Uso:**

```python
resultado = engenheiro.otimizar_prompt(
    prompt="Escreva um código em Python para ordenar uma lista",
    tipo_tarefa="code_generation",
    modelo_alvo="gpt-4"
)
```

### 2. `analisar_estrutura_prompt`

**Descrição:** Analisa a estrutura de um prompt e identifica seus componentes e características.

**Entradas:**

- `prompt` (string): O texto do prompt a ser analisado

**Saídas:**

- `componentes` (dict): Componentes identificados (contexto, instrução, exemplos, etc.)
- `complexidade` (float): Medida de complexidade do prompt (1-10)
- `clareza` (float): Medida de clareza do prompt (1-10)
- `ambiguidade` (list): Áreas potencialmente ambíguas
- `recomendacoes` (list): Recomendações estruturais

**Exemplo de Uso:**

```python
analise = engenheiro.analisar_estrutura_prompt(
    prompt="Você é um assistente especializado em biologia. Explique o processo de fotossíntese em termos simples."
)
```

### 3. `aplicar_estrategia_prompt`

**Descrição:** Aplica uma estratégia específica de engenharia de prompts ao prompt fornecido.

**Entradas:**

- `prompt` (string): O texto do prompt base
- `estrategia` (string): Estratégia a ser aplicada (chain_of_thought, few_shot, role_prompting, etc.)
- `parametros` (dict, opcional): Parâmetros específicos para a estratégia

**Saídas:**

- `prompt_resultante` (string): Prompt com a estratégia aplicada
- `estrutura` (dict): Estrutura do novo prompt
- `notas_uso` (string): Notas sobre o uso efetivo da estratégia

**Exemplo de Uso:**

```python
prompt_cot = engenheiro.aplicar_estrategia_prompt(
    prompt="Resolva o seguinte problema matemático: Se 3x + 2 = 11, qual é o valor de x?",
    estrategia="chain_of_thought",
)
```

### 4. `gerar_prompt_template`

**Descrição:** Gera um template de prompt para um cenário específico.

**Entradas:**

- `cenario` (string): Descrição do cenário ou caso de uso
- `tipo_tarefa` (string): Tipo de tarefa (text_generation, code_generation, image_generation)
- `nivel_complexidade` (string, opcional): Nível de complexidade desejado
- `incluir_exemplos` (boolean, opcional): Se deve incluir exemplos no template

**Saídas:**

- `template` (string): Template de prompt gerado
- `variaveis` (list): Variáveis a serem preenchidas no template
- `exemplos_uso` (list): Exemplos de uso do template
- `notas` (string): Notas explicativas sobre o template

**Exemplo de Uso:**

```python
template = engenheiro.gerar_prompt_template(
    cenario="Resumo de artigos científicos",
    tipo_tarefa="text_generation",
    incluir_exemplos=True
)
```

## 📊 Estratégias de Engenharia de Prompts

O servidor implementa diversas estratégias avançadas de engenharia de prompts:

| Estratégia                | Descrição                                 | Melhor para                        |
| ------------------------- | ----------------------------------------- | ---------------------------------- |
| **Chain-of-Thought**      | Induz raciocínio passo a passo            | Raciocínio lógico, matemática      |
| **Few-Shot Learning**     | Fornece exemplos para aprendizado         | Tarefas com padrões específicos    |
| **Role Prompting**        | Atribui um papel específico ao modelo     | Simulações, cenários específicos   |
| **Self-Consistency**      | Gera múltiplas soluções e as compara      | Problemas complexos                |
| **Tree of Thoughts**      | Explora diferentes caminhos de raciocínio | Problemas com múltiplas abordagens |
| **Reflexão**              | Avalia a qualidade da resposta            | Melhorar precisão iterativamente   |
| **Refinamento Iterativo** | Refina respostas em múltiplas etapas      | Conteúdo de alta qualidade         |
| **Context Distillation**  | Simplifica contexto complexo              | Melhorar eficiência                |

## 🎭 Tipos de Tarefas Suportadas

O servidor oferece otimizações específicas para diferentes tipos de tarefas:

### `TEXT_GENERATION`

Otimizações para geração de texto natural, incluindo:

- Conteúdo criativo (histórias, poemas)
- Conteúdo informativo (resumos, explicações)
- Conversação (diálogos, entrevistas)

### `CODE_GENERATION`

Otimizações para geração de código, incluindo:

- Implementação de algoritmos
- Desenvolvimento de funções/classes específicas
- Debugging e refatoração
- Documentação de código

### `IMAGE_GENERATION`

Otimizações para prompts de geração de imagens, incluindo:

- Descrições detalhadas de cenas
- Especificações de estilo e composição
- Elementos técnicos (iluminação, perspectiva)

## 🧪 Testes

Os testes para o Servidor de Engenharia de Prompts estão disponíveis em `/tests/test_prompt_server.py` e incluem casos para diversas estratégias e tipos de tarefas.

## 📝 Exemplos Completos

### Exemplo 1: Otimização de Prompt para Código

```python
# Prompt original
prompt_original = "Fazer função em Python para ordenar lista"

# Otimização
resultado = engenheiro.otimizar_prompt(
    prompt=prompt_original,
    tipo_tarefa="code_generation"
)

# Resultado
# prompt_otimizado = """
# Crie uma função em Python que ordene uma lista de números.
#
# Requisitos:
# 1. A função deve aceitar uma lista de números como entrada
# 2. Deve retornar a lista ordenada em ordem crescente
# 3. O código deve ser eficiente e seguir boas práticas
# 4. Inclua comentários explicando a lógica
# 5. Forneça um exemplo de uso da função
#
# Por favor, forneça a implementação completa da função.
# """
```

### Exemplo 2: Aplicação de Chain-of-Thought

```python
# Prompt base
prompt_base = "Em um jogo, há 25 jogadores. Se cada jogo envolve 5 jogadores e cada
jogador deve jogar exatamente uma vez, quantos jogos serão necessários?"

# Aplicar estratégia
resultado = engenheiro.aplicar_estrategia_prompt(
    prompt=prompt_base,
    estrategia="chain_of_thought"
)

# Resultado
# prompt_resultante = """
# Em um jogo, há 25 jogadores. Se cada jogo envolve 5 jogadores e cada jogador deve
# jogar exatamente uma vez, quantos jogos serão necessários?
#
# Vamos pensar passo a passo:
# 1. Temos 25 jogadores no total
# 2. Cada jogo envolve 5 jogadores
# 3. Cada jogador deve jogar exatamente uma vez
# 4. Para determinar o número de jogos, preciso calcular quantos grupos de 5 posso formar com 25 jogadores
# 5. Como cada jogador joga exatamente uma vez, o total de "slots de jogadores" será 25
# 6. Cada jogo usa 5 slots
# 7. Portanto, o número de jogos será 25 ÷ 5 = ?
# """
```

## 🔍 Uso Avançado

### Pipeline de Melhoria de Prompts

Você pode criar um pipeline completo para melhorar iterativamente prompts:

```python
from servers.prompt_server import PromptEngineer

engenheiro = PromptEngineer()

# Passo 1: Analisar estrutura inicial
analise = engenheiro.analisar_estrutura_prompt(prompt_inicial)

# Passo 2: Identificar estratégia adequada
estrategia = "few_shot" if analise.complexidade > 7 else "role_prompting"

# Passo 3: Aplicar estratégia
prompt_intermediario = engenheiro.aplicar_estrategia_prompt(
    prompt=prompt_inicial,
    estrategia=estrategia
)

# Passo 4: Otimização final
prompt_final = engenheiro.otimizar_prompt(
    prompt=prompt_intermediario.prompt_resultante,
    tipo_tarefa="text_generation"
)
```

## 📚 Recursos Adicionais

- [Documentação Completa da API](../api/prompt_server_api.md)
- [Guia de Estratégias de Prompts](../guides/prompt_strategies.md)
- [Exemplos de Uso Detalhados](../examples/prompt_engineering_examples.py)

---

**Desenvolvido para o projeto MCP Servers**
