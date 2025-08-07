# Tailwind CSS v4.1 Server

The Tailwind CSS Server provides specialized support for Tailwind CSS v4.1, helping developers transition to the new configuration system and leverage the latest features. It offers contextualized prompts, code generation, and comprehensive information about v4.1 changes.

## Overview

This server assists developers working with Tailwind CSS v4.1 by providing updated information about the new configuration system, utilities, variants, and performance improvements. It helps generate modern, optimized code using the latest Tailwind features.

**Port**: 3002  
**Protocol**: stdio  
**Module**: `servers.tailwind_server`

## Features

### 🆕 Tailwind CSS v4.1 Support
- **New Configuration System**: CSS-based configuration instead of JavaScript
- **Latest Utilities**: Text shadows, masks, container queries, and more
- **New Variants**: user-valid, user-invalid, noscript, inverted-colors
- **Performance**: 3.5x faster builds with new Oxide engine (Rust)

### 🎨 Code Generation
- **Component Templates**: Pre-built components using v4.1 features
- **Modern Utilities**: Leverages latest utility classes
- **Best Practices**: Follows current Tailwind conventions
- **Responsive Design**: Mobile-first responsive patterns

### 📝 Documentation & Migration
- **Migration Guidance**: Helps transition from v3.x to v4.1
- **Feature Documentation**: Detailed information about new features
- **Code Examples**: Practical examples of new utilities and patterns

## Key Changes in v4.1

### Configuration Revolution
- **CSS-First**: Configuration now lives entirely in CSS files
- **No More JS Config**: Eliminates `tailwind.config.js` requirement
- **CSS Variables**: Design tokens as CSS variables by default
- **Inline Theming**: `@theme inline` directive for custom themes

### New Utilities
- **Text Shadows**: `text-shadow-{size}`, `text-shadow-{color}/{opacity}`
- **Gradient Masks**: `mask-{direction}-from-{value}`, `mask-{direction}-to-{value}`
- **Drop Shadow Colors**: `drop-shadow-{color}-{opacity}`
- **Overflow Wrap**: `wrap-break-word`, `wrap-anywhere`
- **Container Queries**: Built-in support (no plugin needed)
- **Field Sizing**: `field-sizing-content` for form controls
- **Color Scheme**: `color-scheme-light`, `color-scheme-dark`

### New Variants
- **User Validation**: `user-valid:`, `user-invalid:` for form states after interaction
- **JavaScript**: `noscript:` for when JavaScript is disabled
- **Accessibility**: `inverted-colors:` for high contrast mode
- **Details**: `details-content:` for `<details>` element content

### Performance Improvements
- **Full Build**: 3.5x faster than v3.x
- **Incremental**: 8x faster with new CSS
- **No Changes**: 100x faster (microseconds)
- **Rust Engine**: New Oxide engine for maximum performance

## Available Tools

### `tailwind_contextualize_prompt(prompt: str)`
Analyzes and enriches prompts with relevant Tailwind CSS v4.1 context.

**Parameters:**
- `prompt` (string): The user's original prompt

**Returns:**
- `original_prompt` (string): The original prompt
- `contextualized_prompt` (string): Enhanced prompt with v4.1 context
- `context_added` (array): List of context elements added
- `relevant_features` (array): Relevant v4.1 features for the prompt
- `relevant_examples` (array): Code examples matching the request

**Example:**
```python
result = tailwind_contextualize_prompt("Create a card component with shadows")
# Returns prompt enhanced with text-shadow utilities and examples
```

### `tailwind_get_v4_info(feature: str = "")`
Provides detailed information about specific Tailwind CSS v4.1 features.

**Parameters:**
- `feature` (string, optional): Specific feature to query

**Common Features:**
- `"shadow"` - Text shadow utilities
- `"mask"` - Gradient mask utilities  
- `"config"` - Configuration system
- `"variant"` - New pseudo-class variants
- `"performance"` - Performance improvements
- `""` (empty) - Complete overview

**Returns:**
- Feature-specific information with utilities, usage patterns, and examples
- Complete overview if no feature specified

**Example:**
```python
info = tailwind_get_v4_info("shadow")
# Returns: utilities, usage patterns, and code examples for text shadows
```

### `tailwind_generate_v4_code(component_type: str, requirements: str = "")`
Generates modern component code using Tailwind CSS v4.1 features.

**Parameters:**
- `component_type` (string): Type of component to generate
- `requirements` (string, optional): Specific requirements or customizations

**Supported Component Types:**
- `"card"` - Product/content cards with modern features
- `"form"` - Forms with validation states
- `"hero"` - Hero sections with gradients and effects
- `"button"` - Interactive buttons with hover effects
- `"modal"` - Modal dialogs with backdrop effects
- `"navigation"` - Navigation components
- `"layout"` - Page layouts with container queries

**Returns:**
- `component_type` (string): Type of component generated
- `code` (string): Complete HTML/CSS code
- `features_used` (array): v4.1 features utilized
- `notes` (array): Implementation notes and best practices

**Example:**
```python
code = tailwind_generate_v4_code("card", "product showcase with hover effects")
# Returns complete card component with text shadows, masks, and animations
```

### `tailwind_get_v4_docs()`
Returns comprehensive documentation about Tailwind CSS v4.1 changes.

**Returns:**
- Complete migration guide
- All new features with examples
- Configuration changes
- Performance improvements
- Browser compatibility

### `tailwind_get_v4_examples()`
Provides a collection of practical code examples using v4.1 features.

**Returns:**
- `basic_setup` - Complete v4.1 configuration example
- `text_shadows` - Text shadow implementations
- `gradient_masks` - Image mask examples
- `form_validation` - New validation states
- `container_queries` - Container query patterns
- `theme_variables` - CSS variable theming

## Migration Guide

### From v3.x to v4.1

**Old Configuration (v3.x):**
```javascript
// tailwind.config.js
module.exports = {
  theme: {
    colors: {
      primary: '#007bff'
    }
  }
}
```

**New Configuration (v4.1):**
```css
/* styles.css */
@import "tailwindcss";

@theme inline {
  --color-primary: #007bff;
}

@source "./src/**/*.{js,jsx,ts,tsx}";
```

### Key Migration Steps

1. **Remove `tailwind.config.js`**
2. **Move configuration to CSS**
3. **Update build process** (if using custom PostCSS)
4. **Leverage new utilities** (text-shadow, masks, etc.)
5. **Update color references** to use CSS variables

## Configuration Examples

### Basic Setup
```css
@import "tailwindcss";

/* Theme customization */
@theme inline {
  --color-primary: #007bff;
  --color-secondary: #6c757d;
  --color-background: #f8f9fa;
}

/* File scanning */
@source "./src/**/*.{js,jsx,ts,tsx,vue}";
@source "./components/**/*.{js,jsx,ts,tsx}";
@source not "./node_modules";

/* Plugins */
@plugin "@tailwindcss/forms";
@plugin "@tailwindcss/typography";
```

### Advanced Configuration
```css
@import "tailwindcss";

/* Custom utilities */
@utility {
  .scrollbar-hide {
    -ms-overflow-style: none;
    scrollbar-width: none;
  }
  .scrollbar-hide::-webkit-scrollbar {
    display: none;
  }
}

/* Responsive breakpoints */
@theme inline {
  --breakpoint-xs: 475px;
  --breakpoint-3xl: 1600px;
}
```

## Code Examples

### Modern Card Component
```html
<div class="bg-white rounded-xl shadow-lg overflow-hidden group hover:shadow-xl transition-shadow">
  <!-- Image with gradient mask -->
  <div class="relative h-48">
    <img src="product.jpg" alt="Product" class="w-full h-full object-cover">
    <div class="absolute inset-0 mask-b-from-transparent mask-b-to-black/60"></div>
  </div>
  
  <!-- Content with text shadow -->
  <div class="p-6">
    <h3 class="text-xl font-bold text-shadow-sm text-shadow-black/20 mb-2">
      Product Title
    </h3>
    <p class="text-gray-600 wrap-anywhere">
      Product description with proper text wrapping
    </p>
    
    <!-- Button with colored drop-shadow -->
    <button class="mt-4 px-4 py-2 bg-blue-500 text-white rounded-lg drop-shadow-blue-500/30 hover:drop-shadow-blue-500/50 transition-all">
      Buy Now
    </button>
  </div>
</div>
```

### Form with Validation States
```html
<form class="space-y-4">
  <div>
    <input 
      type="email" 
      placeholder="Email address"
      class="w-full px-3 py-2 border border-gray-300 rounded-md
             user-invalid:border-red-500 user-invalid:ring-red-500
             user-valid:border-green-500 user-valid:ring-green-500
             field-sizing-content"
    >
    <p class="mt-1 text-sm text-red-600 user-invalid:block hidden">
      Please enter a valid email address
    </p>
  </div>
</form>
```

## Browser Support

- **Safari**: 16.4+
- **Chrome**: 111+
- **Firefox**: 128+
- **Edge**: 111+

## Performance Metrics

- **Build Speed**: 3.5x faster than v3.x
- **Incremental Builds**: 8x faster
- **Bundle Size**: Smaller with better tree-shaking
- **Runtime**: Zero JavaScript runtime overhead

## Dependencies

- **Tailwind CSS**: 4.1.0+
- **PostCSS**: 8.0+ (for build process)
- **FastMCP**: 2.4.0+
- **Python**: 3.12+

---

*This server is part of the MCP Servers Collection developed by Charleno Pires*