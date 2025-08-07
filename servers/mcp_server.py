#!/usr/bin/env python3
"""
MCP server for analyzing MCP server creation prompts.
This server provides tools to evaluate and give feedback on prompts
for creating MCP servers based on MCP documentation best practices.
"""

import logging
from typing import List, Dict, Any, Optional, TypedDict
from fastmcp import FastMCP
from pydantic import BaseModel, Field
import re
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("MCP Prompt Analyzer")


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


@mcp.tool()
def mcp_analyze_server_prompt(prompt: str) -> PromptAnalysis:
    """
    Analyze an MCP server creation prompt for quality and alignment with best practices.

    Args:
        prompt: The prompt text to analyze for MCP server creation

    Returns:
        AnalisePrompt: Detailed analysis with score, strengths, weaknesses and recommendations
    """
    try:
        logger.info(f"Analyzing prompt: {prompt[:100]}...")
        analysis = analyzer.analyze_prompt(prompt)
        logger.info(f"Analysis complete. Score: {analysis.score}/10")
        return analysis
    except Exception as e:
        logger.error(f"Error analyzing prompt: {e}")
        raise


@mcp.tool()
def mcp_get_best_practices() -> Dict[str, str]:
    """
    Get a summary of MCP server development best practices.

    Returns:
        Dict[str, str]: Key best practices for MCP server development
    """
    return {
        "clear_purpose": "Define a specific and focused purpose for your MCP server",
        "tool_design": "Design tools that are focused, well-documented and follow naming conventions",
        "error_handling": "Implement comprehensive error handling and input validation",
        "security": "Include input sanitization and security measures",
        "schemas": "Define clear schemas for all inputs and outputs",
        "documentation": "Provide clear documentation and usage examples",
        "testing": "Include testing and debugging strategies",
        "performance": "Consider performance and scalability requirements",
        "transport": "Choose appropriate transport protocol (stdio for local, HTTP+SSE for remote)",
        "resources": "Implement proper resource management and cleanup"
    }


@mcp.tool()
def mcp_suggest_prompt_improvements(original_prompt: str) -> Dict[str, Any]:
    """
    Suggest specific improvements for an MCP server creation prompt.

    Args:
        original_prompt: The original prompt to improve

    Returns:
        Dict containing improved prompt and explanation of changes
    """
    try:
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


@mcp.tool()
def mcp_validate_requirements(requirements: str) -> ValidationReport:
    """
    Validate MCP server requirements against best practices checklist.

    Args:
        requirements: The requirements specification to validate

    Returns:
        ValidationReport containing validation results and missing requirements
    """
    try:
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


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
