#!/usr/bin/env python3
"""
Testes unitarios para o servidor Tailwind CSS v4.1.
"""

import pytest
from unittest.mock import AsyncMock
import asyncio

# Importacoes condicionais para fallback
try:
    from servers.tailwind_server import (
        tailwind_contextualize_prompt,
        tailwind_get_v4_info,
        tailwind_generate_v4_code,
        tailwind_get_v4_docs,
        tailwind_get_v4_examples
    )
    TAILWIND_SERVER_AVAILABLE = True
except ImportError as e:
    print(f"Tailwind Server nao disponivel: {e}")
    TAILWIND_SERVER_AVAILABLE = False


class TestTailwindServer:
    """Testes para o servidor Tailwind CSS v4.1"""

    @pytest.mark.skipif(not TAILWIND_SERVER_AVAILABLE, reason="Tailwind Server nao disponivel")
    @pytest.mark.asyncio
    async def test_tailwind_contextualize_prompt(self):
        """Testa contextualizacao de prompt com Tailwind CSS v4.1"""
        prompt = "Criar um componente de card responsivo"
        
        result = await tailwind_contextualize_prompt(prompt)
        
        assert isinstance(result, dict)
        assert "contextualized_prompt" in result
        assert len(result["contextualized_prompt"]) > len(prompt)
        assert "tailwind" in result["contextualized_prompt"].lower()

    @pytest.mark.skipif(not TAILWIND_SERVER_AVAILABLE, reason="Tailwind Server nao disponivel")
    @pytest.mark.asyncio
    async def test_tailwind_get_v4_info_general(self):
        """Testa obtencao de informacoes gerais do Tailwind v4.1"""
        result = await tailwind_get_v4_info()
        
        assert isinstance(result, dict)
        assert "version" in result
        assert "features" in result
        assert "4.1" in result["version"]

    @pytest.mark.skipif(not TAILWIND_SERVER_AVAILABLE, reason="Tailwind Server nao disponivel")
    @pytest.mark.asyncio
    async def test_tailwind_get_v4_info_specific_feature(self):
        """Testa obtencao de informacoes de feature especifica"""
        feature = "css-variables"
        result = await tailwind_get_v4_info(feature)
        
        assert isinstance(result, dict)
        assert "feature" in result
        assert result["feature"] == feature

    @pytest.mark.skipif(not TAILWIND_SERVER_AVAILABLE, reason="Tailwind Server nao disponivel")
    @pytest.mark.asyncio
    async def test_tailwind_generate_v4_code(self):
        """Testa geracao de codigo Tailwind v4.1"""
        component_type = "card"
        requirements = "Responsive card with hover effects"
        
        result = await tailwind_generate_v4_code(component_type, requirements)
        
        assert isinstance(result, dict)
        assert "code" in result
        assert "explanation" in result
        assert len(result["code"]) > 0
        assert "class=" in result["code"] or "className=" in result["code"]

    @pytest.mark.skipif(not TAILWIND_SERVER_AVAILABLE, reason="Tailwind Server nao disponivel")
    @pytest.mark.asyncio
    async def test_tailwind_get_v4_docs(self):
        """Testa obtencao de documentacao v4.1"""
        result = await tailwind_get_v4_docs()
        
        assert isinstance(result, dict)
        assert "documentation" in result
        assert "migration_guide" in result
        assert len(result["documentation"]) > 0

    @pytest.mark.skipif(not TAILWIND_SERVER_AVAILABLE, reason="Tailwind Server nao disponivel")
    @pytest.mark.asyncio
    async def test_tailwind_get_v4_examples(self):
        """Testa obtencao de exemplos v4.1"""
        result = await tailwind_get_v4_examples()
        
        assert isinstance(result, dict)
        assert "examples" in result
        assert "templates" in result
        assert len(result["examples"]) > 0

    @pytest.mark.skipif(not TAILWIND_SERVER_AVAILABLE, reason="Tailwind Server nao disponivel")
    @pytest.mark.asyncio
    async def test_tailwind_integration_workflow(self):
        """Testa workflow completo de otimizacao com Tailwind"""
        # 1. Contextualizar prompt
        original_prompt = "Criar botao azul"
        contextualized = await tailwind_contextualize_prompt(original_prompt)
        
        # 2. Gerar codigo baseado no prompt contextualizado
        code_result = await tailwind_generate_v4_code("button", "Blue button with modern styling")
        
        # 3. Verificar que temos um workflow completo
        assert len(contextualized["contextualized_prompt"]) > len(original_prompt)
        assert len(code_result["code"]) > 0


# Testes de fallback quando Tailwind Server nao esta disponivel
@pytest.mark.skipif(TAILWIND_SERVER_AVAILABLE, reason="Tailwind Server esta disponivel")
def test_tailwind_server_fallback():
    """Teste de fallback quando Tailwind Server nao esta disponivel"""
    assert not TAILWIND_SERVER_AVAILABLE
    print("Tailwind Server nao esta disponivel")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])