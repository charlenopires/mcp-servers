# shadcn/ui Server

The shadcn/ui Server provides comprehensive support for shadcn/ui component development, offering intelligent analysis, optimization, code generation, and theming capabilities for modern React applications using the shadcn/ui design system.

## Overview

This server specializes in shadcn/ui component development, providing tools for component analysis, generation, optimization, and custom theming. It helps developers leverage the full power of the shadcn/ui ecosystem with best practices and modern patterns.

**Port**: 3007  
**Protocol**: stdio  
**Module**: `servers.shadcn_server`

## Features

### 📦 Component Intelligence
- **Component Detection**: Automatic shadcn/ui component identification
- **Usage Analysis**: Best practices validation and optimization suggestions
- **Dependency Management**: Smart component dependency resolution
- **Version Compatibility**: Multi-version shadcn/ui support

### 🎨 Theming & Customization
- **Custom Theme Generation**: Brand-specific color scheme creation
- **CSS Variable Management**: Semantic design token handling
- **Dark Mode Support**: Comprehensive dark theme implementation
- **Framework Integration**: Next.js, Vite, Remix, Astro support

### 🛠️ Code Generation
- **Component Scaffolding**: Complete component implementations
- **Example Generation**: Practical usage examples
- **Configuration Setup**: Framework-specific setup guides
- **Best Practices**: Optimized component patterns

## Available Tools

### `analyze_shadcn_component(code: str)`
Analyzes React code using shadcn/ui components for optimization opportunities.

**Parameters:**
- `code` (string): React code with shadcn/ui components

**Returns:**
- `components_detected` (array): Identified shadcn/ui components
- `optimization_score` (number): Code quality score (0-100)
- `suggestions` (array): Improvement recommendations
- `accessibility_issues` (array): A11y concerns
- `performance_notes` (array): Performance optimization tips

### `optimize_shadcn_component(code: str, focus_areas?: string[])`
Optimizes shadcn/ui component code applying best practices.

**Parameters:**
- `code` (string): Original component code
- `focus_areas` (array, optional): Specific optimization areas

**Focus Areas:**
- `"performance"` - Bundle size and rendering optimization
- `"accessibility"` - A11y improvements
- `"best_practices"` - shadcn/ui conventions

**Returns:**
- `original_code` (string): Original code
- `optimized_code` (string): Improved version
- `changes_applied` (array): Applied optimizations
- `explanation` (string): Detailed change explanation

### `generate_shadcn_component(component_type: str, options?)`
Generates optimized shadcn/ui components with modern patterns.

**Parameters:**
- `component_type` (string): Type of component to generate
- `use_case` (string, optional): Specific use case context
- `framework` (string): Target framework (next, vite, remix, astro)
- `theme` (string): Theme variant (default, dark)
- `include_examples` (boolean): Include usage examples

**Component Types:**
- `"button"` - Button variants and states
- `"card"` - Content cards and layouts
- `"form"` - Form components with validation
- `"dialog"` - Modal and dialog components
- `"navigation"` - Nav components and menus
- `"data-table"` - Advanced data tables
- `"chart"` - Data visualization components

### `get_shadcn_component_info(component_name?: str)`
Provides detailed information about shadcn/ui components.

**Parameters:**
- `component_name` (string, optional): Specific component name

**Returns:**
- Component documentation, props, variants, and usage examples
- Complete library overview if no component specified

### `get_shadcn_setup_guide(framework: str = "next")`
Provides comprehensive setup instructions for different frameworks.

**Parameters:**
- `framework` (string): Target framework

**Supported Frameworks:**
- `"next"` - Next.js setup
- `"vite"` - Vite setup  
- `"remix"` - Remix setup
- `"astro"` - Astro setup
- `"react-router"` - React Router setup

**Returns:**
- Complete installation and configuration guide
- Framework-specific optimizations
- Common troubleshooting solutions

### `create_shadcn_theme(primary_color?: str, options?)`
Creates custom themes for shadcn/ui applications.

**Parameters:**
- `primary_color` (string): Primary brand color (hex)
- `secondary_color` (string): Secondary color
- `accent_color` (string): Accent color
- `theme_name` (string): Custom theme name

**Returns:**
- Complete CSS theme configuration
- Design token specifications
- Implementation instructions

### `get_shadcn_best_practices()`
Returns comprehensive shadcn/ui best practices guide.

**Returns:**
- Component usage patterns
- Project structure recommendations
- Performance optimization tips
- Accessibility guidelines

## Component Library

### Layout Components
- **Container**: Responsive container layouts
- **Grid**: Flexible grid systems
- **Stack**: Vertical and horizontal stacking
- **Separator**: Content dividers

### Form Components
- **Input**: Text inputs with variants
- **Textarea**: Multi-line text inputs
- **Select**: Dropdown selections
- **Checkbox**: Boolean selections
- **Radio Group**: Single selections
- **Switch**: Toggle controls
- **Slider**: Range selections
- **Form**: Complete form layouts

### Navigation Components
- **Button**: Interactive buttons
- **Link**: Navigation links
- **Breadcrumb**: Navigation breadcrumbs
- **Tabs**: Tabbed interfaces
- **Navigation Menu**: Complex navigation
- **Pagination**: Content pagination

### Feedback Components
- **Alert**: Status messages
- **Toast**: Notification toasts
- **Progress**: Progress indicators
- **Skeleton**: Loading placeholders
- **Spinner**: Loading spinners

### Overlay Components
- **Dialog**: Modal dialogs
- **Sheet**: Slide-out panels
- **Popover**: Contextual popovers
- **Tooltip**: Hover information
- **Dropdown Menu**: Action menus

### Data Display
- **Table**: Data tables
- **Card**: Content cards
- **Avatar**: User avatars
- **Badge**: Status badges
- **Label**: Form labels

## Framework Integration

### Next.js Setup
```bash
npx shadcn-ui@latest init
npx shadcn-ui@latest add button card form
```

### Vite Setup
```bash
npm create vite@latest my-app -- --template react-ts
npx shadcn-ui@latest init
```

### Custom Configuration
```json
{
  "style": "default",
  "rsc": false,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "app/globals.css",
    "baseColor": "slate",
    "cssVariables": true
  }
}
```

## Theming System

### Color System
```css
:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;
  --primary: 222.2 47.4% 11.2%;
  --primary-foreground: 210 40% 98%;
  --secondary: 210 40% 96%;
  --secondary-foreground: 222.2 84% 4.9%;
}
```

### Dark Mode
```css
.dark {
  --background: 222.2 84% 4.9%;
  --foreground: 210 40% 98%;
  --primary: 210 40% 98%;
  --primary-foreground: 222.2 47.4% 11.2%;
}
```

### Custom Theme Generation
```javascript
const customTheme = {
  primary: "hsl(262, 83%, 58%)",
  secondary: "hsl(220, 14%, 96%)",
  accent: "hsl(220, 14%, 96%)",
  destructive: "hsl(0, 84%, 60%)"
};
```

## Best Practices

### Component Usage
- Use semantic HTML elements
- Implement proper ARIA attributes
- Follow responsive design principles
- Maintain consistent spacing

### Performance
- Import components individually
- Use dynamic imports for large components
- Optimize bundle size with tree shaking
- Implement proper loading states

### Accessibility
- Ensure keyboard navigation
- Provide screen reader support
- Maintain color contrast ratios
- Include focus indicators

### Theming
- Use CSS variables for consistency
- Implement proper dark mode support
- Follow design token conventions
- Maintain semantic naming

## Usage Examples

### Component Analysis
```python
analysis = analyze_shadcn_component("""
import { Button } from "@/components/ui/button"

function MyComponent() {
  return <Button variant="destructive">Delete</Button>
}
""")
# Returns component analysis with optimization suggestions
```

### Component Generation
```python
component = generate_shadcn_component(
  "form",
  use_case="user registration",
  framework="next",
  include_examples=True
)
# Returns complete form component with validation
```

### Theme Creation
```python
theme = create_shadcn_theme(
  primary_color="#7c3aed",
  secondary_color="#f1f5f9", 
  theme_name="brand"
)
# Returns complete CSS theme configuration
```

## Configuration

Environment variables:
- `MCP_SERVER_PORT`: Server port (default: 3007)
- `MCP_SERVER_PROTOCOL`: Communication protocol (default: stdio)
- `SHADCN_VERSION`: shadcn/ui version (default: latest)

## Dependencies

- **shadcn/ui**: Latest stable version
- **Tailwind CSS**: 3.3+
- **React**: 18.0+
- **Radix UI**: Component primitives
- **FastMCP**: 2.4.0+

---

*This server is part of the MCP Servers Collection developed by Charleno Pires*