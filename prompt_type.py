#!/usr/bin/env python3
"""
Servidor MCP de Otimização de Prompts
Fornece técnicas, templates e ferramentas para criar prompts eficazes para LLMs
"""

import json
import asyncio
import re
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime
from enum import Enum

from mcp.server.models import InitializationOptions
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Resource, Tool, TextContent, ServerCapabilities


class PromptType(Enum):
    """Tipos de prompts suportados"""
    INSTRUCTION = "instruction"
    CREATIVE = "creative"
    ANALYSIS = "analysis"
    CODE = "code"
    CHAT = "chat"
    REASONING = "reasoning"
    EXTRACTION = "extraction"
    SUMMARIZATION = "summarization"
    TRANSLATION = "translation"
    ROLE_PLAY = "role_play"


# Base de conhecimento sobre otimização de prompts
PROMPT_OPTIMIZATION_KB = {
    "techniques": {
        "chain_of_thought": {
            "name": "Chain of Thought (CoT)",
            "description": "Guia o modelo a pensar passo a passo antes de responder",
            "when_to_use": "Problemas complexos de raciocínio, matemática, lógica",
            "template": """Let's approach this step-by-step:

1. First, I'll identify the key information
2. Then, I'll break down the problem
3. Next, I'll work through each part
4. Finally, I'll synthesize the solution

[Your specific question here]

Let me think through this systematically...""",
            "example": """Question: If a train travels 120 miles in 2 hours, and then 180 miles in 3 hours, what is its average speed for the entire journey?

Let's solve this step-by-step:
1. First, let me identify what we know:
   - First segment: 120 miles in 2 hours
   - Second segment: 180 miles in 3 hours

2. Calculate total distance:
   - Total distance = 120 + 180 = 300 miles

3. Calculate total time:
   - Total time = 2 + 3 = 5 hours

4. Calculate average speed:
   - Average speed = Total distance / Total time
   - Average speed = 300 / 5 = 60 mph

Therefore, the average speed for the entire journey is 60 mph."""
        },
        "few_shot": {
            "name": "Few-Shot Learning",
            "description": "Fornece exemplos do formato desejado antes da tarefa real",
            "when_to_use": "Tarefas com formato específico, classificação, extração de dados",
            "template": """I'll help you with [task]. Here are some examples of what I'm looking for:

Example 1:
Input: [example input 1]
Output: [example output 1]

Example 2:
Input: [example input 2]
Output: [example output 2]

Example 3:
Input: [example input 3]
Output: [example output 3]

Now, for your input:
Input: [actual input]
Output:""",
            "example": """I'll help you classify customer feedback sentiment. Here are some examples:

Example 1:
Input: "This product exceeded my expectations! Fast shipping and great quality."
Output: Positive (confidence: 95%)

Example 2:
Input: "The item broke after one week. Very disappointed."
Output: Negative (confidence: 90%)

Example 3:
Input: "It works okay, nothing special but does the job."
Output: Neutral (confidence: 85%)

Now, for your input:
Input: "Amazing service! Will definitely order again."
Output: Positive (confidence: 98%)"""
        },
        "role_prompting": {
            "name": "Role/Persona Prompting",
            "description": "Atribui um papel específico ou expertise ao modelo",
            "when_to_use": "Quando precisar de perspectiva especializada ou tom específico",
            "template": """You are a [specific role/expert] with [specific characteristics/experience].

Your expertise includes:
- [Expertise area 1]
- [Expertise area 2]
- [Expertise area 3]

Your communication style is [describe style].

Now, from this perspective, please [specific task].""",
            "example": """You are a senior software architect with 15 years of experience in distributed systems and cloud architecture.

Your expertise includes:
- Microservices design patterns
- AWS/Azure/GCP cloud platforms
- System scalability and performance optimization
- DevOps and CI/CD best practices

Your communication style is technical but accessible, using diagrams and real-world examples.

Now, from this perspective, please review this system design and suggest improvements for scalability."""
        },
        "structured_output": {
            "name": "Structured Output Format",
            "description": "Define formato exato esperado para a resposta",
            "when_to_use": "Quando precisar de dados estruturados, JSON, listas específicas",
            "template": """Please provide your response in the following format:

```[format type]
{
  "field1": "description of what goes here",
  "field2": "description of what goes here",
  "field3": [
    "item format description"
  ],
  "field4": {
    "subfield1": "description",
    "subfield2": "description"
  }
}
```

Ensure all fields are filled and follow the exact structure.""",
            "example": """Analyze this product review and provide a structured summary:

```json
{
  "overall_sentiment": "positive/negative/neutral",
  "rating_predicted": "1-5 scale",
  "key_points": {
    "pros": ["list of positive aspects mentioned"],
    "cons": ["list of negative aspects mentioned"]
  },
  "product_aspects": {
    "quality": "rating/comment if mentioned",
    "value": "rating/comment if mentioned",
    "shipping": "rating/comment if mentioned"
  },
  "would_recommend": "yes/no/unclear"
}
```"""
        },
        "prompt_chaining": {
            "name": "Prompt Chaining",
            "description": "Quebra tarefas complexas em múltiplos prompts sequenciais",
            "when_to_use": "Tarefas muito complexas, workflows multi-etapas",
            "template": """This task will be completed in multiple steps:

Step 1: [First sub-task]
[Complete step 1]

Step 2: [Second sub-task using output from step 1]
[Complete step 2]

Step 3: [Final synthesis]
[Complete final step]""",
            "example": """Let's write a technical blog post about microservices:

Step 1: Create an outline
- Introduction to microservices
- Benefits and challenges
- Best practices
- Real-world example
- Conclusion

Step 2: Expand the introduction section
[Detailed introduction paragraph about microservices...]

Step 3: Develop the benefits and challenges section
[Detailed content about pros and cons...]

[Continue with remaining sections...]"""
        },
        "constraints_specification": {
            "name": "Clear Constraints",
            "description": "Especifica limitações e requisitos claramente",
            "when_to_use": "Quando houver requisitos específicos de formato, tamanho, estilo",
            "template": """Please follow these constraints:
- Length: [specify word/character count]
- Style: [formal/informal/technical/conversational]
- Include: [must-have elements]
- Exclude: [what to avoid]
- Format: [specific formatting requirements]
- Target audience: [who will read/use this]""",
            "example": """Write a product description with these constraints:
- Length: 150-200 words
- Style: Conversational but professional
- Include: Key features, benefits, and use cases
- Exclude: Technical jargon, pricing information
- Format: 2-3 paragraphs with a compelling opening
- Target audience: Small business owners (non-technical)"""
        },
        "self_consistency": {
            "name": "Self-Consistency Check",
            "description": "Pede ao modelo para verificar e melhorar sua própria resposta",
            "when_to_use": "Tarefas críticas que requerem alta precisão",
            "template": """[Initial task]

After providing your answer, please:
1. Review your response for accuracy
2. Check for any inconsistencies or errors
3. Verify that all requirements were met
4. Provide a confidence score (0-100%)
5. If needed, provide a corrected version""",
            "example": """Calculate the compound interest for a $10,000 investment at 5% annual rate for 3 years.

[Initial calculation...]

Self-check:
1. Formula used: A = P(1 + r)^t
2. Values: P=10,000, r=0.05, t=3
3. Calculation: 10,000 × (1.05)³ = 10,000 × 1.157625 = $11,576.25
4. Confidence: 100%
5. The calculation is correct."""
        },
        "tree_of_thoughts": {
            "name": "Tree of Thoughts (ToT)",
            "description": "Explora múltiplas linhas de raciocínio antes de escolher a melhor",
            "when_to_use": "Problemas complexos com múltiplas soluções possíveis",
            "template": """I'll explore different approaches to this problem:

Approach 1: [Description]
- Pros: [advantages]
- Cons: [disadvantages]
- Viability: [score/assessment]

Approach 2: [Description]
- Pros: [advantages]
- Cons: [disadvantages]
- Viability: [score/assessment]

Approach 3: [Description]
- Pros: [advantages]
- Cons: [disadvantages]
- Viability: [score/assessment]

Best approach: [Choose and explain why]
Implementation: [Detailed solution using best approach]""",
            "example": """How can we reduce cloud infrastructure costs by 30%?

Approach 1: Right-sizing resources
- Pros: Quick wins, no architecture changes
- Cons: Limited savings potential (10-15%)
- Viability: High - easy to implement

Approach 2: Serverless migration
- Pros: Pay-per-use, auto-scaling, 40-50% savings
- Cons: Major refactoring needed, learning curve
- Viability: Medium - requires significant effort

Approach 3: Multi-cloud strategy
- Pros: Best prices, avoid vendor lock-in
- Cons: Complex management, security challenges
- Viability: Low - high complexity

Best approach: Combination of 1 and 2
Start with right-sizing for immediate savings, then gradually migrate suitable workloads to serverless."""
        }
    },
    "templates": {
        "instruction": {
            "basic": """Task: {task_description}

Requirements:
- {requirement_1}
- {requirement_2}
- {requirement_3}

Please provide a clear and comprehensive response.""",
            "detailed": """Objective: {main_objective}

Context: {background_information}

Specific Requirements:
1. {detailed_requirement_1}
2. {detailed_requirement_2}
3. {detailed_requirement_3}

Constraints:
- {constraint_1}
- {constraint_2}

Expected Output Format:
{output_format_description}

Please ensure your response is {tone/style} and suitable for {target_audience}."""
        },
        "analysis": {
            "data_analysis": """Analyze the following data and provide insights:

Data: {data_or_description}

Please include:
1. Key patterns and trends
2. Statistical summary (if applicable)
3. Anomalies or outliers
4. Actionable recommendations
5. Limitations of the analysis

Format your response with clear sections and use bullet points for readability.""",
            "swot": """Conduct a SWOT analysis for: {subject}

Context: {context}

Please structure your analysis as follows:

**Strengths** (Internal positive factors)
- [List key strengths]

**Weaknesses** (Internal negative factors)
- [List key weaknesses]

**Opportunities** (External positive factors)
- [List key opportunities]

**Threats** (External negative factors)
- [List key threats]

**Strategic Recommendations**
Based on this analysis, provide 3-5 actionable recommendations."""
        },
        "creative": {
            "storytelling": """Create a {genre} story with these elements:

Setting: {setting}
Main character: {character_description}
Conflict: {central_conflict}
Tone: {desired_tone}

Additional requirements:
- Length: {word_count} words
- Include: {must_include_elements}
- Avoid: {elements_to_avoid}

Begin with a compelling hook and ensure a satisfying resolution.""",
            "brainstorming": """Generate creative ideas for: {topic}

Context: {background}
Constraints: {limitations}
Target audience: {audience}

Please provide:
1. 10-15 diverse ideas
2. Brief description for each (2-3 sentences)
3. Pros and cons for top 3 ideas
4. Implementation difficulty (Easy/Medium/Hard)
5. Potential impact (Low/Medium/High)

Think outside the box and consider unconventional approaches."""
        },
        "code": {
            "implementation": """Implement a {language} solution for:

Problem: {problem_description}

Requirements:
- {functional_requirement_1}
- {functional_requirement_2}
- Performance: {performance_requirement}
- Edge cases to handle: {edge_cases}

Please provide:
1. Clean, well-commented code
2. Time and space complexity analysis
3. Example usage
4. Unit tests for main functionality
5. Potential optimizations

Follow {language} best practices and {style_guide} conventions.""",
            "review": """Review the following code:

```{language}
{code_to_review}
```

Please analyze:
1. **Functionality**: Does it work correctly?
2. **Performance**: Time/space complexity and bottlenecks
3. **Readability**: Code clarity and documentation
4. **Maintainability**: Structure and design patterns
5. **Security**: Potential vulnerabilities
6. **Best Practices**: Language-specific conventions

Provide specific suggestions for improvement with code examples."""
        }
    },
    "best_practices": {
        "clarity": [
            "Be specific about the task - avoid ambiguous language",
            "Define technical terms if using domain-specific language",
            "Use concrete examples rather than abstract descriptions",
            "Break complex instructions into numbered steps",
            "Specify the format, length, and style of desired output"
        ],
        "context": [
            "Provide relevant background information",
            "Explain the purpose and end goal of the task",
            "Mention any constraints or limitations upfront",
            "Include examples of good and bad outputs if possible",
            "Specify the target audience for the output"
        ],
        "structure": [
            "Use clear headers and sections",
            "Put the main instruction first, details second",
            "Use bullet points or numbered lists for multiple requirements",
            "Separate context from instructions clearly",
            "End with a clear call to action"
        ],
        "iteration": [
            "Start with a simple version and refine",
            "Test prompts with edge cases",
            "Be prepared to clarify based on initial outputs",
            "Save successful prompts as templates",
            "Version control your prompts for complex tasks"
        ],
        "avoid": [
            "Avoid negative instructions (say what TO do, not what NOT to do)",
            "Don't overload with too many requirements at once",
            "Avoid contradictory instructions",
            "Don't assume prior knowledge without stating it",
            "Avoid overly complex sentence structures"
        ]
    },
    "scoring_criteria": {
        "clarity": {
            "weight": 0.25,
            "factors": [
                "Specific task definition",
                "Clear success criteria",
                "Unambiguous language",
                "Logical flow"
            ]
        },
        "completeness": {
            "weight": 0.25,
            "factors": [
                "All necessary context provided",
                "Requirements fully specified",
                "Output format defined",
                "Edge cases considered"
            ]
        },
        "structure": {
            "weight": 0.20,
            "factors": [
                "Well-organized sections",
                "Appropriate use of formatting",
                "Logical progression",
                "Easy to scan and understand"
            ]
        },
        "specificity": {
            "weight": 0.20,
            "factors": [
                "Concrete rather than abstract",
                "Measurable success criteria",
                "Examples provided where helpful",
                "Technical precision"
            ]
        },
        "efficiency": {
            "weight": 0.10,
            "factors": [
                "Concise without losing clarity",
                "No redundant instructions",
                "Appropriate level of detail",
                "Direct and to the point"
            ]
        }
    }
}


class PromptOptimizerMCPServer:
    def __init__(self):
        self.server = Server("prompt-optimizer-server")
        self.setup_handlers()
    
    def analyze_prompt_quality(self, prompt: str) -> Dict[str, Any]:
        """Analisa a qualidade de um prompt e retorna score com feedback"""
        scores = {
            "clarity": 0,
            "completeness": 0,
            "structure": 0,
            "specificity": 0,
            "efficiency": 0
        }
        
        feedback = {
            "strengths": [],
            "improvements": [],
            "suggestions": []
        }
        
        # Análise de clareza
        if len(prompt.split()) > 10:
            scores["clarity"] += 0.5
        if "?" in prompt or prompt.strip().endswith(":"):
            scores["clarity"] += 0.3
        if any(word in prompt.lower() for word in ["please", "help", "need", "want"]):
            scores["clarity"] += 0.2
            
        # Análise de completude
        if len(prompt) > 50:
            scores["completeness"] += 0.3
        if any(word in prompt.lower() for word in ["context", "background", "given", "assuming"]):
            scores["completeness"] += 0.3
        if any(word in prompt.lower() for word in ["format", "style", "output", "should"]):
            scores["completeness"] += 0.4
            
        # Análise de estrutura
        lines = prompt.strip().split('\n')
        if len(lines) > 1:
            scores["structure"] += 0.4
        if any(char in prompt for char in ['-', '•', '1.', '2.', '*']):
            scores["structure"] += 0.3
        if prompt.count(':') > 1:
            scores["structure"] += 0.3
            
        # Análise de especificidade
        specific_terms = ["specifically", "exactly", "must", "should", "require", "need"]
        specificity_count = sum(1 for term in specific_terms if term in prompt.lower())
        scores["specificity"] += min(specificity_count * 0.2, 0.8)
        if re.search(r'\d+', prompt):  # Contains numbers
            scores["specificity"] += 0.2
            
        # Análise de eficiência
        word_count = len(prompt.split())
        if 20 <= word_count <= 200:
            scores["efficiency"] = 0.8
        elif word_count < 20:
            scores["efficiency"] = 0.4
            feedback["improvements"].append("Prompt muito curto - adicione mais contexto")
        else:
            scores["efficiency"] = 0.6
            feedback["improvements"].append("Prompt muito longo - considere dividir em partes")
            
        # Calcular score total
        total_score = sum(
            scores[criterion] * PROMPT_OPTIMIZATION_KB["scoring_criteria"][criterion]["weight"]
            for criterion in scores
        )
        
        # Gerar feedback
        if total_score >= 0.8:
            feedback["strengths"].append("Prompt bem estruturado e claro")
        elif total_score >= 0.6:
            feedback["strengths"].append("Prompt razoável com espaço para melhorias")
        else:
            feedback["improvements"].append("Prompt precisa de melhorias significativas")
            
        # Sugestões específicas
        if scores["clarity"] < 0.5:
            feedback["suggestions"].append("Seja mais específico sobre o que você precisa")
        if scores["completeness"] < 0.5:
            feedback["suggestions"].append("Adicione contexto e requisitos específicos")
        if scores["structure"] < 0.5:
            feedback["suggestions"].append("Organize em seções com bullet points ou numeração")
            
        return {
            "total_score": round(total_score * 100, 1),
            "individual_scores": {k: round(v * 100, 1) for k, v in scores.items()},
            "feedback": feedback
        }
    
    def optimize_prompt(self, original_prompt: str, prompt_type: str = None) -> Dict[str, Any]:
        """Otimiza um prompt aplicando melhores práticas"""
        # Identificar tipo de prompt se não especificado
        if not prompt_type:
            prompt_type = self.identify_prompt_type(original_prompt)
        
        # Análise inicial
        original_analysis = self.analyze_prompt_quality(original_prompt)
        
        # Aplicar otimizações
        optimized = original_prompt
        techniques_applied = []
        
        # Adicionar estrutura se necessário
        if original_analysis["individual_scores"]["structure"] < 50:
            optimized = self.add_structure(optimized, prompt_type)
            techniques_applied.append("Added clear structure with sections")
        
        # Adicionar contexto se necessário
        if original_analysis["individual_scores"]["completeness"] < 50:
            optimized = self.add_context_template(optimized, prompt_type)
            techniques_applied.append("Added context and requirements sections")
        
        # Adicionar especificidade
        if original_analysis["individual_scores"]["specificity"] < 50:
            optimized = self.add_specificity(optimized, prompt_type)
            techniques_applied.append("Added specific requirements and constraints")
        
        # Análise do prompt otimizado
        optimized_analysis = self.analyze_prompt_quality(optimized)
        
        return {
            "original_prompt": original_prompt,
            "optimized_prompt": optimized,
            "prompt_type": prompt_type,
            "techniques_applied": techniques_applied,
            "original_score": original_analysis["total_score"],
            "optimized_score": optimized_analysis["total_score"],
            "improvement": round(optimized_analysis["total_score"] - original_analysis["total_score"], 1),
            "detailed_feedback": optimized_analysis["feedback"]
        }
    
    def identify_prompt_type(self, prompt: str) -> str:
        """Identifica o tipo de prompt baseado no conteúdo"""
        prompt_lower = prompt.lower()
        
        # Keywords para cada tipo
        type_keywords = {
            "code": ["code", "implement", "function", "program", "script", "debug", "algorithm"],
            "analysis": ["analyze", "evaluate", "assess", "review", "examine", "investigate"],
            "creative": ["create", "write", "story", "imagine", "design", "invent", "poem"],
            "instruction": ["how to", "explain", "teach", "guide", "steps", "process"],
            "reasoning": ["why", "reason", "logic", "solve", "calculate", "prove"],
            "extraction": ["extract", "find", "identify", "list", "get", "retrieve"],
            "summarization": ["summarize", "summary", "brief", "overview", "key points"],
            "translation": ["translate", "convert", "language", "spanish", "french", "portuguese"]
        }
        
        # Contar matches para cada tipo
        type_scores = {}
        for ptype, keywords in type_keywords.items():
            score = sum(1 for keyword in keywords if keyword in prompt_lower)
            if score > 0:
                type_scores[ptype] = score
        
        # Retornar tipo com maior score
        if type_scores:
            return max(type_scores, key=type_scores.get)
        return "instruction"  # Default
    
    def add_structure(self, prompt: str, prompt_type: str) -> str:
        """Adiciona estrutura apropriada ao prompt"""
        if prompt_type == "code":
            return f"""Task: {prompt}

Requirements:
- Implement a clean, efficient solution
- Include error handling
- Add comments explaining the logic
- Follow best practices

Expected Output:
- Complete, working code
- Example usage
- Time/space complexity analysis"""
        
        elif prompt_type == "analysis":
            return f"""Analysis Request: {prompt}

Please provide:
1. Overview of the subject
2. Key findings and insights
3. Supporting evidence
4. Potential implications
5. Recommendations

Format: Use clear headings and bullet points for readability."""
        
        else:
            return f"""Objective: {prompt}

Please ensure your response:
- Addresses all aspects of the request
- Is well-organized and easy to follow
- Includes relevant examples where appropriate
- Provides actionable information"""
    
    def add_context_template(self, prompt: str, prompt_type: str) -> str:
        """Adiciona template de contexto ao prompt"""
        return f"""Context: [Providing detailed task description]

Specific Request: {prompt}

Additional Information:
- Target audience: [Specify if relevant]
- Desired outcome: [What success looks like]
- Constraints: [Any limitations or requirements]

Please provide a comprehensive response that addresses all aspects."""
    
    def add_specificity(self, prompt: str, prompt_type: str) -> str:
        """Adiciona especificidade ao prompt"""
        additions = [
            "\n\nPlease be specific and provide concrete examples.",
            "\nInclude step-by-step details where applicable.",
            "\nEnsure the response is actionable and practical."
        ]
        
        return prompt + "".join(additions)
    
    def generate_prompt_from_template(
        self, 
        task: str, 
        prompt_type: str,
        requirements: List[str] = None,
        context: str = None,
        constraints: List[str] = None
    ) -> str:
        """Gera um prompt otimizado usando templates"""
        template_category = prompt_type.lower()
        
        # Selecionar template base
        if template_category in ["instruction", "analysis", "creative", "code"]:
            templates = PROMPT_OPTIMIZATION_KB["templates"].get(template_category, {})
            template = templates.get("detailed", templates.get("basic", ""))
        else:
            # Template genérico
            template = PROMPT_OPTIMIZATION_KB["templates"]["instruction"]["detailed"]
        
        # Preencher template
        filled_template = template.format(
            task_description=task,
            main_objective=task,
            background_information=context or "General purpose task",
            requirement_1=requirements[0] if requirements else "Complete the task effectively",
            requirement_2=requirements[1] if requirements and len(requirements) > 1 else "Provide clear explanations",
            requirement_3=requirements[2] if requirements and len(requirements) > 2 else "Follow best practices",
            detailed_requirement_1=requirements[0] if requirements else "Address all aspects",
            detailed_requirement_2=requirements[1] if requirements and len(requirements) > 1 else "Be comprehensive",
            detailed_requirement_3=requirements[2] if requirements and len(requirements) > 2 else "Ensure quality",
            constraint_1=constraints[0] if constraints else "Professional tone",
            constraint_2=constraints[1] if constraints and len(constraints) > 1 else "Clear formatting",
            output_format_description="Well-structured response with clear sections",
            tone="professional and informative",
            target_audience="general professional audience"
        )
        
        return filled_template
    
    def setup_handlers(self):
        """Configura os handlers do servidor MCP"""
        
        @self.server.list_resources()
        async def handle_list_resources() -> List[Resource]:
            return [
                Resource(
                    uri="prompt://techniques",
                    name="Prompt Engineering Techniques",
                    description="Técnicas avançadas de prompt engineering",
                    mimeType="application/json"
                ),
                Resource(
                    uri="prompt://templates",
                    name="Prompt Templates",
                    description="Templates otimizados para diferentes tipos de tarefas",
                    mimeType="application/json"
                ),
                Resource(
                    uri="prompt://best-practices",
                    name="Best Practices Guide",
                    description="Guia de melhores práticas para prompts",
                    mimeType="application/json"
                ),
                Resource(
                    uri="prompt://examples",
                    name="Example Gallery",
                    description="Galeria de exemplos de prompts otimizados",
                    mimeType="application/json"
                )
            ]
        
        @self.server.read_resource()
        async def handle_read_resource(uri: str) -> str:
            if uri == "prompt://techniques":
                return json.dumps(PROMPT_OPTIMIZATION_KB["techniques"], indent=2)
            elif uri == "prompt://templates":
                return json.dumps(PROMPT_OPTIMIZATION_KB["templates"], indent=2)
            elif uri == "prompt://best-practices":
                return json.dumps(PROMPT_OPTIMIZATION_KB["best_practices"], indent=2)
            elif uri == "prompt://examples":
                # Compilar exemplos de cada técnica
                examples = {}
                for technique, data in PROMPT_OPTIMIZATION_KB["techniques"].items():
                    examples[technique] = {
                        "description": data["description"],
                        "example": data.get("example", "See template for structure")
                    }
                return json.dumps(examples, indent=2)
            else:
                raise ValueError(f"Resource not found: {uri}")
        
        @self.server.list_tools()
        async def handle_list_tools() -> List[Tool]:
            return [
                Tool(
                    name="analyze_prompt",
                    description="Analisa a qualidade de um prompt e fornece score detalhado",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "prompt": {
                                "type": "string",
                                "description": "O prompt a ser analisado"
                            }
                        },
                        "required": ["prompt"]
                    }
                ),
                Tool(
                    name="optimize_prompt",
                    description="Otimiza um prompt aplicando melhores práticas",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "prompt": {
                                "type": "string",
                                "description": "O prompt original a ser otimizado"
                            },
                            "prompt_type": {
                                "type": "string",
                                "enum": ["instruction", "creative", "analysis", "code", 
                                        "reasoning", "extraction", "summarization"],
                                "description": "Tipo do prompt (opcional - será detectado se não fornecido)"
                            }
                        },
                        "required": ["prompt"]
                    }
                ),
                Tool(
                    name="generate_prompt",
                    description="Gera um prompt otimizado a partir de requisitos",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "task": {
                                "type": "string",
                                "description": "Descrição da tarefa principal"
                            },
                            "prompt_type": {
                                "type": "string",
                                "enum": ["instruction", "creative", "analysis", "code", 
                                        "reasoning", "extraction", "summarization"]
                            },
                            "requirements": {
                                "type": "array",
                                "items": {"type": "string"},
                                "description": "Lista de requisitos específicos"
                            },
                            "context": {
                                "type": "string",
                                "description": "Contexto adicional ou background"
                            },
                            "constraints": {
                                "type": "array",
                                "items": {"type": "string"},
                                "description": "Limitações ou restrições"
                            }
                        },
                        "required": ["task", "prompt_type"]
                    }
                ),
                Tool(
                    name="get_technique",
                    description="Obtém detalhes sobre uma técnica específica de prompt engineering",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "technique": {
                                "type": "string",
                                "enum": ["chain_of_thought", "few_shot", "role_prompting", 
                                        "structured_output", "prompt_chaining", "constraints_specification",
                                        "self_consistency", "tree_of_thoughts"]
                            }
                        },
                        "required": ["technique"]
                    }
                ),
                Tool(
                    name="suggest_improvements",
                    description="Sugere melhorias específicas para um prompt",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "prompt": {
                                "type": "string",
                                "description": "O prompt a ser melhorado"
                            },
                            "goal": {
                                "type": "string",
                                "description": "O objetivo principal do prompt"
                            }
                        },
                        "required": ["prompt"]
                    }
                )
            ]
        
        @self.server.call_tool()
        async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
            if name == "analyze_prompt":
                prompt = arguments.get("prompt", "")
                analysis = self.analyze_prompt_quality(prompt)
                
                return [TextContent(
                    type="text",
                    text=json.dumps(analysis, indent=2)
                )]
            
            elif name == "optimize_prompt":
                prompt = arguments.get("prompt", "")
                prompt_type = arguments.get("prompt_type")
                
                result = self.optimize_prompt(prompt, prompt_type)
                
                return [TextContent(
                    type="text",
                    text=json.dumps(result, indent=2)
                )]
            
            elif name == "generate_prompt":
                task = arguments.get("task")
                prompt_type = arguments.get("prompt_type")
                requirements = arguments.get("requirements", [])
                context = arguments.get("context")
                constraints = arguments.get("constraints", [])
                
                generated = self.generate_prompt_from_template(
                    task, prompt_type, requirements, context, constraints
                )
                
                # Analisar o prompt gerado
                analysis = self.analyze_prompt_quality(generated)
                
                result = {
                    "generated_prompt": generated,
                    "prompt_type": prompt_type,
                    "quality_score": analysis["total_score"],
                    "techniques_used": [
                        "Structured format",
                        "Clear requirements",
                        "Defined constraints",
                        "Specific output format"
                    ],
                    "usage_tips": [
                        "Customize the template with your specific details",
                        "Add examples if the task is complex",
                        "Iterate based on initial results",
                        "Save successful prompts for reuse"
                    ]
                }
                
                return [TextContent(
                    type="text",
                    text=json.dumps(result, indent=2)
                )]
            
            elif name == "get_technique":
                technique = arguments.get("technique")
                technique_data = PROMPT_OPTIMIZATION_KB["techniques"].get(technique, {})
                
                if not technique_data:
                    return [TextContent(
                        type="text",
                        text=json.dumps({"error": f"Technique '{technique}' not found"}, indent=2)
                    )]
                
                result = {
                    "technique": technique,
                    "details": technique_data,
                    "implementation_tips": [
                        f"Use {technique} when: {technique_data.get('when_to_use', 'appropriate for the task')}",
                        "Start with the template and customize",
                        "Test with different variations",
                        "Combine with other techniques for complex tasks"
                    ]
                }
                
                return [TextContent(
                    type="text",
                    text=json.dumps(result, indent=2)
                )]
            
            elif name == "suggest_improvements":
                prompt = arguments.get("prompt", "")
                goal = arguments.get("goal", "")
                
                # Analisar prompt atual
                analysis = self.analyze_prompt_quality(prompt)
                prompt_type = self.identify_prompt_type(prompt)
                
                improvements = {
                    "current_analysis": analysis,
                    "prompt_type_detected": prompt_type,
                    "specific_improvements": [],
                    "recommended_techniques": [],
                    "example_revision": ""
                }
                
                # Sugestões baseadas nos scores baixos
                if analysis["individual_scores"]["clarity"] < 70:
                    improvements["specific_improvements"].append({
                        "issue": "Lack of clarity",
                        "suggestion": "Add a clear, specific question or instruction",
                        "example": "Instead of 'help with data', use 'Analyze this sales data and identify the top 3 trends'"
                    })
                    improvements["recommended_techniques"].append("constraints_specification")
                
                if analysis["individual_scores"]["structure"] < 70:
                    improvements["specific_improvements"].append({
                        "issue": "Poor structure",
                        "suggestion": "Organize with sections: Context, Task, Requirements, Expected Output",
                        "example": "Use bullet points or numbered lists for multiple requirements"
                    })
                    improvements["recommended_techniques"].append("structured_output")
                
                if analysis["individual_scores"]["completeness"] < 70:
                    improvements["specific_improvements"].append({
                        "issue": "Missing context",
                        "suggestion": "Add background information and specify the intended use",
                        "example": "Context: Working on a web app for small businesses..."
                    })
                
                # Criar exemplo de revisão
                optimized = self.optimize_prompt(prompt, prompt_type)
                improvements["example_revision"] = optimized["optimized_prompt"]
                
                # Técnicas recomendadas baseadas no tipo
                if prompt_type == "reasoning":
                    improvements["recommended_techniques"].append("chain_of_thought")
                elif prompt_type == "code":
                    improvements["recommended_techniques"].append("structured_output")
                elif prompt_type == "creative":
                    improvements["recommended_techniques"].append("role_prompting")
                
                return [TextContent(
                    type="text",
                    text=json.dumps(improvements, indent=2)
                )]
            
            else:
                raise ValueError(f"Unknown tool: {name}")
    
    async def run(self):
        """Executa o servidor MCP"""
        async with stdio_server() as (read_stream, write_stream):
            print("\n🚀 Servidor MCP de Otimização de Prompts está ON e rodando!")
            print("Aguardando requisições...\n")
            
            await self.server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="prompt-optimizer-server",
                    server_version="1.0.0",
                    capabilities=ServerCapabilities()
                ),
                raise_exceptions=False
            )


async def main():
    server = PromptOptimizerMCPServer()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())