"""
React 19 Advanced MCP Server - MCP Server for modern React development
==============================================================================

Advanced MCP server for React 19 development, including:
- Stable Server Components
- Modern Actions and form handling
- `use` hook for async resources
- Ref as prop and performance improvements
- Concurrent rendering and transitions
- Integration with modern frameworks (Next.js 15+, Vite 6+)

Based on the latest React 19 features (December 2024) and 2025 best practices.
"""

from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass
from enum import Enum
from fastmcp import FastMCP, Context
from pydantic import BaseModel, Field
import re
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize MCP server
mcp = FastMCP(
    name="react-19-advanced",
    version="19.0.0",
    description="Advanced MCP server for React 19 development with modern features"
)


# ================================
# REACT 19 CONTEXT AND KNOWLEDGE BASE
# ================================

class ReactFeatureType(Enum):
    ACTIONS = "actions"
    SERVER_COMPONENTS = "server_components"
    USE_HOOK = "use_hook"
    FORM_HANDLING = "form_handling"
    CONCURRENT = "concurrent"
    PERFORMANCE = "performance"

class ReactFramework(Enum):
    NEXTJS = "nextjs"
    VITE = "vite"
    REMIX = "remix"
    GATSBY = "gatsby"
    CREATE_REACT_APP = "cra"

@dataclass
class PromptAnalysis:
    """Result of React prompt analysis"""
    original_prompt: str
    score: float
    strong_areas: List[str]
    weak_areas: List[str]
    suggestions: List[str]
    improved_prompt: str
    react_19_features: List[str]
    recommended_patterns: List[str]

class React19Context:
    """React 19 knowledge base and modern features"""
    
    VERSION = "19.0.0"
    RELEASE_DATE = "2024-12-05"
    
    FEATURES = {
        "actions": {
            "description": "Actions for handling async operations with form states",
            "benefits": [
                "Automatic pending states management",
                "Optimistic updates built-in", 
                "Improved error handling for async calls",
                "Better form submission patterns"
            ],
            "use_cases": ["Form submissions", "Data mutations", "Async operations"],
            "example": """
// React 19 Actions example
function SubmitForm() {
  async function submitAction(formData) {
    // Actions automatically handle pending states
    const result = await submitToServer(formData);
    return result;
  }

  return (
    <form action={submitAction}>
      <input name="email" type="email" required />
      <button type="submit">Submit</button>
    </form>
  );
}"""
        },
        "server_components": {
            "description": "Stable Server Components for server-side rendering",
            "benefits": [
                "Reduced JavaScript bundle size",
                "Faster initial page loads",
                "Better SEO performance",
                "Direct database access capabilities"
            ],
            "use_cases": ["Static content", "Data fetching", "Server-side rendering"],
            "example": """
// React 19 Server Component
async function UserProfile({ userId }) {
  // Direct database access in Server Components
  const user = await db.user.findUnique({ where: { id: userId } });
  
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}"""
        },
        "use_hook": {
            "description": "New `use` hook for consuming async resources",
            "benefits": [
                "Simplified async data fetching",
                "Better integration with Suspense",
                "Cleaner component code",
                "Promise-based resource consumption"
            ],
            "use_cases": ["Data fetching", "Resource loading", "Async operations"],
            "example": """
// React 19 use hook
import { use } from 'react';

function UserComponent({ userPromise }) {
  const user = use(userPromise);
  
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}"""
        },
        "ref_as_prop": {
            "description": "Ref as direct prop in function components",
            "benefits": [
                "No more forwardRef needed",
                "Simpler component APIs",
                "Better TypeScript support",
                "Cleaner component definitions"
            ],
            "use_cases": ["Component libraries", "Input components", "DOM access"],
            "example": """
// React 19 - Ref as prop (no forwardRef needed)
function MyInput({ ref, ...props }) {
  return <input ref={ref} {...props} />;
}

// Usage
function App() {
  const inputRef = useRef();
  return <MyInput ref={inputRef} />;
}"""
        },
        "enhanced_forms": {
            "description": "Native form improvements with Actions integration",
            "benefits": [
                "Automatic form validation",
                "Built-in loading states",
                "Better error handling",
                "Progressive enhancement support"
            ],
            "use_cases": ["Forms", "User input", "Data submission"],
            "example": """
// React 19 Enhanced Forms
function ContactForm() {
  const [error, setError] = useState(null);
  
  async function handleSubmit(formData) {
    try {
      await submitContact(formData);
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <form action={handleSubmit}>
      <input name="name" required />
      <input name="email" type="email" required />
      <textarea name="message" required />
      <button type="submit">Send Message</button>
      {error && <div className="error">{error}</div>}
    </form>
  );
}"""
        }
    }
    
    FRAMEWORKS_SUPPORT = {
        ReactFramework.NEXTJS: {
            "version": "15.0+",
            "features": ["App Router with React 19", "Server Components", "Server Actions", "Streaming"],
            "setup": "npx create-next-app@latest --typescript --tailwind"
        },
        ReactFramework.VITE: {
            "version": "6.0+", 
            "features": ["Fast HMR", "React 19 support", "TypeScript", "Plugin ecosystem"],
            "setup": "npm create vite@latest my-app -- --template react-ts"
        },
        ReactFramework.REMIX: {
            "version": "2.0+",
            "features": ["Server-side rendering", "Forms", "Data loading", "React 19 integration"],
            "setup": "npx create-remix@latest"
        }
    }

# React 19 best practices knowledge base
BEST_PRACTICES = {
    "architecture": {
        "keywords": ["componente", "component", "estrutura", "arquitetura", "organização", "structure", "architecture", "organization"],
        "practices": [
            "Use small, focused and reusable components",
            "Apply Single Responsibility Principle",
            "Organize components in modular structure",
            "Separate logic from presentation"
        ]
    },
    "typescript": {
        "keywords": ["typescript", "tipos", "types", "interface", "tipagem"],
        "practices": [
            "Define interfaces for props and state",
            "Use generic types for reusable components",
            "Apply strict mode in tsconfig.json",
            "Type event handlers correctly"
        ]
    },
    "hooks": {
        "keywords": ["hooks", "useState", "useEffect", "custom hook"],
        "practices": [
            "Prefer functional components with Hooks",
            "Create custom hooks for reusable logic",
            "Manage dependency arrays correctly",
            "Avoid unnecessary useEffect"
        ]
    },
    "performance": {
        "keywords": ["performance", "optimization", "memoization", "lazy", "virtual"],
        "practices": [
            "Implement React.memo for pure components",
            "Use useMemo and useCallback strategically",
            "Apply code splitting with React.lazy",
            "Virtualize large lists with react-window"
        ]
    },
    "state": {
        "keywords": ["estado", "state", "redux", "zustand", "context"],
        "practices": [
            "Choose appropriate state solution",
            "Avoid redundant and duplicate state",
            "Structure state in a flat way",
            "Lift state only when necessary"
        ]
    },
    "ui_ux": {
        "keywords": ["ui", "ux", "interface", "design", "responsivo", "acessibilidade", "responsive", "accessibility"],
        "practices": [
            "Implement mobile-first responsive design",
            "Ensure accessibility with ARIA labels",
            "Use consistent design systems",
            "Apply visual feedback for user actions"
        ]
    },
    "tests": {
        "keywords": ["teste", "test", "jest", "testing library"],
        "practices": [
            "Write unit tests for components",
            "Implement integration tests",
            "Use React Testing Library",
            "Maintain adequate test coverage"
        ]
    },
    "clean_code": {
        "keywords": ["clean", "limpo", "legível", "manutenível", "readable", "maintainable"],
        "practices": [
            "Follow naming conventions (PascalCase for components)",
            "Use ESLint and Prettier for consistency",
            "Document complex components",
            "Apply DRY and SOLID principles"
        ]
    }
}

# Optimized prompt templates
PROMPT_TEMPLATES = {
    "basic_component": """
Create a React component with TypeScript following these specifications:

**Functional Requirements:**
{functional_requirements}

**Technical Requirements:**
- TypeScript with explicit types for props and state
- Functional component using modern Hooks
- Follow naming conventions (PascalCase for component, camelCase for functions)
- Implement appropriate error handling
- Add JSDoc comments for props

**Structure and Organization:**
- Organize in its own folder with test file
- Separate types/interfaces in separate file if complex
- Use barrel exports (index.ts) for clean exports

**Performance:**
- Apply React.memo if component is pure
- Use useMemo/useCallback where appropriate
- Implement lazy loading if applicable

**UI/UX and Accessibility:**
- Mobile-first responsive design
- Include appropriate ARIA attributes
- Implement keyboard navigation
- Provide visual feedback for states (loading, error, success)

**Code Quality:**
- Follow SOLID and DRY principles
- Clean and self-explanatory code
- ESLint/Prettier configuration applied
""",

    "complete_application": """
Develop a complete React application with TypeScript including:

**Architecture and Structure:**
- Scalable and modular folder structure
- Clear separation of concerns (components, hooks, utils, types)
- Routing configuration with React Router
- Tooling setup (ESLint, Prettier, Husky)

**State Management:**
- Implement appropriate solution (Context API, Zustand, or Redux Toolkit)
- Well-defined local vs global state
- Avoid prop drilling
- Structured state without redundancies

**Components and Reusability:**
- Reusable component library
- Consistent design system
- Compound components for complex UI
- Custom hooks for shared logic

**Performance and Optimization:**
- Code splitting by routes
- Lazy loading of heavy components
- Virtualization for large lists
- Re-render optimization

**UI/UX Excellence:**
- Implemented design system
- Light/dark theme
- Smooth animations and transitions
- Intuitive interaction patterns

**Accessibility (a11y):**
- WCAG AA level compliance
- Complete keyboard navigation
- Screen reader support
- Adequate color contrast

**Testing and Quality:**
- Unit tests with Jest and React Testing Library
- Integration tests for critical flows
- CI/CD configuration
- Comprehensive documentation
"""
}


def analyze_covered_areas(prompt: str) -> Dict[str, bool]:
    """Analyzes which best practices areas the prompt covers"""
    covered_areas = {}
    prompt_lower = prompt.lower()

    for area, info in BEST_PRACTICES.items():
        # Check if any keyword from the area is present
        is_covered = any(keyword in prompt_lower for keyword in info["keywords"])
        covered_areas[area] = is_covered

    return covered_areas


def calculate_score(covered_areas: Dict[str, bool]) -> float:
    """Calculates score based on covered areas"""
    total_areas = len(covered_areas)
    covered_areas_count = sum(covered_areas.values())

    # Base score
    score = (covered_areas_count / total_areas) * 100

    # Bonus for critical areas
    critical_areas = ["typescript", "performance",
                      "clean_code", "architecture"]
    bonus = sum(10 for area in critical_areas if covered_areas.get(area, False))

    return min(100, score + bonus)


def generate_suggestions(covered_areas: Dict[str, bool]) -> List[str]:
    """Generates suggestions based on uncovered areas"""
    suggestions = []

    for area, is_covered in covered_areas.items():
        if not is_covered:
            info = BEST_PRACTICES[area]
            suggestion = f"Add requirements about {area.replace('_', ' ')}: "
            suggestion += ", ".join(info["practices"][:2])
            suggestions.append(suggestion)

    return suggestions


def improve_prompt(original_prompt: str, covered_areas: Dict[str, bool]) -> str:
    """Improves the prompt by adding missing aspects"""
    improved_prompt = original_prompt.strip()

    # Add missing sections
    sections_to_add = []

    if not covered_areas.get("typescript"):
        sections_to_add.append("""
**TypeScript Requirements:**
- Use TypeScript with explicit types for all props, state and functions
- Define clear interfaces for data structures
- Configure strict mode in tsconfig.json""")

    if not covered_areas.get("performance"):
        sections_to_add.append("""
**Performance Optimization:**
- Implement memoization where appropriate (React.memo, useMemo, useCallback)
- Use lazy loading for non-critical components
- Consider virtualization for large lists""")

    if not covered_areas.get("ui_ux"):
        sections_to_add.append("""
**UI/UX and Accessibility:**
- Responsive design that works well on mobile and desktop
- Implement accessibility following WCAG standards
- Provide clear visual feedback for all interactions""")

    if not covered_areas.get("clean_code"):
        sections_to_add.append("""
**Code Quality:**
- Follow React naming conventions (PascalCase for components)
- Configure ESLint and Prettier
- Write clean and self-explanatory code with comments where necessary""")

    if sections_to_add:
        improved_prompt += "\n\n" + "\n".join(sections_to_add)

    return improved_prompt


@mcp.tool()
async def react19_analyze_prompt(prompt: str) -> PromptAnalysis:
    """
    Analyzes a React code creation prompt and provides detailed feedback

    Args:
        prompt: The prompt to be analyzed

    Returns:
        Complete analysis with score, strengths/weaknesses and suggestions
    """
    # Analyze covered areas
    covered_areas = analyze_covered_areas(prompt)

    # Calculate score
    score = calculate_score(covered_areas)

    # Identify strong areas
    strong_areas = [
        area.replace('_', ' ').title()
        for area, is_covered in covered_areas.items()
        if is_covered
    ]

    # Identify weak areas
    weak_areas = [
        area.replace('_', ' ').title()
        for area, is_covered in covered_areas.items()
        if not is_covered
    ]

    # Generate suggestions
    suggestions = generate_suggestions(covered_areas)

    # Improve prompt
    improved_prompt = improve_prompt(prompt, covered_areas)

    return PromptAnalysis(
        original_prompt=prompt,
        score=score,
        strong_areas=strong_areas,
        weak_areas=weak_areas,
        suggestions=suggestions,
        improved_prompt=improved_prompt,
        react_19_features=[],
        recommended_patterns=[]
    )


@mcp.tool()
async def react19_get_prompt_template(template_type: str = "basic_component") -> Dict[str, str]:
    """
    Gets an optimized prompt template for React

    Args:
        template_type: Template type ('basic_component' or 'complete_application')

    Returns:
        Prompt template with optimized structure
    """
    template = PROMPT_TEMPLATES.get(
        template_type, PROMPT_TEMPLATES["basic_component"])

    return {
        "type": template_type,
        "template": template,
        "instructions": "Replace {functional_requirements} with your project's specific requirements"
    }


@mcp.tool()
async def react19_suggest_contextual_improvements(
    prompt: str,
    context: str = "component"
) -> Dict[str, Any]:
    """
    Suggests specific improvements based on development context

    Args:
        prompt: Original prompt
        context: Development type ('component', 'hook', 'application', 'library')

    Returns:
        Contextualized suggestions and improved prompt
    """
    improvements_by_context = {
        "component": [
            "Specify if the component should be controlled or uncontrolled",
            "Clearly define required and optional props",
            "Include specific accessibility requirements",
            "Mention if it should support refs (forwardRef)"
        ],
        "hook": [
            "Clearly define the hook's return type",
            "Specify if the hook should be synchronous or asynchronous",
            "Include cleanup/unmount handling",
            "Mention if it should have internal memoization"
        ],
        "application": [
            "Specify the desired routing strategy",
            "Define authentication/authorization requirements",
            "Include internationalization needs",
            "Mention PWA requirements if applicable"
        ],
        "library": [
            "Clearly define the public API",
            "Specify React version compatibility",
            "Include tree-shaking requirements",
            "Mention if it should support SSR"
        ]
    }

    improvements = improvements_by_context.get(
        context, improvements_by_context["component"])

    # Add improvements to prompt
    improved_prompt = prompt + "\n\n**Additional Requirements:**\n"
    improved_prompt += "\n".join(f"- {improvement}" for improvement in improvements)

    return {
        "context": context,
        "suggested_improvements": improvements,
        "improved_prompt": improved_prompt
    }


@mcp.tool()
async def react19_validate_requirements(requirements: str) -> Dict[str, Any]:
    """
    Validates if requirements include essential aspects for React development

    Args:
        requirements: String with project requirements

    Returns:
        Detailed validation with checklist and missing requirements
    """
    checklist = {
        "typescript_typing": bool(re.search(r"typescript|tipos?|types?|interface", requirements, re.I)),
        "state_management": bool(re.search(r"estado|state|redux|context|zustand", requirements, re.I)),
        "functional_components": bool(re.search(r"funcional|functional|hooks?", requirements, re.I)),
        "performance": bool(re.search(r"performance|otimiza|memo|lazy", requirements, re.I)),
        "accessibility": bool(re.search(r"acessib|a11y|aria|wcag", requirements, re.I)),
        "responsiveness": bool(re.search(r"responsiv|mobile|breakpoint", requirements, re.I)),
        "testing": bool(re.search(r"test|jest|testing.library", requirements, re.I)),
        "folder_structure": bool(re.search(r"estrutura|folder|organiza|arquitetura", requirements, re.I)),
        "clean_code": bool(re.search(r"clean|limpo|eslint|prettier", requirements, re.I)),
        "error_handling": bool(re.search(r"erro|error|exception|boundary", requirements, re.I))
    }

    missing_requirements = [
        req.replace('_', ' ').title()
        for req, is_present in checklist.items()
        if not is_present
    ]

    complete_validation = all(checklist.values())
    coverage_percentage = (sum(checklist.values()) / len(checklist)) * 100

    recommendations = []
    if not checklist["typescript_typing"]:
        recommendations.append(
            "Add explicit requirements about using TypeScript with well-defined types")
    if not checklist["accessibility"]:
        recommendations.append(
            "Include accessibility requirements following WCAG standards")
    if not checklist["performance"]:
        recommendations.append(
            "Specify performance and optimization requirements")

    return {
        "complete_validation": complete_validation,
        "coverage_percentage": coverage_percentage,
        "checklist": checklist,
        "missing_requirements": missing_requirements,
        "recommendations": recommendations
    }


@mcp.tool()
async def react19_generate_optimized_prompt(
    project_description: str,
    project_type: str = "component",
    detail_level: str = "complete"
) -> str:
    """
    Generates a complete optimized prompt based on project description

    Args:
        project_description: Basic description of what needs to be developed
        project_type: Project type ('component', 'application', 'library')
        detail_level: Desired detail level ('basic', 'intermediate', 'complete')

    Returns:
        Optimized and structured prompt
    """
    # Base prompt
    prompt = f"Develop {project_description} using React with TypeScript.\n\n"

    # Add sections based on detail level
    if detail_level in ["intermediate", "complete"]:
        prompt += """**Architecture and Structure:**
- Small, focused and reusable components
- Single Responsibility Principle
- Modular and scalable folder structure
- Clear separation between logic and presentation

"""

    prompt += """**TypeScript and Typing:**
- Explicit types for all props, state and function returns
- Well-defined interfaces for data structures
- Use of generics for reusable components
- Strict mode enabled

"""

    if project_type == "application":
        prompt += """**State Management:**
- Appropriate choice between Context API, Zustand or Redux Toolkit
- Structured state without redundancies
- Clear separation between local and global state
- Avoid prop drilling

"""

    prompt += """**Performance and Optimization:**
- Strategic memoization with React.memo, useMemo and useCallback
- Code splitting and lazy loading where appropriate
- Virtualization for large lists
- Analysis and prevention of unnecessary re-renders

"""

    if detail_level == "complete":
        prompt += """**UI/UX and Design:**
- Mobile-first responsive design
- Consistent design system
- Visual feedback for all interactions
- Smooth and non-intrusive animations
- Light/dark mode if applicable

**Accessibility (a11y):**
- WCAG AA level compliance
- Complete keyboard navigation
- Appropriate ARIA labels
- Screen reader support
- Adequate color contrast

**Code Quality:**
- React naming conventions (PascalCase, camelCase)
- ESLint and Prettier configured
- SOLID and DRY principles applied
- Clean and self-explanatory code
- JSDoc documentation for public components

**Testing:**
- Unit tests for components and hooks
- Integration tests for main flows
- Use of React Testing Library
- Minimum 80% coverage

"""

    prompt += f"\n**Specific Requirements:**\n{project_description}"

    return prompt

# Configuração de recursos do servidor


@mcp.tool()
async def react19_get_server_resources() -> Dict[str, Any]:
    """
    Returns information about the resources available in this MCP server

    Returns:
        Dictionary with description of resources and how to use them
    """
    return {
        "name": "React Prompt Enhancer MCP",
        "version": "1.0.0",
        "description": "MCP server for enhancing React/TypeScript development prompts",
        "available_tools": {
            "analyze_react_prompt": "Analyzes and scores a prompt, providing improvement suggestions",
            "get_prompt_template": "Provides optimized templates for different project types",
            "suggest_contextual_improvements": "Suggests specific improvements based on context",
            "validate_react_requirements": "Validates if requirements cover essential aspects",
            "generate_optimized_prompt": "Generates a complete and optimized prompt from a description"
        },
        "covered_best_practices": list(BEST_PRACTICES.keys()),
        "usage_example": {
            "1_analysis": "Use 'analyze_react_prompt' to evaluate your current prompt",
            "2_improvement": "Apply the provided suggestions",
            "3_validation": "Use 'validate_react_requirements' to ensure complete coverage",
            "4_optimization": "Use 'generate_optimized_prompt' to create structured prompts"
        }
    }

if __name__ == "__main__":
    mcp.run()
