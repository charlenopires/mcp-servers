"""
Servidor MCP de Engenharia de Prompts
Implementa técnicas avançadas de engenharia de prompts para otimizar consultas
"""

from typing import Dict, List, Optional, Any
from fastmcp import FastMCP
from pydantic import BaseModel
import re
from enum import Enum

# Inicializa o servidor MCP
mcp = FastMCP("Assistente de Melhores Práticas de Engenharia de Prompts")


class TaskType(Enum):
    """Tipos de tarefas identificadas"""
    TEXT_GENERATION = "text_generation"
    CODE_GENERATION = "code_generation"
    IMAGE_GENERATION = "image_generation"
    ANALYSIS = "analysis"
    CREATIVE = "creative"
    PROBLEM_SOLVING = "problem_solving"
    QUESTION_ANSWERING = "question_answering"
    TRANSLATION = "translation"
    SUMMARIZATION = "summarization"


class PromptOptimizationRequest(BaseModel):
    """Modelo de requisição para otimização de prompt"""
    prompt: str
    task_type: Optional[str] = None
    target_audience: Optional[str] = None
    desired_length: Optional[str] = None
    tone: Optional[str] = None


class OptimizedPrompt(BaseModel):
    """Modelo de resposta com prompt otimizado"""
    original_prompt: str
    optimized_prompt: str
    techniques_applied: List[str]
    task_type: str
    suggestions: List[str]


class PromptEngineer:
    """Classe principal para engenharia de prompts"""

    def __init__(self):
        self.frameworks = {
            "RACE": ["Role", "Action", "Context", "Expectation"],
            "TRACE": ["Task", "Request", "Action", "Context", "Example"],
            "CRISPE": ["Capacity/Role", "Insight", "Statement", "Personality", "Experiment"],
            "CORE": ["Contexto", "Objetivo", "Papel", "Exemplo"],
            "COAST": ["Context", "Objective", "Actions", "Scenario", "Task"]
        }

        self.techniques = {
            "clareza": self._apply_clarity,
            "contexto": self._apply_context,
            "persona": self._apply_persona,
            "few_shot": self._apply_few_shot,
            "cot": self._apply_chain_of_thought,
            "formato": self._apply_format_specification,
            "delimitadores": self._apply_delimiters
        }

    def identify_task_type(self, prompt: str) -> TaskType:
        """Identifica o tipo de tarefa baseado no prompt"""
        prompt_lower = prompt.lower()

        # Palavras-chave para cada tipo de tarefa
        keywords = {
            TaskType.CODE_GENERATION: ["código", "programa", "função", "script", "implementar", "desenvolver"],
            TaskType.IMAGE_GENERATION: ["imagem", "desenhe", "crie uma ilustração", "gere uma foto"],
            TaskType.ANALYSIS: ["analise", "avalie", "examine", "investigue", "compare"],
            TaskType.CREATIVE: ["crie", "invente", "imagine", "história", "poema", "criativo"],
            TaskType.PROBLEM_SOLVING: ["resolva", "solucione", "como fazer", "problema", "desafio"],
            TaskType.QUESTION_ANSWERING: ["o que é", "quem é", "quando", "onde", "por que", "explique"],
            TaskType.TRANSLATION: ["traduza", "tradução", "para inglês", "para português"],
            TaskType.SUMMARIZATION: [
                "resuma", "resumo", "sintetize", "principais pontos"]
        }

        for task_type, words in keywords.items():
            if any(word in prompt_lower for word in words):
                return task_type

        return TaskType.TEXT_GENERATION

    def _apply_clarity(self, prompt: str, context: Dict[str, Any]) -> str:
        """Aplica técnicas de clareza e especificidade"""
        # Remove ambiguidades comuns
        clarity_improvements = {
            "isso": "o conceito/item mencionado anteriormente",
            "aquilo": "o elemento específico",
            "coisa": "o objeto/conceito",
            "fazer": "executar/realizar a tarefa específica"
        }

        improved = prompt
        for vague, specific in clarity_improvements.items():
            if vague in improved.lower():
                improved = re.sub(
                    rf'\b{vague}\b', specific, improved, flags=re.IGNORECASE)

        return improved

    def _apply_context(self, prompt: str, context: Dict[str, Any]) -> str:
        """Adiciona contexto relevante ao prompt"""
        context_additions = []

        if context.get("target_audience"):
            context_additions.append(
                f"Público-alvo: {context['target_audience']}")

        if context.get("desired_length"):
            context_additions.append(
                f"Extensão desejada: {context['desired_length']}")

        if context.get("tone"):
            context_additions.append(f"Tom: {context['tone']}")

        if context_additions:
            return f"{prompt}\n\nContexto:\n" + "\n".join(f"- {item}" for item in context_additions)

        return prompt

    def _apply_persona(self, prompt: str, task_type: TaskType) -> str:
        """Aplica atribuição de papel baseado no tipo de tarefa"""
        personas = {
            TaskType.CODE_GENERATION: "Você é um desenvolvedor de software experiente com profundo conhecimento em boas práticas de programação",
            TaskType.ANALYSIS: "Você é um analista especializado com capacidade de examinar dados e informações de forma crítica e detalhada",
            TaskType.CREATIVE: "Você é um escritor criativo com habilidade para criar conteúdo original e envolvente",
            TaskType.PROBLEM_SOLVING: "Você é um consultor especializado em resolução de problemas complexos",
            TaskType.QUESTION_ANSWERING: "Você é um especialista no assunto com capacidade de explicar conceitos de forma clara e didática"
        }

        persona = personas.get(
            task_type, "Você é um assistente útil e conhecedor")
        return f"{persona}.\n\n{prompt}"

    def _apply_few_shot(self, prompt: str, task_type: TaskType) -> str:
        """Adiciona exemplos relevantes quando apropriado"""
        if task_type == TaskType.CODE_GENERATION:
            return prompt + "\n\nExemplo de formato esperado:\n```python\ndef funcao_exemplo():\n    # Implementação clara e comentada\n    pass\n```"
        elif task_type == TaskType.ANALYSIS:
            return prompt + "\n\nEstrutura esperada:\n1. Introdução\n2. Análise detalhada\n3. Conclusões\n4. Recomendações"

        return prompt

    def _apply_chain_of_thought(self, prompt: str, task_type: TaskType) -> str:
        """Aplica Chain-of-Thought para tarefas complexas"""
        if task_type in [TaskType.PROBLEM_SOLVING, TaskType.ANALYSIS]:
            return prompt + "\n\nPor favor, pense passo a passo e mostre seu raciocínio antes de chegar à resposta final."

        return prompt

    def _apply_format_specification(self, prompt: str, context: Dict[str, Any]) -> str:
        """Especifica o formato de saída desejado"""
        format_specs = []

        if "lista" in prompt.lower():
            format_specs.append("Formato: Lista com marcadores")
        elif "tabela" in prompt.lower():
            format_specs.append("Formato: Tabela estruturada")
        elif "json" in prompt.lower():
            format_specs.append("Formato: JSON válido")

        if format_specs:
            return prompt + "\n\n" + "\n".join(format_specs)

        return prompt

    def _apply_delimiters(self, prompt: str) -> str:
        """Aplica delimitadores para melhor estruturação"""
        # Identifica seções do prompt
        if "\n" in prompt and len(prompt.split("\n")) > 2:
            sections = prompt.split("\n")
            structured = "### Solicitação Principal ###\n" + sections[0]

            if len(sections) > 1:
                structured += "\n\n### Detalhes Adicionais ###\n" + \
                    "\n".join(sections[1:])

            return structured

        return prompt

    def optimize_prompt(self, request: PromptOptimizationRequest) -> OptimizedPrompt:
        """Otimiza o prompt aplicando técnicas apropriadas"""
        original = request.prompt
        task_type = self.identify_task_type(original)
        techniques_used = []

        # Contexto para as técnicas
        context = {
            "target_audience": request.target_audience,
            "desired_length": request.desired_length,
            "tone": request.tone,
            "task_type": task_type
        }

        # Aplica técnicas em ordem
        optimized = original

        # 1. Clareza
        optimized = self._apply_clarity(optimized, context)
        if optimized != original:
            techniques_used.append("Clareza e Especificidade")

        # 2. Persona
        temp = optimized
        optimized = self._apply_persona(optimized, task_type)
        if optimized != temp:
            techniques_used.append("Atribuição de Papel (Persona)")

        # 3. Contexto
        temp = optimized
        optimized = self._apply_context(optimized, context)
        if optimized != temp:
            techniques_used.append("Contexto Detalhado")

        # 4. Chain-of-Thought para tarefas complexas
        temp = optimized
        optimized = self._apply_chain_of_thought(optimized, task_type)
        if optimized != temp:
            techniques_used.append("Chain-of-Thought (CoT)")

        # 5. Few-shot quando apropriado
        temp = optimized
        optimized = self._apply_few_shot(optimized, task_type)
        if optimized != temp:
            techniques_used.append("Few-Shot Examples")

        # 6. Formato
        temp = optimized
        optimized = self._apply_format_specification(optimized, context)
        if optimized != temp:
            techniques_used.append("Especificação de Formato")

        # 7. Delimitadores
        temp = optimized
        optimized = self._apply_delimiters(optimized)
        if optimized != temp:
            techniques_used.append("Delimitadores Estruturais")

        # Sugestões adicionais
        suggestions = self._generate_suggestions(task_type, original)

        return OptimizedPrompt(
            original_prompt=original,
            optimized_prompt=optimized,
            techniques_applied=techniques_used,
            task_type=task_type.value,
            suggestions=suggestions
        )

    def _generate_suggestions(self, task_type: TaskType, prompt: str) -> List[str]:
        """Gera sugestões específicas para melhorar o prompt"""
        suggestions = []

        # Sugestões gerais
        if len(prompt) < 20:
            suggestions.append(
                "Considere adicionar mais detalhes sobre o que você deseja")

        if "?" not in prompt and task_type == TaskType.QUESTION_ANSWERING:
            suggestions.append("Formule sua pergunta de forma clara com '?'")

        # Sugestões específicas por tipo
        task_suggestions = {
            TaskType.CODE_GENERATION: [
                "Especifique a linguagem de programação desejada",
                "Mencione requisitos de performance ou restrições",
                "Indique se precisa de comentários no código"
            ],
            TaskType.IMAGE_GENERATION: [
                "Descreva o estilo artístico desejado",
                "Especifique cores, iluminação e composição",
                "Adicione detalhes sobre o ambiente/cenário"
            ],
            TaskType.ANALYSIS: [
                "Defina os critérios de análise",
                "Especifique o nível de profundidade desejado",
                "Indique se precisa de recomendações"
            ]
        }

        if task_type in task_suggestions:
            suggestions.extend(task_suggestions[task_type])

        return suggestions[:3]  # Retorna no máximo 3 sugestões


# Instancia o engenheiro de prompts
engineer = PromptEngineer()


@mcp.tool()
async def optimize_prompt(
    prompt: str,
    task_type: Optional[str] = None,
    target_audience: Optional[str] = None,
    desired_length: Optional[str] = None,
    tone: Optional[str] = None
) -> Dict[str, Any]:
    """
    Otimiza um prompt aplicando as melhores práticas de engenharia de prompts

    Args:
        prompt: O prompt original a ser otimizado
        task_type: Tipo de tarefa (opcional, será detectado automaticamente)
        target_audience: Público-alvo da resposta
        desired_length: Extensão desejada da resposta
        tone: Tom desejado (formal, informal, técnico, etc.)

    Returns:
        Dicionário com o prompt otimizado e informações sobre as técnicas aplicadas
    """
    request = PromptOptimizationRequest(
        prompt=prompt,
        task_type=task_type,
        target_audience=target_audience,
        desired_length=desired_length,
        tone=tone
    )

    result = engineer.optimize_prompt(request)

    return {
        "original_prompt": result.original_prompt,
        "optimized_prompt": result.optimized_prompt,
        "techniques_applied": result.techniques_applied,
        "task_type": result.task_type,
        "suggestions": result.suggestions
    }


@mcp.tool()
async def analyze_prompt(prompt: str) -> Dict[str, Any]:
    """
    Analisa um prompt e fornece feedback sobre sua qualidade

    Args:
        prompt: O prompt a ser analisado

    Returns:
        Análise detalhada do prompt com pontuação e recomendações
    """
    analysis = {
        "prompt": prompt,
        "length": len(prompt),
        "task_type": engineer.identify_task_type(prompt).value,
        "quality_score": 0,
        "strengths": [],
        "weaknesses": [],
        "recommendations": []
    }

    # Análise de qualidade
    score = 0

    # Clareza (0-25 pontos)
    if len(prompt) > 20:
        score += 10
        analysis["strengths"].append("Comprimento adequado")
    else:
        analysis["weaknesses"].append("Prompt muito curto")

    if not any(word in prompt.lower() for word in ["isso", "aquilo", "coisa"]):
        score += 15
        analysis["strengths"].append("Linguagem específica")
    else:
        analysis["weaknesses"].append("Contém termos vagos")

    # Contexto (0-25 pontos)
    context_indicators = ["para", "quando", "onde", "como", "por que"]
    if any(indicator in prompt.lower() for indicator in context_indicators):
        score += 25
        analysis["strengths"].append("Inclui contexto")
    else:
        analysis["weaknesses"].append("Falta contexto")
        analysis["recommendations"].append(
            "Adicione contexto sobre quando, onde ou como")

    # Objetivo claro (0-25 pontos)
    action_verbs = ["crie", "analise", "explique",
                    "desenvolva", "resuma", "traduza"]
    if any(verb in prompt.lower() for verb in action_verbs):
        score += 25
        analysis["strengths"].append("Objetivo claro")
    else:
        analysis["weaknesses"].append("Objetivo pouco claro")
        analysis["recommendations"].append(
            "Use verbos de ação para clarificar o objetivo")

    # Estrutura (0-25 pontos)
    if "?" in prompt or "\n" in prompt:
        score += 25
        analysis["strengths"].append("Bem estruturado")
    else:
        analysis["recommendations"].append(
            "Considere usar pontuação ou quebras de linha para estruturar melhor")

    analysis["quality_score"] = score

    # Recomendações baseadas na pontuação
    if score < 50:
        analysis["recommendations"].insert(
            0, "Este prompt precisa de melhorias significativas")
    elif score < 75:
        analysis["recommendations"].insert(
            0, "Prompt razoável, mas pode ser melhorado")
    else:
        analysis["recommendations"].insert(0, "Prompt bem estruturado!")

    return analysis


@mcp.tool()
async def suggest_framework(task_description: str) -> Dict[str, Any]:
    """
    Sugere o melhor framework de prompt para uma tarefa específica

    Args:
        task_description: Descrição da tarefa a ser realizada

    Returns:
        Framework recomendado com exemplo de aplicação
    """
    task_type = engineer.identify_task_type(task_description)

    # Mapeamento de tipos de tarefa para frameworks
    framework_mapping = {
        TaskType.TEXT_GENERATION: "TRACE",
        TaskType.CODE_GENERATION: "RACE",
        TaskType.IMAGE_GENERATION: "CRISPE",
        TaskType.ANALYSIS: "COAST",
        TaskType.CREATIVE: "CRISPE",
        TaskType.PROBLEM_SOLVING: "CORE",
        TaskType.QUESTION_ANSWERING: "RACE"
    }

    recommended_framework = framework_mapping.get(task_type, "RACE")
    framework_components = engineer.frameworks[recommended_framework]

    # Cria exemplo baseado na tarefa
    examples = {
        "RACE": {
            "Role": "Você é um especialista no assunto",
            "Action": "Explique detalhadamente",
            "Context": "Para uma audiência técnica",
            "Expectation": "Resposta estruturada com exemplos"
        },
        "TRACE": {
            "Task": "Criar conteúdo informativo",
            "Request": "Desenvolva um texto completo",
            "Action": "Escreva de forma clara e envolvente",
            "Context": "Para profissionais da área",
            "Example": "Similar a artigos de revistas especializadas"
        },
        "CRISPE": {
            "Capacity/Role": "Criador de conteúdo inovador",
            "Insight": "Compreenda as tendências atuais",
            "Statement": "Crie algo único e memorável",
            "Personality": "Tom criativo e inspirador",
            "Experiment": "Explore abordagens não convencionais"
        }
    }

    example = examples.get(recommended_framework, {})

    return {
        "task_type": task_type.value,
        "recommended_framework": recommended_framework,
        "framework_components": framework_components,
        "example_application": example,
        "usage_tip": f"Use o framework {recommended_framework} estruturando seu prompt com cada componente"
    }


@mcp.tool()
async def apply_advanced_technique(
    prompt: str,
    technique: str = "chain_of_thought"
) -> Dict[str, Any]:
    """
    Aplica técnicas avançadas de raciocínio ao prompt

    Args:
        prompt: O prompt original
        technique: Técnica a aplicar (chain_of_thought, self_consistency, react, tree_of_thoughts)

    Returns:
        Prompt modificado com a técnica avançada aplicada
    """
    techniques_map = {
        "chain_of_thought": {
            "name": "Chain-of-Thought (CoT)",
            "suffix": "\n\nVamos pensar passo a passo:\n1. Primeiro, vamos entender o problema\n2. Depois, analisar as possíveis abordagens\n3. Por fim, chegar a uma solução detalhada",
            "description": "Guia o modelo através de etapas de raciocínio"
        },
        "self_consistency": {
            "name": "Self-Consistency",
            "suffix": "\n\nGere 3 abordagens diferentes para esta questão e depois sintetize a melhor resposta com base nas abordagens geradas.",
            "description": "Múltiplos caminhos de raciocínio para maior confiabilidade"
        },
        "react": {
            "name": "ReAct (Reason + Act)",
            "suffix": "\n\nPensamento: Analise o que precisa ser feito\nAção: Determine os passos necessários\nObservação: Avalie os resultados de cada passo\nRepita até chegar à solução completa.",
            "description": "Combina raciocínio com ações iterativas"
        },
        "tree_of_thoughts": {
            "name": "Tree of Thoughts (ToT)",
            "suffix": "\n\nExplore múltiplas possibilidades:\n- Caminho A: [desenvolva esta abordagem]\n- Caminho B: [desenvolva alternativa]\n- Caminho C: [explore outra opção]\nAvalie qual caminho é mais promissor e desenvolva-o completamente.",
            "description": "Exploração de múltiplos caminhos de pensamento"
        }
    }

    if technique not in techniques_map:
        technique = "chain_of_thought"

    tech_info = techniques_map[technique]
    enhanced_prompt = prompt + tech_info["suffix"]

    return {
        "original_prompt": prompt,
        "enhanced_prompt": enhanced_prompt,
        "technique_applied": tech_info["name"],
        "technique_description": tech_info["description"],
        "best_for": "Problemas complexos que requerem raciocínio estruturado"
    }


@mcp.tool()
async def check_bias(prompt: str) -> Dict[str, Any]:
    """
    Verifica potenciais vieses no prompt e sugere mitigações

    Args:
        prompt: O prompt a ser verificado

    Returns:
        Análise de vieses com sugestões de mitigação
    """
    biases_found = []
    mitigations = []

    # Verificação de vieses de gênero
    gender_terms = {
        "masculino": ["ele", "homem", "masculino", "senhor"],
        "feminino": ["ela", "mulher", "feminino", "senhora"]
    }

    gender_bias = {"masculino": 0, "feminino": 0}
    for gender, terms in gender_terms.items():
        for term in terms:
            if term in prompt.lower():
                gender_bias[gender] += 1

    if gender_bias["masculino"] > 0 and gender_bias["feminino"] == 0:
        biases_found.append(
            "Possível viés de gênero (apenas termos masculinos)")
        mitigations.append(
            "Use linguagem neutra em gênero ou inclua exemplos diversos")

    # Verificação de estereótipos profissionais
    stereotypes = {
        "engenheiro": "profissional de engenharia",
        "enfermeira": "profissional de enfermagem",
        "secretária": "profissional administrativo"
    }

    for stereotype, neutral in stereotypes.items():
        if stereotype in prompt.lower():
            biases_found.append(
                f"Termo com potencial estereótipo: '{stereotype}'")
            mitigations.append(
                f"Considere usar '{neutral}' para maior neutralidade")

    # Verificação de premissas culturais
    if any(word in prompt.lower() for word in ["normal", "padrão", "comum"]):
        biases_found.append("Possíveis premissas culturais não especificadas")
        mitigations.append(
            "Especifique o contexto cultural ou use termos mais inclusivos")

    # Sugestão de prompt para desafiar vieses
    bias_challenger = "\n\nAo responder, considere múltiplas perspectivas e evite fazer suposições baseadas em estereótipos."

    return {
        "prompt": prompt,
        "biases_detected": biases_found if biases_found else ["Nenhum viés óbvio detectado"],
        "mitigation_suggestions": mitigations,
        "bias_score": len(biases_found),
        "improved_prompt": prompt + bias_challenger if biases_found else prompt,
        "general_tips": [
            "Use linguagem inclusiva",
            "Evite generalizações",
            "Considere múltiplas perspectivas",
            "Especifique contextos quando relevante"
        ]
    }

# Configuração e inicialização
if __name__ == "__main__":
    import asyncio

    # Exemplo de uso
    async def test_server():
        # Teste de otimização
        result = await optimize_prompt(
            prompt="explique isso",
            target_audience="estudantes universitários",
            tone="didático"
        )
        print("Otimização:", result)

        # Teste de análise
        analysis = await analyze_prompt("Como funciona a fotossíntese?")
        print("\nAnálise:", analysis)

        # Teste de framework
        framework = await suggest_framework("Preciso criar um relatório de vendas")
        print("\nFramework sugerido:", framework)

    # Inicia o servidor
    print("Servidor MCP de Engenharia de Prompts iniciado!")
    print("Ferramentas disponíveis:")
    print("- optimize_prompt: Otimiza prompts automaticamente")
    print("- analyze_prompt: Analisa qualidade de prompts")
    print("- suggest_framework: Sugere frameworks apropriados")
    print("- apply_advanced_technique: Aplica técnicas avançadas")
    print("- check_bias: Verifica e mitiga vieses")

    # Para testes locais
    # asyncio.run(test_server())

    # Inicia o servidor MCP
    mcp.run()
