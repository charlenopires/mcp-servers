#!/usr/bin/env python3
"""
MCP server for Tailwind CSS v4.1 prompt contextualization
Helps generate updated code with new Tailwind CSS features
"""

from fastmcp import FastMCP
from typing import Dict, Any, List
import json

# Initialize MCP server
mcp = FastMCP("Assistant for TailwindCSS v4.1 Context Prompts")

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


@mcp.tool()
async def tailwind_contextualize_prompt(prompt: str) -> Dict[str, Any]:
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


@mcp.tool()
async def tailwind_get_v4_info(feature: str = "") -> Dict[str, Any]:
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


@mcp.tool()
async def tailwind_generate_v4_code(
    component_type: str,
    requirements: str = ""
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


@mcp.tool()
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


@mcp.tool()
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

    mcp.run()
