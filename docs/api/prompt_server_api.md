# API do Servidor de Engenharia de Prompts

Este documento descreve a API completa do Servidor de Engenharia de Prompts, incluindo detalhes sobre todas as classes, enums, métodos e parâmetros disponíveis.

## Classe Principal: `PromptEngineer`

```python
class PromptEngineer:
    """
    Implementa técnicas avançadas de engenharia de prompts para otimizar consultas.
    """
```

### Inicialização

```python
def __init__(self):
    """
    Inicializa o engenheiro de prompts com estratégias e técnicas predefinidas.
    """
```

## Enums e Tipos

### `TaskType`

```python
class TaskType(Enum):
    """Tipos de tarefas identificadas"""
    TEXT_GENERATION = "text_generation"
    CODE_GENERATION = "code_generation"
    IMAGE_GENERATION = "image_generation"
```

### `PromptStrategy`

```python
class PromptStrategy(Enum):
    """Estratégias de engenharia de prompts"""
    CHAIN_OF_THOUGHT = "chain_of_thought"
    FEW_SHOT = "few_shot"
    ROLE_PROMPTING = "role_prompting"
    SELF_CONSISTENCY = "self_consistency"
    TREE_OF_THOUGHTS = "tree_of_thoughts"
    REFLECTION = "reflection"
    ITERATIVE_REFINEMENT = "iterative_refinement"
    CONTEXT_DISTILLATION = "context_distillation"
```

### Modelos

```python
class PromptAnalysis(BaseModel):
    """Resultado da análise de estrutura de um prompt."""

    componentes: Dict[str, Any] = Field(..., description="Componentes identificados no prompt")
    complexidade: float = Field(..., description="Medida de complexidade (1-10)")
    clareza: float = Field(..., description="Medida de clareza (1-10)")
    ambiguidade: List[str] = Field(default_factory=list, description="Áreas potencialmente ambíguas")
    recomendacoes: List[str] = Field(default_factory=list, description="Recomendações estruturais")
```

```python
class PromptOptimizationRequest(BaseModel):
    """Solicitação para otimização de prompt."""

    prompt: str = Field(..., description="O texto do prompt a ser otimizado")
    tipo_tarefa: TaskType = Field(..., description="Tipo de tarefa")
    modelo_alvo: Optional[str] = Field(None, description="Modelo específico para otimização")
    nivel_detalhe: Optional[str] = Field("intermediário", description="Nível de detalhe desejado")
```

```python
class PromptOptimizationResult(BaseModel):
    """Resultado da otimização de prompt."""

    prompt_original: str = Field(..., description="O prompt original")
    prompt_otimizado: str = Field(..., description="O prompt otimizado")
    tecnicas_aplicadas: List[str] = Field(default_factory=list, description="Técnicas aplicadas")
    explicacoes: Dict[str, str] = Field(default_factory=dict, description="Explicação para cada alteração")
    metricas: Dict[str, float] = Field(default_factory=dict, description="Métricas de melhoria estimadas")
```

## Métodos Públicos

### `otimizar_prompt`

```python
def otimizar_prompt(self, prompt: str, tipo_tarefa: Union[str, TaskType],
                    modelo_alvo: Optional[str] = None,
                    nivel_detalhe: str = "intermediário") -> PromptOptimizationResult:
    """
    Otimiza um prompt aplicando técnicas específicas de engenharia de prompts.

    Args:
        prompt (str): O texto do prompt a ser otimizado
        tipo_tarefa (Union[str, TaskType]): Tipo de tarefa
        modelo_alvo (str, opcional): Modelo específico para otimização
        nivel_detalhe (str, opcional): Nível de detalhe desejado

    Returns:
        PromptOptimizationResult: Resultado da otimização
    """
```

### `analisar_estrutura_prompt`

```python
def analisar_estrutura_prompt(self, prompt: str) -> PromptAnalysis:
    """
    Analisa a estrutura de um prompt e identifica seus componentes e características.

    Args:
        prompt (str): O texto do prompt a ser analisado

    Returns:
        PromptAnalysis: Análise da estrutura do prompt
    """
```

### `aplicar_estrategia_prompt`

```python
def aplicar_estrategia_prompt(self, prompt: str, estrategia: Union[str, PromptStrategy],
                             parametros: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Aplica uma estratégia específica de engenharia de prompts ao prompt fornecido.

    Args:
        prompt (str): O texto do prompt base
        estrategia (Union[str, PromptStrategy]): Estratégia a ser aplicada
        parametros (Dict[str, Any], opcional): Parâmetros específicos para a estratégia

    Returns:
        Dict[str, Any]: Resultado da aplicação da estratégia
    """
```

### `gerar_prompt_template`

```python
def gerar_prompt_template(self, cenario: str, tipo_tarefa: Union[str, TaskType],
                         nivel_complexidade: str = "intermediário",
                         incluir_exemplos: bool = True) -> Dict[str, Any]:
    """
    Gera um template de prompt para um cenário específico.

    Args:
        cenario (str): Descrição do cenário ou caso de uso
        tipo_tarefa (Union[str, TaskType]): Tipo de tarefa
        nivel_complexidade (str, opcional): Nível de complexidade desejado
        incluir_exemplos (bool, opcional): Se deve incluir exemplos no template

    Returns:
        Dict[str, Any]: Template e informações relacionadas
    """
```

## Métodos Internos

### `_identificar_tipo_tarefa`

```python
def _identificar_tipo_tarefa(self, prompt: str) -> TaskType:
    """
    Identifica automaticamente o tipo de tarefa com base no conteúdo do prompt.

    Args:
        prompt (str): O texto do prompt

    Returns:
        TaskType: O tipo de tarefa identificado
    """
```

### `_extrair_componentes_prompt`

```python
def _extrair_componentes_prompt(self, prompt: str) -> Dict[str, Any]:
    """
    Extrai os componentes estruturais de um prompt (contexto, instrução, etc.).

    Args:
        prompt (str): O texto do prompt

    Returns:
        Dict[str, Any]: Componentes identificados
    """
```

### `_aplicar_chain_of_thought`

```python
def _aplicar_chain_of_thought(self, prompt: str, parametros: Optional[Dict[str, Any]] = None) -> str:
    """
    Aplica a estratégia Chain-of-Thought ao prompt.

    Args:
        prompt (str): O texto do prompt
        parametros (Dict[str, Any], opcional): Parâmetros específicos

    Returns:
        str: Prompt com Chain-of-Thought aplicado
    """
```

### `_aplicar_few_shot`

```python
def _aplicar_few_shot(self, prompt: str, parametros: Optional[Dict[str, Any]] = None) -> str:
    """
    Aplica a estratégia Few-Shot Learning ao prompt.

    Args:
        prompt (str): O texto do prompt
        parametros (Dict[str, Any], opcional): Parâmetros específicos

    Returns:
        str: Prompt com Few-Shot Learning aplicado
    """
```

### `_selecionar_estrategias_tipo_tarefa`

```python
def _selecionar_estrategias_tipo_tarefa(self, tipo_tarefa: TaskType) -> List[PromptStrategy]:
    """
    Seleciona estratégias de prompt adequadas para o tipo de tarefa.

    Args:
        tipo_tarefa (TaskType): O tipo de tarefa

    Returns:
        List[PromptStrategy]: Lista de estratégias recomendadas
    """
```

## Ferramentas MCP

### `otimizar_prompt`

```python
@mcp.tool("Otimiza um prompt aplicando técnicas de engenharia de prompts.", schema=types.otimizar_prompt)
def otimizar_prompt(prompt: str, tipo_tarefa: str, modelo_alvo: Optional[str] = None,
                   nivel_detalhe: str = "intermediário") -> Dict[str, Any]:
    """
    Otimiza um prompt aplicando técnicas específicas de engenharia de prompts baseadas no tipo de tarefa.

    Args:
        prompt (str): O texto do prompt a ser otimizado
        tipo_tarefa (str): Tipo de tarefa (text_generation, code_generation, image_generation)
        modelo_alvo (str, opcional): Modelo específico para o qual otimizar
        nivel_detalhe (str, opcional): Nível de detalhe desejado na saída

    Returns:
        Dict[str, Any]: Resultado da otimização contendo prompt otimizado,
                        técnicas aplicadas, explicações e métricas
    """
```

### `analisar_estrutura_prompt`

```python
@mcp.tool("Analisa a estrutura de um prompt e seus componentes.", schema=types.analisar_estrutura)
def analisar_estrutura_prompt(prompt: str) -> Dict[str, Any]:
    """
    Analisa a estrutura de um prompt e identifica seus componentes e características.

    Args:
        prompt (str): O texto do prompt a ser analisado

    Returns:
        Dict[str, Any]: Resultado da análise contendo componentes identificados,
                        medidas de complexidade e clareza, áreas ambíguas
                        e recomendações estruturais
    """
```

### `aplicar_estrategia_prompt`

```python
@mcp.tool("Aplica uma estratégia específica a um prompt.", schema=types.aplicar_estrategia)
def aplicar_estrategia_prompt(prompt: str, estrategia: str,
                              parametros: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Aplica uma estratégia específica de engenharia de prompts ao prompt fornecido.

    Args:
        prompt (str): O texto do prompt base
        estrategia (str): Estratégia a ser aplicada (chain_of_thought, few_shot, role_prompting, etc.)
        parametros (Dict[str, Any], opcional): Parâmetros específicos para a estratégia

    Returns:
        Dict[str, Any]: Resultado da aplicação da estratégia, incluindo
                        o prompt resultante, estrutura e notas de uso
    """
```

### `gerar_prompt_template`

```python
@mcp.tool("Gera um template de prompt para um cenário específico.", schema=types.gerar_template)
def gerar_prompt_template(cenario: str, tipo_tarefa: str, nivel_complexidade: str = "intermediário",
                          incluir_exemplos: bool = True) -> Dict[str, Any]:
    """
    Gera um template de prompt para um cenário específico.

    Args:
        cenario (str): Descrição do cenário ou caso de uso
        tipo_tarefa (str): Tipo de tarefa (text_generation, code_generation, image_generation)
        nivel_complexidade (str, opcional): Nível de complexidade desejado
        incluir_exemplos (boolean, opcional): Se deve incluir exemplos no template

    Returns:
        Dict[str, Any]: Template gerado, variáveis a serem preenchidas,
                        exemplos de uso e notas explicativas
    """
```

## Constantes e Configurações

### `ESTRATEGIAS_PROMPT`

```python
ESTRATEGIAS_PROMPT = {
    "chain_of_thought": {
        "descricao": "Induz raciocínio passo a passo explícito antes da resposta final",
        "aplicabilidade": ["resolução de problemas", "matemática", "raciocínio lógico"],
        "template": "Vamos pensar passo a passo sobre {problema}.\n\n1. {primeiro_passo}\n2. ...",
        "exemplos": [
            "Vamos pensar passo a passo sobre como resolver esta equação quadrática: 2x² + 5x - 3 = 0",
            # Outros exemplos...
        ]
    },
    # Outras estratégias...
}
```

### `TEMPLATES_TIPO_TAREFA`

```python
TEMPLATES_TIPO_TAREFA = {
    TaskType.TEXT_GENERATION.value: {
        "básico": "Escreva {tipo_conteudo} sobre {assunto}.",
        "intermediário": "Você é um especialista em {domínio}. Escreva {tipo_conteudo} sobre {assunto} com foco em {aspectos}.",
        "avançado": "Você é um especialista em {domínio} com {experiência}. Crie {tipo_conteudo} sobre {assunto} abordando {aspectos}. O conteúdo deve ser {estilo} e adequado para {público_alvo}. Inclua {elementos_específicos} e evite {elementos_evitar}."
    },
    # Outros tipos de tarefa...
}
```

### `PADROES_COMPONENTES`

```python
PADROES_COMPONENTES = {
    "contexto": [
        r"Você é (um|uma) ([^\.\,\n]+)",
        r"Considere o seguinte contexto:([^\n]+)",
        # Outros padrões...
    ],
    "instrucao": [
        r"(?:Por favor,\s)?(?:Crie|Faça|Escreva|Desenvolva|Elabore)([^\.\,\n]+)",
        r"Sua tarefa é ([^\.\,\n]+)",
        # Outros padrões...
    ],
    # Outros componentes...
}
```

## Tipos e Esquemas

```python
class Types:
    """Definição dos esquemas para as ferramentas MCP."""

    otimizar_prompt = {
        "parameters": {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "O texto do prompt a ser otimizado."
                },
                "tipo_tarefa": {
                    "type": "string",
                    "enum": ["text_generation", "code_generation", "image_generation"],
                    "description": "Tipo de tarefa para o prompt."
                },
                "modelo_alvo": {
                    "type": "string",
                    "description": "Modelo específico para o qual otimizar (opcional)."
                },
                "nivel_detalhe": {
                    "type": "string",
                    "enum": ["básico", "intermediário", "avançado"],
                    "description": "Nível de detalhe desejado na saída (opcional)."
                }
            },
            "required": ["prompt", "tipo_tarefa"]
        },
        "returns": {
            "type": "object",
            "properties": {
                "prompt_original": {
                    "type": "string",
                    "description": "O prompt original."
                },
                "prompt_otimizado": {
                    "type": "string",
                    "description": "Versão otimizada do prompt."
                },
                "tecnicas_aplicadas": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Lista de técnicas aplicadas."
                },
                "explicacoes": {
                    "type": "object",
                    "description": "Explicações para cada alteração."
                },
                "metricas": {
                    "type": "object",
                    "description": "Métricas de melhoria estimadas."
                }
            },
            "required": ["prompt_original", "prompt_otimizado", "tecnicas_aplicadas"]
        }
    }

    # Outros esquemas...
```

## Códigos de Status e Respostas

| Status          | Código | Descrição                                     |
| --------------- | ------ | --------------------------------------------- |
| SUCESSO         | 200    | Operação concluída com sucesso                |
| ERRO_VALIDACAO  | 400    | Erro de validação nos parâmetros de entrada   |
| ERRO_ESTRATEGIA | 422    | Estratégia não aplicável para o prompt/tarefa |
| ERRO_SERVIDOR   | 500    | Erro interno ao processar a solicitação       |

## Exemplos de Uso

### Exemplo 1: Otimização de Prompt para Código

```python
from servers.prompt_server import PromptEngineer, TaskType

engenheiro = PromptEngineer()

prompt_original = "Escreva código para ordernar lista"

resultado = engenheiro.otimizar_prompt(
    prompt=prompt_original,
    tipo_tarefa=TaskType.CODE_GENERATION,
    nivel_detalhe="intermediário"
)

print("Prompt Original:")
print(prompt_original)
print("\nPrompt Otimizado:")
print(resultado.prompt_otimizado)
print("\nTécnicas Aplicadas:")
for tecnica in resultado.tecnicas_aplicadas:
    print(f"- {tecnica}")
```

### Exemplo 2: Análise de Estrutura

```python
prompt = """
Você é um especialista em marketing digital.
Crie um plano de marketing para o lançamento de um aplicativo de fitness
focado em pessoas com mais de 50 anos. Inclua estratégias para redes sociais e email marketing.
"""

analise = engenheiro.analisar_estrutura_prompt(prompt)

print(f"Complexidade: {analise.complexidade}/10")
print(f"Clareza: {analise.clareza}/10")
print("\nComponentes identificados:")
for componente, valor in analise.componentes.items():
    print(f"- {componente}: {valor}")
print("\nRecomendações:")
for rec in analise.recomendacoes:
    print(f"- {rec}")
```

### Exemplo 3: Aplicação de Chain of Thought

```python
prompt_matematica = "Se um trem viaja a 120 km/h e percorre 360 km, quanto tempo leva a viagem?"

resultado = engenheiro.aplicar_estrategia_prompt(
    prompt=prompt_matematica,
    estrategia="chain_of_thought"
)

print("Prompt com Chain of Thought:")
print(resultado["prompt_resultante"])
```

### Exemplo 4: Geração de Template

```python
template = engenheiro.gerar_prompt_template(
    cenario="Resumo de artigos científicos na área de biologia",
    tipo_tarefa="text_generation",
    nivel_complexidade="avançado",
    incluir_exemplos=True
)

print("Template Gerado:")
print(template["template"])
print("\nVariáveis:")
for var in template["variaveis"]:
    print(f"- {var}")
print("\nExemplo de Uso:")
print(template["exemplos_uso"][0])
```

## Tratamento de Erros

O servidor implementa tratamento de erros específicos para cada funcionalidade:

```python
try:
    resultado = engenheiro.otimizar_prompt(prompt, tipo_tarefa)
except ValueError as e:
    print(f"Erro de validação: {e}")
except UnsupportedStrategyError as e:
    print(f"Erro de estratégia: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
```

### Exceções Personalizadas

```python
class UnsupportedStrategyError(Exception):
    """Levantada quando uma estratégia não é suportada para o prompt ou tipo de tarefa."""
    pass

class PromptAnalysisError(Exception):
    """Levantada quando ocorre um erro durante a análise de um prompt."""
    pass

class TemplateGenerationError(Exception):
    """Levantada quando ocorre um erro durante a geração de um template."""
    pass
```

### Códigos de Erro Comuns

- `ESTRATEGIA_NAO_SUPORTADA`: A estratégia não é suportada para o tipo de tarefa
- `TIPO_TAREFA_INVALIDO`: O tipo de tarefa fornecido é inválido
- `PROMPT_MUITO_CURTO`: O prompt é muito curto para aplicar as técnicas
- `NIVEL_INVALIDO`: O nível de detalhe ou complexidade é inválido
