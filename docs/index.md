# Documentação Completa MCP Servers

## 📚 Bem-vindo à Documentação dos MCP Servers

Esta é a documentação completa do projeto MCP Servers, uma coleção de servidores especializados baseados no protocolo MCP (Model Context Protocol) que fornecem ferramentas para análise e otimização de prompts em português.

![Banner MCP Servers](./assets/documentation_banner.png)

## 🧭 Navegação Rápida

### 📘 Guias

- [Guia de Instalação](guides/installation_guide.md)
- [Guia de Lançamento e Execução](guides/launch_guide.md)
- [Guia de Integração dos Servidores](guides/integration_guide.md)
- [Melhores Práticas MCP](guides/mcp_best_practices.md)
- [Estratégias de Engenharia de Prompts](guides/prompt_strategies.md)
- [Guia de Migração para Tailwind v4.1](guides/tailwind_migration_guide.md)

### 🏗️ Arquitetura

- [Arquitetura dos Servidores MCP](architecture.md)
- [Perguntas Frequentes (FAQ)](faq.md)

### 🖥️ Documentação de Servidores

- [Analisador de Prompts MCP](servers/mcp_server.md)
- [Servidor de Engenharia de Prompts](servers/prompt_server.md)
- [Servidor Tailwind CSS v4.1](servers/tailwind_server.md)

### 📝 Referências de API

- [API do Analisador de Prompts MCP](api/mcp_server_api.md)
- [API do Servidor de Engenharia de Prompts](api/prompt_server_api.md)
- [API do Servidor Tailwind CSS v4.1](api/tailwind_server_api.md)
- [API de Migração Tailwind](api/tailwind_migration_api.md)

### 📋 Exemplos

- [Exemplo do Analisador MCP](examples/mcp_analyzer_example.py)
- [Exemplos de Engenharia de Prompts](examples/prompt_engineering_examples.py)
- [Componentes Tailwind v4.1](examples/tailwind_components.md)
- [Exemplo Integrado](examples/integrated_example.py)

## 🚀 Início Rápido

### Instalação

```bash
# Clonar o repositório
git clone https://github.com/user/mcp-servers.git
cd mcp-servers

# Instalar dependências
pip install -r requirements.txt

# Ou usando uv
uv pip install -r requirements.txt
```

### Executar Servidores

```bash
# Executar todos os servidores com interface interativa
./run_servers.sh

# Ou individualmente
uv run --directory ./servers mcp_server.py
uv run --directory ./servers prompt_server.py
uv run --directory ./servers tailwind_server.py
```

## 📊 Visão Geral dos Servidores

### 1. Analisador de Prompts MCP

O Analisador de Prompts MCP avalia a qualidade dos prompts utilizados para criar servidores MCP, pontuando-os e fornecendo recomendações específicas para melhorias.

**Principais ferramentas:**

- `analisar_prompt_mcp` - Análise completa de prompts
- `obter_melhores_praticas_mcp` - Informações sobre boas práticas
- [Ver documentação completa](servers/mcp_server.md)

### 2. Servidor de Engenharia de Prompts

O Servidor de Engenharia de Prompts otimiza prompts para diferentes tarefas usando estratégias avançadas de engenharia de prompts.

**Principais ferramentas:**

- `otimizar_prompt` - Aplica técnicas de otimização
- `aplicar_estrategia_prompt` - Aplica diferentes estratégias
- [Ver documentação completa](servers/prompt_server.md)

### 3. Servidor Tailwind CSS v4.1

O Servidor Tailwind CSS v4.1 fornece contexto e suporte para desenvolvimento com Tailwind CSS v4.1, incluindo ferramentas para migração e criação de componentes.

**Principais ferramentas:**

- `obter_novidades_tailwind` - Resumo das novidades da v4.1
- `converter_codigo_tailwind` - Ajuda na migração entre versões
- [Ver documentação completa](servers/tailwind_server.md)

## 🔄 Fluxos de Trabalho Comuns

### Análise e Melhoria de Prompts

1. Use o Analisador de Prompts MCP para avaliar seu prompt
2. Identifique os pontos fracos principais
3. Use o Servidor de Engenharia de Prompts para otimizar
4. Valide as melhorias com nova análise

### Desenvolvimento de Interface com Tailwind v4.1

1. Consulte as novidades da versão 4.1
2. Use ferramentas de migração para código existente
3. Gere componentes otimizados para seu contexto
4. Integre com seu servidor MCP

### Fluxo Completo de Desenvolvimento

Consulte o [Guia de Integração](guides/integration_guide.md) para um fluxo completo que combina todos os servidores em um processo de desenvolvimento unificado.

## 🧪 Testes e Validação

O projeto inclui testes abrangentes para todos os servidores:

```bash
# Executar todos os testes
python run_tests.py

# Ou testes específicos
python -m pytest tests/test_mcp_server.py
```

## 📦 Estrutura da Documentação

```text
/docs/
├── index.md                    # Esta página
│
├── servers/                    # Documentação dos servidores
│   ├── mcp_server.md           # Analisador de Prompts MCP
│   ├── prompt_server.md        # Servidor de Engenharia de Prompts
│   └── tailwind_server.md      # Servidor Tailwind CSS v4.1
│
├── api/                        # Referências de API
│   ├── mcp_server_api.md       # API do Analisador MCP
│   ├── prompt_server_api.md    # API do Servidor de Prompts
│   ├── tailwind_server_api.md  # API do Servidor Tailwind
│   └── tailwind_migration_api.md # API de Migração Tailwind
│
├── guides/                     # Guias práticos
│   ├── integration_guide.md    # Guia de integração
│   ├── mcp_best_practices.md   # Melhores práticas MCP
│   ├── prompt_strategies.md    # Estratégias de prompts
│   └── tailwind_migration_guide.md # Migração Tailwind
│
├── examples/                   # Exemplos de código
│   ├── mcp_analyzer_example.py # Exemplo do Analisador
│   ├── prompt_engineering_examples.py # Exemplos de Prompts
│   ├── tailwind_components.md  # Exemplos Tailwind
│   └── integrated_example.py   # Exemplo integrado
│
└── assets/                     # Imagens e recursos
    ├── documentation_banner.png # Banner principal
    ├── integration_diagram.png  # Diagrama de integração
    └── ...                      # Outros recursos visuais
```

## 🤝 Contribuindo com a Documentação

Para contribuir com melhorias na documentação:

1. Siga as convenções de formatação existentes
2. Inclua exemplos práticos e casos de uso
3. Mantenha os links entre documentos atualizados
4. Adicione diagramas e imagens quando relevante

Consulte o [Guia de Contribuição](../CONTRIBUTING.md) para diretrizes completas sobre como contribuir com o projeto.

---

**Desenvolvido para o projeto MCP Servers**
