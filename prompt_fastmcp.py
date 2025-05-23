from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
import json
import re
from fastmcp import FastMCP

# Initialize FastMCP
mcp = FastMCP("Prompt Optimizer")

class PromptType(Enum):
    CHAIN_OF_THOUGHT = "chain_of_thought"
    FEW_SHOT = "few_shot"
    ROLE_PROMPTING = "role_prompting"
    CLEAR_CONSTRAINTS = "clear_constraints"
    SELF_CONSISTENCY = "self_consistency"
    TREE_OF_THOUGHTS = "tree_of_thoughts"
    STEP_BY_STEP = "step_by_step"
    CONTEXT_AWARE = "context_aware"

# ... existing code ...

@mcp.tool()
def analyze_prompt(prompt: str) -> Dict[str, Any]:
    """
    Analisa um prompt e fornece feedback detalhado sobre sua qualidade e eficácia.
    
    Args:
        prompt: O prompt a ser analisado
        
    Returns:
        Análise detalhada incluindo pontuação, pontos fortes, fracos e sugestões
    """
    optimizer = PromptOptimizerMCPServer()
    return optimizer.analyze_prompt_tool(prompt)

@mcp.tool()
def optimize_prompt(prompt: str, target_type: Optional[str] = None) -> Dict[str, Any]:
    """
    Otimiza um prompt aplicando técnicas de melhoria baseadas em análise.
    
    Args:
        prompt: O prompt original a ser otimizado
        target_type: Tipo específico de otimização (opcional)
        
    Returns:
        Prompt otimizado com explicações das melhorias aplicadas
    """
    optimizer = PromptOptimizerMCPServer()
    return optimizer.optimize_prompt_tool(prompt, target_type)

@mcp.tool()
def generate_prompt(task_description: str, prompt_type: str) -> Dict[str, Any]:
    """
    Gera um prompt otimizado baseado na descrição da tarefa e tipo especificado.
    
    Args:
        task_description: Descrição da tarefa para a qual o prompt será criado
        prompt_type: Tipo de técnica de prompt a ser aplicada
        
    Returns:
        Prompt gerado com estrutura otimizada
    """
    optimizer = PromptOptimizerMCPServer()
    return optimizer.generate_prompt_tool(task_description, prompt_type)

@mcp.tool()
def get_technique(technique_name: str) -> Dict[str, Any]:
    """
    Retorna informações detalhadas sobre uma técnica específica de otimização de prompts.
    
    Args:
        technique_name: Nome da técnica (ex: 'chain_of_thought', 'few_shot')
        
    Returns:
        Informações detalhadas sobre a técnica incluindo descrição, exemplo e uso
    """
    optimizer = PromptOptimizerMCPServer()
    return optimizer.get_technique_tool(technique_name)

@mcp.tool()
def suggest_improvements(prompt: str) -> Dict[str, Any]:
    """
    Sugere melhorias específicas para um prompt baseado em análise detalhada.
    
    Args:
        prompt: O prompt para o qual sugestões serão fornecidas
        
    Returns:
        Lista de sugestões específicas com explicações e exemplos
    """
    optimizer = PromptOptimizerMCPServer()
    return optimizer.suggest_improvements_tool(prompt)

@mcp.prompt()
def prompt_optimization_guide() -> str:
    """
    Guia completo de otimização de prompts com técnicas e melhores práticas.
    
    Returns:
        Guia detalhado em português brasileiro
    """
    return """
# Guia de Otimização de Prompts

## Técnicas Principais

### 1. Chain of Thought (Cadeia de Pensamento)
Encoraje o modelo a mostrar seu raciocínio passo a passo.
**Exemplo:** "Resolva este problema mostrando cada etapa do seu raciocínio:"

### 2. Few-Shot Learning (Aprendizado com Poucos Exemplos)
Forneça exemplos específicos do formato de resposta desejado.
**Exemplo:** "Aqui estão alguns exemplos: [exemplos]. Agora faça o mesmo para:"

### 3. Role Prompting (Definição de Papel)
Defina claramente o papel que o modelo deve assumir.
**Exemplo:** "Você é um especialista em [área]. Como tal, analise:"

### 4. Restrições Claras
Especifique limitações e requisitos explicitamente.
**Exemplo:** "Responda em no máximo 100 palavras, focando apenas em:"

## Melhores Práticas

1. **Seja Específico**: Use linguagem precisa e evite ambiguidades
2. **Estruture Bem**: Organize o prompt em seções claras
3. **Forneça Contexto**: Inclua informações relevantes de fundo
4. **Teste e Itere**: Refine baseado nos resultados obtidos
5. **Use Exemplos**: Demonstre o formato de saída desejado

## Critérios de Qualidade

- **Clareza**: O prompt é fácil de entender?
- **Completude**: Todas as informações necessárias estão incluídas?
- **Estrutura**: O prompt está bem organizado?
- **Especificidade**: Os requisitos são precisos?
- **Eficiência**: O prompt é conciso mas completo?
"""

@mcp.prompt()
def prompt_templates() -> str:
    """
    Templates de prompts otimizados para diferentes tipos de tarefas.
    
    Returns:
        Coleção de templates em português brasileiro
    """
    return """
# Templates de Prompts Otimizados

## Template para Análise