# MCP Servers v2.3 - Modern Interactive CLI Collection

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![FastMCP](https://img.shields.io/badge/FastMCP-3.0.0%2B-green)](https://github.com/fastmcp/fastmcp)
[![uv](https://img.shields.io/badge/uv-Package%20Manager-purple)](https://github.com/astral-sh/uv)
[![License](https://img.shields.io/badge/License-MIT-orange)](LICENSE)
[![CLI](https://img.shields.io/badge/Interactive%20CLI-Vue%20Style-cyan)](https://questionary.readthedocs.io/)
[![Servers](https://img.shields.io/badge/Servers-19%2F19%20Functional-success)](https://github.com/)

**Modern interactive platform** of MCP (Model Context Protocol) servers with **Vue CLI-style multi-select interface** for specialized prompt processing, containerization, and modern web development.

## Version 2.3 Features

### **NEW: 8 Additional Specialized Servers**

- **Erlang OTP**: GenServer, Supervisor, fault tolerance patterns
- **Elixir**: Functional programming, concurrency, OTP behaviors
- **Phoenix Framework**: Controllers, routing, contexts, plugs
- **Phoenix Channels**: WebSocket, PubSub, Presence tracking
- **Phoenix LiveView**: Real-time UI, hooks, HEEx templates, streams
- **Neo4j**: Cypher queries, graph modeling, path patterns
- **Qdrant**: Vector search, RAG patterns, similarity queries
- **HTMX + Axum**: Hypermedia-driven UI with Rust backend

### **Configuration Installer**

New `install_mcp_configs.py` script automatically installs all servers to:
- Claude Desktop
- Claude Code
- Gemini CLI
- Antigravity
- VSCode Insiders

## Overview

MCP Servers is a collection of 19 specialized servers based on the MCP (Model Context Protocol) that provide tools for prompt analysis, code optimization, and modern development workflows.

### Key Features

- 19 functional MCP servers covering frontend, backend, databases, and DevOps
- Interactive multi-select CLI with Vue CLI-style interface
- Automatic configuration installer for major AI tools
- 0-100 scoring systems for code analysis
- Knowledge bases with patterns and best practices

## Available Servers (19/19 Functional)

### Analysis Servers

| Server | Port | Description |
|--------|------|-------------|
| `mcp` | 3000 | MCP prompt analysis with 1-10 scoring |
| `prompt` | 3001 | Prompt engineering with CRISPE/RACE frameworks |
| `fastmcp` | 3003 | High-performance meta-server for MCP development |

### Frontend Servers

| Server | Port | Description |
|--------|------|-------------|
| `tailwind` | 3002 | Tailwind CSS v4.1 support and migration |
| `react` | 3004 | React 19 features (Server Components, Actions) |
| `shadcn` | 3006 | Advanced shadcn/ui component development |
| `htmx` | 3018 | HTMX with Axum (Rust) backend integration |

### Backend Servers

| Server | Port | Description |
|--------|------|-------------|
| `typescript` | 3005 | TypeScript analysis with Clean Architecture |
| `rust` | 3007 | Idiomatic Rust patterns (mre/idiomatic-rust) |
| `axum` | 3008 | Axum web framework with tokio-rs |
| `python` | 3010 | Python code analysis and modern paradigms |

### Elixir/Erlang Ecosystem

| Server | Port | Description |
|--------|------|-------------|
| `erlang` | 3011 | Erlang/OTP patterns, GenServer, Supervisor |
| `elixir` | 3012 | Elixir functional programming and concurrency |
| `phoenix` | 3013 | Phoenix web framework (controllers, contexts) |
| `phoenix_channels` | 3014 | Phoenix Channels (WebSocket, PubSub, Presence) |
| `phoenix_liveview` | 3015 | Phoenix LiveView real-time UI (hooks, HEEx) |

### Database Servers

| Server | Port | Description |
|--------|------|-------------|
| `neo4j` | 3016 | Neo4j Cypher queries and graph modeling |
| `qdrant` | 3017 | Qdrant vector search and RAG patterns |

### DevOps Servers

| Server | Port | Description |
|--------|------|-------------|
| `docker` | 3009 | Docker optimization with security best practices |

## Installation

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

# Modern interactive CLI (recommended)
uv run mcp_servers

# Show server status
uv run mcp_servers --status

# Traditional command-line
uv run python main.py --help
```

### Install to AI Tools

```bash
# Install all servers to Claude Desktop, Claude Code, Gemini CLI, etc.
uv run python install_mcp_configs.py --all

# Install to specific tool
uv run python install_mcp_configs.py --claude-desktop
uv run python install_mcp_configs.py --gemini-cli

# List configuration paths
uv run python install_mcp_configs.py --paths
```

## Quick Usage

### Interactive CLI

```bash
# Launch interactive multi-select menu
uv run mcp_servers

# Or use the shell script
./run_servers.sh
```

### Direct Commands

```bash
# Run specific server
uv run python main.py phoenix_liveview
uv run python main.py neo4j
uv run python main.py htmx

# Run multiple servers
uv run python main.py react tailwind shadcn

# Run all servers
uv run python main.py all --dev

# List all servers
uv run python main.py list
```

### Run Tests

```bash
# All tests
uv run pytest tests/ -v

# Specific server tests
uv run pytest tests/test_phoenix_liveview_server.py -v
uv run pytest tests/test_neo4j_server.py -v
```

## Server Details

### Erlang OTP Server (`erlang_server.py`)

Provides Erlang/OTP patterns for fault-tolerant systems.

**Tools:**
- `analyze_erlang_code` - Analyze Erlang code with scoring
- `generate_otp_project` - Generate OTP project structure
- `generate_genserver` - Generate GenServer module
- `get_otp_patterns` - Get patterns by category

### Elixir Server (`elixir_server.py`)

Functional programming and concurrency patterns for Elixir.

**Tools:**
- `analyze_elixir_code` - Analyze Elixir code
- `generate_elixir_project` - Generate Mix project
- `generate_genserver_elixir` - Generate GenServer module
- `get_elixir_patterns` - Get functional/OTP patterns

### Phoenix Framework Server (`phoenix_server.py`)

Web development with Phoenix controllers, routing, and contexts.

**Tools:**
- `analyze_phoenix_code` - Analyze Phoenix code
- `generate_phoenix_resource` - Generate CRUD resource
- `generate_context` - Generate Phoenix context
- `get_phoenix_patterns` - Get controller/router patterns

### Phoenix Channels Server (`phoenix_channels_server.py`)

Real-time communication with WebSocket and PubSub.

**Tools:**
- `analyze_channel_code` - Analyze channel code
- `generate_channel` - Generate channel module
- `generate_socket` - Generate socket module
- `generate_presence` - Generate Presence module
- `get_channel_patterns` - Get PubSub/Presence patterns

### Phoenix LiveView Server (`phoenix_liveview_server.py`)

Real-time UI with server-rendered HTML.

**Tools:**
- `analyze_liveview_code` - Analyze LiveView code
- `generate_liveview` - Generate LiveView module
- `generate_live_component` - Generate LiveComponent
- `generate_js_hook` - Generate JavaScript hook
- `generate_liveview_form` - Generate form with validation
- `get_liveview_patterns` - Get lifecycle/event patterns

### Neo4j Server (`neo4j_server.py`)

Graph database development with Cypher queries.

**Tools:**
- `analyze_cypher_query` - Analyze Cypher query
- `generate_cypher_query` - Generate Cypher query
- `optimize_cypher` - Optimize query performance
- `generate_graph_model` - Generate graph model
- `get_cypher_patterns` - Get MATCH/CREATE patterns

### Qdrant Server (`qdrant_server.py`)

Vector search and RAG (Retrieval-Augmented Generation) patterns.

**Tools:**
- `analyze_qdrant_query` - Analyze vector query
- `generate_collection_config` - Generate collection config
- `generate_qdrant_query` - Generate search query
- `optimize_vector_search` - Optimize search performance
- `get_qdrant_patterns` - Get search/filter patterns

### HTMX + Axum Server (`htmx_server.py`)

Hypermedia-driven development with Rust backend.

**Tools:**
- `analyze_htmx_code` - Analyze HTMX code
- `generate_htmx_component` - Generate HTMX component
- `generate_axum_handler` - Generate Axum handler
- `optimize_htmx_requests` - Optimize request patterns
- `get_htmx_patterns` - Get hx-* attribute patterns

## Project Structure

```text
mcp-servers/
├── main.py                       # Unified launcher (v2.3)
├── launcher_cli.py               # Interactive CLI
├── install_mcp_configs.py        # Configuration installer
├── run_servers.sh                # Shell menu interface
├── pyproject.toml                # Project configuration
│
├── servers/                      # MCP servers (19 total)
│   ├── mcp_server.py            # MCP prompt analyzer
│   ├── prompt_server.py         # Prompt engineering
│   ├── tailwind_server.py       # Tailwind CSS v4.1
│   ├── fastmcp_server.py        # FastMCP meta-server
│   ├── react_server.py          # React 19 unified
│   ├── typescript_server.py     # TypeScript analysis
│   ├── shadcn_server.py         # shadcn/ui components
│   ├── rust_server.py           # Rust idiomatic
│   ├── axum_server.py           # Axum web framework
│   ├── docker_optimizer_server.py # Docker optimization
│   ├── python_optimizer_server.py # Python optimizer
│   ├── erlang_server.py         # Erlang/OTP (NEW)
│   ├── elixir_server.py         # Elixir (NEW)
│   ├── phoenix_server.py        # Phoenix Framework (NEW)
│   ├── phoenix_channels_server.py # Phoenix Channels (NEW)
│   ├── phoenix_liveview_server.py # Phoenix LiveView (NEW)
│   ├── neo4j_server.py          # Neo4j Cypher (NEW)
│   ├── qdrant_server.py         # Qdrant Vector (NEW)
│   └── htmx_server.py           # HTMX + Axum (NEW)
│
├── tests/                        # Test files (20 test files)
│   ├── test_mcp_server.py
│   ├── test_erlang_server.py    # NEW
│   ├── test_elixir_server.py    # NEW
│   ├── test_phoenix_server.py   # NEW
│   ├── test_phoenix_channels_server.py # NEW
│   ├── test_phoenix_liveview_server.py # NEW
│   ├── test_neo4j_server.py     # NEW
│   ├── test_qdrant_server.py    # NEW
│   ├── test_htmx_server.py      # NEW
│   └── ...
│
└── docs/                         # Documentation
```

## Configuration Paths

The configuration installer supports:

| Tool | Configuration Path |
|------|-------------------|
| Claude Desktop (macOS) | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Claude Code | `~/.claude.json` |
| Gemini CLI | `~/.gemini/settings.json` |
| Antigravity | `~/.gemini/antigravity/mcp_config.json` |
| VSCode Insiders | `~/Library/Application Support/Code - Insiders/User/mcp.json` |

## Scoring System

All analysis servers use a 0-100 scoring system:

| Score | Grade | Description |
|-------|-------|-------------|
| 90-100 | Excellent | Follows all best practices |
| 75-89 | Good | Minor improvements possible |
| 50-74 | Needs Improvement | Significant patterns missing |
| 0-49 | Poor | Major refactoring needed |

## Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/new-server`)
3. Add tests for new features
4. Commit changes (`git commit -m 'Add new server'`)
5. Push to branch (`git push origin feature/new-server`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

- [FastMCP](https://github.com/fastmcp/fastmcp) - MCP server framework
- [Pydantic](https://docs.pydantic.dev/) - Data validation
- [uv](https://github.com/astral-sh/uv) - Python package manager
- [mre/idiomatic-rust](https://github.com/mre/idiomatic-rust) - Rust patterns
- [Phoenix Framework](https://www.phoenixframework.org/) - Elixir web framework

---

**MCP Servers v2.3** | **19 Servers** | **Python 3.12+** | **Status: Production**

_Developed with love by Charleno Pires_
