"""
Servidor MCP para Aprimoramento de Prompts de Criação de Servidores FastMCP

Este servidor ajuda usuários a criar prompts mais eficazes para desenvolvimento
de servidores MCP com FastMCP, seguindo as melhores práticas documentadas.
"""

import logging
from fastmcp import FastMCP, Context
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
import json
import re
from datetime import datetime

# Inicialização do servidor FastMCP
mcp = FastMCP(
    name="Otimizador de Prompts de Servidores MCP com FastMCP",
    description="Servidor MCP para aprimorar prompts de criação de servidores FastMCP",
    instructions="""Este servidor ajuda a criar prompts mais eficazes para desenvolvimento
    de servidores MCP com FastMCP. Use as ferramentas disponíveis para analisar,
    melhorar e validar seus prompts.""",
    version="1.0.0"
)

# Modelos Pydantic para estruturação de dados


class AnalisePrompt(BaseModel):
    """Resultado da análise de um prompt MCP"""
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


# Base de conhecimento de melhores práticas
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
        "Coletar métricas com Prometheus",
        "Configurar alertas para anomalias",
        "Manter logs detalhados de todas as interações"
    ]
}

# Palavras-chave para detectar intenções no prompt
PALAVRAS_CHAVE = {
    "ferramentas": ["tool", "ferramenta", "função", "executar", "ação", "comando"],
    "recursos": ["resource", "recurso", "dados", "informação", "consultar", "buscar"],
    "seguranca": ["segurança", "security", "autenticação", "auth", "token", "oauth", "validação"],
    "escalabilidade": ["escalar", "scale", "distribuído", "redis", "cluster", "performance"],
    "integracao": ["integrar", "api", "externo", "conectar", "webhook", "third-party"]
}


@mcp.tool()
async def analisar_prompt_mcp(prompt: str) -> AnalisePrompt:
    """
    Analisar um prompt de criação de servidor MCP para qualidade e alinhamento com melhores práticas.

    Args:
        prompt: O texto do prompt para analisar para criação de servidor MCP

    Returns:
        AnalisePrompt: Análise detalhada com pontuação, pontos fortes, pontos fracos e recomendações
    """
    pontuacao = 50  # Pontuação base
    pontos_fortes = []
    pontos_fracos = []
    sugestoes = []

    prompt_lower = prompt.lower()

    # Verificar presença de requisitos técnicos
    possui_requisitos_tecnicos = any(
        palavra in prompt_lower
        for categoria in PALAVRAS_CHAVE.values()
        for palavra in categoria
    )

    if possui_requisitos_tecnicos:
        pontuacao += 15
        pontos_fortes.append("Especifica requisitos técnicos")
    else:
        pontos_fracos.append("Falta especificação de requisitos técnicos")
        sugestoes.append(
            "Detalhe que tipos de ferramentas e recursos o servidor MCP deve ter")

    # Verificar contexto de negócio
    possui_contexto_negocio = any(
        palavra in prompt_lower
        for palavra in ["objetivo", "propósito", "problema", "solução", "caso de uso", "cenário"]
    )

    if possui_contexto_negocio:
        pontuacao += 15
        pontos_fortes.append("Inclui contexto de negócio")
    else:
        pontos_fracos.append("Falta contexto de negócio")
        sugestoes.append(
            "Explique o problema que o servidor MCP deve resolver")

    # Verificar considerações de segurança
    possui_restricoes_seguranca = any(
        palavra in prompt_lower
        for palavra in PALAVRAS_CHAVE["seguranca"]
    )

    if possui_restricoes_seguranca:
        pontuacao += 10
        pontos_fortes.append("Considera aspectos de segurança")
    else:
        pontos_fracos.append("Não menciona requisitos de segurança")
        sugestoes.append(
            "Especifique requisitos de autenticação e segurança necessários")

    # Verificar clareza e especificidade
    if len(prompt.split()) > 50:
        pontuacao += 10
        pontos_fortes.append("Prompt detalhado e específico")
    else:
        pontos_fracos.append("Prompt muito genérico")
        sugestoes.append(
            "Forneça mais detalhes sobre funcionalidades específicas")

    # Verificar menção a integrações
    if any(palavra in prompt_lower for palavra in PALAVRAS_CHAVE["integracao"]):
        pontuacao += 5
        pontos_fortes.append("Especifica integrações necessárias")

    # Verificar menção a escalabilidade
    if any(palavra in prompt_lower for palavra in PALAVRAS_CHAVE["escalabilidade"]):
        pontuacao += 5
        pontos_fortes.append("Considera requisitos de escalabilidade")

    # Garantir pontuação dentro do range
    pontuacao = min(100, max(0, pontuacao))

    return AnalisePrompt(
        pontuacao=pontuacao,
        pontos_fortes=pontos_fortes,
        pontos_fracos=pontos_fracos,
        sugestoes=sugestoes,
        possui_requisitos_tecnicos=possui_requisitos_tecnicos,
        possui_contexto_negocio=possui_contexto_negocio,
        possui_restricoes_seguranca=possui_restricoes_seguranca
    )


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


@mcp.resource("melhores-praticas://todas")
async def obter_melhores_praticas_mcp() -> Dict[str, List[str]]:
    """
    Obter um resumo das melhores práticas de desenvolvimento de servidor MCP.

    Returns:
        Dict[str, str]: Principais melhores práticas para desenvolvimento de servidor MCP
    """
    return MELHORES_PRATICAS


@mcp.resource("melhores-praticas://seguranca")
async def obter_praticas_seguranca() -> List[str]:
    """Obter melhores práticas específicas de segurança para servidores MCP."""
    return MELHORES_PRATICAS["seguranca"]


@mcp.resource("melhores-praticas://escalabilidade")
async def obter_praticas_escalabilidade() -> List[str]:
    """Obter melhores práticas de escalabilidade para servidores MCP."""
    return MELHORES_PRATICAS["escalabilidade"]


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


@mcp.resource("template://prompt-ideal")
async def obter_template_prompt_ideal() -> str:
    """Obter template de um prompt ideal para solicitar criação de servidor MCP."""
    return """# Prompt Ideal para Criação de Servidor MCP com FastMCP

## Contexto e Objetivo
Preciso criar um servidor MCP que [descreva o problema a resolver e o objetivo principal].

## Funcionalidades Requeridas

### Ferramentas (@mcp.tool())
1. **[Nome da Ferramenta]**: [Descrição do que faz]
   - Entrada: [Tipo e descrição dos parâmetros]
   - Saída: [Tipo e descrição do retorno]
   - Validação: [Requisitos de validação]

2. **[Outra Ferramenta]**: [Descrição]
   - ...

### Recursos (@mcp.resource())
1. **[URI do Recurso]**: [O que expõe]
   - Formato: [JSON/Text/etc]
   - Atualização: [Estático/Dinâmico]

### Integrações Externas
- [ ] API [Nome]: [Para que será usada]
- [ ] Banco de dados: [Tipo e propósito]
- [ ] Outros serviços: [Listar]

## Requisitos Técnicos

### Transporte
- [ ] STDIO (execução local)
- [ ] HTTP Streamable (web API)
- [ ] SSE (Server-Sent Events para streaming)

### Segurança
- [ ] Autenticação OAuth 2.1
- [ ] Validação de entrada com JSON Schema
- [ ] Rate limiting
- [ ] Sanitização de dados
- [ ] HTTPS/TLS

### Escalabilidade
- [ ] Suporte a múltiplas conexões simultâneas
- [ ] Estado distribuído com Redis
- [ ] Health checks (liveness/readiness)
- [ ] Processamento assíncrono

### Observabilidade
- [ ] Logging estruturado (JSON)
- [ ] Métricas com Prometheus
- [ ] Tracing com OpenTelemetry
- [ ] Correlation IDs

## Ambiente de Deployment
- [ ] Local/Development
- [ ] Docker/Kubernetes
- [ ] Serverless (AWS Lambda/Vercel)
- [ ] Cloud específica: [AWS/Azure/GCP]

## Restrições e Considerações
- Performance: [Requisitos de latência/throughput]
- Limites: [Rate limits, tamanho de payload]
- Compliance: [GDPR, HIPAA, etc]

## Exemplos de Uso
```python
# Exemplo de como o servidor será usado
# ...
```

## Critérios de Sucesso
- [ ] [Métrica ou resultado esperado]
- [ ] [Outro critério mensurável]
"""


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

# Configuração de logging para observabilidade


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


# Configurar logger
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Para executar o servidor
if __name__ == "__main__":
    import asyncio

    logger.info("Iniciando servidor FastMCP Prompt Enhancer")
    try:
        # FastMCP servers are typically run via the fastmcp command
        # For direct execution, call mcp.run() directly (it's not async)
        mcp.run()
    except ImportError:
        print("FastMCP not found. Install with: pip install fastmcp")
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        raise
