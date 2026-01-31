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
        echo -e "${RED} Error: 'uv' is not installed${NC}"
        echo -e "${YELLOW} Install with: curl -LsSf https://astral.sh/uv/install.sh | sh${NC}"
        exit 1
    fi
}

# Check if Python is available
check_python() {
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED} Error: Python 3 not found${NC}"
        exit 1
    fi
}

# Function to display banner
show_banner() {
    echo -e "${CYAN}"
    echo "======================================================================"
    echo "                     MCP SERVERS LAUNCHER                            "
    echo "                 MCP Servers Manager v2.3                            "
    echo "                    Powered by main.py                               "
    echo "                  19/19 Functional Servers                           "
    echo "======================================================================"
    echo -e "${NC}"
}

# Function to show interactive menu
show_interactive_menu() {
    echo -e "${YELLOW} Select an option:${NC}"
    echo ""
    echo -e "${CYAN} INFORMATION:${NC}"
    echo -e "${GREEN} 1${NC}) List all available servers"
    echo -e "${GREEN} 2${NC}) Detailed server status"
    echo ""
    echo -e "${CYAN} EXECUTION:${NC}"
    echo -e "${GREEN} 3${NC}) Run ALL servers (development mode)"
    echo ""
    echo -e "${CYAN} ANALYSIS SERVERS:${NC}"
    echo -e "${GREEN} 4${NC}) MCP Server (MCP prompt analysis)"
    echo -e "${GREEN} 5${NC}) Prompt Server (Prompt engineering)"
    echo -e "${GREEN} 6${NC}) FastMCP Server (High performance)"
    echo ""
    echo -e "${CYAN} FRONTEND SERVERS:${NC}"
    echo -e "${GREEN} 7${NC}) Tailwind CSS Server v4.1"
    echo -e "${GREEN} 8${NC}) React Unified Server (Analysis + Optimization + React 19)"
    echo -e "${GREEN} 9${NC}) shadcn/ui Advanced Server"
    echo -e "${GREEN}10${NC}) HTMX + Axum Server"
    echo ""
    echo -e "${CYAN} BACKEND SERVERS:${NC}"
    echo -e "${GREEN}11${NC}) TypeScript Server (Advanced analysis and Clean Architecture)"
    echo -e "${GREEN}12${NC}) Rust Idiomatic Server (mre/idiomatic-rust patterns)"
    echo -e "${GREEN}13${NC}) Axum Server (tokio-rs web framework + magic patterns)"
    echo -e "${GREEN}14${NC}) Python Server (Code analysis and modern paradigms)"
    echo ""
    echo -e "${CYAN} ELIXIR/ERLANG SERVERS:${NC}"
    echo -e "${GREEN}15${NC}) Erlang OTP Server (GenServer, Supervisor, fault tolerance)"
    echo -e "${GREEN}16${NC}) Elixir Server (Functional programming, concurrency)"
    echo -e "${GREEN}17${NC}) Phoenix Framework Server (Controllers, routing, contexts)"
    echo -e "${GREEN}18${NC}) Phoenix Channels Server (WebSocket, PubSub, Presence)"
    echo -e "${GREEN}19${NC}) Phoenix LiveView Server (Real-time UI, hooks, HEEx)"
    echo ""
    echo -e "${CYAN} DATABASE SERVERS:${NC}"
    echo -e "${GREEN}20${NC}) Neo4j Cypher Server (Graph database, Cypher queries)"
    echo -e "${GREEN}21${NC}) Qdrant Vector Server (Vector search, RAG patterns)"
    echo ""
    echo -e "${CYAN} DEVOPS:${NC}"
    echo -e "${GREEN}22${NC}) Docker Server (Optimization and containerization)"
    echo ""
    echo -e "${CYAN} INSTALLATION:${NC}"
    echo -e "${GREEN}23${NC}) Install configs to all AI tools"
    echo ""
    echo -e "${GREEN} 0${NC}) Exit"
    echo ""
    echo -e -n "${BLUE}Enter your option (0-23): ${NC}"

    read -r choice

    case $choice in
        1)
            echo -e "\n${CYAN} Listing available servers...${NC}\n"
            uv run python main.py list
            ;;
        2)
            echo ""
            show_server_status
            ;;
        3)
            echo -e "\n${GREEN} Starting ALL servers...${NC}\n"
            uv run python main.py all --dev
            ;;
        4)
            echo -e "\n${GREEN} Starting MCP Server...${NC}\n"
            uv run python main.py mcp
            ;;
        5)
            echo -e "\n${GREEN} Starting Prompt Server...${NC}\n"
            uv run python main.py prompt
            ;;
        6)
            echo -e "\n${GREEN} Starting FastMCP Server...${NC}\n"
            uv run python main.py fastmcp
            ;;
        7)
            echo -e "\n${GREEN} Starting Tailwind CSS Server...${NC}\n"
            uv run python main.py tailwind
            ;;
        8)
            echo -e "\n${GREEN} Starting React Unified Server...${NC}\n"
            uv run python main.py react
            ;;
        9)
            echo -e "\n${GREEN} Starting shadcn/ui Advanced Server...${NC}\n"
            uv run python main.py shadcn
            ;;
        10)
            echo -e "\n${GREEN} Starting HTMX + Axum Server...${NC}\n"
            uv run python main.py htmx
            ;;
        11)
            echo -e "\n${GREEN} Starting TypeScript Server...${NC}\n"
            uv run python main.py typescript
            ;;
        12)
            echo -e "\n${GREEN} Starting Rust Idiomatic Server...${NC}\n"
            uv run python main.py rust
            ;;
        13)
            echo -e "\n${GREEN} Starting Axum Server...${NC}\n"
            uv run python main.py axum
            ;;
        14)
            echo -e "\n${GREEN} Starting Python Server...${NC}\n"
            uv run python main.py python
            ;;
        15)
            echo -e "\n${GREEN} Starting Erlang OTP Server...${NC}\n"
            uv run python main.py erlang
            ;;
        16)
            echo -e "\n${GREEN} Starting Elixir Server...${NC}\n"
            uv run python main.py elixir
            ;;
        17)
            echo -e "\n${GREEN} Starting Phoenix Framework Server...${NC}\n"
            uv run python main.py phoenix
            ;;
        18)
            echo -e "\n${GREEN} Starting Phoenix Channels Server...${NC}\n"
            uv run python main.py phoenix_channels
            ;;
        19)
            echo -e "\n${GREEN} Starting Phoenix LiveView Server...${NC}\n"
            uv run python main.py phoenix_liveview
            ;;
        20)
            echo -e "\n${GREEN} Starting Neo4j Cypher Server...${NC}\n"
            uv run python main.py neo4j
            ;;
        21)
            echo -e "\n${GREEN} Starting Qdrant Vector Server...${NC}\n"
            uv run python main.py qdrant
            ;;
        22)
            echo -e "\n${GREEN} Starting Docker Server...${NC}\n"
            uv run python main.py docker
            ;;
        23)
            echo -e "\n${GREEN} Installing MCP configurations...${NC}\n"
            uv run python install_mcp_configs.py
            ;;
        0)
            echo -e "\n${GREEN} Goodbye!${NC}"
            exit 0
            ;;
        *)
            echo -e "\n${RED} Invalid option. Choose between 0-23.${NC}"
            ;;
    esac
}

# Function to show server status
show_server_status() {
    echo -e "${CYAN} MCP Servers Status:${NC}"
    echo ""

    echo -e "${YELLOW} Analysis Servers:${NC}"
    echo -e "  ${GREEN}mcp${NC} (port 3000): MCP prompt analysis with 1-10 scoring"
    echo -e "  ${GREEN}prompt${NC} (port 3001): Prompt engineering with CRISPE/RACE frameworks"
    echo -e "  ${GREEN}fastmcp${NC} (port 3003): FastMCP 2.0 complete platform"
    echo ""

    echo -e "${YELLOW} Frontend Servers:${NC}"
    echo -e "  ${GREEN}tailwind${NC} (port 3002): Tailwind CSS v4.1 with Oxide engine"
    echo -e "  ${GREEN}react${NC} (port 3004): React 19 (Server Components + Actions)"
    echo -e "  ${GREEN}shadcn${NC} (port 3006): shadcn/ui Advanced"
    echo -e "  ${GREEN}htmx${NC} (port 3018): HTMX + Axum integration"
    echo ""

    echo -e "${YELLOW} Backend Servers:${NC}"
    echo -e "  ${GREEN}typescript${NC} (port 3005): TypeScript with Clean Architecture"
    echo -e "  ${GREEN}rust${NC} (port 3007): Rust Idiomatic (mre/idiomatic-rust)"
    echo -e "  ${GREEN}axum${NC} (port 3008): Axum web framework (tokio-rs)"
    echo -e "  ${GREEN}python${NC} (port 3010): Python development (OOP/Functional/Async)"
    echo ""

    echo -e "${YELLOW} Elixir/Erlang Servers:${NC}"
    echo -e "  ${GREEN}erlang${NC} (port 3011): Erlang/OTP patterns"
    echo -e "  ${GREEN}elixir${NC} (port 3012): Elixir functional programming"
    echo -e "  ${GREEN}phoenix${NC} (port 3013): Phoenix web framework"
    echo -e "  ${GREEN}phoenix_channels${NC} (port 3014): Phoenix Channels (WebSocket/PubSub)"
    echo -e "  ${GREEN}phoenix_liveview${NC} (port 3015): Phoenix LiveView (Real-time UI)"
    echo ""

    echo -e "${YELLOW} Database Servers:${NC}"
    echo -e "  ${GREEN}neo4j${NC} (port 3016): Neo4j Cypher queries"
    echo -e "  ${GREEN}qdrant${NC} (port 3017): Qdrant vector search"
    echo ""

    echo -e "${YELLOW} DevOps Servers:${NC}"
    echo -e "  ${GREEN}docker${NC} (port 3009): Docker optimization"
    echo ""

    echo -e "${YELLOW} Statistics:${NC}"
    echo -e "  - Functional servers: ${GREEN}19/19${NC} (100%)"
    echo -e "  - Framework: ${BLUE}FastMCP 3.0 + Python 3.12+${NC}"
    echo -e "  - Manager: ${PURPLE}uv (ultrafast package manager)${NC}"
    echo ""
    echo -e "${CYAN} New in v2.3:${NC}"
    echo -e "  - Erlang OTP Server (GenServer, Supervisor, fault tolerance)"
    echo -e "  - Elixir Server (functional programming, concurrency)"
    echo -e "  - Phoenix Framework Server (controllers, contexts)"
    echo -e "  - Phoenix Channels Server (WebSocket, PubSub, Presence)"
    echo -e "  - Phoenix LiveView Server (real-time UI, hooks)"
    echo -e "  - Neo4j Cypher Server (graph database)"
    echo -e "  - Qdrant Vector Server (vector search, RAG)"
    echo -e "  - HTMX + Axum Server (hypermedia + Rust)"
}

# Help function
show_help() {
    echo -e "${BLUE} Script Usage:${NC}"
    echo ""
    echo -e "  ${GREEN}$0${NC} [command] [options]"
    echo ""
    echo -e "${YELLOW}Available Commands:${NC}"
    echo -e "  ${GREEN}(no args)${NC}        - Interactive main menu"
    echo -e "  ${GREEN}menu${NC}             - Interactive main menu"
    echo -e "  ${GREEN}list${NC}             - List all available servers"
    echo -e "  ${GREEN}status${NC}           - Detailed server status"
    echo -e "  ${GREEN}all${NC}              - Run all servers"
    echo -e "  ${GREEN}install${NC}          - Install configs to AI tools"
    echo ""
    echo -e "${YELLOW}Individual Servers:${NC}"
    echo -e "  ${GREEN}mcp${NC}              - MCP Server (MCP prompt analysis)"
    echo -e "  ${GREEN}prompt${NC}           - Prompt Server (Prompt engineering)"
    echo -e "  ${GREEN}tailwind${NC}         - Tailwind CSS Server v4.1"
    echo -e "  ${GREEN}fastmcp${NC}          - FastMCP Server (High performance)"
    echo -e "  ${GREEN}shadcn${NC}           - shadcn/ui Advanced Server"
    echo -e "  ${GREEN}react${NC}            - React 19 Server"
    echo -e "  ${GREEN}rust${NC}             - Rust Idiomatic Server"
    echo -e "  ${GREEN}axum${NC}             - Axum Web Framework Server"
    echo -e "  ${GREEN}docker${NC}           - Docker Server"
    echo -e "  ${GREEN}python${NC}           - Python Server"
    echo -e "  ${GREEN}typescript${NC}       - TypeScript Server"
    echo -e "  ${GREEN}erlang${NC}           - Erlang OTP Server"
    echo -e "  ${GREEN}elixir${NC}           - Elixir Server"
    echo -e "  ${GREEN}phoenix${NC}          - Phoenix Framework Server"
    echo -e "  ${GREEN}phoenix_channels${NC} - Phoenix Channels Server"
    echo -e "  ${GREEN}phoenix_liveview${NC} - Phoenix LiveView Server"
    echo -e "  ${GREEN}neo4j${NC}            - Neo4j Cypher Server"
    echo -e "  ${GREEN}qdrant${NC}           - Qdrant Vector Server"
    echo -e "  ${GREEN}htmx${NC}             - HTMX + Axum Server"
    echo ""
    echo -e "${YELLOW}Options:${NC}"
    echo -e "  ${GREEN}--dev${NC}            - Development mode (more logs)"
    echo -e "  ${GREEN}--quiet${NC}          - Quiet mode"
    echo -e "  ${GREEN}--port PORT${NC}      - Set custom port"
    echo -e "  ${GREEN}--help${NC}           - Show this help"
    echo ""
    echo -e "${YELLOW}Examples:${NC}"
    echo -e "  ${PURPLE}$0${NC}                         # Interactive menu"
    echo -e "  ${PURPLE}$0 list${NC}                    # List servers"
    echo -e "  ${PURPLE}$0 mcp${NC}                     # Start MCP server"
    echo -e "  ${PURPLE}$0 status${NC}                  # Server status"
    echo -e "  ${PURPLE}$0 phoenix_liveview${NC}        # Start Phoenix LiveView"
    echo -e "  ${PURPLE}$0 install${NC}                 # Install configs"
    echo -e "  ${PURPLE}$0 all --dev${NC}              # Start all in dev mode"
}

# Main function
main() {
    show_banner

    # Check dependencies
    check_uv
    check_python

    # Change to project directory
    cd "$PROJECT_DIR" || exit 1

    # If no arguments provided, show interactive menu
    if [ $# -eq 0 ]; then
        show_interactive_menu
        exit 0
    fi

    # If first argument is "menu", show interactive menu
    if [ "$1" = "menu" ]; then
        show_interactive_menu
        exit 0
    fi

    # Process arguments
    case "$1" in
        "help"|"--help"|"-h")
            show_help
            ;;
        "list")
            echo -e "${CYAN} Available Servers:${NC}"
            echo ""
            uv run python main.py list
            ;;
        "status")
            show_server_status
            ;;
        "install")
            echo -e "${GREEN} Installing MCP configurations...${NC}"
            echo ""
            uv run python install_mcp_configs.py "${@:2}"
            ;;
        "all"|"mcp"|"prompt"|"tailwind"|"fastmcp"|"react"|"typescript"|"shadcn"|"rust"|"axum"|"docker"|"python"|"erlang"|"elixir"|"phoenix"|"phoenix_channels"|"phoenix_liveview"|"neo4j"|"qdrant"|"htmx")
            echo -e "${GREEN} Starting server(s)...${NC}"
            echo ""

            # Execute with uv
            if ! uv run python main.py "$@"; then
                echo -e "${RED} Error executing server${NC}"
                exit 1
            fi
            ;;
        *)
            echo -e "${RED} Unknown command: $1${NC}"
            echo ""
            show_help
            exit 1
            ;;
    esac
}

# Trap for cleanup
cleanup() {
    echo -e "\n${YELLOW} Interrupted by user${NC}"
    exit 0
}

trap cleanup SIGINT SIGTERM

# Execute main function
main "$@"
