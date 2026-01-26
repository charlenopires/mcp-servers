#!/usr/bin/env python3
"""
MCP server for analyzing MCP server creation prompts.
This server provides tools to evaluate and give feedback on prompts
for creating MCP servers based on MCP documentation best practices.
"""

import logging
from typing import List, Dict, Any, Optional, TypedDict
from fastmcp import FastMCP, Context
from pydantic import BaseModel, Field
import re
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP(
    name="MCP Prompt Analyzer",
    instructions="""Analyzes and provides feedback on MCP server creation prompts.

This server helps you create better MCP servers by:
- Analyzing prompts for quality and completeness
- Validating requirements against best practices
- Suggesting improvements for server creation prompts
- Providing FastMCP patterns and guidelines

Use the tools to optimize your MCP server development process.""",
    version="3.0.0"
)


class PromptAnalysis(BaseModel):
    """Model for prompt analysis results"""
    score: int = Field(description="Overall quality score from 1-10")
    strengths: List[str] = Field(
        description="Strong points identified in the prompt")
    weaknesses: List[str] = Field(description="Areas for improvement")
    recommendations: List[str] = Field(
        description="Specific recommendations for improvement")
    best_practices_alignment: Dict[str, bool] = Field(
        description="Alignment with MCP best practices")
    missing_elements: List[str] = Field(
        description="Important elements missing from the prompt")


class ValidationReport(TypedDict):
    """Typed structure for validation report"""
    overall_score: int
    validation_passed: bool
    requirements_coverage: Dict[str, bool]
    missing_requirements: List[str]
    recommendations: List[str]
    critical_issues: List[str]
    warnings: List[str]


class MCPPromptAnalyzer:
    """Main analyzer for MCP server creation prompts"""

    def __init__(self):
        # Main best practices from MCP documentation
        self.best_practices = {
            "clear_purpose": "Server should have a well-defined and specific purpose",
            "adequate_tool_design": "Tools should be focused, well-documented and follow naming conventions",
            "error_handling": "Comprehensive error handling and validation",
            "security_considerations": "Input validation, sanitization and security measures",
            "resource_management": "Proper resource handling and cleanup",
            "documentation": "Clear documentation and examples",
            "schema_validation": "Proper schema definitions and validation",
            "transport_protocol": "Appropriate transport protocol selection",
            "testing_strategy": "Testing and debugging considerations",
            "performance": "Performance and scalability considerations"
        }

        # Common patterns to look for in good prompts
        self.positive_patterns = [
            r"tool(?:s)?\s+(?:that|for|to)",
            r"implement(?:s|ing|ation)?\s+(?:a|an|the)",
            r"error\s+(?:handling|treatment)",
            r"validation",
            r"security",
            r"schema",
            r"documentation",
            r"test(?:s|ing)?",
            r"debug",
            r"example(?:s)?",
            r"best\s+practice(?:s)?",
            r"performance",
            r"scalability"
        ]

        # Warning signs that indicate poor prompt quality
        self.negative_patterns = [
            r"make?\s+(?:a|an|the)\s+(?:simple|basic|quick)",
            r"just\s+(?:create|make|build)",
            r"anything",
            r"doesn't\s+matter",
            r"generic",
            r"simple\s+(?:server|tool)"
        ]

    def analyze_prompt(self, prompt: str) -> PromptAnalysis:
        """Analyze an MCP server creation prompt"""

        prompt_lowercase = prompt.lower()

        # Calculate base score
        score = 5  # Start with neutral score
        strengths = []
        weaknesses = []
        recommendations = []
        missing_elements = []

        # Check positive patterns
        positive_matches = 0
        for pattern in self.positive_patterns:
            if re.search(pattern, prompt_lowercase):
                positive_matches += 1

        # Check negative patterns
        negative_matches = 0
        for pattern in self.negative_patterns:
            if re.search(pattern, prompt_lowercase):
                negative_matches += 1

        # Adjust score based on patterns
        # Limit positive contribution
        score += min(positive_matches * 0.5, 3)
        score -= negative_matches * 1.5

        # Analyze against best practices
        best_practices_alignment: Dict[str, bool] = {}
        self._analyze_best_practices(prompt_lowercase, best_practices_alignment,
                                   strengths, weaknesses, missing_elements)
        # Generate recommendations
        recommendations = self._generate_recommendations(
            prompt_lowercase, missing_elements)

        # Final score adjustment based on best practices alignment
        alignment_score = sum(
            best_practices_alignment.values()) / len(best_practices_alignment)
        score = int((score + alignment_score * 10) / 2)
        score = max(1, min(10, score))  # Limit between 1-10

        return PromptAnalysis(
            score=score,
            strengths=strengths,
            weaknesses=weaknesses,
            recommendations=recommendations,
            best_practices_alignment=best_practices_alignment,
            missing_elements=missing_elements
        )

    def _analyze_best_practices(self, prompt: str, alignment: Dict[str, bool],
                              strengths: List[str], weaknesses: List[str],
                              missing_elements: List[str]):
        """Analyze prompt against MCP best practices"""

        # Clear purpose
        if any(word in prompt for word in ['purpose', 'objective', 'goal', 'specific', 'focused']):
            alignment['clear_purpose'] = True
            strengths.append(
                "Shows clear understanding of server purpose")
        else:
            alignment['clear_purpose'] = False
            missing_elements.append(
                "Clear statement of server purpose and objectives")

        # Tool design
        if any(word in prompt for word in ['tool', 'function', 'capability', 'functionality']):
            alignment['adequate_tool_design'] = True
            strengths.append("Mentions tools or functionalities")
        else:
            alignment['adequate_tool_design'] = False
            missing_elements.append(
                "Specific tool and capability definitions")

        # Error handling
        if any(word in prompt for word in ['error', 'exception', 'validation', 'handle']):
            alignment['error_handling'] = True
            strengths.append("Considers error handling")
        else:
            alignment['error_handling'] = False
            missing_elements.append(
                "Error handling and validation strategy")

        # Security
        if any(word in prompt for word in ['security', 'secure', 'sanitize', 'validate']):
            alignment['security_considerations'] = True
            strengths.append("Includes security considerations")
        else:
            alignment['security_considerations'] = False
            missing_elements.append(
                "Security considerations and input validation")

        # Documentation
        if any(word in prompt for word in ['document', 'example', 'readme', 'guide']):
            alignment['documentation'] = True
            strengths.append("Values documentation")
        else:
            alignment['documentation'] = False
            missing_elements.append("Documentation and usage examples")

        # Schema validation
        if any(word in prompt for word in ['schema', 'type', 'model', 'structure']):
            alignment['schema_validation'] = True
            strengths.append("Considers data schemas")
        else:
            alignment['schema_validation'] = False
            missing_elements.append(
                "Schema definitions and data validation")

        # Testing
        if any(word in prompt for word in ['test', 'debug', 'verify']):
            alignment['testing_strategy'] = True
            strengths.append("Includes testing considerations")
        else:
            alignment['testing_strategy'] = False
            missing_elements.append("Testing and debugging strategy")

        # Performance
        if any(word in prompt for word in ['performance', 'scalable', 'efficient', 'optimize']):
            alignment['performance'] = True
            strengths.append("Considers performance aspects")
        else:
            alignment['performance'] = False
            missing_elements.append(
                "Performance and scalability considerations")

        # Transport protocol
        if any(word in prompt for word in ['stdio', 'http', 'sse', 'transport', 'protocol']):
            alignment['transport_protocol'] = True
            strengths.append("Specifies transport protocol")
        else:
            alignment['transport_protocol'] = False
            missing_elements.append(
                "Transport protocol specification")

        # Resource management
        if any(word in prompt for word in ['resource', 'cleanup', 'manage', 'lifecycle']):
            alignment['resource_management'] = True
            strengths.append("Considers resource management")
        else:
            alignment['resource_management'] = False
            missing_elements.append("Resource management and cleanup")

    def _generate_recommendations(self, prompt: str, missing_elements: List[str]) -> List[str]:
        """Generate specific recommendations to improve the prompt"""
        recommendations = []

        if not any(word in prompt for word in ['tool', 'function']):
            recommendations.append(
                "Define specific tools and their functionalities clearly")

        if not any(word in prompt for word in ['error', 'validation']):
            recommendations.append(
                "Include error handling and input validation requirements")

        if not any(word in prompt for word in ['security', 'sanitize']):
            recommendations.append(
                "Specify security considerations and input sanitization")

        if not any(word in prompt for word in ['schema', 'type']):
            recommendations.append(
                "Define data schemas and type definitions")

        if not any(word in prompt for word in ['test', 'debug']):
            recommendations.append("Include testing and debugging requirements")

        if not any(word in prompt for word in ['document', 'example']):
            recommendations.append("Request documentation and usage examples")

        if not any(word in prompt for word in ['performance', 'scalable']):
            recommendations.append(
                "Consider performance and scalability requirements")

        if len(prompt.split()) < 20:
            recommendations.append(
                "Provide more detailed requirements and context")

        if not any(word in prompt for word in ['protocol', 'transport']):
            recommendations.append(
                "Specify the desired transport protocol (stdio, HTTP+SSE)")

        return recommendations


# Initialize the analyzer
analyzer = MCPPromptAnalyzer()


@mcp.tool(tags=["analysis", "scoring", "validation"])
async def mcp_analyze_server_prompt(prompt: str, ctx: Optional[Context] = None) -> PromptAnalysis:
    """
    Analyze an MCP server creation prompt for quality and alignment with best practices.

    Args:
        prompt: The prompt text to analyze for MCP server creation
        ctx: Optional context for logging and progress reporting

    Returns:
        AnalisePrompt: Detailed analysis with score, strengths, weaknesses and recommendations
    """
    try:
        if ctx:
            await ctx.info(f"Analyzing prompt: {prompt[:100]}...")
        logger.info(f"Analyzing prompt: {prompt[:100]}...")
        analysis = analyzer.analyze_prompt(prompt)
        if ctx:
            await ctx.info(f"Analysis complete. Score: {analysis.score}/10")
        logger.info(f"Analysis complete. Score: {analysis.score}/10")
        return analysis
    except Exception as e:
        logger.error(f"Error analyzing prompt: {e}")
        raise


@mcp.tool(tags=["best-practices", "documentation", "guidelines"])
async def mcp_get_best_practices() -> Dict[str, str]:
    """
    Get a summary of MCP server development best practices for FastMCP 3.0.

    Returns:
        Dict[str, str]: Key best practices for MCP server development
    """
    return {
        "clear_purpose": "Define a specific and focused purpose for your MCP server",
        "tool_design": "Design tools that are focused, well-documented and follow naming conventions",
        "context_injection": "Use ctx: Context for logging and progress reporting in tools",
        "tags": "Add tags to tools for better organization and discoverability",
        "error_handling": "Implement comprehensive error handling and input validation",
        "security": "Use component-level auth with require_auth or require_scopes()",
        "schemas": "Define clear schemas with Pydantic models for inputs and outputs",
        "documentation": "Provide clear documentation and usage examples",
        "testing": "Test tools directly (decorators return original functions in FastMCP 3.0)",
        "lifespan": "Use lifespan management for resources that need initialization/cleanup",
        "composition": "Use mount() to compose multiple servers with namespaces",
        "transport": "Choose appropriate transport protocol (stdio for local, http for remote)",
        "prompts": "Define @mcp.prompt() for reusable prompt templates"
    }


@mcp.tool(tags=["optimization", "improvement", "suggestions"])
async def mcp_suggest_prompt_improvements(original_prompt: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Suggest specific improvements for an MCP server creation prompt.

    Args:
        original_prompt: The original prompt to improve
        ctx: Optional context for logging and progress reporting

    Returns:
        Dict containing improved prompt and explanation of changes
    """
    try:
        if ctx:
            await ctx.info("Analyzing prompt for improvements...")
        analysis = analyzer.analyze_prompt(original_prompt)

        # Generate improved prompt
        improved_sections = []

        # Add purpose if missing
        if not analysis.best_practices_alignment.get('clear_purpose', False):
            improved_sections.append(
                "Purpose: Create an MCP server with a specific and well-defined objective."
            )

        # Add tool specifications if missing
        if not analysis.best_practices_alignment.get('adequate_tool_design', False):
            improved_sections.append(
                "Tools: Define specific tools with clear names, descriptions and parameters."
            )

        # Add technical requirements
        technical_additions = []
        if not analysis.best_practices_alignment.get('error_handling', False):
            technical_additions.append("comprehensive error handling")
        if not analysis.best_practices_alignment.get('security_considerations', False):
            technical_additions.append(
                "input validation and security measures")
        if not analysis.best_practices_alignment.get('schema_validation', False):
            technical_additions.append("proper schema definitions")

        if technical_additions:
            improved_sections.append(
                f"Technical Requirements: Include {', '.join(technical_additions)}."
            )

        # Add documentation and testing
        if not analysis.best_practices_alignment.get('documentation', False):
            improved_sections.append(
                "Documentation: Provide clear documentation and usage examples."
            )

        if not analysis.best_practices_alignment.get('testing_strategy', False):
            improved_sections.append(
                "Testing: Include testing strategy and debugging considerations."
            )

        improved_prompt = original_prompt
        if improved_sections:
            improved_prompt += "\n\nAdditional Requirements:\n" + \
                "\n".join(improved_sections)

        return {
            "original_prompt": original_prompt,
            "improved_prompt": improved_prompt,
            "improvements_made": improved_sections,
            "score_improvement": f"Expected improvement from {analysis.score}/10 to {min(10, analysis.score + len(improved_sections))}/10"
        }

    except Exception as e:
        logger.error(f"Error improving prompt: {e}")
        raise


@mcp.tool(tags=["validation", "requirements", "checklist"])
async def mcp_validate_requirements(requirements: str, ctx: Optional[Context] = None) -> ValidationReport:
    """
    Validate MCP server requirements against best practices checklist.

    Args:
        requirements: The requirements specification to validate
        ctx: Optional context for logging and progress reporting

    Returns:
        ValidationReport containing validation results and missing requirements
    """
    try:
        if ctx:
            await ctx.info("Validating requirements against best practices...")
        analysis = analyzer.analyze_prompt(requirements)

        # Create detailed validation report
        validation_report: ValidationReport = {
            "overall_score": analysis.score,
            "validation_passed": analysis.score >= 7,
            "requirements_coverage": analysis.best_practices_alignment,
            "missing_requirements": analysis.missing_elements,
            "recommendations": analysis.recommendations,
            "critical_issues": [],
            "warnings": []
        }

        # Identify critical issues
        if not analysis.best_practices_alignment.get('security_considerations', False):
            validation_report["critical_issues"].append(
                "Security considerations missing")

        if not analysis.best_practices_alignment.get('error_handling', False):
            validation_report["critical_issues"].append(
                "Error handling strategy missing")

        # Identify warnings
        if not analysis.best_practices_alignment.get('documentation', False):
            validation_report["warnings"].append(
                "Documentation requirements not specified")

        if not analysis.best_practices_alignment.get('testing_strategy', False):
            validation_report["warnings"].append(
                "Testing strategy not defined")

        return validation_report

    except Exception as e:
        logger.error(f"Error validating requirements: {e}")
        raise


# MCP Prompts for server development guidance

@mcp.prompt("create_mcp_server")
async def create_mcp_server_prompt(
    purpose: str,
    tools: List[str],
    has_resources: bool = False,
    needs_auth: bool = False
) -> List[Dict[str, str]]:
    """
    Generate an optimized prompt for creating an MCP server.

    Args:
        purpose: What the server should accomplish
        tools: List of tools the server needs
        has_resources: Whether the server exposes resources
        needs_auth: Whether authentication is required
    """
    tools_text = "\n".join([f"- {t}" for t in tools])
    auth_text = "\n- Implement component-level auth with require_auth/require_scopes" if needs_auth else ""
    resources_text = "\n- Define @mcp.resource() for data exposure" if has_resources else ""

    return [
        {
            "role": "system",
            "content": """You are an expert FastMCP 3.0 developer.
Create MCP servers following best practices:
- Use @mcp.tool() with tags for organization
- Implement ctx: Context for logging and progress
- Use Pydantic models for validation
- Add comprehensive error handling
- Include docstrings and type hints"""
        },
        {
            "role": "user",
            "content": f"""Create an MCP server with FastMCP 3.0.

## Purpose
{purpose}

## Required Tools
{tools_text}

## Additional Requirements
- Add tags to all tools
- Use Context injection for logging{auth_text}{resources_text}
- Include usage examples
- Add proper error handling"""
        }
    ]


@mcp.prompt("review_mcp_prompt")
async def review_mcp_prompt(prompt_to_review: str) -> List[Dict[str, str]]:
    """
    Generate a prompt for reviewing MCP server creation prompts.

    Args:
        prompt_to_review: The prompt to be reviewed
    """
    return [
        {
            "role": "system",
            "content": """You are an MCP prompt quality expert.
Review prompts for:
- Clarity of purpose and requirements
- Tool and resource specifications
- Security and error handling considerations
- FastMCP 3.0 best practices alignment
- Completeness for implementation"""
        },
        {
            "role": "user",
            "content": f"""Review this MCP server creation prompt:

{prompt_to_review}

Evaluate:
1. Clarity (1-10)
2. Completeness (1-10)
3. Technical accuracy (1-10)
4. Security considerations
5. Missing elements
6. Improvement suggestions"""
        }
    ]


@mcp.prompt("design_mcp_architecture")
async def design_mcp_architecture_prompt(
    domain: str,
    scale: str = "small",
    integrations: List[str] = None
) -> List[Dict[str, str]]:
    """
    Generate a prompt for designing MCP server architecture.

    Args:
        domain: The business domain (e.g., "e-commerce", "analytics")
        scale: Expected scale (small, medium, large)
        integrations: List of external integrations needed
    """
    integrations_text = "\n".join([f"- {i}" for i in integrations]) if integrations else "None specified"

    return [
        {
            "role": "system",
            "content": """You are an MCP architecture expert.
Design scalable, maintainable MCP server architectures using FastMCP 3.0 patterns:
- Server composition with mount()
- Lifespan management for shared resources
- Proper namespace organization
- State management strategies"""
        },
        {
            "role": "user",
            "content": f"""Design an MCP server architecture.

## Domain
{domain}

## Scale
{scale}

## External Integrations
{integrations_text}

## Deliverables
1. Architecture diagram (text-based)
2. Server composition strategy
3. Tool organization by namespace
4. State management approach
5. Resource lifecycle management
6. Security boundaries"""
        }
    ]


@mcp.prompt("troubleshoot_mcp_server")
async def troubleshoot_mcp_server_prompt(
    error_description: str,
    server_code: str = "",
    transport: str = "stdio"
) -> List[Dict[str, str]]:
    """
    Generate a prompt for troubleshooting MCP server issues.

    Args:
        error_description: Description of the error or issue
        server_code: Relevant server code (optional)
        transport: Transport protocol being used
    """
    code_section = f"\n\n## Server Code\n```python\n{server_code}\n```" if server_code else ""

    return [
        {
            "role": "system",
            "content": """You are an MCP troubleshooting expert.
Diagnose and fix issues in FastMCP servers:
- Connection and transport problems
- Tool execution errors
- Context and lifespan issues
- Authentication failures
- Resource access problems"""
        },
        {
            "role": "user",
            "content": f"""Troubleshoot this MCP server issue.

## Error Description
{error_description}

## Transport
{transport}{code_section}

## Analysis Required
1. Identify the root cause
2. Explain why this happens
3. Provide step-by-step fix
4. Suggest preventive measures
5. Include test verification"""
        }
    ]


@mcp.prompt("migrate_mcp_version")
async def migrate_mcp_version_prompt(
    current_version: str,
    target_version: str = "3.0",
    features_to_adopt: List[str] = None
) -> List[Dict[str, str]]:
    """
    Generate a prompt for migrating between FastMCP versions.

    Args:
        current_version: Current FastMCP version (e.g., "2.0")
        target_version: Target FastMCP version (e.g., "3.0")
        features_to_adopt: Specific features to adopt in migration
    """
    features_text = "\n".join([f"- {f}" for f in features_to_adopt]) if features_to_adopt else "All available features"

    return [
        {
            "role": "system",
            "content": """You are a FastMCP migration expert.
Guide migrations between FastMCP versions:
- Breaking changes identification
- Feature adoption strategies
- Code transformation patterns
- Testing migration success"""
        },
        {
            "role": "user",
            "content": f"""Migrate MCP server from FastMCP {current_version} to {target_version}.

## Features to Adopt
{features_text}

## FastMCP 3.0 Key Features
- Decorators return original functions (testability)
- Context injection in tools/resources/prompts
- Server composition with mount()
- Lifespan management
- Component-level authorization
- Tags for tool organization

## Migration Guide Required
1. Breaking changes checklist
2. Code transformation examples
3. New feature adoption
4. Testing strategy
5. Rollback plan"""
        }
    ]


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
