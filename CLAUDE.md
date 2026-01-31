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
uv run python main.py fastmcp               # FastMCP high-performance server
uv run python main.py react                  # React 19 features + code analysis
uv run python main.py shadcn                 # shadcn/ui components
uv run python main.py rust                   # Rust idiomatic patterns
uv run python main.py axum                   # Axum web framework patterns
uv run python main.py docker                 # Docker optimization and best practices
uv run python main.py python                 # Python development optimizer
uv run python main.py typescript            # TypeScript analysis and Clean Architecture
uv run python main.py erlang                 # Erlang/OTP patterns
uv run python main.py elixir                 # Elixir functional programming
uv run python main.py phoenix                # Phoenix web framework
uv run python main.py phoenix_channels       # Phoenix Channels (WebSocket/PubSub)
uv run python main.py phoenix_liveview       # Phoenix LiveView real-time UI
uv run python main.py neo4j                  # Neo4j Cypher queries
uv run python main.py qdrant                 # Qdrant vector search
uv run python main.py htmx                   # HTMX + Axum integration

# Run all servers (development mode)
uv run python main.py all --dev

# Custom port
uv run python main.py mcp --port 3001
```

### Configuration Installation
```bash
# Install to all AI tools (Claude Desktop, Claude Code, Gemini CLI, etc.)
uv run python install_mcp_configs.py --all

# Install to specific tool
uv run python install_mcp_configs.py --claude-desktop
uv run python install_mcp_configs.py --claude-code
uv run python install_mcp_configs.py --gemini-cli

# List available servers
uv run python install_mcp_configs.py --list

# Show configuration paths
uv run python install_mcp_configs.py --paths
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

This is a **Model Context Protocol (MCP) servers collection** written in Python that provides specialized tools for prompt analysis, engineering, and modern web development. The project follows a modular architecture with 19 functional servers (19/19 complete, all servers functional).

### Core Architecture Components

**1. Centralized Launcher System**
- `main.py` - Unified server launcher with async support and process management
- `run_servers.sh` - Interactive shell interface with colored menu system
- `install_mcp_configs.py` - Configuration installer for AI tools
- Each server runs as independent MCP protocol-compliant process on different ports (3000-3018)

**2. Server Modules (`servers/` directory)**
All servers extend FastMCP framework and follow consistent patterns:
- Individual server files (e.g., `mcp_server.py`, `rust_server.py`)
- Each server defines tools via `@mcp.tool()` decorators
- Async/await patterns throughout for concurrent operations
- Pydantic models for type safety and validation

**3. Configuration Management**
- `pyproject.toml` - Modern Python project configuration with uv package manager
- Python 3.12+ requirement with FastMCP 3.0.0+ dependency
- Hatchling build system for packaging

### Server Specializations

**Analysis Servers (Ports 3000-3003):**
- **MCP Server** (`mcp_server.py`): Analyzes prompts for MCP server creation (1-10 scoring)
- **Prompt Server** (`prompt_server.py`): General prompt optimization using CRISPE/RACE frameworks
- **FastMCP Server** (`fastmcp_server.py`): Meta-server for generating other MCP servers

**Frontend Servers (Ports 3002, 3004, 3006, 3018):**
- **Tailwind Server** (`tailwind_server.py`): Tailwind CSS v4.1 migration and optimization
- **React Server** (`react_server.py`): React 19 features + code analysis/optimization
- **shadcn/ui Server** (`shadcn_server.py`): Component analysis, generation, and theming
- **HTMX Server** (`htmx_server.py`): HTMX patterns with Axum (Rust) backend

**Backend Servers (Ports 3005, 3007-3008, 3010):**
- **TypeScript Server** (`typescript_server.py`): Modern TypeScript with Clean Architecture
- **Rust Server** (`rust_server.py`): Idiomatic Rust patterns (mre/idiomatic-rust)
- **Axum Server** (`axum_server.py`): Axum web framework patterns
- **Python Server** (`python_optimizer_server.py`): Python analysis and modern paradigms

**Elixir/Erlang Servers (Ports 3011-3015):**
- **Erlang Server** (`erlang_server.py`): OTP patterns, GenServer, Supervisor
- **Elixir Server** (`elixir_server.py`): Functional programming, concurrency
- **Phoenix Server** (`phoenix_server.py`): Controllers, routing, contexts
- **Phoenix Channels Server** (`phoenix_channels_server.py`): WebSocket, PubSub, Presence
- **Phoenix LiveView Server** (`phoenix_liveview_server.py`): Real-time UI, hooks, HEEx

**Database Servers (Ports 3016-3017):**
- **Neo4j Server** (`neo4j_server.py`): Cypher queries, graph modeling
- **Qdrant Server** (`qdrant_server.py`): Vector search, RAG patterns

**DevOps Servers (Port 3009):**
- **Docker Server** (`docker_optimizer_server.py`): Docker containerization with security best practices

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
- Most servers implement 0-100 scoring systems for code/prompt quality
- Detailed feedback with categories, suggestions, and refactoring examples
- Anti-pattern detection with idiomatic alternatives

**Knowledge Base Pattern:**
- Each specialized server contains extensive knowledge bases (e.g., `RustIdiomaticKnowledgeBase`)
- Pattern libraries with good/bad examples
- Best practices from authoritative sources (rust-lang/api-guidelines, React docs, Phoenix docs, etc.)

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
6. Run `install_mcp_configs.py` to update AI tool configurations

### Configuration Paths

The `install_mcp_configs.py` script manages configurations for:
- **Claude Desktop**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Claude Code**: `~/.claude.json`
- **Gemini CLI**: `~/.gemini/settings.json`
- **Antigravity**: `~/.gemini/antigravity/mcp_config.json`
- **VSCode Insiders**: `~/Library/Application Support/Code - Insiders/User/mcp.json`

The project emphasizes Brazilian Portuguese documentation and comments while maintaining English code interfaces for international compatibility.
