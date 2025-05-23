# Servidor Analisador de Prompts MCP

Um servidor MCP (Model Context Protocol) que analisa prompts para criação de servidores MCP, fornecendo feedback e recomendações baseadas nas melhores práticas da documentação oficial do MCP.

## Visão Geral

Este servidor ajuda desenvolvedores a criar melhores servidores MCP analisando seus prompts de criação e fornecendo feedback detalhado sobre:

- **Pontuação de qualidade** (escala 1-10)
- **Alinhamento com melhores práticas**
- **Identificação de pontos fortes e fracos**
- **Recomendações específicas para melhoria**
- **Detecção de elementos ausentes**

## Funcionalidades

### Ferramentas Disponíveis

1. **`analisar_prompt_mcp`** - Análise abrangente de prompts de criação de servidor MCP
2. **`obter_melhores_praticas_mcp`** - Recuperar melhores práticas de desenvolvimento MCP
3. **`sugerir_melhorias_prompt`** - Obter sugestões específicas para melhorar prompts
4. **`validar_requisitos_mcp`** - Validar requisitos contra lista de verificação de melhores práticas

### Critérios de Análise

O analisador avalia prompts baseado nas principais melhores práticas do MCP:

- ✅ **Propósito Claro** - Objetivos específicos e bem definidos do servidor
- ✅ **Design de Ferramentas** - Ferramentas focadas e documentadas com nomenclatura adequada
- ✅ **Tratamento de Erros** - Tratamento abrangente de erros e validação
- ✅ **Segurança** - Validação de entrada, sanitização e medidas de segurança
- ✅ **Definições de Schema** - Schemas de dados claros e definições de tipos
- ✅ **Documentação** - Documentação clara e exemplos de uso
- ✅ **Estratégia de Testes** - Considerações de teste e depuração
- ✅ **Performance** - Considerações de performance e escalabilidade
- ✅ **Protocolo de Transporte** - Seleção adequada de protocolo (stdio, HTTP+SSE)
- ✅ **Gerenciamento de Recursos** - Tratamento adequado de recursos e limpeza

## Instalação

1. Instalar dependências:

```bash
pip install -r requirements.txt
```

2. Executar o servidor:

```bash
python servers/mcp_server.py
```

## Exemplos de Uso

### Exemplo 1: Analisando um Prompt Básico

**Prompt de Entrada:**

```
"Criar um servidor MCP para operações de arquivo"
```

**Resultado da Análise:**

- Pontuação: 3/10
- Ausentes: Tratamento de erros, segurança, schemas, documentação, testes
- Recomendações: Definir ferramentas específicas, incluir validação, adicionar medidas de segurança

### Exemplo 2: Analisando um Prompt Abrangente

**Prompt de Entrada:**

```
"Criar um servidor MCP para operações de arquivo com ferramentas para ler, escrever e listar arquivos. Incluir tratamento abrangente de erros, validação de entrada, medidas de segurança, schemas claros, documentação com exemplos, estratégia de teste e usar protocolo de transporte stdio."
```

**Resultado da Análise:**

- Pontuação: 9/10
- Pontos fortes: Propósito claro, requisitos abrangentes, foco em segurança
- Melhorias menores: Considerações de performance, limpeza de recursos

## Referência da API

### analisar_prompt_mcp(prompt: str) -> AnalisePrompt

Analisa um prompt de criação de servidor MCP e retorna feedback abrangente.

**Parâmetros:**

- `prompt` (str): O texto do prompt para analisar

**Retorna:**

- `AnalisePrompt`: Objeto contendo:
  - `pontuacao` (int): Pontuação de qualidade 1-10
  - `pontos_fortes` (List[str]): Pontos fortes identificados
  - `pontos_fracos` (List[str]): Áreas para melhoria
  - `recomendacoes` (List[str]): Recomendações específicas
  - `alinhamento_melhores_praticas` (Dict[str, bool]): Lista de verificação de melhores práticas
  - `elementos_ausentes` (List[str]): Elementos importantes ausentes

### obter_melhores_praticas_mcp() -> Dict[str, str]

Retorna um resumo das melhores práticas de desenvolvimento de servidor MCP.

### sugerir_melhorias_prompt(prompt_original: str) -> Dict[str, Any]

Fornece sugestões específicas para melhorar um prompt de criação de servidor MCP.

### validar_requisitos_mcp(requisitos: str) -> Dict[str, Any]

Valida requisitos contra lista de verificação de melhores práticas do MCP.

## Testes

Execute a suíte de testes para validar a funcionalidade:

```bash
python test_mcp_server.py
```

A suíte de testes inclui:

- Análise de prompt ruim (pontuação esperada: 1-4)
- Análise de prompt médio (pontuação esperada: 4-7)
- Análise de prompt bom (pontuação esperada: 7-10)
- Validação de melhores práticas

## Desenvolvimento

### Arquitetura

O servidor é construído usando:

- **FastMCP**: Framework Python moderno para MCP
- **Pydantic**: Validação e serialização de dados
- **Expressões Regulares**: Correspondência de padrões para análise
- **Mecanismo de Análise Abrangente**: Sistema de avaliação multi-critérios

### Componentes Principais

1. **AnalisadorPromptMCP**: Mecanismo principal de análise
2. **AnalisePrompt**: Modelo de dados para resultados de análise
3. **Base de Melhores Práticas**: Critérios abrangentes da documentação MCP
4. **Correspondência de Padrões**: Análise de conteúdo baseada em regex
5. **Algoritmo de Pontuação**: Sistema de pontuação multi-fator

### Estendendo o Analisador

Para adicionar novos critérios de análise:

1. Atualizar dicionário `melhores_praticas` em `AnalisadorPromptMCP`
2. Adicionar lógica de detecção no método `_analisar_melhores_praticas`
3. Atualizar correspondência de padrões em `padroes_positivos` ou `padroes_negativos`
4. Adicionar recomendações correspondentes em `_gerar_recomendacoes`

## Melhores Práticas para Prompts de Servidor MCP

Baseado na documentação oficial do MCP, bons prompts devem incluir:

### 1. Declaração de Propósito Clara

```
"Criar um servidor MCP que [objetivo específico] para [caso de uso específico]"
```

### 2. Definições Específicas de Ferramentas

```
"Ferramentas necessárias:
- nome_ferramenta: Descrição da funcionalidade
- Parâmetros: Especificações claras de entrada/saída"
```

### 3. Requisitos Técnicos

```
"Requisitos:
- Tratamento de erros para [cenários específicos]
- Validação de entrada para [entradas específicas]
- Medidas de segurança incluindo [proteções específicas]"
```

### 4. Detalhes de Implementação

```
"Implementação:
- Usar [protocolo de transporte] para comunicação
- Definir schemas para [tipos de dados]
- Incluir [abordagem de teste]"
```

### 5. Documentação e Exemplos

```
"Documentação:
- Exemplos de uso para cada ferramenta
- Guia de integração
- Exemplos de tratamento de erros"
```

## Contribuindo

1. Faça um fork do repositório
2. Crie um branch de funcionalidade
3. Adicione testes para nova funcionalidade
4. Certifique-se de que todos os testes passem
5. Envie um pull request

## Licença

Este projeto segue a mesma licença da especificação MCP e ferramentas relacionadas.

## Referências

- [Documentação do Model Context Protocol](https://modelcontextprotocol.io/)
- [Guia de Construção MCP](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
- [Especificação Completa MCP](https://modelcontextprotocol.io/llms-full.txt)
- [Framework FastMCP](https://github.com/jlowin/fastmcp)
