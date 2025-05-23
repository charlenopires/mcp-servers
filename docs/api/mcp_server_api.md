# API do Analisador de Prompts MCP

Este documento descreve a API completa do servidor Analisador de Prompts MCP, incluindo detalhes sobre todas as classes, funções e parâmetros disponíveis.

## Classe Principal: `AnalisadorPromptMCP`

```python
class AnalisadorPromptMCP:
    """
    Analisador para prompts de criação de servidores MCP.
    Avalia a qualidade dos prompts e fornece feedback e sugestões de melhoria.
    """
```

### Inicialização

```python
def __init__(self):
    """
    Inicializa o analisador de prompts MCP com critérios e padrões predefinidos.
    """
```

### Modelos

```python
class AnalisePrompt(BaseModel):
    """Resultado da análise de um prompt MCP."""

    prompt: str = Field(..., description="O prompt analisado")
    pontuacao: float = Field(..., description="Pontuação geral (1-10)")
    pontos_fortes: List[str] = Field(default_factory=list, description="Pontos fortes identificados")
    pontos_fracos: List[str] = Field(default_factory=list, description="Pontos fracos identificados")
    sugestoes: List[str] = Field(default_factory=list, description="Sugestões para melhorias")
    criterios_avaliados: Dict[str, float] = Field(default_factory=dict, description="Pontuações por critério")
    analise_detalhada: str = Field("", description="Análise textual detalhada")
```

## Métodos Públicos

### `analisar_prompt`

```python
def analisar_prompt(self, prompt: str) -> AnalisePrompt:
    """
    Analisa um prompt de criação de servidor MCP e retorna uma avaliação detalhada.

    Args:
        prompt (str): O texto do prompt a ser analisado

    Returns:
        AnalisePrompt: Objeto contendo a análise detalhada
    """
```

### `obter_melhores_praticas_mcp`

```python
def obter_melhores_praticas_mcp(self, categoria: Optional[str] = None) -> Dict[str, Any]:
    """
    Obtém informações sobre melhores práticas para desenvolvimento de servidores MCP.

    Args:
        categoria (str, opcional): Categoria específica de melhores práticas
                                  (design, erros, segurança, etc.)

    Returns:
        Dict[str, Any]: Dicionário com práticas, exemplos e referências
    """
```

### `sugerir_melhorias_prompt`

```python
def sugerir_melhorias_prompt(self, prompt: str, foco: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Sugere melhorias específicas para um prompt MCP.

    Args:
        prompt (str): O texto do prompt a ser melhorado
        foco (List[str], opcional): Aspectos específicos a priorizar nas sugestões

    Returns:
        Dict[str, Any]: Dicionário com prompt melhorado, alterações e explicações
    """
```

### `validar_requisitos_mcp`

```python
def validar_requisitos_mcp(self, prompt: str, nivel_rigor: str = "intermediário") -> Dict[str, Any]:
    """
    Valida um prompt contra uma lista de verificação de requisitos para servidores MCP.

    Args:
        prompt (str): O texto do prompt a ser validado
        nivel_rigor (str, opcional): Nível de rigor da validação
                                     (básico, intermediário, avançado)

    Returns:
        Dict[str, Any]: Dicionário com requisitos atendidos, faltantes e conformidade
    """
```

## Métodos Internos

### `_avaliar_criterio`

```python
def _avaliar_criterio(self, prompt: str, criterio: str) -> float:
    """
    Avalia um critério específico para o prompt.

    Args:
        prompt (str): O texto do prompt
        criterio (str): O critério a ser avaliado

    Returns:
        float: Pontuação para o critério (0-10)
    """
```

### `_calcular_pontuacao_final`

```python
def _calcular_pontuacao_final(self, criterios_avaliados: Dict[str, float]) -> float:
    """
    Calcula a pontuação final baseada nos critérios avaliados.

    Args:
        criterios_avaliados (Dict[str, float]): Dicionário com pontuações por critério

    Returns:
        float: Pontuação final (1-10)
    """
```

### `_identificar_pontos_fortes_fracos`

```python
def _identificar_pontos_fortes_fracos(self, criterios_avaliados: Dict[str, float]) -> Tuple[List[str], List[str]]:
    """
    Identifica pontos fortes e fracos com base nas pontuações dos critérios.

    Args:
        criterios_avaliados (Dict[str, float]): Dicionário com pontuações por critério

    Returns:
        Tuple[List[str], List[str]]: Tupla contendo (pontos_fortes, pontos_fracos)
    """
```

### `_gerar_sugestoes`

```python
def _gerar_sugestoes(self, pontos_fracos: List[str], prompt: str) -> List[str]:
    """
    Gera sugestões específicas para melhorar o prompt com base nos pontos fracos.

    Args:
        pontos_fracos (List[str]): Lista de pontos fracos identificados
        prompt (str): O texto original do prompt

    Returns:
        List[str]: Lista de sugestões para melhorias
    """
```

## Ferramentas MCP

### `analisar_prompt_mcp`

```python
@mcp.tool("Analisa a qualidade de um prompt para criação de servidor MCP.", schema=types.analisar_prompt)
def analisar_prompt_mcp(prompt: str) -> Dict[str, Any]:
    """
    Analisa um prompt para criação de servidor MCP, fornecendo pontuação e feedback.

    Args:
        prompt (str): O texto do prompt a ser analisado

    Returns:
        Dict[str, Any]: Resultado da análise contendo pontuação, pontos fortes/fracos,
                        sugestões, critérios avaliados e análise detalhada
    """
```

### `obter_melhores_praticas_mcp`

```python
@mcp.tool("Obtém melhores práticas para criação de servidores MCP.", schema=types.obter_melhores_praticas)
def obter_melhores_praticas_mcp(categoria: Optional[str] = None) -> Dict[str, Any]:
    """
    Fornece informações sobre melhores práticas para desenvolvimento de servidores MCP.

    Args:
        categoria (str, opcional): Categoria específica de melhores práticas
                                  (design, erros, segurança, etc.)

    Returns:
        Dict[str, Any]: Informações sobre melhores práticas, incluindo descrições,
                        exemplos e referências
    """
```

### `sugerir_melhorias_prompt`

```python
@mcp.tool("Sugere melhorias para um prompt de criação de servidor MCP.", schema=types.sugerir_melhorias)
def sugerir_melhorias_prompt(prompt: str, foco: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Sugere melhorias específicas para um prompt de criação de servidor MCP.

    Args:
        prompt (str): O texto do prompt a ser melhorado
        foco (List[str], opcional): Aspectos específicos a priorizar nas sugestões

    Returns:
        Dict[str, Any]: Sugestões de melhorias, incluindo versão aprimorada
                        do prompt e explicações
    """
```

### `validar_requisitos_mcp`

```python
@mcp.tool("Valida um prompt contra requisitos de boas práticas MCP.", schema=types.validar_requisitos)
def validar_requisitos_mcp(prompt: str, nivel_rigor: str = "intermediário") -> Dict[str, Any]:
    """
    Valida um prompt contra uma lista de verificação de requisitos para servidores MCP.

    Args:
        prompt (str): O texto do prompt a ser validado
        nivel_rigor (str, opcional): Nível de rigor da validação
                                     (básico, intermediário, avançado)

    Returns:
        Dict[str, Any]: Resultado da validação, incluindo requisitos
                        atendidos, faltantes e percentual de conformidade
    """
```

## Constantes e Configurações

### `CRITERIOS_AVALIACAO`

```python
CRITERIOS_AVALIACAO = {
    "proposito_claro": {
        "descricao": "O prompt define claramente o propósito e objetivos do servidor MCP",
        "peso": 0.15,
        "padroes_positivos": [
            r"servidor\s+(?:para|que|com)\s+(?:\w+\s+){1,3}(?:de|da|do)\s+\w+",
            r"(?:criar|desenvolver|implementar)\s+(?:um\s+)?servidor\s+(?:para|que|com)\s+\w+",
            # Outros padrões positivos...
        ],
        "padroes_negativos": [
            r"^(?:fazer|criar)\s+(?:um\s+)?servidor\s*$",
            r"^servidor\s+mcp\s*$",
            # Outros padrões negativos...
        ]
    },
    # Outros critérios...
}
```

### `MELHORES_PRATICAS`

```python
MELHORES_PRATICAS = {
    "design_ferramentas": {
        "praticas": [
            {
                "titulo": "Uma ferramenta, uma função",
                "descricao": "Cada ferramenta deve realizar uma única função específica e bem definida",
                "importancia": "alta"
            },
            # Outras práticas...
        ],
        "exemplos": {
            "bom": [
                "📝 Exemplo de boa ferramenta: `converter_temperatura(valor: float, de: str, para: str) -> float`",
                # Outros exemplos...
            ],
            "ruim": [
                "⚠️ Exemplo de ferramenta problemática: `utils(acao: str, params: Dict) -> Any`",
                # Outros exemplos...
            ]
        },
        "referencias": [
            "Documentação oficial MCP - Seção 3.2: Design de Ferramentas",
            # Outras referências...
        ]
    },
    # Outras categorias...
}
```

## Tipos e Esquemas

```python
class Types:
    """Definição dos esquemas para as ferramentas MCP."""

    analisar_prompt = {
        "parameters": {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "O texto do prompt a ser analisado."
                }
            },
            "required": ["prompt"]
        },
        "returns": {
            "type": "object",
            "properties": {
                "pontuacao": {
                    "type": "number",
                    "description": "Pontuação geral de 1 a 10."
                },
                "pontos_fortes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Lista de pontos fortes identificados."
                },
                "pontos_fracos": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Lista de pontos fracos identificados."
                },
                "sugestoes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Sugestões específicas para melhorias."
                },
                "criterios_avaliados": {
                    "type": "object",
                    "description": "Pontuação detalhada por critério."
                },
                "analise_detalhada": {
                    "type": "string",
                    "description": "Análise textual detalhada."
                }
            },
            "required": ["pontuacao", "pontos_fortes", "pontos_fracos", "sugestoes"]
        }
    }

    # Outros esquemas...
```

## Códigos de Status e Respostas

| Status         | Código | Descrição                                   |
| -------------- | ------ | ------------------------------------------- |
| SUCESSO        | 200    | Análise concluída com sucesso               |
| ERRO_VALIDACAO | 400    | Erro de validação nos parâmetros de entrada |
| ERRO_SERVIDOR  | 500    | Erro interno ao processar a análise         |

## Exemplos de Uso

### Exemplo 1: Análise Básica

```python
from servers.mcp_server import AnalisadorPromptMCP

analisador = AnalisadorPromptMCP()
resultado = analisador.analisar_prompt("Crie um servidor MCP para gerenciar arquivos")

print(f"Pontuação: {resultado.pontuacao}/10")
print(f"Pontos fortes: {resultado.pontos_fortes}")
print(f"Pontos fracos: {resultado.pontos_fracos}")
print(f"Sugestões: {resultado.sugestoes}")
```

### Exemplo 2: Obter Melhores Práticas

```python
melhores_praticas = analisador.obter_melhores_praticas_mcp(categoria="tratamento_erros")

for pratica in melhores_praticas["praticas"]:
    print(f"- {pratica['titulo']}: {pratica['descricao']}")

print("\nExemplos:")
for exemplo in melhores_praticas["exemplos"]["bom"]:
    print(f"  ✅ {exemplo}")
```

### Exemplo 3: Validar Requisitos

```python
prompt = """
Crie um servidor MCP para processamento de imagens com as seguintes ferramentas:
1. redimensionar_imagem(arquivo: str, largura: int, altura: int) -> str
2. aplicar_filtro(arquivo: str, filtro: str) -> str
3. converter_formato(arquivo: str, formato: str) -> str

Cada ferramenta deve validar os parâmetros de entrada e tratar erros como
arquivos não encontrados ou formatos inválidos.
"""

validacao = analisador.validar_requisitos_mcp(prompt, nivel_rigor="avançado")

print(f"Conformidade: {validacao['conformidade']}%")
print("\nRequisitos atendidos:")
for req in validacao["requisitos_atendidos"]:
    print(f"  ✅ {req}")

print("\nRequisitos faltantes:")
for req in validacao["requisitos_faltantes"]:
    print(f"  ❌ {req}")
```

## Tratamento de Erros

O servidor implementa tratamento de erros específicos para cada funcionalidade:

```python
try:
    resultado = analisador.analisar_prompt(prompt)
except ValueError as e:
    print(f"Erro de validação: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
```

### Códigos de Erro Comuns

- `PROMPT_VAZIO`: O prompt fornecido está vazio
- `PROMPT_MUITO_CURTO`: O prompt é muito curto para uma análise significativa
- `CATEGORIA_INVALIDA`: A categoria de melhores práticas não existe
- `NIVEL_RIGOR_INVALIDO`: O nível de rigor fornecido é inválido
