# Guia de Lançamento dos Servidores MCP

## 📋 Introdução

Este documento explica em detalhes como iniciar, gerenciar e monitorar os servidores MCP utilizando os scripts de execução fornecidos no projeto.

![Launcher MCP](../assets/launcher_screenshot.png)

## 🚀 Scripts de Execução

O projeto MCP Servers inclui dois scripts principais para execução dos servidores:

1. **run_servers.sh** - Launcher interativo completo com interface visual e controles avançados
2. **start_servers.sh** - Inicializador simplificado para execução rápida

## 🎮 Launcher Interativo (run_servers.sh)

### Funcionalidades

O launcher interativo oferece uma interface completa para gerenciar os servidores:

- Interface colorida com emojis para melhor visualização
- Menu de controle interativo em tempo real
- Monitoramento de status de cada servidor
- Reinicialização individual ou em lote
- Parada gracosa com limpeza de processos
- Informações detalhadas de logs e PIDs

### Comandos Básicos

Para iniciar o launcher interativo:

```bash
./run_servers.sh
```

### Menu de Controle

Após iniciar o launcher, você terá acesso ao seguinte menu:

```
🚀 LAUNCHER MCP SERVERS 🚀

Servidores Disponíveis:
1. 🔍 Analisador de Prompts MCP
2. 📝 Servidor de Engenharia de Prompts
3. 🎨 Servidor Tailwind CSS v4.1
4. 🧪 Servidor MCP Prompt (experimental)

Comandos:
- Iniciar servidores: Digite os números (ex: 1 3) ou "all"
- Status: s ou status
- Reiniciar: r <número> ou restart <número>
- Parar: q ou quit
```

### Exemplos de Uso

#### Iniciar servidores específicos

```
> 1 3
🚀 Iniciando Analisador de Prompts MCP...
🚀 Iniciando Servidor Tailwind CSS v4.1...
✅ Todos os servidores selecionados foram iniciados!
```

#### Verificar status

```
> status
📊 STATUS DOS SERVIDORES:
1. 🔍 Analisador de Prompts MCP: ATIVO (PID: 12345)
2. 📝 Servidor de Engenharia de Prompts: INATIVO
3. 🎨 Servidor Tailwind CSS v4.1: ATIVO (PID: 12346)
4. 🧪 Servidor MCP Prompt: INATIVO
```

#### Reiniciar um servidor

```
> restart 1
🔄 Reiniciando Analisador de Prompts MCP...
✅ Analisador de Prompts MCP reiniciado com sucesso!
```

#### Parar todos os servidores

```
> quit
🛑 Parando todos os servidores...
✅ Todos os servidores foram encerrados com sucesso!
```

## ⚡ Inicializador Rápido (start_servers.sh)

### Funcionalidades

O inicializador rápido oferece uma interface simplificada:

- Interface direta e minimalista
- Seleção rápida por números
- Execução paralela automática
- Tratamento de sinais para parada limpa

### Comandos Básicos

Para iniciar o launcher simplificado:

```bash
./start_servers.sh
```

Quando solicitado, você pode:

- Digitar números separados por espaço para iniciar servidores específicos (ex: `1 3`)
- Digitar `all` para iniciar todos os servidores
- Usar Ctrl+C para parar todos os servidores em execução

### Exemplos de Uso

#### Iniciar servidores específicos

```
$ ./start_servers.sh
Servidores disponíveis:
1. Analisador de Prompts MCP
2. Servidor de Engenharia de Prompts
3. Servidor Tailwind CSS v4.1
4. Servidor MCP Prompt (experimental)

Digite os números dos servidores para iniciar (ex: 1 3) ou "all" para todos:
> 1 2
Iniciando: Analisador de Prompts MCP
Iniciando: Servidor de Engenharia de Prompts
Servidores iniciados em background.
```

#### Iniciar todos os servidores

```
$ ./start_servers.sh
Servidores disponíveis:
1. Analisador de Prompts MCP
2. Servidor de Engenharia de Prompts
3. Servidor Tailwind CSS v4.1
4. Servidor MCP Prompt (experimental)

Digite os números dos servidores para iniciar (ex: 1 3) ou "all" para todos:
> all
Iniciando todos os servidores...
Servidores iniciados em background.
```

## 🔧 Personalização e Configuração

### Variáveis de Ambiente

Os scripts de execução suportam as seguintes variáveis de ambiente:

- `MCP_LOG_DIR`: Diretório para armazenamento de logs (padrão: `./logs`)
- `MCP_DEBUG`: Ativa modo de debug com informações adicionais (valores: `true`/`false`)
- `MCP_TIMEOUT`: Tempo de espera para verificação de inicialização (em segundos)

Exemplo de uso:

```bash
MCP_DEBUG=true MCP_LOG_DIR=./custom_logs ./run_servers.sh
```

### Arquivo de Configuração

Para configurações persistentes, você pode criar um arquivo `.mcp_config` na raiz do projeto:

```bash
# Exemplo de .mcp_config
MCP_LOG_DIR=./custom_logs
MCP_DEBUG=false
MCP_TIMEOUT=5
```

## 📊 Monitoramento e Logs

### Diretório de Logs

Por padrão, os logs são armazenados no diretório `./logs` com a seguinte estrutura:

```
/logs/
├── mcp_server_YYYY-MM-DD.log
├── prompt_server_YYYY-MM-DD.log
├── tailwind_server_YYYY-MM-DD.log
└── mcpprompt_server_YYYY-MM-DD.log
```

### Visualização de Logs em Tempo Real

Para visualizar os logs em tempo real de um servidor específico:

```bash
tail -f logs/mcp_server_$(date +%Y-%m-%d).log
```

## 🔍 Solução de Problemas

### Problemas Comuns e Soluções

#### Servidor não inicia

Verifique:

- Se todas as dependências estão instaladas
- Se não há outro processo usando a mesma porta
- Os logs para mensagens de erro específicas

```bash
cat logs/mcp_server_$(date +%Y-%m-%d).log | grep ERROR
```

#### Servidor trava ou não responde

Para reiniciar um servidor travado:

```bash
# No launcher interativo
> restart <número>

# Ou manualmente
pkill -f "python.*mcp_server.py"
uv run --directory ./servers mcp_server.py
```

#### Conflitos de porta

Se houver conflitos de porta, você pode modificar as portas usadas editando os arquivos de configuração dos servidores.

### Diagnóstico Avançado

Para diagnosticar problemas mais complexos, você pode usar os seguintes comandos e técnicas:

#### 1. Verificar estado de todos os processos

Para ver todos os processos relacionados aos servidores MCP:

```bash
ps aux | grep "python.*server.py"
```

#### 2. Verificar uso de porta

Para verificar se alguma porta necessária já está em uso:

```bash
# Verificar portas comuns usadas pelos servidores
lsof -i :8000
lsof -i :8001
lsof -i :8002
```

#### 3. Verificar logs com detalhes de erro

Para extrair apenas mensagens de erro dos logs:

```bash
grep -E "ERROR|Exception|Failed" logs/*.log
```

#### 4. Análise de dependências

Para verificar se todas as dependências estão instaladas corretamente:

```bash
pip freeze | grep -E "fastmcp|pydantic|typer|rich"
```

#### 5. Executar em modo debug

Para iniciar os servidores em modo de depuração:

```bash
MCP_DEBUG=true ./run_servers.sh
```

Este modo exibirá mensagens detalhadas sobre a inicialização e execução dos servidores.

## 🔧 Customização Avançada

### Personalização do Launcher

Você pode personalizar o comportamento do launcher criando um arquivo `.mcp_launcher_config` na raiz do projeto:

```bash
# Exemplo de .mcp_launcher_config
MCP_STARTUP_TIMEOUT=10        # Tempo de espera para inicialização (segundos)
MCP_DEFAULT_SERVERS="1 3"     # Servidores para iniciar automaticamente
MCP_THEME="emoji"             # Tema da interface (emoji, minimal, classic)
MCP_AUTOSTART=true            # Iniciar automaticamente sem prompt
```

### Hooks Personalizados

O launcher suporta hooks personalizados para executar comandos antes ou depois da inicialização dos servidores:

1. Crie um diretório `hooks` na raiz do projeto:

```bash
mkdir -p hooks/pre-start hooks/post-start hooks/shutdown
```

2. Adicione scripts executáveis a esses diretórios:

```bash
# Exemplo: hooks/pre-start/check-deps.sh
#!/bin/bash
echo "Verificando dependências..."
pip freeze | grep -E "fastmcp|pydantic"
```

### Integração com Serviços Externos

Para integrar os servidores MCP com serviços externos, você pode:

#### 1. Configurar Proxy Reverso

Exemplo com Nginx:

```nginx
# Exemplo de configuração para /etc/nginx/sites-available/mcp-servers
server {
    listen 80;
    server_name mcp.example.com;

    location /mcp/ {
        proxy_pass http://localhost:8000/;
    }

    location /prompt/ {
        proxy_pass http://localhost:8001/;
    }

    location /tailwind/ {
        proxy_pass http://localhost:8002/;
    }
}
```

#### 2. Iniciar como Serviço Systemd

Crie um arquivo de serviço systemd para inicialização automática:

```ini
# /etc/systemd/system/mcp-servers.service
[Unit]
Description=MCP Servers Suite
After=network.target

[Service]
User=<seu_usuario>
WorkingDirectory=/path/to/mcp-servers
ExecStart=/path/to/mcp-servers/run_servers.sh --no-interactive
Restart=on-failure
Environment="MCP_LOG_DIR=/var/log/mcp-servers"

[Install]
WantedBy=multi-user.target
```

Ative e inicie o serviço:

```bash
sudo systemctl enable mcp-servers
sudo systemctl start mcp-servers
```
