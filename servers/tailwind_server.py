#!/usr/bin/env python3
"""
MCP server for Tailwind CSS v4.1 prompt contextualization
Helps generate updated code with new Tailwind CSS features
"""

from fastmcp import FastMCP, Context
from typing import Dict, Any, List, Optional
import json

# Initialize MCP server
mcp = FastMCP(
    name="Tailwind CSS v4.1 Assistant",
    instructions="""Contextualizes prompts and generates code with Tailwind CSS v4.1 features.

This server provides Tailwind CSS v4.1 expertise:
- CSS-first configuration with @theme, @source, @utility directives
- New utilities: text-shadow, mask gradients, overflow-wrap
- New variants: user-valid, user-invalid, noscript, inverted-colors
- Container queries built-in (no plugin needed)
- OKLCH color palette for wider gamut
- Performance: 3.5x faster full builds, 8x faster incremental

Use these tools to build modern UIs with Tailwind v4.1.""",
    version="3.0.0"
)

# Knowledge base about Tailwind CSS v4.1
TAILWIND_V4_CONTEXT = {
    "version": "4.1.0",
    "release_date": "2025-01-22",
    "major_changes": {
        "configuration": {
            "location": "CSS file instead of tailwind.config.js",
            "import": '@import "tailwindcss";',
            "theme_syntax": "@theme inline { --color-primary: #007bff; }",
            "plugin_syntax": '@plugin "tailwindcss-animate";'
        },
        "new_utilities": {
            "text-shadow": ["text-shadow-2xs", "text-shadow-xs", "text-shadow-sm", "text-shadow", "text-shadow-lg", "text-shadow-xl"],
            "mask": ["mask-{direction}-from-{value}", "mask-{direction}-to-{value}", "mask-image-gradient-to-{direction}"],
            "drop-shadow-color": "drop-shadow-{color}-{opacity}",
            "overflow-wrap": ["wrap-break-word", "wrap-anywhere"],
            "container-queries": "Built-in container query support (no plugin needed)",
            "field-sizing": "field-sizing-content for form controls",
            "color-scheme": "color-scheme-light, color-scheme-dark, color-scheme-normal"
        },
        "new_variants": {
            "user-valid": "Applies styles when field is valid after interaction",
            "user-invalid": "Applies styles when field is invalid after interaction",
            "noscript": "Applies styles when JavaScript is disabled",
            "inverted-colors": "Applies styles when inverted colors are active",
            "details-content": "Targets content of <details> elements"
        },
        "directives": {
            "@source": "Controls file scanning",
            "@source not": "Excludes paths from scanning",
            "@source inline": "Works as safelist",
            "@utility": "Defines custom utilities",
            "@theme": "Defines theme variables in CSS"
        },
        "performance": {
            "full_build": "3.5x faster than v3.x",
            "incremental": "8x faster with new CSS",
            "no_changes": "100x faster (microseconds)",
            "engine": "New Oxide engine (Rust) for maximum performance"
        },
        "v4_features": {
            "css_first_config": "Configuration entirely in CSS",
            "css_variables": "Design tokens as CSS variables by default",
            "oklch_colors": "Updated color palette to OKLCH (wider gamut)",
            "container_queries": "Container queries integrated into core",
            "browser_support": "Safari 16.4+, Chrome 111+, Firefox 128+"
        }
    }
}

# Updated code templates
CODE_TEMPLATES = {
    "basic_setup": """/* Basic Tailwind CSS v4.1 configuration */
@import "tailwindcss";

/* Define custom theme */
@theme inline {
  --color-primary: #007bff;
  --color-secondary: #6c757d;
  --color-background: #f8f9fa;
}

/* Configure file scanning */
@source "./src/**/*.{js,jsx,ts,tsx,vue}";
@source "./components/**/*.{js,jsx,ts,tsx}";
@source not "./node_modules";

/* Add plugins if needed */
@plugin "@tailwindcss/forms";
@plugin "@tailwindcss/typography";""",

    "text_shadow_example": """<!-- Text shadow example -->
<h1 class="text-4xl font-bold text-shadow-lg text-shadow-black/50">
  Title with Shadow
</h1>

<!-- Colored shadow -->
<h2 class="text-2xl text-shadow-sm text-shadow-blue-500/30">
  Subtitle with Blue Shadow
</h2>""",

    "mask_example": """<!-- Gradient mask on image -->
<div class="relative">
  <img src="hero.jpg" alt="Hero" class="w-full h-96 object-cover">
  <div class="absolute inset-0 mask-b-from-transparent mask-b-to-black/80"></div>
</div>""",

    "form_validation": """<!-- Form validation with new variants -->
<form>
  <input 
    type="email" 
    class="border-2 border-gray-300 
           user-valid:border-green-500 
           user-invalid:border-red-500
           focus:outline-none px-4 py-2 rounded"
    placeholder="Enter your email"
  >
  
  <!-- Message for when JS is disabled -->
  <div class="hidden noscript:block p-4 bg-yellow-100 text-yellow-800 mt-4">
    JavaScript is required for real-time validation
  </div>
</form>""",

    "responsive_text": """<!-- Responsive text with intelligent wrapping -->
<p class="wrap-anywhere max-w-prose">
  This text can contain very long URLs like 
  https://example.com/very/long/path/that/could/break/the/layout
  and still maintain the layout intact.
</p>""",

    "custom_utility": """/* Define custom utility */
@utility flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

@utility margin-auto {
  margin: auto;
}

<!-- Usage in HTML -->
<div class="flex-center min-h-screen">
  <div class="margin-auto p-8">
    Centered content
  </div>
</div>"""
}


@mcp.tool(tags=["contextualization", "prompts", "v4"])
async def tailwind_contextualize_prompt(prompt: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Contextualizes a Tailwind CSS prompt with v4.1 information

    Args:
        prompt: The user's original prompt

    Returns:
        Prompt enriched with Tailwind CSS v4.1 context
    """

    # Detect Tailwind mentions
    tailwind_keywords = ["tailwind", "tailwindcss", "tw", "utility-first"]
    is_tailwind_related = any(keyword in prompt.lower()
                              for keyword in tailwind_keywords)

    if not is_tailwind_related:
        return {
            "original_prompt": prompt,
            "contextualized": False,
            "message": "Prompt does not appear to be related to Tailwind CSS"
        }

    # Analyze request type
    request_type = analyze_request_type(prompt)

    # Build appropriate context
    context_parts = []

    # Add version information
    context_parts.append(
        f"IMPORTANT: Use Tailwind CSS v{TAILWIND_V4_CONTEXT['version']} (latest stable version).")

    # Add specific context based on request type
    if "config" in request_type or "setup" in request_type:
        context_parts.append("\nUPDATED CONFIGURATION:")
        context_parts.append(
            "- Configuration is now done directly in CSS file, no longer in tailwind.config.js")
        context_parts.append(
            "- Use @theme inline to define theme variables")
        context_parts.append(
            "- Use @source to configure file scanning")
        context_parts.append(f"\nEXAMPLE:\n{CODE_TEMPLATES['basic_setup']}")

    if "shadow" in request_type or "text-shadow" in prompt.lower():
        context_parts.append("\nNEW SHADOW UTILITIES:")
        context_parts.append(
            "- text-shadow-* now available (xs, sm, base, lg, xl)")
        context_parts.append(
            "- Supports colors and opacity: text-shadow-black/50")
        context_parts.append("- Colored drop-shadow: drop-shadow-blue-500/30")
        context_parts.append(
            f"\nEXAMPLE:\n{CODE_TEMPLATES['text_shadow_example']}")

    if "mask" in request_type or "gradient" in request_type:
        context_parts.append("\nNEW MASK UTILITIES:")
        context_parts.append(
            "- mask-* for gradient and transparency effects")
        context_parts.append("- Supports directions: mask-b-from-*, mask-t-to-*")
        context_parts.append(f"\nEXAMPLE:\n{CODE_TEMPLATES['mask_example']}")

    if "form" in request_type or "validation" in request_type:
        context_parts.append("\nNEW VALIDATION VARIANTS:")
        context_parts.append(
            "- user-valid: and user-invalid: for validation after interaction")
        context_parts.append(
            "- Avoids showing errors before user interaction")
        context_parts.append(
            f"\nEXAMPLE:\n{CODE_TEMPLATES['form_validation']}")

    if "text" in request_type or "wrap" in request_type:
        context_parts.append("\nNEW TEXT UTILITIES:")
        context_parts.append(
            "- wrap-anywhere and wrap-break-word for text wrapping")
        context_parts.append("- Useful for long URLs and dynamic content")
        context_parts.append(
            f"\nEXAMPLE:\n{CODE_TEMPLATES['responsive_text']}")

    # Add important general information
    context_parts.append("\nOTHER IMPORTANT CHANGES:")
    context_parts.append("- Performance: builds up to 5x faster")
    context_parts.append("- New variants: noscript:, inverted-colors:")
    context_parts.append("- @utility to create custom utilities")
    context_parts.append("- Improved compatibility with older browsers")

    # Build contextualized prompt
    contextualized_prompt = f"{prompt}\n\n{chr(10).join(context_parts)}"

    return {
        "original_prompt": prompt,
        "contextualized": True,
        "contextualized_prompt": contextualized_prompt,
        "detected_features": request_type,
        "version": TAILWIND_V4_CONTEXT["version"],
        "relevant_examples": get_relevant_examples(request_type)
    }


@mcp.tool(tags=["documentation", "features", "info"])
async def tailwind_get_v4_info(feature: str = "", ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Gets specific information about Tailwind CSS v4.1 features

    Args:
        feature: Specific feature to query (optional)

    Returns:
        Detailed information about the feature or overview
    """

    if not feature:
        return {
            "version": TAILWIND_V4_CONTEXT["version"],
            "overview": TAILWIND_V4_CONTEXT,
            "installation": {
                "steps": [
                    "npm install tailwindcss @tailwindcss/postcss",
                    "Add plugin to postcss.config.js",
                    'Import in CSS: @import "tailwindcss";'
                ]
            }
        }

    feature_lower = feature.lower()

    # Return specific feature information
    feature_info = {}

    if "shadow" in feature_lower:
        feature_info = {
            "feature": "Text Shadows",
            "utilities": TAILWIND_V4_CONTEXT["major_changes"]["new_utilities"]["text-shadow"],
            "usage": "text-shadow-{size} text-shadow-{color}/{opacity}",
            "example": CODE_TEMPLATES["text_shadow_example"]
        }
    elif "mask" in feature_lower:
        feature_info = {
            "feature": "Masks",
            "utilities": TAILWIND_V4_CONTEXT["major_changes"]["new_utilities"]["mask"],
            "usage": "mask-{direction}-from-{value} mask-{direction}-to-{value}",
            "example": CODE_TEMPLATES["mask_example"]
        }
    elif "config" in feature_lower:
        feature_info = {
            "feature": "Configuration",
            "location": "CSS file",
            "directives": TAILWIND_V4_CONTEXT["major_changes"]["directives"],
            "example": CODE_TEMPLATES["basic_setup"]
        }
    elif "variant" in feature_lower:
        feature_info = {
            "feature": "New Variants",
            "variants": TAILWIND_V4_CONTEXT["major_changes"]["new_variants"],
            "example": CODE_TEMPLATES["form_validation"]
        }

    return feature_info


@mcp.tool(tags=["generation", "components", "code"])
async def tailwind_generate_v4_code(
    component_type: str,
    requirements: str = "",
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Generates Tailwind CSS v4.1 code based on component type

    Args:
        component_type: Component type (card, form, hero, etc.)
        requirements: Specific requirements

    Returns:
        Generated code with Tailwind CSS v4.1
    """

    code_snippets = {
        "card": f"""<!-- Modern card with Tailwind CSS v4.1 -->
<div class="bg-white rounded-xl shadow-lg overflow-hidden group hover:shadow-xl transition-shadow">
  <!-- Image with gradient mask -->
  <div class="relative h-48">
    <img src="product.jpg" alt="Product" class="w-full h-full object-cover">
    <div class="absolute inset-0 mask-b-from-transparent mask-b-to-black/60"></div>
  </div>
  
  <!-- Content -->
  <div class="p-6">
    <h3 class="text-xl font-bold text-shadow-sm text-shadow-black/20 mb-2">
      Card Title
    </h3>
    <p class="text-gray-600 wrap-anywhere">
      {requirements or 'Card description with support for long texts'}
    </p>
    
    <!-- Button with colored drop-shadow -->
    <button class="mt-4 bg-blue-500 text-white px-6 py-2 rounded-lg 
                   drop-shadow-lg drop-shadow-blue-500/25 
                   hover:bg-blue-600 transition-colors">
      Learn More
    </button>
  </div>
</div>""",

        "form": f"""<!-- Form with validation Tailwind CSS v4.1 -->
<form class="max-w-md mx-auto p-6 bg-white rounded-lg shadow-md">
  <h2 class="text-2xl font-bold mb-6 text-shadow text-shadow-gray-500/20">
    {requirements or 'Contact Form'}
  </h2>
  
  <!-- Email field with validation -->
  <div class="mb-4">
    <label class="block text-gray-700 mb-2">Email</label>
    <input 
      type="email" 
      required
      class="w-full px-4 py-2 border-2 border-gray-200 rounded-lg
             user-valid:border-green-500 user-valid:bg-green-50
             user-invalid:border-red-500 user-invalid:bg-red-50
             focus:outline-none focus:ring-2 focus:ring-blue-500
             transition-colors"
      placeholder="your@email.com"
    >
  </div>
  
  <!-- Message field -->
  <div class="mb-6">
    <label class="block text-gray-700 mb-2">Message</label>
    <textarea 
      rows="4"
      class="w-full px-4 py-2 border-2 border-gray-200 rounded-lg
             focus:outline-none focus:ring-2 focus:ring-blue-500
             wrap-anywhere"
      placeholder="Enter your message..."
    ></textarea>
  </div>
  
  <!-- Noscript warning -->
  <div class="hidden noscript:block p-3 bg-amber-100 text-amber-800 rounded mb-4">
    JavaScript disabled: basic validation only
  </div>
  
  <!-- Submit button -->
  <button 
    type="submit"
    class="w-full bg-gradient-to-r from-blue-500 to-blue-600 
           text-white font-semibold py-3 rounded-lg
           drop-shadow-lg drop-shadow-blue-500/30
           hover:from-blue-600 hover:to-blue-700
           transition-all duration-200">
    Submit
  </button>
</form>""",

        "hero": f"""<!-- Hero Section with Tailwind CSS v4.1 -->
<section class="relative min-h-screen flex items-center justify-center overflow-hidden">
  <!-- Background with mask -->
  <div class="absolute inset-0">
    <img src="hero-bg.jpg" alt="Background" class="w-full h-full object-cover">
    <div class="absolute inset-0 bg-gradient-to-b from-black/20 to-black/60"></div>
    <div class="absolute inset-0 mask-b-from-50% mask-b-to-black"></div>
  </div>
  
  <!-- Content -->
  <div class="relative z-10 text-center text-white px-6">
    <h1 class="text-5xl md:text-7xl font-bold mb-6 
               text-shadow-lg text-shadow-black/75">
      {requirements or 'Impactful Title'}
    </h1>
    <p class="text-xl md:text-2xl mb-8 max-w-3xl mx-auto
              text-shadow-sm text-shadow-black/50">
      Subtitle with subtle shadow for better readability
    </p>
    
    <!-- CTAs -->
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <button class="px-8 py-4 bg-white text-black font-semibold rounded-lg
                     drop-shadow-xl drop-shadow-white/20
                     hover:bg-gray-100 transition-colors">
        Get Started
      </button>
      <button class="px-8 py-4 border-2 border-white text-white font-semibold rounded-lg
                     hover:bg-white hover:text-black transition-colors">
        Learn More
      </button>
    </div>
  </div>
</section>"""
    }

    # Return appropriate code or generic template
    if component_type.lower() in code_snippets:
        code = code_snippets[component_type.lower()]
    else:
        code = f"""<!-- {component_type} component with Tailwind CSS v4.1 -->
<div class="p-6 bg-white rounded-lg shadow-md">
  <h3 class="text-xl font-bold text-shadow text-shadow-gray-400/30 mb-4">
    {component_type.title()}
  </h3>
  <p class="text-gray-600 wrap-anywhere">
    {requirements or f'{component_type} content'}
  </p>
</div>"""

    return {
        "component_type": component_type,
        "code": code,
        "features_used": [
            "text-shadow",
            "mask utilities",
            "user-valid/invalid variants",
            "colored drop-shadow",
            "wrap-anywhere"
        ],
        "version": TAILWIND_V4_CONTEXT["version"]
    }


@mcp.tool(tags=["documentation", "reference", "v4"])
async def tailwind_get_v4_docs() -> Dict[str, Any]:
    """
    Returns summarized documentation for Tailwind CSS v4.1

    Returns:
        Complete documentation about Tailwind CSS v4.1 changes
    """
    return {
        "description": "Summarized Tailwind CSS v4.1 documentation",
        "content": TAILWIND_V4_CONTEXT,
        "format": "application/json"
    }


@mcp.tool(tags=["examples", "templates", "code"])
async def tailwind_get_v4_examples() -> Dict[str, Any]:
    """
    Returns code examples for Tailwind CSS v4.1

    Returns:
        Collection of templates and code examples for new features
    """
    return {
        "description": "Tailwind CSS v4.1 code examples",
        "content": CODE_TEMPLATES,
        "format": "application/json"
    }

# MCP Prompts for Tailwind CSS v4.1


@mcp.prompt()
async def migrate_to_v4(
    current_config: str = "",
    framework: str = "vite"
) -> List[Dict[str, str]]:
    """
    Generate a prompt to migrate Tailwind v3 configuration to v4.

    Args:
        current_config: Current tailwind.config.js content (optional)
        framework: Target framework (vite, next, remix, astro)
    """
    framework_specifics = {
        "vite": "PostCSS with @tailwindcss/postcss",
        "next": "Next.js built-in PostCSS or @tailwindcss/postcss",
        "remix": "PostCSS with remix-specific setup",
        "astro": "Astro integration @astrojs/tailwind or PostCSS"
    }

    return [
        {
            "role": "system",
            "content": """You are a Tailwind CSS migration expert specializing in v3 to v4 upgrades.

Key migration changes:
1. Configuration moves from tailwind.config.js to CSS file
2. Use @import "tailwindcss"; instead of @tailwind directives
3. Theme values use @theme inline { } directive
4. Content paths use @source directive
5. Plugins use @plugin directive
6. Colors now use OKLCH color space
7. Container queries are built-in (no plugin needed)

Follow these best practices:
- Preserve all custom theme values
- Convert JavaScript config to CSS @theme syntax
- Update any deprecated utilities
- Test with incremental builds for performance"""
        },
        {
            "role": "user",
            "content": f"""Migrate this Tailwind CSS v3 configuration to v4.1:

Framework: {framework}
Setup: {framework_specifics.get(framework, 'PostCSS')}

{f"Current config:{chr(10)}{current_config}" if current_config else "Create a fresh v4.1 CSS configuration"}

Requirements:
1. Convert to CSS-first configuration
2. Use @theme for custom values
3. Use @source for content paths
4. Include migration notes for any breaking changes
5. Provide the complete CSS file structure"""
        }
    ]


@mcp.prompt()
async def design_component(
    component_type: str,
    features: List[str] = [],
    responsive: bool = True,
    dark_mode: bool = True
) -> List[Dict[str, str]]:
    """
    Generate a prompt to design a component with Tailwind v4.1 features.

    Args:
        component_type: Type of component (card, hero, form, modal, etc.)
        features: Specific v4.1 features to use
        responsive: Include responsive design
        dark_mode: Include dark mode support
    """
    v4_features_list = [
        "text-shadow utilities",
        "mask gradients",
        "user-valid/user-invalid variants",
        "noscript variant",
        "colored drop-shadows",
        "wrap-anywhere utility",
        "container queries (@container)",
        "field-sizing-content"
    ]

    features_to_use = features if features else v4_features_list[:4]

    return [
        {
            "role": "system",
            "content": f"""You are a UI developer expert in Tailwind CSS v4.1.

Available v4.1 features:
- text-shadow-* (2xs, xs, sm, base, lg, xl) with color support
- mask-* for gradient masks (mask-b-from-*, mask-t-to-*)
- user-valid:/user-invalid: for form validation after interaction
- noscript: variant for no-JavaScript fallbacks
- drop-shadow-{{color}}/{{opacity}} for colored shadows
- wrap-anywhere for intelligent text wrapping
- @container queries (built-in, no plugin)
- field-sizing-content for auto-sizing inputs
- inverted-colors: for accessibility
- details-content: for <details> elements

Design principles:
- Semantic HTML structure
- Accessibility (WCAG AA)
- Progressive enhancement
- Mobile-first responsive design
- Performance-conscious (minimal classes)"""
        },
        {
            "role": "user",
            "content": f"""Create a {component_type} component using Tailwind CSS v4.1.

Features to incorporate: {', '.join(features_to_use)}
Responsive design: {'Yes - mobile-first with breakpoints' if responsive else 'Desktop only'}
Dark mode: {'Yes - use dark: variant' if dark_mode else 'No'}

Requirements:
1. Use modern v4.1 utilities where appropriate
2. Include hover/focus states
3. Add appropriate ARIA attributes
4. Comment which v4.1 features are being used
5. Provide both the HTML and any custom CSS needed"""
        }
    ]


@mcp.prompt()
async def create_theme(
    brand_colors: Dict[str, str] = {},
    typography_scale: str = "default",
    spacing_scale: str = "default"
) -> List[Dict[str, str]]:
    """
    Generate a prompt to create a custom theme with @theme directive.

    Args:
        brand_colors: Dictionary of brand colors (primary, secondary, etc.)
        typography_scale: Typography scale (compact, default, relaxed)
        spacing_scale: Spacing scale (tight, default, loose)
    """
    default_colors = {
        "primary": "#3b82f6",
        "secondary": "#6366f1",
        "accent": "#f59e0b",
        "neutral": "#6b7280"
    }

    colors = brand_colors if brand_colors else default_colors

    return [
        {
            "role": "system",
            "content": """You are a design systems expert specializing in Tailwind CSS v4.1 theming.

Tailwind v4.1 @theme directive features:
- Define CSS variables directly in CSS
- Variables follow --{category}-{name} pattern
- Support for OKLCH colors (wider gamut)
- Theme values become utility classes automatically
- Can extend or override default theme

Theme variable categories:
- --color-* for colors
- --font-* for font families
- --text-* for font sizes
- --spacing-* for spacing scale
- --radius-* for border radius
- --shadow-* for box shadows
- --container-* for container sizes

Best practices:
- Use semantic color names (primary, secondary, surface)
- Define color scales (50-950)
- Include dark mode variants
- Document design tokens"""
        },
        {
            "role": "user",
            "content": f"""Create a custom Tailwind CSS v4.1 theme configuration.

Brand colors:
{chr(10).join(f'- {name}: {value}' for name, value in colors.items())}

Typography: {typography_scale}
Spacing: {spacing_scale}

Requirements:
1. Use @theme inline {{ }} directive
2. Define color scales for each brand color (50-950)
3. Include semantic color tokens (background, foreground, border)
4. Add dark mode color variants
5. Create custom shadow definitions
6. Document the design system
7. Provide usage examples for the custom utilities"""
        }
    ]


@mcp.prompt()
async def optimize_classes(
    html_code: str,
    optimization_goals: List[str] = []
) -> List[Dict[str, str]]:
    """
    Generate a prompt to optimize and consolidate Tailwind classes.

    Args:
        html_code: HTML code with Tailwind classes to optimize
        optimization_goals: Specific goals (performance, readability, v4-upgrade)
    """
    goals = optimization_goals if optimization_goals else [
        "reduce class count",
        "use v4.1 utilities",
        "improve readability"
    ]

    return [
        {
            "role": "system",
            "content": """You are a Tailwind CSS optimization expert.

Optimization strategies:
1. **Consolidate utilities**: Replace multiple utilities with newer combined ones
2. **Use @apply**: For repeated patterns, create @utility definitions
3. **Leverage v4.1 features**:
   - text-shadow instead of custom CSS
   - mask utilities instead of complex gradients
   - user-valid/invalid instead of JS-based validation styles
4. **Remove redundant classes**: Identify overridden or unused utilities
5. **Group related classes**: Organize by layout, spacing, typography, color
6. **Use arbitrary values sparingly**: Prefer theme values

V4.1 replacements:
- Custom text shadows → text-shadow-*
- Complex gradient masks → mask-*
- JS validation styling → user-valid:/user-invalid:
- overflow-wrap: anywhere → wrap-anywhere
- Custom drop shadows → drop-shadow-{color}/{opacity}

@utility pattern:
@utility card-base {
  @apply bg-white rounded-xl shadow-lg p-6;
}"""
        },
        {
            "role": "user",
            "content": f"""Optimize this Tailwind CSS code for v4.1:

```html
{html_code}
```

Optimization goals: {', '.join(goals)}

Requirements:
1. Identify opportunities for v4.1 utility upgrades
2. Suggest @utility definitions for repeated patterns
3. Remove redundant or overridden classes
4. Improve class organization and readability
5. Provide before/after comparison
6. Note any deprecated utilities that need updating"""
        }
    ]


@mcp.prompt()
async def setup_project(
    framework: str = "vite",
    features: List[str] = [],
    plugins: List[str] = []
) -> List[Dict[str, str]]:
    """
    Generate a prompt to set up a new project with Tailwind CSS v4.

    Args:
        framework: Target framework (vite, next, remix, astro, react-router)
        features: Additional features (forms, typography, dark-mode)
        plugins: Tailwind plugins to include
    """
    framework_commands = {
        "vite": "npm create vite@latest my-app -- --template react-ts",
        "next": "npx create-next-app@latest my-app",
        "remix": "npx create-remix@latest my-app",
        "astro": "npm create astro@latest my-app",
        "react-router": "npx create-react-router@latest my-app"
    }

    default_features = ["dark mode", "responsive design", "CSS variables"]
    default_plugins = ["@tailwindcss/forms", "@tailwindcss/typography"]

    return [
        {
            "role": "system",
            "content": """You are a frontend setup expert specializing in Tailwind CSS v4.1 projects.

Tailwind CSS v4.1 setup requirements:
1. Install: npm install tailwindcss @tailwindcss/postcss
2. PostCSS config with @tailwindcss/postcss plugin
3. Main CSS file with @import "tailwindcss";
4. @source directive for content paths
5. @theme for custom configuration

Framework-specific notes:
- Vite: postcss.config.js with @tailwindcss/postcss
- Next.js: Can use built-in PostCSS or @tailwindcss/postcss
- Remix: PostCSS setup similar to Vite
- Astro: @astrojs/tailwind integration or PostCSS

Best practices:
- Organize CSS with layers (@layer base, components, utilities)
- Use CSS nesting (native support in v4)
- Set up IDE extensions (Tailwind CSS IntelliSense)
- Configure Prettier with prettier-plugin-tailwindcss"""
        },
        {
            "role": "user",
            "content": f"""Set up a new {framework} project with Tailwind CSS v4.1.

Framework command: {framework_commands.get(framework, 'npm create vite@latest')}

Features to include: {', '.join(features if features else default_features)}
Plugins: {', '.join(plugins if plugins else default_plugins)}

Requirements:
1. Provide step-by-step installation commands
2. Show complete postcss.config.js configuration
3. Create the main CSS file with proper structure
4. Include @source paths for the framework
5. Add @theme with basic customization
6. Configure VS Code settings for IntelliSense
7. Set up Prettier configuration
8. Provide a starter component demonstrating v4.1 features"""
        }
    ]


# Helper functions


def analyze_request_type(prompt: str) -> List[str]:
    """Analyzes the request type in the prompt"""
    prompt_lower = prompt.lower()
    request_types = []

    keyword_map = {
        "config": ["config", "configure", "setup", "install", "installation"],
        "shadow": ["shadow", "text-shadow", "drop-shadow"],
        "mask": ["mask", "gradient", "fade", "transparency"],
        "form": ["form", "input", "validation"],
        "text": ["text", "typography", "wrap", "break"],
        "variant": ["variant", "state", "hover", "focus"]
    }

    for request_type, keywords in keyword_map.items():
        if any(keyword in prompt_lower for keyword in keywords):
            request_types.append(request_type)

    return request_types


def get_relevant_examples(request_types: List[str]) -> List[str]:
    """Returns relevant examples based on request types"""
    examples = []

    example_map = {
        "config": "basic_setup",
        "shadow": "text_shadow_example",
        "mask": "mask_example",
        "form": "form_validation",
        "text": "responsive_text"
    }

    for request_type in request_types:
        if request_type in example_map:
            example_key = example_map[request_type]
            if example_key in CODE_TEMPLATES:
                examples.append(CODE_TEMPLATES[example_key])

    return examples


# Server configuration and execution
if __name__ == "__main__":
    # Start server
    print("🎨 MCP Tailwind CSS v4.1 Assistant server started!")
    print("📚 Available tools:")
    print("  - tailwind_contextualize_prompt: Enriches prompts with v4.1 context")
    print("  - tailwind_get_v4_info: Gets information about specific features")
    print("  - tailwind_generate_v4_code: Generates code with new features")
    print("  - tailwind_get_v4_docs: Gets summarized Tailwind CSS v4.1 documentation")
    print("  - tailwind_get_v4_examples: Gets Tailwind CSS v4.1 code examples")
    print("\n📝 Available prompts:")
    print("  - migrate_to_v4: Migrate from Tailwind v3 to v4")
    print("  - design_component: Design components with v4.1 features")
    print("  - create_theme: Create custom theme with @theme directive")
    print("  - optimize_classes: Optimize and consolidate Tailwind classes")
    print("  - setup_project: Set up new project with Tailwind CSS v4")

    mcp.run()
