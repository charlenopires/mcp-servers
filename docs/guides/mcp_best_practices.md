# Guia de Melhores Práticas MCP

## 📋 Introdução

Este guia apresenta as melhores práticas para o desenvolvimento de servidores MCP (Model Context Protocol), compiladas a partir da documentação oficial e experiências da comunidade. Estas práticas ajudam a criar servidores mais eficientes, seguros e fáceis de manter.

## 🎯 Princípios Fundamentais do MCP

### 1. Propósito Claro e Específico

Cada servidor MCP deve ter um propósito claramente definido e específico:

✅ **Recomendado:**

- Definir precisamente o domínio e as funcionalidades do servidor
- Focar em resolver um conjunto de problemas relacionados
- Comunicar o propósito claramente na documentação

❌ **Evitar:**

- Servidores "faz-tudo" sem foco definido
- Descrições vagas de propósito
- Misturar funcionalidades não relacionadas

**Exemplo:**

```python
# Bom exemplo:
mcp = FastMCP("Assistente de Análise Financeira para Pequenas Empresas")

# Exemplo problemático:
mcp = FastMCP("Assistente Geral")
```

### 2. Design de Ferramentas Focado

Cada ferramenta deve realizar uma função específica e bem definida:

✅ **Recomendado:**

- Uma ferramenta, uma função
- Nomes descritivos que refletem a ação realizada
- Parâmetros com nomes claros e tipos bem definidos

❌ **Evitar:**

- Ferramentas "canivete suíço" com múltiplas funcionalidades
- Nomes genéricos ou ambíguos
- Parâmetros excessivos ou confusos

**Exemplo:**

```python
# Bom exemplo:
@mcp.tool("Calcula a amortização de um empréstimo.")
def calcular_amortizacao(principal: float, taxa_juros: float, prazo_meses: int) -> Dict[str, Any]:
    """Calcula tabela de amortização para um empréstimo."""

# Exemplo problemático:
@mcp.tool("Realiza cálculos financeiros.")
def calculos_financeiros(tipo: str, valores: Dict[str, Any]) -> Dict[str, Any]:
    """Realiza vários cálculos financeiros dependendo do tipo."""
```

### 3. Tratamento Abrangente de Erros

Implementar validação robusta e tratamento de erros claro:

✅ **Recomendado:**

- Validar todos os inputs antes de processá-los
- Retornar mensagens de erro específicas e acionáveis
- Tratar exceções de forma elegante

❌ **Evitar:**

- Assumir que inputs serão sempre válidos
- Mensagens de erro genéricas
- Deixar exceções não tratadas propagarem

**Exemplo:**

```python
# Bom exemplo:
@mcp.tool("Converte moedas com base em taxas atuais.")
def converter_moeda(valor: float, de: str, para: str) -> Dict[str, Any]:
    """Converte um valor entre diferentes moedas."""
    if valor < 0:
        return {"erro": "O valor não pode ser negativo"}

    moedas_suportadas = ["USD", "EUR", "BRL", "JPY"]
    if de not in moedas_suportadas:
        return {"erro": f"Moeda de origem '{de}' não suportada. Moedas disponíveis: {moedas_suportadas}"}

    if para not in moedas_suportadas:
        return {"erro": f"Moeda de destino '{para}' não suportada. Moedas disponíveis: {moedas_suportadas}"}

    # Lógica de conversão...
```

## 🛠️ Práticas Essenciais

### 4. Documentação Clara e Completa

Documentar cada componente de forma abrangente:

✅ **Recomendado:**

- Documentar propósito, parâmetros e retornos de cada ferramenta
- Incluir exemplos de uso
- Explicar casos de erro e como lidar com eles

❌ **Evitar:**

- Documentação mínima ou ausente
- Exemplos desatualizados
- Omitir informações sobre limitações

**Exemplo:**

```python
@mcp.tool("Analisa sentimento de um texto em português.")
def analisar_sentimento(texto: str, detalhado: bool = False) -> Dict[str, Any]:
    """
    Analisa o sentimento de um texto em português.

    Args:
        texto: O texto a ser analisado (5-5000 caracteres)
        detalhado: Se True, inclui análise detalhada por sentença

    Returns:
        Dict contendo:
        - sentimento: str ("positivo", "neutro", "negativo")
        - confianca: float (0-1)
        - pontuacao: float (-1 a 1)
        - analise_detalhada: List[Dict] (apenas se detalhado=True)

    Exemplos:
        >>> analisar_sentimento("Adorei o produto, superou minhas expectativas!")
        {"sentimento": "positivo", "confianca": 0.92, "pontuacao": 0.87}
    """
```

### 5. Segurança e Validação

Implementar práticas de segurança em todo o código:

✅ **Recomendado:**

- Validar e sanitizar todas as entradas
- Implementar controles de acesso quando necessário
- Seguir o princípio do privilégio mínimo

❌ **Evitar:**

- Executar código ou comandos fornecidos pelo usuário
- Armazenar dados sensíveis em texto simples
- Ignorar potenciais riscos de segurança

**Exemplo:**

```python
@mcp.tool("Lê um arquivo de texto.")
def ler_arquivo(caminho: str) -> Dict[str, Any]:
    """Lê o conteúdo de um arquivo de texto."""

    # Validação de segurança
    caminho_absoluto = os.path.abspath(caminho)
    diretorio_permitido = os.path.abspath("./arquivos_permitidos")

    if not caminho_absoluto.startswith(diretorio_permitido):
        return {
            "erro": "Acesso negado. Só é permitido acessar arquivos no diretório 'arquivos_permitidos'."
        }

    if not os.path.exists(caminho_absoluto):
        return {"erro": "Arquivo não encontrado"}

    # Leitura segura
    try:
        with open(caminho_absoluto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        return {"conteudo": conteudo}
    except Exception as e:
        return {"erro": f"Erro ao ler arquivo: {str(e)}"}
```

### 6. Esquemas de Dados Bem Definidos

Usar esquemas claros para entradas e saídas:

✅ **Recomendado:**

- Definir claramente os tipos de todos os parâmetros
- Usar tipos estruturados (como Pydantic) para validação
- Documentar as estruturas de dados

❌ **Evitar:**

- Usar tipos genéricos como `Any` sem necessidade
- Retornar estruturas inconsistentes
- Aceitar ou retornar dados não estruturados

**Exemplo:**

```python
from pydantic import BaseModel, Field

class DadosCliente(BaseModel):
    """Modelo de dados para informações de cliente."""

    nome: str = Field(..., description="Nome completo do cliente")
    email: str = Field(..., description="Email válido do cliente")
    idade: int = Field(..., ge=18, description="Idade do cliente (mínimo 18 anos)")
    score_credito: Optional[int] = Field(None, ge=0, le=1000, description="Pontuação de crédito (0-1000)")

@mcp.tool("Registra um novo cliente.")
def registrar_cliente(cliente: DadosCliente) -> Dict[str, Any]:
    """Registra um novo cliente no sistema."""
    # Implementação...
```

### 7. Eficiência e Performance

Otimizar código para eficiência:

✅ **Recomendado:**

- Minimizar processamento desnecessário
- Reutilizar resultados quando possível (caching)
- Evitar chamadas externas repetitivas

❌ **Evitar:**

- Operações computacionalmente intensivas quando desnecessárias
- Loop de chamadas de API
- Carregar dados grandes na memória sem necessidade

**Exemplo:**

```python
# Uso de cache para evitar recálculos
from functools import lru_cache

@lru_cache(maxsize=100)
def calcular_estatisticas_complexas(dados_id: str) -> Dict[str, Any]:
    """Calcula estatísticas complexas para um conjunto de dados."""
    # Processamento intensivo...
    return resultado

@mcp.tool("Obtém estatísticas para um conjunto de dados.")
def obter_estatisticas(dados_id: str) -> Dict[str, Any]:
    """Obtém estatísticas complexas para um conjunto de dados."""
    return calcular_estatisticas_complexas(dados_id)
```

### 8. Extensibilidade

Projetar para facilitar extensões futuras:

✅ **Recomendado:**

- Código modular com responsabilidades bem definidas
- Interfaces estáveis com versionamento semântico
- Permitir configurabilidade

❌ **Evitar:**

- Acoplamento forte entre componentes
- Código monolítico difícil de modificar
- Suposições rígidas sobre o ambiente

**Exemplo:**

```python
class AnalisadorTexto:
    """Classe base para analisadores de texto."""

    def analisar(self, texto: str) -> Dict[str, Any]:
        """Método que deve ser implementado pelas subclasses."""
        raise NotImplementedError

class AnalisadorSentimento(AnalisadorTexto):
    """Implementação específica para análise de sentimento."""

    def analisar(self, texto: str) -> Dict[str, Any]:
        # Implementação específica...
        return resultado

# Isso permite adicionar facilmente novos tipos de análise no futuro
analisadores = {
    "sentimento": AnalisadorSentimento(),
    # Outros analisadores podem ser adicionados aqui
}

@mcp.tool("Analisa texto usando diferentes métodos.")
def analisar_texto(texto: str, tipo_analise: str) -> Dict[str, Any]:
    """Analisa um texto usando o método especificado."""
    if tipo_analise not in analisadores:
        return {"erro": f"Tipo de análise não suportado. Opções: {list(analisadores.keys())}"}

    return analisadores[tipo_analise].analisar(texto)
```

### 9. Convenções MCP

Seguir convenções estabelecidas do protocolo MCP:

✅ **Recomendado:**

- Seguir as convenções de nomeação recomendadas
- Garantir consistência entre as ferramentas
- Validar contra a especificação MCP

❌ **Evitar:**

- Usar convenções inconsistentes
- Ignorar recomendações de formatação
- Criar extensões proprietárias não documentadas

**Exemplo:**

```python
# Convenção de nomeação para ferramentas: verbo_substantivo
@mcp.tool("Calcula o juros composto de um investimento.")
def calcular_juros_composto(principal: float, taxa: float, periodo: int) -> Dict[str, Any]:
    """Calcula o montante final com juros compostos."""
    # Implementação...

# Convenção para nomes de parâmetros: snake_case
@mcp.tool("Formata um número como moeda.")
def formatar_moeda(valor: float, codigo_moeda: str = "BRL", incluir_simbolo: bool = True) -> str:
    """Formata um número como valor monetário."""
    # Implementação...
```

### 10. Testes Abrangentes

Implementar testes robustos para validar a funcionalidade:

✅ **Recomendado:**

- Escrever testes unitários para cada ferramenta
- Incluir testes para casos de erro
- Automatizar testes em pipeline de CI/CD

❌ **Evitar:**

- Testar apenas o "caminho feliz"
- Ignorar casos de borda
- Depender apenas de testes manuais

**Exemplo:**

```python
# test_calculadora_financeira.py
import unittest
from servidor_financeiro import calcular_juros_composto

class TestCalculadoraFinanceira(unittest.TestCase):

    def test_calcular_juros_composto_valores_validos(self):
        resultado = calcular_juros_composto(1000, 0.05, 5)
        self.assertAlmostEqual(resultado["montante"], 1276.28, places=2)

    def test_calcular_juros_composto_principal_negativo(self):
        resultado = calcular_juros_composto(-1000, 0.05, 5)
        self.assertIn("erro", resultado)

    def test_calcular_juros_composto_taxa_invalida(self):
        resultado = calcular_juros_composto(1000, -0.05, 5)
        self.assertIn("erro", resultado)
```

## 📊 Avaliação de Qualidade

A tabela abaixo apresenta os critérios de avaliação usados pelo Analisador de Prompts MCP para pontuar a qualidade dos prompts:

| Critério              | Peso | Descrição                                         |
| --------------------- | ---- | ------------------------------------------------- |
| Propósito Claro       | 15%  | Objetivos específicos e bem definidos do servidor |
| Design de Ferramentas | 15%  | Ferramentas focadas e bem nomeadas                |
| Tratamento de Erros   | 12%  | Validação e tratamento de exceções                |
| Documentação          | 10%  | Descrição clara das ferramentas                   |
| Segurança             | 10%  | Práticas recomendadas de segurança                |
| Esquema de Dados      | 10%  | Estruturas de dados bem definidas                 |
| Eficiência            | 8%   | Otimizações de desempenho                         |
| Extensibilidade       | 8%   | Facilidade de extensão                            |
| Convenções MCP        | 7%   | Alinhamento com padrões MCP                       |
| Testes                | 5%   | Cobertura de testes                               |

## 🚀 Próximos Passos

Para aplicar estas melhores práticas em seus servidores MCP:

1. **Avalie** seus prompts atuais usando o Analisador de Prompts MCP
2. **Identifique** as áreas que precisam de melhorias
3. **Implemente** as práticas recomendadas progressivamente
4. **Teste** regularmente a qualidade dos seus prompts
5. **Itere** para melhorar continuamente
