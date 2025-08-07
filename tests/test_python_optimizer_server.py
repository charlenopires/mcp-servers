#!/usr/bin/env python3
"""
Testes para o Python Development Optimizer Server - Servidor MCP para otimização de desenvolvimento Python

Este módulo testa as funcionalidades do servidor Python especializado em análise de prompts,
geração de templates, validação de código e sugestões de refatoração.
"""

import pytest
from unittest.mock import AsyncMock

# Importações condicionais para fallback
try:
    from servers.python_optimizer_server import (
        analyze_python_prompt,
        enhance_python_prompt,
        generate_python_template,
        validate_python_code,
        suggest_refactoring,
        get_python_best_practices
    )
    PYTHON_SERVER_AVAILABLE = True
except ImportError as e:
    print(f"Python Optimizer Server não disponível: {e}")
    PYTHON_SERVER_AVAILABLE = False


class TestPythonAnalysisFunctions:
    """Testes para as funções de análise do Python Server"""

    @pytest.mark.skipif(not PYTHON_SERVER_AVAILABLE, reason="Python Server não disponível")
    @pytest.mark.asyncio
    async def test_analyze_python_prompt_basic(self):
        """Testa análise básica de prompt Python"""
        prompt = "Criar um script Python para processar arquivos CSV"

        result = await analyze_python_prompt(prompt)

        assert isinstance(result, dict)
        assert "score" in result
        assert "strengths" in result
        assert "weaknesses" in result
        assert "recommendations" in result
        assert 0 <= result["score"] <= 100

    @pytest.mark.skipif(not PYTHON_SERVER_AVAILABLE, reason="Python Server não disponível")
    @pytest.mark.asyncio
    async def test_analyze_python_prompt_comprehensive(self):
        """Testa análise de prompt Python abrangente"""
        comprehensive_prompt = """
        Criar uma aplicação Python para análise de dados com:
        - Paradigma orientado a objetos
        - Type hints completos
        - Tratamento de exceções robusto
        - Documentação com docstrings
        - Testes unitários com pytest
        - Logging estruturado
        - Validação de entrada com Pydantic
        - Conformidade com PEP 8 e Clean Code
        """

        result = await analyze_python_prompt(comprehensive_prompt)

        # Prompt abrangente deve ter score alto
        assert result["score"] >= 70
        assert len(result["strengths"]) > 0

        # Verificar elementos identificados
        strengths_text = " ".join(result["strengths"]).lower()
        assert any(keyword in strengths_text for keyword in [
            "type hints", "testing", "documentation", "pep 8"
        ])

    @pytest.mark.skipif(not PYTHON_SERVER_AVAILABLE, reason="Python Server não disponível")
    @pytest.mark.asyncio
    async def test_enhance_python_prompt(self):
        """Testa melhoria de prompt Python"""
        basic_prompt = "Fazer um script para dados"

        result = await enhance_python_prompt(
            prompt=basic_prompt,
            paradigm="object_oriented",
            complexity="production"
        )

        assert isinstance(result, dict)
        assert "enhanced_prompt" in result
        assert "improvements" in result
        assert "technical_requirements" in result

        enhanced = result["enhanced_prompt"]
        assert len(enhanced) > len(basic_prompt)
        assert any(keyword in enhanced.lower() for keyword in [
            "class", "type hints", "exception", "test"
        ])

    @pytest.mark.skipif(not PYTHON_SERVER_AVAILABLE, reason="Python Server não disponível")
    @pytest.mark.asyncio
    async def test_generate_python_template(self):
        """Testa geração de template Python"""
        template_types = ["script", "package",
                          "web_api", "data_analysis", "cli_tool"]

        for template_type in template_types:
            result = await generate_python_template(
                template_type=template_type,
                name="TestProject",
                paradigm="object_oriented",
                include_tests=True
            )

            assert isinstance(result, dict)
            assert "main_code" in result
            assert "structure" in result
            assert "dependencies" in result
            assert "documentation" in result

            # Verificar código principal
            main_code = result["main_code"]
            assert len(main_code) > 0
            assert "def " in main_code or "class " in main_code

            # Verificar estrutura do projeto
            structure = result["structure"]
            assert isinstance(structure, dict)
            if template_type == "package":
                assert "__init__.py" in str(structure)

    @pytest.mark.skipif(not PYTHON_SERVER_AVAILABLE, reason="Python Server não disponível")
    @pytest.mark.asyncio
    async def test_validate_python_code(self):
        """Testa validação de código Python"""
        code_samples = [
            # Código básico
            """
def hello():
    print("Hello World")
            """,
            # Código com type hints
            """
from typing import List

def process_items(items: List[str]) -> List[str]:
    \"\"\"Processa lista de itens.\"\"\"
    return [item.upper() for item in items]
            """,
            # Código com classe
            """
class DataProcessor:
    \"\"\"Processador de dados.\"\"\"
    
    def __init__(self, data: dict) -> None:
        self.data = data
    
    def process(self) -> dict:
        \"\"\"Processa os dados.\"\"\"
        return self.data
            """
        ]

        for code in code_samples:
            result = await validate_python_code(code)

            assert isinstance(result, dict)
            assert "is_valid" in result
            assert "score" in result
            assert "issues" in result
            assert "suggestions" in result

    @pytest.mark.skipif(not PYTHON_SERVER_AVAILABLE, reason="Python Server não disponível")
    @pytest.mark.asyncio
    async def test_suggest_refactoring(self):
        """Testa sugestões de refatoração"""
        legacy_code = """
def process_data(data):
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
    return result
        """

        result = await suggest_refactoring(
            code=legacy_code,
            focus_areas=["type_hints", "comprehensions", "documentation"]
        )

        assert isinstance(result, dict)
        assert "refactored_code" in result
        assert "improvements" in result
        assert "explanation" in result

        refactored = result["refactored_code"]
        # Código refatorado deve incluir melhorias
        assert "List[" in refactored or "list[" in refactored  # Type hints
        assert '"""' in refactored or "'''" in refactored  # Documentação

    @pytest.mark.skipif(not PYTHON_SERVER_AVAILABLE, reason="Python Server não disponível")
    @pytest.mark.asyncio
    async def test_get_python_best_practices(self):
        """Testa obtenção de melhores práticas Python"""
        result = await get_python_best_practices()

        assert isinstance(result, dict)
        assert "coding_standards" in result
        assert "type_safety" in result
        assert "testing" in result
        assert "documentation" in result

        # Verificar que cada categoria tem práticas
        for category, practices in result.items():
            assert isinstance(practices, list)
            assert len(practices) > 0


class TestPythonIntegration:
    """Testes de integração do Python Server"""

    @pytest.mark.skipif(not PYTHON_SERVER_AVAILABLE, reason="Python Server não disponível")
    @pytest.mark.asyncio
    async def test_full_development_workflow(self):
        """Testa workflow completo de desenvolvimento Python"""
        # 1. Prompt inicial simples
        initial_prompt = "Fazer script para CSV"

        # 2. Analisar prompt inicial
        analysis = await analyze_python_prompt(initial_prompt)
        initial_score = analysis["score"]

        # 3. Melhorar prompt
        enhancement = await enhance_python_prompt(
            prompt=initial_prompt,
            paradigm="object_oriented",
            complexity="production"
        )
        enhanced_prompt = enhancement["enhanced_prompt"]

        # 4. Analisar prompt melhorado
        enhanced_analysis = await analyze_python_prompt(enhanced_prompt)
        enhanced_score = enhanced_analysis["score"]

        # 5. Gerar template baseado no prompt melhorado
        template = await generate_python_template(
            template_type="script",
            name="CSVProcessor",
            paradigm="object_oriented",
            include_tests=True
        )

        # 6. Validar código gerado
        validation = await validate_python_code(template["main_code"])

        # Verificar melhoria ao longo do workflow
        assert enhanced_score > initial_score
        assert len(enhanced_prompt) > len(initial_prompt)
        assert validation["is_valid"] is True
        assert validation["score"] >= 70

    @pytest.mark.skipif(not PYTHON_SERVER_AVAILABLE, reason="Python Server não disponível")
    @pytest.mark.asyncio
    async def test_code_improvement_cycle(self):
        """Testa ciclo de melhoria de código"""
        # Código legado sem padrões modernos
        legacy_code = """
def calc(x, y):
    if x > 0:
        return x + y
    else:
        return 0
        """

        # Validar código legado
        legacy_validation = await validate_python_code(legacy_code)
        legacy_score = legacy_validation["score"]

        # Refatorar código
        refactoring = await suggest_refactoring(
            code=legacy_code,
            focus_areas=["type_hints", "documentation", "error_handling"]
        )

        # Validar código refatorado
        refactored_validation = await validate_python_code(refactoring["refactored_code"])
        refactored_score = refactored_validation["score"]

        # Código refatorado deve ter score melhor
        assert refactored_score > legacy_score
        assert len(refactoring["improvements"]) > 0


# Testes parametrizados para diferentes cenários
@pytest.mark.skipif(not PYTHON_SERVER_AVAILABLE, reason="Python Server não disponível")
@pytest.mark.parametrize("prompt_content,expected_min_score", [
    ("Fazer script", 10),  # Prompt muito básico
    ("Criar script Python para processar dados", 30),  # Prompt simples
    ("Criar aplicação Python OO com type hints e testes", 60),  # Prompt médio
    ("""Criar aplicação Python profissional com:
    - Paradigma orientado a objetos
    - Type hints completos
    - Tratamento de exceções
    - Testes unitários
    - Documentação
    - Conformidade PEP 8""", 80),  # Prompt completo
])
@pytest.mark.asyncio
async def test_analyze_prompt_quality_levels(prompt_content, expected_min_score):
    """Testa que diferentes qualidades de prompt resultam em scores apropriados"""
    result = await analyze_python_prompt(prompt_content)
    assert result["score"] >= expected_min_score


@pytest.mark.skipif(not PYTHON_SERVER_AVAILABLE, reason="Python Server não disponível")
@pytest.mark.parametrize("template_type", [
    "script", "package", "web_api", "data_analysis", "cli_tool"
])
@pytest.mark.asyncio
async def test_generate_all_template_types(template_type):
    """Testa geração de todos os tipos de template"""
    result = await generate_python_template(
        template_type=template_type,
        name="TestProject",
        paradigm="object_oriented"
    )

    assert isinstance(result, dict)
    assert "main_code" in result
    assert "structure" in result
    assert len(result["main_code"]) > 0


# Teste de fallback quando Python Server não está disponível
@pytest.mark.skipif(PYTHON_SERVER_AVAILABLE, reason="Python Server está disponível")
def test_python_server_fallback():
    """Teste de fallback quando Python Server não está disponível"""
    assert not PYTHON_SERVER_AVAILABLE
    print("⚠️ Python Optimizer Server não está disponível - implementação pendente")


# Fixture para mock de contexto
@pytest.fixture
def mock_context():
    """Fixture para criar mock de Context do Python Server"""
    context = AsyncMock()
    context.info = AsyncMock()
    context.warning = AsyncMock()
    context.error = AsyncMock()
    return context


if __name__ == "__main__":
    # Execução direta para desenvolvimento
    pytest.main([__file__, "-v"])
