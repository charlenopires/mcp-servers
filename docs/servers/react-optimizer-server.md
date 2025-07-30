# React Optimizer Server

The React Optimizer Server provides advanced React code analysis, optimization, and prompt enhancement specifically designed for modern React development with 2025 UI/UX trends. It combines code analysis with prompt optimization for AI development tools.

## Overview

This server offers comprehensive React code optimization and prompt enhancement services, helping developers create better React applications while generating optimized prompts for AI tools like v0.dev, Cursor, and GitHub Copilot.

**Port**: 3006  
**Protocol**: stdio  
**Module**: `servers.react_optimizer_server`

## Features

### 🔧 Code Analysis & Optimization
- **Performance Analysis**: Component rendering optimization
- **Accessibility Review**: WCAG compliance checking
- **Modern Patterns**: React 19 and 2025 trends integration
- **Best Practices**: Code quality and maintainability assessment

### 🎯 AI-Optimized Prompts
- **Tool-Specific Optimization**: Tailored for v0.dev, Cursor, Visual Copilot
- **Context Enhancement**: Rich context for better AI responses
- **Template Generation**: Component-specific prompt templates
- **Quality Validation**: Prompt effectiveness scoring

### 📊 2025 UI/UX Trends
- **Design System Integration**: Modern design tokens
- **Micro-Interactions**: Smooth animations and transitions
- **Accessibility First**: Inclusive design patterns
- **Performance Metrics**: Core Web Vitals optimization

## Available Tools

### `analyze_react_code(code: str, component_type: str = "component")`
Analyzes React code for conformity with 2025 best practices.

**Parameters:**
- `code` (string): React component code to analyze
- `component_type` (string): Type of component (component, dashboard, portfolio, landing)

**Returns:**
- `overall_score` (number): Code quality score (0-100)
- `performance_score` (number): Performance optimization score
- `accessibility_score` (number): Accessibility compliance score
- `trends_compliance` (number): 2025 trends alignment score
- `issues` (array): Identified problems and suggestions
- `optimizations` (array): Performance improvement recommendations

### `optimize_react_code(code: str, focus_areas?: string[])`
Optimizes React code applying modern best practices.

**Parameters:**
- `code` (string): Original React component code
- `focus_areas` (array, optional): Areas to focus on

**Focus Areas:**
- `"performance"` - Rendering and bundle optimization
- `"accessibility"` - A11y improvements
- `"trends"` - 2025 UI/UX trends integration
- `"patterns"` - Modern React patterns

**Returns:**
- `original_code` (string): Original code
- `optimized_code` (string): Improved version
- `changes_made` (array): List of applied optimizations
- `performance_impact` (string): Expected performance improvement
- `explanation` (string): Detailed explanation of changes

### `analyze_react_prompt(prompt: str)`
Analyzes React development prompts for optimization opportunities.

**Parameters:**
- `prompt` (string): Original user prompt for React development

**Returns:**
- `quality_score` (number): Prompt quality assessment (0-100)
- `missing_elements` (array): Important missing components
- `suggestions` (array): Improvement recommendations
- `ai_tool_compatibility` (object): Compatibility with different AI tools

### `optimize_react_prompt(prompt: str, target_ai_tool: str = "generic", options?)`
Optimizes prompts for generating modern React code.

**Parameters:**
- `prompt` (string): Original user prompt
- `target_ai_tool` (string): Target AI tool (v0_dev, cursor, visual_copilot, generic)
- `component_type` (string, optional): Component type specification
- `include_accessibility` (boolean): Include accessibility requirements
- `include_performance` (boolean): Include performance optimizations

**Returns:**
- `original_prompt` (string): Original prompt
- `optimized_prompt` (string): Enhanced version
- `enhancements_added` (array): List of improvements
- `target_tool_notes` (string): Tool-specific recommendations

### `validate_prompt_quality(prompt: str)`
Validates prompt quality for React code generation.

**Parameters:**
- `prompt` (string): Prompt to validate

**Returns:**
- `quality_score` (number): Overall quality score (0-100)
- `checklist` (object): Detailed quality checklist
- `recommendations` (array): Improvement suggestions
- `estimated_output_quality` (string): Expected AI output quality

### `generate_component_template(component_type: str, complexity: str = "intermediate", options?)`
Generates optimized prompt templates for specific component types.

**Parameters:**
- `component_type` (string): Type of component to generate
- `complexity` (string): Complexity level (simple, intermediate, complex)
- `target_ai_tool` (string): Target AI development tool
- `include_examples` (boolean): Include usage examples

**Component Types:**
- `"form"` - Form components with validation
- `"modal"` - Modal/dialog components
- `"card"` - Card/content components
- `"dashboard"` - Dashboard layouts
- `"navigation"` - Navigation components
- `"data-table"` - Data display tables
- `"chart"` - Data visualization components

**Returns:**
- `template_prompt` (string): Complete optimized prompt
- `customization_points` (array): Areas for customization
- `best_practices_included` (array): Included best practices
- `expected_features` (array): Features the template will generate

### `get_react_trends_2025()`
Returns comprehensive guide to React and UI/UX trends for 2025.

**Returns:**
- `ui_trends` (object): 2025 UI design trends
- `react_patterns` (object): Modern React development patterns
- `performance_techniques` (object): Latest optimization methods
- `accessibility_standards` (object): Current accessibility requirements
- `tooling_recommendations` (array): Recommended tools and libraries

## 2025 UI/UX Trends Integration

### Design Systems
- **Design Tokens**: Consistent spacing, colors, typography
- **Component Variants**: Flexible component configurations
- **Semantic Colors**: Meaningful color naming conventions
- **Responsive Design**: Mobile-first, container queries

### Micro-Interactions
- **Smooth Animations**: 60fps animations using CSS transforms
- **Loading States**: Skeleton screens and progressive loading
- **Feedback Systems**: Immediate user action feedback
- **Gesture Support**: Touch-friendly interactions

### Modern Patterns
- **Glassmorphism**: Frosted glass effects with backdrop-filter
- **Neumorphism**: Soft shadows and subtle depth
- **Dark Mode**: Comprehensive dark theme support
- **Minimalism**: Clean, focused interfaces

### Performance Optimization
- **Core Web Vitals**: LCP, FID, CLS optimization
- **Bundle Splitting**: Strategic code splitting
- **Image Optimization**: Next-gen formats (WebP, AVIF)
- **Lazy Loading**: Progressive content loading

## AI Tool Optimization

### v0.dev Optimization
- **Prompt Structure**: Shadcn/ui-focused prompts
- **Component Variants**: Multiple design options
- **Responsive Patterns**: Mobile-first specifications
- **Tailwind Classes**: Specific utility class recommendations

### Cursor AI Optimization
- **Context Awareness**: File structure and import context
- **Type Safety**: TypeScript-focused prompts
- **Testing Integration**: Jest and RTL considerations
- **Performance Hints**: Optimization suggestions

### Visual Copilot Optimization
- **Design Tokens**: Figma integration considerations
- **Component Libraries**: Design system alignment
- **Accessibility**: Screen reader compatibility
- **Brand Consistency**: Style guide adherence

## Code Analysis Categories

### Performance (25 points)
- Bundle size optimization
- Rendering performance
- Memory usage
- Network requests

### Accessibility (25 points)
- WCAG 2.1 AA compliance
- Keyboard navigation
- Screen reader support
- Color contrast ratios

### Modern Patterns (25 points)
- React 19 features usage
- Hook patterns
- Component composition
- State management

### Code Quality (25 points)
- TypeScript usage
- Error boundaries
- Testing coverage
- Documentation

## Usage Examples

### Code Analysis
```python
analysis = analyze_react_code("""
function UserCard({ user }) {
  return <div onClick={() => alert(user.name)}>{user.name}</div>;
}
""")
# Returns: accessibility_score: 20, issues: ["Missing keyboard support", "No semantic HTML"]
```

### Code Optimization
```python
optimized = optimize_react_code(code, ["accessibility", "performance"])
# Returns optimized version with proper semantic HTML, keyboard support, memoization
```

### Prompt Optimization
```python
optimized_prompt = optimize_react_prompt(
  "Create a login form",
  target_ai_tool="v0_dev",
  include_accessibility=True
)
# Returns comprehensive prompt with validation, accessibility, and Tailwind classes
```

### Template Generation
```python
template = generate_component_template(
  "dashboard",
  complexity="complex",
  target_ai_tool="cursor"
)
# Returns detailed dashboard template with charts, tables, and responsive layout
```

## Quality Scoring

### Prompt Quality (0-100)
- **Clarity**: 25 points - Clear requirements and objectives
- **Context**: 25 points - Sufficient background information
- **Specificity**: 25 points - Detailed functional requirements
- **Completeness**: 25 points - All necessary elements included

### Code Quality (0-100)
- **Performance**: 25 points - Optimization and efficiency
- **Accessibility**: 25 points - Inclusive design practices
- **Modern Patterns**: 25 points - Current React best practices
- **Maintainability**: 25 points - Clean, readable code

## Configuration

Environment variables:
- `MCP_SERVER_PORT`: Server port (default: 3006)
- `MCP_SERVER_PROTOCOL`: Communication protocol (default: stdio)
- `TRENDS_VERSION`: UI trends version (default: 2025)

## Dependencies

- **FastMCP**: 2.4.0+
- **React Analysis Engine**: Built-in code analysis
- **UI Trends Database**: 2025 design patterns
- **Python**: 3.12+

---

*This server is part of the MCP Servers Collection developed by Charleno Pires*