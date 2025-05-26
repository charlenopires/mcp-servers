"""
FastMCP Prompt Assistant - Servidor MCP para otimização de prompts de criação de servidores MCP

Este servidor implementa as melhores práticas para desenvolvimento com FastMCP,
fornecendo ferramentas para análise e melhoria de prompts relacionados à criação
de servidores MCP.
"""

import asyncio
import json
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime
from pathlib import Path

from fastmcp import FastMCP, Context
from pydantic import BaseModel, Field, field_validator
from typing_extensions import Annotated

# Configuração de logging estruturado
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Inicialização do servidor FastMCP
mcp = FastMCP(
    name="FastMCP-Prompt-Assistant",
    description="Servidor MCP especializado em otimizar prompts para criação de servidores MCP com FastMCP",
    instructions="""
    Este servidor ajuda a criar prompts eficazes para desenvolvimento de servidores MCP.
    
    Capacidades principais:
    - Análise de prompts para criação de servidores MCP
    - Sugestão de melhorias baseadas em melhores práticas
    - Validação de requisitos MCP
    - Fornecimento de templates e exemplos
    - Aplicação de técnicas avançadas de prompt engineering
    """,
    dependencies=["fastmcp>=2.0.0", "pydantic>=2.0.0"]
)

# Modelos Pydantic para estruturação de dados


class PromptAnalysis(BaseModel):
    """Resultado da análise de um prompt MCP"""
    score: float = Field(..., description="Pontuação geral do prompt (0-100)")
    strengths: List[str] = Field(...,
                                 description="Pontos fortes identificados")
    weaknesses: List[str] = Field(..., description="Pontos fracos a melhorar")
    recommendations: List[str] = Field(...,
                                       description="Recomendações específicas")
    missing_elements: List[str] = Field(
        default_factory=list, description="Elementos importantes ausentes")

    @field_validator('score')
    @classmethod
    def validate_score(cls, v):
        """Valida que o score está entre 0 e 100"""
        if not 0 <= v <= 100:
            raise ValueError('Score deve estar entre 0 e 100')
        return v


class MCPRequirements(BaseModel):
    """Requisitos extraídos de um prompt MCP"""
    tools: List[str] = Field(default_factory=list,
                             description="Ferramentas a implementar")
    resources: List[str] = Field(
        default_factory=list, description="Recursos a expor")
    async_operations: bool = Field(
        default=False, description="Necessita operações assíncronas")
    external_apis: List[str] = Field(
        default_factory=list, description="APIs externas mencionadas")
    authentication: bool = Field(
        default=False, description="Requer autenticação")
    error_handling: bool = Field(
        default=False, description="Menciona tratamento de erros")


# Constantes com melhores práticas
BEST_PRACTICES = {
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

# Ferramentas do servidor


@mcp.tool()
async def analyze_mcp_prompt(
    prompt: Annotated[str, Field(description="O prompt para criação de servidor MCP a ser analisado")],
    ctx: Context
) -> PromptAnalysis:
    """
    Analisa um prompt de criação de servidor MCP e fornece feedback detalhado.

    Esta ferramenta avalia a qualidade do prompt considerando:
    - Clareza e completude dos requisitos
    - Aderência às melhores práticas do FastMCP  
    - Presença de elementos essenciais
    - Aspectos técnicos e de produção
    """
    await ctx.info(f"Analisando prompt de {len(prompt)} caracteres...")

    # Análise básica do prompt
    analysis = PromptAnalysis(
        score=0.0,
        strengths=[],
        weaknesses=[],
        recommendations=[]
    )

    # Verificar elementos essenciais
    elements_check = {
        "propósito": any(word in prompt.lower() for word in ["objetivo", "propósito", "finalidade", "para"]),
        "ferramentas": any(word in prompt.lower() for word in ["ferramenta", "tool", "função", "funcionalidade"]),
        "recursos": any(word in prompt.lower() for word in ["recurso", "resource", "dado", "informação"]),
        "exemplos": any(word in prompt.lower() for word in ["exemplo", "exemplo de uso", "como usar"]),
        "tipos": any(word in prompt.lower() for word in ["tipo", "type", "entrada", "saída", "parâmetro"])
    }

    # Calcular pontuação baseada em elementos presentes
    present_elements = sum(elements_check.values())
    analysis.score = (present_elements / len(elements_check)
                      ) * 60  # 60% do score base

    # Verificar aspectos técnicos
    technical_aspects = {
        "async": "async" in prompt.lower() or "assíncrono" in prompt.lower(),
        "error_handling": any(word in prompt.lower() for word in ["erro", "exceção", "tratamento"]),
        "security": any(word in prompt.lower() for word in ["segurança", "autenticação", "validação"]),
        "testing": any(word in prompt.lower() for word in ["teste", "test", "validar"])
    }

    technical_score = sum(technical_aspects.values()) / \
        len(technical_aspects) * 25  # 25% do score
    analysis.score += technical_score

    # Verificar detalhamento
    # 15% do score baseado em detalhamento (mais generoso)
    detail_score = min(15.0, len(prompt) / 30.0)
    analysis.score += detail_score

    # Identificar pontos fortes
    if elements_check["propósito"]:
        analysis.strengths.append("Define claramente o propósito do servidor")
    if elements_check["exemplos"]:
        analysis.strengths.append("Inclui exemplos de uso")
    if technical_aspects["async"]:
        analysis.strengths.append("Considera operações assíncronas")
    if len(prompt) > 200:
        analysis.strengths.append("Prompt detalhado e descritivo")

    # Identificar pontos fracos e recomendações
    if not elements_check["ferramentas"]:
        analysis.weaknesses.append("Não especifica ferramentas claramente")
        analysis.recommendations.append(
            "Adicione uma lista clara de ferramentas que o servidor deve implementar")

    if not elements_check["tipos"]:
        analysis.weaknesses.append(
            "Falta especificação de tipos de entrada/saída")
        analysis.recommendations.append(
            "Defina os tipos de dados esperados para cada ferramenta")

    if not technical_aspects["error_handling"]:
        analysis.weaknesses.append("Não menciona tratamento de erros")
        analysis.recommendations.append(
            "Inclua requisitos de tratamento de erros e casos de falha")

    # Elementos ausentes importantes
    for element, present in elements_check.items():
        if not present:
            analysis.missing_elements.append(f"Especificação de {element}")

    await ctx.info(f"Análise concluída. Pontuação: {analysis.score:.1f}/100")
    return analysis


@mcp.tool()
async def suggest_mcp_prompt_improvements(
    original_prompt: Annotated[str, Field(description="O prompt original a ser melhorado")],
    focus_area: Annotated[Optional[str], Field(
        description="Área de foco: 'clarity', 'technical', 'production', ou None para geral")] = None,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Sugere melhorias específicas para um prompt de criação de servidor MCP.

    Retorna um prompt melhorado e explica as mudanças aplicadas.
    """
    if ctx:
        await ctx.info(f"Gerando sugestões de melhoria para prompt...")

    # Analisar o prompt original primeiro
    analysis = await analyze_mcp_prompt(original_prompt, ctx) if ctx else PromptAnalysis(
        score=50.0, strengths=[], weaknesses=["Análise simplificada"], recommendations=[]
    )

    # Base do prompt melhorado
    improved_sections = []

    # Seção de contexto e propósito
    if "criar" in original_prompt.lower() and "servidor" in original_prompt.lower():
        purpose_section = """## Contexto e Objetivo
Preciso criar um servidor MCP com FastMCP em Python que [DESCREVER PROPÓSITO ESPECÍFICO].

### Caso de Uso
[DESCREVER QUANDO E COMO O SERVIDOR SERÁ USADO]"""
        improved_sections.append(purpose_section)

    # Seção de requisitos funcionais
    functional_section = """## Requisitos Funcionais

### Ferramentas (@mcp.tool())
1. **[NOME_FERRAMENTA_1]**
   - Descrição: [O QUE FAZ]
   - Parâmetros: [TIPO E DESCRIÇÃO]
   - Retorno: [TIPO E FORMATO]
   - Exemplo: [EXEMPLO DE USO]

### Recursos (@mcp.resource())
1. **[URI_RECURSO_1]**
   - Descrição: [DADOS EXPOSTOS]
   - Formato: [JSON/TEXT/OUTROS]"""
    improved_sections.append(functional_section)

    # Seção técnica se o foco for técnico
    if focus_area == "technical" or focus_area is None:
        technical_section = """## Requisitos Técnicos

- **Operações Assíncronas**: [LISTAR OPERAÇÕES QUE PRECISAM SER ASYNC]
- **Integrações Externas**: [APIs, BANCOS DE DADOS, SERVIÇOS]
- **Tratamento de Erros**: [COMO LIDAR COM FALHAS]
- **Validação de Dados**: [USAR PYDANTIC MODELS]"""
        improved_sections.append(technical_section)

    # Seção de produção se relevante
    if focus_area == "production":
        production_section = """## Requisitos de Produção

- **Segurança**: [AUTENTICAÇÃO, AUTORIZAÇÃO, VALIDAÇÃO]
- **Escalabilidade**: [CONSIDERAÇÕES DE ESTADO, REDIS]
- **Observabilidade**: [LOGGING, MÉTRICAS, TRACES]
- **Health Checks**: [ENDPOINTS DE SAÚDE]"""
        improved_sections.append(production_section)

    # Adicionar exemplos
    example_section = """## Exemplos de Uso

```python
# Exemplo de chamada da ferramenta principal
resultado = await client.call_tool("nome_ferramenta", {
    "param1": "valor",
    "param2": 123
})
```"""
    improved_sections.append(example_section)

    improved_prompt = "\n\n".join(improved_sections)

    # Explicar mudanças
    changes_explanation = [
        "Estruturado o prompt em seções claras e bem definidas",
        "Adicionados templates para especificar ferramentas e recursos",
        "Incluídos campos para exemplos de uso concretos",
        "Adicionada seção de requisitos técnicos quando relevante",
        f"Foco aplicado: {focus_area or 'geral'}"
    ]

    return {
        "improved_prompt": improved_prompt,
        "changes_explanation": changes_explanation,
        "improvement_score": min(100.0, analysis.score + 30.0),
        "next_steps": [
            "Preencher os campos template com informações específicas",
            "Adicionar mais detalhes sobre o contexto de uso",
            "Revisar e validar os requisitos técnicos"
        ]
    }


@mcp.tool()
async def validate_mcp_requirements(
    requirements: Annotated[str, Field(description="Especificação de requisitos para validar")],
    ctx: Context
) -> Dict[str, Any]:
    """
    Valida requisitos de servidor MCP contra checklist de melhores práticas.

    Verifica completude e adequação dos requisitos especificados.
    """
    await ctx.info("Validando requisitos contra melhores práticas...")

    validation_results: Dict[str, Any] = {
        "is_valid": True,
        "completeness_score": 0.0,
        "issues": [],
        "missing_requirements": [],
        "suggestions": []
    }

    # Checklist de requisitos essenciais
    essential_checklist = {
        "purpose_defined": "propósito" in requirements.lower() or "objetivo" in requirements.lower(),
        "tools_specified": "ferramenta" in requirements.lower() or "tool" in requirements.lower(),
        "data_types_defined": "tipo" in requirements.lower() or "type" in requirements.lower(),
        "error_handling": "erro" in requirements.lower() or "exceção" in requirements.lower(),
        "examples_included": "exemplo" in requirements.lower(),
        "async_considered": "async" in requirements.lower() or "assíncrono" in requirements.lower()
    }

    # Calcular completude
    checked_items = sum(essential_checklist.values())
    validation_results["completeness_score"] = (
        checked_items / len(essential_checklist)) * 100

    # Identificar problemas
    for requirement, is_present in essential_checklist.items():
        if not is_present:
            validation_results["missing_requirements"].append(requirement)
            validation_results["issues"].append(
                f"Requisito ausente: {requirement}")

    # Validar se há requisitos suficientes
    if validation_results["completeness_score"] < 60:
        validation_results["is_valid"] = False
        validation_results["suggestions"].append(
            "Adicione mais detalhes aos requisitos. Use o template sugerido pela ferramenta de melhorias."
        )

    # Verificar requisitos de produção se mencionados
    if "produção" in requirements.lower() or "production" in requirements.lower():
        production_checks = {
            "security": any(word in requirements.lower() for word in ["segurança", "autenticação"]),
            "scalability": any(word in requirements.lower() for word in ["escala", "redis", "estado"]),
            "monitoring": any(word in requirements.lower() for word in ["log", "métrica", "observabilidade"])
        }

        for check, is_present in production_checks.items():
            if not is_present:
                validation_results["suggestions"].append(
                    f"Para produção, considere adicionar requisitos de {check}"
                )

    await ctx.info(f"Validação concluída. Score: {validation_results['completeness_score']:.0f}%")
    return validation_results


@mcp.tool()
async def generate_mcp_server_template(
    server_type: Annotated[str, Field(description="Tipo de servidor: 'basic', 'api_integration', 'data_processing', 'production_ready'")],
    name: Annotated[str, Field(description="Nome do servidor MCP")],
    description: Annotated[str, Field(description="Descrição do que o servidor faz")],
    ctx: Context
) -> str:
    """
    Gera um template de prompt otimizado para criar um servidor MCP específico.

    Templates disponíveis:
    - basic: Servidor simples com ferramentas e recursos básicos
    - api_integration: Servidor que integra com APIs externas
    - data_processing: Servidor focado em processamento de dados
    - production_ready: Servidor com todas as práticas de produção
    """
    await ctx.info(f"Gerando template de prompt para servidor tipo '{server_type}'...")

    # Template base comum
    base_template = f"""# Criação de Servidor MCP: {name}

## Objetivo
Criar um servidor MCP com FastMCP em Python para {description}.

## Especificações Técnicas
- **Framework**: FastMCP 2.0+
- **Python**: 3.8+
- **Estilo**: Pythônico, com type hints e docstrings detalhadas
"""

    # Templates específicos por tipo
    if server_type == "basic":
        specific_template = """
## Requisitos Funcionais

### Ferramentas
1. **ferramenta_principal**
   - Função: [DESCREVER FUNÇÃO PRINCIPAL]
   - Parâmetros:
     - param1 (str): [DESCRIÇÃO]
     - param2 (int): [DESCRIÇÃO]
   - Retorno: Dict com resultado processado
   - Tratamento de erros: Validar entrada e retornar mensagens claras

### Recursos
1. **info://status**
   - Retorna status atual do servidor
   - Formato: JSON
   
2. **config://settings**
   - Expõe configurações atuais
   - Formato: JSON

### Estrutura de Código
```python
from fastmcp import FastMCP, Context
from pydantic import BaseModel, Field
from typing import Dict, Any

mcp = FastMCP(name="{name}")

@mcp.tool()
async def ferramenta_principal(param1: str, param2: int, ctx: Context) -> Dict[str, Any]:
    '''Docstring detalhada'''
    # Implementação
    pass
```
"""

    elif server_type == "api_integration":
        specific_template = """
## Requisitos de Integração

### APIs Externas
- **API Principal**: [NOME E DOCUMENTAÇÃO]
- **Autenticação**: [MÉTODO - Bearer Token, API Key, etc]
- **Rate Limiting**: [LIMITES E ESTRATÉGIA]

### Ferramentas de Integração
1. **fetch_data**
   - Busca dados da API externa
   - Implementar retry logic e circuit breaker
   - Cache de respostas quando apropriado

2. **process_and_send**
   - Processa dados e envia para API
   - Validação robusta com Pydantic
   - Tratamento de erros de rede

### Requisitos Técnicos
- Usar httpx para chamadas assíncronas
- Implementar timeout e retry configuráveis
- Logging detalhado de todas as interações
- Gerenciamento seguro de credenciais (variáveis de ambiente)

### Exemplo de Implementação
```python
import httpx
from fastmcp import FastMCP, Context

mcp = FastMCP(name="{name}")

@mcp.tool()
async def fetch_data(endpoint: str, ctx: Context) -> Dict[str, Any]:
    async with httpx.AsyncClient() as client:
        # Implementar lógica com retry
        pass
```
"""

    elif server_type == "data_processing":
        specific_template = """
## Requisitos de Processamento de Dados

### Ferramentas de Processamento
1. **process_file**
   - Aceita: CSV, JSON, Excel
   - Processamento assíncrono com progress reporting
   - Validação de schema com Pydantic

2. **analyze_data**
   - Análise estatística ou ML
   - Retorna insights estruturados
   - Suporte a datasets grandes (streaming)

### Recursos de Dados
1. **data://processed/{{id}}**
   - Acesso a dados processados
   - Paginação para grandes volumes

### Requisitos Técnicos
- Usar pandas/polars para processamento eficiente
- Implementar processamento em chunks para grandes arquivos
- Progress reporting via ctx.report_progress()
- Armazenamento temporário com cleanup automático

### Considerações de Performance
- Operações CPU-intensivas em thread pool
- Limitar uso de memória
- Implementar cache inteligente
"""

    elif server_type == "production_ready":
        specific_template = """
## Requisitos de Produção Completos

### Arquitetura
- **Estado**: Distribuído via Redis
- **Transporte**: HTTP Streamable com fallback
- **Deployment**: Docker + Kubernetes ready

### Segurança
- Autenticação via Bearer tokens
- Rate limiting por cliente
- Validação completa de entrada
- Sanitização de dados sensíveis em logs

### Observabilidade
- Logging estruturado (JSON)
- Métricas Prometheus
- Tracing com OpenTelemetry
- Health checks (liveness/readiness)

### Escalabilidade
- Servidor stateless
- Connection pooling
- Cache distribuído
- Graceful shutdown

### Ferramentas Principais
[DEFINIR FERRAMENTAS COM TODOS OS ASPECTOS ACIMA]

### Exemplo de Estrutura
```python
from fastmcp import FastMCP
import redis.asyncio as redis
import structlog

logger = structlog.get_logger()

mcp = FastMCP(
    name="{name}",
    dependencies=["redis", "prometheus-client", "opentelemetry-api"]
)

# Configurar Redis para estado distribuído
# Implementar middleware de autenticação
# Configurar métricas e tracing
```

### Testes Requeridos
- Testes unitários com pytest
- Testes de integração
- Testes de carga
- Testes de segurança
"""

    else:
        specific_template = "\n## Tipo de servidor não reconhecido. Use: basic, api_integration, data_processing, ou production_ready"

    full_template = base_template + specific_template

    # Adicionar seção de melhores práticas
    best_practices = """
## Melhores Práticas a Seguir

1. **Código Limpo**
   - Type hints em todas as funções
   - Docstrings descritivas
   - Nomes de variáveis significativos
   
2. **Tratamento de Erros**
   - Nunca deixar exceções não tratadas
   - Mensagens de erro úteis para debugging
   - Logging apropriado de erros
   
3. **Performance**
   - Async para todas as operações I/O
   - Evitar bloqueios desnecessários
   - Implementar timeouts apropriados
   
4. **Segurança**
   - Validar toda entrada de usuário
   - Não expor informações sensíveis
   - Usar HTTPS em produção
"""

    full_template += best_practices

    await ctx.info(f"Template gerado com sucesso para servidor '{server_type}'")
    return full_template.format(name=name)

# Recursos do servidor


@mcp.resource("mcp://best-practices")
async def get_mcp_best_practices() -> Dict[str, List[str]]:
    """
    Retorna um resumo das melhores práticas para desenvolvimento de servidores MCP.

    Inclui práticas de estrutura, técnicas e produção.
    """
    return BEST_PRACTICES


@mcp.resource("mcp://prompt-examples/{quality_level}")
async def get_prompt_examples(quality_level: str) -> Dict[str, Any]:
    """
    Fornece exemplos de prompts de diferentes níveis de qualidade.

    Níveis: bad, good, excellent
    """
    examples = {
        "bad": {
            "prompt": "criar servidor mcp que faz coisas com dados",
            "issues": [
                "Muito vago e genérico",
                "Não especifica ferramentas ou recursos",
                "Sem detalhes técnicos",
                "Sem exemplos de uso"
            ]
        },
        "good": {
            "prompt": """Criar um servidor MCP com FastMCP para processar arquivos CSV.
            
O servidor deve ter uma ferramenta para ler CSVs e retornar dados em JSON.
Deve tratar erros e validar o formato do arquivo.""",
            "strengths": [
                "Propósito claro",
                "Menciona formato de entrada/saída",
                "Considera tratamento de erros"
            ]
        },
        "excellent": {
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
    }

    if quality_level not in examples:
        return {"error": f"Nível '{quality_level}' não encontrado. Use: bad, good, ou excellent"}

    return examples[quality_level]


@mcp.resource("mcp://frameworks")
async def get_prompt_frameworks() -> Dict[str, Any]:
    """
    Retorna frameworks de prompt engineering aplicáveis a criação de servidores MCP.
    """
    return {
        "frameworks": {
            "CRISP": {
                "name": "Context, Requirements, Instructions, Specifications, Prompts",
                "description": "Framework estruturado para prompts complexos",
                "application": "Ideal para especificar servidores MCP completos",
                "template": """[Context] Preciso criar um servidor MCP para...
[Requirements] O servidor deve ter as seguintes capacidades...
[Instructions] Use FastMCP 2.0 com Python 3.8+...
[Specifications] Ferramentas: [...], Recursos: [...], Tipos: [...]
[Prompts/Examples] Exemplo de uso: ..."""
            },
            "STAR": {
                "name": "Situation, Task, Action, Result",
                "description": "Framework para prompts orientados a resultados",
                "application": "Bom para servidores com objetivo específico",
                "template": """[Situation] Temos dados de vendas em múltiplos formatos...
[Task] Precisamos de um servidor MCP que unifique e analise...
[Action] Implementar ferramentas para importar, processar e gerar relatórios...
[Result] O servidor deve retornar análises em formato JSON..."""
            },
            "Chain-of-Thought": {
                "name": "Pensamento passo a passo",
                "description": "Decompõe o problema em etapas lógicas",
                "application": "Útil para servidores com lógica complexa",
                "template": """Passo 1: Identificar os dados que o servidor processará
Passo 2: Definir as transformações necessárias
Passo 3: Especificar as ferramentas para cada transformação
Passo 4: Determinar os recursos a expor
Passo 5: Adicionar requisitos de erro e segurança"""
            }
        },
        "recommendation": "Para servidores MCP, o framework CRISP é geralmente mais eficaz devido à sua estrutura completa"
    }

# Prompts do servidor


@mcp.prompt("optimize_mcp_prompt")
async def optimize_mcp_prompt_template(
    user_context: str,
    requirements: str
) -> List[Dict[str, str]]:
    """
    Template de prompt para otimização de prompts MCP.
    """
    return [
        {
            "role": "system",
            "content": """Você é um especialista em criação de prompts para desenvolvimento de servidores MCP com FastMCP.
            
Suas especialidades incluem:
- Estruturação clara de requisitos
- Aplicação de melhores práticas do FastMCP
- Considerações de produção e escalabilidade
- Técnicas avançadas de prompt engineering

Ao otimizar prompts, você sempre:
1. Adiciona estrutura clara com seções bem definidas
2. Especifica ferramentas e recursos com detalhes
3. Inclui tipos de dados e exemplos
4. Considera aspectos de produção quando relevante
5. Sugere melhorias incrementais e práticas"""
        },
        {
            "role": "user",
            "content": f"""Contexto: {user_context}

Requisitos atuais: {requirements}

Por favor, otimize este prompt para criar um servidor MCP, seguindo as melhores práticas e tornando-o mais claro, completo e eficaz."""
        }
    ]


@mcp.prompt("mcp_code_review")
async def mcp_code_review_template(code: str) -> List[Dict[str, str]]:
    """
    Template para revisão de código de servidores MCP.
    """
    return [
        {
            "role": "system",
            "content": """Você é um revisor especializado em código FastMCP.
            
Ao revisar, você verifica:
- Uso correto dos decoradores @mcp.tool(), @mcp.resource(), @mcp.prompt()
- Type hints e docstrings adequadas
- Tratamento de erros apropriado
- Uso de async/await para operações I/O
- Padrões de segurança e validação
- Estrutura e organização do código"""
        },
        {
            "role": "user",
            "content": f"""Revise este código de servidor MCP e sugira melhorias:

```python
{code}
```

Identifique problemas e forneça sugestões específicas de melhoria."""
        }
    ]

# Função de inicialização do servidor


async def main():
    """Inicializa e executa o servidor MCP."""
    logger.info(f"Iniciando {mcp.name}...")
    logger.info("Servidor FastMCP configurado e pronto para uso")

    # O servidor FastMCP cuida do loop de eventos
    # Esta função é apenas para logging e inicialização se necessário

if __name__ == "__main__":
    # Para desenvolvimento/teste local
    import sys
    if "--test" in sys.argv:
        # Modo de teste - executar algumas validações
        asyncio.run(main())
    else:
        # Modo normal - o FastMCP gerencia a execução
        logger.info("Servidor pronto para execução via FastMCP CLI")
        # Iniciar o servidor FastMCP
        mcp.run()
