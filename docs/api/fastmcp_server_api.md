# API do FastMCP Server - Referência Técnica

## Visão Geral da API

O FastMCP Server expõe uma API baseada no protocolo MCP (Model Context Protocol) com ferramentas especializadas para análise e otimização de prompts para criação de servidores MCP.

## Modelos de Dados

### PromptAnalysis

Modelo que representa o resultado da análise de um prompt MCP.

```python
class PromptAnalysis(BaseModel):
    score: float                    # Pontuação 0-100
    strengths: List[str]           # Pontos fortes identificados
    weaknesses: List[str]          # Pontos fracos encontrados
    recommendations: List[str]     # Recomendações específicas
    missing_elements: List[str]    # Elementos ausentes importantes
```

**Validações:**

- `score`: Deve estar entre 0 e 100 (validado automaticamente)

### MCPRequirements

Modelo que representa os requisitos extraídos de um prompt MCP.

```python
class MCPRequirements(BaseModel):
    tools: List[str] = []              # Ferramentas a implementar
    resources: List[str] = []          # Recursos a expor
    async_operations: bool = False     # Necessita operações assíncronas
    external_apis: List[str] = []      # APIs externas mencionadas
    authentication: bool = False      # Requer autenticação
    error_handling: bool = False       # Menciona tratamento de erros
```

## Ferramentas (Tools)

### analyze_mcp_prompt

Analisa um prompt de criação de servidor MCP e fornece feedback detalhado.

**Parâmetros:**

```python
prompt: str  # O prompt para análise (required)
ctx: Context # Contexto do FastMCP (required)
```

**Retorno:**

```python
PromptAnalysis  # Resultado da análise
```

**Exemplo de Uso:**

```python
result = await analyze_mcp_prompt(
    prompt="Criar um servidor MCP para análise de dados",
    ctx=context
)
```

**Critérios de Análise:**

| Categoria        | Elementos Verificados                             | Peso |
| ---------------- | ------------------------------------------------- | ---- |
| **Essenciais**   | Propósito, ferramentas, recursos, exemplos, tipos | 50%  |
| **Técnicos**     | Async, tratamento de erros, segurança, testes     | 30%  |
| **Detalhamento** | Profundidade e completude da descrição            | 20%  |

**Algoritmo de Pontuação:**

1. **Elementos Essenciais (50%)**: Verifica presença de propósito, ferramentas, recursos, exemplos e tipos
2. **Aspectos Técnicos (30%)**: Analisa considerações de async, erros, segurança e testes
3. **Detalhamento (20%)**: Baseado no comprimento e profundidade do prompt

### suggest_mcp_prompt_improvements

Sugere melhorias específicas para um prompt de criação de servidor MCP.

**Parâmetros:**

```python
original_prompt: str           # Prompt original (required)
focus_area: Optional[str]      # Área de foco (optional)
ctx: Optional[Context]         # Contexto (optional)
```

**Valores para focus_area:**

- `"clarity"`: Foco em clareza e estrutura
- `"technical"`: Foco em aspectos técnicos
- `"production"`: Foco em requisitos de produção
- `None`: Melhoria geral

**Retorno:**

```python
Dict[str, Any] = {
    "improved_prompt": str,        # Prompt melhorado
    "changes_explanation": List[str], # Explicação das mudanças
    "improvement_score": float,    # Score estimado após melhorias
    "next_steps": List[str]        # Próximos passos sugeridos
}
```

**Exemplo de Uso:**

```python
result = await suggest_mcp_prompt_improvements(
    original_prompt="Criar servidor MCP",
    focus_area="technical",
    ctx=context
)
```

### validate_mcp_requirements

Valida requisitos de servidor MCP contra checklist de melhores práticas.

**Parâmetros:**

```python
requirements: str  # Especificação de requisitos (required)
ctx: Context      # Contexto do FastMCP (required)
```

**Retorno:**

```python
Dict[str, Any] = {
    "is_valid": bool,                    # Se os requisitos são válidos
    "completeness_score": float,         # Score de completude (0-100)
    "issues": List[str],                 # Problemas identificados
    "missing_requirements": List[str],   # Requisitos ausentes
    "suggestions": List[str]             # Sugestões de melhoria
}
```

**Checklist de Validação:**

- ✅ Propósito definido
- ✅ Ferramentas especificadas
- ✅ Tipos de dados definidos
- ✅ Tratamento de erros mencionado
- ✅ Exemplos incluídos
- ✅ Operações assíncronas consideradas

**Exemplo de Uso:**

```python
result = await validate_mcp_requirements(
    requirements="Propósito: análise de dados...",
    ctx=context
)
```

### generate_mcp_server_template

Gera um template de prompt otimizado para criar um servidor MCP específico.

**Parâmetros:**

```python
server_type: str  # Tipo de servidor (required)
name: str         # Nome do servidor (required)
description: str  # Descrição do servidor (required)
ctx: Context     # Contexto do FastMCP (required)
```

**Tipos de Servidor Suportados:**

- `"basic"`: Servidor simples com ferramentas básicas
- `"api_integration"`: Servidor que integra com APIs externas
- `"data_processing"`: Servidor focado em processamento de dados
- `"production_ready"`: Servidor com todas as práticas de produção

**Retorno:**

```python
str  # Template completo formatado
```

**Estrutura do Template:**

1. **Contexto e Objetivo**: Propósito claro do servidor
2. **Requisitos Funcionais**: Ferramentas e recursos necessários
3. **Requisitos Técnicos**: Aspectos de implementação
4. **Exemplos de Uso**: Casos de uso concretos
5. **Melhores Práticas**: Diretrizes a seguir

**Exemplo de Uso:**

```python
template = await generate_mcp_server_template(
    server_type="data_processing",
    name="DataAnalyzer",
    description="Análise de dados de vendas",
    ctx=context
)
```

## Recursos (Resources)

### mcp://best-practices

Retorna melhores práticas para desenvolvimento de servidores MCP.

**URI:** `mcp://best-practices`

**Retorno:**

```python
Dict[str, List[str]] = {
    "structure": [
        "Definir claramente o propósito do servidor MCP",
        "Especificar ferramentas, recursos e prompts necessários",
        "Incluir exemplos de uso concretos",
        "Detalhar tipos de entrada e saída esperados"
    ],
    "technical": [
        "Usar type hints e docstrings detalhadas",
        "Implementar operações assíncronas para I/O",
        "Incluir tratamento de erros robusto",
        "Seguir padrões de segurança (validação, autenticação)"
    ],
    "production": [
        "Configurar logging estruturado",
        "Implementar health checks",
        "Considerar escalabilidade (Redis para estado)",
        "Incluir observabilidade (métricas, traces)"
    ]
}
```

### mcp://prompt-examples/{quality_level}

Fornece exemplos de prompts de diferentes níveis de qualidade.

**URI:** `mcp://prompt-examples/{quality_level}`

**Parâmetros de Rota:**

- `quality_level`: `"bad"`, `"good"`, ou `"excellent"`

**Retorno para "bad":**

```python
Dict[str, Any] = {
    "prompt": str,          # Exemplo de prompt ruim
    "issues": List[str]     # Problemas identificados
}
```

**Retorno para "good" e "excellent":**

```python
Dict[str, Any] = {
    "prompt": str,           # Exemplo de prompt
    "strengths": List[str]   # Pontos fortes
}
```

**Exemplo de Resposta "excellent":**

````python
{
    "prompt": """Criar um servidor MCP com FastMCP em Python para análise de dados de vendas.

## Requisitos Funcionais
- Ferramenta 'analyze_sales': aceita CSV com colunas (date, product, quantity, price)
- Retorna estatísticas: total de vendas, produto mais vendido, tendências mensais
- Recurso 'reports://latest': expõe último relatório gerado em JSON

## Requisitos Técnicos
- Processamento assíncrono para arquivos grandes (>100MB)
- Validação de schema com Pydantic
- Cache de resultados por 1 hora
- Logging estruturado de todas as operações

## Exemplo de Uso
```python
result = await client.call_tool("analyze_sales", {
    "file_path": "sales_2024.csv",
    "group_by": "month"
})
```""",
    "strengths": [
        "Especificação completa e detalhada",
        "Define claramente ferramentas e recursos",
        "Inclui requisitos técnicos importantes",
        "Fornece exemplo de uso concreto",
        "Considera performance e cache"
    ]
}
````

### mcp://frameworks

Retorna frameworks de prompt engineering aplicáveis a criação de servidores MCP.

**URI:** `mcp://frameworks`

**Retorno:**

```python
Dict[str, Any] = {
    "frameworks": {
        "CRISP": {
            "name": str,          # Nome completo do framework
            "description": str,   # Descrição do framework
            "application": str,   # Quando usar
            "template": str       # Template de exemplo
        },
        "STAR": { ... },
        "Chain-of-Thought": { ... }
    },
    "recommendation": str  # Recomendação geral
}
```

**Frameworks Disponíveis:**

1. **CRISP** (Context, Requirements, Instructions, Specifications, Prompts)
2. **STAR** (Situation, Task, Action, Result)
3. **Chain-of-Thought** (Pensamento estruturado passo a passo)

## Prompts Especializados

### optimize_mcp_prompt

Template para otimização de prompts MCP com contexto especializado.

**Parâmetros:**

```python
user_context: str    # Contexto do usuário
requirements: str    # Requisitos atuais
```

**Retorno:**

```python
List[Dict[str, str]]  # Lista de mensagens formatadas para LLM
```

**Estrutura do Retorno:**

```python
[
    {
        "role": "system",
        "content": "Prompt do sistema especializado em MCP"
    },
    {
        "role": "user",
        "content": f"Contexto: {user_context}\nRequisitos: {requirements}..."
    }
]
```

### mcp_code_review

Template para revisão de código de servidores MCP.

**Parâmetros:**

```python
code: str  # Código do servidor MCP para revisar
```

**Retorno:**

```python
List[Dict[str, str]]  # Mensagens formatadas para revisão
```

## Códigos de Status e Erros

### Erros Comuns

**ValidationError (Pydantic)**

```python
# Quando score está fora do range 0-100
{
    "error": "ValidationError",
    "message": "Score deve estar entre 0 e 100",
    "field": "score"
}
```

**InvalidServerType**

```python
# Quando server_type não é reconhecido
{
    "error": "InvalidServerType",
    "message": "Tipo 'invalid' não encontrado. Use: basic, api_integration, data_processing, ou production_ready",
    "valid_types": ["basic", "api_integration", "data_processing", "production_ready"]
}
```

**ResourceNotFound**

```python
# Quando quality_level é inválido
{
    "error": "Nível 'invalid' não encontrado. Use: bad, good, ou excellent"
}
```

## Limites e Restrições

### Limites de Input

- **prompt**: Máximo recomendado de 10.000 caracteres
- **requirements**: Máximo recomendado de 5.000 caracteres
- **code** (para revisão): Máximo recomendado de 20.000 caracteres

### Performance

- **analyze_mcp_prompt**: ~100-500ms dependendo do tamanho
- **suggest_improvements**: ~200-800ms para geração completa
- **validate_requirements**: ~50-200ms para checklist
- **generate_template**: ~100-300ms por template

### Rate Limiting

- Recomendado: Máximo 10 requisições por minuto por cliente
- Operações pesadas: Máximo 5 por minuto

## Exemplos de Integração

### Cliente Python Simples

```python
import asyncio
from fastmcp import FastMCP, Context

async def analyze_my_prompt():
    # Configurar cliente
    client = FastMCP.client("fastmcp-prompt-assistant")

    # Analisar prompt
    result = await client.call_tool("analyze_mcp_prompt", {
        "prompt": "Criar servidor MCP para análise de logs"
    })

    print(f"Score: {result['score']}")
    return result

# Executar
result = asyncio.run(analyze_my_prompt())
```

### Workflow Completo de Otimização

```python
async def optimize_prompt_workflow(initial_prompt: str):
    client = FastMCP.client("fastmcp-prompt-assistant")

    # 1. Análise inicial
    analysis = await client.call_tool("analyze_mcp_prompt", {
        "prompt": initial_prompt
    })

    print(f"Score inicial: {analysis['score']}")

    # 2. Sugerir melhorias
    improvements = await client.call_tool("suggest_mcp_prompt_improvements", {
        "original_prompt": initial_prompt,
        "focus_area": "technical"
    })

    improved_prompt = improvements["improved_prompt"]

    # 3. Validar melhorias
    validation = await client.call_tool("validate_mcp_requirements", {
        "requirements": improved_prompt
    })

    print(f"Score após melhorias: {validation['completeness_score']}")
    return improved_prompt
```

### Geração de Template e Customização

```python
async def create_custom_server_template():
    client = FastMCP.client("fastmcp-prompt-assistant")

    # Gerar template base
    template = await client.call_tool("generate_mcp_server_template", {
        "server_type": "data_processing",
        "name": "LogAnalyzer",
        "description": "Análise de logs de sistema"
    })

    # Customizar template com requisitos específicos
    custom_requirements = template + "\n\n## Requisitos Específicos\n..."

    # Validar template final
    validation = await client.call_tool("validate_mcp_requirements", {
        "requirements": custom_requirements
    })

    return template, validation
```

## Changelog da API

### v1.0.0 (Atual)

- ✅ Ferramentas principais implementadas
- ✅ Recursos de melhores práticas
- ✅ Templates para tipos básicos de servidor
- ✅ Frameworks de prompt engineering

### v1.1.0 (Planejado)

- 🔄 Análise de código MCP existente
- 🔄 Sugestões de refatoração
- 🔄 Templates para testes automatizados

### v1.2.0 (Futuro)

- 📋 API REST complementar
- 📋 Análise de performance
- 📋 Recomendações baseadas em ML

---

**FastMCP Server API v1.0** - Parte do projeto MCP Servers v2.0
_Documentação técnica completa para integração_
