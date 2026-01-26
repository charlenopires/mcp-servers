"""
MCP Prompt Engineering Server
Implements advanced prompt engineering techniques for optimizing queries
"""

from typing import Dict, List, Optional, Any
from fastmcp import FastMCP, Context
from pydantic import BaseModel
import re
from enum import Enum

# Initialize the MCP server
mcp = FastMCP(
    name="Prompt Engineering Best Practices Assistant",
    instructions="""Advanced prompt engineering server with optimization techniques and frameworks.

This server provides comprehensive prompt engineering capabilities:
- Optimize prompts using best practices (CRISPE, RACE, TRACE frameworks)
- Apply advanced reasoning techniques (Chain-of-Thought, ReAct, Tree of Thoughts)
- Analyze prompt quality and provide actionable feedback
- Check for biases and suggest mitigations
- Model-specific optimizations for Claude, GPT-4, Gemini

Use these tools to craft better prompts for any AI model.""",
    version="3.0.0"
)


class TaskType(Enum):
    """Identified task types"""
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
    """Request model for prompt optimization"""
    prompt: str
    task_type: Optional[str] = None
    target_audience: Optional[str] = None
    desired_length: Optional[str] = None
    tone: Optional[str] = None


class OptimizedPrompt(BaseModel):
    """Response model with optimized prompt"""
    original_prompt: str
    optimized_prompt: str
    techniques_applied: List[str]
    task_type: str
    suggestions: List[str]


class PromptEngineer:
    """Main class for prompt engineering"""

    def __init__(self):
        self.frameworks = {
            "RACE": ["Role", "Action", "Context", "Expectation"],
            "TRACE": ["Task", "Request", "Action", "Context", "Example"],
            "CRISPE": ["Capacity/Role", "Insight", "Statement", "Personality", "Experiment"],
            "CORE": ["Context", "Objective", "Role", "Example"],
            "COAST": ["Context", "Objective", "Actions", "Scenario", "Task"]
        }

        self.techniques = {
            "clarity": self._apply_clarity,
            "context": self._apply_context,
            "persona": self._apply_persona,
            "few_shot": self._apply_few_shot,
            "cot": self._apply_chain_of_thought,
            "format": self._apply_format_specification,
            "delimiters": self._apply_delimiters
        }

    def identify_task_type(self, prompt: str) -> TaskType:
        """Identifies the task type based on the prompt"""
        prompt_lower = prompt.lower()

        # Keywords for each task type
        keywords = {
            TaskType.CODE_GENERATION: ["code", "program", "function", "script", "implement", "develop", "coding", "programming", "implementation", "development"],
            TaskType.IMAGE_GENERATION: ["image", "draw", "create illustration", "generate photo", "picture", "visual", "graphic", "artwork"],
            TaskType.ANALYSIS: ["analyze", "evaluate", "examine", "investigate", "compare", "assessment", "review", "study"],
            TaskType.CREATIVE: ["create", "invent", "imagine", "story", "poem", "creative", "write", "compose", "design", "craft"],
            TaskType.PROBLEM_SOLVING: ["solve", "solution", "how to", "problem", "challenge", "fix", "resolve", "troubleshoot", "issue"],
            TaskType.QUESTION_ANSWERING: ["what is", "who is", "when", "where", "why", "explain", "how", "define", "describe", "clarify"],
            TaskType.TRANSLATION: ["translate", "translation", "to english", "to spanish", "to french", "to german", "convert language", "interpret"],
            TaskType.SUMMARIZATION: [
                "summarize", "summary", "synthesize", "main points", "overview", "abstract", "key points", "brief"]
        }

        for task_type, words in keywords.items():
            if any(word in prompt_lower for word in words):
                return task_type

        return TaskType.TEXT_GENERATION

    def _apply_clarity(self, prompt: str, context: Dict[str, Any]) -> str:
        """Applies clarity and specificity techniques"""
        # Remove common ambiguities
        clarity_improvements = {
            "this": "the specific concept/item mentioned previously",
            "that": "the particular element referenced",
            "thing": "the specific object/concept",
            "do": "execute/perform the specific task"
        }

        improved = prompt
        for vague, specific in clarity_improvements.items():
            if vague in improved.lower():
                improved = re.sub(
                    rf'\b{vague}\b', specific, improved, flags=re.IGNORECASE)

        return improved

    def _apply_context(self, prompt: str, context: Dict[str, Any]) -> str:
        """Adds relevant context to the prompt"""
        context_additions = []

        if context.get("target_audience"):
            context_additions.append(
                f"Target audience: {context['target_audience']}")

        if context.get("desired_length"):
            context_additions.append(
                f"Desired length: {context['desired_length']}")

        if context.get("tone"):
            context_additions.append(f"Tone: {context['tone']}")

        if context_additions:
            return f"{prompt}\n\nContext:\n" + "\n".join(f"- {item}" for item in context_additions)

        return prompt

    def _apply_persona(self, prompt: str, task_type: TaskType) -> str:
        """Applies role assignment based on task type"""
        personas = {
            TaskType.CODE_GENERATION: "You are an experienced software developer with deep knowledge of programming best practices",
            TaskType.ANALYSIS: "You are a specialized analyst with the ability to examine data and information critically and in detail",
            TaskType.CREATIVE: "You are a creative writer with the ability to create original and engaging content",
            TaskType.PROBLEM_SOLVING: "You are a consultant specialized in solving complex problems",
            TaskType.QUESTION_ANSWERING: "You are a subject matter expert with the ability to explain concepts clearly and didactically"
        }

        persona = personas.get(
            task_type, "You are a helpful and knowledgeable assistant")
        return f"{persona}.\n\n{prompt}"

    def _apply_few_shot(self, prompt: str, task_type: TaskType) -> str:
        """Adds relevant examples when appropriate"""
        if task_type == TaskType.CODE_GENERATION:
            return prompt + "\n\nExpected format example:\n```python\ndef example_function():\n    # Clear and commented implementation\n    pass\n```"
        elif task_type == TaskType.ANALYSIS:
            return prompt + "\n\nExpected structure:\n1. Introduction\n2. Detailed analysis\n3. Conclusions\n4. Recommendations"

        return prompt

    def _apply_chain_of_thought(self, prompt: str, task_type: TaskType) -> str:
        """Applies Chain-of-Thought for complex tasks"""
        if task_type in [TaskType.PROBLEM_SOLVING, TaskType.ANALYSIS]:
            return prompt + "\n\nPlease think step by step and show your reasoning before reaching the final answer."

        return prompt

    def _apply_format_specification(self, prompt: str, context: Dict[str, Any]) -> str:
        """Specifies the desired output format"""
        format_specs = []

        if "list" in prompt.lower():
            format_specs.append("Format: Bulleted list")
        elif "table" in prompt.lower():
            format_specs.append("Format: Structured table")
        elif "json" in prompt.lower():
            format_specs.append("Format: Valid JSON")

        if format_specs:
            return prompt + "\n\n" + "\n".join(format_specs)

        return prompt

    def _apply_delimiters(self, prompt: str) -> str:
        """Applies delimiters for better structuring"""
        # Identify prompt sections
        if "\n" in prompt and len(prompt.split("\n")) > 2:
            sections = prompt.split("\n")
            structured = "### Main Request ###\n" + sections[0]

            if len(sections) > 1:
                structured += "\n\n### Additional Details ###\n" + \
                    "\n".join(sections[1:])

            return structured

        return prompt

    def optimize_prompt(self, request: PromptOptimizationRequest) -> OptimizedPrompt:
        """Optimizes the prompt by applying appropriate techniques"""
        original = request.prompt
        task_type = self.identify_task_type(original)
        techniques_used = []

        # Context for techniques
        context = {
            "target_audience": request.target_audience,
            "desired_length": request.desired_length,
            "tone": request.tone,
            "task_type": task_type
        }

        # Apply techniques in order
        optimized = original

        # 1. Clarity
        optimized = self._apply_clarity(optimized, context)
        if optimized != original:
            techniques_used.append("Clarity and Specificity")

        # 2. Persona
        temp = optimized
        optimized = self._apply_persona(optimized, task_type)
        if optimized != temp:
            techniques_used.append("Role Assignment (Persona)")

        # 3. Context
        temp = optimized
        optimized = self._apply_context(optimized, context)
        if optimized != temp:
            techniques_used.append("Detailed Context")

        # 4. Chain-of-Thought for complex tasks
        temp = optimized
        optimized = self._apply_chain_of_thought(optimized, task_type)
        if optimized != temp:
            techniques_used.append("Chain-of-Thought (CoT)")

        # 5. Few-shot when appropriate
        temp = optimized
        optimized = self._apply_few_shot(optimized, task_type)
        if optimized != temp:
            techniques_used.append("Few-Shot Examples")

        # 6. Format
        temp = optimized
        optimized = self._apply_format_specification(optimized, context)
        if optimized != temp:
            techniques_used.append("Format Specification")

        # 7. Delimiters
        temp = optimized
        optimized = self._apply_delimiters(optimized)
        if optimized != temp:
            techniques_used.append("Structural Delimiters")

        # Additional suggestions
        suggestions = self._generate_suggestions(task_type, original)

        return OptimizedPrompt(
            original_prompt=original,
            optimized_prompt=optimized,
            techniques_applied=techniques_used,
            task_type=task_type.value,
            suggestions=suggestions
        )

    def _generate_suggestions(self, task_type: TaskType, prompt: str) -> List[str]:
        """Generates specific suggestions to improve the prompt"""
        suggestions = []

        # General suggestions
        if len(prompt) < 20:
            suggestions.append(
                "Consider adding more details about what you want")

        if "?" not in prompt and task_type == TaskType.QUESTION_ANSWERING:
            suggestions.append("Formulate your question clearly with '?'")

        # Type-specific suggestions
        task_suggestions = {
            TaskType.CODE_GENERATION: [
                "Specify the desired programming language",
                "Mention performance requirements or constraints",
                "Indicate if you need comments in the code"
            ],
            TaskType.IMAGE_GENERATION: [
                "Describe the desired artistic style",
                "Specify colors, lighting and composition",
                "Add details about the environment/scenario"
            ],
            TaskType.ANALYSIS: [
                "Define the analysis criteria",
                "Specify the desired level of depth",
                "Indicate if you need recommendations"
            ]
        }

        if task_type in task_suggestions:
            suggestions.extend(task_suggestions[task_type])

        return suggestions[:3]  # Returns maximum 3 suggestions


# Instantiate the prompt engineer
engineer = PromptEngineer()


@mcp.tool(tags=["optimization", "best-practices", "enhancement"])
async def prompt_optimize_generic(
    prompt: str,
    task_type: Optional[str] = None,
    target_audience: Optional[str] = None,
    desired_length: Optional[str] = None,
    tone: Optional[str] = None,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Optimizes a prompt by applying prompt engineering best practices

    Args:
        prompt: The original prompt to be optimized
        task_type: Task type (optional, will be detected automatically)
        target_audience: Target audience for the response
        desired_length: Desired length of the response
        tone: Desired tone (formal, informal, technical, etc.)

    Returns:
        Dictionary with the optimized prompt and information about applied techniques
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


@mcp.tool(tags=["analysis", "scoring", "quality"])
async def prompt_analyze_generic(prompt: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Analyzes a prompt and provides feedback on its quality

    Args:
        prompt: The prompt to be analyzed

    Returns:
        Detailed analysis of the prompt with scoring and recommendations
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

    # Quality analysis
    score = 0

    # Clarity (0-25 points)
    if len(prompt) > 20:
        score += 10
        analysis["strengths"].append("Adequate length")
    else:
        analysis["weaknesses"].append("Prompt too short")

    if not any(word in prompt.lower() for word in ["this", "that", "thing"]):
        score += 15
        analysis["strengths"].append("Specific language")
    else:
        analysis["weaknesses"].append("Contains vague terms")

    # Context (0-25 points)
    context_indicators = ["for", "when", "where", "how", "why", "because", "since", "during", "about", "regarding"]
    if any(indicator in prompt.lower() for indicator in context_indicators):
        score += 25
        analysis["strengths"].append("Includes context")
    else:
        analysis["weaknesses"].append("Lacks context")
        analysis["recommendations"].append(
            "Add context about when, where or how")

    # Clear objective (0-25 points)
    action_verbs = ["create", "analyze", "explain",
                    "develop", "summarize", "translate", "write", "generate", "produce",
                    "design", "build", "implement"]
    if any(verb in prompt.lower() for verb in action_verbs):
        score += 25
        analysis["strengths"].append("Clear objective")
    else:
        analysis["weaknesses"].append("Unclear objective")
        analysis["recommendations"].append(
            "Use action verbs to clarify the objective")

    # Structure (0-25 points)
    if "?" in prompt or "\n" in prompt:
        score += 25
        analysis["strengths"].append("Well structured")
    else:
        analysis["recommendations"].append(
            "Consider using punctuation or line breaks for better structure")

    analysis["quality_score"] = score

    # Recommendations based on score
    if score < 50:
        analysis["recommendations"].insert(
            0, "This prompt needs significant improvements")
    elif score < 75:
        analysis["recommendations"].insert(
            0, "Reasonable prompt, but can be improved")
    else:
        analysis["recommendations"].insert(0, "Well-structured prompt!")

    return analysis


@mcp.tool(tags=["frameworks", "suggestions", "structure"])
async def prompt_suggest_framework(task_description: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Suggests the best prompt framework for a specific task

    Args:
        task_description: Description of the task to be performed

    Returns:
        Recommended framework with application example
    """
    task_type = engineer.identify_task_type(task_description)

    # Mapping of task types to frameworks
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

    # Create task-based example
    examples = {
        "RACE": {
            "Role": "You are a subject matter expert",
            "Action": "Explain in detail",
            "Context": "For a technical audience",
            "Expectation": "Structured response with examples"
        },
        "TRACE": {
            "Task": "Create informative content",
            "Request": "Develop a complete text",
            "Action": "Write clearly and engagingly",
            "Context": "For professionals in the field",
            "Example": "Similar to specialized magazine articles"
        },
        "CRISPE": {
            "Capacity/Role": "Innovative content creator",
            "Insight": "Understand current trends",
            "Statement": "Create something unique and memorable",
            "Personality": "Creative and inspiring tone",
            "Experiment": "Explore unconventional approaches"
        }
    }

    example = examples.get(recommended_framework, {})

    return {
        "task_type": task_type.value,
        "recommended_framework": recommended_framework,
        "framework_components": framework_components,
        "example_application": example,
        "usage_tip": f"Use the {recommended_framework} framework by structuring your prompt with each component"
    }


@mcp.tool(tags=["techniques", "reasoning", "advanced"])
async def prompt_apply_technique(
    prompt: str,
    technique: str = "chain_of_thought",
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Applies advanced reasoning techniques to the prompt

    Args:
        prompt: The original prompt
        technique: Technique to apply (chain_of_thought, self_consistency, react, tree_of_thoughts)

    Returns:
        Modified prompt with the advanced technique applied
    """
    techniques_map = {
        "chain_of_thought": {
            "name": "Chain-of-Thought (CoT)",
            "suffix": "\n\nLet's think step by step:\n1. First, let's understand the problem\n2. Then, analyze possible approaches\n3. Finally, arrive at a detailed solution",
            "description": "Guides the model through reasoning steps"
        },
        "self_consistency": {
            "name": "Self-Consistency",
            "suffix": "\n\nGenerate 3 different approaches to this question and then synthesize the best answer based on the generated approaches.",
            "description": "Multiple reasoning paths for greater reliability"
        },
        "react": {
            "name": "ReAct (Reason + Act)",
            "suffix": "\n\nThought: Analyze what needs to be done\nAction: Determine the necessary steps\nObservation: Evaluate the results of each step\nRepeat until reaching the complete solution.",
            "description": "Combines reasoning with iterative actions"
        },
        "tree_of_thoughts": {
            "name": "Tree of Thoughts (ToT)",
            "suffix": "\n\nExplore multiple possibilities:\n- Path A: [develop this approach]\n- Path B: [develop alternative]\n- Path C: [explore another option]\nEvaluate which path is most promising and develop it completely.",
            "description": "Exploration of multiple thought paths"
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
        "best_for": "Complex problems that require structured reasoning"
    }


@mcp.tool(tags=["bias-check", "ethics", "inclusive"])
async def prompt_check_bias(prompt: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Checks for potential biases in the prompt and suggests mitigations

    Args:
        prompt: The prompt to be checked

    Returns:
        Bias analysis with mitigation suggestions
    """
    biases_found = []
    mitigations = []

    # Gender bias verification
    gender_terms = {
        "masculine": ["he", "man", "masculine", "sir", "male", "gentleman", "his", "him"],
        "feminine": ["she", "woman", "feminine", "madam", "female", "lady", "her", "hers"]
    }

    gender_bias = {"masculine": 0, "feminine": 0}
    for gender, terms in gender_terms.items():
        for term in terms:
            if term in prompt.lower():
                gender_bias[gender] += 1

    if gender_bias["masculine"] > 0 and gender_bias["feminine"] == 0:
        biases_found.append(
            "Possible gender bias (only masculine terms)")
        mitigations.append(
            "Use gender-neutral language or include diverse examples")

    # Professional stereotypes verification
    stereotypes = {
        "engineer": "engineering professional",
        "nurse": "nursing professional",
        "secretary": "administrative professional",
        "developer": "software professional",
        "manager": "management professional",
        "assistant": "administrative professional"
    }

    for stereotype, neutral in stereotypes.items():
        if stereotype in prompt.lower():
            biases_found.append(
                f"Term with potential stereotype: '{stereotype}'")
            mitigations.append(
                f"Consider using '{neutral}' for greater neutrality")

    # Cultural assumptions verification
    if any(word in prompt.lower() for word in ["normal", "standard", "common", "typical"]):
        biases_found.append("Possible unspecified cultural assumptions")
        mitigations.append(
            "Specify cultural context or use more inclusive terms")

    # Prompt suggestion to challenge biases
    bias_challenger = "\n\nWhen responding, consider multiple perspectives and avoid making assumptions based on stereotypes."

    return {
        "prompt": prompt,
        "biases_detected": biases_found if biases_found else ["No obvious bias detected"],
        "mitigation_suggestions": mitigations,
        "bias_score": len(biases_found),
        "improved_prompt": prompt + bias_challenger if biases_found else prompt,
        "general_tips": [
            "Use inclusive language",
            "Avoid generalizations",
            "Consider multiple perspectives",
            "Specify contexts when relevant"
        ]
    }

# MCP Prompts for prompt engineering guidance

@mcp.prompt("optimize_for_model")
async def optimize_for_model_prompt(
    prompt: str,
    model: str = "claude",
    task_type: str = "general"
) -> List[Dict[str, str]]:
    """
    Generate prompt optimized for a specific AI model.

    Args:
        prompt: The prompt to optimize
        model: Target model (claude, gpt4, gemini)
        task_type: Type of task (general, code, creative, analysis)
    """
    model_tips = {
        "claude": "Claude responds well to clear context, structured requests, and explicit role assignments. Use XML tags for complex structures.",
        "gpt4": "GPT-4 benefits from system messages, clear formatting, and step-by-step instructions. Use markdown for structure.",
        "gemini": "Gemini works well with concise prompts, clear objectives, and multimodal context when available."
    }

    return [
        {
            "role": "system",
            "content": f"""You are a prompt optimization expert for {model.upper()}.
{model_tips.get(model, "Apply general prompt engineering best practices.")}

Optimize prompts following model-specific patterns while maintaining clarity and effectiveness."""
        },
        {
            "role": "user",
            "content": f"""Optimize this prompt for {model.upper()}:

Original prompt: {prompt}
Task type: {task_type}

Provide:
1. Optimized prompt
2. Techniques applied
3. Expected improvements
4. Model-specific tips"""
        }
    ]


@mcp.prompt("chain_of_thought_builder")
async def chain_of_thought_builder_prompt(
    problem: str,
    complexity: str = "medium",
    steps: int = 5
) -> List[Dict[str, str]]:
    """
    Build a structured Chain-of-Thought prompt.

    Args:
        problem: The problem to solve
        complexity: Complexity level (simple, medium, complex)
        steps: Number of reasoning steps
    """
    return [
        {
            "role": "system",
            "content": """You are an expert in Chain-of-Thought (CoT) prompting.
Create structured reasoning prompts that guide the model through logical steps.
Include explicit thinking markers and verification steps."""
        },
        {
            "role": "user",
            "content": f"""Create a {steps}-step Chain-of-Thought prompt for:

Problem: {problem}
Complexity: {complexity}

Structure the prompt with:
1. Problem restatement
2. Key information extraction
3. {steps} reasoning steps with explicit markers
4. Solution synthesis
5. Verification step

Output the complete CoT prompt ready for use."""
        }
    ]


@mcp.prompt("few_shot_generator")
async def few_shot_generator_prompt(
    task: str,
    num_examples: int = 3,
    input_type: str = "text",
    output_type: str = "text"
) -> List[Dict[str, str]]:
    """
    Generate few-shot examples for a given task.

    Args:
        task: Description of the task
        num_examples: Number of examples to generate
        input_type: Type of input (text, code, json)
        output_type: Type of output (text, code, json)
    """
    return [
        {
            "role": "system",
            "content": """You are an expert at creating effective few-shot examples.
Generate diverse, representative examples that clearly demonstrate the task pattern.
Ensure examples cover edge cases and common variations."""
        },
        {
            "role": "user",
            "content": f"""Generate {num_examples} few-shot examples for this task:

Task: {task}
Input type: {input_type}
Output type: {output_type}

For each example provide:
- Input
- Expected output
- Brief explanation of why this is a good example

Then provide the complete prompt template with examples included."""
        }
    ]


@mcp.prompt("apply_framework")
async def apply_framework_prompt(
    requirement: str,
    framework: str = "CRISPE"
) -> List[Dict[str, str]]:
    """
    Apply a specific prompt framework to a requirement.

    Args:
        requirement: What the prompt needs to accomplish
        framework: Framework to apply (CRISPE, RACE, TRACE, CORE, COAST)
    """
    frameworks_structure = {
        "CRISPE": ["Capacity/Role", "Insight", "Statement", "Personality", "Experiment"],
        "RACE": ["Role", "Action", "Context", "Expectation"],
        "TRACE": ["Task", "Request", "Action", "Context", "Example"],
        "CORE": ["Context", "Objective", "Role", "Example"],
        "COAST": ["Context", "Objective", "Actions", "Scenario", "Task"]
    }

    components = frameworks_structure.get(framework, frameworks_structure["CRISPE"])
    components_text = "\n".join([f"- {c}" for c in components])

    return [
        {
            "role": "system",
            "content": f"""You are an expert in the {framework} prompt framework.
Apply the framework systematically to create effective, structured prompts.

Framework components:
{components_text}"""
        },
        {
            "role": "user",
            "content": f"""Apply the {framework} framework to this requirement:

{requirement}

Provide:
1. Each framework component filled in
2. The complete structured prompt
3. Tips for using this framework effectively
4. When to use {framework} vs other frameworks"""
        }
    ]


@mcp.prompt("create_system_prompt")
async def create_system_prompt(
    agent_role: str,
    capabilities: List[str],
    constraints: List[str] = None,
    tone: str = "professional"
) -> List[Dict[str, str]]:
    """
    Create an optimized system prompt for an AI agent.

    Args:
        agent_role: The role the agent should play
        capabilities: List of capabilities the agent should have
        constraints: List of constraints or limitations
        tone: Desired tone (professional, friendly, technical)
    """
    capabilities_text = "\n".join([f"- {c}" for c in capabilities])
    constraints_text = "\n".join([f"- {c}" for c in constraints]) if constraints else "None specified"

    return [
        {
            "role": "system",
            "content": """You are an expert at creating effective system prompts for AI agents.
Design prompts that clearly define role, capabilities, and behavior.
Follow best practices for agent instruction design."""
        },
        {
            "role": "user",
            "content": f"""Create a comprehensive system prompt for this agent:

## Role
{agent_role}

## Capabilities
{capabilities_text}

## Constraints
{constraints_text}

## Tone
{tone}

Provide:
1. Complete system prompt
2. Example conversation starters
3. Edge case handling instructions
4. Evaluation criteria for good responses"""
        }
    ]


# Configuration and initialization
if __name__ == "__main__":
    import asyncio

    # Usage example
    async def test_server():
        # Optimization test
        result = await prompt_optimize_generic(
            prompt="explain this concept",
            target_audience="university students",
            tone="didactic"
        )
        print("Optimization:", result)

        # Analysis test
        analysis = await prompt_analyze_generic("How does photosynthesis work?")
        print("\nAnalysis:", analysis)

        # Framework test
        framework = await prompt_suggest_framework("I need to create a sales report")
        print("\nSuggested framework:", framework)

    # Start the server
    print("MCP Prompt Engineering Server started!")
    print("Available tools:")
    print("- prompt_optimize_generic: Optimizes prompts automatically")
    print("- prompt_analyze_generic: Analyzes prompt quality")
    print("- prompt_suggest_framework: Suggests appropriate frameworks")
    print("- prompt_apply_technique: Applies advanced techniques")
    print("- prompt_check_bias: Checks and mitigates biases")

    # For local testing
    # asyncio.run(test_server())

    # Start the MCP server
    mcp.run()
