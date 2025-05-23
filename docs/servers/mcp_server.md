# Analisador de Prompts MCP

## 📋 Visão Geral

O Analisador de Prompts MCP é um servidor especializado que analisa prompts utilizados para criar servidores MCP (Model Context Protocol), fornecendo pontuação, feedback detalhado e recomendações baseadas nas melhores práticas da documentação oficial do MCP.

![Analisador de Prompts](../assets/mcp_analyzer.png)

## 🎯 Propósito

Este servidor foi projetado para ajudar desenvolvedores a criar melhores servidores MCP, analisando a qualidade dos prompts utilizados para esse fim. O servidor avalia diversos aspectos críticos dos prompts e fornece orientações específicas para melhorá-los.

## 🛠️ Ferramentas Disponíveis

### 1. `analisar_prompt_mcp`

**Descrição:** Realiza uma análise completa de um prompt para criação de servidor MCP.

**Entradas:**

- `prompt` (string): O texto do prompt a ser analisado

**Saídas:**

- `pontuacao` (float): Nota geral de 1 a 10
- `pontos_fortes` (list): Lista de pontos fortes identificados
- `pontos_fracos` (list): Lista de pontos fracos identificados
- `sugestoes` (list): Sugestões específicas para melhorias
- `criterios_avaliados` (dict): Pontuação detalhada por critério
- `analise_detalhada` (string): Análise textual detalhada

**Exemplo de Uso:**

```python
resultado = analisador.analisar_prompt(
    "Crie um servidor MCP para processamento de arquivos PDF com ferramentas para extrair texto,
    metadados e imagens, com tratamento de erros para arquivos corrompidos."
)
```

### 2. `obter_melhores_praticas_mcp`

**Descrição:** Retorna informações detalhadas sobre melhores práticas para desenvolvimento de servidores MCP.

**Entradas:**

- `categoria` (string, opcional): Categoria específica de melhores práticas (design, erros, segurança, etc.)

**Saídas:**

- `praticas` (list): Lista de melhores práticas com descrições
- `exemplos` (dict): Exemplos de implementação para cada prática
- `referencias` (list): Links e referências para documentação oficial

**Exemplo de Uso:**

```python
praticas_design = analisador.obter_melhores_praticas_mcp(categoria="design_ferramentas")
```

### 3. `sugerir_melhorias_prompt`

**Descrição:** Fornece sugestões específicas para melhorar um prompt MCP com base em padrões identificados.

**Entradas:**

- `prompt` (string): O texto do prompt a ser melhorado
- `foco` (list, opcional): Aspectos específicos a priorizar nas sugestões

**Saídas:**

- `prompt_melhorado` (string): Versão aprimorada do prompt
- `alteracoes` (list): Lista de alterações realizadas
- `explicacoes` (dict): Explicações para cada alteração

**Exemplo de Uso:**

```python
melhorias = analisador.sugerir_melhorias_prompt(
    prompt="Crie um servidor MCP de manipulação de imagens",
    foco=["clareza", "tratamento_erros"]
)
```

### 4. `validar_requisitos_mcp`

**Descrição:** Valida um prompt contra uma lista de verificação de requisitos para servidores MCP.

**Entradas:**

- `prompt` (string): O texto do prompt a ser validado
- `nivel_rigor` (string, opcional): Nível de rigor da validação (básico, intermediário, avançado)

**Saídas:**

- `requisitos_atendidos` (list): Requisitos atendidos pelo prompt
- `requisitos_faltantes` (list): Requisitos não identificados no prompt
- `conformidade` (float): Percentual de conformidade com os requisitos

**Exemplo de Uso:**

```python
validacao = analisador.validar_requisitos_mcp(
    prompt="Crie um servidor MCP para gerenciamento de arquivos",
    nivel_rigor="intermediário"
)
```

## 📊 Sistema de Pontuação

O Analisador avalia prompts em 10 critérios principais, cada um com um peso específico na pontuação final:

| Critério              | Descrição                                                    | Peso |
| --------------------- | ------------------------------------------------------------ | ---- |
| Propósito Claro       | Objetivos específicos e bem definidos do servidor            | 15%  |
| Design de Ferramentas | Ferramentas focadas e documentadas com nomenclatura adequada | 15%  |
| Tratamento de Erros   | Tratamento abrangente de erros e validação                   | 12%  |
| Documentação          | Descrição clara das ferramentas e suas entradas/saídas       | 10%  |
| Segurança             | Considerações de segurança e melhores práticas               | 10%  |
| Esquema de Dados      | Definição clara de estruturas de dados e tipos               | 10%  |
| Eficiência            | Promove uso eficiente de recursos                            | 8%   |
| Extensibilidade       | Facilidade de extensão e manutenção                          | 8%   |
| Convenções MCP        | Segue as convenções e padrões do MCP                         | 7%   |
| Testes                | Menciona a necessidade de testes adequados                   | 5%   |

## 🔄 Algoritmo de Análise

O processo de análise segue estas etapas:

1. **Tokenização e Análise de Texto**: O prompt é dividido em tokens e analisado por padrões
2. **Detecção de Padrões**: Padrões positivos e negativos são identificados usando regex e análise semântica
3. **Pontuação por Critério**: Cada critério recebe uma pontuação baseada nos padrões detectados
4. **Cálculo da Pontuação Final**: Ponderação das pontuações individuais para gerar nota final
5. **Geração de Sugestões**: Criação de sugestões específicas com base nos pontos fracos detectados

## 📝 Exemplos Completos

### Exemplo 1: Prompt Básico

```python
# Prompt de entrada
prompt_basico = "Faça um servidor MCP simples"

# Análise
resultado = analisador.analisar_prompt(prompt_basico)

# Resultados
# Pontuação: 2.4/10
# Pontos fracos: Falta de propósito específico, sem menção a ferramentas,
# sem tratamento de erros, sem documentação
# Sugestões: Definir objetivo específico do servidor, especificar ferramentas,
# adicionar tratamento de erros
```

### Exemplo 2: Prompt Intermediário

```python
# Prompt de entrada
prompt_intermediario = "Crie um servidor MCP com ferramentas para operações de arquivo
incluindo tratamento de erros"

# Análise
resultado = analisador.analisar_prompt(prompt_intermediario)

# Resultados
# Pontuação: 5.8/10
# Pontos fortes: Menciona ferramentas, inclui tratamento de erros
# Pontos fracos: Propósito ainda genérico, falta detalhar documentação e esquemas
# Sugestões: Especificar tipos de operações de arquivo, detalhar estrutura das ferramentas
```

### Exemplo 3: Prompt Avançado

```python
# Prompt de entrada
prompt_avancado = "Desenvolva um servidor MCP especializado em processamento de documentos
com as seguintes ferramentas: extrair_texto, analisar_estrutura e converter_formato.
Cada ferramenta deve validar suas entradas, tratar erros específicos de formato e
documentar claramente suas saídas com esquemas bem definidos. Implemente tratamento
de segurança para evitar injeção de código e inclua logs detalhados."

# Análise
resultado = analisador.analisar_prompt(prompt_avancado)

# Resultados
# Pontuação: 9.2/10
# Pontos fortes: Propósito específico, ferramentas bem definidas, tratamento de erros,
# segurança, documentação
# Sugestões: Adicionar considerações sobre testes automatizados
```

## 🧪 Testes

Os testes para o Analisador de Prompts MCP estão disponíveis em `/tests/test_mcp_server.py` e incluem casos para diversos níveis de qualidade de prompts.

## 🔍 Uso Avançado

### Integração com Outros Servidores

O Analisador pode ser combinado com o Servidor de Engenharia de Prompts para um fluxo completo:

```python
from servers.mcp_server import AnalisadorPromptMCP
from servers.prompt_server import PromptEngineer

# Analisar prompt existente
analisador = AnalisadorPromptMCP()
resultado = analisador.analisar_prompt(prompt_original)

# Se pontuação abaixo do esperado, otimizar com o engenheiro de prompts
if resultado.pontuacao < 7.0:
    engenheiro = PromptEngineer()
    prompt_otimizado = engenheiro.otimizar_prompt(
        prompt=prompt_original,
        focus_areas=resultado.pontos_fracos
    )
```

## 📚 Recursos Adicionais

- [Documentação Completa da API](../api/mcp_server_api.md)
- [Guia de Melhores Práticas MCP](../guides/mcp_best_practices.md)
- [Exemplo de Uso Detalhado](../examples/mcp_analyzer_example.py)

---

**Desenvolvido para o projeto MCP Servers**
