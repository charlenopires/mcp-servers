# 🚀 MCP Servers v2.0 - Conjunto de Servidores MCP em Português

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![FastMCP](https://img.shields.io/badge/FastMCP-2.4.0%2B-green)](https://python.langchain.com/)
[![Licença](https://img.shields.io/badge/Licença-MIT-orange)](LICENSE)
[![Testes](https://img.shields.io/badge/Testes-Pytest-green)](https://pytest.org/)

Plataforma modernizada de servidores MCP (Model Context Protocol) em português para processamento especializado de prompts, incluindo análise de prompts MCP, engenharia de prompts e suporte para Tailwind CSS v4.1.

![Banner MCP Servers](https://github.com/user/mcp-servers/raw/main/docs/banner.png)

## 🌟 Novidades da Versão 2.0

### 🚀 Gerenciamento Centralizado

- **Launcher Principal**: `main.py` unifica a execução de todos os servidores
- **Interface Simplificada**: Scripts `run_servers.sh` e `run_tests.py` modernizados
- **Execução Assíncrona**: Suporte nativo a operações assíncronas

### 🛠️ Sistema de Build Moderno

- **uv Package Manager**: Migração completa do pip para uv
- **pyproject.toml**: Configuração centralizada do projeto
- **Build System**: Hatchling como backend de build

### 🧪 Framework de Testes Modernizado

- **Pytest**: Framework de testes profissional
- **Cobertura de Código**: Relatórios de cobertura integrados
- **Testes Paralelos**: Execução otimizada de testes

## 🌟 Visão Geral

MCP Servers é uma coleção de servidores especializados baseados no protocolo MCP (Model Context Protocol) que fornecem ferramentas para análise e otimização de prompts em português. Este projeto apresenta uma abordagem modular para trabalhar com diferentes aspectos de engenharia de prompts e desenvolvimento de servidores MCP.

### ✨ Principais Recursos

- 🔍 **Análise de Prompts MCP**: Avalia prompts para criação de servidores MCP
- 📝 **Engenharia de Prompts**: Otimiza prompts para diferentes tarefas
- 🎨 **Suporte a Tailwind CSS v4.1**: Ajuda com prompts no contexto da nova versão
- 🧪 **Testes Completos**: Conjunto abrangente de testes para todos os servidores
- 🚀 **Execução Paralela**: Scripts para executar servidores em paralelo
- 🇧🇷 **100% em Português**: Código, comentários e documentação

## 📦 Servidores Disponíveis

### 1. Analisador de Prompts MCP (`mcp_server.py`)

Analisa prompts para criação de servidores MCP, pontuando-os (1-10) e fornecendo recomendações específicas baseadas nas melhores práticas da documentação MCP.

**Ferramentas:**

- `analisar_prompt_mcp` - Análise completa de prompts
- `obter_melhores_praticas_mcp` - Informações sobre boas práticas
- `sugerir_melhorias_prompt` - Sugestões específicas
- `validar_requisitos_mcp` - Validação contra requisitos MCP

### 2. Servidor de Engenharia de Prompts (`prompt_server.py`)

Otimiza prompts para diferentes tarefas usando estratégias avançadas de engenharia de prompts.

**Ferramentas:**

- `otimizar_prompt` - Aplica técnicas de otimização
- `analisar_estrutura_prompt` - Avalia estrutura do prompt
- `aplicar_estrategia_prompt` - Aplica diferentes estratégias
- `gerar_prompt_template` - Cria templates para diferentes cenários

### 3. Servidor Tailwind CSS v4.1 (`tailwind_server.py`)

Fornece contexto e suporte para desenvolvimento com Tailwind CSS v4.1.

**Ferramentas:**

- `obter_novidades_tailwind` - Resumo das novidades da v4.1
- `converter_codigo_tailwind` - Ajuda na migração entre versões
- `otimizar_classes_tailwind` - Otimiza uso de classes
- `gerar_componentes_tailwind` - Cria componentes seguindo boas práticas

### 4. Servidor MCP Prompt (Experimental) (`mcpprompt_server.py`)

Versão experimental para criação de prompts MCP (em desenvolvimento).

## 📚 Documentação

Documentação completa está disponível no diretório `/docs`:

- [Índice da Documentação](docs/index.md)
- **Guias**:
  - [Guia de Instalação](docs/guides/installation_guide.md)
  - [Guia de Lançamento](docs/guides/launch_guide.md)
  - [Guia de Integração](docs/guides/integration_guide.md)
  - [Melhores Práticas MCP](docs/guides/mcp_best_practices.md)
  - [Estratégias de Prompts](docs/guides/prompt_strategies.md)
  - [Migração Tailwind v4.1](docs/guides/tailwind_migration_guide.md)
- **Arquitetura**:
  - [Visão Geral da Arquitetura](docs/architecture.md)
  - [Perguntas Frequentes (FAQ)](docs/faq.md)
- **API de Referência**:
  - [API do Analisador MCP](docs/api/mcp_server_api.md)
  - [API do Servidor de Prompts](docs/api/prompt_server_api.md)
  - [API do Servidor Tailwind](docs/api/tailwind_server_api.md)
  - [API de Migração Tailwind](docs/api/tailwind_migration_api.md)
- **Exemplos**:
  - [Exemplo Integrado](docs/examples/integrated_example.py)
  - [Exemplo do Analisador MCP](docs/examples/mcp_analyzer_example.py)
  - [Exemplos de Engenharia de Prompts](docs/examples/prompt_engineering_examples.py)
  - [Componentes Tailwind v4.1](docs/examples/tailwind_components.md)

## 🛠️ Instalação

### Pré-requisitos

- Python 3.12+
- uv (Universal Python Package Manager)

### Configuração Rápida

```bash
# Clonar o repositório
git clone https://github.com/user/mcp-servers.git
cd mcp-servers

# Instalar uv (se ainda não instalado)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Instalar dependências
uv sync

# Verificar instalação
python main.py --help
```

## 🚀 Uso Rápido

### Launcher Principal

O novo launcher centralizado permite executar todos os servidores de forma unificada:

```bash
# Executar servidor específico
python main.py mcp          # Analisador de prompts MCP
python main.py prompt       # Servidor de engenharia de prompts
python main.py tailwind     # Servidor Tailwind CSS

# Executar todos os servidores (modo desenvolvimento)
python main.py all

# Ajuda completa
python main.py --help
```

### Scripts de Execução

```bash
# Interface interativa (recomendado)
./run_servers.sh

# Execução direta com menu
bash run_servers.sh menu

# Executar servidor específico
bash run_servers.sh mcp
```

### Executar Testes

```bash
# Todos os testes
python run_tests.py

# Teste específico
python run_tests.py mcp_server

# Usando pytest diretamente
uv run python -m pytest tests/ -v
```

## 📋 Exemplos de Uso

### Análise de Prompt MCP

```python
# Usando o launcher principal
import subprocess

# Iniciar o servidor MCP
process = subprocess.Popen(['python', 'main.py', 'mcp'])

# Ou usar diretamente a biblioteca
from servers.mcp_server import AnalisadorPromptMCP

analisador = AnalisadorPromptMCP()
resultado = analisador.analisar_prompt(
    "Criar um servidor MCP para análise de código Python"
)

print(f"Pontuação: {resultado.pontuacao}/10")
print(f"Recomendações: {resultado.recomendacoes}")
```

### Execução de Múltiplos Servidores

```bash
# Interface interativa completa
./run_servers.sh

# Executar todos os servidores em desenvolvimento
python main.py all --dev

# Executar servidores específicos
python main.py mcp prompt tailwind
```

```python
from servers.mcp_server import AnalisadorPromptMCP

# Inicializar analisador
analisador = AnalisadorPromptMCP()

# Analisar um prompt
resultado = analisador.analisar_prompt(
python main.py mcp prompt tailwind
```

## 🧪 Testes

O projeto v2.0 inclui um sistema de testes modernizado com pytest:

```bash
# Executar todos os testes
python run_tests.py

# Testes específicos
python run_tests.py mcp_server
python run_tests.py prompt_server

# Usando pytest diretamente
uv run python -m pytest tests/ -v

# Com cobertura (se disponível)
uv run python -m pytest tests/ --cov=servers --cov-report=term-missing
```

### Testes Incluídos

- ✅ `test_mcp_server.py` - Analisador de Prompts MCP
- ✅ `test_prompt_server.py` - Servidor de Engenharia de Prompts
- ✅ `test_tailwind_server.py` - Servidor Tailwind CSS

## 📁 Estrutura do Projeto v2.0

```text
mcp-servers/
├── 🚀 main.py                  # Launcher principal
├── 🔧 pyproject.toml           # Configuração do projeto (uv)
├── 🧪 run_tests.py             # Runner de testes modernizado
├── 📜 run_servers.sh           # Script de execução simplificado
├── � README.md                # Este arquivo
│
├── 🖥️ servers/                 # Servidores MCP
│   ├── mcp_server.py           # Analisador de prompts MCP
│   ├── prompt_server.py        # Engenharia de prompts
│   ├── tailwind_server.py      # Suporte Tailwind CSS v4.1
│   ├── fastmcp_server.py       # Servidor FastMCP
│   ├── react_server.py         # Servidor React
│   └── typescript_server.py    # Servidor TypeScript
│
├── 🧪 tests/                   # Testes com pytest
│   ├── test_mcp_server.py      # Testes do analisador MCP
│   ├── test_prompt_server.py   # Testes do servidor de prompts
│   └── test_tailwind_server.py # Testes do servidor Tailwind
│
└── 📚 docs/                    # Documentação completa
    ├── guides/                 # Guias de uso
    ├── api/                    # Referências de API
    ├── examples/               # Exemplos práticos
    └── servers/                # Docs dos servidores
```

├── �📜 run_servers.sh # Launcher interativo completo
├── 📜 start_servers.sh # Inicializador rápido
├── 📜 run_tests.py # Executor de testes

```

## 🌐 Protocolo MCP (Model Context Protocol)

O MCP é um protocolo que permite estender modelos de linguagem com ferramentas personalizadas. Cada servidor neste projeto implementa ferramentas MCP específicas para diferentes domínios de processamento de prompts.

### Princípios de Design MCP v2.0

1. **Design Focado**: Cada ferramenta realiza uma função específica e bem definida
2. **Arquitetura Assíncrona**: Suporte nativo a operações assíncronas
3. **Tratamento Robusto de Erros**: Validação robusta de entradas e saídas
4. **Documentação Clara**: Cada ferramenta tem documentação detalhada
5. **Entradas/Saídas Estruturadas**: Uso de Pydantic para validação de esquema

## 📊 Sistema de Pontuação

O Analisador de Prompts MCP avalia prompts em critérios específicos (pontuação 1-10):

| Critério                     | Descrição                                  | Importância |
| ---------------------------- | ------------------------------------------ | ----------- |
| 🎯 Propósito Claro           | Objetivo específico e bem definido         | Alta        |
| 🛠️ Design de Ferramentas     | Ferramentas focadas e bem nomeadas        | Alta        |
| ⚠️ Tratamento de Erros       | Validação e tratamento de exceções        | Alta        |
| 📝 Documentação              | Descrição clara das ferramentas           | Média       |
| 🔒 Segurança                 | Práticas recomendadas de segurança        | Média       |
| 📋 Esquema de Dados          | Estruturas de dados bem definidas         | Média       |
| ⚡ Performance               | Considerações de otimização               | Baixa       |
| 🔧 Protocolo de Transporte   | Especificação clara do protocolo          | Baixa       |

## 🧰 Ferramentas de Desenvolvimento

### Sistema de Build Moderno

- **uv**: Gerenciador de pacotes ultrarrápido
- **pyproject.toml**: Configuração centralizada
- **Hatchling**: Backend de build moderno

### Scripts de Automação

- 🚀 `main.py` - Launcher centralizado para todos os servidores
- 🔧 `run_servers.sh` - Interface interativa simplificada
- 🧪 `run_tests.py` - Runner de testes modernizado

Versão simplificada para inicialização rápida:

- Mínima interação necessária
- Execução paralela automática
- Tratamento de sinais para parada limpa

Para documentação completa sobre os scripts, consulte o [Guia de Lançamento](docs/guides/launch_guide.md).

## 📈 Roadmap

- [ ] Adicionar suporte para análise de prompts em inglês
- [ ] Integrar novos modelos de avaliação de prompts
- [ ] Expandir conjunto de testes com casos mais complexos
- [ ] Criar API REST para acesso remoto aos servidores
- [ ] Desenvolver interface web para visualização de resultados
- [ ] Adicionar benchmark comparativo entre estratégias de prompts
- [ ] Implementar suporte a Tailwind v4.2 (próxima versão)
- [ ] Adicionar integração com frameworks populares (React, Vue, etc.)

Para sugerir novos recursos ou colaborar em itens do roadmap, abra uma issue no GitHub.

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-ferramenta`)
## 📚 Documentação

Documentação completa está disponível no diretório `/docs`:

- [📖 Índice da Documentação](docs/index.md)
- **📘 Guias**:
  - [Guia de Instalação](docs/guides/installation_guide.md)
  - [Guia de Lançamento](docs/guides/launch_guide.md)
  - [Guia de Integração](docs/guides/integration_guide.md)
  - [Melhores Práticas MCP](docs/guides/mcp_best_practices.md)
  - [Estratégias de Prompts](docs/guides/prompt_strategies.md)
  - [Migração Tailwind v4.1](docs/guides/tailwind_migration_guide.md)
- **🏗️ Arquitetura**:
  - [Visão Geral da Arquitetura](docs/architecture.md)
  - [Perguntas Frequentes (FAQ)](docs/faq.md)
- **📝 API de Referência**:
  - [API do Analisador MCP](docs/api/mcp_server_api.md)
  - [API do Servidor de Prompts](docs/api/prompt_server_api.md)
  - [API do Servidor Tailwind](docs/api/tailwind_server_api.md)

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-ferramenta`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova ferramenta de análise'`)
4. Push para a branch (`git push origin feature/nova-ferramenta`)
5. Abra um Pull Request

## 📜 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo `LICENSE` para detalhes.

## 🙏 Agradecimentos

- [FastMCP](https://github.com/fastmcp/fastmcp) - Framework para desenvolvimento de servidores MCP
- [Pydantic](https://docs.pydantic.dev/) - Validação de dados e esquemas
- [uv](https://github.com/astral-sh/uv) - Gerenciador de pacotes Python ultrarrápido
- [Pytest](https://docs.pytest.org/) - Framework de testes moderno

## 📌 Informações do Projeto

**Versão**: 2.0
**Python**: 3.12+
**Tipo**: Servidores MCP
**Status**: Produção

---

<div align="center">

**🚀 MCP Servers v2.0**
*Desenvolvido com ❤️ pela Comunidade MCP Brasil*

[![⭐ Star no GitHub](https://img.shields.io/github/stars/user/mcp-servers?style=social)](https://github.com/user/mcp-servers)

</div>
```
