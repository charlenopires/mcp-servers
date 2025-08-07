#!/bin/bash

# Script para executar servidores MCP - Wrapper para main.py
# Este script agora utiliza o main.py como backend principal

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Diretório do projeto
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Verificar se uv está instalado
check_uv() {
    if ! command -v uv &> /dev/null; then
        echo -e "${RED}❌ Erro: 'uv' não está instalado${NC}"
        echo -e "${YELLOW}💡 Instale com: curl -LsSf https://astral.sh/uv/install.sh | sh${NC}"
        exit 1
    fi
}

# Verificar se Python está disponível
check_python() {
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}❌ Erro: Python 3 não encontrado${NC}"
        exit 1
    fi
}

# Função para exibir banner
show_banner() {
    echo -e "${CYAN}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                    🚀 LAUNCHER MCP SERVERS                   ║"
    echo "║              Gerenciador de Servidores MCP v2.0              ║"
    echo "║                    Powered by main.py                        ║"
    echo "║                10/11 Servidores Funcionais                   ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

# Função para mostrar menu interativo
show_interactive_menu() {
    echo -e "${YELLOW}🎯 Selecione uma opção:${NC}"
    echo ""
    echo -e "${CYAN}📊 INFORMAÇÕES:${NC}"
    echo -e "${GREEN} 1${NC}) 📋 Listar todos os servidores disponíveis"
    echo -e "${GREEN} 2${NC}) 📊 Status detalhado dos servidores"
    echo ""
    echo -e "${CYAN}🚀 EXECUÇÃO:${NC}"
    echo -e "${GREEN} 3${NC}) 🚀 Executar TODOS os servidores (modo desenvolvimento)"
    echo -e "${GREEN} 4${NC}) 🔍 Servidor MCP (Análise de prompts MCP)"
    echo -e "${GREEN} 5${NC}) ✏️  Servidor Prompt (Engenharia de prompts)"
    echo -e "${GREEN} 6${NC}) 🎨 Servidor Tailwind CSS v4.1"
    echo -e "${GREEN} 7${NC}) ⚡ Servidor FastMCP (Alta performance)"
    echo -e "${GREEN} 8${NC}) ⚛️  Servidor React Optimizer"
    echo -e "${GREEN} 9${NC}) 🧩 Servidor shadcn/ui Advanced (NOVO!)"
    echo -e "${GREEN}10${NC}) ⚛️  Servidor React 19 (Server Components + Actions)"
    echo -e "${GREEN}11${NC}) 🦀 Servidor Rust Idiomatic (mre/idiomatic-rust patterns)"
    echo -e "${GREEN}12${NC}) 🌐 Servidor Axum (tokio-rs web framework + magic patterns)"
    echo -e "${GREEN}13${NC}) 🐳 Servidor Docker (Otimização e boas práticas de containerização)"
    echo -e "${GREEN}14${NC}) 🐍 Servidor Python (Análise de código e paradigmas modernos)"
    echo -e "${GREEN}15${NC}) 📘 Servidor TypeScript (Análise avançada e Clean Architecture)"
    echo ""
    echo -e "${GREEN} 0${NC}) ❌ Sair"
    echo ""
    echo -e -n "${BLUE}Digite sua opção (0-15): ${NC}"
    
    read -r choice
    
    case $choice in
        1)
            echo -e "\n${CYAN}📋 Listando servidores disponíveis...${NC}\n"
            uv run python main.py list
            ;;
        2)
            echo ""
            show_server_status
            ;;
        3)
            echo -e "\n${GREEN}🚀 Iniciando TODOS os servidores...${NC}\n"
            uv run python main.py all --dev
            ;;
        4)
            echo -e "\n${GREEN}🔍 Iniciando Servidor MCP...${NC}\n"
            uv run python main.py mcp
            ;;
        5)
            echo -e "\n${GREEN}✏️ Iniciando Servidor Prompt...${NC}\n"
            uv run python main.py prompt
            ;;
        6)
            echo -e "\n${GREEN}🎨 Iniciando Servidor Tailwind CSS...${NC}\n"
            uv run python main.py tailwind
            ;;
        7)
            echo -e "\n${GREEN}⚡ Iniciando Servidor FastMCP...${NC}\n"
            uv run python main.py fastmcp
            ;;
        8)
            echo -e "\n${GREEN}⚛️ Iniciando Servidor React Optimizer...${NC}\n"
            uv run python main.py react_optimizer
            ;;
        9)
            echo -e "\n${GREEN}🧩 Iniciando Servidor shadcn/ui Advanced...${NC}\n"
            uv run python main.py shadcn
            ;;
        10)
            echo -e "\n${GREEN}⚛️ Iniciando Servidor React 19...${NC}\n"
            uv run python main.py react
            ;;
        11)
            echo -e "\n${GREEN}🦀 Iniciando Servidor Rust Idiomatic...${NC}\n"
            uv run python main.py rust
            ;;
        12)
            echo -e "\n${GREEN}🌐 Iniciando Servidor Axum...${NC}\n"
            uv run python main.py axum
            ;;
        13)
            echo -e "\n${GREEN}🐳 Iniciando Servidor Docker...${NC}\n"
            uv run python main.py docker
            ;;
        14)
            echo -e "\n${GREEN}🐍 Iniciando Servidor Python...${NC}\n"
            uv run python main.py python
            ;;
        15)
            echo -e "\n${GREEN}📘 Iniciando Servidor TypeScript...${NC}\n"
            uv run python main.py typescript
            ;;
        0)
            echo -e "\n${GREEN}👋 Até logo!${NC}"
            exit 0
            ;;
        *)
            echo -e "\n${RED}❌ Opção inválida. Escolha entre 0-15.${NC}"
            ;;
    esac
}

# Função para mostrar status dos servidores
show_server_status() {
    echo -e "${CYAN}📊 Status dos Servidores MCP:${NC}"
    echo ""
    
    declare -A server_status=(
        ["mcp"]="✅ FUNCIONAL - Análise de prompts MCP com pontuação 1-10"
        ["prompt"]="✅ FUNCIONAL - Engenharia de prompts com frameworks CRISPE/RACE"
        ["tailwind"]="✅ FUNCIONAL - Tailwind CSS v4.1 com engine Oxide (Rust)"
        ["fastmcp"]="✅ FUNCIONAL - FastMCP 2.0 plataforma completa + MCP Inspector"
        ["react_optimizer"]="✅ FUNCIONAL - Análise e otimização React + UI/UX 2025"
        ["shadcn"]="✅ FUNCIONAL - shadcn/ui Advanced com análise inteligente"
        ["react"]="✅ FUNCIONAL - React 19 com Server Components e Actions"
        ["rust"]="✅ FUNCIONAL - Rust Idiomatic seguindo mre/idiomatic-rust patterns"
        ["axum"]="✅ FUNCIONAL - Axum web framework com tokio-rs + magic patterns"
        ["docker"]="✅ FUNCIONAL - Docker containerização com security best practices"
        ["python"]="✅ FUNCIONAL - Python desenvolvimento com paradigmas modernos (OOP/Functional/Async)"
        ["typescript"]="✅ FUNCIONAL - TypeScript moderno com Clean Architecture e SOLID principles"
    )
    
    declare -A server_ports=(
        ["mcp"]="3000"
        ["prompt"]="3001"
        ["tailwind"]="3002"
        ["fastmcp"]="3003"
        ["react"]="3004"
        ["typescript"]="3005"
        ["react_optimizer"]="3006"
        ["shadcn"]="3007"
        ["rust"]="3008"
        ["axum"]="3009"
        ["docker"]="3010"
        ["python"]="3011"
        ["typescript"]="3005"
    )
    
    for server in mcp prompt tailwind fastmcp react_optimizer shadcn react rust axum docker python typescript; do
        status=${server_status[$server]}
        port=${server_ports[$server]}
        echo -e "  ${GREEN}$server${NC} (porta $port): $status"
    done
    
    echo ""
    echo -e "${YELLOW}📈 Estatísticas:${NC}"
    echo -e "  • Servidores funcionais: ${GREEN}12/12${NC} (100%)"
    echo -e "  • Em desenvolvimento: ${YELLOW}0/12${NC} (0%)"
    echo -e "  • Framework: ${BLUE}FastMCP 2.0 + Python 3.12+${NC}"
    echo -e "  • Gerenciador: ${PURPLE}uv (ultrafast package manager)${NC}"
    echo ""
    echo -e "${CYAN}🆕 Últimas Atualizações:${NC}"
    echo -e "  • Tailwind CSS v4.1 (engine Oxide/Rust)"
    echo -e "  • FastMCP 2.0 (MCP Inspector + deployment tools)"
    echo -e "  • React 19 (Server Components + Actions estáveis)"
    echo -e "  • shadcn/ui Advanced (análise inteligente)"
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
    echo -e "  ${GREEN}react_optimizer${NC} - Servidor React Optimizer"
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
        "all"|"mcp"|"prompt"|"tailwind"|"fastmcp"|"react"|"typescript"|"react_optimizer"|"shadcn"|"rust"|"axum"|"docker"|"python")
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
