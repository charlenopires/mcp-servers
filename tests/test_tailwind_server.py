#!/usr/bin/env python3
"""
Unit tests for the Tailwind CSS v4.1 server.
"""

import pytest
from unittest.mock import AsyncMock

# Conditional imports for fallback
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
    print(f"Tailwind Server not available: {e}")
    TAILWIND_SERVER_AVAILABLE = False


class TestTailwindServer:
    """Tests for the Tailwind CSS v4.1 server"""

    @pytest.mark.skipif(not TAILWIND_SERVER_AVAILABLE, reason="Tailwind Server not available")
    @pytest.mark.asyncio
    async def test_tailwind_contextualize_prompt(self):
        """Test prompt contextualization with Tailwind CSS v4.1"""
        # Prompt must mention tailwind to be contextualized
        prompt = "Create a responsive card component with tailwind css"

        # Use .fn to access the underlying function
        result = await tailwind_contextualize_prompt.fn(prompt)

        assert isinstance(result, dict)
        assert "contextualized_prompt" in result
        assert result["contextualized"] is True

    @pytest.mark.skipif(not TAILWIND_SERVER_AVAILABLE, reason="Tailwind Server not available")
    @pytest.mark.asyncio
    async def test_tailwind_get_v4_info_general(self):
        """Test getting general Tailwind v4.1 info"""
        # Use .fn to access the underlying function
        result = await tailwind_get_v4_info.fn()

        assert isinstance(result, dict)
        assert "version" in result or "features" in result or "overview" in result

    @pytest.mark.skipif(not TAILWIND_SERVER_AVAILABLE, reason="Tailwind Server not available")
    @pytest.mark.asyncio
    async def test_tailwind_get_v4_info_specific_feature(self):
        """Test getting info for a specific feature"""
        feature = "css-variables"
        # Use .fn to access the underlying function
        result = await tailwind_get_v4_info.fn(feature)

        assert isinstance(result, dict)

    @pytest.mark.skipif(not TAILWIND_SERVER_AVAILABLE, reason="Tailwind Server not available")
    @pytest.mark.asyncio
    async def test_tailwind_generate_v4_code(self):
        """Test Tailwind v4.1 code generation"""
        component_type = "card"
        requirements = "Responsive card with hover effects"

        # Use .fn to access the underlying function
        result = await tailwind_generate_v4_code.fn(component_type, requirements)

        assert isinstance(result, dict)
        assert "code" in result or "html" in result or "component" in result

    @pytest.mark.skipif(not TAILWIND_SERVER_AVAILABLE, reason="Tailwind Server not available")
    @pytest.mark.asyncio
    async def test_tailwind_get_v4_docs(self):
        """Test getting v4.1 documentation"""
        # Use .fn to access the underlying function
        result = await tailwind_get_v4_docs.fn()

        assert isinstance(result, dict)
        assert len(result) > 0

    @pytest.mark.skipif(not TAILWIND_SERVER_AVAILABLE, reason="Tailwind Server not available")
    @pytest.mark.asyncio
    async def test_tailwind_get_v4_examples(self):
        """Test getting v4.1 examples"""
        # Use .fn to access the underlying function
        result = await tailwind_get_v4_examples.fn()

        assert isinstance(result, dict)
        assert len(result) > 0

    @pytest.mark.skipif(not TAILWIND_SERVER_AVAILABLE, reason="Tailwind Server not available")
    @pytest.mark.asyncio
    async def test_tailwind_integration_workflow(self):
        """Test complete Tailwind optimization workflow"""
        # 1. Contextualize prompt (must mention tailwind)
        original_prompt = "Create blue button with tailwind"
        contextualized = await tailwind_contextualize_prompt.fn(original_prompt)

        # 2. Generate code based on contextualized prompt
        code_result = await tailwind_generate_v4_code.fn("button", "Blue button with modern styling")

        # 3. Verify we have a complete workflow
        assert contextualized["contextualized"] is True
        assert "contextualized_prompt" in contextualized
        assert code_result is not None


# Fallback tests when Tailwind Server is not available
@pytest.mark.skipif(TAILWIND_SERVER_AVAILABLE, reason="Tailwind Server is available")
def test_tailwind_server_fallback():
    """Fallback test when Tailwind Server is not available"""
    assert not TAILWIND_SERVER_AVAILABLE
    print("Tailwind Server is not available")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
