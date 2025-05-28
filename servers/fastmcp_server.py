"""
Servidor MCP Unificado para Otimização de Prompts FastMCP

Este servidor combina funcionalidades de análise de prompts, geração de templates
e aplicação de melhores práticas para desenvolvimento de servidores MCP com FastMCP.
"""

import logging
import json
import re
import asyncio
from datetime import datetime
from typing import Dict, List, Optional, Any, Union
from pydantic import BaseModel, Field
from fastmcp import FastMCP, Context

# Inicialização do servidor FastMCP
mcp = FastMCP(
    name="Servidor MCP Unificado para Otimização de Prompts FastMCP",
    description="Servidor completo para análise, otimização e geração de prompts para servidores FastMCP",
    instructions="""Este servidor oferece ferramentas abrangentes para:
    - Analisar qualidade de prompts de criação de servidores MCP
    - Sugerir melhorias específicas e contextuais
    - Gerar templates otimizados para diferentes tipos de servidor
    - Validar requisitos contra melhores práticas
    - Fornecer frameworks de prompt engineering
    Use as ferramentas disponíveis para criar prompts mais eficazes.""",
    version="2.0.0"
)

# Configuração de logging estruturado


class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_obj = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
        }
        if hasattr(record, 'correlation_id'):
            log_obj['correlation_id'] = record.correlation_id
        return json.dumps(log_obj)


logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Modelos Pydantic para estruturação de dados


class PromptAnalysis(BaseModel):
    """Resultado da análise de um prompt MCP (modelo internacional)"""
    score: float = Field(
        description="Pontuação de 0-100 indicando qualidade do prompt")
    strengths: List[str] = Field(
        description="Aspectos positivos identificados")
    weaknesses: List[str] = Field(description="Áreas que precisam melhorias")
    recommendations: List[str] = Field(
        description="Recomendações específicas de melhoria")
    has_technical_requirements: bool = Field(
        description="Se especifica requisitos técnicos")
    has_business_context: bool = Field(
        description="Se inclui contexto de negócio")
    has_security_considerations: bool = Field(
        description="Se menciona considerações de segurança")


class AnalisePrompt(BaseModel):
    """Resultado da análise de um prompt MCP (modelo em português)"""
    pontuacao: int = Field(
        description="Pontuação de 0-100 indicando qualidade do prompt")
    pontos_fortes: List[str] = Field(
        description="Aspectos positivos identificados")
    pontos_fracos: List[str] = Field(
        description="Áreas que precisam melhorias")
    sugestoes: List[str] = Field(
        description="Sugestões específicas de melhoria")
    possui_requisitos_tecnicos: bool = Field(
        description="Se o prompt especifica requisitos técnicos")
    possui_contexto_negocio: bool = Field(
        description="Se o prompt inclui contexto de negócio")
    possui_restricoes_seguranca: bool = Field(
        description="Se menciona considerações de segurança")


class MCPRequirement(BaseModel):
    """Requisitos para um servidor MCP"""
    ferramentas: List[str] = Field(
        default_factory=list, description="Lista de ferramentas necessárias")
    recursos: List[str] = Field(
        default_factory=list, description="Lista de recursos necessários")
    transportes: List[str] = Field(
        default_factory=list, description="Protocolos de transporte")
    autenticacao: bool = Field(
        default=False, description="Se requer autenticação")
    escalabilidade: bool = Field(
        default=False, description="Se precisa ser escalável")
    integracao_externa: List[str] = Field(
        default_factory=list, description="APIs externas necessárias")


# Base de conhecimento de melhores práticas (versão unificada e expandida)
BEST_PRACTICES = {
    "architecture": [
        "Use FastMCP 2.0+ with proper tool and resource decorators",
        "Implement modular structure with clear separation of concerns",
        "Choose appropriate transport protocol (STDIO, HTTP, SSE)",
        "Use Pydantic models for data validation and serialization",
        "Implement proper error handling with meaningful messages",
        "Follow async/await patterns for all I/O operations"
    ],
    "security": [
        "Implement OAuth 2.1 authentication with short-lived tokens",
        "Validate all inputs using JSON Schema",
        "Sanitize paths to prevent directory traversal",
        "Use HTTPS with valid TLS certificates",
        "Implement rate limiting to prevent DoS attacks",
        "Validate tool metadata rigorously",
        "Never expose sensitive information in logs"
    ],
    "scalability": [
        "Use Redis for distributed state storage",
        "Implement SSE transport for stateful connections",
        "Use asynchronous processing with async/await",
        "Implement health checks (liveness/readiness)",
        "Use connection pooling for external dependencies",
        "Consider serverless architecture when appropriate",
        "Implement circuit breakers for external APIs"
    ],
    "performance": [
        "Choose appropriate transport (STDIO for local, HTTP for web)",
        "Implement caching when possible",
        "Use parallel processing for independent tasks",
        "Optimize cold start in serverless environments",
        "Minimize latency with persistent connections",
        "Implement semantic chunking for large documents"
    ],
    "observability": [
        "Implement structured logging with JSON",
        "Use correlation IDs for tracing",
        "Integrate with OpenTelemetry for distributed traces",
        "Expose Prometheus metrics",
        "Implement comprehensive health checks",
        "Monitor tool execution times and error rates"
    ],
    "testing": [
        "Write comprehensive unit tests with pytest",
        "Test with fastmcp.Client",
        "Validate with MCP Inspector",
        "Test error scenarios and edge cases",
        "Implement integration tests for external APIs",
        "Use McpSafetyScanner for security testing"
    ]
}

MELHORES_PRATICAS = {
    "seguranca": [
        "Implementar autenticação OAuth 2.1 com tokens de curta duração",
        "Validar todas as entradas usando JSON Schema",
        "Sanitizar caminhos para prevenir directory traversal",
        "Usar HTTPS com certificados TLS válidos",
        "Implementar rate limiting para prevenir DoS",
        "Validar metadados de ferramentas rigorosamente"
    ],
    "escalabilidade": [
        "Usar Redis para armazenamento de estado distribuído",
        "Implementar transporte SSE para conexões stateful",
        "Utilizar processamento assíncrono com async/await",
        "Implementar health checks (liveness/readiness)",
        "Usar pooling de conexões para dependências externas",
        "Considerar arquitetura serverless quando apropriado"
    ],
    "modularidade": [
        "Separar ferramentas, recursos e prompts em módulos distintos",
        "Usar decoradores @mcp.tool() e @mcp.resource() adequadamente",
        "Implementar estrutura clara de diretórios",
        "Criar funções reutilizáveis e testáveis",
        "Usar mcp.mount() para composição de servidores",
        "Manter responsabilidades bem definidas"
    ],
    "desempenho": [
        "Escolher transporte apropriado (STDIO, HTTP, SSE)",
        "Implementar cache quando possível",
        "Usar processamento paralelo para tarefas independentes",
        "Otimizar inicialização a frio em ambientes serverless",
        "Minimizar latência com conexões persistentes",
        "Implementar fragmentação semântica para documentos grandes"
    ],
    "observabilidade": [
        "Implementar logging estruturado com JSON",
        "Usar correlation IDs para rastreamento",
        "Integrar com OpenTelemetry para traces distribuídos",
        "Expor métricas Prometheus",
        "Implementar health checks abrangentes",
        "Monitorar tempos de execução e taxas de erro"
    ]
}

# Palavras-chave para análise de prompts
KEYWORDS = {
    "tools": ["@mcp.tool", "tool", "ferramenta", "função", "ação", "comando"],
    "resources": ["@mcp.resource", "resource", "recurso", "dados", "informação"],
    "transport": ["stdio", "http", "sse", "streamable", "transporte", "protocolo"],
    "security": ["auth", "oauth", "security", "segurança", "autenticação", "validação"],
    "scalability": ["redis", "scale", "escala", "distribuído", "performance"],
    "business": ["objective", "objetivo", "propósito", "negócio", "problema", "usuário"]
}

PALAVRAS_CHAVE = {
    "ferramentas": ["@mcp.tool", "tool", "ferramenta", "função", "ação", "comando"],
    "recursos": ["@mcp.resource", "resource", "recurso", "dados", "informação"],
    "transporte": ["stdio", "http", "sse", "streamable", "transporte", "protocolo"],
    "seguranca": ["auth", "oauth", "security", "segurança", "autenticação", "validação"],
    "escalabilidade": ["redis", "scale", "escala", "distribuído", "performance"],
    "negocio": ["objective", "objetivo", "propósito", "negócio", "problema", "usuário"]
}

# Ferramentas de análise de prompt


@mcp.tool()
async def analyze_mcp_prompt(
    prompt: str,
    ctx: Optional[Context] = None
) -> PromptAnalysis:
    """
    Analisa um prompt de criação de servidor MCP e fornece feedback detalhado.

    Esta ferramenta avalia a qualidade do prompt considerando:
    - Clareza e completude dos requisitos
    - Aderência às melhores práticas do FastMCP  
    - Presença de elementos essenciais
    - Aspectos técnicos e de produção
    """
    if ctx:
        await ctx.info("Analyzing MCP prompt for quality and completeness...")

    prompt_lower = prompt.lower()
    score = 0.0
    strengths = []
    weaknesses = []
    recommendations = []

    # Análise de estrutura e clareza (0-25 pontos)
    if len(prompt) > 100:
        score += 10
        strengths.append(
            "Prompt has adequate length for detailed requirements")
    else:
        weaknesses.append("Prompt is too brief and lacks detail")
        recommendations.append("Expand prompt with more specific requirements")

    if any(word in prompt_lower for word in ["objective", "objetivo", "purpose", "propósito"]):
        score += 10
        strengths.append("Clear objective or purpose is defined")
    else:
        weaknesses.append("Missing clear objective or purpose")
        recommendations.append(
            "Add a clear statement of what the server should accomplish")

    if prompt.count('\n') > 3:
        score += 5
        strengths.append("Well-structured with multiple sections")
    else:
        weaknesses.append("Lacks clear structure")
        recommendations.append(
            "Organize into clear sections (Objective, Requirements, Technical, etc.)")

    # Análise técnica (0-30 pontos)
    has_tools = any(word in prompt_lower for word in KEYWORDS["tools"])
    has_resources = any(word in prompt_lower for word in KEYWORDS["resources"])

    if has_tools:
        score += 15
        strengths.append("Specifies tools/functions needed")
    else:
        weaknesses.append("Missing tool specifications")
        recommendations.append(
            "Define specific tools using @mcp.tool() pattern")

    if has_resources:
        score += 10
        strengths.append("Defines resources to expose")
    else:
        weaknesses.append("No resource specifications")
        recommendations.append(
            "Consider what data should be exposed via @mcp.resource()")

    if any(word in prompt_lower for word in KEYWORDS["transport"]):
        score += 5
        strengths.append("Mentions transport protocol")
    else:
        recommendations.append("Specify transport protocol (STDIO/HTTP/SSE)")

    # Análise de melhores práticas (0-25 pontos)
    has_security = any(word in prompt_lower for word in KEYWORDS["security"])
    has_scalability = any(
        word in prompt_lower for word in KEYWORDS["scalability"])

    if has_security:
        score += 10
        strengths.append("Considers security requirements")
    else:
        weaknesses.append("Missing security considerations")
        recommendations.append(
            "Add authentication and validation requirements")

    if has_scalability:
        score += 10
        strengths.append("Addresses scalability concerns")
    else:
        recommendations.append(
            "Consider scalability requirements for production use")

    if any(word in prompt_lower for word in ["async", "assíncrono", "await"]):
        score += 5
        strengths.append("Mentions asynchronous processing")

    # Análise de contexto de negócio (0-20 pontos)
    has_business_context = any(
        word in prompt_lower for word in KEYWORDS["business"])

    if has_business_context:
        score += 15
        strengths.append("Includes business context and objectives")
    else:
        weaknesses.append("Lacks business context")
        recommendations.append(
            "Explain the business problem this server will solve")

    if any(word in prompt_lower for word in ["example", "exemplo", "usage", "uso"]):
        score += 5
        strengths.append("Includes usage examples")
    else:
        recommendations.append("Add concrete usage examples")

    return PromptAnalysis(
        score=min(100.0, score),
        strengths=strengths,
        weaknesses=weaknesses,
        recommendations=recommendations,
        has_technical_requirements=has_tools or has_resources,
        has_business_context=has_business_context,
        has_security_considerations=has_security
    )


@mcp.tool()
async def analisar_prompt_mcp(prompt: str) -> AnalisePrompt:
    """
    Analisar um prompt de criação de servidor MCP para qualidade e alinhamento com melhores práticas.

    Args:
        prompt: O texto do prompt para analisar para criação de servidor MCP

    Returns:
        AnalisePrompt: Análise detalhada com pontuação, pontos fortes, pontos fracos e recomendações
    """
    prompt_lower = prompt.lower()
    pontuacao = 0
    pontos_fortes = []
    pontos_fracos = []
    sugestoes = []

    # Análise de estrutura básica (0-20 pontos)
    if len(prompt) > 100:
        pontuacao += 10
        pontos_fortes.append(
            "Prompt tem comprimento adequado para especificações detalhadas")
    else:
        pontos_fracos.append("Prompt muito breve, falta detalhamento")
        sugestoes.append("Expanda o prompt com requisitos mais específicos")

    if any(palavra in prompt_lower for palavra in ["objetivo", "propósito", "serve para"]):
        pontuacao += 10
        pontos_fortes.append("Objetivo ou propósito bem definido")
    else:
        pontos_fracos.append("Falta definição clara do objetivo")
        sugestoes.append(
            "Adicione uma declaração clara do que o servidor deve fazer")

    # Análise técnica (0-35 pontos)
    possui_requisitos_tecnicos = False

    if any(palavra in prompt_lower for palavra in PALAVRAS_CHAVE["ferramentas"]):
        pontuacao += 15
        pontos_fortes.append("Especifica ferramentas necessárias")
        possui_requisitos_tecnicos = True
    else:
        pontos_fracos.append("Não especifica ferramentas necessárias")
        sugestoes.append(
            "Defina ferramentas específicas usando padrão @mcp.tool()")

    if any(palavra in prompt_lower for palavra in PALAVRAS_CHAVE["recursos"]):
        pontuacao += 10
        pontos_fortes.append("Define recursos a serem expostos")
        possui_requisitos_tecnicos = True
    else:
        pontos_fracos.append("Não especifica recursos")
        sugestoes.append(
            "Considere quais dados devem ser expostos via @mcp.resource()")

    if any(palavra in prompt_lower for palavra in PALAVRAS_CHAVE["transporte"]):
        pontuacao += 5
        pontos_fortes.append("Menciona protocolo de transporte")
    else:
        sugestoes.append(
            "Especifique protocolo de transporte (STDIO/HTTP/SSE)")

    if any(palavra in prompt_lower for palavra in ["type", "tipos", "pydantic", "validação"]):
        pontuacao += 5
        pontos_fortes.append("Considera tipagem e validação")

    # Análise de segurança (0-20 pontos)
    possui_restricoes_seguranca = False

    if any(palavra in prompt_lower for palavra in PALAVRAS_CHAVE["seguranca"]):
        pontuacao += 15
        pontos_fortes.append("Considera requisitos de segurança")
        possui_restricoes_seguranca = True
    else:
        pontos_fracos.append("Não menciona considerações de segurança")
        sugestoes.append("Adicione requisitos de autenticação e validação")

    if any(palavra in prompt_lower for palavra in ["validar", "sanitizar", "verificar"]):
        pontuacao += 5
        pontos_fortes.append("Menciona validação de dados")

    # Análise de contexto de negócio (0-15 pontos)
    possui_contexto_negocio = False

    if any(palavra in prompt_lower for palavra in PALAVRAS_CHAVE["negocio"]):
        pontuacao += 10
        pontos_fortes.append("Inclui contexto de negócio")
        possui_contexto_negocio = True
    else:
        pontos_fracos.append("Falta contexto de negócio")
        sugestoes.append(
            "Explique o problema de negócio que o servidor resolve")

    if any(palavra in prompt_lower for palavra in ["exemplo", "uso", "chamada"]):
        pontuacao += 5
        pontos_fortes.append("Inclui exemplos de uso")
    else:
        sugestoes.append("Adicione exemplos concretos de uso")

    # Análise de escalabilidade (0-10 pontos)
    if any(palavra in prompt_lower for palavra in PALAVRAS_CHAVE["escalabilidade"]):
        pontuacao += 10
        pontos_fortes.append("Considera escalabilidade")
    else:
        sugestoes.append(
            "Considere requisitos de escalabilidade para produção")

    return AnalisePrompt(
        pontuacao=pontuacao,
        pontos_fortes=pontos_fortes,
        pontos_fracos=pontos_fracos,
        sugestoes=sugestoes,
        possui_requisitos_tecnicos=possui_requisitos_tecnicos,
        possui_contexto_negocio=possui_contexto_negocio,
        possui_restricoes_seguranca=possui_restricoes_seguranca
    )

# Ferramentas de otimização de prompt


@mcp.tool()
async def suggest_mcp_prompt_improvements(
    original_prompt: str,
    focus_area: Optional[str] = None,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Sugere melhorias específicas para um prompt de criação de servidor MCP.

    Retorna um prompt melhorado e explica as mudanças aplicadas.
    """
    if ctx:
        await ctx.info(f"Generating improvement suggestions for prompt...")

    # Analisar o prompt original primeiro
    analysis = await analyze_mcp_prompt(original_prompt, ctx) if ctx else PromptAnalysis(
        score=50.0, strengths=[], weaknesses=["Simplified analysis"], recommendations=[]
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
async def sugerir_melhorias_prompt(prompt_original: str) -> Dict[str, Any]:
    """
    Sugerir melhorias específicas para um prompt de criação de servidor MCP.

    Args:
        prompt_original: O prompt original para melhorar

    Returns:
        Dict contendo prompt melhorado e explicação das mudanças
    """
    analise = await analisar_prompt_mcp(prompt_original)

    melhorias = []
    prompt_melhorado = prompt_original

    # Adicionar contexto técnico se necessário
    if not analise.possui_requisitos_tecnicos:
        melhorias.append("Adicionado especificação de ferramentas e recursos")
        prompt_melhorado += "\n\nO servidor deve incluir:\n"
        prompt_melhorado += "- Ferramentas (@mcp.tool()) para [especifique as ações]\n"
        prompt_melhorado += "- Recursos (@mcp.resource()) para [especifique os dados]\n"
        prompt_melhorado += "- Transporte apropriado (STDIO/HTTP/SSE) baseado no caso de uso\n"

    # Adicionar segurança se não mencionada
    if not analise.possui_restricoes_seguranca:
        melhorias.append("Adicionado requisitos de segurança")
        prompt_melhorado += "\n\nRequisitos de segurança:\n"
        prompt_melhorado += "- Implementar validação de entrada com JSON Schema\n"
        prompt_melhorado += "- Usar autenticação OAuth 2.1 se necessário\n"
        prompt_melhorado += "- Sanitizar todas as entradas do usuário\n"

    # Adicionar contexto de negócio
    if not analise.possui_contexto_negocio:
        melhorias.append("Adicionado template para contexto de negócio")
        prompt_melhorado += "\n\nContexto e objetivos:\n"
        prompt_melhorado += "- Problema a resolver: [descreva o problema]\n"
        prompt_melhorado += "- Usuários alvo: [quem usará o servidor]\n"
        prompt_melhorado += "- Resultado esperado: [o que o servidor deve entregar]\n"

    # Adicionar melhores práticas
    prompt_melhorado += "\n\nMelhores práticas a seguir:\n"
    prompt_melhorado += "- Usar type hints e docstrings detalhadas\n"
    prompt_melhorado += "- Implementar tratamento de erros adequado\n"
    prompt_melhorado += "- Seguir estrutura modular com separação clara\n"
    prompt_melhorado += "- Incluir testes e documentação\n"

    return {
        "prompt_original": prompt_original,
        "prompt_melhorado": prompt_melhorado,
        "melhorias_aplicadas": melhorias,
        "pontuacao_original": analise.pontuacao,
        "pontuacao_estimada": min(100, analise.pontuacao + len(melhorias) * 15)
    }

# Ferramentas de validação


@mcp.tool()
async def validate_mcp_requirements(
    requirements: str,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Valida requisitos de servidor MCP contra checklist de melhores práticas.

    Verifica completude e adequação dos requisitos especificados.
    """
    if ctx:
        await ctx.info("Validating requirements against best practices...")

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

    if ctx:
        await ctx.info(f"Validation completed. Score: {validation_results['completeness_score']:.0f}%")

    return validation_results


@mcp.tool()
async def validar_requisitos_mcp(requisitos: str) -> Dict[str, Any]:
    """
    Validar requisitos de servidor MCP contra lista de verificação de melhores práticas.

    Args:
        requisitos: A especificação de requisitos para validar

    Returns:
        Dict contendo resultados de validação e requisitos ausentes
    """
    requisitos_lower = requisitos.lower()
    validacao = {
        "ferramentas_definidas": False,
        "recursos_definidos": False,
        "transporte_especificado": False,
        "seguranca_considerada": False,
        "escalabilidade_planejada": False,
        "observabilidade_incluida": False,
        "testes_mencionados": False,
        "documentacao_planejada": False
    }

    requisitos_ausentes = []
    recomendacoes = []

    # Validar presença de ferramentas
    if any(palavra in requisitos_lower for palavra in PALAVRAS_CHAVE["ferramentas"]):
        validacao["ferramentas_definidas"] = True
    else:
        requisitos_ausentes.append("Definição de ferramentas (@mcp.tool())")
        recomendacoes.append(
            "Especifique quais ações o servidor deve executar")

    # Validar recursos
    if any(palavra in requisitos_lower for palavra in PALAVRAS_CHAVE["recursos"]):
        validacao["recursos_definidos"] = True
    else:
        requisitos_ausentes.append("Definição de recursos (@mcp.resource())")
        recomendacoes.append("Defina quais dados o servidor deve expor")

    # Validar transporte
    transportes = ["stdio", "http", "sse", "streamable"]
    if any(t in requisitos_lower for t in transportes):
        validacao["transporte_especificado"] = True
    else:
        requisitos_ausentes.append("Especificação de protocolo de transporte")
        recomendacoes.append(
            "Escolha entre STDIO (local), HTTP (web) ou SSE (streaming)")

    # Validar segurança
    if any(palavra in requisitos_lower for palavra in PALAVRAS_CHAVE["seguranca"]):
        validacao["seguranca_considerada"] = True
    else:
        requisitos_ausentes.append("Requisitos de segurança")
        recomendacoes.append(
            "Defina autenticação, validação de entrada e sanitização")

    # Validar escalabilidade
    if any(palavra in requisitos_lower for palavra in PALAVRAS_CHAVE["escalabilidade"]):
        validacao["escalabilidade_planejada"] = True
    else:
        requisitos_ausentes.append("Planejamento de escalabilidade")
        recomendacoes.append(
            "Considere uso de Redis para estado distribuído se necessário")

    # Validar observabilidade
    obs_palavras = ["log", "metric", "trace", "monitor", "observ"]
    if any(palavra in requisitos_lower for palavra in obs_palavras):
        validacao["observabilidade_incluida"] = True
    else:
        requisitos_ausentes.append("Estratégia de observabilidade")
        recomendacoes.append("Planeje logging estruturado e métricas")

    # Validar testes
    if any(palavra in requisitos_lower for palavra in ["test", "pytest", "unittest"]):
        validacao["testes_mencionados"] = True
    else:
        requisitos_ausentes.append("Estratégia de testes")
        recomendacoes.append("Inclua testes unitários e de integração")

    # Validar documentação
    if any(palavra in requisitos_lower for palavra in ["doc", "readme", "exemplo"]):
        validacao["documentacao_planejada"] = True
    else:
        requisitos_ausentes.append("Plano de documentação")
        recomendacoes.append("Planeje documentação com exemplos de uso")

    # Calcular pontuação de completude
    total_validacoes = len(validacao)
    validacoes_passadas = sum(1 for v in validacao.values() if v)
    completude = int((validacoes_passadas / total_validacoes) * 100)

    return {
        "validacao": validacao,
        "requisitos_ausentes": requisitos_ausentes,
        "recomendacoes": recomendacoes,
        "completude_percentual": completude,
        "pronto_para_desenvolvimento": completude >= 80
    }

# Ferramentas de geração de templates


@mcp.tool()
async def generate_mcp_server_template(
    server_type: str,
    name: str,
    description: str,
    ctx: Optional[Context] = None
) -> str:
    """
    Gera um template de prompt otimizado para criar um servidor MCP específico.

    Templates disponíveis:
    - basic: Servidor simples com ferramentas e recursos básicos
    - api_integration: Servidor que integra com APIs externas
    - data_processing: Servidor focado em processamento de dados
    - production_ready: Servidor com todas as práticas de produção
    """
    if ctx:
        await ctx.info(f"Generating template for server type '{server_type}'...")

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
        specific_template = f"""
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
        specific_template = f"""
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
        specific_template = f"""
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

    if ctx:
        await ctx.info(f"Template generated successfully for '{server_type}' server")

    return full_template.format(name=name)

# Recursos do servidor


@mcp.resource("mcp://best-practices")
async def get_mcp_best_practices() -> Dict[str, List[str]]:
    """
    Retorna um resumo das melhores práticas para desenvolvimento de servidores MCP.

    Inclui práticas de estrutura, técnicas e produção.
    """
    return BEST_PRACTICES


@mcp.resource("melhores-praticas://todas")
async def obter_melhores_praticas_mcp() -> Dict[str, List[str]]:
    """
    Obter um resumo das melhores práticas de desenvolvimento de servidor MCP.

    Returns:
        Dict[str, List[str]]: Principais melhores práticas para desenvolvimento de servidor MCP
    """
    return MELHORES_PRATICAS


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


@mcp.resource("template://servidor-basico")
async def obter_template_basico() -> str:
    """Obter template básico para criar um servidor FastMCP."""
    return '''"""
Servidor MCP para [DESCREVA O PROPÓSITO]

Este servidor [DESCREVA O QUE FAZ].
"""

from fastmcp import FastMCP, Context
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
import asyncio

# Inicializar servidor
mcp = FastMCP(
    name="meu-servidor-mcp",
    description="[DESCRIÇÃO DO SERVIDOR]",
    version="1.0.0"
)

# Modelos de dados
class MeuModelo(BaseModel):
    """Modelo para [DESCREVA]"""
    campo: str = Field(description="Descrição do campo")

# Ferramentas
@mcp.tool()
async def minha_ferramenta(parametro: str) -> str:
    """
    [DESCREVA O QUE A FERRAMENTA FAZ]
    
    Args:
        parametro: [DESCREVA O PARÂMETRO]
        
    Returns:
        [DESCREVA O RETORNO]
    """
    # Implementar lógica aqui
    return f"Processado: {parametro}"

# Recursos
@mcp.resource("dados://exemplo")
async def meu_recurso() -> Dict[str, Any]:
    """[DESCREVA O RECURSO]"""
    return {"exemplo": "dados"}

# Para executar localmente
if __name__ == "__main__":
    import asyncio
    from fastmcp.cli import main
    asyncio.run(main(mcp))
'''


@mcp.resource("checklist://desenvolvimento")
async def obter_checklist_desenvolvimento() -> Dict[str, List[str]]:
    """Obter checklist completo para desenvolvimento de servidor MCP."""
    return {
        "planejamento": [
            "Definir objetivo e escopo do servidor",
            "Identificar ferramentas necessárias",
            "Mapear recursos a expor",
            "Escolher protocolo de transporte",
            "Definir requisitos de segurança",
            "Planejar estratégia de escalabilidade"
        ],
        "desenvolvimento": [
            "Configurar ambiente Python 3.8+",
            "Instalar FastMCP via pip/uv",
            "Criar estrutura de diretórios modular",
            "Implementar ferramentas com @mcp.tool()",
            "Implementar recursos com @mcp.resource()",
            "Adicionar type hints e docstrings",
            "Implementar validação de entrada",
            "Adicionar tratamento de erros",
            "Configurar logging estruturado"
        ],
        "testes": [
            "Escrever testes unitários com pytest",
            "Testar com fastmcp.Client",
            "Validar com MCP Inspector",
            "Testar cenários de erro",
            "Verificar performance",
            "Testar integrações externas"
        ],
        "seguranca": [
            "Implementar autenticação se necessário",
            "Validar todas as entradas",
            "Sanitizar dados sensíveis",
            "Configurar HTTPS em produção",
            "Implementar rate limiting",
            "Revisar código para vulnerabilidades",
            "Testar com McpSafetyScanner"
        ],
        "deployment": [
            "Configurar CI/CD pipeline",
            "Criar Dockerfile se necessário",
            "Configurar health checks",
            "Implementar monitoramento",
            "Configurar backups",
            "Documentar processo de deployment",
            "Criar runbook operacional"
        ],
        "documentacao": [
            "Escrever README completo",
            "Documentar API de ferramentas",
            "Criar exemplos de uso",
            "Documentar configuração",
            "Adicionar troubleshooting guide",
            "Manter changelog atualizado"
        ]
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


@mcp.prompt("criar_servidor_mcp")
async def prompt_criar_servidor(
    objetivo: str,
    ferramentas_necessarias: List[str],
    tem_integracao_externa: bool = False,
    precisa_escalar: bool = False
) -> List[Dict[str, str]]:
    """
    Gerar um prompt otimizado para criar servidor MCP.

    Args:
        objetivo: O que o servidor deve fazer
        ferramentas_necessarias: Lista de ferramentas requeridas
        tem_integracao_externa: Se precisa integrar com APIs externas
        precisa_escalar: Se precisa suportar alta carga

    Returns:
        Lista de mensagens para o prompt
    """
    prompt_parts = [
        f"Crie um servidor MCP com FastMCP em Python que {objetivo}.",
        "\nRequisitos técnicos:",
        f"- Ferramentas necessárias: {', '.join(ferramentas_necessarias)}",
        "- Use type hints e docstrings detalhadas",
        "- Implemente validação de entrada com Pydantic",
        "- Adicione tratamento de erros apropriado",
        "- Siga estrutura modular com separação clara"
    ]

    if tem_integracao_externa:
        prompt_parts.extend([
            "\nIntegrações:",
            "- Configure clients HTTP assíncronos para APIs externas",
            "- Implemente retry logic e circuit breakers",
            "- Use variáveis de ambiente para credenciais"
        ])

    if precisa_escalar:
        prompt_parts.extend([
            "\nEscalabilidade:",
            "- Use Redis para estado distribuído",
            "- Implemente connection pooling",
            "- Configure health checks adequados",
            "- Use processamento assíncrono"
        ])

    prompt_parts.extend([
        "\nSegurança:",
        "- Valide todas as entradas com JSON Schema",
        "- Sanitize paths e dados do usuário",
        "- Implemente rate limiting se apropriado",
        "\nInclua também:",
        "- Exemplo de uso completo",
        "- Instruções de configuração",
        "- Testes básicos com pytest"
    ])

    return [
        {"role": "user", "content": "\n".join(prompt_parts)}
    ]

# Função de inicialização do servidor


async def main():
    """Inicializa e executa o servidor MCP."""
    logger.info(f"Iniciando {mcp.name}...")
    logger.info("Servidor FastMCP unificado configurado e pronto para uso")

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
