#!/usr/bin/env python3
"""
Python Development Optimizer MCP Server - Modern Python Programming Patterns 2025
==================================================================================

Advanced MCP server for optimizing Python development with comprehensive paradigm support:
- Object-Oriented Programming (OOP) with SOLID principles
- Functional Programming with immutability and composability
- Asynchronous Programming with modern async/await patterns
- Hybrid approaches combining multiple paradigms
- Clean Code principles and PEP 8 compliance
- Type safety with comprehensive type hints
- Testing strategies and performance optimization

Based on: PEP 8, Clean Code principles, Python 3.12+ features, and modern development practices
"""

import ast
import json
import logging
import re
from enum import Enum
from typing import Any

from typing import Optional

from fastmcp import FastMCP, Context
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize MCP server
mcp = FastMCP(
    name="Python Development Optimizer Server",
    instructions="""Advanced MCP server for optimizing Python development with comprehensive paradigm support.

Supported paradigms:
- Object-Oriented Programming (OOP) with SOLID principles
- Functional Programming with immutability and composability
- Asynchronous Programming with modern async/await patterns
- Hybrid approaches combining multiple paradigms

Features:
- Python prompt analysis with quality scoring
- Automatic prompt enhancement with paradigm-specific patterns
- Code validation against PEP 8 and best practices
- Template generation for all paradigms
- Refactoring suggestions with concrete examples

Use these tools for:
- analyze_python_prompt: Analyze prompts for quality and paradigm detection
- enhance_python_prompt: Transform prompts into comprehensive specifications
- validate_python_code: Validate code against PEP 8 and best practices
- generate_python_template: Generate code templates for any paradigm
- suggest_refactoring: Get refactoring suggestions with examples

Use these prompts for:
- design_python_architecture: Design module structure and architecture
- refactor_python_code: Modernize legacy Python code
- apply_paradigm: Apply specific paradigm patterns to code
- add_type_hints: Add comprehensive type annotations
- create_async_service: Create async services with proper patterns""",
    version="3.0.0"
)

# ================================
# PYTHON PARADIGMS & ENUMS
# ================================


class PythonParadigm(str, Enum):
    """Python programming paradigms"""

    OOP = "object_oriented"
    FUNCTIONAL = "functional"
    ASYNC = "asynchronous"
    HYBRID = "hybrid"


class CodeComplexity(str, Enum):
    """Code complexity levels"""

    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


class OptimizationCategory(str, Enum):
    """Categories of Python optimization"""

    CLEAN_CODE = "clean_code"
    PEP8_COMPLIANCE = "pep8_compliance"
    TYPE_SAFETY = "type_safety"
    PERFORMANCE = "performance"
    TESTING = "testing"
    SECURITY = "security"
    MAINTAINABILITY = "maintainability"


# ================================
# PYDANTIC MODELS
# ================================


class PromptAnalysis(BaseModel):
    """Model for Python prompt analysis results"""

    score: float = Field(..., ge=0, le=100, description="Overall quality score")
    paradigm_detected: PythonParadigm | None = Field(
        None, description="Detected programming paradigm"
    )
    complexity_level: CodeComplexity = Field(
        CodeComplexity.INTERMEDIATE, description="Detected complexity level"
    )
    strengths: list[str] = Field(
        default_factory=list, description="Identified strong points"
    )
    weaknesses: list[str] = Field(
        default_factory=list, description="Areas for improvement"
    )
    missing_elements: list[str] = Field(
        default_factory=list, description="Missing important elements"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Specific recommendations"
    )
    pep8_compliance: bool = Field(False, description="PEP 8 compliance mentioned")
    has_type_hints: bool = Field(False, description="Type hints mentioned")
    has_clean_code: bool = Field(False, description="Clean code principles mentioned")


class EnhancedPrompt(BaseModel):
    """Model for enhanced Python prompt"""

    original_prompt: str = Field(description="Original user prompt")
    enhanced_prompt: str = Field(description="Enhanced prompt with best practices")
    paradigm: PythonParadigm = Field(description="Target paradigm")
    added_patterns: list[str] = Field(description="Added programming patterns")
    code_template: str = Field(description="Generated code template")
    best_practices: list[str] = Field(description="Applied best practices")
    estimated_loc: int = Field(description="Estimated lines of code")


class CodeValidation(BaseModel):
    """Model for Python code validation results"""

    is_valid: bool = Field(description="Whether code is syntactically valid")
    syntax_errors: list[str] = Field(
        default_factory=list, description="Syntax errors found"
    )
    pep8_violations: list[str] = Field(
        default_factory=list, description="PEP 8 violations"
    )
    type_hint_coverage: float = Field(
        0.0, ge=0, le=100, description="Percentage of functions with type hints"
    )
    complexity_score: int = Field(0, ge=0, description="Cyclomatic complexity score")
    paradigm_adherence: dict[str, float] = Field(
        default_factory=dict, description="Paradigm adherence scores"
    )
    suggestions: list[str] = Field(
        default_factory=list, description="Improvement suggestions"
    )


class RefactoringResult(BaseModel):
    """Model for code refactoring results"""

    original_code: str = Field(description="Original code")
    refactored_code: str = Field(description="Refactored code")
    changes_made: list[str] = Field(description="List of changes applied")
    improvements: list[str] = Field(description="Improvements achieved")
    performance_impact: str = Field(description="Expected performance impact")


# ================================
# KNOWLEDGE BASE - PYTHON BEST PRACTICES 2025
# ================================

PYTHON_BEST_PRACTICES = {
    "pep8": {
        "indentation": "Use 4 spaces for indentation, never tabs",
        "line_length": "Maximum 79 characters per line (code), 72 for comments",
        "naming": "snake_case for functions/variables, PascalCase for classes, UPPER_CASE for constants",
        "imports": "Imports at top, grouped and sorted (standard, third-party, local)",
        "whitespace": "Spaces around operators, after commas, no trailing whitespace",
        "comments": "Clear and concise comments, docstrings for all functions/classes",
    },
    "clean_code": {
        "single_responsibility": "Each function/class should have a single, well-defined responsibility",
        "meaningful_names": "Use descriptive, intention-revealing names",
        "small_functions": "Keep functions small (ideally under 20 lines)",
        "no_magic_numbers": "Use named constants instead of magic numbers",
        "dry": "Don't Repeat Yourself - avoid code duplication",
        "kiss": "Keep It Simple, Stupid - prefer simplicity over cleverness",
    },
    "type_hints": {
        "parameters": "All function parameters should have type hints",
        "return_types": "Always specify return types for functions",
        "generics": "Use Generic types for reusable components",
        "optional": "Use Optional for values that can be None",
        "union": "Use Union for multiple possible types",
        "collections": "Use specific collection types (List, Dict, Set, etc.)",
    },
    "performance": {
        "list_comprehensions": "Prefer list comprehensions over explicit loops",
        "generators": "Use generators for large datasets",
        "string_concatenation": "Use join() for multiple string concatenations",
        "dictionary_lookups": "Use dictionaries for O(1) lookups instead of lists",
        "built_in_functions": "Leverage built-in functions (map, filter, reduce)",
        "caching": "Use functools.lru_cache for expensive computations",
    },
}

# SOLID Principles for OOP
SOLID_PRINCIPLES = {
    "S": {
        "name": "Single Responsibility Principle",
        "description": "A class should have only one reason to change",
        "example": "Separate UserRepository (data access) from UserValidator (business logic)",
    },
    "O": {
        "name": "Open/Closed Principle",
        "description": "Open for extension, closed for modification",
        "example": "Use protocols/interfaces to allow extension without modifying existing code",
    },
    "L": {
        "name": "Liskov Substitution Principle",
        "description": "Subclasses should be substitutable for their base classes",
        "example": "A Square should not inherit from Rectangle if it breaks expected behavior",
    },
    "I": {
        "name": "Interface Segregation Principle",
        "description": "Clients should not depend on interfaces they don't use",
        "example": "Multiple specific protocols instead of one large interface",
    },
    "D": {
        "name": "Dependency Inversion Principle",
        "description": "Depend on abstractions, not concrete implementations",
        "example": "Inject dependencies via __init__ instead of creating them inside classes",
    },
}

# Design Patterns for OOP
OOP_DESIGN_PATTERNS = {
    "creational": [
        "Factory Method",
        "Abstract Factory",
        "Singleton",
        "Builder",
        "Prototype",
    ],
    "structural": [
        "Adapter",
        "Bridge",
        "Composite",
        "Decorator",
        "Facade",
        "Flyweight",
        "Proxy",
    ],
    "behavioral": [
        "Chain of Responsibility",
        "Command",
        "Iterator",
        "Mediator",
        "Observer",
        "State",
        "Strategy",
        "Template Method",
        "Visitor",
    ],
}

# Functional Programming Concepts
FUNCTIONAL_CONCEPTS = {
    "pure_functions": "Functions without side effects that always return the same output for the same input",
    "immutability": "Data structures that cannot be modified after creation",
    "higher_order_functions": "Functions that take or return other functions",
    "map_filter_reduce": "Transform data without explicit loops using functional primitives",
    "lambda_expressions": "Anonymous functions for simple operations",
    "recursion": "Prefer recursion over loops when appropriate",
    "function_composition": "Combine simple functions to create complex functionality",
}

# Async/Await Patterns
ASYNC_PATTERNS = {
    "coroutines": "async def functions that can be paused and resumed",
    "event_loop": "Event loop that manages execution of coroutines",
    "gather": "Execute multiple coroutines concurrently with asyncio.gather()",
    "tasks": "Schedule coroutines for future execution with create_task()",
    "async_context": "Use async with for asynchronous context managers",
    "async_iteration": "Use async for for asynchronous iteration",
    "exception_handling": "Proper try/except in asynchronous code with asyncio patterns",
}

# ================================
# HELPER FUNCTIONS
# ================================


def detect_paradigm(prompt: str) -> PythonParadigm | None:
    """Detect the predominant programming paradigm in the prompt"""
    prompt_lower = prompt.lower()

    oop_keywords = [
        "class",
        "object",
        "inheritance",
        "polymorphism",
        "encapsulation",
        "method",
        "attribute",
        "property",
        "solid",
        "design pattern",
    ]
    functional_keywords = [
        "map",
        "filter",
        "reduce",
        "lambda",
        "functional",
        "immutable",
        "pure function",
        "higher order",
        "composition",
    ]
    async_keywords = [
        "async",
        "await",
        "asyncio",
        "coroutine",
        "concurrent",
        "asynchronous",
        "event loop",
        "gather",
        "task",
    ]

    oop_score = sum(1 for kw in oop_keywords if kw in prompt_lower)
    func_score = sum(1 for kw in functional_keywords if kw in prompt_lower)
    async_score = sum(1 for kw in async_keywords if kw in prompt_lower)

    max_score = max(oop_score, func_score, async_score)

    if max_score == 0:
        return None
    elif oop_score + func_score + async_score > 5:
        return PythonParadigm.HYBRID
    elif oop_score == max_score:
        return PythonParadigm.OOP
    elif func_score == max_score:
        return PythonParadigm.FUNCTIONAL
    else:
        return PythonParadigm.ASYNC


def analyze_code_complexity(code: str) -> tuple[CodeComplexity, int]:
    """Analyze code complexity using AST parsing"""
    try:
        tree = ast.parse(code)

        # Count various elements
        classes = sum(1 for node in ast.walk(tree) if isinstance(node, ast.ClassDef))
        functions = sum(
            1 for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
        )
        async_funcs = sum(
            1 for node in ast.walk(tree) if isinstance(node, ast.AsyncFunctionDef)
        )
        lambdas = sum(1 for node in ast.walk(tree) if isinstance(node, ast.Lambda))

        # Calculate approximate cyclomatic complexity
        complexity = 1  # Base complexity
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.AsyncFor)):
                complexity += 1
            elif isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1

        # Determine complexity level
        total_elements = classes + functions + async_funcs + lambdas

        if complexity < 5 and total_elements < 3:
            return CodeComplexity.BEGINNER, complexity
        elif complexity < 10 and total_elements < 10:
            return CodeComplexity.INTERMEDIATE, complexity
        elif complexity < 20 and total_elements < 20:
            return CodeComplexity.ADVANCED, complexity
        else:
            return CodeComplexity.EXPERT, complexity

    except SyntaxError:
        return CodeComplexity.BEGINNER, 0


def check_pep8_compliance(code: str) -> list[str]:
    """Check PEP 8 compliance (simplified analysis)"""
    violations = []
    lines = code.split("\n")

    for i, line in enumerate(lines, 1):
        # Line length
        if len(line) > 79:
            violations.append(f"Line {i}: Exceeds 79 characters")

        # Tabs vs spaces
        if "\t" in line:
            violations.append(f"Line {i}: Use spaces, not tabs")

        # Trailing whitespace
        if line.rstrip() != line:
            violations.append(f"Line {i}: Trailing whitespace")

        # Operators without spaces
        for op in ["==", "!=", "<=", ">=", "+", "-", "*", "/"]:
            if op in line:
                pattern = f"[^ ]{re.escape(op)}|{re.escape(op)}[^ ]"
                if re.search(pattern, line):
                    violations.append(f"Line {i}: Missing space around '{op}' operator")

    return violations


def extract_type_hint_coverage(code: str) -> float:
    """Calculate percentage of functions with type hints"""
    try:
        tree = ast.parse(code)
        total_funcs = 0
        funcs_with_hints = 0

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                total_funcs += 1
                # Check for type hints in parameters or return type
                has_param_hints = any(arg.annotation for arg in node.args.args)
                has_return_hint = node.returns is not None

                if has_param_hints or has_return_hint:
                    funcs_with_hints += 1

        if total_funcs == 0:
            return 100.0  # No functions means 100% coverage

        return (funcs_with_hints / total_funcs) * 100

    except SyntaxError:
        return 0.0


# ================================
# MCP TOOLS
# ================================


@mcp.tool(tags=["analysis", "prompt", "paradigm"])
async def analyze_python_prompt(
    prompt: str, check_paradigm: bool = True, ctx: Optional[Context] = None
) -> dict[str, Any]:
    """
    Analyze a Python code creation prompt for quality and completeness.

    Evaluates prompts based on:
    - Programming paradigm clarity
    - Best practices mentions (PEP 8, Clean Code, Type Hints)
    - Technical requirements completeness
    - Testing and documentation considerations

    Args:
        prompt: User prompt for analysis
        check_paradigm: Whether to detect programming paradigm

    Returns:
        Comprehensive analysis with score, paradigm, and improvement suggestions
    """
    logger.info(f"Analyzing Python prompt: {prompt[:100]}...")

    analysis = PromptAnalysis(
        score=0,
        paradigm_detected=None,
        complexity_level=CodeComplexity.INTERMEDIATE,
        strengths=[],
        weaknesses=[],
        missing_elements=[],
        recommendations=[],
        pep8_compliance=False,
        has_type_hints=False,
        has_clean_code=False,
    )

    prompt_lower = prompt.lower()

    # Detect programming paradigm
    if check_paradigm:
        paradigm = detect_paradigm(prompt)
        if paradigm:
            analysis.paradigm_detected = paradigm
            analysis.strengths.append(
                f"Programming paradigm clearly defined: {paradigm.value}"
            )
            analysis.score += 15
        else:
            analysis.weaknesses.append("Programming paradigm not clearly specified")
            analysis.recommendations.append(
                "Specify whether you want OOP, Functional, Async, or Hybrid approach"
            )

    # Check for best practices mentions
    if "pep8" in prompt_lower or "pep 8" in prompt_lower:
        analysis.pep8_compliance = True
        analysis.strengths.append("Mentions PEP 8 compliance")
        analysis.score += 10
    else:
        analysis.missing_elements.append("PEP 8 compliance not mentioned")
        analysis.recommendations.append("Request code following PEP 8 style guide")

    if (
        "type hint" in prompt_lower
        or "typing" in prompt_lower
        or "annotation" in prompt_lower
    ):
        analysis.has_type_hints = True
        analysis.strengths.append("Requests type hints")
        analysis.score += 10
    else:
        analysis.missing_elements.append("Type hints not mentioned")
        analysis.recommendations.append(
            "Ask for comprehensive type hints in all functions"
        )

    if "clean code" in prompt_lower:
        analysis.has_clean_code = True
        analysis.strengths.append("Mentions Clean Code principles")
        analysis.score += 10
    else:
        analysis.recommendations.append("Request code following Clean Code principles")

    # Check paradigm-specific requirements
    if analysis.paradigm_detected == PythonParadigm.OOP:
        if "solid" in prompt_lower:
            analysis.strengths.append("Mentions SOLID principles")
            analysis.score += 15
        else:
            analysis.recommendations.append(
                "For OOP, request application of SOLID principles"
            )

    if analysis.paradigm_detected == PythonParadigm.FUNCTIONAL:
        func_concepts = ["immutable", "pure function", "map", "filter", "reduce"]
        if any(concept in prompt_lower for concept in func_concepts):
            analysis.strengths.append(
                "Includes specific functional programming concepts"
            )
            analysis.score += 10
        else:
            analysis.recommendations.append(
                "Specify desired functional programming concepts"
            )

    if analysis.paradigm_detected == PythonParadigm.ASYNC:
        async_concepts = ["asyncio", "gather", "task", "concurrent"]
        if any(concept in prompt_lower for concept in async_concepts):
            analysis.strengths.append(
                "Details asynchronous implementation requirements"
            )
            analysis.score += 10
        else:
            analysis.recommendations.append("Specify desired async/await patterns")

    # Check for documentation and testing
    if "docstring" in prompt_lower or "documentation" in prompt_lower:
        analysis.strengths.append("Requests documentation")
        analysis.score += 10
    else:
        analysis.recommendations.append(
            "Ask for docstrings in all functions and classes"
        )

    if "test" in prompt_lower or "pytest" in prompt_lower or "unittest" in prompt_lower:
        analysis.strengths.append("Includes testing requirements")
        analysis.score += 15
    else:
        analysis.missing_elements.append("Testing not mentioned")
        analysis.recommendations.append("Request unit tests with pytest or unittest")

    # Check for error handling
    if "error" in prompt_lower or "exception" in prompt_lower:
        analysis.strengths.append("Mentions error handling")
        analysis.score += 10
    else:
        analysis.recommendations.append(
            "Specify appropriate error handling requirements"
        )

    # Adjust final score
    analysis.score = min(100, max(20, analysis.score))

    return {
        "analysis": analysis.model_dump(),
        "summary": f"Score: {analysis.score}/100 | "
        f"Paradigm: {analysis.paradigm_detected.value if analysis.paradigm_detected else 'Not detected'} | "
        f"PEP8: {'✅' if analysis.pep8_compliance else '❌'} | "
        f"Type Hints: {'✅' if analysis.has_type_hints else '❌'}",
    }


@mcp.tool(tags=["enhancement", "generation", "paradigm"])
async def enhance_python_prompt(
    prompt: str,
    paradigm: str | None = None,
    complexity: str = "intermediate",
    include_tests: bool = True,
    include_examples: bool = True,
    ctx: Optional[Context] = None,
) -> dict[str, Any]:
    """
    Enhance a Python prompt with best practices and modern patterns.

    Transforms basic prompts into comprehensive specifications including:
    - Programming paradigm-specific requirements
    - Clean Code and PEP 8 compliance
    - Type safety and documentation standards
    - Testing and performance considerations

    Args:
        prompt: Original prompt to enhance
        paradigm: Target paradigm (oop, functional, async, hybrid)
        complexity: Complexity level (beginner, intermediate, advanced, expert)
        include_tests: Whether to include testing requirements
        include_examples: Whether to include usage examples

    Returns:
        Enhanced prompt with templates and best practices
    """
    logger.info(f"Enhancing Python prompt for paradigm: {paradigm}")

    # Detect paradigm if not specified
    if not paradigm:
        detected = detect_paradigm(prompt)
        paradigm = detected.value if detected else "hybrid"

    paradigm_enum = PythonParadigm(paradigm)
    complexity_enum = CodeComplexity(complexity)

    # Build enhanced prompt
    enhanced_parts = [
        f"# 📋 Original Request\n{prompt}\n",
        "\n# 🎯 ENHANCED REQUIREMENTS\n",
        f"## Programming Paradigm: {paradigm_enum.value.upper()}\n",
        f"## Complexity Level: {complexity_enum.value}\n",
    ]

    # Add general requirements
    enhanced_parts.extend(
        [
            "\n## 📚 General Requirements:\n",
            "### Clean Code & PEP 8:\n",
            "- ✅ Follow PEP 8 style guide strictly (use black/flake8)\n",
            "- ✅ Use descriptive, intention-revealing names\n",
            "- ✅ Keep functions small with single responsibility\n",
            "- ✅ Avoid magic numbers - use named constants\n",
            "- ✅ Apply DRY (Don't Repeat Yourself) principle\n",
            "\n### Type Safety:\n",
            "- ✅ All function parameters with type hints\n",
            "- ✅ Specify return types for all functions\n",
            "- ✅ Use Optional, Union, List, Dict appropriately\n",
            "- ✅ Compatible with mypy --strict\n",
            "\n### Documentation:\n",
            "- ✅ Docstrings for all classes and functions\n",
            "- ✅ Use Google or NumPy docstring format\n",
            "- ✅ Include usage examples in docstrings\n",
            "- ✅ Comments only when necessary for clarity\n",
        ]
    )

    # Add paradigm-specific requirements
    code_template = ""

    if paradigm_enum == PythonParadigm.OOP:
        enhanced_parts.extend(
            [
                "\n## 🏗️ Object-Oriented Requirements:\n",
                "### SOLID Principles:\n",
                "- **S**: Single Responsibility - each class has one reason to change\n",
                "- **O**: Open/Closed - open for extension, closed for modification\n",
                "- **L**: Liskov Substitution - subclasses substitutable for base classes\n",
                "- **I**: Interface Segregation - specific interfaces over general ones\n",
                "- **D**: Dependency Inversion - depend on abstractions, not concretions\n",
                "\n### Design Patterns:\n",
                "- Use appropriate design patterns (Factory, Strategy, Observer, etc.)\n",
                "- Prefer composition over inheritance when possible\n",
                "- Implement __repr__ and __str__ for all classes\n",
                "- Use properties for getters/setters\n",
                "- Implement protocols/interfaces with ABC\n",
            ]
        )
        code_template = generate_oop_template(complexity_enum)

    elif paradigm_enum == PythonParadigm.FUNCTIONAL:
        enhanced_parts.extend(
            [
                "\n## 🧪 Functional Programming Requirements:\n",
                "### Core Concepts:\n",
                "- ✅ Pure functions without side effects\n",
                "- ✅ Immutability - don't modify existing data\n",
                "- ✅ Use map(), filter(), reduce() instead of loops\n",
                "- ✅ Lambda expressions for simple operations\n",
                "- ✅ Higher-order functions (functions that take/return functions)\n",
                "- ✅ Function composition for complex operations\n",
                "- ✅ Recursion when appropriate\n",
                "\n### Functional Patterns:\n",
                "- Use functools (partial, lru_cache, reduce)\n",
                "- Implement memoization for optimization\n",
                "- Prefer comprehensions over imperative loops\n",
                "- Use generators for large datasets\n",
            ]
        )
        code_template = generate_functional_template(complexity_enum)

    elif paradigm_enum == PythonParadigm.ASYNC:
        enhanced_parts.extend(
            [
                "\n## ⚡ Asynchronous Programming Requirements:\n",
                "### Async Patterns:\n",
                "- ✅ Use async/await appropriately\n",
                "- ✅ asyncio.gather() for concurrent execution\n",
                "- ✅ asyncio.create_task() for independent tasks\n",
                "- ✅ async with for context managers\n",
                "- ✅ async for for asynchronous iteration\n",
                "- ✅ Proper exception handling in async code\n",
                "\n### Async Best Practices:\n",
                "- Never block the event loop with synchronous I/O\n",
                "- Use asyncio.Queue for task communication\n",
                "- Implement timeouts with asyncio.wait_for()\n",
                "- Use semaphores to limit concurrency\n",
                "- Handle task cancellation gracefully\n",
            ]
        )
        code_template = generate_async_template(complexity_enum)

    else:  # HYBRID
        enhanced_parts.extend(
            [
                "\n## 🔄 Hybrid Programming Requirements:\n",
                "- Combine OOP for structure and organization\n",
                "- Apply functional concepts within methods\n",
                "- Use async/await for I/O operations\n",
                "- Maintain clear separation between paradigms\n",
            ]
        )
        code_template = generate_hybrid_template(complexity_enum)

    # Add testing requirements if requested
    if include_tests:
        enhanced_parts.extend(
            [
                "\n## 🧪 Testing Requirements:\n",
                "- ✅ Unit tests with pytest\n",
                "- ✅ Minimum 80% test coverage\n",
                "- ✅ Use fixtures for setup/teardown\n",
                "- ✅ Mock external dependencies\n",
                "- ✅ Parametrized tests when appropriate\n",
                "- ✅ pytest-asyncio for async code testing\n",
            ]
        )

    # Add performance requirements
    enhanced_parts.extend(
        [
            "\n## ⚡ Performance Considerations:\n",
            "- Use profiling to identify bottlenecks\n",
            "- Implement caching when appropriate\n",
            "- Prefer list comprehensions over explicit loops\n",
            "- Use generators for memory-efficient processing\n",
            "- Consider NumPy/Pandas for numerical operations\n",
        ]
    )

    enhanced_prompt = "".join(enhanced_parts)

    # Identify added patterns
    added_patterns = []
    if paradigm_enum == PythonParadigm.OOP:
        added_patterns = [
            "SOLID Principles",
            "Design Patterns",
            "Abstract Base Classes",
            "Properties",
        ]
    elif paradigm_enum == PythonParadigm.FUNCTIONAL:
        added_patterns = [
            "Pure Functions",
            "Immutability",
            "Higher-Order Functions",
            "Function Composition",
        ]
    elif paradigm_enum == PythonParadigm.ASYNC:
        added_patterns = ["Coroutines", "Event Loop", "Tasks", "Concurrent Execution"]
    else:
        added_patterns = ["Multi-Paradigm", "Best of All Paradigms"]

    result = EnhancedPrompt(
        original_prompt=prompt,
        enhanced_prompt=enhanced_prompt,
        paradigm=paradigm_enum,
        added_patterns=added_patterns,
        code_template=code_template,
        best_practices=[
            "PEP 8 Compliance",
            "Type Hints",
            "Clean Code Principles",
            "Comprehensive Documentation",
            "Unit Testing",
        ],
        estimated_loc=estimate_lines_of_code(complexity_enum),
    )

    return result.model_dump()


@mcp.tool(tags=["validation", "code-quality", "pep8"])
async def validate_python_code(
    code: str, check_paradigm: bool = True, strict_mode: bool = False, ctx: Optional[Context] = None
) -> dict[str, Any]:
    """
    Validate Python code against modern best practices and standards.

    Performs comprehensive analysis including:
    - Syntax validation
    - PEP 8 compliance checking
    - Type hint coverage analysis
    - Code complexity assessment
    - Programming paradigm adherence

    Args:
        code: Python code to validate
        check_paradigm: Whether to check paradigm adherence
        strict_mode: Enable strict validation mode

    Returns:
        Comprehensive validation report with suggestions
    """
    logger.info("Validating Python code against best practices")

    validation = CodeValidation(
        is_valid=True,
        syntax_errors=[],
        pep8_violations=[],
        type_hint_coverage=0.0,
        complexity_score=0,
        paradigm_adherence={},
        suggestions=[],
    )

    # Check syntax
    try:
        ast.parse(code)
    except SyntaxError as e:
        validation.is_valid = False
        validation.syntax_errors.append(f"Syntax error at line {e.lineno}: {e.msg}")
        return validation.model_dump()

    # Check PEP 8 compliance
    pep8_violations = check_pep8_compliance(code)
    validation.pep8_violations = pep8_violations

    if strict_mode and pep8_violations:
        validation.is_valid = False

    # Check type hint coverage
    type_coverage = extract_type_hint_coverage(code)
    validation.type_hint_coverage = type_coverage

    if type_coverage < 50:
        validation.suggestions.append(
            f"Low type hint coverage ({type_coverage:.1f}%). Add type hints to all functions"
        )

    # Analyze complexity
    complexity_level, complexity_score = analyze_code_complexity(code)
    validation.complexity_score = complexity_score

    if complexity_score > 10:
        validation.suggestions.append(
            f"High complexity score ({complexity_score}). Consider breaking into smaller functions"
        )

    # Check paradigm adherence if requested
    if check_paradigm:
        tree = ast.parse(code)

        # Object-Oriented Programming
        classes = sum(1 for node in ast.walk(tree) if isinstance(node, ast.ClassDef))
        if classes > 0:
            solid_score = 0
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    methods = [n for n in node.body if isinstance(n, ast.FunctionDef)]
                    # Single Responsibility (fewer methods suggest focused responsibility)
                    if len(methods) < 10:
                        solid_score += 20
                    # Check for magic methods implementation
                    if any(
                        m.name.startswith("__") and m.name.endswith("__")
                        for m in methods
                    ):
                        solid_score += 20

            validation.paradigm_adherence["oop"] = min(100, solid_score)

        # Functional Programming
        lambdas = sum(1 for node in ast.walk(tree) if isinstance(node, ast.Lambda))
        functional_patterns = (
            code.count("map(") + code.count("filter(") + code.count("reduce(")
        )

        if lambdas > 0 or functional_patterns > 0:
            func_score = min(100, (lambdas * 20) + (functional_patterns * 30))
            validation.paradigm_adherence["functional"] = func_score

        # Asynchronous Programming
        async_funcs = sum(
            1 for node in ast.walk(tree) if isinstance(node, ast.AsyncFunctionDef)
        )
        if async_funcs > 0:
            async_score = min(100, async_funcs * 25)
            validation.paradigm_adherence["async"] = async_score

    # Additional suggestions based on analysis
    if not validation.paradigm_adherence:
        validation.suggestions.append(
            "Code doesn't clearly follow any specific programming paradigm"
        )

    if "# type: ignore" in code:
        validation.suggestions.append(
            "Avoid using '# type: ignore'. Fix types appropriately instead"
        )

    if not any(
        line.strip().startswith('"""') or line.strip().startswith("'''")
        for line in code.split("\n")
    ):
        validation.suggestions.append("Add docstrings to functions and classes")

    return validation.model_dump()


@mcp.tool(tags=["generation", "template", "paradigm"])
async def generate_python_template(
    description: str,
    paradigm: str = "oop",
    include_tests: bool = True,
    include_main: bool = True,
    ctx: Optional[Context] = None,
) -> dict[str, Any]:
    """
    Generate Python code template based on description and paradigm.

    Creates production-ready code templates following best practices:
    - Paradigm-appropriate structure and patterns
    - Complete type hints and documentation
    - Testing setup and examples
    - Modern Python features and idioms

    Args:
        description: Description of what the code should do
        paradigm: Programming paradigm (oop, functional, async, hybrid)
        include_tests: Whether to include test template
        include_main: Whether to include if __name__ == "__main__" block

    Returns:
        Complete code templates with structure and examples
    """
    logger.info(f"Generating Python template for: {description[:50]}...")

    paradigm_enum = PythonParadigm(paradigm)

    templates = {"main_code": "", "test_code": "", "requirements": [], "structure": {}}

    # Generate main code based on paradigm
    if paradigm_enum == PythonParadigm.OOP:
        templates["main_code"] = generate_oop_example(description, include_main)
        templates["structure"] = {
            "classes": ["BaseClass", "ConcreteImplementation", "Factory"],
            "methods": ["__init__", "__repr__", "process", "validate"],
            "patterns": ["Factory Pattern", "Strategy Pattern", "Observer Pattern"],
        }

    elif paradigm_enum == PythonParadigm.FUNCTIONAL:
        templates["main_code"] = generate_functional_example(description, include_main)
        templates["structure"] = {
            "functions": ["pure_transform", "filter_data", "reduce_results"],
            "concepts": ["map", "filter", "reduce", "compose"],
            "utilities": ["memoize", "curry", "partial"],
        }

    elif paradigm_enum == PythonParadigm.ASYNC:
        templates["main_code"] = generate_async_example(description, include_main)
        templates["structure"] = {
            "coroutines": ["async_fetch", "async_process", "async_save"],
            "patterns": ["gather", "create_task", "Queue"],
            "utilities": ["rate_limiter", "retry", "timeout"],
        }

    else:  # HYBRID
        templates["main_code"] = generate_hybrid_example(description, include_main)
        templates["structure"] = {
            "components": [
                "AsyncDataProcessor class",
                "functional transformers",
                "async workers",
            ],
            "integration": [
                "OOP for structure",
                "FP for data processing",
                "Async for I/O",
            ],
        }

    # Generate tests if requested
    if include_tests:
        templates["test_code"] = generate_test_template(paradigm_enum)
        templates["requirements"].extend(
            ["pytest>=7.0.0", "pytest-asyncio>=0.21.0", "pytest-mock>=3.10.0"]
        )

    # Add paradigm-specific requirements
    if paradigm_enum == PythonParadigm.ASYNC:
        templates["requirements"].extend(["aiohttp>=3.9.0", "aiofiles>=23.0.0"])

    # Add common development tools
    templates["requirements"].extend(["mypy>=1.0.0", "black>=23.0.0", "flake8>=6.0.0"])

    return templates


@mcp.tool(tags=["refactoring", "optimization", "clean-code"])
async def suggest_refactoring(
    code: str,
    target_paradigm: str | None = None,
    focus_areas: list[str] | None = None,
    ctx: Optional[Context] = None,
) -> dict[str, Any]:
    """
    Suggest refactoring improvements for Python code.

    Analyzes code and provides specific refactoring suggestions:
    - Code complexity reduction
    - Design pattern applications
    - Performance optimizations
    - Paradigm-specific improvements

    Args:
        code: Current Python code to analyze
        target_paradigm: Target paradigm for refactoring
        focus_areas: Areas of focus (readability, performance, maintainability, etc.)

    Returns:
        Detailed refactoring suggestions with examples
    """
    logger.info("Analyzing code for refactoring suggestions")

    focus_areas = focus_areas or ["readability", "performance", "maintainability"]
    suggestions = []

    try:
        tree = ast.parse(code)

        # Analyze current structure
        for node in ast.walk(tree):
            # Long functions
            if isinstance(node, ast.FunctionDef):
                if len(node.body) > 20:
                    suggestions.append(
                        {
                            "type": "complexity",
                            "issue": f"Function '{node.name}' is too long ({len(node.body)} statements)",
                            "suggestion": "Break into smaller functions with single responsibilities",
                            "example": f"""
# Instead of:
def {node.name}_complex():
    # 50+ lines of code...
    
# Use:
def {node.name}_step1():
    # Isolated step 1
    
def {node.name}_step2():
    # Isolated step 2
    
def {node.name}():
    result1 = {node.name}_step1()
    return {node.name}_step2(result1)
""",
                        }
                    )

            # Classes without __init__
            if isinstance(node, ast.ClassDef):
                has_init = any(
                    isinstance(n, ast.FunctionDef) and n.name == "__init__"
                    for n in node.body
                )
                if not has_init:
                    suggestions.append(
                        {
                            "type": "oop",
                            "issue": f"Class '{node.name}' missing __init__ method",
                            "suggestion": "Add __init__ method for proper initialization",
                            "example": f"""
class {node.name}:
    def __init__(self):
        # Initialize attributes
        self._data = []
""",
                        }
                    )

        # Check for anti-patterns
        if "global " in code:
            suggestions.append(
                {
                    "type": "anti-pattern",
                    "issue": "Global variables detected",
                    "suggestion": "Pass data as parameters or use classes for state",
                    "example": """
# Instead of global:
class Config:
    def __init__(self):
        self.setting = "value"
        
config = Config()
""",
                }
            )

        # Paradigm-specific suggestions
        if target_paradigm == "functional":
            # Look for loops that could be functional
            for node in ast.walk(tree):
                if isinstance(node, ast.For):
                    suggestions.append(
                        {
                            "type": "paradigm",
                            "issue": "Imperative loop could be more functional",
                            "suggestion": "Use map/filter/reduce or comprehensions",
                            "example": """
# Instead of:
result = []
for item in items:
    if condition(item):
        result.append(transform(item))
        
# Use:
result = [transform(item) for item in items if condition(item)]
# Or:
result = list(map(transform, filter(condition, items)))
""",
                        }
                    )
                    break

        elif target_paradigm == "async":
            # Check for functions that could be async
            has_io = any(word in code for word in ["requests.", "open(", "time.sleep"])
            if has_io and "async def" not in code:
                suggestions.append(
                    {
                        "type": "paradigm",
                        "issue": "I/O operations could benefit from async/await",
                        "suggestion": "Convert to asynchronous implementation",
                        "example": """
# Instead of:
import requests
def fetch_data(url):
    return requests.get(url).json()
    
# Use:
import aiohttp
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
""",
                    }
                )

        # Performance suggestions
        if "performance" in focus_areas:
            if "+" in code and "join(" not in code:
                # Check for string concatenation in loops
                suggestions.append(
                    {
                        "type": "performance",
                        "issue": "String concatenation may be inefficient",
                        "suggestion": "Use join() for multiple concatenations",
                        "example": """
# Instead of:
result = ""
for item in items:
    result += str(item)
    
# Use:
result = "".join(str(item) for item in items)
""",
                    }
                )

    except SyntaxError as e:
        suggestions.append(
            {
                "type": "syntax",
                "issue": f"Syntax error: {e}",
                "suggestion": "Fix syntax error before refactoring",
            }
        )

    return {
        "suggestions": suggestions,
        "total_issues": len(suggestions),
        "priority_order": [
            "syntax",
            "anti-pattern",
            "complexity",
            "paradigm",
            "performance",
        ],
    }


# ================================
# TEMPLATE GENERATORS
# ================================


def generate_oop_template(complexity: CodeComplexity) -> str:
    """Generate OOP template based on complexity level"""
    if complexity == CodeComplexity.BEGINNER:
        return '''"""
Basic OOP Example - Management System
"""
from typing import List, Optional
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Entity:
    """Base entity with ID"""
    id: int
    name: str
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name='{self.name}')"


class Repository(ABC):
    """Repository interface"""
    
    @abstractmethod
    def save(self, entity: Entity) -> None:
        """Save entity"""
        pass
    
    @abstractmethod
    def find(self, id: int) -> Optional[Entity]:
        """Find entity by ID"""
        pass


class MemoryRepository(Repository):
    """In-memory repository implementation"""
    
    def __init__(self) -> None:
        self._storage: Dict[int, Entity] = {}
    
    def save(self, entity: Entity) -> None:
        self._storage[entity.id] = entity
    
    def find(self, id: int) -> Optional[Entity]:
        return self._storage.get(id)
'''
    else:
        return '''"""
Advanced OOP System with SOLID Principles
"""
from typing import Protocol, List, Optional, Generic, TypeVar
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from datetime import datetime
import logging


T = TypeVar('T')
logger = logging.getLogger(__name__)


# Interface Segregation - Multiple specific interfaces
class Readable(Protocol):
    def read(self, id: int) -> Optional[T]: ...

class Writable(Protocol):
    def write(self, item: T) -> None: ...


# Single Responsibility - Each class has one responsibility
@dataclass
class DomainEntity:
    """Base domain entity"""
    id: int
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    
    def update_timestamp(self) -> None:
        self.updated_at = datetime.now()


# Open/Closed - Open for extension via inheritance
class BaseRepository(ABC, Generic[T]):
    """Generic base repository"""
    
    @abstractmethod
    def save(self, entity: T) -> T:
        """Persist entity"""
        pass
    
    @abstractmethod
    def find_by_id(self, id: int) -> Optional[T]:
        """Find by ID"""
        pass


# Dependency Inversion - Depends on abstractions
class Service:
    """Business service"""
    
    def __init__(self, repository: BaseRepository[DomainEntity]) -> None:
        self._repository = repository  # Depends on abstraction
    
    def process(self, entity: DomainEntity) -> DomainEntity:
        """Process entity with business rules"""
        entity.update_timestamp()
        return self._repository.save(entity)
'''


def generate_functional_template(complexity: CodeComplexity) -> str:
    """Generate functional programming template"""
    if complexity == CodeComplexity.BEGINNER:
        return '''"""
Basic Functional Programming in Python
"""
from typing import List, Callable, Any
from functools import reduce


# Pure functions - no side effects
def add(x: int, y: int) -> int:
    """Add two numbers (pure function)"""
    return x + y


# Map, Filter, Reduce
def process_numbers(numbers: List[int]) -> int:
    """
    Process list of numbers functionally
    1. Filter evens
    2. Square them
    3. Sum all
    """
    # Filter - keep only evens
    evens = filter(lambda x: x % 2 == 0, numbers)
    
    # Map - square them
    squares = map(lambda x: x ** 2, evens)
    
    # Reduce - sum all
    total = reduce(add, squares, 0)
    
    return total


# Function composition
def compose(f: Callable, g: Callable) -> Callable:
    """Compose two functions: (f ∘ g)(x) = f(g(x))"""
    return lambda x: f(g(x))
'''
    else:
        return '''"""
Advanced Functional Programming in Python
"""
from typing import TypeVar, Callable, Optional, Iterable, Iterator
from functools import wraps, partial, reduce, lru_cache
from itertools import chain


T = TypeVar('T')
U = TypeVar('U')


# Memoization decorator
def memoize(func: Callable) -> Callable:
    """Decorator for result caching"""
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    wrapper.cache_clear = cache.clear
    return wrapper


# Higher-order function - Currying
def curry(func: Callable) -> Callable:
    """Transform function to curried version"""
    @wraps(func)
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return partial(func, *args, **kwargs)
    return curried


# Pipe - left-to-right composition
def pipe(*functions: Callable) -> Callable:
    """Compose functions left-to-right"""
    def piped(value):
        return reduce(lambda v, f: f(v), functions, value)
    return piped


# Maybe monad for null safety
class Maybe:
    """Maybe monad implementation"""
    
    def __init__(self, value: Optional[T]) -> None:
        self._value = value
    
    @staticmethod
    def of(value: T) -> 'Maybe[T]':
        return Maybe(value)
    
    def map(self, func: Callable[[T], U]) -> 'Maybe[U]':
        if self._value is None:
            return Maybe(None)
        return Maybe.of(func(self._value))
    
    def get_or_else(self, default: T) -> T:
        return default if self._value is None else self._value
'''


def generate_async_template(complexity: CodeComplexity) -> str:
    """Generate async/await template"""
    if complexity == CodeComplexity.BEGINNER:
        return '''"""
Basic Asynchronous Programming with asyncio
"""
import asyncio
from typing import List
import aiohttp


async def fetch_data(url: str) -> dict:
    """Fetch data from URL asynchronously"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def process_item(item: dict) -> dict:
    """Process item with simulated delay"""
    await asyncio.sleep(0.1)  # Simulate processing
    return {
        "id": item.get("id"),
        "processed": True
    }


async def main() -> None:
    """Main asynchronous function"""
    # Execute tasks concurrently
    urls = [
        "https://api.example.com/data/1",
        "https://api.example.com/data/2",
        "https://api.example.com/data/3"
    ]
    
    # Gather - execute multiple coroutines
    results = await asyncio.gather(
        *[fetch_data(url) for url in urls],
        return_exceptions=True
    )
    
    # Process results
    for result in results:
        if isinstance(result, Exception):
            print(f"Error: {result}")
        else:
            processed = await process_item(result)
            print(f"Processed: {processed}")


if __name__ == "__main__":
    asyncio.run(main())
'''
    else:
        return '''"""
Advanced Asynchronous Programming with asyncio
"""
import asyncio
from typing import TypeVar, Generic, Optional, List, AsyncIterator
from contextlib import asynccontextmanager
import aiohttp
import time
from functools import wraps


T = TypeVar('T')


# Async retry decorator
def async_retry(max_attempts: int = 3, delay: float = 1.0):
    """Decorator for async function retry"""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        await asyncio.sleep(delay * (2 ** attempt))
            raise last_exception
        return wrapper
    return decorator


# Async rate limiter
class AsyncRateLimiter:
    """Asynchronous rate limiter"""
    
    def __init__(self, rate: int, per: float) -> None:
        self.rate = rate
        self.per = per
        self.allowance = rate
        self.last_check = time.monotonic()
    
    async def acquire(self) -> None:
        """Acquire permission respecting rate limit"""
        current = time.monotonic()
        time_passed = current - self.last_check
        self.last_check = current
        self.allowance += time_passed * (self.rate / self.per)
        
        if self.allowance > self.rate:
            self.allowance = self.rate
        
        if self.allowance < 1.0:
            sleep_time = (1.0 - self.allowance) * (self.per / self.rate)
            await asyncio.sleep(sleep_time)
            self.allowance = 0.0
        else:
            self.allowance -= 1.0


# Async context manager
@asynccontextmanager
async def async_resource(name: str):
    """Async context manager for resources"""
    resource = await acquire_resource(name)
    try:
        yield resource
    finally:
        await release_resource(resource)


async def acquire_resource(name: str) -> dict:
    """Simulate resource acquisition"""
    await asyncio.sleep(0.1)
    return {"name": name, "acquired": True}


async def release_resource(resource: dict) -> None:
    """Simulate resource release"""
    await asyncio.sleep(0.1)


# Async worker pool
class AsyncWorkerPool:
    """Async worker pool with concurrency limit"""
    
    def __init__(self, max_workers: int = 10) -> None:
        self.semaphore = asyncio.Semaphore(max_workers)
        self.tasks: List[asyncio.Task] = []
    
    async def submit(self, coro, *args, **kwargs) -> asyncio.Task:
        """Submit task to pool"""
        async def wrapped():
            async with self.semaphore:
                return await coro(*args, **kwargs)
        
        task = asyncio.create_task(wrapped())
        self.tasks.append(task)
        return task
    
    async def gather(self) -> List[Any]:
        """Wait for all tasks"""
        results = await asyncio.gather(*self.tasks, return_exceptions=True)
        self.tasks.clear()
        return results


async def main() -> None:
    """Advanced async main function"""
    limiter = AsyncRateLimiter(rate=10, per=1.0)
    pool = AsyncWorkerPool(max_workers=5)
    
    # Process with async patterns
    async with async_resource("database") as resource:
        for i in range(10):
            await limiter.acquire()
            await pool.submit(process_with_resource, resource, i)
    
    results = await pool.gather()
    print(f"Processed {len(results)} items")


@async_retry(max_attempts=3)
async def process_with_resource(resource: dict, item_id: int) -> dict:
    """Process item with resource and retry"""
    await asyncio.sleep(0.1)  # Simulate work
    return {"id": item_id, "processed": True}


if __name__ == "__main__":
    asyncio.run(main())
'''


def generate_hybrid_template(complexity: CodeComplexity) -> str:
    """Generate hybrid paradigm template"""
    return '''"""
Hybrid Approach - Combining OOP, Functional, and Async
"""
from typing import TypeVar, List, Optional, Callable, AsyncIterator
from dataclasses import dataclass, field
from functools import reduce, partial
from abc import ABC, abstractmethod
import asyncio
import aiohttp
from datetime import datetime


T = TypeVar('T')


# ===== OOP: Structure and Organization =====

@dataclass
class DataItem:
    """Immutable data model (OOP + Functional)"""
    id: int
    value: str
    timestamp: datetime = field(default_factory=datetime.now)
    
    def transform(self, func: Callable[[str], str]) -> 'DataItem':
        """Return transformed copy (immutability)"""
        return DataItem(
            id=self.id,
            value=func(self.value),
            timestamp=self.timestamp
        )


class DataProcessor(ABC):
    """Processing interface (OOP)"""
    
    @abstractmethod
    async def process(self, item: DataItem) -> DataItem:
        """Process item asynchronously"""
        pass


# ===== FUNCTIONAL: Pure Transformations =====

def normalize(text: str) -> str:
    """Normalize text (pure function)"""
    return text.strip().lower()


def compose(*functions: Callable) -> Callable:
    """Compose multiple functions"""
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


# ===== ASYNC: I/O and Concurrency =====

class AsyncDataPipeline(DataProcessor):
    """Async pipeline combining paradigms"""
    
    def __init__(self, transformers: List[Callable[[str], str]]) -> None:
        self.transformers = transformers
    
    async def process(self, item: DataItem) -> DataItem:
        """Process item with functional transformations"""
        # Apply functional transformations
        transformed_value = reduce(
            lambda val, func: func(val),
            self.transformers,
            item.value
        )
        
        # Return immutable copy
        return item.transform(lambda _: transformed_value)


# ===== INTEGRATION: Combining Everything =====

class HybridService:
    """Service combining all paradigms"""
    
    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []
        self._transformers = [normalize, str.upper]
    
    async def batch_process(self, items: List[DataItem]) -> List[DataItem]:
        """Process batch with multiple paradigms"""
        
        # Functional filtering
        valid_items = filter(lambda x: len(x.value) > 0, items)
        
        # Async processing
        async def async_transform(item: DataItem) -> DataItem:
            for processor in self._processors:
                item = await processor.process(item)
            return item
        
        # Concurrent execution
        tasks = [async_transform(item) for item in valid_items]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Functional filtering of results
        return [r for r in results if not isinstance(r, Exception)]


async def main() -> None:
    """Hybrid usage demonstration"""
    items = [
        DataItem(id=i, value=f"  Item {i}  ")
        for i in range(10)
    ]
    
    # Setup pipeline
    pipeline = AsyncDataPipeline([normalize, str.upper])
    service = HybridService()
    service._processors.append(pipeline)
    
    # Process with hybrid approach
    results = await service.batch_process(items)
    
    print(f"Processed {len(results)} items")


if __name__ == "__main__":
    asyncio.run(main())
'''


def generate_oop_example(description: str, include_main: bool) -> str:
    """Generate OOP example based on description"""
    return generate_oop_template(CodeComplexity.INTERMEDIATE)


def generate_functional_example(description: str, include_main: bool) -> str:
    """Generate functional example based on description"""
    return generate_functional_template(CodeComplexity.INTERMEDIATE)


def generate_async_example(description: str, include_main: bool) -> str:
    """Generate async example based on description"""
    return generate_async_template(CodeComplexity.INTERMEDIATE)


def generate_hybrid_example(description: str, include_main: bool) -> str:
    """Generate hybrid example based on description"""
    return generate_hybrid_template(CodeComplexity.INTERMEDIATE)


def generate_test_template(paradigm: PythonParadigm) -> str:
    """Generate test template based on paradigm"""
    return f'''"""
Tests for {paradigm.value} Python code
"""
import pytest
import asyncio
from unittest.mock import Mock, AsyncMock
from typing import Any


# Fixtures
@pytest.fixture
def sample_data() -> list:
    """Sample data fixture"""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def mock_service() -> Mock:
    """Mock service fixture"""
    return Mock()


# Synchronous tests
class TestSyncCode:
    """Tests for synchronous code"""
    
    def test_pure_function(self, sample_data: list) -> None:
        """Test pure function"""
        result = process_data(sample_data)
        assert result == expected_value
        
        # Test immutability
        assert sample_data == [1, 2, 3, 4, 5]
    
    def test_with_mock(self, mock_service: Mock) -> None:
        """Test with mock"""
        mock_service.get_data.return_value = "mocked"
        
        result = function_under_test(mock_service)
        
        mock_service.get_data.assert_called_once()
        assert result == "expected"
    
    @pytest.mark.parametrize("input,expected", [
        (1, 2),
        (2, 4),
        (3, 6),
    ])
    def test_parametrized(self, input: int, expected: int) -> None:
        """Parametrized test"""
        assert double(input) == expected


# Asynchronous tests
@pytest.mark.asyncio
class TestAsyncCode:
    """Tests for asynchronous code"""
    
    async def test_async_function(self) -> None:
        """Test async function"""
        result = await async_process()
        assert result is not None
    
    async def test_with_async_mock(self) -> None:
        """Test with async mock"""
        mock = AsyncMock()
        mock.fetch.return_value = {{"data": "test"}}
        
        result = await fetch_and_process(mock)
        
        mock.fetch.assert_awaited_once()
        assert result["data"] == "test"


# Integration test
@pytest.mark.integration
async def test_full_pipeline() -> None:
    """Test complete pipeline"""
    data = create_test_data()
    result = await process_pipeline(data)
    
    assert len(result) > 0
    assert all(validate_item(item) for item in result)
'''


def estimate_lines_of_code(complexity: CodeComplexity) -> int:
    """Estimate lines of code based on complexity"""
    estimates = {
        CodeComplexity.BEGINNER: 50,
        CodeComplexity.INTERMEDIATE: 150,
        CodeComplexity.ADVANCED: 300,
        CodeComplexity.EXPERT: 500,
    }
    return estimates.get(complexity, 100)


# ================================
# RESOURCES
# ================================


@mcp.resource("python://best-practices")
async def get_best_practices() -> str:
    """Return comprehensive Python best practices guide"""
    return json.dumps(
        {
            "pep8": PYTHON_BEST_PRACTICES["pep8"],
            "clean_code": PYTHON_BEST_PRACTICES["clean_code"],
            "type_hints": PYTHON_BEST_PRACTICES["type_hints"],
            "performance": PYTHON_BEST_PRACTICES["performance"],
            "testing": {
                "framework": "pytest",
                "coverage": "minimum 80%",
                "mocking": "use unittest.mock or pytest-mock",
                "fixtures": "for reusable setup/teardown",
            },
        },
        indent=2,
    )


@mcp.resource("python://solid-principles")
async def get_solid_principles() -> str:
    """Return SOLID principles explanation"""
    return json.dumps(SOLID_PRINCIPLES, indent=2)


@mcp.resource("python://paradigms/{paradigm}")
async def get_paradigm_guide(paradigm: str) -> str:
    """Return specific paradigm guide"""
    guides = {
        "oop": {
            "principles": SOLID_PRINCIPLES,
            "patterns": OOP_DESIGN_PATTERNS,
            "best_practices": {
                "use_abc": "Use ABC for interfaces",
                "properties": "Use @property for getters/setters",
                "dunder_methods": "Implement __repr__, __str__, __eq__",
                "composition": "Prefer composition over inheritance",
            },
        },
        "functional": {
            "concepts": FUNCTIONAL_CONCEPTS,
            "functions": {
                "map": "Transform each element",
                "filter": "Filter elements by condition",
                "reduce": "Reduce to single value",
                "partial": "Partial function application",
                "compose": "Function composition",
            },
            "libraries": ["functools", "itertools", "operator"],
        },
        "async": {
            "patterns": ASYNC_PATTERNS,
            "functions": {
                "gather": "Execute multiple coroutines",
                "create_task": "Schedule coroutine",
                "wait": "Wait with timeout",
                "as_completed": "Process as they complete",
            },
            "best_practices": {
                "avoid_blocking": "Never block the event loop",
                "use_async_libs": "Use async libraries (aiohttp, aiofiles)",
                "handle_cancellation": "Handle cancellation gracefully",
            },
        },
    }

    if paradigm not in guides:
        raise ValueError(f"Paradigm '{paradigm}' not supported")

    return json.dumps(guides[paradigm], indent=2)


# ================================
# MCP PROMPTS - FastMCP 3.0
# ================================


@mcp.prompt()
async def design_python_architecture(
    project_type: str = "web_api",
    paradigm: str = "oop",
    modules: list[str] = [],
) -> list[dict[str, str]]:
    """Generate guidance for designing Python module structure and architecture."""
    modules_list = ", ".join(modules) if modules else "core, services, models, utils"
    return [
        {
            "role": "system",
            "content": """You are a Python architecture expert specializing in clean, maintainable codebases.

Your expertise includes:
- Clean Architecture and Hexagonal Architecture
- Domain-Driven Design (DDD) patterns
- SOLID principles application in Python
- Module organization and dependency management
- Configuration management (Pydantic Settings, dynaconf)
- Dependency injection patterns

Architecture principles:
- Separate concerns into layers (domain, application, infrastructure)
- Use abstractions at boundaries (protocols/ABCs)
- Keep domain logic pure and testable
- Follow the dependency rule (inner layers don't know outer layers)
- Use explicit dependencies (no hidden global state)"""
        },
        {
            "role": "user",
            "content": f"""Design Python architecture for a {project_type} project.

Target paradigm: {paradigm}
Modules to include: {modules_list}

Requirements:
1. Define clear module boundaries and responsibilities
2. Design the package/module structure
3. Identify interfaces between modules
4. Plan dependency injection strategy
5. Set up configuration management
6. Design error handling strategy

Provide:
- Complete directory structure with explanations
- Module interface definitions (protocols/ABCs)
- Dependency flow diagram
- Configuration setup
- Example code showing module interaction"""
        }
    ]


@mcp.prompt()
async def refactor_python_code(
    current_issues: list[str] = [],
    target_version: str = "3.12",
    preserve_api: bool = True,
) -> list[dict[str, str]]:
    """Generate guidance for modernizing legacy Python code to current best practices."""
    issues = ", ".join(current_issues) if current_issues else "general modernization needed"
    return [
        {
            "role": "system",
            "content": """You are a Python modernization expert helping upgrade legacy code.

Your expertise includes:
- Python 3.10+ features (match statements, type union syntax)
- Python 3.11+ features (ExceptionGroup, tomllib, Self type)
- Python 3.12+ features (type parameter syntax, f-string improvements)
- Migration from legacy patterns to modern idioms
- Type hint modernization (TypedDict, Protocol, ParamSpec)
- Async/await migration patterns

Modernization priorities:
- Replace old-style formatting with f-strings
- Add comprehensive type hints
- Use dataclasses or Pydantic models
- Replace manual context managers with contextlib
- Use pathlib instead of os.path
- Apply structural pattern matching where beneficial"""
        },
        {
            "role": "user",
            "content": f"""Refactor Python code to modern standards.

Current issues: {issues}
Target Python version: {target_version}
Preserve existing API: {preserve_api}

Requirements:
1. Identify legacy patterns needing modernization
2. Apply Python {target_version} features appropriately
3. Add comprehensive type hints
4. Improve error handling with modern patterns
5. Enhance testability
6. Maintain backward compatibility if required

Provide:
- Refactored code with detailed comments
- Migration checklist for each change
- Type hint additions explained
- Testing strategy for refactored code
- Breaking changes documentation (if any)"""
        }
    ]


@mcp.prompt()
async def apply_paradigm(
    target_paradigm: str = "oop",
    code_description: str = "",
    complexity: str = "intermediate",
) -> list[dict[str, str]]:
    """Generate guidance for applying specific programming paradigm patterns to code."""
    return [
        {
            "role": "system",
            "content": f"""You are a Python paradigm expert specializing in {target_paradigm} patterns.

Paradigm-specific expertise:

OOP (Object-Oriented):
- SOLID principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion)
- Design patterns (Factory, Strategy, Observer, Decorator, Repository)
- Proper inheritance vs composition
- Abstract base classes and protocols

Functional:
- Pure functions and immutability
- Higher-order functions and closures
- functools (reduce, partial, lru_cache)
- itertools for lazy evaluation
- Pattern matching with match/case

Async:
- asyncio event loop and tasks
- Proper async context managers
- Concurrent execution patterns (gather, wait, as_completed)
- Async generators and iterators
- Error handling in async code

Hybrid:
- Combining paradigms appropriately
- Functional core, imperative shell
- Async with OOP patterns"""
        },
        {
            "role": "user",
            "content": f"""Apply {target_paradigm} paradigm to Python code.

Code purpose: {code_description if code_description else "[Describe what the code should do]"}
Complexity level: {complexity}

Requirements:
1. Design using {target_paradigm} principles
2. Apply appropriate design patterns
3. Ensure clean, maintainable structure
4. Include comprehensive type hints
5. Add proper documentation
6. Provide testing strategy

Provide:
- Complete code implementation
- Pattern explanations
- Alternative approaches considered
- Testing examples
- Extension points for future development"""
        }
    ]


@mcp.prompt()
async def add_type_hints(
    strict_mode: bool = True,
    include_docstrings: bool = True,
    use_modern_syntax: bool = True,
) -> list[dict[str, str]]:
    """Generate guidance for adding comprehensive type annotations to Python code."""
    return [
        {
            "role": "system",
            "content": f"""You are a Python typing expert adding comprehensive type annotations.

Your expertise includes:
- Standard library types (list, dict, tuple, set with generics)
- typing module (Union, Optional, Literal, TypedDict, Protocol)
- Modern syntax (Python 3.10+ union with |, Python 3.12 type parameter syntax)
- Generic types and TypeVars
- Protocol for structural subtyping
- ParamSpec and Concatenate for decorators
- Self type for return type annotations
- Overload for multiple signatures

Type hint best practices:
- Use concrete types over Any where possible
- Prefer Protocol over ABC for duck typing
- Use TypedDict for dictionary schemas
- Apply Literal for fixed string/int values
- Use Final for constants
- Add type: ignore comments sparingly with explanation

Modern syntax (Python 3.12+):
- `def func[T](x: T) -> T:` instead of TypeVar
- `type Point = tuple[int, int]` for type aliases
- `class Container[T]:` for generic classes"""
        },
        {
            "role": "user",
            "content": f"""Add comprehensive type hints to Python code.

Configuration:
- Strict mode (no implicit Any): {strict_mode}
- Include docstrings: {include_docstrings}
- Use modern Python 3.12+ syntax: {use_modern_syntax}

Requirements:
1. Add type hints to all function signatures
2. Type all class attributes and instance variables
3. Use appropriate generic types
4. Add Protocol definitions for interfaces
5. Include TypedDict for dictionary structures
6. Handle Optional/None properly

Provide:
- Fully typed code
- Type alias definitions where helpful
- Protocol definitions for interfaces
- mypy configuration recommendations
- Explanation of complex type expressions"""
        }
    ]


@mcp.prompt()
async def create_async_service(
    service_type: str = "api_client",
    features: list[str] = [],
    use_asyncio: bool = True,
) -> list[dict[str, str]]:
    """Generate guidance for creating async services with proper patterns."""
    features_list = ", ".join(features) if features else "error handling, retries, connection pooling"
    return [
        {
            "role": "system",
            "content": """You are an async Python expert creating production-ready async services.

Your expertise includes:
- asyncio fundamentals (event loop, tasks, futures)
- Async context managers and generators
- Connection pooling (aiohttp, httpx, asyncpg)
- Proper error handling in async code
- Cancellation and timeout handling
- Structured concurrency patterns (TaskGroup in 3.11+)
- Rate limiting and backoff strategies

Async best practices:
- Use async context managers for resource management
- Implement proper cancellation handling
- Use TaskGroup for managing concurrent operations
- Handle exceptions in gather with return_exceptions
- Implement graceful shutdown
- Use asyncio.timeout for operation timeouts
- Avoid blocking calls in async code"""
        },
        {
            "role": "user",
            "content": f"""Create an async {service_type} service.

Required features: {features_list}
Use asyncio: {use_asyncio}

Requirements:
1. Implement proper async/await patterns
2. Add connection pooling if applicable
3. Include error handling with retries
4. Support cancellation and timeouts
5. Implement graceful shutdown
6. Add comprehensive type hints

Provide:
- Complete async service implementation
- Context manager for lifecycle management
- Error handling strategy
- Retry and backoff logic
- Usage examples
- Testing patterns for async code"""
        }
    ]


# ================================
# SERVER STARTUP
# ================================

if __name__ == "__main__":
    logger.info("Python Development Optimizer MCP Server starting...")
    logger.info("Supported paradigms: OOP, Functional, Async, Hybrid")
    logger.info("Features: Code analysis, prompt enhancement, template generation, refactoring")
    logger.info("New in 3.0: Context injection, MCP Prompts, Tags for discovery")
    logger.info("")
    logger.info("Available MCP Prompts:")
    logger.info("  - design_python_architecture: Design module structure and architecture")
    logger.info("  - refactor_python_code: Modernize legacy Python code")
    logger.info("  - apply_paradigm: Apply specific paradigm patterns (OOP/Functional/Async)")
    logger.info("  - add_type_hints: Add comprehensive type annotations")
    logger.info("  - create_async_service: Create async services with proper patterns")
    mcp.run()
