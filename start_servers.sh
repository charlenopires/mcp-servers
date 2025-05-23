#!/bin/bash

# Script simples para executar servidores MCP
# Versão básica sem interface interativa elaborada

SERVERS_DIR="/Users/fazapp/projects/mcp-servers/servers"

echo "🚀 Iniciador Rápido de Servidores MCP"
echo "======================================"
echo ""

# Lista de servidores
echo "Servidores disponíveis:"
echo "1) mcp_server.py - Analisador de Prompts MCP"
echo "2) prompt_server.py - Servidor de Engenharia de Prompts"  
echo "3) tailwind_server.py - Servidor Tailwind CSS v4.1"
echo "4) mcpprompt_server.py - Servidor MCP Prompt (experimental)"
echo ""
echo "Digite os números dos servidores que deseja executar (ex: 1 3)"
echo "ou 'all' para todos os servidores:"

read -r selection

pids=()

run_server() {
    local file=$1
    local name=$2
    
    echo "▶️  Iniciando $name..."
    (cd "$SERVERS_DIR" && uv run "$file") &
    pids+=($!)
    echo "   PID: ${pids[-1]}"
}

# Processar seleção
if [[ "$selection" == "all" ]]; then
    run_server "mcp_server.py" "Analisador de Prompts MCP"
    run_server "prompt_server.py" "Servidor de Engenharia de Prompts"
    run_server "tailwind_server.py" "Servidor Tailwind CSS v4.1"
    run_server "mcpprompt_server.py" "Servidor MCP Prompt"
else
    for num in $selection; do
        case $num in
            1) run_server "mcp_server.py" "Analisador de Prompts MCP" ;;
            2) run_server "prompt_server.py" "Servidor de Engenharia de Prompts" ;;
            3) run_server "tailwind_server.py" "Servidor Tailwind CSS v4.1" ;;
            4) run_server "mcpprompt_server.py" "Servidor MCP Prompt" ;;
            *) echo "❌ Servidor inválido: $num" ;;
        esac
    done
fi

if [ ${#pids[@]} -gt 0 ]; then
    echo ""
    echo "✅ ${#pids[@]} servidor(es) iniciado(s)!"
    echo "PIDs: ${pids[*]}"
    echo ""
    echo "Pressione Ctrl+C para parar todos os servidores..."
    
    # Aguardar sinal de interrupção
    trap 'echo ""; echo "🛑 Parando servidores..."; for pid in "${pids[@]}"; do kill "$pid" 2>/dev/null; done; echo "✅ Servidores parados."; exit 0' SIGINT
    
    # Aguardar indefinidamente
    while true; do
        sleep 1
    done
else
    echo "❌ Nenhum servidor foi iniciado."
fi
