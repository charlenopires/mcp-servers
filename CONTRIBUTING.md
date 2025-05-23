# Guia de Contribuição

## 👋 Bem-vindo!

Obrigado pelo interesse em contribuir para o projeto MCP Servers! Este documento fornece diretrizes para contribuir de forma eficiente.

## 🚀 Como Contribuir

### 1. Encontrando Problemas para Trabalhar

- Veja os [Issues abertos](https://github.com/user/mcp-servers/issues) no GitHub
- Procure issues com a etiqueta `good first issue` se for sua primeira contribuição
- Verifique o [Roadmap](https://github.com/user/mcp-servers/projects) para ver áreas em desenvolvimento

### 2. Configurando o Ambiente

1. Faça um fork do repositório para sua conta GitHub
2. Clone o fork para seu ambiente local:

```bash
git clone https://github.com/SEU_USUARIO/mcp-servers.git
cd mcp-servers
```

3. Adicione o repositório original como remote:

```bash
git remote add upstream https://github.com/user/mcp-servers.git
```

4. Instale as dependências de desenvolvimento:

```bash
pip install -r requirements-dev.txt
```

5. Configure os hooks de pre-commit:

```bash
pre-commit install
```

### 3. Criando uma Branch

Crie uma branch a partir da `main` para sua contribuição:

```bash
git checkout -b feature/nome-da-sua-feature
# ou
git checkout -b fix/nome-do-bug
```

### 4. Fazendo Alterações

Ao fazer alterações, siga estas diretrizes:

1. **Estilo de Código**: Siga PEP 8 e as convenções do projeto
2. **Documentação**: Atualize a documentação relacionada às suas mudanças
3. **Testes**: Adicione testes para novas funcionalidades ou correções
4. **Commits**: Use mensagens de commit descritivas e no formato apropriado

```bash
# Exemplo de mensagem de commit
git commit -m "feat: adiciona novo método de análise de tokens no Analisador MCP"
```

5. **Importações**: Organize as importações usando `isort`
6. **Formatação**: Use `black` para formatar seu código

```bash
# Formatar código
black .
isort .
```

### 5. Testando suas Alterações

Execute os testes para garantir que tudo está funcionando corretamente:

```bash
# Executar todos os testes
python run_tests.py

# Ou executar testes específicos
pytest tests/test_mcp_server.py
```

Verifique também a cobertura de testes:

```bash
pytest --cov=servers tests/
```

### 6. Enviando um Pull Request

1. Atualize sua branch com as alterações mais recentes da `main`:

```bash
git fetch upstream
git rebase upstream/main
```

2. Resolva quaisquer conflitos de merge
3. Faça push da sua branch para o GitHub:

```bash
git push origin feature/nome-da-sua-feature
```

4. Abra um Pull Request no GitHub
5. Preencha o template de Pull Request com todas as informações necessárias
6. Aguarde a revisão dos mantenedores

## 📋 Padrões de Código

### Convenções de Nomenclatura

- **Arquivos**: Nomes em `snake_case`
- **Classes**: Nomes em `PascalCase`
- **Funções e Métodos**: Nomes em `snake_case`
- **Constantes**: Nomes em `UPPER_SNAKE_CASE`
- **Variáveis**: Nomes em `snake_case`

### Docstrings

Use docstrings no formato Google para documentar classes e funções:

```python
def analisar_prompt(self, prompt: str) -> Dict[str, Any]:
    """
    Analisa um prompt para criação de servidor MCP.

    Args:
        prompt: O texto do prompt a ser analisado

    Returns:
        Dict contendo resultado da análise com pontuação, pontos fortes, fracos, etc.

    Raises:
        ValueError: Se o prompt estiver vazio ou for inválido
    """
```

### Imports

Organize os imports na seguinte ordem:

1. Bibliotecas padrão do Python
2. Bibliotecas de terceiros
3. Imports locais (dentro do projeto)

Exemplo:

```python
# Bibliotecas padrão
import os
import sys
from typing import Dict, List

# Bibliotecas de terceiros
import pydantic
from fastmcp import MCPServer

# Imports locais
from servers.utils import tokenizer
from servers.models import AnaliseResult
```

## 🧪 Testes

### Escrevendo Testes

- Use o `pytest` para escrever e executar testes
- Nomeie os arquivos de teste com o prefixo `test_`
- Tente alcançar pelo menos 80% de cobertura de código
- Escreva testes para caminhos felizes e casos de erro

### Exemplo de Teste

```python
import pytest
from servers.mcp_server import AnalisadorPromptMCP

def test_analisar_prompt_valido():
    """Testa se a análise de um prompt válido retorna resultados corretos."""
    analisador = AnalisadorPromptMCP()
    resultado = analisador.analisar_prompt(
        "Crie um servidor MCP para processamento de arquivos com tratamento de erros."
    )

    assert isinstance(resultado, dict)
    assert "pontuacao" in resultado
    assert 1 <= resultado["pontuacao"] <= 10
    assert len(resultado["pontos_fortes"]) > 0

def test_analisar_prompt_vazio():
    """Testa se a análise de um prompt vazio lança exceção."""
    analisador = AnalisadorPromptMCP()

    with pytest.raises(ValueError):
        analisador.analisar_prompt("")
```

## 📚 Documentação

### Atualizando a Documentação

Se suas alterações afetarem a documentação, certifique-se de:

1. Atualizar os arquivos relevantes em `/docs`
2. Atualizar docstrings no código
3. Adicionar exemplos de uso quando relevante
4. Atualizar o README.md se necessário

### Exemplos

Sempre que implementar uma nova funcionalidade, adicione exemplos de uso em:

- Docstrings
- Arquivos de exemplo em `/docs/examples`
- Guias específicos em `/docs/guides` se apropriado

## ⚙️ Tipos de Contribuições

### 1. Correções de Bugs

Para correções de bugs:

- Descreva claramente o bug em seu PR
- Adicione testes que reproduzem o bug
- Explique sua solução

### 2. Novas Funcionalidades

Para novas funcionalidades:

- Discuta a funcionalidade em uma issue antes de implementar
- Documente completamente a funcionalidade
- Adicione testes abrangentes
- Atualize a documentação relevante

### 3. Melhorias de Documentação

Para melhorias na documentação:

- Verifique ortografia e gramática
- Garanta que exemplos estejam atualizados
- Siga a formatação e estilo existentes

### 4. Refatoração de Código

Para refatorações:

- Mantenha a compatibilidade da API
- Não misture refatorações com novas funcionalidades
- Explique os benefícios da refatoração

## 🎯 Processo de Review

### O que Esperamos

- Os revisores responderão dentro de uma semana
- Se houver feedback, faça as alterações solicitadas
- Seja receptivo ao feedback e mantenha uma comunicação positiva
- Aguarde a aprovação de pelo menos um mantenedor

### Checklist de PR

Antes de enviar seu PR, verifique:

- [ ] Os testes estão passando
- [ ] O código segue os padrões de estilo
- [ ] A documentação foi atualizada
- [ ] Os commits estão organizados e descritivos
- [ ] O código foi testado localmente

## 🙏 Código de Conduta

Ao contribuir para este projeto, você concorda em seguir nosso [Código de Conduta](CODE_OF_CONDUCT.md). Resumidamente:

- Seja respeitoso e inclusivo
- Aceite feedback construtivo
- Foque no que é melhor para a comunidade
- Demonstre empatia com outros membros da comunidade

## 🎉 Agradecimentos

Suas contribuições são muito valiosas! A cada contribuição, você será adicionado à lista de colaboradores no arquivo README.md.

---

**Desenvolvido para o projeto MCP Servers**
