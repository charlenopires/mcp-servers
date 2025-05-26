# FastMCP Server - Servidor de Otimização de Prompts MCP

## Visão Geral

O FastMCP Server é um servidor MCP especializado em análise e otimização de prompts para criação de servidores MCP. Utilizando o framework FastMCP, este servidor fornece ferramentas avançadas para melhorar a qualidade e eficácia de prompts usados no desenvolvimento de servidores MCP.

## Funcionalidades Principais

### 🔍 Análise de Prompts

- **Pontuação Automática**: Avalia prompts de 0-100 baseado em critérios específicos
- **Identificação de Pontos Fortes**: Destaca elementos bem implementados
- **Detecção de Fraquezas**: Identifica áreas que precisam de melhoria
- **Recomendações Personalizadas**: Sugere melhorias específicas

### 🛠️ Ferramentas Disponíveis

#### `analyze_mcp_prompt`

Analisa um prompt de criação de servidor MCP e fornece feedback detalhado.

**Parâmetros:**

- `prompt` (str): O prompt para análise

**Retorna:**

- `PromptAnalysis`: Objeto com score, pontos fortes, fracos e recomendações

**Critérios de Avaliação:**

- Clareza do propósito (definição clara do objetivo)
- Especificação de ferramentas (tools definidas)
- Definição de recursos (resources especificados)
- Inclusão de exemplos de uso
- Especificação de tipos de dados
- Considerações técnicas (async, tratamento de erros)
- Aspectos de segurança e produção

#### `suggest_mcp_prompt_improvements`

Sugere melhorias específicas para um prompt existente.

**Parâmetros:**

- `original_prompt` (str): Prompt original para melhorar
- `focus_area` (str, opcional): Área de foco ('clarity', 'technical', 'production')

**Retorna:**

- `Dict`: Prompt melhorado, explicação das mudanças e próximos passos

#### `validate_mcp_requirements`

Valida requisitos contra checklist de melhores práticas.

**Parâmetros:**

- `requirements` (str): Especificação de requisitos para validar

**Retorna:**

- `Dict`: Resultado da validação com score de completude e sugestões

#### `generate_mcp_server_template`

Gera templates otimizados para diferentes tipos de servidores.

**Parâmetros:**

- `server_type` (str): Tipo do servidor ('basic', 'api_integration', 'data_processing', 'production_ready')
- `name` (str): Nome do servidor
- `description` (str): Descrição do servidor

**Retorna:**

- `str`: Template completo com estrutura otimizada

### 📚 Recursos Disponíveis

#### `mcp://best-practices`

Retorna melhores práticas para desenvolvimento de servidores MCP organizadas por categoria:

- **Estrutura**: Práticas de organização e design
- **Técnicas**: Aspectos técnicos e implementação
- **Produção**: Considerações para ambiente de produção

#### `mcp://prompt-examples/{quality_level}`

Fornece exemplos de prompts com diferentes níveis de qualidade:

- **bad**: Exemplos de prompts problemáticos
- **good**: Prompts bem estruturados
- **excellent**: Prompts exemplares com todas as melhores práticas

#### `mcp://frameworks`

Frameworks de prompt engineering aplicáveis a servidores MCP:

- **CRISP**: Context, Requirements, Instructions, Specifications, Prompts
- **STAR**: Situation, Task, Action, Result
- **Chain-of-Thought**: Pensamento estruturado passo a passo

### 🎯 Prompts Especializados

#### `optimize_mcp_prompt`

Template para otimização de prompts MCP com contexto especializado.

#### `mcp_code_review`

Template para revisão de código de servidores MCP.

## Tipos de Servidor Suportados

### 1. Basic Server

Servidor simples com ferramentas e recursos básicos.

- Ferramentas essenciais
- Recursos de informação
- Estrutura de código básica

### 2. API Integration Server

Servidor que integra com APIs externas.

- Configuração de autenticação
- Rate limiting e retry logic
- Tratamento de erros de rede
- Cache inteligente

### 3. Data Processing Server

Servidor focado em processamento de dados.

- Processamento assíncrono
- Suporte a grandes volumes
- Progress reporting
- Validação de schema

### 4. Production Ready Server

Servidor com todas as práticas de produção.

- Estado distribuído (Redis)
- Segurança completa
- Observabilidade (logging, métricas, tracing)
- Escalabilidade e performance

## Critérios de Pontuação

O sistema de pontuação avalia prompts baseado nos seguintes critérios:

| Critério                 | Peso | Descrição                                         |
| ------------------------ | ---- | ------------------------------------------------- |
| **Elementos Essenciais** | 50%  | Propósito, ferramentas, recursos, exemplos, tipos |
| **Aspectos Técnicos**    | 30%  | Async, tratamento de erros, segurança, testes     |
| **Detalhamento**         | 20%  | Profundidade e completude da descrição            |

### Pontuação por Faixas:

- **90-100**: Excelente - Prompt completo com todas as melhores práticas
- **70-89**: Bom - Prompt bem estruturado com elementos essenciais
- **50-69**: Regular - Prompt funcional mas com melhorias necessárias
- **30-49**: Fraco - Prompt básico com muitas lacunas
- **0-29**: Muito fraco - Prompt incompleto ou muito vago

## Frameworks de Prompt Engineering

### CRISP Framework

Estrutura recomendada para prompts complexos:

```
[Context] Contexto e background do problema
[Requirements] Requisitos funcionais e não-funcionais
[Instructions] Instruções técnicas específicas
[Specifications] Especificações detalhadas de ferramentas/recursos
[Prompts/Examples] Exemplos concretos de uso
```

### STAR Framework

Para prompts orientados a resultados:

```
[Situation] Situação atual ou problema
[Task] Tarefa ou objetivo específico
[Action] Ações necessárias para implementar
[Result] Resultado esperado ou critérios de sucesso
```

### Chain-of-Thought

Para problemas complexos que requerem decomposição:

```
Passo 1: Análise do problema
Passo 2: Identificação de componentes
Passo 3: Definição de interfaces
Passo 4: Especificação de implementação
Passo 5: Considerações de qualidade
```

## Exemplos de Uso

### Análise Básica de Prompt

```python
from servers.fastmcp_server import analyze_mcp_prompt
from fastmcp import Context

# Criar contexto mock para exemplo
ctx = Context()

prompt = """
Criar um servidor MCP para análise de logs de sistema.
O servidor deve processar arquivos de log e extrair métricas.
"""

result = await analyze_mcp_prompt(prompt, ctx)
print(f"Score: {result.score}/100")
print(f"Pontos fortes: {result.strengths}")
print(f"Recomendações: {result.recommendations}")
```

### Geração de Template

```python
template = await generate_mcp_server_template(
    server_type="data_processing",
    name="LogAnalyzer",
    description="Análise e processamento de logs de sistema",
    ctx=ctx
)
print(template)
```

### Validação de Requisitos

```python
requirements = """
Propósito: Análise de logs de sistema
Ferramentas: parse_log, extract_metrics, generate_report
Recursos: logs://processed, metrics://current
Tipos de entrada: Arquivos de log (.log, .txt)
Tipos de saída: JSON com métricas extraídas
Tratamento de erros: Validação de formato e conteúdo
Operações assíncronas: Processamento de arquivos grandes
"""

validation = await validate_mcp_requirements(requirements, ctx)
print(f"Válido: {validation['is_valid']}")
print(f"Score de completude: {validation['completeness_score']}")
```

## Melhores Práticas para Prompts MCP

### ✅ Estrutura Recomendada

1. **Objetivo Claro**: Defina claramente o propósito do servidor
2. **Ferramentas Específicas**: Liste todas as ferramentas necessárias
3. **Recursos Definidos**: Especifique recursos a serem expostos
4. **Tipos de Dados**: Defina formatos de entrada e saída
5. **Exemplos Concretos**: Inclua casos de uso reais

### ✅ Aspectos Técnicos

1. **Operações Assíncronas**: Identifique operações que devem ser async
2. **Tratamento de Erros**: Especifique como lidar com falhas
3. **Validação de Dados**: Use modelos Pydantic para validação
4. **Segurança**: Considere autenticação e autorização
5. **Performance**: Mencione otimizações necessárias

### ✅ Considerações de Produção

1. **Escalabilidade**: Considere estado distribuído se necessário
2. **Observabilidade**: Inclua logging e métricas
3. **Health Checks**: Defina endpoints de saúde
4. **Deployment**: Considere containerização
5. **Testes**: Especifique estratégia de testes

## Integração com Main Launcher

O FastMCP Server está integrado ao launcher principal do projeto:

```bash
# Executar o servidor FastMCP
python main.py fastmcp

# Executar em modo desenvolvimento
python main.py fastmcp --dev

# Executar em porta específica
python main.py fastmcp --port 3002
```

## Desenvolvimento e Testes

### Executar Testes

```bash
# Todos os testes do FastMCP Server
python run_tests.py fastmcp_server

# Usando pytest diretamente
pytest tests/test_fastmcp_server.py -v

# Testes específicos
pytest tests/test_fastmcp_server.py::TestPromptAnalysis -v
```

### Estrutura de Testes

- **TestPromptAnalysis**: Testes dos modelos Pydantic
- **TestMCPRequirements**: Testes de requisitos
- **TestFastMCPAnalysisFunctions**: Testes das ferramentas principais
- **TestFastMCPResources**: Testes dos recursos
- **TestFastMCPIntegration**: Testes de integração

## Dependências

- **fastmcp**: Framework principal (>=2.0.0)
- **pydantic**: Validação de dados (>=2.0.0)
- **typing-extensions**: Anotações de tipo
- **asyncio**: Operações assíncronas

## Roadmap

### v2.1 (Próxima Versão)

- [ ] Análise de código MCP existente
- [ ] Sugestões de refatoração
- [ ] Templates para testes automatizados
- [ ] Integração com CI/CD

### v2.2 (Futuro)

- [ ] Interface web para análise de prompts
- [ ] API REST para integração externa
- [ ] Banco de dados de templates
- [ ] Análise de performance de prompts

### v2.3 (Longo Prazo)

- [ ] Machine learning para scoring
- [ ] Análise semântica avançada
- [ ] Recomendações contextuais
- [ ] Integração com IDEs

## Contribuição

Para contribuir com o FastMCP Server:

1. **Adicionar Novos Templates**: Implemente templates para tipos específicos de servidor
2. **Melhorar Análise**: Adicione novos critérios de avaliação
3. **Expandir Frameworks**: Adicione novos frameworks de prompt engineering
4. **Otimizar Performance**: Melhore a velocidade de análise
5. **Documentar Exemplos**: Adicione mais exemplos de uso

## Suporte

- **Documentação**: [docs/servers/fastmcp_server.md](./fastmcp_server.md)
- **Exemplos**: [docs/examples/](../examples/)
- **Testes**: [tests/test_fastmcp_server.py](../../tests/test_fastmcp_server.py)
- **Issues**: Reporte problemas via GitHub Issues

---

**FastMCP Server v1.0** - Parte do projeto MCP Servers v2.0
_Especializado em otimização de prompts para desenvolvimento MCP_
