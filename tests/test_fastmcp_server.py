"""
Testes para o FastMCP Server - Servidor de otimização de prompts MCP

Este módulo testa as funcionalidades do servidor FastMCP especializado
em análise e otimização de prompts para criação de servidores MCP.
"""

import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock
from typing import Dict, Any

# Importações condicionais para fallback
try:
    from servers.fastmcp_server import (
        PromptAnalysis,
        MCPRequirements,
        analyze_mcp_prompt,
        suggest_mcp_prompt_improvements,
        validate_mcp_requirements,
        generate_mcp_server_template,
        get_mcp_best_practices,
        get_prompt_examples,
        get_prompt_frameworks,
        BEST_PRACTICES
    )
    FASTMCP_AVAILABLE = True
except ImportError as e:
    print(f"FastMCP não disponível: {e}")
    FASTMCP_AVAILABLE = False


class TestPromptAnalysis:
    """Testes para a classe PromptAnalysis"""

    @pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
    def test_prompt_analysis_creation(self):
        """Testa criação de instância PromptAnalysis"""
        analysis = PromptAnalysis(
            score=85.5,
            strengths=["Propósito claro", "Boa estrutura"],
            weaknesses=["Falta exemplos"],
            recommendations=["Adicionar exemplos de uso"],
            missing_elements=["Tratamento de erros"]
        )

        assert analysis.score == 85.5
        assert len(analysis.strengths) == 2
        assert len(analysis.weaknesses) == 1
        assert len(analysis.recommendations) == 1
        assert len(analysis.missing_elements) == 1

    @pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
    def test_prompt_analysis_score_validation(self):
        """Testa validação do score (0-100)"""
        # Score válido
        analysis = PromptAnalysis(
            score=50.0,
            strengths=[],
            weaknesses=[],
            recommendations=[]
        )
        assert analysis.score == 50.0

        # Score inválido deve gerar erro
        with pytest.raises(ValueError, match="Score deve estar entre 0 e 100"):
            PromptAnalysis(
                score=150.0,
                strengths=[],
                weaknesses=[],
                recommendations=[]
            )

        with pytest.raises(ValueError, match="Score deve estar entre 0 e 100"):
            PromptAnalysis(
                score=-10.0,
                strengths=[],
                weaknesses=[],
                recommendations=[]
            )


class TestMCPRequirements:
    """Testes para a classe MCPRequirements"""

    @pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
    def test_mcp_requirements_creation(self):
        """Testa criação de MCPRequirements"""
        requirements = MCPRequirements(
            tools=["analyze_data", "export_report"],
            resources=["data://processed"],
            async_operations=True,
            external_apis=["https://api.example.com"],
            authentication=True,
            error_handling=True
        )

        assert len(requirements.tools) == 2
        assert len(requirements.resources) == 1
        assert requirements.async_operations is True
        assert len(requirements.external_apis) == 1
        assert requirements.authentication is True
        assert requirements.error_handling is True

    @pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
    def test_mcp_requirements_defaults(self):
        """Testa valores padrão de MCPRequirements"""
        requirements = MCPRequirements()

        assert requirements.tools == []
        assert requirements.resources == []
        assert requirements.async_operations is False
        assert requirements.external_apis == []
        assert requirements.authentication is False
        assert requirements.error_handling is False


class TestFastMCPAnalysisFunctions:
    """Testes para as funções de análise do FastMCP Server"""

    @pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
    @pytest.mark.asyncio
    async def test_analyze_mcp_prompt_basic(self):
        """Testa análise básica de prompt MCP"""
        # Mock do contexto
        mock_ctx = AsyncMock()

        prompt = """
        Criar um servidor MCP para análise de dados de vendas.
        O servidor deve ter ferramentas para processar arquivos CSV
        e gerar relatórios em JSON. Incluir tratamento de erros
        e exemplos de uso.
        """

        result = await analyze_mcp_prompt(prompt, mock_ctx)

        assert isinstance(result, PromptAnalysis)
        assert 0 <= result.score <= 100
        assert isinstance(result.strengths, list)
        assert isinstance(result.weaknesses, list)
        assert isinstance(result.recommendations, list)

        # Verifica se o contexto foi chamado
        mock_ctx.info.assert_called()

    @pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
    @pytest.mark.asyncio
    async def test_analyze_mcp_prompt_good_quality(self):
        """Testa análise de prompt de boa qualidade"""
        mock_ctx = AsyncMock()

        good_prompt = """
        Objetivo: Criar um servidor MCP para processamento de dados de vendas
        
        Ferramentas necessárias:
        - analyze_sales: processa arquivos CSV com dados de vendas
        - generate_report: gera relatórios em formato JSON
        
        Recursos:
        - data://processed: expõe dados processados
        
        Tipos de entrada: CSV com colunas (date, product, quantity, price)
        Tipos de saída: JSON com estatísticas e insights
        
        Tratamento de erros: validar formato de arquivo e dados
        Operações assíncronas: processamento de arquivos grandes
        
        Exemplo de uso:
        result = await client.call_tool("analyze_sales", {"file": "sales.csv"})
        """

        result = await analyze_mcp_prompt(good_prompt, mock_ctx)

        # Prompt bem estruturado deve ter score alto
        assert result.score >= 70
        assert len(result.strengths) > 0

        # Verifica elementos identificados
        strengths_text = " ".join(result.strengths).lower()
        assert any(keyword in strengths_text for keyword in [
                   "propósito", "exemplo", "detalhado"])

    @pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
    @pytest.mark.asyncio
    async def test_suggest_mcp_prompt_improvements(self):
        """Testa sugestão de melhorias para prompt"""
        mock_ctx = AsyncMock()

        basic_prompt = "Criar servidor MCP para dados"

        result = await suggest_mcp_prompt_improvements(basic_prompt, None, mock_ctx)

        assert isinstance(result, dict)
        assert "improved_prompt" in result
        assert "changes_explanation" in result
        assert "improvement_score" in result
        assert "next_steps" in result

        assert isinstance(result["improved_prompt"], str)
        assert len(result["improved_prompt"]) > len(basic_prompt)
        assert result["improvement_score"] > 0

    @pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
    @pytest.mark.asyncio
    async def test_suggest_improvements_with_focus(self):
        """Testa melhorias com foco específico"""
        mock_ctx = AsyncMock()

        prompt = "Criar servidor MCP básico"

        # Teste com foco técnico
        result_tech = await suggest_mcp_prompt_improvements(prompt, "technical", mock_ctx)
        assert "technical" in result_tech["changes_explanation"][-1].lower()

        # Teste com foco em produção
        result_prod = await suggest_mcp_prompt_improvements(prompt, "production", mock_ctx)
        assert "production" in result_prod["changes_explanation"][-1].lower()

    @pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
    @pytest.mark.asyncio
    async def test_validate_mcp_requirements(self):
        """Testa validação de requisitos MCP"""
        mock_ctx = AsyncMock()

        good_requirements = """
        Propósito: Análise de dados de vendas
        Ferramentas: analyze_data, export_report
        Tipos: CSV input, JSON output
        Tratamento de erros: validação completa
        Exemplos: incluídos na documentação
        Operações assíncronas: sim, para arquivos grandes
        """

        result = await validate_mcp_requirements(good_requirements, mock_ctx)

        assert isinstance(result, dict)
        assert "is_valid" in result
        assert "completeness_score" in result
        assert "issues" in result
        assert "missing_requirements" in result
        assert "suggestions" in result

        # Requisitos completos devem ter score alto
        assert result["completeness_score"] >= 80
        assert result["is_valid"] is True

    @pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
    @pytest.mark.asyncio
    async def test_validate_incomplete_requirements(self):
        """Testa validação de requisitos incompletos"""
        mock_ctx = AsyncMock()

        incomplete_requirements = "Criar algo com dados"

        result = await validate_mcp_requirements(incomplete_requirements, mock_ctx)

        assert result["completeness_score"] < 60
        assert result["is_valid"] is False
        assert len(result["missing_requirements"]) > 0
        assert len(result["suggestions"]) > 0

    @pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
    @pytest.mark.asyncio
    async def test_generate_mcp_server_template(self):
        """Testa geração de templates de servidor"""
        mock_ctx = AsyncMock()

        template_types = ["basic", "api_integration",
                          "data_processing", "production_ready"]

        for server_type in template_types:
            result = await generate_mcp_server_template(
                server_type=server_type,
                name="TestServer",
                description="Servidor de teste",
                ctx=mock_ctx
            )

            assert isinstance(result, str)
            assert len(result) > 100  # Template deve ser substancial
            assert "TestServer" in result
            assert "Servidor de teste" in result

            # Verificar conteúdo específico por tipo
            if server_type == "basic":
                assert "Requisitos Funcionais" in result
            elif server_type == "api_integration":
                assert "APIs Externas" in result
            elif server_type == "data_processing":
                assert "Processamento de Dados" in result
            elif server_type == "production_ready":
                assert "Produção Completos" in result


class TestFastMCPResources:
    """Testes para os recursos do FastMCP Server"""

    @pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
    @pytest.mark.asyncio
    async def test_get_mcp_best_practices(self):
        """Testa obtenção de melhores práticas"""
        result = await get_mcp_best_practices()

        assert isinstance(result, dict)
        assert "structure" in result
        assert "technical" in result
        assert "production" in result

        # Verifica se as práticas são as mesmas da constante
        assert result == BEST_PRACTICES

    @pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
    @pytest.mark.asyncio
    async def test_get_prompt_examples(self):
        """Testa obtenção de exemplos de prompts"""
        quality_levels = ["bad", "good", "excellent"]

        for level in quality_levels:
            result = await get_prompt_examples(level)

            assert isinstance(result, dict)
            assert "prompt" in result

            if level == "bad":
                assert "issues" in result
            elif level in ["good", "excellent"]:
                assert "strengths" in result

    @pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
    @pytest.mark.asyncio
    async def test_get_prompt_examples_invalid_level(self):
        """Testa exemplo com nível inválido"""
        result = await get_prompt_examples("invalid")

        assert "error" in result
        assert "não encontrado" in result["error"]

    @pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
    @pytest.mark.asyncio
    async def test_get_prompt_frameworks(self):
        """Testa obtenção de frameworks de prompt engineering"""
        result = await get_prompt_frameworks()

        assert isinstance(result, dict)
        assert "frameworks" in result
        assert "recommendation" in result

        frameworks = result["frameworks"]
        assert "CRISP" in frameworks
        assert "STAR" in frameworks
        assert "Chain-of-Thought" in frameworks

        # Verifica estrutura dos frameworks
        for framework_name, framework_data in frameworks.items():
            assert "name" in framework_data
            assert "description" in framework_data
            assert "application" in framework_data
            assert "template" in framework_data


class TestFastMCPIntegration:
    """Testes de integração do FastMCP Server"""

    @pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
    @pytest.mark.asyncio
    async def test_full_workflow_prompt_optimization(self):
        """Testa workflow completo de otimização de prompt"""
        mock_ctx = AsyncMock()

        # 1. Prompt inicial simples
        initial_prompt = "Fazer servidor para arquivos"

        # 2. Analisar prompt inicial
        analysis = await analyze_mcp_prompt(initial_prompt, mock_ctx)
        initial_score = analysis.score

        # 3. Sugerir melhorias
        improvements = await suggest_mcp_prompt_improvements(initial_prompt, None, mock_ctx)
        improved_prompt = improvements["improved_prompt"]

        # 4. Analisar prompt melhorado
        improved_analysis = await analyze_mcp_prompt(improved_prompt, mock_ctx)
        improved_score = improved_analysis.score

        # 5. Validar que houve melhoria
        assert improved_score > initial_score
        assert len(improved_prompt) > len(initial_prompt)
        assert len(improved_analysis.strengths) >= len(analysis.strengths)

    @pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
    @pytest.mark.asyncio
    async def test_template_generation_and_validation(self):
        """Testa geração de template e validação"""
        mock_ctx = AsyncMock()

        # 1. Gerar template
        template = await generate_mcp_server_template(
            server_type="basic",
            name="DataProcessor",
            description="Processamento de dados",
            ctx=mock_ctx
        )

        # 2. Validar o template gerado
        validation = await validate_mcp_requirements(template, mock_ctx)

        # 3. Template gerado deve ser válido
        assert validation["is_valid"] is True
        assert validation["completeness_score"] >= 70


# Testes de fallback quando FastMCP não está disponível
@pytest.mark.skipif(FASTMCP_AVAILABLE, reason="FastMCP está disponível")
def test_fastmcp_server_fallback():
    """Teste de fallback quando FastMCP não está disponível"""
    # Este teste roda quando FastMCP não está disponível
    assert not FASTMCP_AVAILABLE
    print("⚠️ FastMCP Server não está disponível - implementação pendente")


# Fixture para mock de contexto
@pytest.fixture
def mock_context():
    """Fixture para criar mock de Context do FastMCP"""
    context = AsyncMock()
    context.info = AsyncMock()
    context.warning = AsyncMock()
    context.error = AsyncMock()
    return context


# Testes parametrizados para diferentes tipos de prompt
@pytest.mark.skipif(not FASTMCP_AVAILABLE, reason="FastMCP não disponível")
@pytest.mark.parametrize("prompt_content,expected_min_score", [
    ("Criar servidor MCP", 0.5),  # Prompt muito básico
    ("Criar servidor MCP com ferramentas para processar dados", 25),  # Prompt simples
    # Prompt médio
    ("Criar servidor MCP com ferramentas específicas, recursos definidos e exemplos", 35),
    ("""Criar servidor MCP para análise de dados
    Ferramentas: analyze_data, export_report
    Recursos: data://processed
    Tipos: CSV input, JSON output
    Tratamento de erros: validação completa
    Exemplos incluídos""", 65),  # Prompt completo
])
@pytest.mark.asyncio
async def test_analyze_prompt_scores(prompt_content, expected_min_score, mock_context):
    """Testa que diferentes qualidades de prompt resultam em scores apropriados"""
    result = await analyze_mcp_prompt(prompt_content, mock_context)
    assert result.score >= expected_min_score


if __name__ == "__main__":
    # Execução direta para desenvolvimento
    pytest.main([__file__, "-v"])
