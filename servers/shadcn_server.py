#!/usr/bin/env python3
"""
shadcn/ui MCP Server - Advanced MCP Server for shadcn/ui
=======================================================

Comprehensive and enhanced MCP server for shadcn/ui integration that combines:

1. COMPONENT ACCESS
   - Search and analysis of shadcn/ui components
   - Demonstrations and usage examples
   - Component metadata with dependencies

2. INTELLIGENT GENERATION
   - Optimized templates for different use cases
   - Automatic theme customization
   - Integration with modern React frameworks

3. ANALYSIS AND OPTIMIZATION
   - Analysis of existing components
   - Improvement and optimization suggestions
   - Modern design system patterns

4. COMPLETE INTEGRATION
   - Support for Next.js, Vite, Remix
   - CLI commands and automatic configuration
   - Compatibility with Tailwind CSS

Based on:
- Official shadcn/ui repository
- Complete library documentation
- Design systems best practices
- Modern React patterns 2025

Key Features:
- Component analysis with compatibility scoring
- Theme generation and customization
- Framework-specific setup guides
- Component code generation with examples
- Performance optimization recommendations
"""

import asyncio
import json
import re
import aiohttp
import logging
from dataclasses import dataclass
from typing import Dict, List, Optional, Any, Tuple, Union
from enum import Enum
from fastmcp import FastMCP
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server (following pattern of other servers)
mcp = FastMCP("shadcn/ui Advanced Server")

# ================================
# KNOWLEDGE BASE - SHADCN/UI CONTEXT
# ================================

class ShadcnComponentType(Enum):
    LAYOUT = "layout"
    FORM = "form"
    DATA_DISPLAY = "data_display"
    NAVIGATION = "navigation"
    FEEDBACK = "feedback"
    OVERLAY = "overlay"
    INPUT = "input"
    MEDIA = "media"

class ShadcnFramework(Enum):
    NEXTJS = "next"
    VITE = "vite"
    REMIX = "remix"
    ASTRO = "astro"
    ROUTER = "react-router"

class ShadcnComplexity(Enum):
    SIMPLE = "simple"
    INTERMEDIATE = "intermediate"
    COMPLEX = "complex"

@dataclass
class ShadcnComponent:
    name: str
    category: ShadcnComponentType
    description: str
    dependencies: List[str]
    complexity: ShadcnComplexity
    use_cases: List[str]
    props: Dict[str, str]
    examples: List[str]

class ShadcnKnowledgeBase:
    """Updated shadcn/ui knowledge base"""
    
    COMPONENTS_DATA = {
        "accordion": ShadcnComponent(
            name="accordion",
            category=ShadcnComponentType.LAYOUT,
            description="Vertically stacked set of interactive headings that each reveal a section of content",
            dependencies=["@radix-ui/react-accordion", "class-variance-authority"],
            complexity=ShadcnComplexity.SIMPLE,
            use_cases=["FAQ sections", "Vertical navigation", "Content organization"],
            props={
                "type": "single | multiple",
                "collapsible": "boolean",
                "className": "string",
                "children": "ReactNode"
            },
            examples=["FAQ section", "Settings panel", "Product details"]
        ),
        "alert-dialog": ShadcnComponent(
            name="alert-dialog",
            category=ShadcnComponentType.OVERLAY,
            description="Modal dialog for important confirmations and alerts",
            dependencies=["@radix-ui/react-alert-dialog"],
            complexity=ShadcnComplexity.INTERMEDIATE,
            use_cases=["Confirmations", "Critical warnings", "Destructive actions"],
            props={
                "open": "boolean",
                "onOpenChange": "function",
                "children": "ReactNode"
            },
            examples=["Delete confirmation", "Logout dialog", "Destructive action"]
        ),
        "badge": ShadcnComponent(
            name="badge", 
            category=ShadcnComponentType.DATA_DISPLAY,
            description="Small informative labels for status and categorization",
            dependencies=["class-variance-authority"],
            complexity=ShadcnComplexity.SIMPLE,
            use_cases=["Status indicators", "Tags", "Categorization"],
            props={
                "variant": "default | secondary | destructive | outline",
                "className": "string",
                "children": "ReactNode"
            },
            examples=["Status badge", "Category tag", "Count indicator"]
        ),
        "button": ShadcnComponent(
            name="button",
            category=ShadcnComponentType.INPUT,
            description="Interactive button with multiple variants and sizes",
            dependencies=["@radix-ui/react-slot", "class-variance-authority"],
            complexity=ShadcnComplexity.SIMPLE,
            use_cases=["CTAs", "Primary actions", "Navigation"],
            props={
                "variant": "default | destructive | outline | secondary | ghost | link",
                "size": "default | sm | lg | icon",
                "asChild": "boolean",
                "disabled": "boolean"
            },
            examples=["Submit button", "Navigation CTA", "Icon button"]
        ),
        "card": ShadcnComponent(
            name="card",
            category=ShadcnComponentType.LAYOUT,
            description="Flexible container for displaying related content",
            dependencies=[],
            complexity=ShadcnComplexity.SIMPLE,
            use_cases=["Product cards", "Content sections", "Dashboard widgets"],
            props={
                "className": "string",
                "children": "ReactNode"
            },
            examples=["Product showcase", "Blog post card", "Dashboard metric"]
        ),
        "dialog": ShadcnComponent(
            name="dialog",
            category=ShadcnComponentType.OVERLAY,
            description="Modal overlay for focused interactions",
            dependencies=["@radix-ui/react-dialog"],
            complexity=ShadcnComplexity.INTERMEDIATE,
            use_cases=["Forms", "Details", "Settings"],
            props={
                "open": "boolean",
                "onOpenChange": "function",
                "modal": "boolean"
            },
            examples=["Edit form", "Settings panel", "Content details"]
        ),
        "form": ShadcnComponent(
            name="form",
            category=ShadcnComponentType.FORM,
            description="Complete form system with validation",
            dependencies=["react-hook-form", "@hookform/resolvers", "zod"],
            complexity=ShadcnComplexity.COMPLEX,
            use_cases=["Validation", "Data submission", "User input"],
            props={
                "onSubmit": "function",
                "schema": "ZodSchema",
                "defaultValues": "object"
            },
            examples=["Contact form", "User registration", "Settings form"]
        ),
        "input": ShadcnComponent(
            name="input",
            category=ShadcnComponentType.INPUT,
            description="Standard input field with consistent styling",
            dependencies=[],
            complexity=ShadcnComplexity.SIMPLE,
            use_cases=["Text input", "Form fields", "Search boxes"],
            props={
                "type": "text | email | password | number | etc.",
                "placeholder": "string",
                "disabled": "boolean",
                "className": "string"
            },
            examples=["Contact form field", "Search input", "Login form"]
        ),
        "table": ShadcnComponent(
            name="table",
            category=ShadcnComponentType.DATA_DISPLAY,
            description="Semantic table component for structured data display",
            dependencies=[],
            complexity=ShadcnComplexity.INTERMEDIATE,
            use_cases=["Data tables", "Lists", "Comparisons"],
            props={
                "className": "string",
                "children": "ReactNode"
            },
            examples=["User list", "Product comparison", "Data dashboard"]
        ),
        "toast": ShadcnComponent(
            name="toast",
            category=ShadcnComponentType.FEEDBACK,
            description="Brief notification messages",
            dependencies=["@radix-ui/react-toast"],
            complexity=ShadcnComplexity.INTERMEDIATE,
            use_cases=["Success messages", "Error notifications", "Status updates"],
            props={
                "variant": "default | destructive",
                "duration": "number",
                "onOpenChange": "function"
            },
            examples=["Success notification", "Error message", "Status update"]
        ),
        "tabs": ShadcnComponent(
            name="tabs",
            category=ShadcnComponentType.NAVIGATION,
            description="Navigation between multiple panels of content",
            dependencies=["@radix-ui/react-tabs"],
            complexity=ShadcnComplexity.SIMPLE,
            use_cases=["Content switching", "Settings panels", "Navigation"],
            props={
                "defaultValue": "string",
                "onValueChange": "function",
                "orientation": "horizontal | vertical"
            },
            examples=["Settings tabs", "Content sections", "Dashboard views"]
        ),
        "select": ShadcnComponent(
            name="select",
            category=ShadcnComponentType.INPUT,
            description="Dropdown selection component",
            dependencies=["@radix-ui/react-select"],
            complexity=ShadcnComplexity.INTERMEDIATE,
            use_cases=["Option selection", "Dropdowns", "Filters"],
            props={
                "value": "string",
                "onValueChange": "function",
                "placeholder": "string",
                "disabled": "boolean"
            },
            examples=["Country selector", "Category filter", "Sort options"]
        ),
        "popover": ShadcnComponent(
            name="popover",
            category=ShadcnComponentType.OVERLAY,
            description="Floating content panel triggered by user interaction",
            dependencies=["@radix-ui/react-popover"],
            complexity=ShadcnComplexity.INTERMEDIATE,
            use_cases=["Contextual menus", "Additional info", "Quick actions"],
            props={
                "open": "boolean",
                "onOpenChange": "function",
                "modal": "boolean"
            },
            examples=["User menu", "Color picker", "Context menu"]
        )
    }

    SETUP_GUIDES = {
        "next": {
            "name": "Next.js",
            "install_command": "npx shadcn-ui@latest init",
            "config_files": ["tailwind.config.js", "components.json"],
            "dependencies": ["tailwindcss", "@types/node", "typescript"],
            "setup_steps": [
                "Initialize project with create-next-app",
                "Install shadcn-ui CLI",
                "Run init command",
                "Configure components.json",
                "Add components as needed"
            ]
        },
        "vite": {
            "name": "Vite",
            "install_command": "npx shadcn-ui@latest init",
            "config_files": ["vite.config.ts", "tailwind.config.js", "components.json"],
            "dependencies": ["@vitejs/plugin-react", "tailwindcss", "typescript"],
            "setup_steps": [
                "Create Vite project with React",
                "Install Tailwind CSS",
                "Install shadcn-ui CLI",
                "Run init command",
                "Configure paths in components.json"
            ]
        },
        "remix": {
            "name": "Remix",
            "install_command": "npx shadcn-ui@latest init",
            "config_files": ["remix.config.js", "tailwind.config.js", "components.json"],
            "dependencies": ["@remix-run/react", "tailwindcss"],
            "setup_steps": [
                "Create Remix app",
                "Set up Tailwind CSS",
                "Install shadcn-ui",
                "Configure components.json with Remix paths",
                "Add components"
            ]
        }
    }

    THEMING_SYSTEM = {
        "colors": {
            "primary": {
                "description": "Primary brand color for buttons and active states",
                "css_variables": ["--primary", "--primary-foreground"],
                "usage": "Main CTAs, active nav items, primary buttons"
            },
            "secondary": {
                "description": "Secondary color for subtle backgrounds and accents",
                "css_variables": ["--secondary", "--secondary-foreground"],
                "usage": "Secondary buttons, subtle backgrounds"
            },
            "accent": {
                "description": "Used for hover states and subtle emphasis",
                "css_variables": ["--accent", "--accent-foreground"],
                "usage": "Hover states, subtle highlights"
            },
            "destructive": {
                "description": "For error states and destructive actions",
                "css_variables": ["--destructive", "--destructive-foreground"],
                "usage": "Error messages, delete buttons"
            },
            "muted": {
                "description": "For muted text and subtle backgrounds",
                "css_variables": ["--muted", "--muted-foreground"],
                "usage": "Placeholder text, disabled states"
            }
        },
        "radius": {
            "description": "Border radius for consistent rounded corners",
            "options": ["0rem", "0.25rem", "0.5rem", "0.75rem", "1rem"],
            "default": "0.5rem"
        },
        "fonts": {
            "sans": "Inter, system-ui, sans-serif",
            "mono": "Fira Code, monospace"
        }
    }

# ================================
# COMPONENT ANALYZER & GENERATOR
# ================================

class ShadcnAnalyzer:
    """Advanced analyzer for shadcn/ui components and patterns"""

    def __init__(self):
        self.knowledge_base = ShadcnKnowledgeBase()

    async def analyze_component_code(self, code: str) -> Dict[str, Any]:
        """Analyzes existing shadcn/ui component code for best practices"""
        
        score = 70  # Base score
        detected_components = []
        issues = []
        recommendations = []
        optimizations = []

        # Detect shadcn/ui components
        component_patterns = {
            r'<Button\b': 'button',
            r'<Card\b': 'card', 
            r'<Input\b': 'input',
            r'<Dialog\b': 'dialog',
            r'<Form\b': 'form',
            r'<Badge\b': 'badge',
            r'<Accordion\b': 'accordion',
            r'<Tabs\b': 'tabs',
            r'<Select\b': 'select',
            r'<Toast\b': 'toast'
        }

        for pattern, component in component_patterns.items():
            if re.search(pattern, code):
                detected_components.append(component)
                score += 5

        # Check for proper imports
        if 'from "@/components/ui/' in code:
            score += 10
            recommendations.append("✅ Using proper component imports")
        else:
            issues.append("❌ Missing proper shadcn/ui component imports")
            recommendations.append("Import components from @/components/ui/")

        # Check for TypeScript usage
        if re.search(r':\s*(React\.FC|JSX\.Element|interface)', code):
            score += 10
            recommendations.append("✅ Using TypeScript for type safety")
        else:
            recommendations.append("Consider adding TypeScript for better type safety")

        # Check for className usage (Tailwind integration)
        if 'className=' in code:
            score += 8
            recommendations.append("✅ Using className for styling")

        # Check for accessibility features
        accessibility_patterns = [
            r'aria-\w+',
            r'role=',
            r'tabIndex',
            r'htmlFor'
        ]
        
        accessibility_found = sum(1 for pattern in accessibility_patterns 
                                if re.search(pattern, code))
        
        if accessibility_found > 0:
            score += accessibility_found * 5
            recommendations.append(f"✅ Found {accessibility_found} accessibility features")
        else:
            issues.append("⚠️ Consider adding accessibility attributes")

        # Check for form validation (if form components detected)
        if 'form' in detected_components:
            if any(pattern in code for pattern in ['zod', 'zodResolver', 'useForm']):
                score += 15
                recommendations.append("✅ Using form validation with zod")
            else:
                issues.append("⚠️ Form components should include validation")
                optimizations.append("Add zod validation schema")

        # Check for proper error handling
        if any(pattern in code for pattern in ['try', 'catch', 'error']):
            score += 8
            recommendations.append("✅ Includes error handling")

        # Performance checks
        if 'useMemo' in code or 'useCallback' in code or 'React.memo' in code:
            score += 10
            recommendations.append("✅ Using performance optimizations")
        elif len(code) > 500:
            optimizations.append("Consider memoization for performance")

        # Theme integration
        if any(pattern in code for pattern in ['dark:', 'theme', 'useTheme']):
            score += 12
            recommendations.append("✅ Theme integration detected")
        else:
            optimizations.append("Consider adding dark mode support")

        final_score = min(100, score)

        return {
            "score": final_score,
            "detected_components": detected_components,
            "issues": issues,
            "recommendations": recommendations,
            "optimizations": optimizations,
            "grade": "A" if final_score >= 90 else "B" if final_score >= 75 else "C" if final_score >= 60 else "D",
            "summary": f"Score: {final_score}/100, Components: {len(detected_components)}, Issues: {len(issues)}"
        }

    async def optimize_component_code(self, code: str, focus_areas: Optional[List[str]] = None) -> Dict[str, Any]:
        """Optimizes shadcn/ui component code with best practices"""
        
        if focus_areas is None:
            focus_areas = ["accessibility", "performance", "best_practices"]

        optimized_code = code
        changes_made = []

        # Apply optimizations based on focus areas
        if "accessibility" in focus_areas:
            # Add missing accessibility attributes
            if re.search(r'<Button\b(?![^>]*aria-label)', optimized_code):
                optimized_code = re.sub(
                    r'<Button(\s+[^>]*?)>',
                    r'<Button\1 aria-label="Button">',
                    optimized_code
                )
                changes_made.append("Added aria-label to buttons")

        if "performance" in focus_areas:
            # Add React.memo if component is large
            if len(code) > 300 and "React.memo" not in code and "export default" in code:
                optimized_code = re.sub(
                    r'export default (\w+)',
                    r'export default React.memo(\1)',
                    optimized_code
                )
                changes_made.append("Added React.memo for performance")

        if "best_practices" in focus_areas:
            # Add proper TypeScript types if missing
            if "props" in code and ":" not in code:
                changes_made.append("Consider adding TypeScript interface for props")

        return {
            "original_code": code,
            "optimized_code": optimized_code,
            "changes_made": changes_made,
            "focus_areas": focus_areas
        }

    async def generate_component_example(self, component_name: str, use_case: str, framework: str = "next") -> Dict[str, Any]:
        """Generates optimized component examples"""
        
        if component_name not in self.knowledge_base.COMPONENTS_DATA:
            return {"error": f"Component '{component_name}' not found in knowledge base"}

        component = self.knowledge_base.COMPONENTS_DATA[component_name]
        
        # Generate component code based on use case
        examples = {
            "button": {
                "contact_form": '''import { Button } from "@/components/ui/button"

export function ContactButton() {
  return (
    <Button 
      variant="default" 
      size="default"
      className="w-full"
      aria-label="Send message"
    >
      Send Message
    </Button>
  )
}''',
                "cta": '''import { Button } from "@/components/ui/button"
import { ArrowRight } from "lucide-react"

export function CTAButton() {
  return (
    <Button 
      variant="default" 
      size="lg"
      className="group"
    >
      Get Started
      <ArrowRight className="ml-2 h-4 w-4 group-hover:translate-x-1 transition-transform" />
    </Button>
  )
}'''
            },
            "card": {
                "product": '''import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"

export function ProductCard({ product }: { product: Product }) {
  return (
    <Card className="w-[350px]">
      <CardHeader>
        <div className="flex items-center justify-between">
          <CardTitle>{product.name}</CardTitle>
          <Badge variant="secondary">{product.category}</Badge>
        </div>
        <CardDescription>{product.description}</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="flex items-center justify-between">
          <span className="text-2xl font-bold">${product.price}</span>
          <span className="text-sm text-muted-foreground">In stock: {product.stock}</span>
        </div>
      </CardContent>
      <CardFooter>
        <Button className="w-full">Add to Cart</Button>
      </CardFooter>
    </Card>
  )
}''',
                "dashboard": '''import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"

export function MetricCard({ title, value, description, trend }: MetricCardProps) {
  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium">
          {title}
        </CardTitle>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          className="h-4 w-4 text-muted-foreground"
        >
          <path d="M12 2v20m9-9H3" />
        </svg>
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold">{value}</div>
        <p className="text-xs text-muted-foreground">
          {description}
        </p>
      </CardContent>
    </Card>
  )
}'''
            },
            "form": {
                "contact": '''import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"
import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"

const formSchema = z.object({
  name: z.string().min(2, "Name must be at least 2 characters."),
  email: z.string().email("Please enter a valid email address."),
  message: z.string().min(10, "Message must be at least 10 characters."),
})

export function ContactForm() {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      name: "",
      email: "",
      message: "",
    },
  })

  function onSubmit(values: z.infer<typeof formSchema>) {
    console.log(values)
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
        <FormField
          control={form.control}
          name="name"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Name</FormLabel>
              <FormControl>
                <Input placeholder="Your name" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="email"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Email</FormLabel>
              <FormControl>
                <Input placeholder="your@email.com" type="email" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="message"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Message</FormLabel>
              <FormControl>
                <Textarea 
                  placeholder="Your message here..."
                  className="resize-none"
                  {...field}
                />
              </FormControl>
              <FormDescription>
                Tell us how we can help you.
              </FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />
        <Button type="submit" className="w-full">Send Message</Button>
      </form>
    </Form>
  )
}'''
            }
        }

        # Get example code
        component_examples = examples.get(component_name, {})
        example_code = component_examples.get(use_case, f"// Example for {component_name} - {use_case} not implemented yet")

        # Generate installation instructions
        installation_cmd = f"npx shadcn-ui@latest add {component_name}"
        if component.dependencies:
            additional_deps = " ".join(component.dependencies)
            installation_cmd += f" && npm install {additional_deps}"

        return {
            "component_name": component_name,
            "use_case": use_case,
            "framework": framework,
            "code": example_code,
            "installation": installation_cmd,
            "dependencies": component.dependencies,
            "complexity": component.complexity.value,
            "category": component.category.value,
            "props": component.props,
            "description": component.description
        }

# ================================
# MCP TOOLS
# ================================

@mcp.tool()
async def analyze_shadcn_component(code: str) -> Dict[str, Any]:
    """
    Analyzes code that uses shadcn/ui components and provides detailed insights.
    
    Args:
        code: React code that utilizes shadcn/ui components
        
    Returns:
        Complete analysis with component detection, optimizations and suggestions
    """
    try:
        analyzer = ShadcnAnalyzer()
        analysis = await analyzer.analyze_component_code(code)
        
        logger.info(f"shadcn/ui component analyzed - score: {analysis['score']}, components: {len(analysis['detected_components'])}")
        
        return analysis

    except Exception as e:
        logger.error(f"Error analyzing shadcn component: {str(e)}")
        raise

@mcp.tool()
async def optimize_shadcn_component(
    code: str,
    focus_areas: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Optimizes shadcn/ui code applying best practices and modern patterns.
    
    Args:
        code: React code with shadcn/ui components
        focus_areas: Focus areas for optimization (performance, accessibility, best_practices)
        
    Returns:
        Optimized code with explanation of applied changes
    """
    try:
        analyzer = ShadcnAnalyzer()
        optimization = await analyzer.optimize_component_code(code, focus_areas)
        
        logger.info(f"shadcn/ui component optimized - changes: {len(optimization['changes_made'])}")
        
        return optimization

    except Exception as e:
        logger.error(f"Error optimizing shadcn component: {str(e)}")
        raise

@mcp.tool()
async def generate_shadcn_component(
    component_type: str,
    use_case: str = "",
    framework: str = "next",
    theme: str = "default",
    include_examples: bool = True
) -> Dict[str, Any]:
    """
    Generates optimized and ready-to-use shadcn/ui component.
    
    Args:
        component_type: Component type (button, card, form, dialog, etc.)
        use_case: Specific use case for customization
        framework: Target framework (next, vite, remix, astro)
        theme: Theme to apply (default, dark)
        include_examples: Include usage examples
        
    Returns:
        Complete component code with examples and configuration
    """
    try:
        analyzer = ShadcnAnalyzer()
        
        # Generate component example
        result = await analyzer.generate_component_example(component_type, use_case, framework)
        
        if "error" in result:
            return result
        
        # Add theme-specific modifications if needed
        if theme == "dark":
            result["theme_notes"] = [
                "Component includes dark mode support via dark: classes",
                "Ensure your app has dark mode provider configured",
                "Use 'dark' class on html element to activate dark theme"
            ]
        
        # Add framework-specific setup if needed
        framework_setup = ShadcnKnowledgeBase.SETUP_GUIDES.get(framework, {})
        if framework_setup:
            result["framework_setup"] = framework_setup
        
        logger.info(f"Generated shadcn/ui component: {component_type} for {use_case}")
        
        return result

    except Exception as e:
        logger.error(f"Error generating shadcn component: {str(e)}")
        raise

@mcp.tool()
async def get_shadcn_component_info(component_name: str = "") -> Dict[str, Any]:
    """
    Gets detailed information about available shadcn/ui components.
    
    Args:
        component_name: Specific component name (optional)
        
    Returns:
        Complete information about shadcn/ui component(s)
    """
    try:
        knowledge_base = ShadcnKnowledgeBase()
        
        if component_name:
            if component_name in knowledge_base.COMPONENTS_DATA:
                component = knowledge_base.COMPONENTS_DATA[component_name]
                return {
                    "name": component.name,
                    "category": component.category.value,
                    "description": component.description,
                    "dependencies": component.dependencies,
                    "complexity": component.complexity.value,
                    "use_cases": component.use_cases,
                    "props": component.props,
                    "examples": component.examples,
                    "installation": f"npx shadcn-ui@latest add {component.name}"
                }
            else:
                return {"error": f"Component '{component_name}' not found"}
        else:
            # Return all components organized by category
            components_by_category = {}
            for comp_name, component in knowledge_base.COMPONENTS_DATA.items():
                category = component.category.value
                if category not in components_by_category:
                    components_by_category[category] = []
                
                components_by_category[category].append({
                    "name": component.name,
                    "description": component.description,
                    "complexity": component.complexity.value,
                    "use_cases": component.use_cases[:3]  # First 3 use cases
                })
            
            return {
                "total_components": len(knowledge_base.COMPONENTS_DATA),
                "components_by_category": components_by_category,
                "available_frameworks": list(knowledge_base.SETUP_GUIDES.keys())
            }

    except Exception as e:
        logger.error(f"Error getting component info: {str(e)}")
        raise

@mcp.tool()
async def get_shadcn_setup_guide(framework: str = "next") -> Dict[str, Any]:
    """
    Provides complete setup guide for shadcn/ui with different frameworks.
    
    Args:
        framework: Target framework (next, vite, remix, astro, react-router)
        
    Returns:
        Complete installation and configuration guide
    """
    try:
        knowledge_base = ShadcnKnowledgeBase()
        
        if framework not in knowledge_base.SETUP_GUIDES:
            return {
                "error": f"Framework '{framework}' not supported",
                "available_frameworks": list(knowledge_base.SETUP_GUIDES.keys())
            }
        
        setup_guide = knowledge_base.SETUP_GUIDES[framework]
        
        # Generate complete setup instructions
        setup_instructions = f"""
# shadcn/ui Setup Guide for {setup_guide['name']}

## Prerequisites
- Node.js 18+ installed
- {setup_guide['name']} project created

## Installation Steps

1. **Install dependencies:**
   ```bash
   npm install {' '.join(setup_guide['dependencies'])}
   ```

2. **Initialize shadcn/ui:**
   ```bash
   {setup_guide['install_command']}
   ```

3. **Configure your project:**
   - Update {', '.join(setup_guide['config_files'])}
   - Set up proper paths in components.json

4. **Add components:**
   ```bash
   npx shadcn-ui@latest add button
   npx shadcn-ui@latest add card
   npx shadcn-ui@latest add input
   ```

## Configuration Files

### components.json
```json
{{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "default",
  "rsc": {framework == "next"},
  "tsx": true,
  "tailwind": {{
    "config": "tailwind.config.js",
    "css": "app/globals.css",
    "baseColor": "slate",
    "cssVariables": true
  }},
  "aliases": {{
    "components": "@/components",
    "utils": "@/lib/utils"
  }}
}}
```

### Global CSS (globals.css)
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
 
@layer base {{
  :root {{
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --primary: 222.2 47.4% 11.2%;
    --primary-foreground: 210 40% 98%;
    --secondary: 210 40% 96%;
    --secondary-foreground: 222.2 47.4% 11.2%;
    --muted: 210 40% 96%;
    --muted-foreground: 215.4 16.3% 46.9%;
    --accent: 210 40% 96%;
    --accent-foreground: 222.2 47.4% 11.2%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 210 40% 98%;
    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;
    --ring: 222.2 47.4% 11.2%;
    --radius: 0.5rem;
  }}
 
  .dark {{
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
    --primary: 210 40% 98%;
    --primary-foreground: 222.2 47.4% 11.2%;
    --secondary: 217.2 32.6% 17.5%;
    --secondary-foreground: 210 40% 98%;
    --muted: 217.2 32.6% 17.5%;
    --muted-foreground: 215 20.2% 65.1%;
    --accent: 217.2 32.6% 17.5%;
    --accent-foreground: 210 40% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 210 40% 98%;
    --border: 217.2 32.6% 17.5%;
    --input: 217.2 32.6% 17.5%;
    --ring: 212.7 26.8% 83.9%;
  }}
}}
```

## Framework-Specific Notes
"""
        
        # Add framework-specific steps
        framework_notes = {
            "next": "- Enable RSC support in components.json\n- Import components in app/ directory\n- Use 'use client' directive for interactive components",
            "vite": "- Configure path aliases in vite.config.ts\n- Import components in src/ directory\n- Ensure proper TypeScript configuration",
            "remix": "- Configure Tailwind in remix.config.js\n- Use appropriate import paths\n- Handle client-side components properly"
        }
        
        setup_instructions += framework_notes.get(framework, "")
        
        return {
            "framework": framework,
            "setup_guide": setup_guide,
            "setup_instructions": setup_instructions,
            "next_steps": [
                "Add your first components",
                "Customize theme colors",
                "Set up dark mode",
                "Configure your design system"
            ]
        }

    except Exception as e:
        logger.error(f"Error getting setup guide: {str(e)}")
        raise

@mcp.tool()
async def create_shadcn_theme(
    primary_color: str = "#000000",
    secondary_color: str = "#f1f5f9",
    accent_color: str = "#0ea5e9",
    theme_name: str = "custom"
) -> Dict[str, Any]:
    """
    Creates custom theme for shadcn/ui with specified colors.
    
    Args:
        primary_color: Primary color in hexadecimal
        secondary_color: Secondary color in hexadecimal  
        accent_color: Accent color in hexadecimal
        theme_name: Custom theme name
        
    Returns:
        Custom theme CSS and configuration
    """
    try:
        # Helper function to convert hex to HSL
        def hex_to_hsl(hex_color):
            # Remove # if present
            hex_color = hex_color.lstrip('#')
            
            # Convert to RGB
            r = int(hex_color[0:2], 16) / 255
            g = int(hex_color[2:4], 16) / 255
            b = int(hex_color[4:6], 16) / 255
            
            max_val = max(r, g, b)
            min_val = min(r, g, b)
            diff = max_val - min_val
            
            # Lightness
            l = (max_val + min_val) / 2
            
            if diff == 0:
                h = s = 0
            else:
                # Saturation
                s = diff / (2 - max_val - min_val) if l > 0.5 else diff / (max_val + min_val)
                
                # Hue
                if max_val == r:
                    h = (g - b) / diff + (6 if g < b else 0)
                elif max_val == g:
                    h = (b - r) / diff + 2
                else:
                    h = (r - g) / diff + 4
                h /= 6
            
            return f"{round(h * 360)} {round(s * 100)}% {round(l * 100)}%"

        # Convert colors to HSL
        primary_hsl = hex_to_hsl(primary_color)
        secondary_hsl = hex_to_hsl(secondary_color)
        accent_hsl = hex_to_hsl(accent_color)

        # Generate theme CSS
        theme_css = f"""
/* {theme_name} Theme for shadcn/ui */
@layer base {{
  .theme-{theme_name.lower()} {{
    --background: 0 0% 100%;
    --foreground: {primary_hsl};
    --primary: {primary_hsl};
    --primary-foreground: 210 40% 98%;
    --secondary: {secondary_hsl};
    --secondary-foreground: {primary_hsl};
    --accent: {accent_hsl};
    --accent-foreground: 210 40% 98%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 210 40% 98%;
    --muted: {secondary_hsl};
    --muted-foreground: 215.4 16.3% 46.9%;
    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;
    --ring: {accent_hsl};
    --radius: 0.5rem;
  }}
  
  .dark .theme-{theme_name.lower()} {{
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
    --primary: {primary_hsl};
    --primary-foreground: 222.2 47.4% 11.2%;
    --secondary: 217.2 32.6% 17.5%;
    --secondary-foreground: 210 40% 98%;
    --accent: {accent_hsl};
    --accent-foreground: 210 40% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 210 40% 98%;
    --muted: 217.2 32.6% 17.5%;
    --muted-foreground: 215 20.2% 65.1%;
    --border: 217.2 32.6% 17.5%;
    --input: 217.2 32.6% 17.5%;
    --ring: {accent_hsl};
  }}
}}
"""

        # Usage instructions
        usage_instructions = f"""
# How to use your {theme_name} theme

## 1. Add the CSS to your globals.css file
Add the generated CSS variables to your main CSS file.

## 2. Apply the theme class
Add the theme class to your root element:
```jsx
<div className="theme-{theme_name.lower()}">
  {{/* Your app content */}}
</div>
```

## 3. Use with dark mode
The theme automatically supports dark mode:
```jsx
<div className="theme-{theme_name.lower()} dark">
  {{/* Dark mode content */}}
</div>
```

## 4. Update components.json (optional)
```json
{{
  "themes": [
    {{
      "name": "{theme_name.lower()}",
      "label": "{theme_name.title()}",
      "activeColor": {{
        "light": "{primary_color}",
        "dark": "{primary_color}"
      }}
    }}
  ]
}}
```
"""

        logger.info(f"Created custom shadcn/ui theme: {theme_name}")

        return {
            "theme_name": theme_name,
            "colors": {
                "primary": primary_color,
                "secondary": secondary_color,
                "accent": accent_color
            },
            "theme_css": theme_css,
            "usage_instructions": usage_instructions,
            "theme_class": f"theme-{theme_name.lower()}",
            "css_variables": {
                "primary": primary_hsl,
                "secondary": secondary_hsl,
                "accent": accent_hsl
            }
        }

    except Exception as e:
        logger.error(f"Error creating custom theme: {str(e)}")
        raise

@mcp.tool()
async def get_shadcn_best_practices() -> Dict[str, Any]:
    """
    Returns best practices guide for using shadcn/ui.
    
    Returns:
        Complete guide with recommended patterns, project structure and tips
    """
    try:
        best_practices = {
            "project_structure": {
                "recommended": [
                    "components/ui/ - shadcn/ui components",
                    "components/common/ - shared custom components", 
                    "components/forms/ - form-specific components",
                    "lib/utils.ts - utility functions",
                    "hooks/ - custom React hooks",
                    "types/ - TypeScript type definitions"
                ],
                "example": """
src/
├── components/
│   ├── ui/           # shadcn/ui components
│   ├── common/       # shared components
│   └── forms/        # form components
├── lib/
│   ├── utils.ts      # utilities
│   └── validations.ts # zod schemas
├── hooks/            # custom hooks
└── types/            # TypeScript types
"""
            },
            "component_patterns": {
                "compound_components": "Use compound patterns for complex components like Card.Header, Card.Content",
                "composition": "Compose complex UIs from simple shadcn/ui primitives",
                "customization": "Extend components through className prop and CSS variables",
                "accessibility": "Leverage built-in accessibility features from Radix UI"
            },
            "styling_guidelines": {
                "css_variables": "Use CSS variables for theming and customization",
                "tailwind_integration": "Combine shadcn/ui with custom Tailwind classes",
                "dark_mode": "Implement dark mode using CSS variables and dark: prefix",
                "responsive_design": "Use Tailwind responsive prefixes with shadcn/ui components"
            },
            "performance_tips": {
                "tree_shaking": "Import only the components you need",
                "code_splitting": "Use dynamic imports for heavy components",
                "memoization": "Memoize expensive computations in custom components",
                "bundle_analysis": "Regularly analyze your bundle size"
            },
            "form_handling": {
                "validation": "Use zod with react-hook-form for type-safe validation",
                "error_handling": "Implement proper error states and messages",
                "accessibility": "Ensure forms are keyboard navigable and screen reader friendly",
                "user_experience": "Provide real-time validation feedback"
            },
            "testing_strategies": {
                "unit_tests": "Test component logic and interactions",
                "integration_tests": "Test form submissions and user flows",
                "accessibility_tests": "Use @testing-library/jest-dom for a11y assertions",
                "visual_regression": "Consider visual testing for consistent UI"
            },
            "deployment_considerations": {
                "css_optimization": "Ensure Tailwind CSS is properly purged",
                "font_loading": "Optimize web font loading strategies",
                "bundle_size": "Monitor and optimize JavaScript bundle size",
                "cdn_usage": "Consider CDN for better performance"
            }
        }

        tips_and_tricks = [
            "Use the shadcn/ui CLI for easy component updates",
            "Customize theme colors through CSS variables",
            "Leverage Radix UI's compound component patterns",
            "Create wrapper components for commonly used variants",
            "Use TypeScript interfaces for consistent prop types",
            "Implement proper loading and error states",
            "Test components with different color schemes",
            "Document your custom component variants"
        ]

        common_pitfalls = [
            "Not updating components when shadcn/ui releases updates",
            "Overriding styles instead of using CSS variables",
            "Ignoring accessibility features provided by Radix UI",
            "Not testing dark mode variants",
            "Hardcoding colors instead of using theme variables",
            "Missing proper TypeScript types for custom props"
        ]

        return {
            "best_practices": best_practices,
            "tips_and_tricks": tips_and_tricks,
            "common_pitfalls": common_pitfalls,
            "recommended_tools": {
                "development": ["TypeScript", "Tailwind CSS", "ESLint", "Prettier"],
                "forms": ["react-hook-form", "zod", "@hookform/resolvers"],
                "testing": ["@testing-library/react", "jest", "@testing-library/jest-dom"],
                "styling": ["tailwindcss-animate", "class-variance-authority"]
            },
            "resources": {
                "official_docs": "https://ui.shadcn.com",
                "radix_ui_docs": "https://www.radix-ui.com",
                "tailwind_docs": "https://tailwindcss.com",
                "react_hook_form": "https://react-hook-form.com"
            }
        }

    except Exception as e:
        logger.error(f"Error getting best practices: {str(e)}")
        raise

# ================================
# MCP RESOURCES
# ================================

@mcp.resource(uri="shadcn://components")
async def get_shadcn_components_resource() -> str:
    """Complete shadcn/ui components reference"""
    knowledge_base = ShadcnKnowledgeBase()
    
    components_data = {}
    for name, component in knowledge_base.COMPONENTS_DATA.items():
        components_data[name] = {
            "name": component.name,
            "category": component.category.value,
            "description": component.description,
            "complexity": component.complexity.value,
            "dependencies": component.dependencies,
            "use_cases": component.use_cases,
            "props": component.props,
            "examples": component.examples
        }
    
    return json.dumps({
        "total_components": len(components_data),
        "components": components_data,
        "categories": list(set(comp["category"] for comp in components_data.values()))
    }, indent=2)

@mcp.resource(uri="shadcn://themes")
async def get_shadcn_themes_resource() -> str:
    """shadcn/ui theming system guide"""
    return json.dumps(ShadcnKnowledgeBase.THEMING_SYSTEM, indent=2)

# ================================
# SERVER INITIALIZATION
# ================================

if __name__ == "__main__":
    logger.info("🚀 shadcn/ui Advanced MCP Server starting...")
    logger.info("🎨 Component analysis, generation, and optimization")
    logger.info("🔧 Theme customization and framework integration") 
    logger.info("📚 Complete shadcn/ui knowledge base and best practices")
    mcp.run()