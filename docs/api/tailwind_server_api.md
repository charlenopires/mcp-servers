# API do Servidor Tailwind CSS v4.1

Este documento descreve a API completa do Servidor Tailwind CSS v4.1, incluindo detalhes sobre todas as classes, funções e parâmetros disponíveis.

## Classe Principal: `TailwindServer`

```python
class TailwindServer:
    """
    Servidor MCP para contextualização de prompts do Tailwind CSS v4.1.
    Fornece informações sobre novas funcionalidades, migração de versões anteriores e exemplos de uso.
    """
```

### Inicialização

```python
def __init__(self):
    """
    Inicializa o servidor com a base de conhecimento do Tailwind CSS v4.1.
    """
```

## Modelos

```python
class TailwindConversionRequest(BaseModel):
    """Solicitação para conversão de código Tailwind."""

    codigo: str = Field(..., description="Código HTML/JSX com classes Tailwind para converter")
    versao_origem: str = Field("3.x", description="Versão de origem do código")
    incluir_comentarios: bool = Field(True, description="Se deve incluir comentários explicativos")
```

```python
class TailwindConversionResult(BaseModel):
    """Resultado da conversão de código Tailwind."""

    codigo_original: str = Field(..., description="Código original")
    codigo_convertido: str = Field(..., description="Código com classes atualizadas")
    alteracoes: List[Dict[str, str]] = Field(default_factory=list, description="Lista de alterações realizadas")
    notas: List[str] = Field(default_factory=list, description="Notas explicativas")
    problemas: List[str] = Field(default_factory=list, description="Possíveis problemas identificados")
```

```python
class ComponentRequest(BaseModel):
    """Solicitação para geração de componente Tailwind."""

    descricao: str = Field(..., description="Descrição do componente desejado")
    framework: str = Field("React", description="Framework de UI")
    estilo: str = Field("minimal", description="Estilo visual desejado")
    responsivo: bool = Field(True, description="Se o componente deve ser responsivo")
```

## Métodos Públicos

### `obter_novidades_tailwind`

```python
def obter_novidades_tailwind(self, categoria: Optional[str] = None,
                            formato: str = "detalhado") -> Dict[str, Any]:
    """
    Fornece informações sobre as novas funcionalidades e mudanças no Tailwind CSS v4.1.

    Args:
        categoria (str, opcional): Categoria específica de mudanças
                                  (configuração, utilidades, plugins, etc.)
        formato (str, opcional): Formato da resposta (resumo, detalhado, comparativo)

    Returns:
        Dict[str, Any]: Informações sobre novidades do Tailwind v4.1
    """
```

### `converter_codigo_tailwind`

```python
def converter_codigo_tailwind(self, codigo: str, versao_origem: str = "3.x",
                             incluir_comentarios: bool = True) -> TailwindConversionResult:
    """
    Converte código Tailwind de versões anteriores para a versão 4.1.

    Args:
        codigo (str): Código HTML/JSX com classes Tailwind para converter
        versao_origem (str, opcional): Versão de origem do código (default: 3.x)
        incluir_comentarios (bool, opcional): Se deve incluir comentários explicativos

    Returns:
        TailwindConversionResult: Resultado da conversão
    """
```

### `otimizar_classes_tailwind`

```python
def otimizar_classes_tailwind(self, codigo: str, nivel_otimizacao: str = "intermediário",
                             preservar_comentarios: bool = True) -> Dict[str, Any]:
    """
    Otimiza o uso de classes Tailwind para tornar o código mais limpo e eficiente.

    Args:
        codigo (str): Código HTML/JSX com classes Tailwind para otimizar
        nivel_otimizacao (str, opcional): Nível de otimização
                                         (básico, intermediário, avançado)
        preservar_comentarios (bool, opcional): Se deve preservar comentários existentes

    Returns:
        Dict[str, Any]: Resultado da otimização
    """
```

### `gerar_componentes_tailwind`

```python
def gerar_componentes_tailwind(self, descricao: str, framework: str = "React",
                              estilo: str = "minimal", responsivo: bool = True) -> Dict[str, Any]:
    """
    Gera componentes utilizando Tailwind CSS v4.1 com base em descrições ou requisitos.

    Args:
        descricao (str): Descrição do componente desejado
        framework (str, opcional): Framework de UI (React, Vue, Angular, HTML)
        estilo (str, opcional): Estilo visual desejado (minimal, corporate, playful, etc.)
        responsivo (bool, opcional): Se o componente deve ser responsivo

    Returns:
        Dict[str, Any]: Componente gerado e informações relacionadas
    """
```

## Métodos Internos

### `_obter_base_conhecimento`

```python
def _obter_base_conhecimento(self, categoria: Optional[str] = None) -> Dict[str, Any]:
    """
    Recupera informações da base de conhecimento do Tailwind CSS v4.1.

    Args:
        categoria (str, opcional): Categoria específica

    Returns:
        Dict[str, Any]: Informações da base de conhecimento
    """
```

### `_identificar_classes_tailwind`

```python
def _identificar_classes_tailwind(self, codigo: str) -> List[str]:
    """
    Identifica todas as classes Tailwind em um trecho de código.

    Args:
        codigo (str): Código HTML/JSX com classes Tailwind

    Returns:
        List[str]: Lista de classes Tailwind identificadas
    """
```

### `_converter_classe`

```python
def _converter_classe(self, classe: str, versao_origem: str = "3.x") -> Dict[str, str]:
    """
    Converte uma classe Tailwind específica para a versão 4.1.

    Args:
        classe (str): Classe Tailwind para converter
        versao_origem (str, opcional): Versão de origem da classe

    Returns:
        Dict[str, str]: Informações sobre a conversão
    """
```

### `_otimizar_classes`

```python
def _otimizar_classes(self, classes: List[str], nivel_otimizacao: str = "intermediário") -> Dict[str, Any]:
    """
    Otimiza um conjunto de classes Tailwind.

    Args:
        classes (List[str]): Lista de classes Tailwind
        nivel_otimizacao (str, opcional): Nível de otimização

    Returns:
        Dict[str, Any]: Resultado da otimização
    """
```

### `_gerar_template_componente`

```python
def _gerar_template_componente(self, tipo_componente: str, framework: str,
                              estilo: str) -> Dict[str, Any]:
    """
    Gera um template base para um tipo específico de componente.

    Args:
        tipo_componente (str): Tipo de componente (card, modal, form, etc.)
        framework (str): Framework de UI
        estilo (str): Estilo visual

    Returns:
        Dict[str, Any]: Template base para o componente
    """
```

## Ferramentas MCP

### `obter_novidades_tailwind`

```python
@mcp.tool("Obtém informações sobre as novidades do Tailwind CSS v4.1.", schema=types.obter_novidades)
def obter_novidades_tailwind(categoria: Optional[str] = None,
                            formato: str = "detalhado") -> Dict[str, Any]:
    """
    Fornece informações sobre as novas funcionalidades e mudanças no Tailwind CSS v4.1.

    Args:
        categoria (str, opcional): Categoria específica de mudanças
                                  (configuração, utilidades, plugins, etc.)
        formato (str, opcional): Formato da resposta (resumo, detalhado, comparativo)

    Returns:
        Dict[str, Any]: Informações sobre as novidades, incluindo descrições,
                        alterações importantes, exemplos e recursos adicionais
    """
```

### `converter_codigo_tailwind`

```python
@mcp.tool("Converte código Tailwind de versões anteriores para a v4.1.", schema=types.converter_codigo)
def converter_codigo_tailwind(codigo: str, versao_origem: str = "3.x",
                             incluir_comentarios: bool = True) -> Dict[str, Any]:
    """
    Converte código Tailwind de versões anteriores para a versão 4.1.

    Args:
        codigo (str): Código HTML/JSX com classes Tailwind para converter
        versao_origem (str, opcional): Versão de origem do código (default: 3.x)
        incluir_comentarios (boolean, opcional): Se deve incluir comentários explicativos

    Returns:
        Dict[str, Any]: Resultado da conversão, incluindo código convertido,
                        lista de alterações, notas explicativas e possíveis problemas
    """
```

### `otimizar_classes_tailwind`

```python
@mcp.tool("Otimiza o uso de classes Tailwind.", schema=types.otimizar_classes)
def otimizar_classes_tailwind(codigo: str, nivel_otimizacao: str = "intermediário",
                             preservar_comentarios: bool = True) -> Dict[str, Any]:
    """
    Otimiza o uso de classes Tailwind para tornar o código mais limpo e eficiente.

    Args:
        codigo (str): Código HTML/JSX com classes Tailwind para otimizar
        nivel_otimizacao (str, opcional): Nível de otimização
                                         (básico, intermediário, avançado)
        preservar_comentarios (boolean, opcional): Se deve preservar comentários existentes

    Returns:
        Dict[str, Any]: Resultado da otimização, incluindo código otimizado,
                        lista de otimizações, métricas de melhoria e recomendações
    """
```

### `gerar_componentes_tailwind`

```python
@mcp.tool("Gera componentes utilizando Tailwind CSS v4.1.", schema=types.gerar_componentes)
def gerar_componentes_tailwind(descricao: str, framework: str = "React",
                              estilo: str = "minimal", responsivo: bool = True) -> Dict[str, Any]:
    """
    Gera componentes utilizando Tailwind CSS v4.1 com base em descrições ou requisitos.

    Args:
        descricao (str): Descrição do componente desejado
        framework (str, opcional): Framework de UI (React, Vue, Angular, HTML)
        estilo (str, opcional): Estilo visual desejado (minimal, corporate, playful, etc.)
        responsivo (boolean, opcional): Se o componente deve ser responsivo

    Returns:
        Dict[str, Any]: Componente gerado, URL para preview (se disponível),
                        variações e notas de implementação
    """
```

## Constantes e Configurações

### `TAILWIND_V4_CONTEXT`

```python
TAILWIND_V4_CONTEXT = {
    "version": "4.1.7",
    "release_date": "2025-05-15",
    "major_changes": {
        "configuration": {
            "location": "CSS file instead of tailwind.config.js",
            "syntax": "Using @config directive in CSS",
            "examples": [
                """
                @config {
                  content: ["./src/**/*.{html,js,jsx,ts,tsx}"];
                  plugins: [formPlugin, typographyPlugin];
                }
                """
            ]
        },
        "color_system": {
            "updates": "Enhanced color palette with new colors",
            "examples": [
                "slate-950", "zinc-950", "stone-950"
            ]
        },
        # Outras mudanças...
    },
    # Outras categorias...
}
```

### `CLASS_MAPPINGS`

```python
CLASS_MAPPINGS = {
    # Cores
    r"bg-gray-(\d+)": "bg-slate-\\1",
    r"text-gray-(\d+)": "text-slate-\\1",
    r"border-gray-(\d+)": "border-slate-\\1",

    # Sombras
    r"shadow-md": "shadow-md",  # Mantido
    r"shadow-lg": "shadow-xl",  # Alterado
    r"shadow-xl": "shadow-2xl", # Alterado

    # Outras conversões...
}
```

### `COMPONENT_TEMPLATES`

```python
COMPONENT_TEMPLATES = {
    "React": {
        "card": {
            "minimal": {
                "template": """
                export default function Card({ title, description, imageUrl }) {
                  return (
                    <div className="bg-white rounded-xl shadow-md overflow-hidden">
                      {imageUrl && (
                        <div className="h-48 w-full overflow-hidden">
                          <img className="w-full h-full object-cover" src={imageUrl} alt={title} />
                        </div>
                      )}
                      <div className="p-6">
                        <h2 className="text-xl font-semibold text-slate-900">{title}</h2>
                        <p className="mt-2 text-slate-600">{description}</p>
                      </div>
                    </div>
                  );
                }
                """,
                "props": ["title", "description", "imageUrl"]
            },
            # Outros estilos...
        },
        # Outros componentes...
    },
    # Outros frameworks...
}
```

## Tipos e Esquemas

```python
class Types:
    """Definição dos esquemas para as ferramentas MCP."""

    obter_novidades = {
        "parameters": {
            "type": "object",
            "properties": {
                "categoria": {
                    "type": "string",
                    "enum": ["configuração", "utilidades", "plugins", "cores", "tipografia", "layout", "animações", "todos"],
                    "description": "Categoria específica de mudanças (opcional)."
                },
                "formato": {
                    "type": "string",
                    "enum": ["resumo", "detalhado", "comparativo"],
                    "description": "Formato da resposta (opcional)."
                }
            }
        },
        "returns": {
            "type": "object",
            "properties": {
                "novidades": {
                    "type": "object",
                    "description": "Descrição detalhada das novas funcionalidades."
                },
                "alteracoes_importantes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Mudanças que podem quebrar compatibilidade."
                },
                "exemplos": {
                    "type": "object",
                    "description": "Exemplos de uso para as novas funcionalidades."
                },
                "recursos": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Links e recursos adicionais."
                }
            },
            "required": ["novidades"]
        }
    }

    # Outros esquemas...
```

## Códigos de Status e Respostas

| Status         | Código | Descrição                                   |
| -------------- | ------ | ------------------------------------------- |
| SUCESSO        | 200    | Operação concluída com sucesso              |
| ERRO_VALIDACAO | 400    | Erro de validação nos parâmetros de entrada |
| ERRO_CONVERSAO | 422    | Erro durante a conversão do código          |
| ERRO_SERVIDOR  | 500    | Erro interno ao processar a solicitação     |

## Exemplos de Uso

### Exemplo 1: Obter Novidades do Tailwind v4.1

```python
from servers.tailwind_server import TailwindServer

tailwind = TailwindServer()

# Obter novidades sobre configuração
novidades = tailwind.obter_novidades_tailwind(
    categoria="configuração",
    formato="comparativo"
)

print("Novidades na Configuração do Tailwind v4.1:")
for key, value in novidades["novidades"].items():
    print(f"- {key}: {value}")

print("\nAlterações Importantes:")
for alteracao in novidades["alteracoes_importantes"]:
    print(f"- {alteracao}")

print("\nExemplos:")
for tipo, exemplo in novidades["exemplos"].items():
    print(f"\n{tipo}:")
    print(exemplo)
```

### Exemplo 2: Converter Código de Tailwind v3 para v4.1

```python
# Código da versão anterior
codigo_antigo = """
<button class="bg-gray-800 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded shadow-lg">
  Clique Aqui
</button>
"""

# Conversão para v4.1
resultado = tailwind.converter_codigo_tailwind(
    codigo=codigo_antigo,
    versao_origem="3.x",
    incluir_comentarios=True
)

print("Código Original:")
print(codigo_antigo)
print("\nCódigo Convertido:")
print(resultado.codigo_convertido)
print("\nAlterações:")
for alteracao in resultado.alteracoes:
    print(f"- {alteracao['original']} → {alteracao['novo']}")
```

### Exemplo 3: Otimizar Classes Tailwind

```python
# Código com classes não otimizadas
codigo = """
<div class="pt-4 pr-4 pb-4 pl-4 text-blue-500 text-opacity-75 flex flex-row items-center justify-center">
  <span class="font-bold font-sans">Conteúdo</span>
</div>
"""

# Otimização
resultado = tailwind.otimizar_classes_tailwind(
    codigo=codigo,
    nivel_otimizacao="intermediário"
)

print("Código Original:")
print(codigo)
print("\nCódigo Otimizado:")
print(resultado["codigo_otimizado"])
print("\nOtimizações:")
for otimizacao in resultado["otimizacoes"]:
    print(f"- {otimizacao}")
print("\nMétricas:")
for metrica, valor in resultado["metricas"].items():
    print(f"- {metrica}: {valor}")
```

### Exemplo 4: Gerar Componente Tailwind

```python
# Solicitar geração de componente
componente = tailwind.gerar_componentes_tailwind(
    descricao="Card de produto com imagem, título, preço e botão de compra",
    framework="React",
    estilo="corporate",
    responsivo=True
)

print("Componente Gerado:")
print(componente["codigo"])
if "variacoes" in componente and componente["variacoes"]:
    print("\nVariações Disponíveis:")
    for i, variacao in enumerate(componente["variacoes"], 1):
        print(f"\nVariação {i}:")
        print(variacao["descricao"])
```

## Tratamento de Erros

O servidor implementa tratamento de erros específicos para cada funcionalidade:

```python
try:
    resultado = tailwind.converter_codigo_tailwind(codigo)
except ValueError as e:
    print(f"Erro de validação: {e}")
except ConversionError as e:
    print(f"Erro de conversão: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
```

### Exceções Personalizadas

```python
class ConversionError(Exception):
    """Levantada quando ocorre um erro durante a conversão de código Tailwind."""
    pass

class OptimizationError(Exception):
    """Levantada quando ocorre um erro durante a otimização de classes Tailwind."""
    pass

class ComponentGenerationError(Exception):
    """Levantada quando ocorre um erro durante a geração de componentes."""
    pass
```

### Códigos de Erro Comuns

- `CODIGO_INVALIDO`: O código fornecido não é válido ou não contém classes Tailwind
- `VERSAO_INVALIDA`: A versão de origem fornecida não é suportada
- `FRAMEWORK_INVALIDO`: O framework solicitado não é suportado
- `ESTILO_INVALIDO`: O estilo visual solicitado não é suportado
