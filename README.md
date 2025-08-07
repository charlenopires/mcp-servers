# 🚀 MCP Servers v2.1 - Modern Interactive CLI Collection

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![FastMCP](https://img.shields.io/badge/FastMCP-2.4.0%2B-green)](https://github.com/fastmcp/fastmcp)
[![uv](https://img.shields.io/badge/uv-Package%20Manager-purple)](https://github.com/astral-sh/uv)
[![License](https://img.shields.io/badge/License-MIT-orange)](LICENSE)
[![CLI](https://img.shields.io/badge/Interactive%20CLI-Vue%20Style-cyan)](https://questionary.readthedocs.io/)
[![Tests](https://img.shields.io/badge/Tests-32%2F37%20Passed-green)](https://pytest.org/)

**Modern interactive platform** of MCP (Model Context Protocol) servers with **Vue CLI-style multi-select interface** for specialized prompt processing, containerization, and modern web development.

## 🌟 Version 2.1 Features

### 🎯 **NEW: Interactive CLI Experience**

- **Vue CLI-style Interface**: Multi-select checkboxes for server selection
- **Rich Formatted Output**: Colorized tables, progress bars, and status indicators  
- **Smart Categorization**: Servers grouped by function (Analysis, Frontend, Backend, DevOps)
- **Real-time Monitoring**: Live server status and graceful shutdown handling

### 🚀 Centralized Management

- **Multiple Launchers**: Choose between CLI (`launcher_cli.py`), main (`main.py`), or shell (`run_servers.sh`)
- **Execution Modes**: Development, Production, and Silent modes with parallel/sequential options
- **Asynchronous Architecture**: Native async/await support with concurrent server management

### 🛠️ Modern Build System

- **uv Package Manager**: Ultra-fast dependency management
- **Rich Dependencies**: questionary, rich, colorama for enhanced UX
- **pyproject.toml**: Centralized project configuration
- **Build System**: Hatchling with optimized packaging

## 🌟 Overview

MCP Servers is a collection of specialized servers based on the MCP (Model Context Protocol) that provide tools for prompt analysis and optimization. This project presents a modular approach to working with different aspects of prompt engineering and MCP server development.

### ✨ Key Features

- 🎯 **Interactive Multi-Select CLI**: Vue CLI-style checkbox interface for server selection
- 📊 **Rich Status Dashboard**: Real-time server monitoring with colorized output
- 🔍 **MCP Prompt Analysis**: Advanced prompts evaluation with scoring systems
- 📝 **Prompt Engineering**: Multi-framework optimization (CRISPE, RACE, TRACE)
- 🐳 **Docker Optimization**: Container security best practices and multi-stage builds
- 🎨 **Modern Frontend Tools**: Tailwind v4.1, React 19, shadcn/ui support
- 🦀 **Backend Excellence**: Rust idiomatic patterns and Axum web framework
- ⚡ **Parallel Execution**: Concurrent server management with graceful shutdown
- 🔧 **Multiple Interfaces**: CLI, terminal menu, or programmatic access

## 📦 Available Servers

### 1. ✅ MCP Prompt Analyzer (`mcp_server.py`) - **FUNCTIONAL**

Analyzes prompts for MCP server creation, scoring them (1-10) and providing specific recommendations based on MCP documentation best practices.

**Tools:**

- `mcp_analyze_server_prompt` - Complete prompt analysis
- `mcp_get_best_practices` - Information about best practices
- `mcp_suggest_prompt_improvements` - Specific suggestions
- `mcp_validate_requirements` - Validation against MCP requirements

### 2. ✅ Prompt Engineering Server (`prompt_server.py`) - **FUNCTIONAL**

Optimizes prompts for different tasks using advanced prompt engineering strategies.

**Tools:**

- `prompt_optimize_generic` - Applies optimization techniques
- `prompt_analyze_generic` - Evaluates prompt structure
- `prompt_suggest_framework` - Applies different strategies
- `prompt_apply_technique` - Creates templates for different scenarios
- `prompt_check_bias` - Checks for potential biases in prompts

### 3. ✅ Tailwind CSS v4.1 Server (`tailwind_server.py`) - **FUNCTIONAL**

Provides context and support for development with Tailwind CSS v4.1.

**Tools:**

- `tailwind_contextualize_prompt` - Summary of v4.1 features
- `tailwind_get_v4_info` - Helps with migration between versions
- `tailwind_generate_v4_code` - Optimizes class usage
- `tailwind_get_v4_docs` - Creates components following best practices
- `tailwind_get_v4_examples` - Provides code examples for v4.1 features

### 4. ✅ React Optimizer Server (`react_optimizer_server.py`) - **FUNCTIONAL** 🆕

Unified server for analysis/optimization of existing React code and prompt optimization for modern React code generation following UI/UX 2025 trends.

**Main Features:**

- 🔍 **Code Analysis**: Evaluates existing React components with scoring and recommendations
- ⚡ **Automatic Optimization**: Applies 2025 trends automatically (glassmorphism, dark mode, micro-animations)
- 📝 **Prompt Analysis**: Evaluates quality of prompts for React code generation
- 🚀 **Prompt Optimization**: Transforms basic prompts into structured versions for AI tools

**Tools:**

- `react_optimizer_analyze_code` - Analysis of existing React code
- `react_optimizer_optimize_code` - Automatic optimization with 2025 trends
- `react_optimizer_analyze_prompt` - Prompt quality analysis
- `react_optimizer_optimize_prompt` - Prompt optimization for AI tools (v0.dev, Cursor, etc.)
- `react_optimizer_validate_prompt_quality` - Development workflow generation
- `react_optimizer_get_trends_2025` - React 2025 best practices
- `react_optimizer_generate_component_template` - Component integration validation

**Supported UI/UX 2025 Trends:**

- 🪟 Glassmorphism and glass effects
- 🌙 Dark mode as primary default
- ✨ Micro-animations and interactions
- 🎨 Bold and maximalist typography
- 🔗 Interactive 3D elements
- ♿ WCAG 2.1 AA accessibility

**AI Tools Integration:**

- v0.dev (Vercel), Cursor AI, GitHub Copilot, Visual Copilot

### 5. ✅ shadcn/ui Advanced Server (`shadcn_server.py`) - **FUNCTIONAL** 🆕

Advanced MCP server for complete shadcn/ui integration, offering intelligent analysis, optimized generation, and component customization following library best practices.

**Main Features:**

- 🔍 **Intelligent Analysis**: Detects shadcn/ui components in code with dependency analysis
- ⚡ **Automatic Optimization**: Applies best practices (React.memo, cn() utility, ARIA roles)
- 🎨 **Component Generation**: Optimized TypeScript templates for 10+ components
- 🌙 **Theme Creation**: Custom theme generator with dark mode support
- 📋 **Setup Guides**: Framework-specific configuration for Next.js, Vite, Remix, Astro

**Tools:**

- `shadcn_analyze_component` - Code analysis with shadcn/ui components
- `shadcn_optimize_component` - Automatic optimization with best practices
- `shadcn_generate_component` - Custom component generation
- `shadcn_get_component_info` - Detailed component information
- `shadcn_get_setup_guide` - Configuration guides by framework
- `shadcn_create_theme` - Custom theme creator
- `shadcn_get_best_practices` - Recommended patterns and practices

**Supported Components:**

- 🧩 Layout: Accordion, Card, Dialog
- 📝 Forms: Button, Input, Select, Form (React Hook Form + Zod)
- 📊 Data Display: Table, Badge
- 🔔 Feedback: Toast, Alert Dialog
- 🎨 Advanced: Compound Components, Custom Hooks, TypeScript interfaces

**Supported Frameworks:**

- Next.js, Vite, Remix, Astro, React Router

### 6. ✅ FastMCP Server (`fastmcp_server.py`) - **FUNCTIONAL**

Optimized server using FastMCP for MCP prompt analysis with advanced analysis and template generation features.

**Tools:**

- `fastmcp_analyze_mcp_prompt` - Advanced MCP prompt analysis with scoring
- `fastmcp_suggest_prompt_improvements` - Specific improvement suggestions
- `fastmcp_validate_requirements` - Complete MCP requirements validation
- `fastmcp_generate_server_template` - Server template generation

**Resources:**

- `mcp://best-practices` - Updated MCP best practices
- `mcp://prompt-examples/{level}` - Prompt examples by level
- `mcp://prompt-frameworks` - Prompt analysis frameworks

### 7. ✅ React 19 Advanced Server (`react_server.py`) - **FUNCTIONAL** 🆕

Advanced MCP server for React 19 development with modern features, including Server Components, Actions, and complete integration with modern frameworks.

**Main Features:**

- ⚛️ **React 19 Features**: Stable Server Components, Actions, `use` hook
- 🎯 **Prompt Analysis**: Evaluates React prompts with scoring and suggestions
- 🏗️ **Modern Templates**: Optimized templates for components and applications
- 🔧 **Requirements Validation**: Complete checklist for React projects
- 📊 **Best Practices**: Conformance with React 2025 standards

**Tools:**

- `react19_analyze_prompt` - Prompt analysis with scoring and feedback
- `react19_get_prompt_template` - Optimized templates for different project types
- `react19_suggest_contextual_improvements` - Context-specific improvements
- `react19_validate_requirements` - Essential requirements validation
- `react19_generate_optimized_prompt` - Automatic structured prompt generation
- `react19_get_server_resources` - Information about server resources

**Supported React 19 Features:**

- 🚀 **Server Components**: Server-side rendering with optimized performance
- ⚡ **Actions**: Automatic form handling with pending states
- 🎣 **`use` Hook**: Asynchronous resource consumption
- 🔄 **Ref as Prop**: No need for forwardRef
- 📝 **Enhanced Forms**: Advanced validation and handling

**Supported Frameworks:**

- Next.js 15+, Vite 6+, Remix 2.0+, Create React App

### 8. ✅ Rust Idiomatic Server (`rust_server.py`) - **FUNCTIONAL** 🆕

MCP server refactored to follow idiomatic Rust patterns based on the `mre/idiomatic-rust` repository and official `rust-lang/api-guidelines`.

**Main Features:**

- 🦀 **Idiomatic Analysis**: Detects idiomatic patterns and anti-patterns
- 🔧 **Immutability by Default**: Analysis of correct `mut` usage
- 🛡️ **Ergonomic Error Handling**: Result/Option with thiserror/anyhow
- 🔄 **Type Conversions**: From/Into traits for elegant conversions
- 🎯 **Enums over Booleans**: Detection of problematic boolean flags
- ⚡ **Async Patterns**: Idiomatic Tokio and async/await
- 🏗️ **API Design**: Conformance with rust-lang/api-guidelines

**Idiomatic Tools:**

- `rust_analyze_idiomatic_code` - Idiomatic analysis with scoring by category
- `rust_generate_idiomatic_project` - Project generation following idiomatic patterns
- `rust_get_idiomatic_patterns` - Complete pattern library with examples
- `rust_refactor_to_idiomatic` - Automatic refactoring to idiomatic code
- `rust_get_api_guidelines` - Official guidelines organized by category

**Analysis Categories:**

- 🔧 **Immutability**: "Aim for immutability by default" with mut analysis
- 🛡️ **Error Handling**: Result over panic, context preservation
- 🔄 **Type Conversions**: Ergonomic From/Into/TryFrom patterns
- 🎯 **Enums over Bools**: Expressiveness through enums
- ⚡ **Async Patterns**: Idiomatic async/await with Tokio
- 🏗️ **API Design**: snake_case, PascalCase, documentation
- 🚀 **Performance**: Zero-cost abstractions, iterator chains
- 📚 **Documentation**: Doc comments with testable examples

### 9. ✅ Axum Web Framework Server (`axum_server.py`) - **FUNCTIONAL** 🆕

Advanced MCP server for Axum web framework development following official best practices and magic patterns from the Rust ecosystem.

**Main Features:**

- 🕸️ **Axum Analysis**: Detects Axum patterns and analyzes handler quality
- 🔧 **Magic Patterns**: Implements advanced patterns from rust-magic-patterns
- 🛡️ **Security Best Practices**: CORS, authentication, input validation
- ⚡ **Performance Optimization**: Async handlers, connection pooling
- 🏗️ **Project Generation**: Complete project structures with different architectures

**Tools:**

- `axum_analyze_code` - Axum code analysis with pattern detection
- `axum_generate_project` - Complete project generation
- `axum_get_patterns` - Pattern library with practical examples
- `axum_optimize_handler` - Handler optimization with best practices
- `axum_get_magic_patterns` - Magic patterns from rust ecosystem
- `axum_create_middleware` - Custom middleware creation

### 10. ✅ Docker Optimizer Server (`docker_optimizer_server.py`) - **FUNCTIONAL** 🆕

Advanced MCP server for Docker containerization with focus on prompt optimization and best practices implementation following 2025 container security standards.

**Main Features:**

- 🐳 **Docker Prompt Analysis**: Evaluates Docker prompts with 0-100 scoring system
- 🔧 **Automatic Enhancement**: Transforms basic prompts into production-ready specifications
- 🛡️ **Security Best Practices**: Non-root users, minimal images, vulnerability scanning
- ⚡ **Multi-stage Optimization**: Intelligent layer caching and size reduction
- 🏗️ **Complete Configuration**: Dockerfile + docker-compose + .dockerignore generation

**Tools:**

- `docker_analyze_prompt` - Docker prompt analysis with detailed feedback
- `docker_enhance_prompt` - Automatic prompt enhancement with best practices
- `docker_validate_dockerfile` - Dockerfile validation against security standards
- `docker_generate_config` - Complete Docker configuration generation

**Supported Technologies:**

- 🐍 Python (FastAPI, Django, Flask)
- 🟢 Node.js (Express, Next.js, React)
- 🦀 Rust (Axum, Actix)
- 🐹 Go (Gin, Echo)

**2025 Best Practices:**

- 🛡️ Security-first approach with non-root execution
- 🚀 Multi-stage builds for optimal image sizes
- 🔍 Health checks and monitoring integration
- 📋 Production-ready docker-compose configurations
- 🎯 Framework-specific optimizations

### 🚧 Servers in Development

### TypeScript MCP Server (`typescript_server.py`) - **IN DEVELOPMENT**

Portuguese-language MCP server for TypeScript server creation analysis following MCP best practices.

**Tools (In Development):**

- `typescript_analyze_mcp_prompt` - Análise completa de prompt para MCP
- `typescript_get_mcp_best_practices` - Melhores práticas de desenvolvimento MCP
- `typescript_suggest_prompt_improvements` - Sugestões específicas de melhorias
- `typescript_validate_mcp_requirements` - Validação contra requisitos MCP

## 🛠️ Installation

### Prerequisites

- Python 3.12+
- uv (Universal Python Package Manager)

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/user/mcp-servers.git
cd mcp-servers

# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies and create virtual environment
uv sync

# 🎯 Try the modern interactive CLI (recommended)
uv run mcp_servers

# 📊 Check server status with rich formatting  
uv run mcp_servers --status

# Alternative ways to launch
python launcher_cli.py
uv run python launcher_cli.py

# 🔧 Traditional command-line interface
uv run python main.py --help
```

## 🚀 Quick Usage

### 🎯 **Modern Interactive CLI (Recommended)**

Experience the Vue CLI-style interface with multi-select checkboxes:

```bash
# Launch interactive CLI with multi-select (recommended)
uv run mcp_servers

# Show rich server status dashboard
uv run mcp_servers --status

# Alternative direct calls
python launcher_cli.py
uv run python launcher_cli.py

# Quick demo of all features
uv run python demo_cli.py
```

**Interactive Features:**
- 🚀 **Quick Start All**: One-click option to launch all functional servers
- ✅ **Multi-select servers** with checkboxes (↑↓ navigate, SPACE select)
- ⚙️ **Execution modes**: Development, Production, Silent
- 🔄 **Parallel options**: Run servers simultaneously or sequentially  
- 📊 **Real-time monitoring** with colored progress indicators
- 🛑 **Graceful shutdown** with Ctrl+C handling

### 🔧 **Traditional Command-Line**

Direct server execution for automation and scripting:

```bash
# Run specific servers
uv run python main.py mcp docker rust    # Multiple servers
uv run python main.py react_optimizer    # Single server with long name
uv run python main.py all --dev         # All servers in development mode

# Custom port and options
uv run python main.py mcp --port 3001   # Custom port
uv run python main.py tailwind --quiet  # Quiet mode

# Complete help and server list
uv run python main.py --help
uv run python main.py list
```

### 🎨 **Interactive Menu Interface**

Traditional terminal menu with numbered options:

```bash
# Colored interactive menu
./run_servers.sh

# Direct commands
bash run_servers.sh docker
bash run_servers.sh status
```

### Run Tests

```bash
# All tests (using modernized runner)
uv run python run_tests.py

# Specific test by module
uv run python run_tests.py mcp_server
uv run python run_tests.py prompt_server
uv run python run_tests.py tailwind_server

# Using pytest directly
uv run python -m pytest tests/ -v

# With detailed report
uv run python run_tests.py --verbose
```

## ⚡ Quick Start Examples

### 🎯 **Scenario 1: Frontend Development**

Select React, Tailwind, and shadcn/ui servers for modern frontend development:

```bash
# Interactive multi-select (recommended)
uv run mcp_servers
# Select: React Optimizer + Tailwind CSS + shadcn/ui + Development Mode

# Direct command
uv run python main.py react_optimizer tailwind shadcn --dev
```

### 🐳 **Scenario 2: Full-Stack Development Environment**

Complete development environment setup:

```bash
# Quick Start All - Launch all functional servers at once
uv run mcp_servers
# Select: 🚀 START ALL SERVERS (first option)

# Custom selection with rich interface
uv run mcp_servers --status  # Check all servers first
uv run mcp_servers           # Then select: Docker + React + Rust + Axum

# Command-line approach  
uv run python main.py docker rust axum react --dev
```

### 🔍 **Scenario 3: Prompt Engineering Workflow**

MCP server development and prompt optimization:

```bash
# Quick demo of interactive features
uv run python demo_cli.py

# Full prompt engineering stack
uv run mcp_servers
# Select: MCP Analysis + Prompt Engineering + FastMCP + Production Mode
```

## 📋 Advanced Usage

### 🎛️ **CLI Interface Comparison**

| Interface | Command | Best For | Features |
|-----------|---------|----------|----------|
| **Interactive CLI** | `uv run mcp_servers` | **Interactive Development** | Vue CLI-style, multi-select, rich output |
| **Direct CLI** | `uv run python launcher_cli.py` | **Development & Testing** | Same features, direct Python call |
| **Main Launcher** | `uv run python main.py` | **Automation & Scripts** | Direct commands, programmatic access |
| **Shell Menu** | `./run_servers.sh` | **Traditional Terminal** | Numbered menu, bash compatibility |

### 🔧 **Integration Examples**

```bash
# Development workflow with multiple interfaces
uv run mcp_servers --status           # Check server health  
uv run python main.py mcp --port 3001 # Start specific server
./run_servers.sh docker               # Traditional menu approach

# Automation and CI/CD
uv run python main.py all --quiet             # Silent bulk execution
uv run python main.py list | grep FUNCTIONAL  # Server validation
uv run python demo_cli.py > server_report.txt # Generate reports
```

### 📊 **Monitoring and Status**

```bash
# Rich formatted status dashboard
uv run mcp_servers --status

# Server health check for automation  
uv run python main.py list

# Traditional status with colors
./run_servers.sh status
```

## 🧪 Testing System v2.0

The v2.0 project includes a modernized testing system with pytest:

```bash
# Current test status
✅ 11/15 tests passing
⏭️ 4 tests skipped (servers in development)
⚠️ 1 warning (pytest-asyncio not installed)

# Run all tests
uv run python run_tests.py

# Specific tests by module
uv run python run_tests.py mcp_server      # ✅ 10/10 tests passing
uv run python run_tests.py prompt_server   # ✅ 1/1 test passing, 4 skipped
uv run python run_tests.py tailwind_server # 🚧 In development

# Using pytest directly
uv run python -m pytest tests/ -v

# With coverage (requires pytest-cov)
uv run python -m pytest tests/ --cov=servers --cov-report=term-missing
```

## 📁 Project Structure v2.0

```text
mcp-servers/
├── 🚀 main.py                  # Unified main launcher
├── 🎯 launcher_cli.py          # Modern interactive CLI (Vue CLI-style)
├── 🔧 pyproject.toml           # Project configuration (uv)
├── 🧪 run_tests.py             # Modernized test runner
├── 📜 run_servers.sh           # Interactive execution script
├── 📖 README.md                # This file
│
├── 🖥️ servers/                 # MCP servers
│   ├── ✅ mcp_server.py        # MCP prompt analyzer (functional)
│   ├── ✅ prompt_server.py     # Prompt engineering (functional)
│   ├── ✅ tailwind_server.py   # Tailwind CSS v4.1 support (functional)
│   ├── ✅ react_optimizer_server.py # React Optimizer (functional)
│   ├── ✅ shadcn_server.py     # shadcn/ui Advanced (functional)
│   ├── ✅ fastmcp_server.py    # FastMCP server (functional)
│   ├── ✅ react_server.py      # React server (functional)
│   ├── ✅ rust_server.py       # Rust Idiomatic server (functional)
│   ├── ✅ axum_server.py       # Axum Web Framework server (functional)
│   ├── ✅ docker_optimizer_server.py # Docker Optimizer server (functional)
│   └── 🚧 typescript_server.py # TypeScript server (in development)
│
├── 🧪 tests/                   # Tests with pytest (11/15 passing)
│   ├── ✅ test_mcp_server.py   # 10/10 MCP analyzer tests
│   ├── ✅ test_prompt_server.py # 1/1 prompt server test
│   └── 🚧 test_tailwind_server.py # Tailwind server tests
│
└── 📚 docs/                    # Complete documentation
    └── servers/                # Individual server documentation
        ├── mcp-analysis-server.md
        ├── prompt-engineering-server.md
        ├── tailwind-css-server.md
        ├── fastmcp-server.md
        ├── react-components-server.md
        ├── react-optimizer-server.md
        ├── shadcn-ui-server.md
        ├── rust-idiomatic-server.md
        └── axum-web-framework-server.md
```

## 📚 Server Documentation

Comprehensive documentation is available for each server:

### Core Analysis Servers
- 🔍 **[MCP Analysis Server](docs/servers/mcp-analysis-server.md)** - MCP prompt analysis and validation
- 📝 **[Prompt Engineering Server](docs/servers/prompt-engineering-server.md)** - Advanced prompt optimization techniques
- 🚀 **[FastMCP Server](docs/servers/fastmcp-server.md)** - Meta-server for MCP development

### Frontend & Design Servers  
- 🎨 **[Tailwind CSS Server](docs/servers/tailwind-css-server.md)** - Tailwind CSS v4.1 support and migration
- ⚛️ **[React Components Server](docs/servers/react-components-server.md)** - React 19 development support
- 🔧 **[React Optimizer Server](docs/servers/react-optimizer-server.md)** - React code analysis and AI prompt optimization
- 🎯 **[shadcn/ui Server](docs/servers/shadcn-ui-server.md)** - Advanced shadcn/ui component development

### Backend & Systems Servers
- 🦀 **[Rust Idiomatic Server](docs/servers/rust-idiomatic-server.md)** - Idiomatic Rust development patterns
- 🕸️ **[Axum Web Framework Server](docs/servers/axum-web-framework-server.md)** - Axum web development with tokio

Each documentation includes:
- **Feature Overview** - Core capabilities and use cases
- **Available Tools** - Complete API reference with examples
- **Usage Examples** - Practical implementation patterns
- **Best Practices** - Framework-specific recommendations
- **Configuration** - Setup and customization options

## 🌐 MCP Protocol (Model Context Protocol)

MCP is a protocol that allows extending language models with custom tools. Each server in this project implements specific MCP tools for different prompt processing domains.

### MCP v2.0 Design Principles

1. **Focused Design**: Each tool performs a specific and well-defined function
2. **Asynchronous Architecture**: Native support for asynchronous operations
3. **Robust Error Handling**: Robust validation of inputs and outputs
4. **Clear Documentation**: Each tool has detailed documentation
5. **Structured Inputs/Outputs**: Use of Pydantic for schema validation

## 📊 Scoring System

The MCP Prompt Analyzer evaluates prompts on specific criteria (1-10 scoring):

| Criterion                   | Description                          | Importance |
| -------------------------- | ---------------------------------- | ----------- |
| 🎯 Clear Purpose         | Specific and well-defined objective | High        |
| 🛠️ Tool Design   | Focused and well-named tools | High        |
| ⚠️ Error Handling     | Validation and exception handling | High        |
| 📝 Documentation            | Clear tool descriptions    | Medium       |
| 🔒 Security               | Recommended security practices | Medium       |
| 📋 Data Schema        | Well-defined data structures  | Medium       |
| ⚡ Performance             | Optimization considerations        | Low       |
| 🔧 Transport Protocol | Clear protocol specification   | Low       |

## 🧰 Development Tools v2.0

### Modern Build System

- **uv**: Ultra-fast Python package manager
- **pyproject.toml**: Centralized project configuration
- **Hatchling**: Modern and efficient build backend

### Interface Scripts

- 🎯 **uv run mcp_servers** - **Primary interactive CLI** with Vue-style multi-select checkboxes
- 🎯 **launcher_cli.py** - **Direct interactive CLI** (same features, direct Python call)
- 🚀 **main.py** - **Direct command launcher** for automation and scripting  
- 🔧 **run_servers.sh** - **Traditional terminal menu** with numbered options
- 🧪 **run_tests.py** - **Modernized test runner** with coverage reports
- 🎬 **demo_cli.py** - **Feature demonstration** and capability showcase

### Advanced Features

- 🎯 **Vue CLI-style Interface**: Checkbox selection with rich formatting and real-time feedback
- ⚡ **Asynchronous Execution**: Parallel server management with async/await patterns
- 📊 **Rich Status Dashboard**: Colorized tables, progress bars, and live monitoring
- 🔄 **Execution Modes**: Development (verbose), Production (optimized), Silent (minimal)
- 🛡️ **Graceful Shutdown**: Clean Ctrl+C handling with process termination
- 📋 **Smart Validation**: Real-time server file checking and dependency verification

## 📈 Project Status

### ✅ Implemented Features

- **Core Servers**: 10/11 functional servers (mcp, prompt, tailwind, react_optimizer, shadcn, fastmcp, react, rust, axum, docker)
- **Testing System**: 11/15 tests passing (73% success rate)
- **Build System**: Complete migration to uv + pyproject.toml
- **Documentation**: README v2.0 and updated docs/
- **Scripts**: Unified launcher and interactive interface

### 🚧 In Development

- **Additional Servers**: TypeScript (1/11 servers pending)
- **Remaining Tests**: 4 pending tests for new servers
- **Dependencies**: Optional pytest-asyncio and pytest-cov

### 🎯 Roadmap Next Versions

- [ ] **v2.1**: Implement remaining TypeScript server
- [ ] **v2.2**: Add support for English prompt analysis
- [ ] **v2.3**: Create REST API for remote access to servers
- [ ] **v2.4**: Develop web interface for result visualization
- [ ] **v2.5**: Integrate new prompt evaluation models

## 🤝 How to Contribute

Contributions are welcome! To contribute:

1. Fork the project on GitHub
2. Create a branch for your feature (`git checkout -b feature/new-tool`)
3. Commit your changes (`git commit -m 'Add new analysis tool'`)
4. Push to the branch (`git push origin feature/new-tool`)
5. Open a Pull Request

### Contribution Guidelines

- Add tests for new features
- Follow existing naming conventions
- Update documentation as needed
- Ensure code quality with linting tools

## 📜 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## 🙏 Acknowledgments

- [FastMCP](https://github.com/fastmcp/fastmcp) - Framework for MCP server development
- [Pydantic](https://docs.pydantic.dev/) - Data validation and schemas
- [uv](https://github.com/astral-sh/uv) - Ultra-fast Python package manager
- [Pytest](https://docs.pytest.org/) - Modern testing framework

---

**🚀 MCP Servers v2.0** | **Version**: 2.0 | **Python**: 3.12+ | **Status**: Production

_Developed with ❤️ by Charleno Pires_