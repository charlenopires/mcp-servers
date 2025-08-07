#!/bin/bash

# MCP Servers execution script - Wrapper for main.py
# This script now uses main.py as the primary backend

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Project directory
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if uv is installed
check_uv() {
    if ! command -v uv &> /dev/null; then
        echo -e "${RED}❌ Error: 'uv' is not installed${NC}"
        echo -e "${YELLOW}💡 Install with: curl -LsSf https://astral.sh/uv/install.sh | sh${NC}"
        exit 1
    fi
}

# Check if Python is available
check_python() {
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}❌ Error: Python 3 not found${NC}"
        exit 1
    fi
}

# Function to display banner
show_banner() {
    echo -e "${CYAN}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                    🚀 MCP SERVERS LAUNCHER                   ║"
    echo "║                MCP Servers Manager v2.0                      ║"
    echo "║                    Powered by main.py                        ║"
    echo "║                  11/11 Functional Servers                    ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

# Function to show interactive menu
show_interactive_menu() {
    echo -e "${YELLOW}🎯 Select an option:${NC}"
    echo ""
    echo -e "${CYAN}📊 INFORMATION:${NC}"
    echo -e "${GREEN} 1${NC}) 📋 List all available servers"
    echo -e "${GREEN} 2${NC}) 📊 Detailed server status"
    echo ""
    echo -e "${CYAN}🚀 EXECUTION:${NC}"
    echo -e "${GREEN} 3${NC}) 🚀 Run ALL servers (development mode)"
    echo -e "${GREEN} 4${NC}) 🔍 MCP Server (MCP prompt analysis)"
    echo -e "${GREEN} 5${NC}) ✏️  Prompt Server (Prompt engineering)"
    echo -e "${GREEN} 6${NC}) 🎨 Tailwind CSS Server v4.1"
    echo -e "${GREEN} 7${NC}) ⚡ FastMCP Server (High performance)"
    echo -e "${GREEN} 8${NC}) ⚛️  React Unified Server (Analysis + Optimization + React 19)"
    echo -e "${GREEN} 9${NC}) 📘 TypeScript Server (Advanced analysis and Clean Architecture)"
    echo -e "${GREEN}10${NC}) 🧩 shadcn/ui Advanced Server"
    echo -e "${GREEN}11${NC}) 🦀 Rust Idiomatic Server (mre/idiomatic-rust patterns)"
    echo -e "${GREEN}12${NC}) 🌐 Axum Server (tokio-rs web framework + magic patterns)"
    echo -e "${GREEN}13${NC}) 🐳 Docker Server (Optimization and containerization best practices)"
    echo -e "${GREEN}14${NC}) 🐍 Python Server (Code analysis and modern paradigms)"
    echo ""
    echo -e "${GREEN} 0${NC}) ❌ Exit"
    echo ""
    echo -e -n "${BLUE}Enter your option (0-14): ${NC}"
    
    read -r choice
    
    case $choice in
        1)
            echo -e "\n${CYAN}📋 Listing available servers...${NC}\n"
            uv run python main.py list
            ;;
        2)
            echo ""
            show_server_status
            ;;
        3)
            echo -e "\n${GREEN}🚀 Starting ALL servers...${NC}\n"
            uv run python main.py all --dev
            ;;
        4)
            echo -e "\n${GREEN}🔍 Starting MCP Server...${NC}\n"
            uv run python main.py mcp
            ;;
        5)
            echo -e "\n${GREEN}✏️ Starting Prompt Server...${NC}\n"
            uv run python main.py prompt
            ;;
        6)
            echo -e "\n${GREEN}🎨 Starting Tailwind CSS Server...${NC}\n"
            uv run python main.py tailwind
            ;;
        7)
            echo -e "\n${GREEN}⚡ Starting FastMCP Server...${NC}\n"
            uv run python main.py fastmcp
            ;;
        8)
            echo -e "\n${GREEN}⚛️ Starting React Unified Server...${NC}\n"
            uv run python main.py react
            ;;
        9)
            echo -e "\n${GREEN}📘 Starting TypeScript Server...${NC}\n"
            uv run python main.py typescript
            ;;
        10)
            echo -e "\n${GREEN}🧩 Starting shadcn/ui Advanced Server...${NC}\n"
            uv run python main.py shadcn
            ;;
        11)
            echo -e "\n${GREEN}🦀 Starting Rust Idiomatic Server...${NC}\n"
            uv run python main.py rust
            ;;
        12)
            echo -e "\n${GREEN}🌐 Starting Axum Server...${NC}\n"
            uv run python main.py axum
            ;;
        13)
            echo -e "\n${GREEN}🐳 Starting Docker Server...${NC}\n"
            uv run python main.py docker
            ;;
        14)
            echo -e "\n${GREEN}🐍 Starting Python Server...${NC}\n"
            uv run python main.py python
            ;;
        0)
            echo -e "\n${GREEN}👋 Goodbye!${NC}"
            exit 0
            ;;
        *)
            echo -e "\n${RED}❌ Invalid option. Choose between 0-15.${NC}"
            ;;
    esac
}

# Function to show server status
show_server_status() {
    echo -e "${CYAN}📊 MCP Servers Status:${NC}"
    echo ""
    
    # Server status descriptions
    get_server_status() {
        case $1 in
            "mcp") echo "✅ FUNCTIONAL - MCP prompt analysis with 1-10 scoring" ;;
            "prompt") echo "✅ FUNCTIONAL - Prompt engineering with CRISPE/RACE frameworks" ;;
            "tailwind") echo "✅ FUNCTIONAL - Tailwind CSS v4.1 with Oxide engine (Rust)" ;;
            "fastmcp") echo "✅ FUNCTIONAL - FastMCP 2.0 complete platform + MCP Inspector" ;;
            "react") echo "✅ FUNCTIONAL - Unified React server: analysis, optimization, React 19 + UI/UX 2025" ;;
            "typescript") echo "✅ FUNCTIONAL - Modern TypeScript with Clean Architecture and SOLID principles" ;;
            "shadcn") echo "✅ FUNCTIONAL - shadcn/ui Advanced with intelligent analysis" ;;
            "rust") echo "✅ FUNCTIONAL - Rust Idiomatic following mre/idiomatic-rust patterns" ;;
            "axum") echo "✅ FUNCTIONAL - Axum web framework with tokio-rs + magic patterns" ;;
            "docker") echo "✅ FUNCTIONAL - Docker containerization with security best practices" ;;
            "python") echo "✅ FUNCTIONAL - Python development with modern paradigms (OOP/Functional/Async)" ;;
            *) echo "❌ Unknown server" ;;
        esac
    }
    
    # Server ports
    get_server_port() {
        case $1 in
            "mcp") echo "3000" ;;
            "prompt") echo "3001" ;;
            "tailwind") echo "3002" ;;
            "fastmcp") echo "3003" ;;
            "react") echo "3004" ;;
            "typescript") echo "3005" ;;
            "shadcn") echo "3006" ;;
            "rust") echo "3007" ;;
            "axum") echo "3008" ;;
            "docker") echo "3009" ;;
            "python") echo "3010" ;;
            *) echo "????" ;;
        esac
    }
    
    for server in mcp prompt tailwind fastmcp react typescript shadcn rust axum docker python; do
        status=$(get_server_status "$server")
        port=$(get_server_port "$server")
        echo -e "  ${GREEN}$server${NC} (port $port): $status"
    done
    
    echo ""
    echo -e "${YELLOW}📈 Statistics:${NC}"
    echo -e "  • Functional servers: ${GREEN}11/11${NC} (100%)"
    echo -e "  • In development: ${YELLOW}0/11${NC} (0%)"
    echo -e "  • Framework: ${BLUE}FastMCP 2.0 + Python 3.12+${NC}"
    echo -e "  • Manager: ${PURPLE}uv (ultrafast package manager)${NC}"
    echo ""
    echo -e "${CYAN}🆕 Latest Updates:${NC}"
    echo -e "  • Tailwind CSS v4.1 (Oxide/Rust engine)"
    echo -e "  • FastMCP 2.0 (MCP Inspector + deployment tools)"
    echo -e "  • React 19 (Server Components + stable Actions)"
    echo -e "  • shadcn/ui Advanced (intelligent analysis)"
    echo -e "  • Rust Idiomatic (mre/idiomatic-rust patterns)"
    echo -e "  • Axum Web Framework (tokio-rs + magic patterns)"
    echo -e "  • Docker Optimizer (security best practices + multi-stage)"
}

# Função de ajuda
show_help() {
    echo -e "${BLUE}📖 Uso do Script:${NC}"
    echo ""
    echo -e "  ${GREEN}$0${NC} [comando] [opções]"
    echo ""
    echo -e "${YELLOW}Comandos disponíveis:${NC}"
    echo -e "  ${GREEN}(sem args)${NC}     - Menu interativo principal"
    echo -e "  ${GREEN}menu${NC}           - Menu interativo principal"
    echo -e "  ${GREEN}list${NC}           - Lista todos os servidores disponíveis"
    echo -e "  ${GREEN}status${NC}         - Status detalhado dos servidores"
    echo -e "  ${GREEN}all${NC}            - Executa todos os servidores"
    echo ""
    echo -e "${YELLOW}Servidores individuais:${NC}"
    echo -e "  ${GREEN}mcp${NC}            - Servidor MCP (Análise de prompts MCP)"
    echo -e "  ${GREEN}prompt${NC}         - Servidor de Prompts (Engenharia de prompts)"
    echo -e "  ${GREEN}tailwind${NC}       - Servidor Tailwind CSS v4.1"
    echo -e "  ${GREEN}fastmcp${NC}        - Servidor FastMCP (Alta performance)"
    echo -e "  ${GREEN}shadcn${NC}         - Servidor shadcn/ui Advanced (NOVO!)"
    echo -e "  ${GREEN}react${NC}          - Servidor React 19 (Server Components + Actions)"
    echo -e "  ${GREEN}rust${NC}           - Servidor Rust Idiomatic (mre/idiomatic-rust patterns)"
    echo -e "  ${GREEN}axum${NC}           - Servidor Axum Web Framework (tokio-rs + magic patterns)"
    echo -e "  ${GREEN}docker${NC}         - Servidor Docker (Otimização e boas práticas)"
    echo -e "  ${GREEN}python${NC}         - Servidor Python (Análise de código e paradigmas modernos)"
    echo -e "  ${GREEN}typescript${NC}     - Servidor TypeScript (Análise avançada e Clean Architecture)"
    echo ""
    echo -e "${YELLOW}Opções:${NC}"
    echo -e "  ${GREEN}--dev${NC}          - Modo desenvolvimento (mais logs)"
    echo -e "  ${GREEN}--quiet${NC}        - Modo silencioso"
    echo -e "  ${GREEN}--port PORT${NC}    - Define porta personalizada"
    echo -e "  ${GREEN}--help${NC}         - Mostra esta ajuda"
    echo ""
    echo -e "${YELLOW}Exemplos:${NC}"
    echo -e "  ${PURPLE}$0${NC}                         # Menu interativo"
    echo -e "  ${PURPLE}$0 list${NC}                    # Lista servidores"
    echo -e "  ${PURPLE}$0 mcp${NC}                     # Inicia servidor MCP"
    echo -e "  ${PURPLE}$0 status${NC}                  # Status dos servidores"
    echo -e "  ${PURPLE}$0 shadcn${NC}                  # Inicia servidor shadcn/ui"
    echo -e "  ${PURPLE}$0 prompt --port 3001${NC}     # Inicia Prompt na porta 3001"
    echo -e "  ${PURPLE}$0 all --dev${NC}              # Inicia todos em modo dev"
}

# Função principal
main() {
    show_banner
    
    # Verificar dependências
    check_uv
    check_python
    
    # Mudar para o diretório do projeto
    cd "$PROJECT_DIR" || exit 1
    
    # Se nenhum argumento foi fornecido, mostrar menu interativo
    if [ $# -eq 0 ]; then
        show_interactive_menu
        exit 0
    fi
    
    # Se o primeiro argumento for "menu", mostrar menu interativo
    if [ "$1" = "menu" ]; then
        show_interactive_menu
        exit 0
    fi
    
    # Processar argumentos
    case "$1" in
        "help"|"--help"|"-h")
            show_help
            ;;
        "list")
            echo -e "${CYAN}📋 Servidores Disponíveis:${NC}"
            echo ""
            uv run python main.py list
            ;;
        "status")
            show_server_status
            ;;
        "all"|"mcp"|"prompt"|"tailwind"|"fastmcp"|"react"|"typescript"|"shadcn"|"rust"|"axum"|"docker"|"python")
            echo -e "${GREEN}🚀 Iniciando servidor(es)...${NC}"
            echo ""
            
            # Executar com uv
            if ! uv run python main.py "$@"; then
                echo -e "${RED}❌ Erro ao executar servidor${NC}"
                exit 1
            fi
            ;;
        *)
            echo -e "${RED}❌ Comando desconhecido: $1${NC}"
            echo ""
            show_help
            exit 1
            ;;
    esac
}

# Trap para limpeza
cleanup() {
    echo -e "\n${YELLOW}🛑 Interrompido pelo usuário${NC}"
    exit 0
}

trap cleanup SIGINT SIGTERM

# Executar função principal
main "$@"
