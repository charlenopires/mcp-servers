#!/usr/bin/env python3
"""
Tests for HTMX + Axum Server - MCP server for HTMX with Rust backend.

Tests cover HTMX attributes, Axum handlers, and integration patterns.
"""

import pytest
from unittest.mock import AsyncMock

try:
    from servers.htmx_server import (
        analyze_htmx_code,
        generate_htmx_component,
        generate_axum_handler,
        get_htmx_patterns,
        optimize_htmx_requests,
        HtmxKnowledgeBase
    )
    HTMX_SERVER_AVAILABLE = True
except ImportError as e:
    print(f"HTMX Server not available: {e}")
    HTMX_SERVER_AVAILABLE = False


class TestHtmxKnowledgeBase:
    """Tests for HTMX knowledge base"""

    @pytest.mark.skipif(not HTMX_SERVER_AVAILABLE, reason="HTMX Server not available")
    def test_request_attributes_exist(self):
        """Test that request attributes are defined"""
        kb = HtmxKnowledgeBase()
        assert hasattr(kb, 'REQUEST_ATTRIBUTES')

    @pytest.mark.skipif(not HTMX_SERVER_AVAILABLE, reason="HTMX Server not available")
    def test_swap_patterns_exist(self):
        """Test that swap patterns are defined"""
        kb = HtmxKnowledgeBase()
        assert hasattr(kb, 'SWAP_PATTERNS')

    @pytest.mark.skipif(not HTMX_SERVER_AVAILABLE, reason="HTMX Server not available")
    def test_axum_patterns_exist(self):
        """Test that Axum patterns are defined"""
        kb = HtmxKnowledgeBase()
        assert hasattr(kb, 'AXUM_PATTERNS')

    @pytest.mark.skipif(not HTMX_SERVER_AVAILABLE, reason="HTMX Server not available")
    def test_ui_patterns_exist(self):
        """Test that UI patterns are defined"""
        kb = HtmxKnowledgeBase()
        assert hasattr(kb, 'UI_PATTERNS')


class TestHtmxAnalysisFunctions:
    """Tests for HTMX Server analysis functions"""

    @pytest.mark.skipif(not HTMX_SERVER_AVAILABLE, reason="HTMX Server not available")
    @pytest.mark.asyncio
    async def test_analyze_htmx_code_basic(self):
        """Test basic HTMX code analysis"""
        htmx_code = """
        <button hx-get="/api/users" hx-target="#users-list" hx-swap="innerHTML">
            Load Users
        </button>
        <div id="users-list"></div>
        """

        result = await analyze_htmx_code(htmx_code)

        assert isinstance(result, dict)
        assert "score" in result
        assert 0 <= result["score"] <= 100
        assert "suggestions" in result

    @pytest.mark.skipif(not HTMX_SERVER_AVAILABLE, reason="HTMX Server not available")
    @pytest.mark.asyncio
    async def test_analyze_htmx_code_advanced(self):
        """Test HTMX code analysis with advanced patterns"""
        htmx_code = """
        <form hx-post="/api/users" hx-target="#result" hx-swap="outerHTML"
              hx-indicator="#spinner" hx-confirm="Are you sure?">
            <input name="name" required>
            <button type="submit">Submit</button>
        </form>
        <div id="spinner" class="htmx-indicator">Loading...</div>
        """

        result = await analyze_htmx_code(htmx_code)
        assert result["score"] >= 60  # Advanced patterns should boost score

    @pytest.mark.skipif(not HTMX_SERVER_AVAILABLE, reason="HTMX Server not available")
    @pytest.mark.asyncio
    async def test_generate_htmx_component(self):
        """Test HTMX component generation"""
        result = await generate_htmx_component(
            component_type="list",
            endpoint="/api/items"
        )

        assert isinstance(result, dict)
        assert "html" in result
        assert "hx-" in result["html"]

    @pytest.mark.skipif(not HTMX_SERVER_AVAILABLE, reason="HTMX Server not available")
    @pytest.mark.asyncio
    async def test_generate_axum_handler(self):
        """Test Axum handler generation for HTMX"""
        result = await generate_axum_handler(
            method="get",
            path="/users",
            response_type="html"
        )

        assert isinstance(result, dict)
        assert "code" in result
        assert "async fn" in result["code"]
        assert "Html" in result["code"] or "html" in result["code"].lower()

    @pytest.mark.skipif(not HTMX_SERVER_AVAILABLE, reason="HTMX Server not available")
    @pytest.mark.asyncio
    async def test_optimize_htmx_requests(self):
        """Test HTMX request optimization"""
        original_code = """
        <div hx-get="/api/data" hx-trigger="load">
            Loading...
        </div>
        """

        result = await optimize_htmx_requests(original_code)

        assert isinstance(result, dict)
        assert "optimized_code" in result
        assert "improvements" in result

    @pytest.mark.skipif(not HTMX_SERVER_AVAILABLE, reason="HTMX Server not available")
    @pytest.mark.asyncio
    async def test_get_htmx_patterns_all(self):
        """Test getting all HTMX patterns"""
        result = await get_htmx_patterns()

        assert isinstance(result, dict)
        assert "categories" in result
        assert "request" in result["categories"] or "attributes" in result["categories"]

    @pytest.mark.skipif(not HTMX_SERVER_AVAILABLE, reason="HTMX Server not available")
    @pytest.mark.asyncio
    async def test_get_htmx_patterns_by_category(self):
        """Test getting patterns by category"""
        result = await get_htmx_patterns(category="swap")

        assert isinstance(result, dict)
        assert "category" in result
        assert "patterns" in result


class TestHtmxAxumIntegration:
    """Tests for HTMX and Axum integration"""

    @pytest.mark.skipif(not HTMX_SERVER_AVAILABLE, reason="HTMX Server not available")
    @pytest.mark.asyncio
    async def test_full_stack_generation(self):
        """Test generating both HTMX component and Axum handler"""
        # Generate HTMX component
        htmx_result = await generate_htmx_component(
            component_type="form",
            endpoint="/api/submit"
        )

        # Generate Axum handler
        axum_result = await generate_axum_handler(
            method="post",
            path="/api/submit",
            response_type="html"
        )

        assert "html" in htmx_result
        assert "code" in axum_result


@pytest.fixture
def mock_context():
    """Fixture for mocking Context"""
    context = AsyncMock()
    return context


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
