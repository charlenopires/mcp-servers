# API de Migração do Tailwind CSS v3 → v4.1

Este documento descreve a API completa das ferramentas de migração do Tailwind CSS v3 para v4.1, disponíveis como parte do Servidor Tailwind CSS.

## 📋 Visão Geral

O módulo de migração oferece ferramentas para facilitar a transição de projetos do Tailwind CSS v3.x para a versão 4.1, incluindo conversão de configurações, transformação de classes, e validação de compatibilidade.

## 🛠️ Classes e Métodos

### `TailwindMigrationAssistant`

A classe principal responsável por gerenciar a migração de projetos Tailwind.

```python
class TailwindMigrationAssistant:
    """
    Assistente de migração do Tailwind CSS v3.x para v4.1.

    Fornece ferramentas para converter configurações, transformar classes,
    validar compatibilidade e gerar relatórios de migração.
    """

    def __init__(self, project_path: Optional[str] = None, config_file: Optional[str] = None):
        """
        Inicializa o assistente de migração.

        Args:
            project_path (str, opcional): Caminho para a raiz do projeto
            config_file (str, opcional): Caminho para o arquivo de configuração do Tailwind
        """
        pass
```

### `analisar_projeto`

```python
def analisar_projeto(
    self,
    include_patterns: List[str] = ["**/*.html", "**/*.jsx", "**/*.tsx", "**/*.vue"],
    exclude_patterns: List[str] = ["**/node_modules/**", "**/dist/**"]
) -> Dict[str, Any]:
    """
    Analisa um projeto para identificar o uso de classes Tailwind v3 e potenciais problemas de migração.

    Args:
        include_patterns (List[str]): Padrões glob para incluir arquivos na análise
        exclude_patterns (List[str]): Padrões glob para excluir arquivos da análise

    Returns:
        Dict[str, Any]: Relatório de análise contendo:
            - arquivos_analisados (int): Número de arquivos analisados
            - classes_encontradas (Dict[str, int]): Mapa de classes encontradas e suas frequências
            - classes_problematicas (Dict[str, List[str]]): Classes que precisarão de atenção especial
            - estimativa_esforco (str): Estimativa qualitativa do esforço de migração
            - recomendacoes (List[str]): Recomendações específicas para o projeto

    Raises:
        FileNotFoundError: Se o diretório do projeto não for encontrado
        PermissionError: Se não tiver permissão para ler os arquivos
    """
    pass
```

### `converter_configuracao`

```python
def converter_configuracao(
    self,
    output_format: str = "css",
    output_path: Optional[str] = None
) -> Dict[str, Any]:
    """
    Converte um arquivo de configuração Tailwind v3 (JavaScript) para o novo formato v4.1 (CSS).

    Args:
        output_format (str): Formato de saída ("css" para v4.1 ou "js" para compatibilidade retroativa)
        output_path (str, opcional): Caminho para salvar o arquivo convertido (se None, apenas retorna o conteúdo)

    Returns:
        Dict[str, Any]: Resultado da conversão contendo:
            - configuracao_original (str): Conteúdo da configuração original
            - configuracao_convertida (str): Conteúdo da configuração convertida
            - alteracoes (List[Dict]): Lista detalhada de alterações realizadas
            - avisos (List[str]): Avisos sobre potenciais problemas

    Raises:
        ValueError: Se o formato de saída for inválido
        FileNotFoundError: Se o arquivo de configuração não for encontrado
        SyntaxError: Se o arquivo de configuração contiver erros de sintaxe
    """
    pass
```

### `converter_arquivo`

```python
def converter_arquivo(
    self,
    file_path: str,
    output_path: Optional[str] = None,
    include_comments: bool = True
) -> Dict[str, Any]:
    """
    Converte um arquivo contendo classes Tailwind v3 para usar classes v4.1.

    Args:
        file_path (str): Caminho para o arquivo a ser convertido
        output_path (str, opcional): Caminho para salvar o arquivo convertido (se None, apenas retorna o conteúdo)
        include_comments (bool): Se deve incluir comentários explicativos sobre as alterações

    Returns:
        Dict[str, Any]: Resultado da conversão contendo:
            - arquivo_original (str): Conteúdo do arquivo original
            - arquivo_convertido (str): Conteúdo do arquivo convertido
            - classes_alteradas (Dict[str, str]): Mapeamento de classes antigas para novas
            - contagem_alteracoes (int): Número total de alterações realizadas

    Raises:
        FileNotFoundError: Se o arquivo não for encontrado
        PermissionError: Se não tiver permissão para ler ou escrever os arquivos
    """
    pass
```

### `converter_string_classes`

```python
def converter_string_classes(
    self,
    class_string: str,
    include_comments: bool = False
) -> Dict[str, Any]:
    """
    Converte uma string de classes Tailwind v3 para usar classes v4.1.

    Args:
        class_string (str): String contendo classes Tailwind
        include_comments (bool): Se deve incluir comentários explicativos

    Returns:
        Dict[str, Any]: Resultado da conversão contendo:
            - classes_originais (str): String original de classes
            - classes_convertidas (str): String convertida de classes
            - alteracoes (List[Dict]): Lista detalhada de alterações

    Raises:
        ValueError: Se a string de classes for inválida
    """
    pass
```

### `gerar_relatorio_migracao`

```python
def gerar_relatorio_migracao(
    self,
    formato: str = "markdown",
    incluir_guia: bool = True
) -> Dict[str, Any]:
    """
    Gera um relatório detalhado sobre a migração de um projeto.

    Args:
        formato (str): Formato do relatório ("markdown", "html", "json")
        incluir_guia (bool): Se deve incluir um guia de migração junto com o relatório

    Returns:
        Dict[str, Any]: Relatório de migração contendo:
            - resumo (Dict): Resumo executivo da migração
            - arquivos (List[Dict]): Detalhes por arquivo
            - alteracoes_comuns (Dict): Padrões comuns de alterações
            - proximos_passos (List[str]): Ações recomendadas
            - relatorio_completo (str): Relatório formatado no formato especificado

    Raises:
        ValueError: Se o formato especificado não for suportado
    """
    pass
```

### `validar_compatibilidade`

```python
def validar_compatibilidade(
    self,
    codigo: str,
    tipo_arquivo: Optional[str] = None
) -> Dict[str, Any]:
    """
    Valida a compatibilidade de um trecho de código com o Tailwind CSS v4.1.

    Args:
        codigo (str): Código a ser validado
        tipo_arquivo (str, opcional): Tipo de arquivo ("html", "jsx", "tsx", "vue", etc.)
                                     Se None, tenta detectar automaticamente

    Returns:
        Dict[str, Any]: Resultado da validação contendo:
            - compativel (bool): Se o código é totalmente compatível com v4.1
            - problemas (List[Dict]): Problemas de compatibilidade encontrados
            - sugestoes (List[str]): Sugestões para resolver os problemas
            - pontuacao_compatibilidade (float): Pontuação de 0 a 1 indicando o nível de compatibilidade

    Raises:
        ValueError: Se o código ou tipo de arquivo for inválido
    """
    pass
```

## 📊 Mapeamento de Classes

O módulo inclui mapeamentos detalhados de classes entre versões:

```python
COLOR_MAPPINGS = {
    # Mapeamentos de cores da v3 para v4.1
    "gray": "slate",
    "red": "ruby",
    "yellow": "amber",
    "green": "emerald",
    # ...outros mapeamentos
}

UTILITY_MAPPINGS = {
    # Mapeamentos de utilidades da v3 para v4.1
    "shadow-sm": "shadow-xs",
    "shadow-md": "shadow-sm",
    "shadow-lg": "shadow-md",
    "shadow-xl": "shadow-lg",
    "shadow-2xl": "shadow-xl",
    # ...outros mapeamentos
}

REMOVED_CLASSES = [
    # Classes removidas na v4.1
    "ring-offset-*",
    "filter",
    "backdrop-filter",
    # ...outras classes removidas
]

NEW_CLASSES = [
    # Novas classes na v4.1
    "motion-safe:*",
    "motion-reduce:*",
    "support-*",
    # ...outras novas classes
]
```

## 🧪 Exemplos de Uso

### Análise de Projeto

```python
from tailwind.migration import TailwindMigrationAssistant

# Inicializar o assistente apontando para o projeto
assistant = TailwindMigrationAssistant(project_path="/caminho/para/projeto")

# Analisar o projeto
analise = assistant.analisar_projeto(
    include_patterns=["**/*.jsx", "**/*.tsx"],
    exclude_patterns=["**/node_modules/**", "**/test/**"]
)

# Verificar resultados
print(f"Arquivos analisados: {analise['arquivos_analisados']}")
print(f"Classes encontradas: {len(analise['classes_encontradas'])}")
print(f"Classes problemáticas: {len(analise['classes_problematicas'])}")
print(f"Estimativa de esforço: {analise['estimativa_esforco']}")

# Recomendações
print("\nRecomendações:")
for i, rec in enumerate(analise['recomendacoes'], 1):
    print(f"{i}. {rec}")
```

### Conversão de Configuração

```python
# Converter o arquivo de configuração
configuracao = assistant.converter_configuracao(
    output_format="css",
    output_path="./tailwind.config.css"
)

# Visualizar alterações
print("Principais alterações na configuração:")
for alteracao in configuracao['alteracoes']:
    print(f"- {alteracao['descricao']}")
    if 'antes' in alteracao and 'depois' in alteracao:
        print(f"  Antes: {alteracao['antes']}")
        print(f"  Depois: {alteracao['depois']}")
```

### Conversão de Classes

```python
# Converter string de classes
resultado = assistant.converter_string_classes(
    "flex items-center justify-between p-4 bg-gray-100 shadow-lg rounded-lg",
    include_comments=True
)

print(f"Original: {resultado['classes_originais']}")
print(f"Convertido: {resultado['classes_convertidas']}")

print("\nAlterações detalhadas:")
for alteracao in resultado['alteracoes']:
    print(f"- {alteracao['original']} → {alteracao['nova']} ({alteracao['razao']})")
```

## 🔍 Solução de Problemas

### Códigos de Erro

| Código | Descrição                                   | Solução                                      |
| ------ | ------------------------------------------- | -------------------------------------------- |
| `E001` | Arquivo de configuração não encontrado      | Verifique o caminho do arquivo               |
| `E002` | Formato de configuração não suportado       | Use apenas arquivos JS para configuração v3  |
| `E003` | Sintaxe inválida no arquivo de configuração | Corrija os erros de sintaxe no arquivo       |
| `E004` | Diretório do projeto não encontrado         | Verifique se o caminho do projeto existe     |
| `E005` | Plugin incompatível com v4.1                | Atualize o plugin para uma versão compatível |
| `E006` | Classe Tailwind inválida                    | Verifique a sintaxe das classes Tailwind     |

### Avisos Comuns

| Aviso  | Descrição                          | Ação Recomendada                               |
| ------ | ---------------------------------- | ---------------------------------------------- |
| `W001` | Personalização complexa de tema    | Revise manualmente a conversão do tema         |
| `W002` | Uso de plugins não verificados     | Verifique compatibilidade dos plugins com v4.1 |
| `W003` | Uso extensivo de classes removidas | Considere refatoração de componentes afetados  |
| `W004` | Sobreposição de configurações      | Simplifique configurações redundantes          |

## 📚 Recursos Relacionados

- [Documentação do Servidor Tailwind CSS](../servers/tailwind_server.md)
- [Guia de Migração v3 → v4.1](../guides/tailwind_migration_guide.md)
- [Exemplos de Componentes v4.1](../examples/tailwind_components.md)

---

**Desenvolvido para o projeto MCP Servers**
