# 🐍 Python Development Optimizer Server

**Server ID**: `python`  
**Port**: 3011  
**Status**: ✅ **FUNCTIONAL**  
**Version**: 1.0.0

## 📖 Overview

The Python Development Optimizer is an advanced MCP server designed for comprehensive Python code analysis, optimization, and modern development paradigm support. It provides intelligent analysis of Python prompts and code, following 2025 best practices including Clean Code principles, PEP 8 compliance, and comprehensive type safety.

## 🎯 Main Features

### 🔍 **Prompt Analysis & Enhancement**
- **Paradigm Detection**: Automatically detects intended programming paradigm (OOP, Functional, Async, Hybrid)
- **Quality Scoring**: 0-100 scoring system based on clarity, completeness, and best practices
- **Smart Enhancement**: Transforms basic prompts into comprehensive specifications
- **Best Practices Integration**: Adds PEP 8, type hints, and Clean Code considerations

### 🏗️ **Template Generation**
- **Paradigm-Specific Templates**: Creates code templates for different programming approaches
- **Testing Setup**: Includes pytest configuration and test examples
- **Type Safety**: Comprehensive type hints with Pydantic models
- **Documentation**: Auto-generates docstrings and usage examples

### 🧪 **Code Validation & Analysis**
- **Syntax Validation**: Comprehensive Python syntax checking
- **PEP 8 Compliance**: Style guide validation and recommendations
- **Type Hint Coverage**: Analyzes function type annotation completeness
- **Complexity Analysis**: Cyclomatic complexity assessment and optimization suggestions

### ⚡ **Intelligent Refactoring**
- **Code Optimization**: Performance and readability improvements
- **Pattern Recognition**: Identifies and suggests design patterns
- **Paradigm Migration**: Helps transition between programming paradigms
- **Security Analysis**: Identifies potential security issues and fixes

## 🛠️ Available Tools

### 1. `analyze_python_prompt`
**Purpose**: Analyze Python prompts for quality and completeness

**Parameters**:
- `prompt` (str): Python code creation prompt to analyze
- `check_paradigm` (bool, optional): Enable paradigm detection (default: true)

**Returns**:
```json
{
  "score": 85.5,
  "paradigm_detected": "object_oriented",
  "complexity_level": "intermediate", 
  "strengths": ["Clear requirements", "Mentions testing"],
  "weaknesses": ["Missing type hints requirement"],
  "missing_elements": ["Error handling specification"],
  "recommendations": ["Add PEP 8 compliance requirement"],
  "pep8_compliance": false,
  "has_type_hints": false,
  "has_clean_code": true
}
```

**Use Cases**:
- Quality assessment before code generation
- Prompt optimization for AI tools
- Requirements completeness validation

### 2. `enhance_python_prompt`
**Purpose**: Transform basic prompts into comprehensive specifications

**Parameters**:
- `prompt` (str): Original prompt to enhance
- `paradigm` (str, optional): Target paradigm ("object_oriented", "functional", "asynchronous", "hybrid")
- `complexity` (str, optional): Target complexity ("beginner", "intermediate", "advanced", "expert")
- `include_tests` (bool, optional): Include testing requirements (default: true)
- `include_examples` (bool, optional): Include usage examples (default: true)

**Returns**:
```json
{
  "original_prompt": "Create a user class",
  "enhanced_prompt": "Create a comprehensive user management system following object-oriented principles...",
  "paradigm": "object_oriented",
  "added_patterns": ["Repository Pattern", "Factory Pattern"],
  "code_template": "# Generated template code...",
  "best_practices": ["Type hints", "PEP 8", "Docstrings"],
  "estimated_loc": 150
}
```

**Use Cases**:
- Prompt optimization for AI code generation
- Requirements expansion and clarification
- Best practices integration

### 3. `validate_python_code`
**Purpose**: Validate Python code against modern standards

**Parameters**:
- `code` (str): Python code to validate
- `check_paradigm` (bool, optional): Enable paradigm adherence checking (default: true)
- `strict_mode` (bool, optional): Enable strict validation (default: false)

**Returns**:
```json
{
  "is_valid": true,
  "syntax_errors": [],
  "pep8_violations": ["Line 45: Line too long"],
  "type_hint_coverage": 85.0,
  "complexity_score": 12,
  "paradigm_adherence": {"object_oriented": 92.5},
  "suggestions": ["Add type hints to function parameters"]
}
```

**Use Cases**:
- Code quality assessment
- Pre-commit validation
- Refactoring planning

### 4. `generate_python_template`
**Purpose**: Generate paradigm-specific code templates

**Parameters**:
- `description` (str): Description of what to generate
- `paradigm` (str, optional): Target paradigm (default: "object_oriented")
- `include_tests` (bool, optional): Include test files (default: true)
- `include_main` (bool, optional): Include main execution block (default: true)

**Returns**:
```json
{
  "code_template": "# Complete template with type hints and docstrings...",
  "test_template": "# Corresponding pytest test suite...",
  "requirements": ["pydantic>=2.0", "pytest>=7.0"],
  "paradigm_features": ["Classes", "Inheritance", "Polymorphism"],
  "setup_instructions": ["Install dependencies", "Run tests"]
}
```

**Use Cases**:
- Quick project scaffolding
- Paradigm learning and examples
- Consistent code structure

### 5. `suggest_refactoring`
**Purpose**: Provide intelligent refactoring suggestions

**Parameters**:
- `code` (str): Code to analyze for refactoring
- `target_paradigm` (str, optional): Target paradigm for migration
- `focus_areas` (list[str], optional): Specific areas to focus on

**Returns**:
```json
{
  "original_code": "def process_data(data): ...",
  "refactored_code": "def process_data(data: List[Dict[str, Any]]) -> ProcessedData: ...",
  "changes_made": ["Added type hints", "Extracted helper functions"],
  "improvements": ["Better readability", "Type safety"],
  "performance_impact": "Minimal impact, better maintainability"
}
```

**Use Cases**:
- Code modernization
- Performance optimization
- Paradigm migration

### 6. `get_best_practices`
**Purpose**: Retrieve comprehensive Python best practices guide

**Parameters**: None

**Returns**:
```json
{
  "practices": {
    "pep8": {
      "principles": ["Line length ≤79 characters", "4-space indentation"],
      "examples": [{"good": "snake_case", "bad": "camelCase"}]
    },
    "type_hints": {
      "principles": ["Use explicit types", "Prefer Union over Optional"],
      "examples": [{"good": "def func(x: int) -> str:", "bad": "def func(x):"}]
    }
  },
  "last_updated": "2025",
  "categories": ["PEP 8", "Type Hints", "Clean Code", "Testing", "Security"]
}
```

**Use Cases**:
- Developer education and reference
- Code review guidelines
- Team standards establishment

### 7. `get_paradigm_guide`
**Purpose**: Get paradigm-specific development guides

**Parameters**:
- `paradigm` (str): Target paradigm to get guide for

**Returns**:
```json
{
  "paradigm": "functional",
  "principles": ["Immutability", "Pure functions", "Higher-order functions"],
  "patterns": ["Map/Filter/Reduce", "Monads", "Currying"],
  "examples": {
    "pure_function": "def add(x: int, y: int) -> int: return x + y",
    "immutable_data": "from typing import NamedTuple..."
  },
  "libraries": ["functools", "itertools", "toolz"],
  "best_practices": ["Avoid side effects", "Prefer composition over inheritance"]
}
```

**Use Cases**:
- Paradigm learning and reference
- Code review for paradigm adherence
- Team training materials

### 8. `get_solid_principles`
**Purpose**: Get SOLID principles implementation guide

**Parameters**: None

**Returns**:
```json
{
  "principles": {
    "single_responsibility": {
      "description": "A class should have only one reason to change",
      "example": "class UserValidator: ...",
      "violations": ["God objects", "Multiple responsibilities"]
    }
  },
  "implementation_examples": {
    "python_specific": "Examples using Python idioms..."
  },
  "common_violations": ["Fat interfaces", "Tight coupling"],
  "refactoring_techniques": ["Extract class", "Interface segregation"]
}
```

**Use Cases**:
- Object-oriented design guidance
- Code review and refactoring
- Architecture planning

## 🎯 Supported Programming Paradigms

### 🏛️ **Object-Oriented Programming**
**Features**:
- Class design and inheritance hierarchies
- SOLID principles implementation
- Design patterns (Factory, Observer, Strategy, etc.)
- Encapsulation and abstraction patterns

**Generated Templates Include**:
- Base classes with proper inheritance
- Abstract base classes and interfaces
- Property decorators and descriptors
- Comprehensive docstrings and type hints

### 🔄 **Functional Programming** 
**Features**:
- Pure function design and composition
- Immutable data structures
- Higher-order functions and decorators
- Monadic patterns and error handling

**Generated Templates Include**:
- Pure function libraries
- Immutable data classes with frozen dataclasses
- Function composition utilities
- Functional error handling with Result types

### ⚡ **Asynchronous Programming**
**Features**:
- async/await patterns and best practices
- Concurrent programming with asyncio
- Stream processing and reactive patterns
- Performance optimization techniques

**Generated Templates Include**:
- Async context managers and decorators
- Concurrent task management
- Stream processing pipelines
- Error handling in async contexts

### 🔀 **Hybrid Approaches**
**Features**:
- Combining multiple paradigms effectively
- Object-oriented async programming
- Functional reactive programming
- Domain-driven design patterns

**Generated Templates Include**:
- Async classes with functional methods
- Event-driven architectures
- CQRS and Event Sourcing patterns
- Clean Architecture implementations

## 📋 Configuration & Setup

### Installation
```bash
# Install dependencies
uv sync

# Run Python optimizer server
uv run python main.py python

# Alternative direct launch
uv run python -m servers.python_optimizer_server
```

### Environment Variables
```bash
MCP_SERVER_PORT=3011        # Server port (default: 3011)
MCP_SERVER_PROTOCOL=stdio   # Protocol (default: stdio)
```

### Integration with IDEs
The server can be integrated with various development environments:
- **VS Code**: Use MCP extension for direct integration
- **PyCharm**: Configure as external tool
- **Vim/Neovim**: Use MCP clients for integration
- **Cursor AI**: Optimized prompts for enhanced code generation

## 🧪 Testing & Quality Assurance

### Running Tests
```bash
# Run server-specific tests
uv run python run_tests.py python_optimizer_server

# Run all tests with coverage
uv run pytest tests/ --cov=servers.python_optimizer_server
```

### Quality Metrics
- **Code Coverage**: 95%+ for core functionality
- **Type Hint Coverage**: 100% for public APIs
- **PEP 8 Compliance**: Full compliance with exceptions documented
- **Documentation Coverage**: Complete API and usage documentation

## 🚀 Performance & Scalability

### Performance Characteristics
- **Analysis Speed**: ~100ms for typical prompts
- **Template Generation**: ~200ms for complex templates
- **Code Validation**: ~50ms for files up to 1000 lines
- **Memory Usage**: <50MB typical operation

### Scalability Features
- Async processing for concurrent requests
- Caching of frequently used templates
- Incremental analysis for large codebases
- Streaming responses for large outputs

## 🔧 Advanced Usage Examples

### Prompt Enhancement Workflow
```python
# 1. Analyze original prompt
analysis = await analyze_python_prompt(
    "Create a user management system"
)

# 2. Enhance based on analysis
enhanced = await enhance_python_prompt(
    "Create a user management system",
    paradigm="object_oriented",
    complexity="intermediate",
    include_tests=True
)

# 3. Generate template
template = await generate_python_template(
    enhanced["enhanced_prompt"],
    paradigm="object_oriented"
)
```

### Code Quality Pipeline
```python
# 1. Validate existing code
validation = await validate_python_code(
    code_content,
    check_paradigm=True,
    strict_mode=True
)

# 2. Get refactoring suggestions
suggestions = await suggest_refactoring(
    code_content,
    target_paradigm="functional",
    focus_areas=["performance", "readability"]
)

# 3. Apply best practices
practices = await get_best_practices()
```

### Learning and Reference
```python
# Get paradigm-specific guidance
oop_guide = await get_paradigm_guide("object_oriented")
functional_guide = await get_paradigm_guide("functional")

# Get architecture principles
solid_principles = await get_solid_principles()
```

## 🤝 Integration with Other Tools

### AI Code Generation Tools
- **v0.dev (Vercel)**: Optimized prompts for React/Next.js integration
- **Cursor AI**: Enhanced context for Python development
- **GitHub Copilot**: Structured prompts for better suggestions
- **Claude Code**: Native integration with Claude development workflow

### Python Development Stack
- **FastAPI**: Web API template generation
- **Django**: MVC pattern templates
- **Pydantic**: Data validation and serialization
- **pytest**: Testing framework integration
- **mypy**: Type checking integration

### DevOps and Deployment
- **Docker**: Container-ready templates
- **CI/CD**: GitHub Actions workflow generation
- **Monitoring**: Logging and metrics integration
- **Documentation**: Sphinx and MkDocs templates

## 📚 Related Documentation

- [MCP Analysis Server](mcp-analysis-server.md) - MCP prompt analysis
- [FastMCP Server](fastmcp-server.md) - MCP server generation
- [Docker Optimizer Server](docker-optimizer-server.md) - Containerization
- [React Optimizer Server](react-optimizer-server.md) - Frontend integration

## 🆕 Recent Updates

### Version 1.0.0 (Latest)
- ✅ **Complete Refactoring**: Migrated from Portuguese to English
- ✅ **Modern Python Support**: Python 3.12+ features and syntax
- ✅ **Paradigm Detection**: Automatic paradigm identification
- ✅ **Template Generation**: Comprehensive code templates
- ✅ **Enhanced Testing**: pytest integration and examples
- ✅ **Type Safety**: Full type hint coverage
- ✅ **Best Practices**: 2025 Python development standards

---

**🐍 Python Development Optimizer Server** | **Status**: Production Ready | **Maintained by**: MCP Servers Team