#!/usr/bin/env python3
"""
Tests for Elixir Development Server - MCP server for Elixir functional programming.

Tests cover functional patterns, OTP behaviors, and code analysis.
"""

import pytest
from unittest.mock import AsyncMock

try:
    from servers.elixir_server import (
        analyze_elixir_code,
        generate_elixir_project,
        generate_genserver_elixir,
        get_elixir_patterns,
        ElixirKnowledgeBase
    )
    ELIXIR_SERVER_AVAILABLE = True
except ImportError as e:
    print(f"Elixir Server not available: {e}")
    ELIXIR_SERVER_AVAILABLE = False


class TestElixirKnowledgeBase:
    """Tests for Elixir knowledge base"""

    @pytest.mark.skipif(not ELIXIR_SERVER_AVAILABLE, reason="Elixir Server not available")
    def test_genserver_patterns_exist(self):
        """Test that GenServer patterns are defined"""
        kb = ElixirKnowledgeBase()
        assert hasattr(kb, 'GENSERVER_PATTERNS')
        assert "basic" in kb.GENSERVER_PATTERNS

    @pytest.mark.skipif(not ELIXIR_SERVER_AVAILABLE, reason="Elixir Server not available")
    def test_functional_patterns_exist(self):
        """Test that functional patterns are defined"""
        kb = ElixirKnowledgeBase()
        assert hasattr(kb, 'FUNCTIONAL_PATTERNS')
        assert "pipe" in kb.FUNCTIONAL_PATTERNS
        assert "pattern_matching" in kb.FUNCTIONAL_PATTERNS

    @pytest.mark.skipif(not ELIXIR_SERVER_AVAILABLE, reason="Elixir Server not available")
    def test_concurrency_patterns_exist(self):
        """Test that concurrency patterns are defined"""
        kb = ElixirKnowledgeBase()
        assert hasattr(kb, 'CONCURRENCY_PATTERNS')


class TestElixirAnalysisFunctions:
    """Tests for Elixir Server analysis functions"""

    @pytest.mark.skipif(not ELIXIR_SERVER_AVAILABLE, reason="Elixir Server not available")
    @pytest.mark.asyncio
    async def test_analyze_elixir_code_basic(self):
        """Test basic Elixir code analysis"""
        elixir_code = """
        defmodule MyApp.Worker do
          use GenServer

          def start_link(opts) do
            GenServer.start_link(__MODULE__, opts, name: __MODULE__)
          end

          @impl true
          def init(opts), do: {:ok, opts}

          @impl true
          def handle_call(:get, _from, state) do
            {:reply, state, state}
          end
        end
        """

        result = await analyze_elixir_code(elixir_code)

        assert isinstance(result, dict)
        assert "score" in result
        assert 0 <= result["score"] <= 100
        assert "suggestions" in result

    @pytest.mark.skipif(not ELIXIR_SERVER_AVAILABLE, reason="Elixir Server not available")
    @pytest.mark.asyncio
    async def test_analyze_elixir_code_with_pipe(self):
        """Test Elixir code analysis with pipe operator"""
        elixir_code = """
        defmodule MyApp.Transform do
          def process(data) do
            data
            |> Enum.map(&transform/1)
            |> Enum.filter(&valid?/1)
            |> Enum.sort()
          end
        end
        """

        result = await analyze_elixir_code(elixir_code)
        assert result["score"] >= 50  # Pipe usage should boost score

    @pytest.mark.skipif(not ELIXIR_SERVER_AVAILABLE, reason="Elixir Server not available")
    @pytest.mark.asyncio
    async def test_generate_elixir_project(self):
        """Test Elixir project generation"""
        result = await generate_elixir_project(name="TestApp")

        assert isinstance(result, dict)
        assert "project_name" in result
        assert "files" in result
        assert "commands" in result

    @pytest.mark.skipif(not ELIXIR_SERVER_AVAILABLE, reason="Elixir Server not available")
    @pytest.mark.asyncio
    async def test_generate_genserver_elixir(self):
        """Test GenServer module generation"""
        result = await generate_genserver_elixir(name="Worker")

        assert isinstance(result, dict)
        assert "module" in result
        assert "code" in result
        assert "use GenServer" in result["code"]
        assert "@impl true" in result["code"]

    @pytest.mark.skipif(not ELIXIR_SERVER_AVAILABLE, reason="Elixir Server not available")
    @pytest.mark.asyncio
    async def test_get_elixir_patterns_all(self):
        """Test getting all Elixir patterns"""
        result = await get_elixir_patterns()

        assert isinstance(result, dict)
        assert "categories" in result
        assert "functional" in result["categories"]
        assert "genserver" in result["categories"]

    @pytest.mark.skipif(not ELIXIR_SERVER_AVAILABLE, reason="Elixir Server not available")
    @pytest.mark.asyncio
    async def test_get_elixir_patterns_by_category(self):
        """Test getting patterns by category"""
        result = await get_elixir_patterns(category="functional")

        assert isinstance(result, dict)
        assert "category" in result
        assert "patterns" in result


@pytest.fixture
def mock_context():
    """Fixture for mocking Context"""
    context = AsyncMock()
    return context


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
