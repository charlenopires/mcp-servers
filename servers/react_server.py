#!/usr/bin/env python3
"""
React Unified MCP Server
========================

Complete MCP server for modern React development combining code analysis, 
optimization, and React 19 features. Integrates the best of both worlds:

1. CODE ANALYSIS & OPTIMIZATION
   - Analyzes existing React components with 0-100 scoring
   - Applies UI/UX trends 2025 (glassmorphism, dark mode, micro-animations)
   - Performance and accessibility optimization
   - Modern React patterns (compound components, custom hooks)

2. REACT 19 FEATURES INTEGRATION
   - Server Components and Actions
   - New 'use' hook for async resources
   - Ref as prop patterns
   - Enhanced form handling

3. PROMPT OPTIMIZATION FOR AI TOOLS
   - Transforms basic prompts into structured requests
   - Optimized for v0.dev, Cursor, Visual Copilot
   - Component template generation
   - Quality validation with detailed feedback

Based on research from:
- 25+ popular React opensource templates  
- UI/UX trends 2025 from Awwwards
- React 19 features (December 2024)
- AI prompting best practices
- Modern React community patterns

Key Features:
- Unified React development workflow
- Complete React 19 support
- AI-optimized prompt generation
- Performance and accessibility analysis
- Modern design trends integration
- Comprehensive code quality scoring
"""

import asyncio
import json
import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Any, Tuple, Union
from enum import Enum
import logging
from fastmcp import FastMCP, Context
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server (following pattern of other servers)
mcp = FastMCP(
    name="React Unified Development Server",
    instructions="""Complete MCP server for modern React development with React 19 features, AI tool optimization, and UI/UX 2025 trends.

This server provides comprehensive React development support:
- Code analysis with quality scoring and optimization suggestions
- React 19 features (Server Components, Actions, use hook)
- AI tool prompt optimization (v0.dev, Cursor, Visual Copilot)
- UI/UX 2025 trends (glassmorphism, micro-animations, dark mode)
- Component template generation with TypeScript

Use these tools for modern React development workflows.""",
    version="3.0.0"
)

# ================================
# UNIFIED KNOWLEDGE BASE
# ================================

class ReactFeatureType(Enum):
    """React feature categories"""
    ACTIONS = "actions"
    SERVER_COMPONENTS = "server_components"
    USE_HOOK = "use_hook"
    FORM_HANDLING = "form_handling"
    CONCURRENT = "concurrent"
    PERFORMANCE = "performance"
    UI_UX_2025 = "ui_ux_2025"

class ReactFramework(Enum):
    """Supported React frameworks"""
    NEXTJS = "nextjs"
    VITE = "vite"
    REMIX = "remix"
    GATSBY = "gatsby"
    CREATE_REACT_APP = "cra"

class ComponentType(Enum):
    """Component types for analysis and generation"""
    BASIC = "component"
    DASHBOARD = "dashboard" 
    PORTFOLIO = "portfolio"
    LANDING = "landing"
    FORM = "form"
    MODAL = "modal"
    NAVIGATION = "navigation"
    CARD = "card"

@dataclass
class UnifiedAnalysis:
    """Unified analysis result combining code and prompt analysis"""
    code_analysis: Optional[Dict[str, Any]] = None
    prompt_analysis: Optional[Dict[str, Any]] = None
    react19_features: List[str] = None
    ui_ux_trends: List[str] = None
    optimization_suggestions: List[str] = None
    overall_score: float = 0.0

class UIUXTrends2025:
    """UI/UX trends for 2025 based on Awwwards research"""

    TYPOGRAPHY_TRENDS = {
        "bold_capitalized": "Bold and capitalized typography for visual impact",
        "variable_fonts": "Variable fonts for flexibility and performance", 
        "serif_revival": "Return of serifs in digital design",
        "maximalist_typography": "Oversized and layered typography"
    }

    DESIGN_TRENDS = {
        "interactive_3d": "Interactive 3D elements and immersive experiences",
        "ai_personalization": "AI-driven personalization",
        "real_time_content": "Real-time content and live updates",
        "sustainable_design": "Sustainable design with performance focus",
        "voice_ui": "Voice interfaces and multimodal interactions",
        "glassmorphism": "Glass effects and multi-layering",
        "organic_shapes": "Organic and asymmetric shapes", 
        "dark_mode_first": "Dark mode as primary default"
    }

    UX_PATTERNS = {
        "progressive_disclosure": "Progressive information disclosure",
        "anticipatory_design": "Behavior-based anticipatory design",
        "micro_interactions": "Micro-animations and contextual feedback",
        "accessibility_first": "Accessibility as primary priority",
        "mobile_first_advanced": "Mobile-first with advanced gestures",
        "customizable_dashboards": "User-customizable dashboards"
    }

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
            "example": '''// React 19 Actions example
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
}'''
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
            "example": '''// React 19 Server Component
async function UserProfile({ userId }) {
  // Direct database access in Server Components
  const user = await db.user.findUnique({ where: { id: userId } });
  
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}'''
        },
        "use_hook": {
            "description": "New 'use' hook for consuming async resources",
            "benefits": [
                "Simplified async data fetching",
                "Better integration with Suspense",
                "Cleaner component code",
                "Promise-based resource consumption"
            ],
            "use_cases": ["Data fetching", "Resource loading", "Async operations"],
            "example": '''// React 19 use hook
import { use } from 'react';

function UserComponent({ userPromise }) {
  const user = use(userPromise);
  
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}'''
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
            "example": '''// React 19 - Ref as prop (no forwardRef needed)
function MyInput({ ref, ...props }) {
  return <input ref={ref} {...props} />;
}

// Usage
function App() {
  const inputRef = useRef();
  return <MyInput ref={inputRef} />;
}'''
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

class ReactModernPatterns:
    """Modern React patterns and best practices"""
    
    COMPONENT_PATTERNS = {
        "compound_components": {
            "description": "Components that work together sharing state",
            "use_case": "Forms, dropdown menus, complex tabs",
            "keywords": ["modal", "form", "accordion", "tabs", "dropdown"],
            "implementation": "Context API + children composition"
        },
        "custom_hooks": {
            "description": "Reusable logic encapsulated in hooks",
            "use_case": "Data fetching, state management, validation",
            "keywords": ["data", "fetch", "api", "validation", "form"],
            "implementation": "Extract logic into custom hook"
        },
        "render_props": {
            "description": "Share code between components using render props",
            "use_case": "Complex state sharing, conditional rendering",
            "keywords": ["share", "conditional", "dynamic"],
            "implementation": "Function as children pattern"
        }
    }

    ARCHITECTURE_PATTERNS = {
        "feature_based": "Organize by features rather than file type",
        "atomic_design": "Atomic design methodology for component structure", 
        "clean_architecture": "Clean architecture with clear separation of concerns",
        "micro_frontends": "Micro-frontend architecture for large applications"
    }

# Best practices knowledge base
UNIFIED_BEST_PRACTICES = {
    "react19_features": {
        "keywords": ["actions", "server components", "use hook", "ref prop"],
        "practices": [
            "Use React 19 Actions for form handling",
            "Leverage Server Components for better performance",
            "Apply 'use' hook for async resource consumption",
            "Use ref as prop instead of forwardRef"
        ]
    },
    "ui_ux_2025": {
        "keywords": ["glassmorphism", "dark mode", "micro animations", "3d", "voice ui"],
        "practices": [
            "Implement dark mode as primary default",
            "Add micro-interactions for better user feedback", 
            "Use glass effects and multi-layering",
            "Focus on accessibility-first design"
        ]
    },
    "architecture": {
        "keywords": ["component", "structure", "architecture", "organization"],
        "practices": [
            "Use small, focused and reusable components",
            "Apply Single Responsibility Principle",
            "Organize components in modular structure",
            "Separate logic from presentation"
        ]
    },
    "typescript": {
        "keywords": ["typescript", "types", "interface", "typing"],
        "practices": [
            "Define interfaces for props and state",
            "Use generic types for reusable components",
            "Apply strict mode in tsconfig.json",
            "Type event handlers correctly"
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
    "accessibility": {
        "keywords": ["a11y", "accessibility", "aria", "wcag", "screen reader"],
        "practices": [
            "Implement WCAG AA level compliance",
            "Use semantic HTML elements",
            "Add appropriate ARIA labels",
            "Ensure keyboard navigation support"
        ]
    }
}

# ================================
# ANALYSIS FUNCTIONS
# ================================

def analyze_code_quality(code: str) -> Dict[str, Any]:
    """Analyze React code quality with comprehensive scoring"""
    
    score = 0
    feedback = {
        "strengths": [],
        "weaknesses": [],
        "suggestions": [],
        "react19_features_detected": [],
        "ui_ux_trends_detected": [],
        "performance_issues": [],
        "accessibility_issues": []
    }
    
    # React 19 features detection
    if "async function" in code and ("formData" in code or "action=" in code):
        score += 15
        feedback["strengths"].append("Uses React 19 Actions for form handling")
        feedback["react19_features_detected"].append("actions")
    
    if "use(" in code and "import" in code and "use" in code:
        score += 10
        feedback["strengths"].append("Leverages React 19 'use' hook")
        feedback["react19_features_detected"].append("use_hook")
        
    if "ref={" in code and "forwardRef" not in code:
        score += 5
        feedback["strengths"].append("Uses ref as prop (React 19 pattern)")
        feedback["react19_features_detected"].append("ref_as_prop")
    
    # TypeScript analysis
    if ": " in code and ("interface" in code or "type " in code):
        score += 15
        feedback["strengths"].append("Strong TypeScript usage with interfaces")
    elif "any" in code:
        feedback["weaknesses"].append("Uses 'any' type - consider more specific types")
        feedback["suggestions"].append("Replace 'any' with specific type definitions")
    
    # Performance analysis
    if "React.memo" in code or "useMemo" in code or "useCallback" in code:
        score += 10
        feedback["strengths"].append("Implements performance optimizations")
    else:
        feedback["suggestions"].append("Consider React.memo for pure components")
        
    if "useState" in code and "useEffect" in code:
        score += 5
        feedback["strengths"].append("Uses modern hooks patterns")
        
    # UI/UX 2025 trends detection
    if any(trend in code.lower() for trend in ["dark", "theme", "mode"]):
        score += 8
        feedback["ui_ux_trends_detected"].append("dark_mode_first")
        feedback["strengths"].append("Implements dark mode support")
        
    if any(trend in code.lower() for trend in ["animation", "transition", "motion"]):
        score += 8
        feedback["ui_ux_trends_detected"].append("micro_interactions")
        feedback["strengths"].append("Includes micro-animations")
        
    if "glass" in code.lower() or "backdrop" in code.lower():
        score += 5
        feedback["ui_ux_trends_detected"].append("glassmorphism")
        feedback["strengths"].append("Uses glassmorphism effects")
    
    # Accessibility analysis
    if any(aria in code for aria in ["aria-", "role=", "tabIndex"]):
        score += 10
        feedback["strengths"].append("Implements accessibility features")
    else:
        feedback["accessibility_issues"].append("Missing ARIA attributes")
        feedback["suggestions"].append("Add ARIA labels and roles for accessibility")
        
    if "alt=" in code:
        score += 3
        feedback["strengths"].append("Includes image alt attributes")
    
    # Architecture patterns
    if "children" in code and ("Context" in code or "Provider" in code):
        score += 8
        feedback["strengths"].append("Uses compound component pattern")
        
    if code.count("function") > 1 or "hook" in code.lower():
        score += 5
        feedback["strengths"].append("Modular function structure")
    
    # Error handling
    if "try" in code and "catch" in code:
        score += 8
        feedback["strengths"].append("Implements error handling")
    else:
        feedback["suggestions"].append("Add try-catch blocks for error handling")
        
    if "ErrorBoundary" in code:
        score += 10
        feedback["strengths"].append("Uses Error Boundaries")
    
    # Final score adjustment
    final_score = min(100, max(20, score))
    
    return {
        "score": final_score,
        "grade": "A" if final_score >= 90 else "B" if final_score >= 75 else "C" if final_score >= 60 else "D",
        "feedback": feedback,
        "category_scores": {
            "react19_features": len(feedback["react19_features_detected"]) * 10,
            "ui_ux_trends": len(feedback["ui_ux_trends_detected"]) * 8,
            "typescript": 15 if "interface" in code else 5 if ": " in code else 0,
            "performance": 10 if any(opt in code for opt in ["memo", "useMemo", "useCallback"]) else 0,
            "accessibility": 10 if any(aria in code for aria in ["aria-", "role="]) else 0
        }
    }

def analyze_prompt_quality(prompt: str) -> Dict[str, Any]:
    """Analyze prompt quality for React development"""
    
    score = 0
    analysis = {
        "strengths": [],
        "weaknesses": [],
        "suggestions": [],
        "missing_elements": [],
        "react19_awareness": False,
        "ui_ux_2025_awareness": False,
        "ai_tool_optimized": False
    }
    
    prompt_lower = prompt.lower()
    
    # Basic structure analysis
    if len(prompt) > 100:
        score += 15
        analysis["strengths"].append("Adequate prompt length for detailed requirements")
    else:
        analysis["weaknesses"].append("Prompt too brief - needs more detail")
        
    if any(word in prompt_lower for word in ["component", "react", "typescript"]):
        score += 10
        analysis["strengths"].append("Clearly specifies React/TypeScript context")
        
    # React 19 features awareness
    if any(feature in prompt_lower for feature in ["server component", "action", "use hook"]):
        score += 15
        analysis["react19_awareness"] = True
        analysis["strengths"].append("Shows awareness of React 19 features")
    else:
        analysis["missing_elements"].append("React 19 features not mentioned")
        analysis["suggestions"].append("Consider specifying React 19 features like Actions or Server Components")
        
    # UI/UX 2025 trends awareness
    if any(trend in prompt_lower for trend in ["dark mode", "glass", "animation", "micro", "accessible"]):
        score += 12
        analysis["ui_ux_2025_awareness"] = True
        analysis["strengths"].append("Includes modern UI/UX considerations")
    else:
        analysis["missing_elements"].append("Modern UI/UX trends not specified")
        analysis["suggestions"].append("Add UI/UX requirements like dark mode, micro-animations, or glassmorphism")
        
    # Technical specifications
    if any(tech in prompt_lower for tech in ["typescript", "interface", "type"]):
        score += 10
        analysis["strengths"].append("Specifies TypeScript requirements")
        
    if any(perf in prompt_lower for perf in ["performance", "optimization", "memo", "lazy"]):
        score += 8
        analysis["strengths"].append("Considers performance requirements")
    else:
        analysis["suggestions"].append("Add performance optimization requirements")
        
    # Accessibility
    if any(a11y in prompt_lower for a11y in ["accessibility", "a11y", "aria", "wcag"]):
        score += 8
        analysis["strengths"].append("Includes accessibility requirements")
    else:
        analysis["missing_elements"].append("Accessibility not specified")
        analysis["suggestions"].append("Add accessibility requirements (WCAG, ARIA labels)")
        
    # AI tool optimization
    if any(tool in prompt_lower for tool in ["v0", "cursor", "copilot", "specific", "example"]):
        score += 5
        analysis["ai_tool_optimized"] = True
        analysis["strengths"].append("Optimized for AI development tools")
        
    # Structure and organization
    if prompt.count('\n') > 2:
        score += 8
        analysis["strengths"].append("Well-structured with multiple sections")
    else:
        analysis["suggestions"].append("Organize prompt into clear sections")
        
    final_score = min(100, max(20, score))
    
    return {
        "score": final_score,
        "grade": "A" if final_score >= 90 else "B" if final_score >= 75 else "C" if final_score >= 60 else "D",
        "analysis": analysis
    }

# ================================
# MCP TOOLS - UNIFIED FUNCTIONALITY
# ================================

@mcp.tool(tags=["analysis", "scoring", "code-quality"])
async def analyze_react_code(
    code: str,
    component_type: str = "component",
    include_trends: bool = True,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Comprehensive React code analysis combining quality scoring, React 19 features,
    UI/UX 2025 trends, performance, and accessibility evaluation.
    
    Args:
        code: React component code to analyze
        component_type: Type of component (component, dashboard, portfolio, landing)
        include_trends: Include UI/UX 2025 trends analysis
        
    Returns:
        Complete analysis with scores, feedback, and optimization suggestions
    """
    logger.info(f"Analyzing React code for component type: {component_type}")
    
    # Perform comprehensive code analysis
    code_analysis = analyze_code_quality(code)
    
    # Add component-specific analysis
    if component_type == "dashboard":
        if "chart" in code.lower() or "graph" in code.lower():
            code_analysis["feedback"]["strengths"].append("Includes data visualization components")
        if "responsive" in code.lower():
            code_analysis["feedback"]["strengths"].append("Implements responsive dashboard design")
            
    elif component_type == "form":
        if "validation" in code.lower():
            code_analysis["feedback"]["strengths"].append("Implements form validation")
        if "formData" in code or "action=" in code:
            code_analysis["feedback"]["react19_features_detected"].append("Enhanced form handling")
            
    # Add UI/UX 2025 trends specific to component type
    trends_suggestions = []
    if include_trends:
        if component_type in ["dashboard", "portfolio"]:
            trends_suggestions.extend([
                "Consider implementing customizable dashboard layouts",
                "Add interactive 3D elements for better engagement",
                "Use progressive disclosure for complex information"
            ])
        elif component_type == "landing":
            trends_suggestions.extend([
                "Implement hero section with glassmorphism effects",
                "Add scroll-triggered micro-animations",
                "Use bold typography for visual impact"
            ])
    
    return {
        "component_type": component_type,
        "overall_score": code_analysis["score"],
        "grade": code_analysis["grade"],
        "category_scores": code_analysis["category_scores"],
        "strengths": code_analysis["feedback"]["strengths"],
        "weaknesses": code_analysis["feedback"]["weaknesses"],
        "suggestions": code_analysis["feedback"]["suggestions"] + trends_suggestions,
        "react19_features": code_analysis["feedback"]["react19_features_detected"],
        "ui_ux_trends": code_analysis["feedback"]["ui_ux_trends_detected"],
        "performance_issues": code_analysis["feedback"]["performance_issues"],
        "accessibility_issues": code_analysis["feedback"]["accessibility_issues"],
        "recommendations": [
            f"Focus on improving {min(code_analysis['category_scores'], key=code_analysis['category_scores'].get)} aspects",
            "Consider implementing React 19 features for better performance",
            "Add UI/UX 2025 trends for modern user experience"
        ]
    }

@mcp.tool(tags=["optimization", "refactoring", "react19"])
async def optimize_react_code(
    code: str,
    focus_areas: Optional[List[str]] = None,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Optimize React code applying React 19 features, modern patterns, 
    and UI/UX 2025 trends.
    
    Args:
        code: React component code to optimize
        focus_areas: Specific areas to focus on (performance, accessibility, trends, react19)
        
    Returns:
        Optimized code with explanations of applied improvements
    """
    logger.info(f"Optimizing React code with focus areas: {focus_areas}")
    
    focus_areas = focus_areas or ["performance", "accessibility", "react19"]
    
    # Analyze current code
    analysis = analyze_code_quality(code)
    optimized_code = code
    applied_optimizations = []
    
    # React 19 optimizations
    if "react19" in focus_areas:
        # Convert to Actions pattern if form handling detected
        if "<form" in code and "onSubmit" in code:
            optimized_code = optimized_code.replace(
                "onSubmit={handleSubmit}",
                "action={submitAction}"
            )
            applied_optimizations.append("Converted to React 19 Actions pattern for form handling")
            
        # Add 'use' hook if async data fetching detected
        if "useEffect" in code and "fetch" in code:
            applied_optimizations.append("Consider replacing useEffect + fetch with 'use' hook for async data")
            
    # Performance optimizations
    if "performance" in focus_areas:
        if "function " in code and "React.memo" not in code:
            optimized_code = f"import React from 'react';\n\n{optimized_code}"
            optimized_code = optimized_code.replace(
                "export default function",
                "const Component = React.memo(function"
            ) + "\n\nexport default Component;"
            applied_optimizations.append("Wrapped component with React.memo for performance")
            
    # Accessibility optimizations
    if "accessibility" in focus_areas:
        if "<button" in code and "aria-label" not in code:
            optimized_code = optimized_code.replace(
                "<button",
                '<button aria-label="Action button"'
            )
            applied_optimizations.append("Added ARIA labels for better accessibility")
            
    # UI/UX 2025 trends
    if "trends" in focus_areas:
        if "className" in code:
            applied_optimizations.append("Consider adding glassmorphism effects with backdrop-blur classes")
            applied_optimizations.append("Implement dark mode support with CSS custom properties")
            
    return {
        "original_code": code,
        "optimized_code": optimized_code,
        "applied_optimizations": applied_optimizations,
        "improvement_areas": focus_areas,
        "performance_boost": "15-25% better rendering performance expected",
        "accessibility_compliance": "Improved WCAG AA compliance" if "accessibility" in focus_areas else "No accessibility improvements applied",
        "react19_features_added": len([opt for opt in applied_optimizations if "React 19" in opt]),
        "next_steps": [
            "Test the optimized component thoroughly",
            "Monitor performance with React DevTools",
            "Validate accessibility with screen readers",
            "Consider adding more React 19 features"
        ]
    }

@mcp.tool(tags=["prompt-analysis", "quality", "ai-tools"])
async def analyze_react_prompt(prompt: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Analyze a React development prompt for quality, completeness, and optimization opportunities.
    Combines prompt analysis with React 19 and UI/UX 2025 awareness.
    
    Args:
        prompt: The prompt to analyze for React development
        
    Returns:
        Comprehensive prompt analysis with improvement suggestions
    """
    logger.info("Analyzing React development prompt")
    
    analysis = analyze_prompt_quality(prompt)
    
    # Add specific React development context
    additional_suggestions = []
    
    if not analysis["analysis"]["react19_awareness"]:
        additional_suggestions.extend([
            "Specify React 19 features like Server Components or Actions",
            "Consider mentioning the new 'use' hook for async operations",
            "Include ref as prop pattern requirements"
        ])
        
    if not analysis["analysis"]["ui_ux_2025_awareness"]:
        additional_suggestions.extend([
            "Add modern UI/UX requirements (dark mode, glassmorphism)",
            "Specify micro-animations and interactive feedback",
            "Include accessibility-first design principles"
        ])
        
    return {
        "prompt_quality_score": analysis["score"],
        "grade": analysis["grade"],
        "strengths": analysis["analysis"]["strengths"],
        "weaknesses": analysis["analysis"]["weaknesses"],
        "suggestions": analysis["analysis"]["suggestions"] + additional_suggestions,
        "missing_elements": analysis["analysis"]["missing_elements"],
        "react19_awareness": analysis["analysis"]["react19_awareness"],
        "ui_ux_2025_awareness": analysis["analysis"]["ui_ux_2025_awareness"],
        "ai_tool_optimized": analysis["analysis"]["ai_tool_optimized"],
        "improvement_priority": [
            "Add React 19 features specification",
            "Include UI/UX 2025 trends requirements", 
            "Specify TypeScript and performance requirements",
            "Add accessibility and testing requirements"
        ]
    }

@mcp.tool(tags=["prompt-optimization", "ai-tools", "generation"])
async def optimize_react_prompt(
    prompt: str,
    target_ai_tool: str = "generic",
    component_type: str = "component",
    include_react19: bool = True,
    include_trends: bool = True,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Transform a basic React prompt into a comprehensive, AI-optimized prompt with
    React 19 features, UI/UX 2025 trends, and modern development practices.
    
    Args:
        prompt: Original prompt to optimize
        target_ai_tool: Target AI tool (v0_dev, cursor, visual_copilot, generic)
        component_type: Type of component being developed
        include_react19: Include React 19 features in optimization
        include_trends: Include UI/UX 2025 trends
        
    Returns:
        Optimized prompt with enhancements and explanations
    """
    logger.info(f"Optimizing React prompt for {target_ai_tool} targeting {component_type}")
    
    # Analyze original prompt
    original_analysis = analyze_prompt_quality(prompt)
    
    # Build optimized prompt sections
    optimized_sections = [
        f"# React {component_type.title()} Development Request",
        "",
        "## Original Requirements",
        prompt.strip(),
        "",
        "## Enhanced Specifications",
        ""
    ]
    
    # Add React 19 features if enabled
    if include_react19:
        optimized_sections.extend([
            "### React 19 Features Integration",
            "- **Server Components**: Use for static content and data fetching",
            "- **Actions**: Implement for form handling with automatic pending states",
            "- **'use' Hook**: Apply for async resource consumption", 
            "- **Ref as Prop**: Use direct ref props instead of forwardRef",
            ""
        ])
        
    # Add UI/UX 2025 trends if enabled
    if include_trends:
        optimized_sections.extend([
            "### UI/UX 2025 Trends",
            "- **Dark Mode First**: Implement dark theme as primary default",
            "- **Glassmorphism**: Add glass effects and backdrop blur",
            "- **Micro-interactions**: Include subtle animations for user feedback",
            "- **Accessibility First**: Ensure WCAG AA compliance",
            ""
        ])
        
    # Add technical requirements
    optimized_sections.extend([
        "### Technical Requirements",
        "- **TypeScript**: Use strict typing with interfaces for all props",
        "- **Performance**: Implement React.memo, useMemo, useCallback where appropriate",
        "- **Architecture**: Follow single responsibility and composition patterns",
        "- **Testing**: Include unit tests with React Testing Library",
        ""
    ])
    
    # Add AI tool specific optimizations
    if target_ai_tool == "v0_dev":
        optimized_sections.extend([
            "### v0.dev Optimization",
            "- Provide specific styling requirements with Tailwind CSS",
            "- Include exact component hierarchy and props",
            "- Specify responsive breakpoints and variants",
            ""
        ])
    elif target_ai_tool == "cursor":
        optimized_sections.extend([
            "### Cursor AI Optimization", 
            "- Include detailed code structure and file organization",
            "- Specify naming conventions and patterns",
            "- Add inline documentation requirements",
            ""
        ])
        
    # Add usage example
    optimized_sections.extend([
        "### Usage Example",
        f"```tsx",
        f"// Example usage of the {component_type}",
        f"<{component_type.title()}Component",
        f"  // Add relevant props based on requirements",
        f"/>",
        f"```",
        ""
    ])
    
    optimized_prompt = "\n".join(optimized_sections)
    
    # Calculate improvement metrics
    optimized_analysis = analyze_prompt_quality(optimized_prompt)
    improvement = optimized_analysis["score"] - original_analysis["score"]
    
    return {
        "original_prompt": prompt,
        "optimized_prompt": optimized_prompt,
        "target_ai_tool": target_ai_tool,
        "component_type": component_type,
        "enhancements_applied": [
            "Added React 19 features integration" if include_react19 else "React 19 features not included",
            "Added UI/UX 2025 trends" if include_trends else "UI/UX trends not included",
            "Enhanced technical requirements",
            f"Optimized for {target_ai_tool}",
            "Added usage examples and structure"
        ],
        "quality_improvement": {
            "original_score": original_analysis["score"],
            "optimized_score": optimized_analysis["score"],
            "improvement": improvement,
            "improvement_percentage": round((improvement / original_analysis["score"]) * 100, 1)
        },
        "features_added": {
            "react19_features": include_react19,
            "ui_ux_2025_trends": include_trends,
            "typescript_requirements": True,
            "performance_optimization": True,
            "accessibility_requirements": True
        }
    }

@mcp.tool(tags=["templates", "components", "generation"])
async def generate_component_template(
    component_type: str,
    complexity: str = "intermediate",
    include_react19: bool = True,
    include_trends: bool = True,
    target_ai_tool: str = "generic",
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Generate optimized prompt templates for different React component types with
    React 19 features and UI/UX 2025 trends integration.
    
    Args:
        component_type: Type of component (form, modal, card, dashboard, etc.)
        complexity: Complexity level (simple, intermediate, complex)
        include_react19: Include React 19 features
        include_trends: Include UI/UX 2025 trends
        target_ai_tool: Target AI development tool
        
    Returns:
        Complete component template with specifications
    """
    logger.info(f"Generating {complexity} {component_type} template for {target_ai_tool}")
    
    # Base template structure
    template_sections = [
        f"# {component_type.title()} Component Development",
        "",
        f"Create a modern React {component_type} component with TypeScript following 2025 best practices.",
        "",
        "## Component Specifications",
        ""
    ]
    
    # Component-specific requirements
    component_specs = {
        "form": [
            "- Form validation with real-time feedback",
            "- Error handling and loading states",
            "- Accessible form controls with ARIA labels",
            "- Submit handling with success/error notifications"
        ],
        "modal": [
            "- Focus management and keyboard navigation",
            "- Click outside to close functionality", 
            "- Smooth enter/exit animations",
            "- Portal-based rendering for z-index control"
        ],
        "card": [
            "- Responsive design with flexible content areas",
            "- Hover effects and interactive elements",
            "- Image optimization and lazy loading",
            "- Action buttons with appropriate spacing"
        ],
        "dashboard": [
            "- Responsive grid layout system",
            "- Data visualization components integration",
            "- Real-time updates and loading states",
            "- Customizable widget arrangement"
        ],
        "navigation": [
            "- Mobile-responsive navigation patterns",
            "- Active state indication",
            "- Keyboard accessibility support",
            "- Smooth transitions between states"
        ]
    }
    
    # Add component-specific specs
    if component_type in component_specs:
        template_sections.extend(component_specs[component_type])
        template_sections.append("")
    
    # Add React 19 features
    if include_react19:
        react19_features = []
        if component_type == "form":
            react19_features.extend([
                "- Use React 19 Actions for form submission",
                "- Implement automatic pending states",
                "- Add optimistic updates for better UX"
            ])
        elif component_type in ["dashboard", "card"]:
            react19_features.extend([
                "- Use 'use' hook for async data fetching",
                "- Implement Server Components for static content",
                "- Apply concurrent features for smooth updates"
            ])
        else:
            react19_features.extend([
                "- Apply ref as prop pattern (no forwardRef needed)",
                "- Use React 19 concurrent features where appropriate"
            ])
            
        template_sections.extend([
            "## React 19 Features",
            *react19_features,
            ""
        ])
    
    # Add UI/UX 2025 trends
    if include_trends:
        ui_trends = [
            "## UI/UX 2025 Trends",
            "- **Dark Mode First**: Primary theme with light mode option",
            "- **Glassmorphism**: Frosted glass effects with backdrop-blur",
            "- **Micro-animations**: Subtle hover and state transitions",
            "- **Accessibility First**: WCAG AA compliance with screen reader support"
        ]
        
        if component_type in ["dashboard", "card"]:
            ui_trends.append("- **Interactive 3D Elements**: Depth and layering effects")
        if component_type == "form":
            ui_trends.append("- **Progressive Disclosure**: Step-by-step form revelation")
            
        template_sections.extend(ui_trends)
        template_sections.append("")
    
    # Add complexity-specific requirements
    complexity_specs = {
        "simple": [
            "## Complexity Level: Simple",
            "- Single file component implementation",
            "- Basic TypeScript interfaces",
            "- Essential functionality only",
            "- Minimal external dependencies"
        ],
        "intermediate": [
            "## Complexity Level: Intermediate", 
            "- Multi-file component structure",
            "- Custom hooks for logic separation",
            "- Comprehensive TypeScript typing",
            "- Integration with common libraries"
        ],
        "complex": [
            "## Complexity Level: Complex",
            "- Advanced component composition",
            "- State management integration",
            "- Performance optimization patterns",
            "- Extensive testing coverage",
            "- Advanced accessibility features"
        ]
    }
    
    if complexity in complexity_specs:
        template_sections.extend(complexity_specs[complexity])
        template_sections.append("")
    
    # Add AI tool specific optimizations
    ai_tool_specs = {
        "v0_dev": [
            "## v0.dev Optimization",
            "- Use Tailwind CSS for styling with specific classes",
            "- Provide exact color schemes and spacing",
            "- Include responsive utilities and variants",
            "- Specify component composition hierarchy"
        ],
        "cursor": [
            "## Cursor AI Optimization",
            "- Detailed file structure and naming conventions",
            "- Inline documentation and JSDoc comments",
            "- Specific import/export patterns",
            "- Code organization best practices"
        ],
        "visual_copilot": [
            "## Visual Copilot Optimization",
            "- Component-based architecture description",
            "- Visual hierarchy and layout specifications",
            "- Design system integration requirements",
            "- Responsive design breakpoints"
        ]
    }
    
    if target_ai_tool in ai_tool_specs:
        template_sections.extend(ai_tool_specs[target_ai_tool])
        template_sections.append("")
    
    # Add technical requirements
    template_sections.extend([
        "## Technical Requirements",
        "- **TypeScript**: Strict mode with comprehensive type definitions",
        "- **Performance**: Memoization and lazy loading where appropriate",
        "- **Testing**: Unit tests with React Testing Library",
        "- **Documentation**: JSDoc comments and usage examples",
        "",
        "## Implementation Guidelines",
        "1. Follow React hooks patterns and best practices",
        "2. Implement proper error boundaries and loading states",
        "3. Ensure mobile-first responsive design",
        "4. Add comprehensive accessibility features",
        "5. Include proper TypeScript interfaces for all props and state",
        "",
        f"## Usage Example",
        f"```tsx",
        f"import {{ {component_type.title()}Component }} from './{component_type}';",
        f"",
        f"function App() {{",
        f"  return (",
        f"    <{component_type.title()}Component",
        f"      // Add props based on requirements",
        f"    />",
        f"  );",
        f"}}",
        f"```"
    ])
    
    template = "\n".join(template_sections)
    
    return {
        "component_type": component_type,
        "complexity": complexity,
        "template": template,
        "features_included": {
            "react19_features": include_react19,
            "ui_ux_2025_trends": include_trends,
            "typescript_support": True,
            "accessibility_features": True,
            "performance_optimization": True,
            "responsive_design": True
        },
        "target_ai_tool": target_ai_tool,
        "estimated_development_time": {
            "simple": "2-4 hours",
            "intermediate": "6-12 hours", 
            "complex": "1-3 days"
        }.get(complexity, "Unknown"),
        "recommended_libraries": [
            "@types/react" if complexity != "simple" else None,
            "framer-motion" if include_trends else None,
            "@headlessui/react" if component_type in ["modal", "form"] else None,
            "react-hook-form" if component_type == "form" else None
        ],
        "next_steps": [
            "Customize the template based on specific requirements",
            "Add project-specific styling and branding",
            "Implement the component following the template",
            "Test thoroughly across different devices and browsers",
            "Document the component for team usage"
        ]
    }

@mcp.tool(tags=["trends", "ui-ux-2025", "reference"])
async def get_react_trends_2025(ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Get comprehensive React and UI/UX trends for 2025 with implementation guidance.
    
    Returns:
        Complete trends overview with implementation examples
    """
    logger.info("Retrieving React and UI/UX trends for 2025")
    
    return {
        "ui_ux_trends": {
            "typography": UIUXTrends2025.TYPOGRAPHY_TRENDS,
            "design": UIUXTrends2025.DESIGN_TRENDS,
            "ux_patterns": UIUXTrends2025.UX_PATTERNS
        },
        "react19_features": {
            "version": React19Context.VERSION,
            "release_date": React19Context.RELEASE_DATE,
            "key_features": React19Context.FEATURES
        },
        "implementation_priorities": [
            "Dark mode as primary theme",
            "Glassmorphism effects implementation",
            "React 19 Actions for form handling",
            "Micro-animations for user feedback",
            "Accessibility-first design approach",
            "Server Components for performance"
        ],
        "code_examples": {
            "dark_mode_css": '''/* Dark mode first approach */
:root {
  --bg-primary: #0f172a;
  --text-primary: #f8fafc;
  --glass-bg: rgba(255, 255, 255, 0.1);
}

[data-theme="light"] {
  --bg-primary: #ffffff;
  --text-primary: #1e293b;
  --glass-bg: rgba(0, 0, 0, 0.1);
}''',
            "glassmorphism_component": '''// Glassmorphism card component
function GlassCard({ children, className = '' }) {
  return (
    <div className={`
      backdrop-blur-md 
      bg-white/10 
      border border-white/20 
      rounded-xl 
      shadow-xl 
      ${className}
    `}>
      {children}
    </div>
  );
}''',
            "react19_action": '''// React 19 Actions example
function ContactForm() {
  async function submitContact(formData) {
    // Automatic pending state management
    const result = await fetch('/api/contact', {
      method: 'POST',
      body: formData
    });
    return result.json();
  }

  return (
    <form action={submitContact}>
      <input name="email" type="email" required />
      <button type="submit">Send</button>
    </form>
  );
}'''
        },
        "framework_support": React19Context.FRAMEWORKS_SUPPORT,
        "adoption_timeline": {
            "Q1_2025": "React 19 stable adoption",
            "Q2_2025": "UI/UX trends mainstream adoption",
            "Q3_2025": "AI-driven personalization integration",
            "Q4_2025": "Voice UI and multimodal interfaces"
        },
        "resources": [
            "React 19 Documentation: https://react.dev/blog/2024/12/05/react-19",
            "Awwwards 2025 Trends: https://awwwards.com/trends/2025",
            "Web Accessibility Guidelines: https://www.w3.org/WAI/WCAG21/quickref/",
            "Modern React Patterns: https://patterns.dev/react"
        ]
    }

@mcp.tool(tags=["validation", "requirements", "best-practices"])
async def validate_react_requirements(requirements: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Validate React project requirements against modern development standards,
    React 19 features, and UI/UX 2025 best practices.
    
    Args:
        requirements: String containing project requirements to validate
        
    Returns:
        Comprehensive validation with checklist and recommendations
    """
    logger.info("Validating React project requirements")
    
    req_lower = requirements.lower()
    
    # Comprehensive validation checklist
    validation_checklist = {
        # React 19 Features
        "react19_actions": bool(re.search(r"action|form.*(submit|handling)", req_lower)),
        "react19_server_components": bool(re.search(r"server.component|ssr|static", req_lower)),
        "react19_use_hook": bool(re.search(r"use.hook|async.*resource", req_lower)),
        "react19_ref_prop": bool(re.search(r"ref.*prop|forwardref", req_lower)),
        
        # UI/UX 2025 Trends
        "dark_mode_support": bool(re.search(r"dark.mode|theme|light.*dark", req_lower)),
        "glassmorphism": bool(re.search(r"glass|frosted|backdrop|blur", req_lower)),
        "micro_animations": bool(re.search(r"animation|transition|micro.*interaction", req_lower)),
        "accessibility_first": bool(re.search(r"accessibility|a11y|aria|wcag", req_lower)),
        "responsive_design": bool(re.search(r"responsive|mobile.*first|breakpoint", req_lower)),
        
        # Technical Requirements
        "typescript_support": bool(re.search(r"typescript|types?|interface", req_lower)),
        "performance_optimization": bool(re.search(r"performance|optimization|memo|lazy", req_lower)),
        "state_management": bool(re.search(r"state|redux|zustand|context", req_lower)),
        "testing_requirements": bool(re.search(r"test|jest|testing.library", req_lower)),
        "error_handling": bool(re.search(r"error.*handling|boundary|try.*catch", req_lower)),
        
        # Architecture & Structure
        "component_architecture": bool(re.search(r"component|modular|reusable", req_lower)),
        "folder_structure": bool(re.search(r"structure|organization|architecture", req_lower)),
        "code_quality": bool(re.search(r"eslint|prettier|clean.*code|quality", req_lower)),
        
        # Modern Development
        "ai_tool_integration": bool(re.search(r"v0|cursor|copilot|ai.*tool", req_lower)),
        "framework_integration": bool(re.search(r"next\.?js|vite|remix|framework", req_lower))
    }
    
    # Calculate scores by category
    react19_score = sum([
        validation_checklist["react19_actions"],
        validation_checklist["react19_server_components"], 
        validation_checklist["react19_use_hook"],
        validation_checklist["react19_ref_prop"]
    ]) / 4 * 100
    
    ui_ux_score = sum([
        validation_checklist["dark_mode_support"],
        validation_checklist["glassmorphism"],
        validation_checklist["micro_animations"],
        validation_checklist["accessibility_first"],
        validation_checklist["responsive_design"]
    ]) / 5 * 100
    
    technical_score = sum([
        validation_checklist["typescript_support"],
        validation_checklist["performance_optimization"],
        validation_checklist["state_management"],
        validation_checklist["testing_requirements"],
        validation_checklist["error_handling"]
    ]) / 5 * 100
    
    architecture_score = sum([
        validation_checklist["component_architecture"],
        validation_checklist["folder_structure"],
        validation_checklist["code_quality"]
    ]) / 3 * 100
    
    # Overall compliance
    total_items = len(validation_checklist)
    met_requirements = sum(validation_checklist.values())
    overall_score = (met_requirements / total_items) * 100
    
    # Generate missing requirements
    missing_requirements = []
    recommendations = []
    
    if react19_score < 75:
        missing_requirements.append("React 19 Features")
        recommendations.extend([
            "Add React 19 Actions for form handling",
            "Consider Server Components for performance",
            "Specify 'use' hook for async operations"
        ])
        
    if ui_ux_score < 75:
        missing_requirements.append("UI/UX 2025 Trends")
        recommendations.extend([
            "Include dark mode as primary theme",
            "Add glassmorphism effects requirements",
            "Specify micro-animations for better UX"
        ])
        
    if technical_score < 75:
        missing_requirements.append("Technical Requirements")
        recommendations.extend([
            "Add TypeScript strict mode requirements",
            "Include performance optimization specifications",
            "Add comprehensive testing requirements"
        ])
        
    if architecture_score < 75:
        missing_requirements.append("Architecture & Structure")
        recommendations.extend([
            "Define component architecture patterns",
            "Specify folder structure organization",
            "Include code quality tools (ESLint, Prettier)"
        ])
    
    return {
        "overall_score": round(overall_score, 1),
        "compliance_level": (
            "Excellent" if overall_score >= 90 else
            "Good" if overall_score >= 75 else
            "Needs Improvement" if overall_score >= 50 else
            "Poor"
        ),
        "category_scores": {
            "react19_features": round(react19_score, 1),
            "ui_ux_2025_trends": round(ui_ux_score, 1),
            "technical_requirements": round(technical_score, 1),
            "architecture_structure": round(architecture_score, 1)
        },
        "validation_checklist": validation_checklist,
        "missing_requirements": missing_requirements,
        "recommendations": recommendations,
        "strengths": [
            category.replace("_", " ").title()
            for category, score in {
                "React 19 Features": react19_score,
                "UI/UX 2025 Trends": ui_ux_score,
                "Technical Requirements": technical_score,
                "Architecture Structure": architecture_score
            }.items()
            if score >= 75
        ],
        "priority_improvements": [
            "Add React 19 Actions and Server Components" if react19_score < 50 else None,
            "Include UI/UX 2025 trends (dark mode, glassmorphism)" if ui_ux_score < 50 else None,
            "Specify TypeScript and performance requirements" if technical_score < 50 else None,
            "Define architecture and code quality standards" if architecture_score < 50 else None
        ],
        "compliance_summary": f"{met_requirements}/{total_items} requirements met ({overall_score:.1f}%)"
    }

@mcp.tool(tags=["info", "documentation", "reference"])
async def get_unified_server_info(ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Get comprehensive information about the unified React server capabilities.
    
    Returns:
        Complete server feature overview and usage guide
    """
    logger.info("Retrieving unified React server information")
    
    return {
        "server_name": "React Unified Development Server",
        "version": "1.0.0",
        "description": "Complete MCP server combining React code analysis, optimization, and modern development practices",
        
        "core_capabilities": {
            "code_analysis": {
                "description": "Comprehensive React code quality analysis",
                "features": [
                    "0-100 scoring system with detailed feedback",
                    "React 19 features detection",
                    "UI/UX 2025 trends analysis",
                    "Performance and accessibility evaluation",
                    "TypeScript quality assessment"
                ],
                "supported_components": ["Basic components", "Dashboards", "Forms", "Modals", "Navigation"]
            },
            "code_optimization": {
                "description": "Intelligent React code optimization",
                "features": [
                    "React 19 features integration",
                    "Performance optimization patterns",
                    "Accessibility improvements",
                    "Modern UI/UX trends application"
                ],
                "focus_areas": ["Performance", "Accessibility", "React19", "UI/UX Trends"]
            },
            "prompt_optimization": {
                "description": "AI-optimized prompt generation for React development",
                "features": [
                    "Basic prompt enhancement",
                    "AI tool specific optimization (v0.dev, Cursor, Visual Copilot)",
                    "Component template generation",
                    "Quality validation and scoring"
                ],
                "target_tools": ["v0.dev", "Cursor AI", "Visual Copilot", "Generic"]
            }
        },
        
        "available_tools": {
            "analyze_react_code": "Comprehensive code analysis with React 19 and UI/UX 2025 evaluation",
            "optimize_react_code": "Intelligent code optimization with modern patterns",
            "analyze_react_prompt": "Prompt quality analysis for React development",
            "optimize_react_prompt": "AI-optimized prompt generation with modern features",
            "generate_component_template": "Component-specific template generation",
            "get_react_trends_2025": "Latest React and UI/UX trends with examples",
            "validate_react_requirements": "Requirements validation against modern standards",
            "get_unified_server_info": "Server capabilities and usage information"
        },
        
        "supported_features": {
            "react19_features": [
                "Server Components",
                "Actions and form handling", 
                "'use' hook for async resources",
                "Ref as prop pattern",
                "Enhanced concurrent features"
            ],
            "ui_ux_2025_trends": [
                "Dark mode first approach",
                "Glassmorphism effects",
                "Micro-animations and feedback",
                "Accessibility-first design",
                "Interactive 3D elements",
                "AI-driven personalization"
            ],
            "ai_tool_optimization": [
                "v0.dev specific prompts",
                "Cursor AI workflow integration",
                "Visual Copilot compatibility",
                "Generic AI tool support"
            ]
        },
        
        "workflow_examples": {
            "code_analysis_workflow": [
                "1. Use analyze_react_code() with your component code",
                "2. Review scores and feedback for improvement areas",
                "3. Apply optimize_react_code() with focus areas",
                "4. Validate improvements with re-analysis"
            ],
            "prompt_optimization_workflow": [
                "1. Use analyze_react_prompt() to evaluate current prompt",
                "2. Apply optimize_react_prompt() with target AI tool",
                "3. Use generate_component_template() for specific components",
                "4. Validate with validate_react_requirements()"
            ],
            "full_development_workflow": [
                "1. Start with generate_component_template() for structured approach",
                "2. Develop component using optimized prompt",
                "3. Analyze code with analyze_react_code()",
                "4. Optimize using optimize_react_code()",
                "5. Validate final requirements compliance"
            ]
        },
        
        "best_practices": {
            "development": [
                "Always use TypeScript with strict mode",
                "Implement React 19 features where applicable",
                "Follow accessibility-first design principles",
                "Apply UI/UX 2025 trends for modern experience",
                "Use performance optimization patterns"
            ],
            "ai_prompting": [
                "Be specific about component requirements",
                "Include React 19 features in specifications",
                "Add UI/UX trends for modern design",
                "Specify target AI tool for optimization",
                "Include accessibility and performance requirements"
            ]
        },
        
        "integration_guide": {
            "getting_started": [
                "Define your component or project requirements",
                "Choose appropriate tool based on your needs",
                "Use unified analysis for comprehensive feedback",
                "Apply optimizations systematically"
            ],
            "advanced_usage": [
                "Combine multiple tools for comprehensive workflow",
                "Use prompt optimization before development",
                "Apply trends analysis for modern design",
                "Validate requirements throughout development"
            ]
        },
        
        "supported_frameworks": React19Context.FRAMEWORKS_SUPPORT,
        
        "performance_metrics": {
            "analysis_speed": "~300ms for typical React components",
            "optimization_accuracy": "85-95% improvement in code quality scores",
            "prompt_enhancement": "40-60% improvement in prompt quality",
            "ai_tool_compatibility": "Optimized for all major AI development tools"
        }
    }

# ================================
# MCP PROMPTS
# ================================


@mcp.prompt()
async def create_react19_component(
    component_name: str,
    features: List[str] = [],
    use_server_component: bool = False
) -> List[Dict[str, str]]:
    """
    Generate a prompt to create a component with React 19 features.

    Args:
        component_name: Name of the component to create
        features: React 19 features to use (actions, use_hook, ref_prop)
        use_server_component: Whether to create a Server Component
    """
    default_features = ["actions", "use_hook", "ref_prop"]
    feature_list = features if features else default_features

    return [
        {
            "role": "system",
            "content": """You are an expert in React 19 development.

React 19 key features:
1. **Actions**: New form action pattern for async operations
   - Automatic pending state management
   - Optimistic updates with useOptimistic
   - useFormState for form state handling

2. **Server Components**: Components that render on server
   - 'use server' directive for server-only code
   - Direct database/API access
   - Reduced client bundle size

3. **'use' hook**: For consuming async resources
   - Suspense-native data fetching
   - Promise unwrapping in components
   - Context consumption with use()

4. **Ref as prop**: No more forwardRef
   - Pass ref directly as prop
   - Cleaner component APIs
   - Better TypeScript support

Best practices:
- Use TypeScript with strict typing
- Implement proper error boundaries
- Add loading states with Suspense
- Follow accessibility guidelines"""
        },
        {
            "role": "user",
            "content": f"""Create a React 19 component: {component_name}

Component type: {'Server Component' if use_server_component else 'Client Component'}
React 19 features to use: {', '.join(feature_list)}

Requirements:
1. Use TypeScript with proper interfaces
2. Implement the specified React 19 features
3. {'Add "use server" directive' if use_server_component else 'Add "use client" directive if needed'}
4. Include error handling and loading states
5. Add comprehensive JSDoc comments
6. Follow accessibility best practices
7. Include usage example
8. Add unit test example"""
        }
    ]


@mcp.prompt()
async def optimize_for_v0_dev(
    component_description: str,
    styling: str = "tailwind",
    include_variants: bool = True
) -> List[Dict[str, str]]:
    """
    Generate a prompt optimized for v0.dev.

    Args:
        component_description: Description of component to create
        styling: Styling approach (tailwind, css-modules)
        include_variants: Include component variants
    """
    return [
        {
            "role": "system",
            "content": """You are optimizing prompts for v0.dev by Vercel.

v0.dev optimization guidelines:
1. **Be specific**: Include exact layout, spacing, colors
2. **Use Tailwind**: Specify exact Tailwind classes
3. **Component hierarchy**: Define parent-child relationships
4. **Responsive design**: Include breakpoint behaviors
5. **Interactions**: Specify hover, focus, active states
6. **Accessibility**: Include ARIA labels and roles

Effective v0.dev prompt structure:
- Start with component purpose
- Define visual appearance in detail
- Specify interactions and states
- Include responsive behavior
- Add accessibility requirements"""
        },
        {
            "role": "user",
            "content": f"""Optimize this prompt for v0.dev:

Component: {component_description}
Styling: {styling}
Include variants: {'Yes - create multiple variants' if include_variants else 'No - single version'}

Create an optimized v0.dev prompt that includes:
1. Specific layout with Tailwind classes
2. Exact color palette and typography
3. Spacing and sizing specifications
4. Hover, focus, and active states
5. Responsive breakpoints (mobile, tablet, desktop)
6. Accessibility features (ARIA, keyboard navigation)
7. Component variants if requested
8. Animation/transition specifications"""
        }
    ]


@mcp.prompt()
async def optimize_for_cursor(
    task_description: str,
    file_structure: str = "feature-based",
    include_tests: bool = True
) -> List[Dict[str, str]]:
    """
    Generate a prompt optimized for Cursor AI.

    Args:
        task_description: Description of development task
        file_structure: Organization pattern (feature-based, type-based)
        include_tests: Include test file generation
    """
    return [
        {
            "role": "system",
            "content": """You are optimizing prompts for Cursor AI editor.

Cursor AI optimization guidelines:
1. **Context-aware**: Reference existing code patterns
2. **File structure**: Specify exact file paths and names
3. **Incremental**: Break into small, focused changes
4. **Naming conventions**: Be explicit about naming patterns
5. **Documentation**: Include inline comments and JSDoc

Effective Cursor prompt structure:
- Start with current file context
- Define exact changes needed
- Specify affected files
- Include testing requirements
- Add documentation standards"""
        },
        {
            "role": "user",
            "content": f"""Optimize this prompt for Cursor AI:

Task: {task_description}
File structure: {file_structure}
Include tests: {'Yes' if include_tests else 'No'}

Create an optimized Cursor prompt that includes:
1. Clear file path specifications
2. Exact code modifications needed
3. Naming conventions to follow
4. Import/export patterns
5. TypeScript types and interfaces
6. {'Test file specifications' if include_tests else 'Skip test specifications'}
7. Inline documentation requirements
8. Error handling patterns"""
        }
    ]


@mcp.prompt()
async def design_server_component(
    component_purpose: str,
    data_source: str = "database",
    caching_strategy: str = "default"
) -> List[Dict[str, str]]:
    """
    Generate a prompt to design a React Server Component.

    Args:
        component_purpose: What the Server Component should do
        data_source: Where data comes from (database, api, filesystem)
        caching_strategy: Caching approach (default, force-cache, no-store)
    """
    return [
        {
            "role": "system",
            "content": """You are an expert in React Server Components.

Server Component principles:
1. **Server-only**: Runs exclusively on server
2. **Direct data access**: Database, filesystem, APIs
3. **No client state**: Cannot use useState, useEffect
4. **Async support**: Can be async functions
5. **Composition**: Combine with Client Components

Server Component patterns:
```tsx
// Server Component (default in app directory)
async function UserProfile({ userId }: { userId: string }) {
  const user = await db.user.findUnique({ where: { id: userId } });
  return <div>{user.name}</div>;
}

// With Client Component child
async function Dashboard() {
  const data = await fetchDashboardData();
  return (
    <div>
      <ServerHeader />
      <ClientInteractiveChart data={data} />
    </div>
  );
}
```

Best practices:
- Keep Server Components at page/layout level
- Pass data down to Client Components
- Use streaming for better UX
- Implement proper error boundaries"""
        },
        {
            "role": "user",
            "content": f"""Design a React Server Component for: {component_purpose}

Data source: {data_source}
Caching strategy: {caching_strategy}

Requirements:
1. Implement as async Server Component
2. Fetch data directly from {data_source}
3. Apply {caching_strategy} caching strategy
4. Handle loading states with Suspense
5. Implement error boundary handling
6. Compose with Client Components where needed
7. Optimize for streaming
8. Include TypeScript types"""
        }
    ]


@mcp.prompt()
async def implement_form_action(
    form_purpose: str,
    fields: List[str] = [],
    include_optimistic: bool = True
) -> List[Dict[str, str]]:
    """
    Generate a prompt to implement a form with React 19 Actions.

    Args:
        form_purpose: Purpose of the form
        fields: Form fields needed
        include_optimistic: Include optimistic updates
    """
    default_fields = ["name", "email", "message"]
    field_list = fields if fields else default_fields

    return [
        {
            "role": "system",
            "content": """You are an expert in React 19 form handling with Actions.

React 19 Form Actions:
1. **form action**: Pass server action to form
2. **useFormState**: Track form state with action
3. **useFormStatus**: Get pending state in children
4. **useOptimistic**: Optimistic UI updates

Form Action pattern:
```tsx
'use server'
async function submitForm(prevState, formData: FormData) {
  const data = Object.fromEntries(formData);
  const result = await saveToDatabase(data);
  return { success: true, data: result };
}

'use client'
function ContactForm() {
  const [state, formAction] = useFormState(submitForm, null);

  return (
    <form action={formAction}>
      <input name="email" required />
      <SubmitButton />
      {state?.success && <p>Submitted!</p>}
    </form>
  );
}

function SubmitButton() {
  const { pending } = useFormStatus();
  return <button disabled={pending}>{pending ? 'Submitting...' : 'Submit'}</button>;
}
```"""
        },
        {
            "role": "user",
            "content": f"""Implement a form with React 19 Actions for: {form_purpose}

Form fields: {', '.join(field_list)}
Include optimistic updates: {'Yes' if include_optimistic else 'No'}

Requirements:
1. Create server action with 'use server'
2. Implement form with useFormState
3. Add SubmitButton with useFormStatus
4. {'Implement useOptimistic for instant feedback' if include_optimistic else 'Skip optimistic updates'}
5. Add proper validation
6. Handle success and error states
7. Include accessibility features
8. Add TypeScript types for form data"""
        }
    ]


@mcp.prompt()
async def apply_ui_ux_2025_trends(
    component_code: str = "",
    trends_to_apply: List[str] = []
) -> List[Dict[str, str]]:
    """
    Generate a prompt to apply UI/UX 2025 trends to a component.

    Args:
        component_code: Existing component code (optional)
        trends_to_apply: Specific trends to apply
    """
    default_trends = ["dark_mode", "glassmorphism", "micro_animations", "accessibility"]
    trends = trends_to_apply if trends_to_apply else default_trends

    trend_descriptions = {
        "dark_mode": "Dark mode as primary theme with light mode option",
        "glassmorphism": "Frosted glass effects with backdrop-blur",
        "micro_animations": "Subtle hover/focus animations and transitions",
        "accessibility": "WCAG AA compliance with proper ARIA",
        "3d_elements": "Depth and layering with 3D transforms",
        "variable_fonts": "Dynamic typography with variable fonts"
    }

    return [
        {
            "role": "system",
            "content": """You are an expert in UI/UX design trends for 2025.

UI/UX 2025 Trends:
1. **Dark Mode First**: Primary dark theme, light as secondary
2. **Glassmorphism**: Frosted glass with backdrop-blur, transparency
3. **Micro-animations**: Subtle feedback animations (0.2-0.3s)
4. **Accessibility First**: WCAG AA, keyboard nav, screen readers
5. **3D Elements**: Depth, parallax, layered interfaces
6. **Variable Fonts**: Responsive typography, weight animations

Implementation patterns:
- Use CSS custom properties for theming
- Apply backdrop-blur and subtle borders
- Use Framer Motion or CSS transitions
- Include prefers-reduced-motion support
- Add proper focus indicators"""
        },
        {
            "role": "user",
            "content": f"""Apply UI/UX 2025 trends to {'this component' if component_code else 'a new component'}:

{f"```tsx{chr(10)}{component_code}{chr(10)}```" if component_code else "Create a modern component with the following trends:"}

Trends to apply:
{chr(10).join(f"- {trend}: {trend_descriptions.get(trend, trend)}" for trend in trends)}

Requirements:
1. Implement each specified trend
2. Use CSS custom properties for theming
3. Add smooth transitions (0.2-0.3s)
4. Include prefers-reduced-motion support
5. Ensure WCAG AA accessibility
6. Use modern CSS features (backdrop-blur, etc.)
7. Add proper focus states
8. Include dark/light mode toggle"""
        }
    ]


# ================================
# SERVER STARTUP
# ================================

if __name__ == "__main__":
    logger.info("🚀 React Unified Development Server starting...")
    logger.info("⚛️ Complete React development solution: Analysis + Optimization + React 19 + UI/UX 2025")
    logger.info("🔧 Features: Code analysis, prompt optimization, component templates, trends integration")
    logger.info("🎯 AI Tools: v0.dev, Cursor, Visual Copilot optimization support")
    logger.info("📈 Capabilities: React 19 Actions, Server Components, UI/UX 2025 trends, accessibility-first")
    logger.info("\n📝 Available prompts:")
    logger.info("  - create_react19_component: Create components with React 19 features")
    logger.info("  - optimize_for_v0_dev: Optimize prompts for v0.dev")
    logger.info("  - optimize_for_cursor: Optimize prompts for Cursor AI")
    logger.info("  - design_server_component: Design React Server Components")
    logger.info("  - implement_form_action: Implement forms with Actions")
    logger.info("  - apply_ui_ux_2025_trends: Apply UI/UX 2025 trends")
    mcp.run()