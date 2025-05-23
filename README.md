# 🚀 MCP Servers - Conjunto de Servidores MCP em Português

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![FastMCP](https://img.shields.io/badge/FastMCP-0.6.0%2B-green)](https://python.langchain.com/)
[![Licença](https://img.shields.io/badge/Licença-MIT-orange)](LICENSE)

Plataforma de servidores MCP (Model Context Protocol) em português para processamento especializado de prompts, incluindo análise de prompts MCP, engenharia de prompts e suporte para Tailwind CSS v4.1.

![Banner MCP Servers](https://github.com/user/mcp-servers/raw/main/docs/banner.png)

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
- **Arquitetura**:
  - [Visão Geral da Arquitetura](docs/architecture.md)
  - [Perguntas Frequentes (FAQ)](docs/faq.md)
- **Exemplos**:
  - [Exemplo Integrado](docs/examples/integrated_example.py)
  - [Exemplo do Analisador MCP](docs/examples/mcp_analyzer_example.py)

## 🛠️ Instalação

### Pré-requisitos

- Python 3.8+
- uv (Universal Python Package Manager)

### Configuração Rápida

```bash
# Clonar o repositório
git clone https://github.com/user/mcp-servers.git
cd mcp-servers

# Instalar dependências
pip install -r requirements.txt

# Ou usando uv
uv pip install -r requirements.txt
```

## 🚀 Uso

### Executar Servidores Individualmente

```bash
# Analisador de Prompts MCP
uv run --directory ./servers mcp_server.py

# Servidor de Engenharia de Prompts
uv run --directory ./servers prompt_server.py

# Servidor Tailwind CSS v4.1
uv run --directory ./servers tailwind_server.py
```

### Executar Múltiplos Servidores (Modo Interativo)

Utilizando o script launcher interativo:

```bash
./run_servers.sh
```

Interface colorida com seleção interativa e controle em tempo real.

### Modo Rápido (Inicialização Simplificada)

```bash
./start_servers.sh
# Digite os números dos servidores (ex: 1 3) ou "all" para todos
```

### Exemplo de Uso em Python

```python
from servers.mcp_server import AnalisadorPromptMCP

# Inicializar analisador
analisador = AnalisadorPromptMCP()

# Analisar um prompt
resultado = analisador.analisar_prompt(
    "Crie um servidor MCP com ferramentas para otimização de prompts,
     incluindo tratamento de erros e validação de entradas."
)

# Exibir resultado
print(f"Pontuação: {resultado.pontuacao}/10")
print(f"Pontos fortes: {resultado.pontos_fortes}")
print(f"Sugestões: {resultado.sugestoes}")
```

Para exemplos mais detalhados, consulte `exemplo_uso.py`.

## 🧪 Testes

Execute todos os testes com:

```bash
# Usando pytest diretamente
pytest ./tests

# Ou usando o script de testes
python run_tests.py
```

## 📁 Estrutura do Projeto

```
/mcp-servers/
├── 🖥️ servers/
│   ├── mcp_server.py           # Analisador de Prompts MCP
│   ├── prompt_server.py        # Servidor de Engenharia de Prompts
│   ├── tailwind_server.py      # Servidor Tailwind CSS v4.1
│   └── mcpprompt_server.py     # Servidor MCP Prompt (experimental)
│
├── 🧪 tests/
│   ├── __init__.py             # Módulo de testes
│   ├── test_mcp_server.py      # Teste do analisador
│   ├── test_prompt_server.py   # Teste do servidor de prompts
│   ├── test_tailwind_server.py # Teste do servidor Tailwind
│   └── test_mcpprompt_server.py # Teste do servidor experimental
│
├── 📜 run_servers.sh           # Launcher interativo completo
├── 📜 start_servers.sh         # Inicializador simples
├── 📜 run_tests.py             # Executor de testes
│
├── 📚 MCP_ANALYZER_README.md   # Documentação do analisador
├── 📚 LAUNCHER_README.md       # Documentação dos launchers
├── 📚 PROJETO_ESTRUTURA.md     # Estrutura completa do projeto
│
├── 📋 requirements.txt         # Dependências Python
├── 📋 pyproject.toml           # Configuração do projeto
├── 📋 exemplo_uso.py           # Exemplo de uso dos servidores
└── 📋 README.md                # Este arquivo
```

## 🌐 Protocolo MCP (Model Context Protocol)

O MCP é um protocolo que permite estender modelos de linguagem com ferramentas personalizadas. Cada servidor neste projeto implementa ferramentas MCP específicas para diferentes domínios de processamento de prompts.

### Princípios de Design MCP

1. **Design Focado**: Cada ferramenta realiza uma função específica e bem definida
2. **Tratamento Abrangente de Erros**: Validação robusta de entradas e saídas
3. **Documentação Clara**: Cada ferramenta tem documentação detalhada
4. **Entradas/Saídas Estruturadas**: Uso de Pydantic para validação de esquema

## 📊 Benchmarks e Pontuação

O Analisador de Prompts MCP avalia prompts em 10 critérios, cada um contribuindo para uma pontuação total (1-10):

| Critério              | Descrição                          | Peso |
| --------------------- | ---------------------------------- | ---- |
| Propósito Claro       | Objetivo específico do servidor    | 15%  |
| Design de Ferramentas | Ferramentas focadas e bem nomeadas | 15%  |
| Tratamento de Erros   | Validação e tratamento de exceções | 12%  |
| Documentação          | Descrição clara das ferramentas    | 10%  |
| Segurança             | Práticas recomendadas de segurança | 10%  |
| Esquema de Dados      | Estruturas de dados bem definidas  | 10%  |
| Eficiência            | Otimizações e desempenho           | 8%   |
| Extensibilidade       | Facilidade de extensão             | 8%   |
| Convenções MCP        | Alinhamento com padrões MCP        | 7%   |
| Testes                | Cobertura de testes robusta        | 5%   |

## 🧰 Scripts e Ferramentas

### Script de Execução Completo (`run_servers.sh`)

Launcher interativo com:

- Interface colorida e visual
- Menu de controle em tempo real
- Monitoramento de status
- Reinicialização individual ou em lote
- Parada gracosa de servidores

### Inicializador Rápido (`start_servers.sh`)

Versão simplificada para inicialização rápida:

- Mínima interação necessária
- Execução paralela automática
- Tratamento de sinais para parada limpa

Para documentação completa sobre os scripts, consulte `LAUNCHER_README.md`.

## 📈 Roadmap

- [ ] Adicionar suporte para análise de prompts em inglês
- [ ] Integrar novos modelos de avaliação de prompts
- [ ] Expandir conjunto de testes com casos mais complexos
- [ ] Criar API REST para acesso remoto aos servidores
- [ ] Desenvolver interface web para visualização de resultados
- [ ] Adicionar benchmark comparativo entre estratégias de prompts

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-ferramenta`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova ferramenta de análise'`)
4. Push para a branch (`git push origin feature/nova-ferramenta`)
5. Abra um Pull Request

Consulte `CONTRIBUTING.md` para mais detalhes sobre o processo de contribuição.

## 📜 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo `LICENSE` para detalhes.

## 🙏 Agradecimentos

- [FastMCP](https://github.com/fastmcp/fastmcp) - Framework para desenvolvimento de servidores MCP
- [Pydantic](https://docs.pydantic.dev/) - Validação de dados
- [uv](https://github.com/astral-sh/uv) - Gerenciador de pacotes Python

---

Desenvolvido com ❤️ por [Seu Nome/Equipe]
