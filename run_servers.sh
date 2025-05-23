#!/bin/bash

# Script para executar servidores MCP de forma paralela
# Permite seleção interativa dos servidores a serem executados

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Diretório base
BASE_DIR="/Users/fazapp/projects/mcp-servers/servers"

# Array de servidores disponíveis
declare -a SERVERS=(
    "mcp_server.py:Analisador de Prompts MCP"
    "prompt_server.py:Assistente de Melhores Práticas de Engenharia de Prompts"
    "tailwind_server.py:Assistente para Prompts no Contexto do TailwindCSS v4.1"
)

# Array para armazenar PIDs dos processos
declare -a PIDS=()
declare -a SELECTED_SERVERS=()

# Função para exibir banner
show_banner() {
    echo -e "${CYAN}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                    🚀 LAUNCHER MCP SERVERS                   ║"
    echo "║              Execução Paralela de Servidores MCP             ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

# Função para exibir menu de seleção
show_menu() {
    echo -e "${BLUE}📋 Servidores MCP Disponíveis:${NC}"
    echo ""
    
    for i in "${!SERVERS[@]}"; do
        IFS=':' read -r filename description <<< "${SERVERS[$i]}"
        echo -e "  ${YELLOW}[$((i+1))]${NC} ${GREEN}$description${NC}"
        echo -e "      ${PURPLE}→${NC} $filename"
        echo ""
    done
    
    echo -e "${YELLOW}[a]${NC} ${GREEN}Todos os servidores${NC}"
    echo -e "${YELLOW}[q]${NC} ${RED}Sair${NC}"
    echo ""
}

# Função para validar seleção
validate_selection() {
    local input=$1
    
    # Verificar se é 'a' (todos) ou 'q' (sair)
    if [[ "$input" == "a" ]] || [[ "$input" == "q" ]]; then
        return 0
    fi
    
    # Verificar se é um número válido
    if [[ "$input" =~ ^[0-9]+$ ]] && [ "$input" -ge 1 ] && [ "$input" -le "${#SERVERS[@]}" ]; then
        return 0
    fi
    
    return 1
}

# Função para executar servidor
run_server() {
    local server_file=$1
    local description=$2
    
    echo -e "${GREEN}🚀 Iniciando: $description${NC}"
    echo -e "${PURPLE}   Arquivo: $server_file${NC}"
    echo -e "${CYAN}   Comando: uv run --directory $BASE_DIR $server_file${NC}"
    echo ""
    
    # Executar servidor em background
    (
        cd "$BASE_DIR" || exit 1
        uv run "$server_file"
    ) &
    
    local pid=$!
    PIDS+=($pid)
    
    echo -e "${GREEN}✅ Servidor iniciado com PID: $pid${NC}"
    echo ""
}

# Função para parar todos os servidores
stop_all_servers() {
    if [ ${#PIDS[@]} -eq 0 ]; then
        echo -e "${YELLOW}⚠️  Nenhum servidor em execução.${NC}"
        return
    fi
    
    echo -e "${YELLOW}🛑 Parando todos os servidores...${NC}"
    
    for pid in "${PIDS[@]}"; do
        if kill -0 "$pid" 2>/dev/null; then
            echo -e "${BLUE}   Parando PID: $pid${NC}"
            kill -TERM "$pid" 2>/dev/null
            
            # Aguardar término gracioso
            sleep 2
            
            # Forçar término se necessário
            if kill -0 "$pid" 2>/dev/null; then
                echo -e "${RED}   Forçando término do PID: $pid${NC}"
                kill -KILL "$pid" 2>/dev/null
            fi
        fi
    done
    
    PIDS=()
    echo -e "${GREEN}✅ Todos os servidores foram parados.${NC}"
}

# Função para verificar status dos servidores
check_servers_status() {
    if [ ${#PIDS[@]} -eq 0 ]; then
        echo -e "${YELLOW}⚠️  Nenhum servidor em execução.${NC}"
        return
    fi
    
    echo -e "${BLUE}📊 Status dos Servidores:${NC}"
    echo ""
    
    local active_count=0
    for i in "${!PIDS[@]}"; do
        local pid=${PIDS[$i]}
        local server_info=${SELECTED_SERVERS[$i]}
        
        if kill -0 "$pid" 2>/dev/null; then
            echo -e "${GREEN}✅ PID $pid: $server_info (RODANDO)${NC}"
            ((active_count++))
        else
            echo -e "${RED}❌ PID $pid: $server_info (PARADO)${NC}"
        fi
    done
    
    echo ""
    echo -e "${CYAN}📈 Total: $active_count/${#PIDS[@]} servidores ativos${NC}"
}

# Função para exibir logs em tempo real
show_logs() {
    echo -e "${BLUE}📋 Para visualizar logs dos servidores:${NC}"
    echo ""
    
    for i in "${!PIDS[@]}"; do
        local pid=${PIDS[$i]}
        local server_info=${SELECTED_SERVERS[$i]}
        
        if kill -0 "$pid" 2>/dev/null; then
            echo -e "${GREEN}  PID $pid ($server_info):${NC}"
            echo -e "${PURPLE}    tail -f /proc/$pid/fd/1${NC}"
        fi
    done
    echo ""
}

# Função para verificar dependências
check_dependencies() {
    echo -e "${BLUE}🔍 Verificando dependências...${NC}"
    
    # Verificar uv
    if ! command -v uv &> /dev/null; then
        echo -e "${RED}❌ 'uv' não encontrado! Instale com:${NC}"
        echo -e "${YELLOW}   curl -LsSf https://astral.sh/uv/install.sh | sh${NC}"
        return 1
    fi
    
    echo -e "${GREEN}✅ uv encontrado${NC}"
    
    # Verificar se o diretório de servidores existe
    if [ ! -d "$BASE_DIR" ]; then
        echo -e "${RED}❌ Diretório de servidores não encontrado: $BASE_DIR${NC}"
        return 1
    fi
    
    echo -e "${GREEN}✅ Diretório de servidores encontrado${NC}"
    
    # Verificar se os arquivos de servidor existem
    local missing_servers=()
    for server_info in "${SERVERS[@]}"; do
        IFS=':' read -r filename description <<< "$server_info"
        if [ ! -f "$BASE_DIR/$filename" ]; then
            missing_servers+=("$filename")
        fi
    done
    
    if [ ${#missing_servers[@]} -ne 0 ]; then
        echo -e "${YELLOW}⚠️  Servidores não encontrados:${NC}"
        for server in "${missing_servers[@]}"; do
            echo -e "${RED}   - $server${NC}"
        done
        echo ""
        echo -e "${BLUE}ℹ️  Continuando com os servidores disponíveis...${NC}"
    else
        echo -e "${GREEN}✅ Todos os servidores encontrados${NC}"
    fi
    
    echo ""
    return 0
}

# Função principal de controle
control_menu() {
    while true; do
        echo ""
        echo -e "${CYAN}🎛️  Menu de Controle:${NC}"
        echo -e "${YELLOW}[s]${NC} Status dos servidores"
        echo -e "${YELLOW}[l]${NC} Informações de logs"
        echo -e "${YELLOW}[r]${NC} Reiniciar seleção"
        echo -e "${YELLOW}[q]${NC} Parar todos e sair"
        echo ""
        
        read -p "Escolha uma opção: " control_choice
        
        case $control_choice in
            s|S)
                check_servers_status
                ;;
            l|L)
                show_logs
                ;;
            r|R)
                stop_all_servers
                main
                return
                ;;
            q|Q)
                stop_all_servers
                echo -e "${GREEN}👋 Até logo!${NC}"
                exit 0
                ;;
            *)
                echo -e "${RED}❌ Opção inválida!${NC}"
                ;;
        esac
    done
}

# Função principal
main() {
    show_banner
    
    # Verificar dependências
    if ! check_dependencies; then
        exit 1
    fi
    
    while true; do
        show_menu
        
        read -p "Digite sua seleção (números separados por espaço, 'a' para todos, 'q' para sair): " selection
        
        # Processar seleção
        if [[ "$selection" == "q" ]]; then
            echo -e "${GREEN}👋 Até logo!${NC}"
            exit 0
        elif [[ "$selection" == "a" ]]; then
            # Selecionar todos os servidores
            SELECTED_SERVERS=()
            for server_info in "${SERVERS[@]}"; do
                IFS=':' read -r filename description <<< "$server_info"
                if [ -f "$BASE_DIR/$filename" ]; then
                    SELECTED_SERVERS+=("$description")
                    run_server "$filename" "$description"
                fi
            done
            break
        else
            # Processar seleções individuais
            SELECTED_SERVERS=()
            local valid_selection=true
            
            # Converter string em array
            read -ra choices <<< "$selection"
            
            # Validar todas as escolhas primeiro
            for choice in "${choices[@]}"; do
                if ! validate_selection "$choice"; then
                    echo -e "${RED}❌ Seleção inválida: $choice${NC}"
                    valid_selection=false
                    break
                fi
            done
            
            if [ "$valid_selection" = true ]; then
                # Executar servidores selecionados
                for choice in "${choices[@]}"; do
                    local index=$((choice - 1))
                    local server_info=${SERVERS[$index]}
                    IFS=':' read -r filename description <<< "$server_info"
                    
                    if [ -f "$BASE_DIR/$filename" ]; then
                        SELECTED_SERVERS+=("$description")
                        run_server "$filename" "$description"
                    else
                        echo -e "${YELLOW}⚠️  Servidor não encontrado: $filename${NC}"
                    fi
                done
                break
            fi
        fi
    done
    
    # Menu de controle
    if [ ${#PIDS[@]} -gt 0 ]; then
        echo -e "${GREEN}🎉 Servidores iniciados com sucesso!${NC}"
        control_menu
    else
        echo -e "${YELLOW}⚠️  Nenhum servidor foi iniciado.${NC}"
    fi
}

# Capturar sinais para limpeza
trap 'stop_all_servers; exit 0' SIGINT SIGTERM

# Executar função principal
main
