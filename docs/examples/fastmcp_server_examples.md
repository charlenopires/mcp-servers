# FastMCP Server - Exemplos Detalhados

## 📋 Visão Geral

O FastMCP Server é especializado em assistir o desenvolvimento de servidores MCP usando o framework FastMCP. Ele oferece análise de prompts, otimização de código, validação de melhores práticas e geração de templates para desenvolvimento eficiente de servidores MCP.

## 🎯 Funcionalidades Principais

- **Análise de Prompts MCP**: Avalia prompts para criação de servidores MCP
- **Validação de Requisitos**: Verifica compatibilidade com protocolo MCP
- **Geração de Templates**: Cria estruturas base para diferentes tipos de servidores
- **Otimização de Código**: Melhora performance e estrutura de servidores existentes
- **Melhores Práticas**: Aplica padrões recomendados do FastMCP

## 🚀 Análise e Otimização de Prompts

### 1. Análise Completa de Prompt MCP

```python
from servers.fastmcp_server import FastMCPAssistant

# Inicializar assistente
fastmcp = FastMCPAssistant()

# Prompt para análise
prompt_mcp = """
Crie um servidor MCP que gerencie uma biblioteca de livros.
Deve permitir buscar livros, adicionar novos livros, emprestar e devolver.
Use banco de dados SQLite.
"""

# Análise detalhada
analise = fastmcp.analisar_prompt_mcp(prompt_mcp)

print("=== ANÁLISE DO PROMPT MCP ===")
print(f"Pontuação Geral: {analise.score}/100")
print(f"\nPontos Fortes:")
for forte in analise.strengths:
    print(f"  ✅ {forte}")

print(f"\nPontos Fracos:")
for fraco in analise.weaknesses:
    print(f"  ❌ {fraco}")

print(f"\nRecomendações:")
for rec in analise.recommendations:
    print(f"  💡 {rec}")

print(f"\nElementos Ausentes:")
for ausente in analise.missing_elements:
    print(f"  ⚠️ {ausente}")
```

**Resultado Esperado:**

```
=== ANÁLISE DO PROMPT MCP ===
Pontuação Geral: 68/100

Pontos Fortes:
  ✅ Domínio de aplicação bem definido (biblioteca)
  ✅ Operações CRUD claramente especificadas
  ✅ Tecnologia de persistência mencionada (SQLite)
  ✅ Escopo razoável para um servidor MCP

Pontos Fracos:
  ❌ Não especifica ferramentas MCP necessárias
  ❌ Ausência de tratamento de erros
  ❌ Não menciona validação de dados
  ❌ Estrutura de resposta não definida

Recomendações:
  💡 Especificar ferramentas MCP: search_books, add_book, borrow_book, return_book
  💡 Definir modelos Pydantic para validação de dados
  💡 Incluir tratamento de erros com códigos apropriados
  💡 Especificar formato de resposta para cada operação
  💡 Considerar operações assíncronas para banco de dados

Elementos Ausentes:
  ⚠️ Definição de recursos MCP (se aplicável)
  ⚠️ Estrutura de logging e monitoramento
  ⚠️ Configuração de ambiente e dependências
  ⚠️ Testes unitários e validação
```

### 2. Extração de Requisitos MCP

```python
# Extrair requisitos técnicos
requisitos = fastmcp.extrair_requisitos_mcp(prompt_mcp)

print("=== REQUISITOS EXTRAÍDOS ===")
print(f"Ferramentas necessárias: {requisitos.tools}")
print(f"Recursos a expor: {requisitos.resources}")
print(f"Operações assíncronas: {requisitos.async_operations}")
print(f"APIs externas: {requisitos.external_apis}")
print(f"Autenticação necessária: {requisitos.authentication}")
print(f"Tratamento de erros: {requisitos.error_handling}")
```

**Resultado Esperado:**

```
=== REQUISITOS EXTRAÍDOS ===
Ferramentas necessárias: ['search_books', 'add_book', 'borrow_book', 'return_book', 'list_available_books']
Recursos a expor: ['books_database', 'library_schema']
Operações assíncronas: True
APIs externas: []
Autenticação necessária: False
Tratamento de erros: False
```

### 3. Otimização de Prompt para FastMCP

```python
# Otimizar prompt aplicando melhores práticas FastMCP
prompt_otimizado = fastmcp.otimizar_prompt_fastmcp(
    prompt=prompt_mcp,
    nivel_detalhe="completo",
    incluir_testes=True,
    incluir_documentacao=True
)

print("=== PROMPT OTIMIZADO ===")
print(prompt_otimizado['enhanced_prompt'])
print(f"\nMelhorias aplicadas: {len(prompt_otimizado['improvements'])} items")
print(f"Pontuação estimada: {prompt_otimizado['estimated_score']}/100")
```

**Resultado Esperado:**

````
=== PROMPT OTIMIZADO ===

# Servidor MCP para Gerenciamento de Biblioteca de Livros

## Objetivo
Desenvolver um servidor MCP completo para gerenciar uma biblioteca de livros usando FastMCP, com operações CRUD, persistência SQLite e validação robusta.

## Especificações Técnicas

### Dependências
- fastmcp >= 2.0.0
- sqlite3 (built-in)
- pydantic >= 2.0.0
- asyncio

### Modelos de Dados (Pydantic)
```python
class Book(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=200)
    author: str = Field(..., min_length=1, max_length=100)
    isbn: str = Field(..., regex=r'^\d{10}|\d{13}$')
    available: bool = True
    borrowed_by: Optional[str] = None
    borrowed_date: Optional[datetime] = None
    due_date: Optional[datetime] = None

class BorrowRequest(BaseModel):
    book_id: int
    borrower_name: str = Field(..., min_length=1, max_length=100)
    borrow_days: int = Field(default=14, ge=1, le=90)
````

### Ferramentas MCP Necessárias

1. **search_books**

   - Parâmetros: query (str), filter_available (bool, default=True)
   - Retorno: List[Book]
   - Funcionalidade: Busca livros por título, autor ou ISBN

2. **add_book**

   - Parâmetros: book_data (Book)
   - Retorno: Book (com ID atribuído)
   - Funcionalidade: Adiciona novo livro à biblioteca

3. **borrow_book**

   - Parâmetros: borrow_request (BorrowRequest)
   - Retorno: Book (atualizado)
   - Funcionalidade: Registra empréstimo de livro

4. **return_book**

   - Parâmetros: book_id (int), return_condition (str, optional)
   - Retorno: Book (atualizado)
   - Funcionalidade: Processa devolução de livro

5. **list_overdue_books**
   - Parâmetros: days_overdue (int, default=0)
   - Retorno: List[Book]
   - Funcionalidade: Lista livros em atraso

### Recursos MCP (Opcionais)

- books_database: Acesso de leitura ao banco de dados
- library_statistics: Estatísticas da biblioteca

### Tratamento de Erros

- BookNotFoundError: Livro não encontrado
- BookNotAvailableError: Livro já emprestado
- InvalidISBNError: ISBN inválido
- DatabaseError: Erro de banco de dados

### Implementação

- Use padrão async/await para operações de banco
- Implemente logging estruturado
- Valide todos os inputs com Pydantic
- Use transações SQLite para consistência
- Implemente rate limiting se necessário

### Testes Necessários

- Testes unitários para cada ferramenta
- Testes de integração com banco de dados
- Testes de validação de dados
- Testes de tratamento de erros

### Documentação

- Docstrings completas para todas as funções
- README com instruções de instalação e uso
- Exemplos de uso para cada ferramenta

Melhorias aplicadas: 12 items
Pontuação estimada: 92/100

````

## 🏗️ Geração de Templates

### 4. Template de Servidor Básico

```python
# Gerar template base para servidor MCP
template_basico = fastmcp.gerar_template_servidor(
    nome="BibliotecaServer",
    descricao="Servidor MCP para gerenciamento de biblioteca",
    ferramentas=["search_books", "add_book", "borrow_book", "return_book"],
    usa_banco_dados=True,
    async_operations=True
)

print("=== TEMPLATE GERADO ===")
print(template_basico['codigo_servidor'])
````

**Resultado Esperado:**

```python
=== TEMPLATE GERADO ===

"""
BibliotecaServer - Servidor MCP para gerenciamento de biblioteca
Implementado com FastMCP para operações de biblioteca com SQLite
"""

import asyncio
import sqlite3
import logging
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
from pathlib import Path

from fastmcp import FastMCP, Context
from pydantic import BaseModel, Field, field_validator
from typing_extensions import Annotated

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicialização do servidor FastMCP
mcp = FastMCP(
    name="biblioteca-server",
    description="Servidor MCP para gerenciamento completo de biblioteca de livros",
    instructions="""
    Este servidor permite o gerenciamento completo de uma biblioteca:
    - Buscar livros por título, autor ou ISBN
    - Adicionar novos livros ao acervo
    - Registrar empréstimos e devoluções
    - Monitorar livros em atraso
    """,
    dependencies=["fastmcp>=2.0.0", "pydantic>=2.0.0"]
)

# Modelos Pydantic
class Book(BaseModel):
    """Modelo para representar um livro"""
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=200, description="Título do livro")
    author: str = Field(..., min_length=1, max_length=100, description="Autor do livro")
    isbn: str = Field(..., description="ISBN do livro")
    available: bool = Field(default=True, description="Se o livro está disponível")
    borrowed_by: Optional[str] = Field(default=None, description="Nome do usuário que emprestou")
    borrowed_date: Optional[datetime] = Field(default=None, description="Data do empréstimo")
    due_date: Optional[datetime] = Field(default=None, description="Data de vencimento")

    @field_validator('isbn')
    @classmethod
    def validate_isbn(cls, v):
        """Valida formato do ISBN"""
        if not (v.isdigit() and len(v) in [10, 13]):
            raise ValueError('ISBN deve ter 10 ou 13 dígitos')
        return v

class BorrowRequest(BaseModel):
    """Modelo para requisição de empréstimo"""
    book_id: int = Field(..., gt=0, description="ID do livro a ser emprestado")
    borrower_name: str = Field(..., min_length=1, max_length=100, description="Nome do usuário")
    borrow_days: int = Field(default=14, ge=1, le=90, description="Dias de empréstimo")

# Gerenciador de banco de dados
class DatabaseManager:
    """Gerencia operações do banco de dados SQLite"""

    def __init__(self, db_path: str = "biblioteca.db"):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """Inicializa o banco de dados"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    isbn TEXT UNIQUE NOT NULL,
                    available BOOLEAN DEFAULT TRUE,
                    borrowed_by TEXT,
                    borrowed_date TIMESTAMP,
                    due_date TIMESTAMP
                )
            ''')
            conn.commit()

    async def execute_query(self, query: str, params: tuple = ()) -> List[Dict]:
        """Executa query de forma assíncrona"""
        loop = asyncio.get_event_loop()

        def _execute():
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.execute(query, params)
                return [dict(row) for row in cursor.fetchall()]

        return await loop.run_in_executor(None, _execute)

    async def execute_update(self, query: str, params: tuple = ()) -> int:
        """Executa update/insert de forma assíncrona"""
        loop = asyncio.get_event_loop()

        def _execute():
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute(query, params)
                conn.commit()
                return cursor.lastrowid or cursor.rowcount

        return await loop.run_in_executor(None, _execute)

# Instância global do gerenciador
db_manager = DatabaseManager()

# Ferramentas MCP
@mcp.tool()
async def search_books(
    query: Annotated[str, "Termo de busca para título, autor ou ISBN"],
    filter_available: Annotated[bool, "Filtrar apenas livros disponíveis"] = True
) -> List[Book]:
    """Busca livros na biblioteca por título, autor ou ISBN"""

    try:
        where_clause = "WHERE (title LIKE ? OR author LIKE ? OR isbn LIKE ?)"
        params = [f"%{query}%", f"%{query}%", f"%{query}%"]

        if filter_available:
            where_clause += " AND available = ?"
            params.append(True)

        sql_query = f"SELECT * FROM books {where_clause}"
        results = await db_manager.execute_query(sql_query, tuple(params))

        books = [Book(**row) for row in results]
        logger.info(f"Encontrados {len(books)} livros para busca: {query}")

        return books

    except Exception as e:
        logger.error(f"Erro ao buscar livros: {e}")
        raise

@mcp.tool()
async def add_book(book_data: Book) -> Book:
    """Adiciona um novo livro à biblioteca"""

    try:
        # Verificar se ISBN já existe
        existing = await db_manager.execute_query(
            "SELECT id FROM books WHERE isbn = ?", (book_data.isbn,)
        )

        if existing:
            raise ValueError(f"Livro com ISBN {book_data.isbn} já existe")

        # Inserir novo livro
        book_id = await db_manager.execute_update(
            "INSERT INTO books (title, author, isbn, available) VALUES (?, ?, ?, ?)",
            (book_data.title, book_data.author, book_data.isbn, book_data.available)
        )

        # Retornar livro com ID
        book_data.id = book_id
        logger.info(f"Livro adicionado: {book_data.title} (ID: {book_id})")

        return book_data

    except Exception as e:
        logger.error(f"Erro ao adicionar livro: {e}")
        raise

@mcp.tool()
async def borrow_book(borrow_request: BorrowRequest) -> Book:
    """Registra empréstimo de um livro"""

    try:
        # Verificar se livro existe e está disponível
        book_data = await db_manager.execute_query(
            "SELECT * FROM books WHERE id = ? AND available = ?",
            (borrow_request.book_id, True)
        )

        if not book_data:
            raise ValueError(f"Livro ID {borrow_request.book_id} não encontrado ou não disponível")

        # Calcular datas
        borrow_date = datetime.now()
        due_date = borrow_date + timedelta(days=borrow_request.borrow_days)

        # Atualizar registro
        await db_manager.execute_update(
            """UPDATE books
               SET available = ?, borrowed_by = ?, borrowed_date = ?, due_date = ?
               WHERE id = ?""",
            (False, borrow_request.borrower_name, borrow_date, due_date, borrow_request.book_id)
        )

        # Retornar livro atualizado
        updated_book = Book(**book_data[0])
        updated_book.available = False
        updated_book.borrowed_by = borrow_request.borrower_name
        updated_book.borrowed_date = borrow_date
        updated_book.due_date = due_date

        logger.info(f"Livro emprestado: ID {borrow_request.book_id} para {borrow_request.borrower_name}")

        return updated_book

    except Exception as e:
        logger.error(f"Erro ao emprestar livro: {e}")
        raise

@mcp.tool()
async def return_book(
    book_id: Annotated[int, "ID do livro a ser devolvido"],
    return_condition: Annotated[str, "Condição do livro na devolução"] = "good"
) -> Book:
    """Processa devolução de um livro"""

    try:
        # Verificar se livro existe e está emprestado
        book_data = await db_manager.execute_query(
            "SELECT * FROM books WHERE id = ? AND available = ?",
            (book_id, False)
        )

        if not book_data:
            raise ValueError(f"Livro ID {book_id} não encontrado ou já disponível")

        # Marcar como disponível
        await db_manager.execute_update(
            """UPDATE books
               SET available = ?, borrowed_by = NULL, borrowed_date = NULL, due_date = NULL
               WHERE id = ?""",
            (True, book_id)
        )

        # Retornar livro atualizado
        updated_book = Book(**book_data[0])
        updated_book.available = True
        updated_book.borrowed_by = None
        updated_book.borrowed_date = None
        updated_book.due_date = None

        logger.info(f"Livro devolvido: ID {book_id} em condição {return_condition}")

        return updated_book

    except Exception as e:
        logger.error(f"Erro ao devolver livro: {e}")
        raise

if __name__ == "__main__":
    # Executar servidor
    mcp.run()
```

### 5. Template Avançado com Recursos

```python
# Gerar template com recursos MCP
template_avancado = fastmcp.gerar_template_com_recursos(
    nome="BibliotecaAdvancedServer",
    recursos=["library_stats", "books_catalog"],
    ferramentas=["search_books", "add_book", "generate_report"],
    authentication=True
)

print("=== TEMPLATE AVANÇADO ===")
print(template_avancado['codigo_recursos'][:500] + "...")
```

**Resultado Esperado:**

```python
=== TEMPLATE AVANÇADO ===

# Recursos MCP para BibliotecaAdvancedServer

@mcp.resource("library_stats")
async def get_library_stats(context: Context) -> str:
    """Fornece estatísticas da biblioteca em formato JSON"""

    # Verificar autenticação
    if not context.is_authenticated:
        raise PermissionError("Acesso a estatísticas requer autenticação")

    try:
        # Buscar estatísticas do banco
        total_books = await db_manager.execute_query(
            "SELECT COUNT(*) as count FROM books"
        )

        available_books = await db_manager.execute_query(
            "SELECT COUNT(*) as count FROM books WHERE available = ?"...
```

## 🔧 Validação e Análise de Código

### 6. Validação de Servidor Existente

```python
# Código de servidor para validação
codigo_servidor = """
from fastmcp import FastMCP

mcp = FastMCP("test-server")

@mcp.tool()
def simple_tool(param: str):
    return f"Hello {param}"

if __name__ == "__main__":
    mcp.run()
"""

# Validar código
validacao = fastmcp.validar_codigo_servidor(codigo_servidor)

print("=== VALIDAÇÃO DO SERVIDOR ===")
print(f"Pontuação: {validacao['score']}/100")
print(f"Status: {validacao['status']}")

print(f"\nProblemas encontrados:")
for problema in validacao['issues']:
    print(f"  🔴 {problema['tipo']}: {problema['descricao']}")
    print(f"     Sugestão: {problema['sugestao']}")

print(f"\nMelhores práticas seguidas:")
for pratica in validacao['good_practices']:
    print(f"  ✅ {pratica}")
```

**Resultado Esperado:**

```
=== VALIDAÇÃO DO SERVIDOR ===
Pontuação: 45/100
Status: Necessita melhorias

Problemas encontrados:
  🔴 CRITICAL: Ausência de documentação no servidor
     Sugestão: Adicionar description e instructions ao FastMCP

  🔴 WARNING: Ferramenta sem type hints adequados
     Sugestão: Usar Annotated para documentar parâmetros

  🔴 WARNING: Ausência de tratamento de erros
     Sugestão: Implementar try/catch e logging

  🔴 INFO: Não usa operações assíncronas
     Sugestão: Considerar async def para operações que podem ser lentas

Melhores práticas seguidas:
  ✅ Usa FastMCP framework
  ✅ Estrutura básica correta
  ✅ Padrão de execução adequado
```

### 7. Otimização de Servidor Existente

```python
# Otimizar servidor com base na validação
servidor_otimizado = fastmcp.otimizar_servidor_existente(
    codigo_original=codigo_servidor,
    aplicar_async=True,
    adicionar_logging=True,
    melhorar_documentacao=True,
    adicionar_validacao=True
)

print("=== SERVIDOR OTIMIZADO ===")
print(servidor_otimizado['codigo_melhorado'])
print(f"\nMelhorias aplicadas: {len(servidor_otimizado['melhorias'])}")
print(f"Nova pontuação estimada: {servidor_otimizado['nova_pontuacao']}/100")
```

**Resultado Esperado:**

```python
=== SERVIDOR OTIMIZADO ===

"""
Test Server - Servidor MCP otimizado
Implementa melhores práticas FastMCP com validação e logging
"""

import asyncio
import logging
from typing import Any
from fastmcp import FastMCP, Context
from pydantic import BaseModel, Field
from typing_extensions import Annotated

# Configuração de logging estruturado
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Inicialização do servidor com documentação completa
mcp = FastMCP(
    name="test-server",
    description="Servidor MCP de demonstração com melhores práticas implementadas",
    instructions="""
    Este servidor demonstra implementação otimizada com FastMCP:
    - Validação de entrada com Pydantic
    - Logging estruturado
    - Tratamento de erros
    - Operações assíncronas quando apropriado
    """,
    dependencies=["fastmcp>=2.0.0", "pydantic>=2.0.0"]
)

# Modelos de validação
class ToolInput(BaseModel):
    """Entrada validada para a ferramenta"""
    param: str = Field(..., min_length=1, max_length=100, description="Parâmetro de entrada")

@mcp.tool()
async def simple_tool(
    param: Annotated[str, "Parâmetro de entrada para processamento"]
) -> str:
    """
    Ferramenta simples que processa um parâmetro de entrada

    Args:
        param: String a ser processada

    Returns:
        String processada com saudação

    Raises:
        ValueError: Se o parâmetro for inválido
    """

    try:
        # Validar entrada
        input_data = ToolInput(param=param)

        # Log da operação
        logger.info(f"Processando parâmetro: {input_data.param}")

        # Simular operação que pode ser assíncrona
        await asyncio.sleep(0.1)

        # Processar e retornar
        result = f"Hello {input_data.param}! Processado com sucesso."
        logger.info(f"Resultado gerado para: {input_data.param}")

        return result

    except Exception as e:
        logger.error(f"Erro ao processar parâmetro '{param}': {str(e)}")
        raise ValueError(f"Erro no processamento: {str(e)}")

if __name__ == "__main__":
    try:
        logger.info("Iniciando Test Server...")
        mcp.run()
    except Exception as e:
        logger.error(f"Erro ao iniciar servidor: {e}")
        raise

Melhorias aplicadas: 8
Nova pontuação estimada: 89/100
```

## 📊 Análise de Performance

### 8. Análise de Performance de Servidor

```python
# Analisar performance de um servidor
analise_performance = fastmcp.analisar_performance_servidor(
    codigo_servidor=servidor_otimizado['codigo_melhorado'],
    simular_carga=True
)

print("=== ANÁLISE DE PERFORMANCE ===")
print(f"Tempo médio de resposta: {analise_performance['response_time']}ms")
print(f"Throughput estimado: {analise_performance['throughput']} req/s")
print(f"Uso de memória: {analise_performance['memory_usage']}MB")
print(f"Pontuação de performance: {analise_performance['performance_score']}/100")

print(f"\nOtimizações recomendadas:")
for otimizacao in analise_performance['optimizations']:
    print(f"  🚀 {otimizacao}")
```

**Resultado Esperado:**

```
=== ANÁLISE DE PERFORMANCE ===
Tempo médio de resposta: 45ms
Throughput estimado: 150 req/s
Uso de memória: 12MB
Pontuação de performance: 78/100

Otimizações recomendadas:
  🚀 Implementar cache em memória para operações frequentes
  🚀 Usar connection pooling para banco de dados
  🚀 Adicionar rate limiting para evitar sobrecarga
  🚀 Considerar processamento em batch para múltiplas operações
  🚀 Implementar compressão de resposta para dados grandes
```

## 🧪 Geração de Testes

### 9. Testes Automatizados

```python
# Gerar testes para servidor
testes_gerados = fastmcp.gerar_testes_servidor(
    codigo_servidor=servidor_otimizado['codigo_melhorado'],
    incluir_testes_carga=True,
    incluir_testes_integracao=True
)

print("=== TESTES GERADOS ===")
print(testes_gerados['test_file_content'][:1000] + "...")
print(f"\nTipos de teste incluídos: {', '.join(testes_gerados['test_types'])}")
print(f"Cobertura estimada: {testes_gerados['estimated_coverage']}%")
```

**Resultado Esperado:**

```python
=== TESTES GERADOS ===

"""
Testes automatizados para Test Server
Gerados pelo FastMCP Assistant
"""

import pytest
import asyncio
from unittest.mock import Mock, patch
from fastmcp.testing import MCPTestClient
from servers.test_server import mcp, simple_tool

class TestSimpleTool:
    """Testes para a ferramenta simple_tool"""

    @pytest.mark.asyncio
    async def test_simple_tool_success(self):
        """Testa operação bem-sucedida"""
        result = await simple_tool("World")
        assert "Hello World" in result
        assert "sucesso" in result

    @pytest.mark.asyncio
    async def test_simple_tool_empty_param(self):
        """Testa parâmetro vazio"""
        with pytest.raises(ValueError):
            await simple_tool("")

    @pytest.mark.asyncio
    async def test_simple_tool_long_param(self):
        """Testa parâmetro muito longo"""
        long_param = "a" * 101
        with pytest.raises(ValueError):
            await simple_tool(long_param)

    @pytest.mark.asyncio
    async def test_simple_tool_special_chars(self):
        """Testa caracteres especiais"""
        result = await simple_tool("Test@123")
        assert "Hello Test@123" in result

class TestServerIntegration:
    """Testes de integração do servidor"""

    def setup_method(self):
        """Setup para cada teste"""
        self.client = MCPTestClient(mcp)

    @pytest.mark.asyncio
    async def test_server_startup(self):
        """Testa inicialização do servidor"""
        assert self.client.server.name == "test-server"
        assert len(self.client.server.tools) > 0

    @pytest.mark.asyncio
    async def test_tool_call_via_client(self):
        """Testa chamada de ferramenta via cliente"""
        response = await self.client.call_tool("simple_tool", {"param": "Integration"})
        assert response.success
        assert "Hello Integration" in response.result

@pytest.mark.load
class TestServerLoad:
    """Testes de carga"""

    @pytest.mark.asyncio
    async def test_concurrent_requests(self):
        """Testa requisições concorrentes"""
        tasks = []
        for i in range(10):
            task = simple_tool(f"User{i}")
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        assert len(results) == 10
        assert all("Hello User" in result for result in results)

    @pytest.mark.asyncio
    async def test_stress_test(self):
        """Teste de estresse básico"""
        start_time = asyncio.get_event_loop().time()

        tasks = [simple_tool(f"Stress{i}") for i in range(100)]
        await asyncio.gather(*tasks)

        end_time = asyncio.get_event_loop().time()
        duration = end_time - start_time

        # Deve completar em menos de 30 segundos
        assert duration < 30.0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])...

Tipos de teste incluídos: unit, integration, load, error_handling
Cobertura estimada: 85%
```

## 🔗 Integração e Workflows

### 10. Workflow Completo de Desenvolvimento

```python
def workflow_desenvolvimento_completo(prompt_inicial):
    """Workflow completo para desenvolvimento de servidor MCP"""

    # 1. Análise inicial do prompt
    analise_inicial = fastmcp.analisar_prompt_mcp(prompt_inicial)

    # 2. Otimização do prompt se necessário
    if analise_inicial.score < 80:
        prompt_otimizado = fastmcp.otimizar_prompt_fastmcp(
            prompt_inicial,
            nivel_detalhe="completo"
        )
        prompt_final = prompt_otimizado['enhanced_prompt']
    else:
        prompt_final = prompt_inicial

    # 3. Extração de requisitos
    requisitos = fastmcp.extrair_requisitos_mcp(prompt_final)

    # 4. Geração do template inicial
    template = fastmcp.gerar_template_servidor(
        nome=requisitos.server_name,
        ferramentas=requisitos.tools,
        usa_banco_dados=requisitos.async_operations,
        async_operations=requisitos.async_operations
    )

    # 5. Validação do código gerado
    validacao = fastmcp.validar_codigo_servidor(template['codigo_servidor'])

    # 6. Otimização se necessário
    if validacao['score'] < 85:
        codigo_otimizado = fastmcp.otimizar_servidor_existente(
            template['codigo_servidor']
        )
        codigo_final = codigo_otimizado['codigo_melhorado']
    else:
        codigo_final = template['codigo_servidor']

    # 7. Geração de testes
    testes = fastmcp.gerar_testes_servidor(codigo_final)

    # 8. Análise de performance
    performance = fastmcp.analisar_performance_servidor(codigo_final)

    return {
        'prompt_original': prompt_inicial,
        'prompt_otimizado': prompt_final,
        'requisitos': requisitos,
        'codigo_servidor': codigo_final,
        'testes': testes,
        'performance': performance,
        'validacao_final': validacao,
        'recomendacoes': performance['optimizations']
    }

# Exemplo de uso
prompt_exemplo = """
Crie um servidor MCP para gerenciar tarefas de um projeto.
Deve permitir criar, listar, atualizar e marcar tarefas como concluídas.
Use SQLite para persistência.
"""

resultado_completo = workflow_desenvolvimento_completo(prompt_exemplo)
print(f"Desenvolvimento concluído! Pontuação final: {resultado_completo['validacao_final']['score']}/100")
```

### 11. Integração com Outros Servidores MCP

```python
def integrar_com_outros_servidores():
    """Exemplo de integração com outros servidores MCP"""

    # 1. Otimizar prompt inicial com Prompt Server
    from servers.prompt_server import PromptEngineer
    prompt_engineer = PromptEngineer()

    prompt_otimizado = prompt_engineer.otimizar_prompt(
        "Crie um servidor MCP para análise de dados",
        task_type="code_generation"
    )

    # 2. Analisar com MCP Server se necessário
    from servers.mcp_server import MCPAnalyzer
    mcp_analyzer = MCPAnalyzer()

    analise_estrutural = mcp_analyzer.analisar_estrutura_projeto(
        prompt_otimizado['optimized_prompt']
    )

    # 3. Aplicar contexto FastMCP
    servidor_mcp = fastmcp.contextualizar_para_fastmcp(
        prompt_otimizado['optimized_prompt'],
        estrutura_recomendada=analise_estrutural
    )

    # 4. Se for desenvolvimento web, aplicar Tailwind
    if 'web' in prompt_otimizado['task_type']:
        from servers.tailwind_server import TailwindContextualizer
        tailwind = TailwindContextualizer()

        servidor_mcp = tailwind.adicionar_contexto_ui(servidor_mcp)

    return servidor_mcp

# Uso da integração
resultado_integrado = integrar_com_outros_servidores()
```

## 📝 Documentação Automática

### 12. Geração de Documentação

```python
# Gerar documentação completa para servidor
documentacao = fastmcp.gerar_documentacao_servidor(
    codigo_servidor=codigo_final,
    incluir_exemplos=True,
    incluir_api_docs=True,
    formato="markdown"
)

print("=== DOCUMENTAÇÃO GERADA ===")
print(documentacao['readme_content'][:800] + "...")
print(f"\nArquivos de documentação: {len(documentacao['doc_files'])}")
```

**Resultado Esperado:**

````markdown
=== DOCUMENTAÇÃO GERADA ===

# Test Server

Servidor MCP otimizado para demonstração de melhores práticas FastMCP.

## 📋 Visão Geral

Este servidor implementa um exemplo simples mas robusto de servidor MCP usando o framework FastMCP, incluindo validação de entrada, logging estruturado, tratamento de erros e operações assíncronas.

## 🚀 Instalação

```bash
pip install fastmcp pydantic
```
````

## 🔧 Configuração

O servidor não requer configuração adicional para uso básico.

## 📖 API Reference

### Ferramentas Disponíveis

#### simple_tool

Ferramenta simples que processa um parâmetro de entrada.

**Parâmetros:**

- `param` (str): Parâmetro de entrada para processamento (1-100 caracteres)

**Retorna:**

- String processada com saudação

**Exemplo:**

```python
result = await simple_tool("World")
# Retorna: "Hello World! Processado com sucesso."
```

**Erros Possíveis:**

- `ValueError`: Parâmetro inválido ou fora dos limites

## 🧪 Testes

```bash
pytest tests/ -v
```

## 📊 Performance

- Tempo médio de resposta: ~45ms
- Throughput: ~150 req/s
- Uso de memória: ~12MB

Arquivos de documentação: 4

```

## 🎯 Casos de Uso Específicos

O FastMCP Server é especialmente útil para:

1. **Desenvolvimento Rápido**: Templates prontos aceleram desenvolvimento
2. **Validação de Qualidade**: Análise automática identifica problemas
3. **Otimização de Performance**: Sugestões específicas para FastMCP
4. **Melhores Práticas**: Aplicação automática de padrões recomendados
5. **Documentação**: Geração automática de docs completas
6. **Testes**: Criação de suites de teste abrangentes

Este servidor é fundamental para desenvolvedores que querem criar servidores MCP de alta qualidade de forma eficiente e seguindo as melhores práticas do framework FastMCP.
```
