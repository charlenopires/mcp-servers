# React Components Server

The React Components Server provides comprehensive support for React 19 development, offering prompt analysis, component generation, and validation tools specifically designed for modern React patterns including Server Components, Actions, and the new `use` hook.

## Overview

This server specializes in React 19 development workflows, providing intelligent analysis of React-related prompts, best practices validation, and code generation tools that leverage the latest React features and patterns.

**Port**: 3004  
**Protocol**: stdio  
**Module**: `servers.react_server`

## Features

### ⚛️ React 19 Support
- **Server Components**: Server-side rendering patterns
- **Actions**: Form handling and mutations
- **use Hook**: Resource loading and suspense
- **Concurrent Features**: Transitions and deferred values
- **Modern Patterns**: Hooks, context, and state management

### 🔍 Advanced Analysis
- **Prompt Quality Assessment**: React-specific scoring system
- **Best Practices Validation**: Alignment with React guidelines
- **Pattern Recognition**: Identification of React anti-patterns
- **Requirements Coverage**: Comprehensive requirement analysis

### 🛠️ Code Generation
- **Component Templates**: Modern React component patterns
- **Hook Implementations**: Custom hooks with best practices
- **Testing Patterns**: Jest and React Testing Library setups
- **Project Structure**: Complete application scaffolding

## Available Tools

### `analyze_react_prompt(prompt: str)`
Analyzes React development prompts for quality and completeness.

**Parameters:**
- `prompt` (string): The React-related prompt to analyze

**Returns:**
- `score` (number): Quality score (0-100)
- `react_features_detected` (array): Identified React features
- `strengths` (array): Strong points in the prompt
- `weaknesses` (array): Areas needing improvement
- `recommendations` (array): Specific improvement suggestions
- `best_practices_alignment` (object): Alignment with React patterns

**Example:**
```python
analysis = analyze_react_prompt("""
Create a React component for user authentication with form validation,
loading states, and error handling. Use React 19 features where appropriate.
""")
# Returns: score: 78, features: ["forms", "state_management", "error_handling"]
```

### `get_prompt_template(template_type: str = "basic_component")`
Provides optimized prompt templates for React development.

**Parameters:**
- `template_type` (string): Type of template to retrieve

**Template Types:**
- `"basic_component"` - Simple functional component template
- `"complete_application"` - Full application structure template
- `"custom_hook"` - Custom hook development template
- `"server_component"` - React 19 Server Component template

**Returns:**
- `template_type` (string): Type of template provided
- `template_prompt` (string): Complete prompt template
- `key_sections` (array): Important sections to customize
- `react_features` (array): React features covered
- `best_practices` (array): Included best practices

### `suggest_contextual_improvements(prompt: str, context: str = "component")`
Suggests React-specific improvements based on development context.

**Parameters:**
- `prompt` (string): Original prompt to improve
- `context` (string): Development context

**Context Types:**
- `"component"` - React component development
- `"hook"` - Custom hook creation
- `"application"` - Full application development
- `"library"` - React library development

**Returns:**
- `original_prompt` (string): Original prompt
- `improved_prompt` (string): Enhanced version
- `context_specific_additions` (array): Context-based improvements
- `react_patterns_added` (array): React patterns included
- `score_improvement` (number): Expected score improvement

### `validate_react_requirements(requirements: str)`
Validates React project requirements against best practices.

**Parameters:**
- `requirements` (string): Project requirements to validate

**Returns:**
- `overall_score` (number): Validation score (0-100)
- `validation_passed` (boolean): Whether validation passed
- `requirements_coverage` (object): Coverage by category
- `missing_requirements` (array): Critical missing elements
- `react_specific_issues` (array): React-related concerns
- `recommendations` (array): Improvement suggestions

### `generate_optimized_prompt(project_description: str, project_type: str = "component", detail_level: str = "complete")`
Generates comprehensive React development prompts.

**Parameters:**
- `project_description` (string): Basic project description
- `project_type` (string): Type of React project
- `detail_level` (string): Level of detail required

**Project Types:**
- `"component"` - Individual component
- `"application"` - Complete application
- `"library"` - React library/package

**Detail Levels:**
- `"basic"` - Essential requirements only
- `"intermediate"` - Balanced detail level
- `"complete"` - Comprehensive specifications

**Returns:**
- `optimized_prompt` (string): Complete structured prompt
- `sections_included` (array): Prompt sections
- `react_features_recommended` (array): Suggested React features
- `additional_considerations` (array): Extra recommendations

### `get_server_resources()`
Returns information about available React development resources.

**Returns:**
- `components_library` (object): Available component patterns
- `hooks_library` (object): Custom hook examples
- `patterns_library` (object): React design patterns
- `testing_strategies` (array): Testing approaches
- `performance_tips` (array): Optimization recommendations

## React 19 Features Covered

### Server Components
- **Static Generation**: Components that render on the server
- **Data Fetching**: Server-side data loading patterns
- **Streaming**: Progressive rendering techniques
- **SEO Optimization**: Search engine friendly patterns

### Actions
- **Form Actions**: Server-side form handling
- **Mutations**: Data modification patterns
- **Error Handling**: Robust error management
- **Loading States**: User feedback during operations

### use Hook
- **Resource Loading**: Efficient data fetching
- **Suspense Integration**: Seamless loading states
- **Error Boundaries**: Graceful error handling
- **Caching**: Optimized resource management

### Concurrent Features
- **Transitions**: Non-blocking state updates
- **Deferred Values**: Performance optimization
- **Suspense**: Loading state management
- **Error Boundaries**: Error isolation

## Best Practices Validation

### Component Design
- **Single Responsibility**: One purpose per component
- **Props Interface**: Well-defined prop types
- **Composition**: Preferred over inheritance
- **Accessibility**: WCAG compliance considerations

### State Management
- **Local State**: useState for component state
- **Context**: For shared state across components
- **Reducers**: For complex state logic
- **External Libraries**: Redux, Zustand integration

### Performance
- **Memoization**: React.memo, useMemo, useCallback
- **Code Splitting**: Dynamic imports and lazy loading
- **Bundle Optimization**: Tree shaking and minimization
- **Runtime Performance**: Efficient rendering patterns

### Testing
- **Unit Tests**: Individual component testing
- **Integration Tests**: Component interaction testing
- **E2E Tests**: Full user workflow testing
- **Accessibility Tests**: Screen reader compatibility

## Usage Examples

### Component Analysis
```python
analysis = analyze_react_prompt("""
Create a shopping cart component with add/remove functionality,
quantity updates, total calculation, and checkout integration.
""")
print(f"Score: {analysis['score']}")
print(f"Recommendations: {analysis['recommendations']}")
```

### Template Generation
```python
template = get_prompt_template("server_component")
# Returns structured template for React 19 Server Components
```

### Requirement Validation
```python
validation = validate_react_requirements("""
Project: E-commerce Dashboard
Components: ProductList, CartSummary, UserProfile
Features: Authentication, data fetching, form handling
Testing: Jest, React Testing Library
Performance: Code splitting, lazy loading
""")
```

### Prompt Optimization
```python
optimized = generate_optimized_prompt(
    "User authentication system",
    project_type="application",
    detail_level="complete"
)
# Returns comprehensive prompt with all requirements
```

## Component Patterns

### Functional Components
```javascript
function UserProfile({ user, onUpdate }) {
  const [editing, setEditing] = useState(false);
  
  return (
    <div className="user-profile">
      {editing ? (
        <EditForm user={user} onSave={onUpdate} />
      ) : (
        <DisplayView user={user} onEdit={() => setEditing(true)} />
      )}
    </div>
  );
}
```

### Custom Hooks
```javascript
function useAuth() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    // Authentication logic
  }, []);
  
  return { user, loading, login, logout };
}
```

### Server Components (React 19)
```javascript
async function ProductList() {
  const products = await fetchProducts();
  
  return (
    <div>
      {products.map(product => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
}
```

## Configuration

Environment variables:
- `MCP_SERVER_PORT`: Server port (default: 3004)
- `MCP_SERVER_PROTOCOL`: Communication protocol (default: stdio)
- `REACT_VERSION`: Target React version (default: 19)

## Dependencies

- **FastMCP**: 2.4.0+
- **Pydantic**: For data validation
- **Python**: 3.12+
- **React Knowledge Base**: Built-in React patterns library

## Performance

- **Analysis Speed**: < 150ms for prompt analysis
- **Template Generation**: < 100ms for template retrieval  
- **Memory Usage**: Efficient pattern caching
- **Concurrent Operations**: Multiple analysis support

---

*This server is part of the MCP Servers Collection developed by Charleno Pires*