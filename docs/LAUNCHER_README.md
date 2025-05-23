# 🚀 Scripts de Execução dos Servidores MCP

Este diretório contém scripts para facilitar a execução dos servidores MCP de forma individual ou paralela.

## 📁 Estrutura dos Scripts

### `run_servers.sh` - Launcher Completo

Script interativo avançado com interface colorida e controle completo dos servidores.

**Características:**

- ✨ Interface interativa com cores
- 🎛️ Menu de controle em tempo real
- 📊 Monitoramento de status dos servidores
- 🔄 Reinicialização individual ou em lote
- 🛑 Parada gracosa de todos os servidores
- 📋 Informações de logs
- ✅ Verificação de dependências

**Como usar:**

```bash
./run_servers.sh
```

### `start_servers.sh` - Inicializador Simples

Script básico e direto para execução rápida dos servidores.

**Características:**

- 🎯 Interface simples e direta
- ⚡ Execução rápida
- 🔢 Seleção por números ou "all"
- 🛑 Parada com Ctrl+C

**Como usar:**

```bash
./start_servers.sh
```

## 🖥️ Servidores Disponíveis

1. **`mcp_server.py`** - Analisador de Prompts MCP

   - Analisa e pontua prompts para criação de servidores MCP
   - Fornece sugestões de melhorias e melhores práticas

2. **`prompt_server.py`** - Servidor de Engenharia de Prompts

   - Otimização e refinamento de prompts
   - Diferentes estratégias de prompt engineering

3. **`tailwind_server.py`** - Servidor Tailwind CSS v4.1

   - Contexto e documentação do Tailwind CSS v4.1
   - Assistência para desenvolvimento com Tailwind

4. **`mcpprompt_server.py`** - Servidor MCP Prompt (experimental)
   - Servidor experimental para criação de prompts MCP

## ⚙️ Pré-requisitos

### uv (Universal Python Package Manager)

```bash
# Instalar uv
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Dependências Python

```bash
# Instalar dependências
pip install -r requirements.txt
```

## 🎮 Exemplos de Uso

### Executar Todos os Servidores

```bash
# Com o launcher completo
./run_servers.sh
# Selecionar "a" para todos

# Com o inicializador simples
./start_servers.sh
# Digite "all"
```

### Executar Servidores Específicos

```bash
# Executar apenas o analisador e o Tailwind
./start_servers.sh
# Digite "1 3"
```

### Controle Avançado (run_servers.sh)

Após iniciar os servidores, você terá acesso a:

- **[s]** - Verificar status dos servidores
- **[l]** - Obter informações de logs
- **[r]** - Reiniciar seleção
- **[q]** - Parar todos e sair

## 🐛 Troubleshooting

### Problema: "uv: command not found"

```bash
# Instalar uv
curl -LsSf https://astral.sh/uv/install.sh | sh
# Reiniciar terminal ou executar:
source ~/.bashrc  # ou ~/.zshrc
```

### Problema: "Servidor não encontrado"

Verifique se os arquivos estão no diretório correto:

```bash
ls -la /Users/fazapp/projects/mcp-servers/servers/
```

### Problema: Porta já em uso

Se um servidor não conseguir iniciar devido a porta em uso:

```bash
# Verificar processos usando a porta
lsof -i :PORT_NUMBER
# Matar processo específico
kill -9 PID
```

## 📝 Logs e Monitoramento

### Visualizar Logs em Tempo Real

```bash
# Para um PID específico
tail -f /proc/PID/fd/1

# Ou usar o comando logs do sistema
journalctl -f
```

### Verificar Status dos Processos

```bash
# Listar todos os processos Python/uv
ps aux | grep -E "(python|uv)"

# Verificar servidor específico
ps aux | grep mcp_server
```

## 🔧 Personalização

Para adicionar novos servidores, edite o array `SERVERS` nos scripts:

```bash
# Em run_servers.sh
SERVERS=(
    "seu_servidor.py:Descrição do Seu Servidor"
    # ... outros servidores
)

# Em start_servers.sh, adicione nova opção no case
5) run_server "seu_servidor.py" "Descrição do Seu Servidor" ;;
```

## 🚨 Importante

- ⚠️ **Nunca execute em produção sem revisar os scripts**
- 🔒 **Sempre verifique permissões antes de executar**
- 📝 **Mantenha logs para debugging**
- 🔄 **Use Ctrl+C para parada gracosa**

---

**Desenvolvido para o projeto MCP Servers**  
📧 Para suporte, verifique os logs ou abra uma issue no repositório.
