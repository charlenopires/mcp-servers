"""
Servidor MCP para aprimoramento de prompts de TypeScript
Baseado em melhores práticas e padrões de codificação modernos
"""

from typing import Dict, List, Optional, Any
from fastmcp import FastMCP
from pydantic import BaseModel, Field
import re
from datetime import datetime

# Inicializar o servidor MCP
mcp = FastMCP("Otimização de Prompts TypeScript")

# Modelos de dados


class AnalisePrompt(BaseModel):
    """Resultado da análise de um prompt TypeScript"""
    pontuacao: float = Field(
        description="Pontuação de qualidade do prompt (0-100)")
    pontos_fortes: List[str] = Field(
        description="Aspectos positivos do prompt")
    pontos_fracos: List[str] = Field(description="Aspectos a melhorar")
    recomendacoes: List[str] = Field(description="Recomendações específicas")
    categorias_ausentes: List[str] = Field(
        description="Categorias importantes não mencionadas")


class MelhoriaPrompt(BaseModel):
    """Sugestão de melhoria para um prompt"""
    prompt_melhorado: str = Field(description="Versão aprimorada do prompt")
    justificativa: str = Field(
        description="Explicação das melhorias aplicadas")
    tecnicas_aplicadas: List[str] = Field(
        description="Técnicas de melhoria utilizadas")


# Constantes com melhores práticas
CATEGORIAS_ESSENCIAIS = {
    "legibilidade": [
        "convenções de nomenclatura (PascalCase, camelCase)",
        "formatação com Prettier",
        "linting com ESLint",
        "modularização por funcionalidade",
        "documentação JSDoc/TSDoc"
    ],
    "tipagem": [
        "evitar any, usar unknown",
        "interfaces vs type aliases",
        "tipos utilitários (Readonly, Partial, Pick, Omit)",
        "discriminated unions",
        "type guards e type predicates"
    ],
    "performance": [
        "compilação incremental",
        "tree shaking e bundling",
        "estratégias de imutabilidade",
        "import type para tipos",
        "otimização de inferência de tipos"
    ],
    "arquitetura": [
        "abordagem híbrida OOP/FP",
        "princípios SOLID",
        "padrões de design GoF",
        "injeção de dependência",
        "separação de responsabilidades"
    ],
    "programacao_funcional": [
        "funções puras",
        "imutabilidade com readonly",
        "composição de funções",
        "tratamento de erros com Either/TaskEither",
        "uso de fp-ts para robustez"
    ],
    "seguranca": [
        "validação e sanitização de entradas",
        "evitar eval() e execução dinâmica",
        "Content Security Policy",
        "gerenciamento seguro de dependências",
        "princípio do menor privilégio"
    ],
    "testes": [
        "TDD com Jest/Vitest",
        "testes de unidade para funções puras",
        "mocking de dependências",
        "testes para TaskEither e tipos fp-ts",
        "cobertura de código"
    ],
    "escalabilidade": [
        "design modular e coeso",
        "programação assíncrona eficiente",
        "gerenciamento de estado desacoplado",
        "padrões de microsserviços",
        "documentação arquitetural (C4, ADRs)"
    ]
}

PALAVRAS_CHAVE_QUALIDADE = {
    "positivas": [
        "tipagem", "segurança de tipos", "performance", "escalável", "manutenível",
        "testável", "modular", "SOLID", "funcional", "imutável", "async/await",
        "error handling", "documentação", "clean code", "best practices"
    ],
    "alertas": [
        "any", "rápido", "simples", "básico", "exemplo", "sem tipos",
        "javascript puro", "sem testes", "monolítico"
    ]
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
    prompt_lower = prompt.lower()

    # Inicializar análise
    pontos_fortes = []
    pontos_fracos = []
    recomendacoes = []
    categorias_mencionadas = set()
    pontuacao = 50.0  # Pontuação base

    # Verificar menção a categorias essenciais
    for categoria, keywords in CATEGORIAS_ESSENCIAIS.items():
        categoria_encontrada = False
        for keyword in keywords:
            if keyword.lower() in prompt_lower:
                categoria_encontrada = True
                categorias_mencionadas.add(categoria)
                break

        if categoria_encontrada:
            pontos_fortes.append(f"Menciona aspectos de {categoria}")
            pontuacao += 5

    # Verificar palavras-chave de qualidade
    palavras_positivas_encontradas = []
    for palavra in PALAVRAS_CHAVE_QUALIDADE["positivas"]:
        if palavra.lower() in prompt_lower:
            palavras_positivas_encontradas.append(palavra)
            pontuacao += 2

    if palavras_positivas_encontradas:
        pontos_fortes.append(
            f"Usa termos técnicos apropriados: {', '.join(palavras_positivas_encontradas[:5])}")

    # Verificar palavras de alerta
    palavras_alerta_encontradas = []
    for palavra in PALAVRAS_CHAVE_QUALIDADE["alertas"]:
        if palavra.lower() in prompt_lower and palavra != "exemplo":  # exemplo pode ser válido em contexto
            palavras_alerta_encontradas.append(palavra)
            pontuacao -= 3

    if palavras_alerta_encontradas:
        pontos_fracos.append(
            f"Usa termos que podem indicar práticas subótimas: {', '.join(palavras_alerta_encontradas)}")

    # Verificar especificidade do prompt
    if len(prompt.split()) < 20:
        pontos_fracos.append(
            "Prompt muito curto - falta contexto e requisitos detalhados")
        pontuacao -= 10
    elif len(prompt.split()) > 50:
        pontos_fortes.append("Prompt detalhado com contexto adequado")
        pontuacao += 5

    # Verificar menção a abordagem híbrida OOP/FP
    if "oop" in prompt_lower and ("funcional" in prompt_lower or "fp" in prompt_lower):
        pontos_fortes.append("Menciona abordagem híbrida OOP/FP recomendada")
        pontuacao += 10
    elif "oop" not in prompt_lower and "funcional" not in prompt_lower:
        recomendacoes.append(
            "Considere especificar uma abordagem híbrida OOP/FP para máxima flexibilidade")

    # Verificar menção a fp-ts ou tratamento robusto de erros
    if "fp-ts" in prompt_lower or "either" in prompt_lower or "taskeither" in prompt_lower:
        pontos_fortes.append(
            "Menciona tratamento robusto de erros com tipos funcionais")
        pontuacao += 8
    else:
        recomendacoes.append(
            "Inclua requisitos para tratamento robusto de erros usando Either/TaskEither")

    # Verificar menção a testes
    if any(test in prompt_lower for test in ["test", "tdd", "jest", "vitest", "bdd"]):
        pontos_fortes.append("Inclui requisitos de testes")
        pontuacao += 7
    else:
        pontos_fracos.append("Não menciona estratégia de testes")
        recomendacoes.append(
            "Especifique requisitos de testes (TDD/BDD com Jest ou Vitest)")

    # Determinar categorias ausentes
    todas_categorias = set(CATEGORIAS_ESSENCIAIS.keys())
    categorias_ausentes = list(todas_categorias - categorias_mencionadas)

    # Adicionar recomendações para categorias ausentes
    # Top 3 categorias mais importantes
    for categoria in categorias_ausentes[:3]:
        recomendacoes.append(f"Adicione requisitos sobre {categoria}")

    # Verificar se menciona ESLint e Prettier
    if "eslint" not in prompt_lower or "prettier" not in prompt_lower:
        recomendacoes.append(
            "Especifique configuração de ESLint e Prettier para qualidade de código")

    # Ajustar pontuação final
    pontuacao = max(0.0, min(100.0, pontuacao))

    # Adicionar recomendação geral se pontuação baixa
    if pontuacao < 70:
        recomendacoes.insert(
            0, "Considere ser mais específico sobre os padrões de codificação desejados")

    return AnalisePrompt(
        pontuacao=pontuacao,
        pontos_fortes=pontos_fortes or ["Prompt básico fornecido"],
        pontos_fracos=pontos_fracos or [
            "Nenhum ponto fraco crítico identificado"],
        recomendacoes=recomendacoes or [
            "Continue refinando com requisitos específicos do projeto"],
        categorias_ausentes=categorias_ausentes
    )


@mcp.tool()
async def obter_melhores_praticas_mcp() -> Dict[str, str]:
    """
    Obter um resumo das melhores práticas de desenvolvimento de servidor MCP.

    Returns:
        Dict[str, str]: Principais melhores práticas para desenvolvimento de servidor MCP
    """
    return {
        "estrutura_codigo": """
- Use convenções de nomenclatura TypeScript (PascalCase para tipos, camelCase para variáveis)
- Organize código por funcionalidade, não por tipo técnico
- Um arquivo por componente lógico principal
- Módulos ES6 para importações explícitas
        """,
        "tipagem": """
- Evite 'any', use 'unknown' quando o tipo é desconhecido
- Prefira 'interface' para formas de objetos, 'type' para uniões/interseções
- Use tipos utilitários: Readonly<T>, Partial<T>, Pick<T,K>, Omit<T,K>
- Implemente discriminated unions para tipos complexos
        """,
        "abordagem_hibrida": """
- OOP para estrutura e modelagem de domínio (classes, serviços)
- FP para transformações de dados e lógica pura
- Princípios SOLID para design de classes
- Imutabilidade com readonly e bibliotecas como Immer
        """,
        "tratamento_erros": """
- Use Either<E,A> para operações síncronas que podem falhar
- Use TaskEither<E,A> para operações assíncronas
- Tipos de erro explícitos no sistema de tipos
- Evite throw em código funcional
        """,
        "performance": """
- Compilação incremental e skipLibCheck
- Tree shaking com módulos ESNext
- Import type para importações apenas de tipos
- Estratégias de imutabilidade conscientes de performance
        """,
        "seguranca": """
- Validação rigorosa de todas as entradas externas
- Evitar eval() e execução dinâmica de código
- Gerenciamento seguro de dependências
- Modificadores de acesso apropriados (private, protected)
        """,
        "testes": """
- TDD/BDD como prática padrão
- Jest ou Vitest para testes unitários
- Testes específicos para TaskEither e tipos fp-ts
- Cobertura mínima de 80% para código crítico
        """,
        "ferramentas": """
- ESLint com @typescript-eslint e eslint-plugin-functional
- Prettier para formatação consistente
- Husky para hooks de pre-commit
- TypeDoc para documentação de API
        """
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
    # Analisar o prompt original
    analise = await analisar_prompt_mcp(prompt_original)

    # Construir prompt melhorado
    melhorias = []
    prompt_melhorado = prompt_original

    # Adicionar contexto se muito curto
    if len(prompt_original.split()) < 30:
        contexto = """
Contexto: Preciso de um servidor MCP robusto e escalável seguindo as melhores práticas modernas de TypeScript.

"""
        prompt_melhorado = contexto + prompt_melhorado
        melhorias.append("Adicionado contexto para clareza")

    # Adicionar requisitos essenciais ausentes
    requisitos_adicionais = []

    if "híbrida" not in prompt_original.lower() and "oop" not in prompt_original.lower():
        requisitos_adicionais.append(
            "- Usar abordagem híbrida OOP/FP: classes para estrutura e serviços, "
            "funções puras e imutabilidade para lógica de negócios"
        )
        melhorias.append("Especificada abordagem híbrida OOP/FP")

    if "fp-ts" not in prompt_original.lower() and "either" not in prompt_original.lower():
        requisitos_adicionais.append(
            "- Implementar tratamento robusto de erros com Either/TaskEither (fp-ts) "
            "para operações que podem falhar"
        )
        melhorias.append("Adicionado tratamento robusto de erros")

    if "test" not in prompt_original.lower():
        requisitos_adicionais.append(
            "- Incluir testes unitários com Jest/Vitest seguindo TDD, "
            "com estratégias específicas para testar TaskEither"
        )
        melhorias.append("Adicionados requisitos de testes")

    if "eslint" not in prompt_original.lower():
        requisitos_adicionais.append(
            "- Configurar ESLint com @typescript-eslint e eslint-plugin-functional "
            "para enforçar padrões híbridos"
        )
        melhorias.append("Adicionada configuração de linting")

    if "segur" not in prompt_original.lower():
        requisitos_adicionais.append(
            "- Implementar validação rigorosa de entradas e práticas de segurança "
            "(evitar any, validar tipos em runtime)"
        )
        melhorias.append("Adicionados requisitos de segurança")

    # Adicionar requisitos ao prompt se necessário
    if requisitos_adicionais:
        prompt_melhorado += "\n\nRequisitos adicionais:\n" + \
            "\n".join(requisitos_adicionais)

    # Adicionar especificações técnicas se não presentes
    especificacoes = []

    if "typescript" in prompt_original.lower() and "versão" not in prompt_original.lower():
        especificacoes.append("- TypeScript 5.x com strict mode habilitado")

    if "performance" not in prompt_original.lower():
        especificacoes.append(
            "- Otimizações de performance: compilação incremental, tree shaking")

    if especificacoes:
        prompt_melhorado += "\n\nEspecificações técnicas:\n" + \
            "\n".join(especificacoes)
        melhorias.append("Adicionadas especificações técnicas")

    # Adicionar exemplo de estrutura se apropriado
    if len(analise.categorias_ausentes) > 3:
        prompt_melhorado += """

Estrutura esperada:
- Organização modular por funcionalidade
- Tipos explícitos e bem documentados (JSDoc)
- Serviços com injeção de dependência
- DTOs imutáveis com validação
- Testes abrangentes para todos os componentes
"""
        melhorias.append("Adicionado exemplo de estrutura esperada")

    justificativa = f"""
O prompt foi aprimorado para incluir as melhores práticas identificadas em projetos TypeScript modernos:

1. **Clareza e Especificidade**: {melhorias[0] if melhorias else 'Prompt já era claro'}
2. **Cobertura de Requisitos**: Adicionadas {len(requisitos_adicionais)} categorias essenciais ausentes
3. **Alinhamento com Padrões**: Especificados padrões de codificação e ferramentas recomendadas
4. **Foco em Qualidade**: Enfatizados aspectos de segurança, performance e manutenibilidade

Pontuação original: {analise.pontuacao:.1f}/100
Pontuação estimada após melhorias: {min(analise.pontuacao + len(melhorias) * 8, 95):.1f}/100
"""

    return {
        "prompt_melhorado": prompt_melhorado,
        "justificativa": justificativa,
        "melhorias_aplicadas": melhorias,
        "categorias_adicionadas": list(set(CATEGORIAS_ESSENCIAIS.keys()) - set(analise.categorias_ausentes))
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
    validacoes = {}
    requisitos_ausentes = []
    score_total = 0
    max_score = 0

    # Checklist de validação baseada nas melhores práticas
    checklist = {
        "Arquitetura e Design": {
            "Abordagem híbrida OOP/FP mencionada": ["híbrida", "oop", "funcional", "fp"],
            "Princípios SOLID mencionados": ["solid", "single responsibility", "open closed"],
            "Padrões de design especificados": ["padrão", "pattern", "factory", "singleton", "strategy"],
            "Modularização definida": ["modular", "módulo", "componente", "funcionalidade"]
        },
        "Tipagem e Segurança de Tipos": {
            "Evitar 'any' mencionado": ["evitar any", "no any", "unknown"],
            "Tipos utilitários mencionados": ["readonly", "partial", "pick", "omit"],
            "Discriminated unions": ["discriminated", "union", "tipo união"],
            "Type guards especificados": ["type guard", "is", "instanceof", "typeof"]
        },
        "Tratamento de Erros": {
            "Either/TaskEither mencionado": ["either", "taskeither", "fp-ts"],
            "Estratégia de erros definida": ["tratamento de erro", "error handling", "exceção"],
            "Tipos de erro especificados": ["tipo de erro", "error type", "custom error"]
        },
        "Performance": {
            "Otimizações de compilação": ["incremental", "skipLibCheck", "performance"],
            "Tree shaking mencionado": ["tree shaking", "bundling", "webpack", "rollup"],
            "Estratégias de imutabilidade": ["imutável", "immutable", "readonly", "immer"]
        },
        "Qualidade de Código": {
            "ESLint configurado": ["eslint", "linting", "lint"],
            "Prettier mencionado": ["prettier", "formatação", "format"],
            "Documentação especificada": ["jsdoc", "tsdoc", "documentação", "comentário"],
            "Convenções de nomenclatura": ["nomenclatura", "naming", "camelcase", "pascalcase"]
        },
        "Testes": {
            "Framework de testes especificado": ["jest", "vitest", "test", "tdd", "bdd"],
            "Estratégia de testes definida": ["teste unitário", "unit test", "cobertura", "coverage"],
            "Mocking mencionado": ["mock", "stub", "spy"]
        },
        "Segurança": {
            "Validação de entradas": ["validação", "sanitização", "validation", "sanitize"],
            "Práticas de segurança": ["segurança", "security", "csp", "owasp"],
            "Gerenciamento de dependências": ["dependência", "npm audit", "vulnerabilidade"]
        },
        "Escalabilidade": {
            "Arquitetura escalável": ["escalável", "scalable", "microsserviço", "modular monolith"],
            "Async/await eficiente": ["async", "await", "assíncrono", "promise"],
            "Gerenciamento de estado": ["estado", "state", "redux", "zustand"]
        }
    }

    # Validar cada categoria
    for categoria, items in checklist.items():
        validacoes[categoria] = {}
        for item, keywords in items.items():
            encontrado = any(
                keyword in requisitos_lower for keyword in keywords)
            validacoes[categoria][item] = encontrado
            max_score += 1
            if encontrado:
                score_total += 1
            else:
                requisitos_ausentes.append(f"{categoria}: {item}")

    # Calcular percentual de conformidade
    percentual_conformidade = (score_total / max_score) * \
        100 if max_score > 0 else 0

    # Determinar nível de maturidade
    if percentual_conformidade >= 90:
        nivel_maturidade = "Excelente - Requisitos muito bem definidos"
    elif percentual_conformidade >= 70:
        nivel_maturidade = "Bom - Requisitos sólidos com algumas lacunas"
    elif percentual_conformidade >= 50:
        nivel_maturidade = "Regular - Requisitos básicos presentes"
    else:
        nivel_maturidade = "Insuficiente - Muitos requisitos essenciais ausentes"

    # Recomendações prioritárias
    recomendacoes_prioritarias = []
    if not any(validacoes["Tratamento de Erros"][k] for k in validacoes["Tratamento de Erros"]):
        recomendacoes_prioritarias.append(
            "CRÍTICO: Adicione requisitos para tratamento robusto de erros com Either/TaskEither"
        )

    if not any(validacoes["Tipagem e Segurança de Tipos"][k] for k in validacoes["Tipagem e Segurança de Tipos"]):
        recomendacoes_prioritarias.append(
            "IMPORTANTE: Especifique estratégias de tipagem forte e segurança de tipos"
        )

    if not validacoes["Qualidade de Código"].get("ESLint configurado", False):
        recomendacoes_prioritarias.append(
            "RECOMENDADO: Configure ESLint com regras para abordagem híbrida OOP/FP"
        )

    return {
        "validacoes_detalhadas": validacoes,
        # Top 10 mais importantes
        "requisitos_ausentes": requisitos_ausentes[:10],
        "score_total": score_total,
        "max_score": max_score,
        "percentual_conformidade": f"{percentual_conformidade:.1f}%",
        "nivel_maturidade": nivel_maturidade,
        "recomendacoes_prioritarias": recomendacoes_prioritarias,
        "timestamp": datetime.now().isoformat()
    }

# Configuração do servidor
if __name__ == "__main__":
    # O servidor será executado quando o arquivo for chamado
    mcp.run()
