# 🚀 MCP Servers v2.0 - Conjunto de Servidores MCP em Português

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![FastMCP](https://img.shields.io/badge/FastMCP-2.4.0%2B-green)](https://github.com/fastmcp/fastmcp)
[![uv](https://img.shields.io/badge/uv-Package%20Manager-purple)](https://github.com/astral-sh/uv)
[![Licença](https://img.shields.io/badge/Licença-MIT-orange)](LICENSE)
[![Testes](https://img.shields.io/badge/Testes-32%2F37%20Passed-green)](https://pytest.org/)

Plataforma modernizada de servidores MCP (Model Context Protocol) em português para processamento especializado de prompts, incluindo análise de prompts MCP, engenharia de prompts e suporte para Tailwind CSS v4.1.

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
- 🧪 **Testes Completos**: 32/37 testes passando com cobertura abrangente
- 🚀 **Execução Paralela**: Scripts para executar servidores em paralelo
- 🇧🇷 **100% em Português**: Código, comentários e documentação em português
- ⚡ **Build System Moderno**: uv + pyproject.toml + hatchling
- 🔧 **Launcher Unificado**: main.py centraliza execução de todos os servidores

## 📦 Servidores Disponíveis

### 1. ✅ Analisador de Prompts MCP (`mcp_server.py`) - **FUNCIONAL**

Analisa prompts para criação de servidores MCP, pontuando-os (1-10) e fornecendo recomendações específicas baseadas nas melhores práticas da documentação MCP.

**Ferramentas:**

- `analisar_prompt_mcp` - Análise completa de prompts
- `obter_melhores_praticas_mcp` - Informações sobre boas práticas
- `sugerir_melhorias_prompt` - Sugestões específicas
- `validar_requisitos_mcp` - Validação contra requisitos MCP

### 2. ✅ Servidor de Engenharia de Prompts (`prompt_server.py`) - **FUNCIONAL**

Otimiza prompts para diferentes tarefas usando estratégias avançadas de engenharia de prompts.

**Ferramentas:**

- `otimizar_prompt` - Aplica técnicas de otimização
- `analisar_estrutura_prompt` - Avalia estrutura do prompt
- `aplicar_estrategia_prompt` - Aplica diferentes estratégias
- `gerar_prompt_template` - Cria templates para diferentes cenários

### 3. ✅ Servidor Tailwind CSS v4.1 (`tailwind_server.py`) - **FUNCIONAL**

Fornece contexto e suporte para desenvolvimento com Tailwind CSS v4.1.

**Ferramentas:**

- `obter_novidades_tailwind` - Resumo das novidades da v4.1
- `converter_codigo_tailwind` - Ajuda na migração entre versões
- `otimizar_classes_tailwind` - Otimiza uso de classes
- `gerar_componentes_tailwind` - Cria componentes seguindo boas práticas

### 4. ✅ React Optimizer Server (`react_optimizer_server.py`) - **FUNCIONAL** 🆕

Servidor unificado para análise/otimização de código React existente e otimização de prompts para geração de código React moderno seguindo tendências UI/UX 2025.

**Principais Funcionalidades:**

- 🔍 **Análise de Código**: Avalia componentes React existentes com scoring e recomendações
- ⚡ **Otimização Automática**: Aplica tendências 2025 automaticamente (glassmorphism, dark mode, micro-animações)
- 📝 **Análise de Prompts**: Avalia qualidade de prompts para geração de código React
- 🚀 **Otimização de Prompts**: Transforma prompts básicos em versões estruturadas para AI tools

**Ferramentas:**

- `analyze_react_code` - Análise de código React existente
- `optimize_react_code` - Otimização automática com tendências 2025
- `analyze_react_prompt` - Análise de qualidade de prompts
- `optimize_react_prompt` - Otimização de prompts para AI tools (v0.dev, Cursor, etc.)
- `generate_react_workflow` - Geração de workflows de desenvolvimento
- `get_react_best_practices` - Melhores práticas React 2025
- `validate_react_integration` - Validação de integração de componentes

**Tendências UI/UX 2025 Suportadas:**

- 🪟 Glassmorphism e efeitos de vidro
- 🌙 Dark mode como padrão primário
- ✨ Micro-animações e interações
- 🎨 Typography bold e maximalista
- 🔗 Elementos 3D interativos
- ♿ Acessibilidade WCAG 2.1 AA

**Integração com AI Tools:**

- v0.dev (Vercel), Cursor AI, GitHub Copilot, Visual Copilot

📚 **Documentação**: `docs/servers/react_optimizer_server.md` | **Exemplos**: `docs/examples/react_optimizer_examples.py`

### 5. ✅ shadcn/ui Advanced Server (`shadcn_server.py`) - **FUNCIONAL** 🆕

Servidor MCP avançado para integração completa com shadcn/ui, oferecendo análise inteligente, geração otimizada e customização de componentes seguindo as melhores práticas da biblioteca.

**Principais Funcionalidades:**

- 🔍 **Análise Inteligente**: Detecta componentes shadcn/ui no código com análise de dependências
- ⚡ **Otimização Automática**: Aplica melhores práticas (React.memo, cn() utility, ARIA roles)
- 🎨 **Geração de Componentes**: Templates TypeScript otimizados para 10+ componentes
- 🌙 **Criação de Temas**: Gerador de temas personalizados com suporte a dark mode
- 📋 **Guias de Setup**: Configuração específica para Next.js, Vite, Remix, Astro

**Ferramentas:**

- `analyze_shadcn_component` - Análise de código com componentes shadcn/ui
- `optimize_shadcn_component` - Otimização automática com melhores práticas
- `generate_shadcn_component` - Geração de componentes customizados
- `get_shadcn_component_info` - Informações detalhadas sobre componentes
- `get_shadcn_setup_guide` - Guias de configuração por framework
- `create_shadcn_theme` - Criador de temas personalizados
- `get_shadcn_best_practices` - Padrões e práticas recomendadas

**Componentes Suportados:**

- 🧩 Layout: Accordion, Card, Dialog
- 📝 Forms: Button, Input, Select, Form (React Hook Form + Zod)
- 📊 Data Display: Table, Badge
- 🔔 Feedback: Toast, Alert Dialog
- 🎨 Advanced: Compound Components, Custom Hooks, TypeScript interfaces

**Frameworks Suportados:**

- Next.js, Vite, Remix, Astro, React Router

**Características Avançadas:**

- 🎯 **Base de Conhecimento**: Metadados completos de componentes e dependências
- 🔧 **Templates TypeScript**: Código otimizado com validação Zod e React Hook Form
- 📊 **Score de Acessibilidade**: Análise automática de conformidade WCAG
- 🚀 **Multi-Framework**: Configurações específicas para cada framework
- 🎨 **Theme Generator**: Conversão automática hex → HSL com CSS variables

📚 **Documentação**: Baseada na documentação oficial shadcn/ui e padrões React modernos

### 6. ✅ FastMCP Server (`fastmcp_server.py`) - **FUNCIONAL**

Servidor otimizado usando FastMCP para análise de prompts MCP com funcionalidades avançadas de análise e geração de templates.

**Ferramentas:**

- `analyze_mcp_prompt` - Análise avançada de prompts MCP com pontuação
- `suggest_mcp_prompt_improvements` - Sugestões de melhorias específicas
- `validate_mcp_requirements` - Validação completa de requisitos MCP
- `generate_mcp_server_template` - Geração de templates de servidores

**Recursos:**

- `mcp://best-practices` - Melhores práticas MCP atualizadas
- `mcp://prompt-examples/{level}` - Exemplos de prompts por nível
- `mcp://prompt-frameworks` - Frameworks de análise de prompts

### 7. ✅ React 19 Advanced Server (`react_server.py`) - **FUNCIONAL** 🆕

Servidor MCP avançado para desenvolvimento React 19 com funcionalidades modernas, incluindo Server Components, Actions e integração completa com frameworks modernos.

**Principais Funcionalidades:**

- ⚛️ **React 19 Features**: Server Components estáveis, Actions, hook `use`
- 🎯 **Análise de Prompts**: Avalia prompts React com pontuação e sugestões
- 🏗️ **Templates Modernos**: Templates otimizados para componentes e aplicações
- 🔧 **Validação de Requisitos**: Checklist completo para projetos React
- 📊 **Best Practices**: Conformidade com padrões React 2025

**Ferramentas:**

- `analisar_prompt_react` - Análise de prompts com pontuação e feedback
- `obter_template_prompt` - Templates otimizados para diferentes tipos de projeto
- `sugerir_melhorias_contextuais` - Melhorias específicas por contexto
- `validar_requisitos_react` - Validação de requisitos essenciais
- `gerar_prompt_otimizado` - Geração automática de prompts estruturados

**React 19 Features Suportadas:**

- 🚀 **Server Components**: Rendering no servidor com performance otimizada
- ⚡ **Actions**: Form handling automático com estados de pending
- 🎣 **Hook `use`**: Consumo de recursos assíncronos
- 🔄 **Ref as Prop**: Sem necessidade de forwardRef
- 📝 **Enhanced Forms**: Validação e handling avançados

**Frameworks Suportados:**

- Next.js 15+, Vite 6+, Remix 2.0+, Create React App

📚 **Documentação**: Baseada no React 19 (December 2024) e melhores práticas 2025

### 8. ✅ Rust Idiomatic Server (`rust_server.py`) - **FUNCIONAL** 🆕

Servidor MCP refatorado para seguir padrões idiomáticos Rust baseado no repositório `mre/idiomatic-rust` e diretrizes oficiais `rust-lang/api-guidelines`.

**Principais Funcionalidades:**

- 🦀 **Análise Idiomática**: Detecta padrões idiomáticos e anti-patterns
- 🔧 **Immutability by Default**: Análise de uso correto de `mut`
- 🛡️ **Error Handling Ergonômico**: Result/Option com thiserror/anyhow
- 🔄 **Type Conversions**: From/Into traits para conversões elegantes
- 🎯 **Enums over Booleans**: Detecção de boolean flags problemáticos
- ⚡ **Async Patterns**: Tokio e async/await idiomático
- 🏗️ **API Design**: Conformidade com rust-lang/api-guidelines

**Ferramentas Idiomáticas:**

- `analyze_idiomatic_rust` - Análise de idiomaticidade com scoring por categoria
- `generate_idiomatic_project` - Geração de projetos seguindo padrões idiomáticos
- `get_idiomatic_patterns` - Biblioteca completa de padrões com exemplos
- `refactor_to_idiomatic` - Refatoração automática para código idiomático
- `get_rust_api_guidelines` - Diretrizes oficiais organizadas por categoria

**Categorias de Análise:**

- 🔧 **Immutability**: "Aim for immutability by default" com análise de mut
- 🛡️ **Error Handling**: Result over panic, context preservation
- 🔄 **Type Conversions**: From/Into/TryFrom patterns ergonômicos
- 🎯 **Enums over Bools**: Expressividade através de enums
- ⚡ **Async Patterns**: async/await idiomático com Tokio
- 🏗️ **API Design**: snake_case, PascalCase, documentação
- 🚀 **Performance**: Zero-cost abstractions, iterator chains
- 📚 **Documentation**: Doc comments com exemplos testáveis

**Padrões Idiomáticos Implementados:**

- ✅ Variables imutáveis por padrão
- ✅ Result-based error handling com thiserror
- ✅ Builder pattern para configurações complexas
- ✅ Iterator chains para estilo funcional
- ✅ From/Into traits para type conversions
- ✅ Enums expressivos ao invés de booleans
- ✅ Comprehensive documentation com examples
- ✅ API guidelines compliance (naming, structure)

**Baseado em:**

- [mre/idiomatic-rust](https://github.com/mre/idiomatic-rust) - Padrões idiomáticos curados
- [rust-lang/api-guidelines](https://rust-lang.github.io/api-guidelines/) - Diretrizes oficiais
- [blessed.rs](https://blessed.rs/) - Ecosystem recommendations
- [cheats.rs](https://cheats.rs/) - Idiomatic Rust tips

📚 **Documentação**: Padrões idiomáticos Rust 2025 com scoring detalhado

### 9. 🚧 Servidores em Desenvolvimento

- **TypeScript Server** (`typescript_server.py`) - Em desenvolvimento

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
  - [API do FastMCP Server](docs/api/fastmcp_server_api.md)
  - [API do React 19 Server](docs/api/react_server_api.md)
  - [API do Rust Advanced Server](docs/api/rust_server_api.md)
- **Exemplos**:
  - [Exemplo Integrado](docs/examples/integrated_example.py)
  - [Exemplo do Analisador MCP](docs/examples/mcp_analyzer_example.py)
  - [Exemplos de Engenharia de Prompts](docs/examples/prompt_engineering_examples.py)
  - [Componentes Tailwind v4.1](docs/examples/tailwind_components.md)

## 📚 Documentação Completa

### 🚀 Guias de Início Rápido

- **[Tutorial Prático](docs/examples/tutorial_pratico.md)** - Guia passo a passo completo
- **[Exemplos Rápidos](docs/examples/exemplos_rapidos.md)** - Exemplos básicos para começar
- **[Demo Integrado](docs/examples/complete_integration_demo.py)** - Demonstração completa funcionando

### 📖 Documentação Detalhada por Servidor

- **[Servidor de Análise MCP](docs/examples/mcp_server_examples.md)** - Exemplos de análise de prompts
- **[Servidor de Engenharia de Prompts](docs/examples/prompt_server_examples.md)** - Otimização avançada
- **[Servidor Tailwind CSS v4.1](docs/examples/tailwind_server_examples.md)** - Componentes modernos
- **[FastMCP Server](docs/examples/fastmcp_server_examples.md)** - Geração de servidores
- **[React 19 Advanced Server](docs/examples/react_server_examples.md)** - Desenvolvimento React moderno
- **[Rust Advanced Server](docs/examples/rust_server_examples.md)** - Padrões Rust modernos

### 🔄 Workflows e Integração

- **[Workflows Integrados](docs/examples/integrated_workflows.md)** - Casos de uso completos
- **[Exemplos Avançados](docs/examples/exemplos_avancados.md)** - Casos empresariais
- **[Exemplos de Uso Geral](docs/examples/usage_examples.md)** - Visão geral e navegação

### 🛠️ Ferramentas e Utilitários

- **[CLI Unificada](mcp_cli.py)** - Interface de linha de comando para todos os servidores
- **[Scripts de Automação](run_servers.sh)** - Execução automatizada de servidores
- **[Testes](run_tests.py)** - Framework de testes completo

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

# Instalar dependências e criar ambiente virtual
uv sync

# Verificar instalação
python main.py --help
```

## 🚀 Uso Rápido

### Launcher Principal

O launcher centralizado permite executar todos os servidores de forma unificada:

```bash
# Executar servidor específico
python main.py mcp          # Analisador de prompts MCP
python main.py prompt       # Servidor de engenharia de prompts
python main.py tailwind     # Servidor Tailwind CSS
python main.py react_optimizer  # Servidor React Optimizer
python main.py shadcn        # Servidor shadcn/ui Advanced (NOVO!)

# Executar todos os servidores (modo desenvolvimento)
python main.py all

# Ajuda completa
python main.py --help
```

### Interface Interativa

```bash
# Interface com menu colorido (recomendado)
./run_servers.sh

# Execução direta com opções
bash run_servers.sh menu
bash run_servers.sh mcp
```

### Executar Testes

```bash
# Todos os testes (usando runner modernizado)
python run_tests.py

# Teste específico por módulo
python run_tests.py mcp_server
python run_tests.py prompt_server
python run_tests.py tailwind_server

# Usando pytest diretamente
uv run python -m pytest tests/ -v

# Com relatório detalhado
python run_tests.py --verbose
```

## ⚡ Início Rápido

### 🎯 Demo Integrado Completo

Execute nosso demo que mostra todos os servidores trabalhando juntos:

```bash
# Demo completo de integração
python docs/examples/complete_integration_demo.py
```

Este demo demonstra:

- ✅ Análise completa de prompts MCP
- ✅ Otimização com frameworks CRISPE/RACE/TRACE
- ✅ Criação de componentes Tailwind v4.1
- ✅ Geração automática de servidores MCP
- ✅ Workflow integrado end-to-end

### 🛠️ Interface de Linha de Comando (CLI)

Use nossa CLI unificada para interagir com todos os servidores:

```bash
# Ver todos os comandos disponíveis
python mcp_cli.py --help

# Análise rápida de prompt
python mcp_cli.py analyze "Criar servidor para e-commerce"

# Otimização com framework específico
python mcp_cli.py optimize "Prompt original" --framework CRISPE

# Criar componente Tailwind v4.1
python mcp_cli.py tailwind button '{"cor": "blue", "tamanho": "lg"}'

# Gerar servidor MCP completo
python mcp_cli.py fastmcp loja_server '["add_product", "process_order"]'

# Workflow integrado completo
python mcp_cli.py workflow "Sistema de Vendas"
```

### 📚 Tutorial Passo a Passo

Siga nosso tutorial prático detalhado:

```bash
# Abra o tutorial completo
cat docs/examples/tutorial_pratico.md
```

O tutorial inclui:

- 🎯 Exemplos práticos passo a passo
- 🔄 Workflows completos para diferentes cenários
- 🎨 Uso avançado do Tailwind CSS v4.1
- 🔧 Integração com Claude Desktop
- 📈 Métricas de performance e economia de tempo

## 📋 Exemplos de Uso

### Análise de Prompt MCP

```python
# Usando diretamente a biblioteca
from servers.mcp_server import AnalisadorPromptMCP

analisador = AnalisadorPromptMCP()
resultado = analisador.analisar_prompt(
    "Criar um servidor MCP para análise de código Python"
)

print(f"Pontuação: {resultado.pontuacao}/10")
print(f"Recomendações: {resultado.recomendacoes}")
```

### Execução via Launcher

```bash
# Interface interativa completa
./run_servers.sh

# Executar todos os servidores em desenvolvimento
python main.py all --dev

# Executar servidores específicos em paralelo
python main.py mcp prompt tailwind
```

## 🧪 Sistema de Testes v2.0

O projeto v2.0 inclui um sistema de testes modernizado com pytest:

```bash
# Status atual dos testes
✅ 11/15 testes passando
⏭️ 4 testes ignorados (servidores em desenvolvimento)
⚠️ 1 warning (pytest-asyncio não instalado)

# Executar todos os testes
python run_tests.py

# Testes específicos por módulo
python run_tests.py mcp_server      # ✅ 10/10 testes passando
python run_tests.py prompt_server   # ✅ 1/1 teste passando, 4 ignorados
python run_tests.py tailwind_server # 🚧 Em desenvolvimento

# Usando pytest diretamente
uv run python -m pytest tests/ -v

# Com cobertura (requer pytest-cov)
uv run python -m pytest tests/ --cov=servers --cov-report=term-missing
```

### Testes Incluídos

- ✅ **test_mcp_server.py** - Analisador de Prompts MCP (10 testes)
  - Inicialização do analisador
  - Análise de prompts (ruim, médio, bom)
  - Validação de campos e pontuação
  - Ferramentas MCP integradas
- ✅ **test_prompt_server.py** - Servidor de Engenharia de Prompts (1 teste)
  - Teste de fallback funcional
  - 4 testes ignorados (servidor em desenvolvimento)
- 🚧 **test_tailwind_server.py** - Servidor Tailwind CSS (em desenvolvimento)

## 📁 Estrutura do Projeto v2.0

```text
mcp-servers/
├── 🚀 main.py                  # Launcher principal unificado
├── 🔧 pyproject.toml           # Configuração do projeto (uv)
├── 🧪 run_tests.py             # Runner de testes modernizado
├── 📜 run_servers.sh           # Script de execução interativo
├── 📖 README.md                # Este arquivo
│
├── 🖥️ servers/                 # Servidores MCP
│   ├── ✅ mcp_server.py        # Analisador de prompts MCP (funcional)
│   ├── ✅ prompt_server.py     # Engenharia de prompts (funcional)
│   ├── ✅ tailwind_server.py   # Suporte Tailwind CSS v4.1 (funcional)
│   ├── ✅ react_optimizer_server.py # React Optimizer (funcional)
│   ├── ✅ shadcn_server.py     # shadcn/ui Advanced (funcional) 🆕
│   ├── ✅ fastmcp_server.py    # Servidor FastMCP (funcional)
│   ├── 🚧 react_server.py      # Servidor React (em desenvolvimento)
│   └── 🚧 typescript_server.py # Servidor TypeScript (em desenvolvimento)
│
├── 🧪 tests/                   # Testes com pytest (11/15 passando)
│   ├── ✅ test_mcp_server.py   # 10/10 testes do analisador MCP
│   ├── ✅ test_prompt_server.py # 1/1 teste do servidor de prompts
│   └── 🚧 test_tailwind_server.py # Testes do servidor Tailwind
│
└── 📚 docs/                    # Documentação completa
    ├── guides/                 # Guias de uso e instalação
    ├── api/                    # Referências de API
    ├── examples/               # Exemplos práticos
    └── servers/                # Documentação dos servidores
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

| Critério                   | Descrição                          | Importância |
| -------------------------- | ---------------------------------- | ----------- |
| 🎯 Propósito Claro         | Objetivo específico e bem definido | Alta        |
| 🛠️ Design de Ferramentas   | Ferramentas focadas e bem nomeadas | Alta        |
| ⚠️ Tratamento de Erros     | Validação e tratamento de exceções | Alta        |
| 📝 Documentação            | Descrição clara das ferramentas    | Média       |
| 🔒 Segurança               | Práticas recomendadas de segurança | Média       |
| 📋 Esquema de Dados        | Estruturas de dados bem definidas  | Média       |
| ⚡ Performance             | Considerações de otimização        | Baixa       |
| 🔧 Protocolo de Transporte | Especificação clara do protocolo   | Baixa       |

## 🧰 Ferramentas de Desenvolvimento

### Sistema de Build Moderno

- **uv**: Gerenciador de pacotes ultrarrápido
- **pyproject.toml**: Configuração centralizada
- **Hatchling**: Backend de build moderno

### Scripts de Automação

- 🚀 `main.py` - Launcher centralizado para todos os servidores
- 🔧 `run_servers.sh` - Interface interativa simplificada
- 🧪 `run_tests.py` - Runner de testes modernizado

## 🧰 Ferramentas de Desenvolvimento v2.0

### Sistema de Build Moderno

- **uv**: Gerenciador de pacotes Python ultrarrápido
- **pyproject.toml**: Configuração centralizada do projeto
- **Hatchling**: Backend de build moderno e eficiente

### Scripts de Automação

- 🚀 **main.py** - Launcher centralizado para todos os servidores
- 🔧 **run_servers.sh** - Interface interativa com menu colorido
- 🧪 **run_tests.py** - Runner de testes modernizado com relatórios

### Funcionalidades Avançadas

- ⚡ **Execução Assíncrona**: Suporte nativo a operações async/await
- 🔄 **Recarga Automática**: Hot reload em modo desenvolvimento
- 📊 **Relatórios de Teste**: Coverage e relatórios detalhados
- 🎨 **Interface Colorida**: Output colorizado para melhor UX
- 🛡️ **Tratamento de Sinais**: Parada limpa com Ctrl+C

## 📈 Status do Projeto

### ✅ Funcionalidades Implementadas

- **Servidores Core**: 8/9 servidores funcionais (mcp, prompt, tailwind, react_optimizer, shadcn, fastmcp, react, rust)
- **Sistema de Testes**: 11/15 testes passando (73% de sucesso)
- **Build System**: Migração completa para uv + pyproject.toml
- **Documentação**: README v2.0 e docs/ atualizados
- **Scripts**: Launcher unificado e interface interativa

### 🚧 Em Desenvolvimento

- **Servidores Adicionais**: React, TypeScript (2/8 servidores pendentes)
- **Testes Restantes**: 4 testes pendentes para novos servidores
- **Dependências**: pytest-asyncio e pytest-cov opcionais

### 🎯 Roadmap Próximas Versões

- [ ] **v2.1**: Implementar servidores React e TypeScript restantes
- [ ] **v2.2**: Adicionar suporte para análise de prompts em inglês
- [ ] **v2.3**: Criar API REST para acesso remoto aos servidores
- [ ] **v2.4**: Desenvolver interface web para visualização de resultados
- [ ] **v2.5**: Integrar novos modelos de avaliação de prompts

## 🤝 Como Contribuir

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto no GitHub
2. Crie uma branch para sua feature (`git checkout -b feature/nova-ferramenta`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova ferramenta de análise'`)
4. Push para a branch (`git push origin feature/nova-ferramenta`)
5. Abra um Pull Request

### Diretrizes de Contribuição

- Mantenha o código em português (comentários e documentação)
- Adicione testes para novas funcionalidades
- Siga as convenções de nomenclatura existentes
- Atualize a documentação conforme necessário

## 📜 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo `LICENSE` para detalhes.

## 🙏 Agradecimentos

- [FastMCP](https://github.com/fastmcp/fastmcp) - Framework para desenvolvimento de servidores MCP
- [Pydantic](https://docs.pydantic.dev/) - Validação de dados e esquemas
- [uv](https://github.com/astral-sh/uv) - Gerenciador de pacotes Python ultrarrápido
- [Pytest](https://docs.pytest.org/) - Framework de testes moderno

---

**🚀 MCP Servers v2.0** | **Versão**: 2.0 | **Python**: 3.12+ | **Status**: Produção

_Desenvolvido com ❤️ pela Comunidade MCP Brasil_
