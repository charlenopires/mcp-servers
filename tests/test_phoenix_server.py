#!/usr/bin/env python3
"""
Tests for Phoenix Framework Server - MCP server for Phoenix web development.

Tests cover controllers, routing, contexts, and plugs.
"""

import pytest
from unittest.mock import AsyncMock

try:
    from servers.phoenix_server import (
        analyze_phoenix_code,
        generate_phoenix_resource,
        generate_context,
        get_phoenix_patterns,
        PhoenixKnowledgeBase
    )
    PHOENIX_SERVER_AVAILABLE = True
except ImportError as e:
    print(f"Phoenix Server not available: {e}")
    PHOENIX_SERVER_AVAILABLE = False


class TestPhoenixKnowledgeBase:
    """Tests for Phoenix knowledge base"""

    @pytest.mark.skipif(not PHOENIX_SERVER_AVAILABLE, reason="Phoenix Server not available")
    def test_controller_patterns_exist(self):
        """Test that controller patterns are defined"""
        kb = PhoenixKnowledgeBase()
        assert hasattr(kb, 'CONTROLLER_PATTERNS')
        assert "basic" in kb.CONTROLLER_PATTERNS
        assert "api" in kb.CONTROLLER_PATTERNS

    @pytest.mark.skipif(not PHOENIX_SERVER_AVAILABLE, reason="Phoenix Server not available")
    def test_router_patterns_exist(self):
        """Test that router patterns are defined"""
        kb = PhoenixKnowledgeBase()
        assert hasattr(kb, 'ROUTER_PATTERNS')
        assert "basic" in kb.ROUTER_PATTERNS

    @pytest.mark.skipif(not PHOENIX_SERVER_AVAILABLE, reason="Phoenix Server not available")
    def test_context_patterns_exist(self):
        """Test that context patterns are defined"""
        kb = PhoenixKnowledgeBase()
        assert hasattr(kb, 'CONTEXT_PATTERNS')


class TestPhoenixAnalysisFunctions:
    """Tests for Phoenix Server analysis functions"""

    @pytest.mark.skipif(not PHOENIX_SERVER_AVAILABLE, reason="Phoenix Server not available")
    @pytest.mark.asyncio
    async def test_analyze_phoenix_code_basic(self):
        """Test basic Phoenix code analysis"""
        phoenix_code = """
        defmodule MyAppWeb.UserController do
          use MyAppWeb, :controller

          alias MyApp.Accounts

          def index(conn, _params) do
            users = Accounts.list_users()
            render(conn, :index, users: users)
          end

          def show(conn, %{"id" => id}) do
            user = Accounts.get_user!(id)
            render(conn, :show, user: user)
          end
        end
        """

        result = await analyze_phoenix_code(phoenix_code)

        assert isinstance(result, dict)
        assert "score" in result
        assert 0 <= result["score"] <= 100
        assert "suggestions" in result

    @pytest.mark.skipif(not PHOENIX_SERVER_AVAILABLE, reason="Phoenix Server not available")
    @pytest.mark.asyncio
    async def test_analyze_phoenix_code_with_context(self):
        """Test Phoenix code analysis with context patterns"""
        phoenix_code = """
        defmodule MyApp.Accounts do
          import Ecto.Query
          alias MyApp.Repo
          alias MyApp.Accounts.User

          def list_users do
            Repo.all(User)
          end

          def get_user!(id), do: Repo.get!(User, id)

          def create_user(attrs) do
            %User{}
            |> User.changeset(attrs)
            |> Repo.insert()
          end
        end
        """

        result = await analyze_phoenix_code(phoenix_code)
        assert result["score"] >= 50

    @pytest.mark.skipif(not PHOENIX_SERVER_AVAILABLE, reason="Phoenix Server not available")
    @pytest.mark.asyncio
    async def test_generate_phoenix_resource(self):
        """Test Phoenix resource generation"""
        result = await generate_phoenix_resource(
            name="User",
            fields=["name:string", "email:string"]
        )

        assert isinstance(result, dict)
        assert "commands" in result
        assert "files_created" in result

    @pytest.mark.skipif(not PHOENIX_SERVER_AVAILABLE, reason="Phoenix Server not available")
    @pytest.mark.asyncio
    async def test_generate_context(self):
        """Test context generation"""
        result = await generate_context(
            name="Accounts",
            schema="User"
        )

        assert isinstance(result, dict)
        assert "context" in result
        assert "template" in result

    @pytest.mark.skipif(not PHOENIX_SERVER_AVAILABLE, reason="Phoenix Server not available")
    @pytest.mark.asyncio
    async def test_get_phoenix_patterns_all(self):
        """Test getting all Phoenix patterns"""
        result = await get_phoenix_patterns()

        assert isinstance(result, dict)
        assert "categories" in result
        assert "controller" in result["categories"]
        assert "router" in result["categories"]

    @pytest.mark.skipif(not PHOENIX_SERVER_AVAILABLE, reason="Phoenix Server not available")
    @pytest.mark.asyncio
    async def test_get_phoenix_patterns_by_category(self):
        """Test getting patterns by category"""
        result = await get_phoenix_patterns(category="controller")

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
