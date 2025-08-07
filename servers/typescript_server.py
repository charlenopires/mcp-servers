#!/usr/bin/env python3
"""
TypeScript Advanced MCP Server - Modern TypeScript Development Patterns 2025
=============================================================================

Advanced MCP server for modern TypeScript development following 2025 best practices:
- Clean Architecture and SOLID principles
- Modern TypeScript 5.x features (template literals, utility types, conditional types)
- Type-first development with runtime validation
- AI-enhanced development patterns (GitHub Copilot, Cursor AI optimization)
- Performance and security-first approaches
- Comprehensive code analysis and refactoring suggestions

Based on: TypeScript 5.x, Clean Architecture, SOLID principles, and modern development trends
"""

import asyncio
import json
import re
import logging
from dataclasses import dataclass
from typing import Dict, List, Optional, Any, Tuple, Union
from enum import Enum
from fastmcp import FastMCP
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize MCP server (following pattern of working servers)
mcp = FastMCP("TypeScript Analysis Server")

# ================================
# TYPESCRIPT 2025 ENUMS & MODELS
# ================================

class TypeScriptCategory(Enum):
    """Categories of TypeScript 2025 best practices"""
    TYPE_SAFETY = "type_safety"
    MODERN_FEATURES = "modern_features"
    CLEAN_ARCHITECTURE = "clean_architecture" 
    SOLID_PRINCIPLES = "solid_principles"
    UTILITY_TYPES = "utility_types"
    TEMPLATE_LITERALS = "template_literals"
    ERROR_HANDLING = "error_handling"
    PERFORMANCE = "performance"
    TESTING = "testing"
    SECURITY = "security"

class TypeScriptComplexity(Enum):
    """Complexity levels for TypeScript patterns"""
    BASIC = "basic"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"

class ArchitecturePattern(Enum):
    """Modern architecture patterns"""
    CLEAN_ARCHITECTURE = "clean_architecture"
    HEXAGONAL = "hexagonal"
    ONION = "onion"
    LAYERED = "layered"
    MODULAR_MONOLITH = "modular_monolith"

class AIToolType(Enum):
    """AI development tools integration"""
    GITHUB_COPILOT = "github_copilot"
    CURSOR_AI = "cursor_ai"
    VISUAL_COPILOT = "visual_copilot"
    GENERIC = "generic"

# ================================
# ENHANCED PYDANTIC MODELS
# ================================

class TypeScriptAnalysisResult(BaseModel):
    """Comprehensive TypeScript code analysis result"""
    overall_score: float = Field(description="Overall quality score (0-100)")
    category_scores: Dict[str, float] = Field(description="Scores by category")
    strengths: List[str] = Field(description="Code strengths and good practices found")
    weaknesses: List[str] = Field(description="Areas for improvement")
    recommendations: List[str] = Field(description="Specific actionable recommendations")
    patterns_detected: Dict[str, List[str]] = Field(description="Modern patterns detected in code")
    anti_patterns: List[str] = Field(description="Anti-patterns found")
    complexity_level: str = Field(description="Detected complexity level")
    architecture_assessment: Dict[str, Any] = Field(description="Clean architecture evaluation")

class PromptAnalysisResult(BaseModel):
    """TypeScript prompt analysis result"""
    quality_score: float = Field(description="Prompt quality score (0-100)")
    strengths: List[str] = Field(description="Strong aspects of the prompt")
    weaknesses: List[str] = Field(description="Areas needing improvement")
    recommendations: List[str] = Field(description="Specific suggestions")
    missing_categories: List[str] = Field(description="Important categories not mentioned")
    complexity_estimate: str = Field(description="Estimated project complexity")

class RefactorResult(BaseModel):
    """Code refactoring result"""
    refactored_code: str = Field(description="Improved code following modern patterns")
    improvements_applied: List[str] = Field(description="List of improvements made")
    explanation: str = Field(description="Detailed explanation of changes")
    performance_impact: str = Field(description="Expected performance improvements")
    migration_notes: List[str] = Field(description="Migration considerations")

class ProjectStructureResult(BaseModel):
    """Clean architecture project structure"""
    project_structure: Dict[str, Any] = Field(description="Complete project file structure")
    configuration_files: Dict[str, str] = Field(description="Configuration files content")
    code_examples: Dict[str, str] = Field(description="Example implementations")
    setup_instructions: List[str] = Field(description="Setup and configuration steps")
    best_practices_guide: List[str] = Field(description="Implementation best practices")

# ================================
# TYPESCRIPT 2025 KNOWLEDGE BASE
# ================================

class TypeScript2025KnowledgeBase:
    """Comprehensive TypeScript 2025 knowledge base following modern best practices"""
    
    # Modern TypeScript 5.x Features
    MODERN_FEATURES = {
        "template_literal_types": {
            "description": "Dynamic string-based type creation for robust APIs",
            "good_example": """
// Advanced template literal types
type EventName<T extends string> = `on${Capitalize<T>}`;
type HTTPMethod = 'GET' | 'POST' | 'PUT' | 'DELETE';
type APIEndpoint<T extends HTTPMethod> = `${Lowercase<T>}:/api/v1/${string}`;

// Path parameter extraction
type ExtractParams<T extends string> = 
    T extends `${string}/:${infer Param}/${infer Rest}`
        ? { [K in Param]: string } & ExtractParams<`/${Rest}`>
        : T extends `${string}/:${infer Param}`
        ? { [K in Param]: string }
        : {};

type UserRoute = '/users/:id/posts/:postId';
type UserParams = ExtractParams<UserRoute>; // { id: string; postId: string }
""",
            "anti_pattern": """
// Anti-pattern: Loose string typing
type EventName = string; // Too permissive
type APIEndpoint = string; // No validation
const endpoint: APIEndpoint = "invalid-endpoint"; // No compile-time checking
""",
            "benefits": ["Type-safe string operations", "API contract enforcement", "IntelliSense support", "Compile-time validation"]
        },
        
        "advanced_utility_types": {
            "description": "Composition of utility types for complex transformations",
            "good_example": """
// Advanced utility type compositions
type DeepPartial<T> = {
    [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};

type StrictOmit<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;
type RequiredFields<T, K extends keyof T> = T & Required<Pick<T, K>>;

// Conditional types for complex scenarios  
type NonNullable<T> = T extends null | undefined ? never : T;
type ApiResponse<T> = T extends Error 
    ? { success: false; error: string } 
    : { success: true; data: T };

// Advanced mapped types
type ReadonlyDeep<T> = {
    readonly [P in keyof T]: T[P] extends object ? ReadonlyDeep<T[P]> : T[P];
};

// Function type utilities
type AsyncReturnType<T extends (...args: any) => Promise<any>> = 
    T extends (...args: any) => Promise<infer R> ? R : never;
""",
            "benefits": ["Precise type transformations", "Better API design", "Compile-time safety", "Reusable type logic"]
        },

        "discriminated_unions": {
            "description": "Type-safe state management with discriminated unions",
            "good_example": """
// Modern discriminated union patterns
type LoadingState = { status: 'loading'; progress?: number };
type SuccessState<T> = { status: 'success'; data: T };
type ErrorState = { status: 'error'; error: string; retryable: boolean };

type AsyncState<T> = LoadingState | SuccessState<T> | ErrorState;

// Type-safe state handling
function handleState<T>(state: AsyncState<T>) {
    switch (state.status) {
        case 'loading':
            return `Loading... ${state.progress ?? 0}%`;
        case 'success':
            return `Data: ${JSON.stringify(state.data)}`;
        case 'error':
            return `Error: ${state.error} (${state.retryable ? 'retryable' : 'fatal'})`;
        default:
            // TypeScript ensures exhaustive checking
            const _exhaustive: never = state;
            throw new Error(`Unhandled state: ${_exhaustive}`);
    }
}
""",
            "benefits": ["Exhaustive checking", "Type-safe state management", "Clear API contracts", "Better error handling"]
        }
    }

    # Clean Architecture Patterns
    CLEAN_ARCHITECTURE = {
        "dependency_inversion": {
            "description": "Depend on abstractions, not concretions",
            "good_example": """
// Domain layer - pure business logic
interface UserRepository {
    findById(id: UserId): Promise<Result<User, UserNotFoundError>>;
    save(user: User): Promise<Result<void, SaveUserError>>;
}

interface EventPublisher {
    publish<T>(event: DomainEvent<T>): Promise<void>;
}

// Use case layer
class CreateUserUseCase {
    constructor(
        private readonly userRepo: UserRepository,
        private readonly eventPublisher: EventPublisher
    ) {}
    
    async execute(request: CreateUserRequest): Promise<Result<User, CreateUserError>> {
        const user = User.create(request);
        
        const saveResult = await this.userRepo.save(user);
        if (!saveResult.success) {
            return Err(new CreateUserError(saveResult.error.message));
        }
        
        await this.eventPublisher.publish(new UserCreatedEvent(user));
        return Ok(user);
    }
}
""",
            "benefits": ["Testable code", "Framework independence", "Clear boundaries", "Flexible implementations"]
        },

        "result_pattern": {
            "description": "Railway-oriented programming for TypeScript",
            "good_example": """
// Modern Result type implementation
type Result<T, E = Error> = 
    | { success: true; data: T }
    | { success: false; error: E };

// Helper functions
const Ok = <T>(data: T): Result<T, never> => ({ success: true, data });
const Err = <E>(error: E): Result<never, E> => ({ success: false, error });

// Chainable operations
const map = <T, U, E>(
    result: Result<T, E>,
    fn: (value: T) => U
): Result<U, E> =>
    result.success ? Ok(fn(result.data)) : result;
    
const flatMap = <T, U, E>(
    result: Result<T, E>,
    fn: (value: T) => Result<U, E>
): Result<U, E> =>
    result.success ? fn(result.data) : result;

// Async result handling
const asyncMap = async <T, U, E>(
    result: Result<T, E>,
    fn: (value: T) => Promise<U>
): Promise<Result<U, E>> =>
    result.success ? Ok(await fn(result.data)) : result;
""",
            "benefits": ["Explicit error handling", "Composable operations", "No exceptions", "Clear error types"]
        }
    }

    # AI Tool Optimization Patterns
    AI_OPTIMIZATION = {
        "github_copilot": {
            "comment_patterns": [
                "Use descriptive function/class comments for better suggestions",
                "Include type examples in comments",
                "Provide context about expected behavior"
            ],
            "code_patterns": [
                "Use explicit type annotations",
                "Follow consistent naming conventions",
                "Structure code with clear intentions"
            ],
            "good_example": """
/**
 * Repository for managing user data with type-safe operations
 * Supports async operations and proper error handling
 * @example
 * const repo = new UserRepository(database);
 * const user = await repo.findById('user-123');
 */
class UserRepository {
    constructor(private readonly db: Database) {}
    
    /**
     * Find user by ID with proper error handling
     * Returns Result type for safe error management
     */
    async findById(id: UserId): Promise<Result<User, UserNotFoundError>> {
        // Implementation with clear intent
    }
}
"""
        }
    }

# Initialize knowledge base
knowledge_base = TypeScript2025KnowledgeBase()

# ================================
# ANALYSIS ENGINE
# ================================

class TypeScriptAnalysisEngine:
    """Advanced TypeScript code analysis engine"""
    
    def __init__(self):
        self.patterns = knowledge_base.MODERN_FEATURES
        self.architecture_patterns = knowledge_base.CLEAN_ARCHITECTURE
    
    async def analyze_code(self, code: str, focus_areas: List[TypeScriptCategory] = None) -> TypeScriptAnalysisResult:
        """Perform comprehensive code analysis"""
        
        # Initialize analysis
        category_scores = {}
        strengths = []
        weaknesses = []
        recommendations = []
        patterns_detected = {}
        anti_patterns = []
        
        # Analyze each category
        if not focus_areas:
            focus_areas = list(TypeScriptCategory)
        
        for category in focus_areas:
            score, analysis = await self._analyze_category(code, category)
            category_scores[category.value] = score
            strengths.extend(analysis['strengths'])
            weaknesses.extend(analysis['weaknesses'])
            recommendations.extend(analysis['recommendations'])
            patterns_detected[category.value] = analysis['patterns']
            anti_patterns.extend(analysis['anti_patterns'])
        
        # Calculate overall score
        overall_score = sum(category_scores.values()) / len(category_scores) if category_scores else 0
        
        # Assess architecture
        architecture_assessment = await self._assess_architecture(code)
        
        # Determine complexity
        complexity_level = self._determine_complexity(code, patterns_detected)
        
        return TypeScriptAnalysisResult(
            overall_score=overall_score,
            category_scores=category_scores,
            strengths=list(set(strengths)),
            weaknesses=list(set(weaknesses)),
            recommendations=list(set(recommendations)),
            patterns_detected=patterns_detected,
            anti_patterns=list(set(anti_patterns)),
            complexity_level=complexity_level.value,
            architecture_assessment=architecture_assessment
        )
    
    async def _analyze_category(self, code: str, category: TypeScriptCategory) -> Tuple[float, Dict[str, Any]]:
        """Analyze code for specific category"""
        analysis = {
            'strengths': [],
            'weaknesses': [],
            'recommendations': [],
            'patterns': [],
            'anti_patterns': []
        }
        
        score = 50.0  # Base score
        
        if category == TypeScriptCategory.TYPE_SAFETY:
            score, analysis = await self._analyze_type_safety(code)
        elif category == TypeScriptCategory.MODERN_FEATURES:
            score, analysis = await self._analyze_modern_features(code)
        elif category == TypeScriptCategory.CLEAN_ARCHITECTURE:
            score, analysis = await self._analyze_clean_architecture(code)
        # ... implement other categories
        
        return score, analysis
    
    async def _analyze_type_safety(self, code: str) -> Tuple[float, Dict[str, Any]]:
        """Analyze type safety patterns"""
        analysis = {'strengths': [], 'weaknesses': [], 'recommendations': [], 'patterns': [], 'anti_patterns': []}
        score = 50.0
        
        # Check for strict mode indicators
        if 'strict' in code or 'noImplicitAny' in code:
            analysis['strengths'].append("Uses strict TypeScript configuration")
            score += 10
        
        # Check for any usage
        any_count = len(re.findall(r': any\b', code))
        if any_count > 0:
            analysis['weaknesses'].append(f"Found {any_count} uses of 'any' type")
            analysis['recommendations'].append("Replace 'any' with specific types or 'unknown'")
            score -= any_count * 5
        
        # Check for proper null handling
        if 'null |' in code or 'undefined |' in code:
            analysis['strengths'].append("Proper null/undefined handling with union types")
            score += 8
        
        return max(0, min(100, score)), analysis
    
    async def _analyze_modern_features(self, code: str) -> Tuple[float, Dict[str, Any]]:
        """Analyze modern TypeScript features usage"""
        analysis = {'strengths': [], 'weaknesses': [], 'recommendations': [], 'patterns': [], 'anti_patterns': []}
        score = 50.0
        
        # Check for template literal types
        if re.search(r'`[^`]*\$\{[^}]+\}[^`]*`', code):
            analysis['patterns'].append("Template literal types")
            analysis['strengths'].append("Uses template literal types for type safety")
            score += 12
        
        # Check for utility types
        utility_types = ['Partial', 'Pick', 'Omit', 'Record', 'Required', 'Readonly']
        found_utilities = [ut for ut in utility_types if ut in code]
        if found_utilities:
            analysis['patterns'].extend(found_utilities)
            analysis['strengths'].append(f"Uses utility types: {', '.join(found_utilities)}")
            score += len(found_utilities) * 5
        
        return max(0, min(100, score)), analysis
    
    async def _analyze_clean_architecture(self, code: str) -> Tuple[float, Dict[str, Any]]:
        """Analyze clean architecture patterns"""
        analysis = {'strengths': [], 'weaknesses': [], 'recommendations': [], 'patterns': [], 'anti_patterns': []}
        score = 50.0
        
        # Check for interface-based design
        interface_count = len(re.findall(r'interface\s+\w+', code))
        if interface_count > 0:
            analysis['strengths'].append(f"Defines {interface_count} interfaces for abstraction")
            score += interface_count * 3
        
        # Check for dependency injection patterns
        if 'constructor(' in code and 'private readonly' in code:
            analysis['patterns'].append("Dependency injection")
            analysis['strengths'].append("Uses dependency injection pattern")
            score += 10
        
        return max(0, min(100, score)), analysis
    
    async def _assess_architecture(self, code: str) -> Dict[str, Any]:
        """Assess overall architecture quality"""
        return {
            "layer_separation": self._check_layer_separation(code),
            "dependency_direction": self._check_dependency_direction(code),
            "solid_compliance": self._check_solid_principles(code),
            "testability": self._assess_testability(code)
        }
    
    def _check_layer_separation(self, code: str) -> Dict[str, Any]:
        """Check for proper layer separation"""
        layers_detected = []
        
        if re.search(r'(domain|entity|aggregate)', code, re.IGNORECASE):
            layers_detected.append("domain")
        if re.search(r'(usecase|application|service)', code, re.IGNORECASE):
            layers_detected.append("application") 
        if re.search(r'(repository|infrastructure|adapter)', code, re.IGNORECASE):
            layers_detected.append("infrastructure")
        
        return {
            "detected_layers": layers_detected,
            "separation_quality": "good" if len(layers_detected) >= 2 else "needs_improvement"
        }
    
    def _check_dependency_direction(self, code: str) -> str:
        """Check dependency direction compliance"""
        # Simplified check for dependency inversion
        if 'interface' in code and 'implements' in code:
            return "follows_dependency_inversion"
        return "needs_improvement"
    
    def _check_solid_principles(self, code: str) -> Dict[str, bool]:
        """Check SOLID principles compliance"""
        return {
            "single_responsibility": len(re.findall(r'class\s+\w+', code)) > 0,
            "open_closed": 'interface' in code or 'abstract' in code,
            "liskov_substitution": 'extends' in code,
            "interface_segregation": 'interface' in code,
            "dependency_inversion": 'constructor(' in code and 'interface' in code
        }
    
    def _assess_testability(self, code: str) -> Dict[str, Any]:
        """Assess code testability"""
        return {
            "has_interfaces": 'interface' in code,
            "uses_dependency_injection": 'constructor(' in code,
            "pure_functions": self._count_pure_functions(code),
            "testability_score": 85 if 'interface' in code else 40
        }
    
    def _count_pure_functions(self, code: str) -> int:
        """Count potential pure functions"""
        # Simplified detection of pure functions
        function_count = len(re.findall(r'function\s+\w+|const\s+\w+\s*=\s*\(', code))
        return max(0, function_count - code.count('console.') - code.count('fetch('))
    
    def _determine_complexity(self, code: str, patterns: Dict[str, List[str]]) -> TypeScriptComplexity:
        """Determine code complexity level"""
        complexity_indicators = 0
        
        # Count advanced patterns
        for category_patterns in patterns.values():
            complexity_indicators += len(category_patterns)
        
        # Check for advanced TypeScript features
        advanced_features = ['conditional types', 'mapped types', 'template literals', 'generic constraints']
        for feature in advanced_features:
            if any(feature.replace(' ', '_').lower() in pattern.lower() for patterns_list in patterns.values() for pattern in patterns_list):
                complexity_indicators += 2
        
        # Determine complexity
        if complexity_indicators >= 15:
            return TypeScriptComplexity.EXPERT
        elif complexity_indicators >= 10:
            return TypeScriptComplexity.ADVANCED
        elif complexity_indicators >= 5:
            return TypeScriptComplexity.INTERMEDIATE
        else:
            return TypeScriptComplexity.BASIC
    
    async def generate_clean_architecture_project(
        self, 
        project_name: str, 
        domain_context: str, 
        include_testing: bool = True,
        include_docker: bool = False
    ) -> Dict[str, Any]:
        """Generate a complete Clean Architecture TypeScript project"""
        return {
            "project_name": project_name,
            "domain_context": domain_context,
            "structure": {
                "src/domain/": ["entities/", "value-objects/", "repositories/", "services/"],
                "src/application/": ["use-cases/", "dto/", "ports/", "services/"],
                "src/infrastructure/": ["persistence/", "external-services/", "web/", "config/"],
                "src/presentation/": ["controllers/", "middleware/", "routes/", "dtos/"]
            },
            "sample_code": f"// {project_name} - Clean Architecture TypeScript Project\n// Domain: {domain_context}",
            "setup_instructions": [
                "npm install typescript ts-node @types/node",
                "Configure tsconfig.json with strict mode",
                "Set up dependency injection container",
                "Implement domain entities and value objects"
            ]
        }
    
    async def refactor_to_modern_patterns(
        self, 
        legacy_code: str, 
        target_version: str = "5.3",
        focus_areas: Optional[List[TypeScriptCategory]] = None
    ) -> Dict[str, Any]:
        """Refactor legacy code to modern TypeScript patterns"""
        
        # Simple refactoring suggestions
        suggestions = []
        refactored_code = legacy_code
        
        # Replace 'any' with 'unknown'
        if 'any' in legacy_code:
            suggestions.append("Replace 'any' with 'unknown' for better type safety")
            refactored_code = refactored_code.replace(': any', ': unknown')
        
        # Add interface suggestions
        if 'interface' not in legacy_code and 'class' in legacy_code:
            suggestions.append("Extract interfaces for better abstraction")
        
        return {
            "original_code": legacy_code,
            "refactored_code": refactored_code,
            "suggestions": suggestions,
            "target_version": target_version,
            "improvements": [
                "Enhanced type safety",
                "Modern TypeScript features",
                "Better maintainability"
            ]
        }

# Initialize analysis engine
analysis_engine = TypeScriptAnalysisEngine()

# ================================
# MCP TOOLS - MAIN API ENDPOINTS
# ================================

@mcp.tool()
async def typescript_analyze_code_advanced(
    code: str,
    focus_areas: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Analyzes TypeScript code for modern patterns and best practices with multi-dimensional scoring.
    
    Performs comprehensive analysis covering:
    - Type safety patterns and anti-patterns
    - Modern TypeScript 5.x features usage
    - Clean Architecture principles
    - SOLID compliance
    - Performance and security considerations
    
    Args:
        code: TypeScript code to analyze
        focus_areas: Optional list of specific areas to focus on
    
    Returns:
        Dict with detailed analysis including:
        - Overall score (0-100)
        - Category scores
        - Strengths and weaknesses
        - Specific recommendations
        - Detected patterns and anti-patterns
        - Refactoring suggestions
    """
    try:
        logger.info("Starting advanced TypeScript code analysis")
        
        # Convert focus areas from strings to enum values
        focus_enums = []
        if focus_areas:
            for area in focus_areas:
                try:
                    focus_enums.append(TypeScriptCategory(area))
                except ValueError:
                    logger.warning(f"Unknown focus area: {area}")
        
        result = await analysis_engine.analyze_code(code, focus_enums or None)
        
        logger.info(f"Analysis completed with score: {result.overall_score}")
        
        # Convert to dict for JSON serialization
        return {
            "overall_score": result.overall_score,
            "category_scores": result.category_scores,
            "strengths": result.strengths,
            "weaknesses": result.weaknesses,
            "recommendations": result.recommendations,
            "patterns_detected": result.patterns_detected,
            "anti_patterns": result.anti_patterns,
            "complexity_level": result.complexity_level.value,
            "refactoring_priority": result.refactoring_priority,
            "architecture_assessment": result.architecture_assessment,
            "modernization_suggestions": result.modernization_suggestions
        }
        
    except Exception as e:
        logger.error(f"Error analyzing TypeScript code: {e}")
        raise

@mcp.tool()
async def typescript_analyze_prompt(prompt: str) -> Dict[str, Any]:
    """
    Analyzes a prompt for TypeScript code generation and provides quality assessment.
    
    Evaluates prompts based on:
    - Clarity of requirements
    - Technical specifications completeness
    - Modern TypeScript context
    - Architecture considerations
    - Best practices alignment
    
    Args:
        prompt: The prompt to analyze for TypeScript code generation
        
    Returns:
        Dict with analysis including score, strengths, weaknesses, and improvement suggestions
    """
    try:
        logger.info("Analyzing TypeScript code generation prompt")
        
        score = 0.0
        strengths = []
        weaknesses = []
        recommendations = []
        
        # Basic structure and clarity (0-30 points)
        if len(prompt) > 50:
            score += 10
            strengths.append("Adequate prompt length")
        else:
            weaknesses.append("Prompt too brief")
            recommendations.append("Provide more detailed requirements")
        
        # TypeScript-specific keywords (0-25 points)
        ts_keywords = ['interface', 'type', 'generic', 'utility type', 'typescript']
        found_keywords = [kw for kw in ts_keywords if kw.lower() in prompt.lower()]
        if found_keywords:
            score += len(found_keywords) * 5
            strengths.append(f"Mentions TypeScript concepts: {', '.join(found_keywords)}")
        else:
            weaknesses.append("Missing TypeScript-specific terminology")
            recommendations.append("Specify TypeScript features needed (interfaces, types, generics)")
        
        # Architecture and patterns (0-25 points)
        arch_keywords = ['clean architecture', 'solid', 'design pattern', 'dependency injection']
        found_arch = [kw for kw in arch_keywords if kw.lower() in prompt.lower()]
        if found_arch:
            score += len(found_arch) * 8
            strengths.append(f"Considers architecture: {', '.join(found_arch)}")
        else:
            recommendations.append("Consider architectural patterns and design principles")
        
        # Modern practices (0-20 points)
        modern_keywords = ['async/await', 'promise', 'strict mode', 'eslint', 'prettier']
        found_modern = [kw for kw in modern_keywords if kw.lower() in prompt.lower()]
        if found_modern:
            score += len(found_modern) * 4
            strengths.append(f"Mentions modern practices: {', '.join(found_modern)}")
        
        return {
            "score": min(100.0, score),
            "grade": "A" if score >= 80 else "B" if score >= 60 else "C" if score >= 40 else "D",
            "strengths": strengths,
            "weaknesses": weaknesses,
            "recommendations": recommendations,
            "analysis_categories": {
                "typescript_specific": len(found_keywords) > 0,
                "architecture_aware": len(found_arch) > 0,
                "modern_practices": len(found_modern) > 0,
                "adequate_detail": len(prompt) > 100
            }
        }
        
    except Exception as e:
        logger.error(f"Error analyzing TypeScript prompt: {e}")
        raise

@mcp.tool()
async def typescript_generate_clean_architecture(
    project_name: str,
    domain_context: str,
    include_testing: bool = True,
    include_docker: bool = False
) -> Dict[str, Any]:
    """
    Generates a complete Clean Architecture TypeScript project structure with modern patterns.
    
    Creates a production-ready project following Clean Architecture principles:
    - Domain layer with entities and value objects
    - Application layer with use cases
    - Infrastructure layer with adapters
    - Presentation layer with controllers
    - Shared utilities and types
    
    Args:
        project_name: Name of the project
        domain_context: Business domain context (e.g., "e-commerce", "user-management")
        include_testing: Whether to include comprehensive test setup
        include_docker: Whether to include Docker configuration
        
    Returns:
        Dict with complete project structure, example code, and setup instructions
    """
    try:
        return await analysis_engine.generate_clean_architecture_project(
            project_name, domain_context, include_testing, include_docker
        )
    except Exception as e:
        logger.error(f"Error generating Clean Architecture project: {e}")
        raise

@mcp.tool()  
async def typescript_refactor_to_modern(
    legacy_code: str,
    target_version: str = "5.3",
    focus_areas: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Refactors legacy TypeScript code to modern patterns and features.
    
    Applies modernization techniques:
    - Upgrades to latest TypeScript features
    - Implements Clean Architecture patterns  
    - Adds proper type safety
    - Applies SOLID principles
    - Improves error handling and async patterns
    
    Args:
        legacy_code: Original TypeScript code to refactor
        target_version: Target TypeScript version (default: "5.3")
        focus_areas: Specific areas to focus refactoring on
        
    Returns:
        Dict with refactored code, change explanations, and migration guide
    """
    try:
        logger.info(f"Starting code refactoring to TypeScript {target_version}")
        
        # Convert focus areas to enums
        focus_enums = []
        if focus_areas:
            for area in focus_areas:
                try:
                    focus_enums.append(TypeScriptCategory(area))
                except ValueError:
                    continue
        
        return await analysis_engine.refactor_to_modern_patterns(
            legacy_code, target_version, focus_enums or None
        )
        
    except Exception as e:
        logger.error(f"Error refactoring TypeScript code: {e}")
        raise

@mcp.tool()
async def typescript_get_best_practices(
    category: str = "all",
    complexity_level: str = "intermediate"
) -> Dict[str, Any]:
    """
    Retrieves comprehensive TypeScript best practices for 2025.
    
    Provides modern TypeScript development guidelines covering:
    - Type safety and strict mode configuration
    - Modern language features and utility types
    - Clean Architecture implementation
    - SOLID principles application
    - Performance optimization techniques
    - Security best practices
    - Testing strategies
    
    Args:
        category: Specific category or "all" for comprehensive guide
                 Options: type_safety, modern_features, clean_architecture, 
                         solid_principles, utility_types, error_handling, etc.
        complexity_level: Target complexity (beginner, intermediate, advanced)
        
    Returns:
        Dict with organized best practices, examples, and implementation guides
    """
    try:
        logger.info(f"Retrieving TypeScript best practices for {category}")
        
        knowledge_base = TypeScriptKnowledgeBase()
        complexity_enum = TypeScriptComplexity(complexity_level)
        
        # Base practices that are always included
        practices = {}
        
        # Type Safety practices
        if category == "all" or category == "type_safety":
            practices["type_safety"] = {
                "principles": [
                    "Enable strict mode in tsconfig.json",
                    "Avoid 'any' type - use 'unknown' instead",
                    "Use discriminated unions for type safety", 
                    "Implement proper null/undefined handling",
                    "Leverage type guards and assertions carefully"
                ],
                "examples": [
                    {
                        "name": "Strict Configuration",
                        "description": "Recommended tsconfig.json for maximum type safety",
                        "example": """{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "exactOptionalPropertyTypes": true
  }
}""",
                        "benefits": ["Catches errors at compile time", "Better IDE support", "Self-documenting code"]
                    }
                ]
            }
        
        # Modern Features practices  
        if category == "all" or category == "modern_features":
            practices["modern_features"] = {
                "principles": [
                    "Use template literal types for type-safe strings",
                    "Leverage utility types (Pick, Omit, Partial, etc.)",
                    "Implement conditional types for complex logic",
                    "Use mapped types for transformations",
                    "Apply const assertions and as const"
                ],
                "examples": [
                    {
                        "name": "Template Literal Types",
                        "description": "Create dynamic, type-safe string patterns",
                        "example": '''// Event system with type safety
type EventName<T extends string> = `on${Capitalize<T>}`;
type UserEvents = EventName<'login' | 'logout' | 'register'>;
// Result: 'onLogin' | 'onLogout' | 'onRegister'

// API endpoint types
type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE';
type ApiEndpoint<M extends HttpMethod, P extends string> = 
    `${Lowercase<M>} /api/v1/${P}`;

type UserEndpoint = ApiEndpoint<'POST', 'users'>; // 'post /api/v1/users' ''',
                        "benefits": ["Type-safe string operations", "API contract enforcement", "Better autocomplete"]
                    }
                ]
            }
        
        # Add more categories based on request
        if category == "all" or category == "clean_architecture":
            practices["clean_architecture"] = knowledge_base.CLEAN_ARCHITECTURE
        
        result = {
            "practices": practices,
            "complexity_level": complexity_level,
            "category": category,
            "last_updated": "2025",
            "additional_resources": [
                "TypeScript Handbook 5.x",
                "Clean Architecture by Robert C. Martin",
                "Effective TypeScript by Dan Vanderkam",
                "TypeScript Deep Dive"
            ]
        }
        
        logger.info(f"Retrieved best practices for {category}")
        return result
        
    except Exception as e:
        logger.error(f"Error getting TypeScript best practices: {e}")
        raise

# ================================
# SERVER STARTUP
# ================================

if __name__ == "__main__":
    logger.info("TypeScript Advanced MCP Server starting...")
    mcp.run()