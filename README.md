# 🚀 MCP Servers v2.0 - Collection of MCP Servers

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![FastMCP](https://img.shields.io/badge/FastMCP-2.4.0%2B-green)](https://github.com/fastmcp/fastmcp)
[![uv](https://img.shields.io/badge/uv-Package%20Manager-purple)](https://github.com/astral-sh/uv)
[![License](https://img.shields.io/badge/License-MIT-orange)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-32%2F37%20Passed-green)](https://pytest.org/)

Modernized platform of MCP (Model Context Protocol) servers for specialized prompt processing, including MCP prompt analysis, prompt engineering, and Tailwind CSS v4.1 support.

## 🌟 Version 2.0 Features

### 🚀 Centralized Management

- **Main Launcher**: `main.py` unifies execution of all servers
- **Simplified Interface**: Modernized `run_servers.sh` and `run_tests.py` scripts
- **Asynchronous Execution**: Native support for asynchronous operations

### 🛠️ Modern Build System

- **uv Package Manager**: Complete migration from pip to uv
- **pyproject.toml**: Centralized project configuration
- **Build System**: Hatchling as build backend

### 🧪 Modernized Testing Framework

- **Pytest**: Professional testing framework
- **Code Coverage**: Integrated coverage reports
- **Parallel Tests**: Optimized test execution

## 🌟 Overview

MCP Servers is a collection of specialized servers based on the MCP (Model Context Protocol) that provide tools for prompt analysis and optimization. This project presents a modular approach to working with different aspects of prompt engineering and MCP server development.

### ✨ Key Features

- 🔍 **MCP Prompt Analysis**: Evaluates prompts for MCP server creation
- 📝 **Prompt Engineering**: Optimizes prompts for different tasks
- 🎨 **Tailwind CSS v4.1 Support**: Helps with prompts in the context of the new version
- 🧪 **Complete Testing**: 32/37 tests passing with comprehensive coverage
- 🚀 **Parallel Execution**: Scripts to run servers in parallel
- ⚡ **Modern Build System**: uv + pyproject.toml + hatchling
- 🔧 **Unified Launcher**: main.py centralizes execution of all servers

## 📦 Available Servers

### 1. ✅ MCP Prompt Analyzer (`mcp_server.py`) - **FUNCTIONAL**

Analyzes prompts for MCP server creation, scoring them (1-10) and providing specific recommendations based on MCP documentation best practices.

**Tools:**

- `analisar_prompt_mcp` - Complete prompt analysis
- `obter_melhores_praticas_mcp` - Information about best practices
- `sugerir_melhorias_prompt` - Specific suggestions
- `validar_requisitos_mcp` - Validation against MCP requirements

### 2. ✅ Prompt Engineering Server (`prompt_server.py`) - **FUNCTIONAL**

Optimizes prompts for different tasks using advanced prompt engineering strategies.

**Tools:**

- `optimize_prompt` - Applies optimization techniques
- `analyze_prompt` - Evaluates prompt structure
- `suggest_framework` - Applies different strategies
- `apply_advanced_technique` - Creates templates for different scenarios

### 3. ✅ Tailwind CSS v4.1 Server (`tailwind_server.py`) - **FUNCTIONAL**

Provides context and support for development with Tailwind CSS v4.1.

**Tools:**

- `contextualize_tailwind_prompt` - Summary of v4.1 features
- `get_tailwind_v4_info` - Helps with migration between versions
- `generate_tailwind_v4_code` - Optimizes class usage
- `get_tailwind_v4_docs` - Creates components following best practices

### 4. ✅ React Optimizer Server (`react_optimizer_server.py`) - **FUNCTIONAL** 🆕

Unified server for analysis/optimization of existing React code and prompt optimization for modern React code generation following UI/UX 2025 trends.

**Main Features:**

- 🔍 **Code Analysis**: Evaluates existing React components with scoring and recommendations
- ⚡ **Automatic Optimization**: Applies 2025 trends automatically (glassmorphism, dark mode, micro-animations)
- 📝 **Prompt Analysis**: Evaluates quality of prompts for React code generation
- 🚀 **Prompt Optimization**: Transforms basic prompts into structured versions for AI tools

**Tools:**

- `analyze_react_code` - Analysis of existing React code
- `optimize_react_code` - Automatic optimization with 2025 trends
- `analyze_react_prompt` - Prompt quality analysis
- `optimize_react_prompt` - Prompt optimization for AI tools (v0.dev, Cursor, etc.)
- `validate_prompt_quality` - Development workflow generation
- `get_react_trends_2025` - React 2025 best practices
- `generate_component_template` - Component integration validation

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

- `analyze_shadcn_component` - Code analysis with shadcn/ui components
- `optimize_shadcn_component` - Automatic optimization with best practices
- `generate_shadcn_component` - Custom component generation
- `get_shadcn_component_info` - Detailed component information
- `get_shadcn_setup_guide` - Configuration guides by framework
- `create_shadcn_theme` - Custom theme creator
- `get_shadcn_best_practices` - Recommended patterns and practices

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

- `analyze_mcp_prompt` - Advanced MCP prompt analysis with scoring
- `suggest_mcp_prompt_improvements` - Specific improvement suggestions
- `validate_mcp_requirements` - Complete MCP requirements validation
- `generate_mcp_server_template` - Server template generation

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

- `analisar_prompt_react` - Prompt analysis with scoring and feedback
- `obter_template_prompt` - Optimized templates for different project types
- `sugerir_melhorias_contextuais` - Context-specific improvements
- `validar_requisitos_react` - Essential requirements validation
- `gerar_prompt_otimizado` - Automatic structured prompt generation

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

- `analyze_idiomatic_rust` - Idiomatic analysis with scoring by category
- `generate_idiomatic_project` - Project generation following idiomatic patterns
- `get_idiomatic_patterns` - Complete pattern library with examples
- `refactor_to_idiomatic` - Automatic refactoring to idiomatic code
- `get_rust_api_guidelines` - Official guidelines organized by category

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

- `analyze_axum_code` - Axum code analysis with pattern detection
- `generate_axum_project` - Complete project generation
- `get_axum_patterns` - Pattern library with practical examples
- `optimize_axum_handler` - Handler optimization with best practices
- `get_axum_magic_patterns` - Magic patterns from rust ecosystem
- `create_axum_middleware` - Custom middleware creation

### 🚧 Servers in Development

- **TypeScript Server** (`typescript_server.py`) - In development

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

# Verify installation
python main.py --help
```

## 🚀 Quick Usage

### Main Launcher

The centralized launcher allows running all servers in a unified way:

```bash
# Run specific server
python main.py mcp          # MCP prompt analyzer
python main.py prompt       # Prompt engineering server
python main.py tailwind     # Tailwind CSS server
python main.py react_optimizer  # React Optimizer server
python main.py shadcn        # shadcn/ui Advanced server
python main.py rust          # Rust Idiomatic server
python main.py axum          # Axum Web Framework server

# Run all servers (development mode)
python main.py all

# Complete help
python main.py --help
```

### Interactive Interface

```bash
# Interface with colored menu (recommended)
./run_servers.sh

# Direct execution with options
bash run_servers.sh menu
bash run_servers.sh mcp
```

### Run Tests

```bash
# All tests (using modernized runner)
python run_tests.py

# Specific test by module
python run_tests.py mcp_server
python run_tests.py prompt_server
python run_tests.py tailwind_server

# Using pytest directly
uv run python -m pytest tests/ -v

# With detailed report
python run_tests.py --verbose
```

## ⚡ Quick Start

### 🎯 Complete Integration Demo

Run our demo that shows all servers working together:

```bash
# Complete integration demo
python docs/examples/complete_integration_demo.py
```

This demo demonstrates:

- ✅ Complete MCP prompt analysis
- ✅ Optimization with CRISPE/RACE/TRACE frameworks
- ✅ Tailwind v4.1 component creation
- ✅ Automatic MCP server generation
- ✅ End-to-end integrated workflow

## 📋 Usage Examples

### MCP Prompt Analysis

```python
# Using the library directly
from servers.mcp_server import AnalisadorPromptMCP

analisador = AnalisadorPromptMCP()
resultado = analisador.analisar_prompt(
    "Create an MCP server for Python code analysis"
)

print(f"Score: {resultado.pontuacao}/10")
print(f"Recommendations: {resultado.recomendacoes}")
```

### Execution via Launcher

```bash
# Complete interactive interface
./run_servers.sh

# Run all servers in development
python main.py all --dev

# Run specific servers in parallel
python main.py mcp prompt tailwind
```

## 🧪 Testing System v2.0

The v2.0 project includes a modernized testing system with pytest:

```bash
# Current test status
✅ 11/15 tests passing
⏭️ 4 tests skipped (servers in development)
⚠️ 1 warning (pytest-asyncio not installed)

# Run all tests
python run_tests.py

# Specific tests by module
python run_tests.py mcp_server      # ✅ 10/10 tests passing
python run_tests.py prompt_server   # ✅ 1/1 test passing, 4 skipped
python run_tests.py tailwind_server # 🚧 In development

# Using pytest directly
uv run python -m pytest tests/ -v

# With coverage (requires pytest-cov)
uv run python -m pytest tests/ --cov=servers --cov-report=term-missing
```

## 📁 Project Structure v2.0

```text
mcp-servers/
├── 🚀 main.py                  # Unified main launcher
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

### Automation Scripts

- 🚀 **main.py** - Centralized launcher for all servers
- 🔧 **run_servers.sh** - Interactive interface with colored menu
- 🧪 **run_tests.py** - Modernized test runner with reports

### Advanced Features

- ⚡ **Asynchronous Execution**: Native support for async/await operations
- 🔄 **Auto Reload**: Hot reload in development mode
- 📊 **Test Reports**: Coverage and detailed reports
- 🎨 **Colored Interface**: Colorized output for better UX
- 🛡️ **Signal Handling**: Clean shutdown with Ctrl+C

## 📈 Project Status

### ✅ Implemented Features

- **Core Servers**: 9/10 functional servers (mcp, prompt, tailwind, react_optimizer, shadcn, fastmcp, react, rust, axum)
- **Testing System**: 11/15 tests passing (73% success rate)
- **Build System**: Complete migration to uv + pyproject.toml
- **Documentation**: README v2.0 and updated docs/
- **Scripts**: Unified launcher and interactive interface

### 🚧 In Development

- **Additional Servers**: TypeScript (1/10 servers pending)
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