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
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

# Função de ajuda
show_help() {
    echo -e "${BLUE}📖 Uso do Script:${NC}"
    echo ""
    echo -e "  ${GREEN}$0${NC} [comando] [opções]"
    echo ""
    echo -e "${YELLOW}Comandos disponíveis:${NC}"
    echo -e "  ${GREEN}list${NC}           - Lista todos os servidores disponíveis"
    echo -e "  ${GREEN}all${NC}            - Executa todos os servidores"
    echo -e "  ${GREEN}mcp${NC}            - Executa o servidor MCP"
    echo -e "  ${GREEN}prompt${NC}         - Executa o servidor de Prompts"
    echo -e "  ${GREEN}tailwind${NC}       - Executa o servidor Tailwind"
    echo -e "  ${GREEN}fastmcp${NC}        - Executa o servidor FastMCP"
    echo -e "  ${GREEN}react${NC}          - Executa o servidor React"
    echo -e "  ${GREEN}typescript${NC}     - Executa o servidor TypeScript"
    echo ""
    echo -e "${YELLOW}Opções:${NC}"
    echo -e "  ${GREEN}--dev${NC}          - Modo desenvolvimento (mais logs)"
    echo -e "  ${GREEN}--quiet${NC}        - Modo silencioso"
    echo -e "  ${GREEN}--port PORT${NC}    - Define porta personalizada"
    echo -e "  ${GREEN}--help${NC}         - Mostra esta ajuda"
    echo ""
    echo -e "${YELLOW}Exemplos:${NC}"
    echo -e "  ${PURPLE}$0 list${NC}                    # Lista servidores"
    echo -e "  ${PURPLE}$0 mcp${NC}                     # Inicia servidor MCP"
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
    
    # Se nenhum argumento foi fornecido, mostrar ajuda
    if [ $# -eq 0 ]; then
        show_help
        echo ""
        echo -e "${CYAN}🔍 Listando servidores disponíveis:${NC}"
        echo ""
        uv run python main.py list
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
        "all"|"mcp"|"prompt"|"tailwind"|"fastmcp"|"react"|"typescript")
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
