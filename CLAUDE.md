# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Essential Commands

### Development Setup
```bash
# Install dependencies using uv (required package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync

# Check system dependencies
./run_servers.sh status
```

### Server Management
```bash
# Modern interactive CLI with multi-select (recommended)
uv run mcp_servers

# Show server status with rich formatting  
uv run mcp_servers --status

# Alternative direct calls
python launcher_cli.py
uv run python launcher_cli.py

# Interactive server launcher with menu  
./run_servers.sh

# Run specific server
uv run python main.py mcp                    # MCP prompt analyzer
uv run python main.py prompt                 # Prompt engineering
uv run python main.py tailwind              # Tailwind CSS v4.1
uv run python main.py react_optimizer       # React code analysis/optimization  
uv run python main.py shadcn                 # shadcn/ui components
uv run python main.py rust                   # Rust idiomatic patterns
uv run python main.py react                  # React 19 features
uv run python main.py axum                   # Axum web framework patterns
uv run python main.py docker                 # Docker optimization and best practices
uv run python main.py python                 # Python development optimizer
uv run python main.py typescript            # TypeScript analysis and Clean Architecture

# Run all servers (development mode)
uv run python main.py all --dev

# Custom port
uv run python main.py mcp --port 3001
```

### Testing
```bash
# Run all tests
uv run python run_tests.py

# Run specific test file
uv run pytest tests/test_mcp_server.py -v

# Run with coverage
uv run pytest --cov=servers --cov-report=html

# Run single test function
uv run pytest tests/test_mcp_server.py::test_analisar_prompt_mcp -v
```

### Linting and Code Quality
```bash
# Run ruff linter (configured in pyproject.toml)
uv run ruff check .
uv run ruff format .

# Check specific file
uv run ruff check servers/mcp_server.py
```

## Architecture Overview

This is a **Model Context Protocol (MCP) servers collection** written in Python that provides specialized tools for prompt analysis, engineering, and modern web development. The project follows a modular architecture with 12 functional servers (12/12 complete, all servers functional).

### Core Architecture Components

**1. Centralized Launcher System**
- `main.py` - Unified server launcher with async support and process management
- `run_servers.sh` - Interactive shell interface with colored menu system
- Each server runs as independent MCP protocol-compliant process on different ports (3000-3010)

**2. Server Modules (`servers/` directory)**
All servers extend FastMCP framework and follow consistent patterns:
- Individual server files (e.g., `mcp_server.py`, `rust_server.py`)
- Each server defines tools via `@mcp.tool()` decorators
- Async/await patterns throughout for concurrent operations
- Pydantic models for type safety and validation

**3. Configuration Management**
- `pyproject.toml` - Modern Python project configuration with uv package manager
- Python 3.12+ requirement with FastMCP 2.4.0+ dependency
- Hatchling build system for packaging

### Server Specializations

**Language/Framework Servers:**
- **Python Server** (`python_optimizer_server.py`): Python code analysis, optimization, and modern paradigms (OOP, Functional, Async, Hybrid) following Clean Code principles
- **TypeScript Server** (`typescript_server.py`): Modern TypeScript 5.x development with Clean Architecture, SOLID principles, and AI tool integration
- **Rust Server** (`rust_server.py`): Idiomatic Rust patterns based on mre/idiomatic-rust repository with scoring system for code analysis
- **React Server** (`react_server.py`): React 19 features (Server Components, Actions, `use` hook)
- **React Optimizer** (`react_optimizer_server.py`): Unified React code analysis + prompt optimization for AI tools (v0.dev, Cursor)
- **shadcn/ui Server** (`shadcn_server.py`): shadcn/ui component analysis, generation, and theming
- **Axum Server** (`axum_server.py`): Axum web framework patterns and magic patterns from rust ecosystem

**DevOps/Infrastructure Servers:**
- **Docker Server** (`docker_optimizer_server.py`): Docker containerization with security best practices and multi-stage optimization

**Prompt Engineering Servers:**
- **MCP Server** (`mcp_server.py`): Analyzes prompts for MCP server creation (1-10 scoring system)
- **Prompt Server** (`prompt_server.py`): General prompt optimization using CRISPE/RACE frameworks
- **Tailwind Server** (`tailwind_server.py`): Tailwind CSS v4.1 migration and optimization

**High-Performance Server:**
- **FastMCP Server** (`fastmcp_server.py`): Meta-server for generating other MCP servers with templates

### Key Design Patterns

**Async-First Architecture:**
```python
# All server tools use async patterns
@mcp.tool()
async def analyze_rust_code(code: str) -> Dict[str, Any]:
    analyzer = RustIdiomaticAnalyzer()
    return await analyzer.analyze_idiomatic_rust(code)
```

**Scoring and Analysis Systems:**
- Most servers implement 0-100 or 1-10 scoring systems for code/prompt quality
- Detailed feedback with categories, suggestions, and refactoring examples
- Anti-pattern detection with idiomatic alternatives

**Knowledge Base Pattern:**
- Each specialized server contains extensive knowledge bases (e.g., `RustIdiomaticKnowledgeBase`)
- Pattern libraries with good/bad examples
- Best practices from authoritative sources (rust-lang/api-guidelines, React docs, etc.)

**Resource Management:**
- MCP resources via `@mcp.resource()` decorators for documentation
- JSON-based knowledge bases for extensibility
- Structured error handling with meaningful messages

### Integration Points

**Inter-Server Communication:**
- Servers designed to work independently or in integrated workflows
- Common data structures and response formats
- Shared utility patterns for prompt analysis and code generation

**External Tool Integration:**
- React Optimizer specifically designed for AI development tools (v0.dev, Cursor AI, GitHub Copilot)
- Git integration for commit message generation
- Build system integration with modern Python tooling (uv, pytest, ruff)

### Development Workflow

The codebase supports rapid development of new MCP servers:
1. Create new server file in `servers/` directory following existing patterns
2. Add server configuration to `main.py` SERVERS_CONFIG
3. Update `run_servers.sh` menu system
4. Add tests in `tests/` directory
5. Update documentation in `README.md`

The project emphasizes Brazilian Portuguese documentation and comments while maintaining English code interfaces for international compatibility.