#!/usr/bin/env python3
"""
Tests for Phoenix LiveView Server - MCP server for real-time UI development.

Tests cover LiveView lifecycle, events, hooks, and components.
"""

import pytest
from unittest.mock import AsyncMock

try:
    from servers.phoenix_liveview_server import (
        analyze_liveview_code,
        generate_liveview,
        generate_live_component,
        generate_js_hook,
        get_liveview_patterns,
        generate_liveview_form,
        LiveViewKnowledgeBase
    )
    PHOENIX_LIVEVIEW_SERVER_AVAILABLE = True
except ImportError as e:
    print(f"Phoenix LiveView Server not available: {e}")
    PHOENIX_LIVEVIEW_SERVER_AVAILABLE = False


class TestLiveViewKnowledgeBase:
    """Tests for LiveView knowledge base"""

    @pytest.mark.skipif(not PHOENIX_LIVEVIEW_SERVER_AVAILABLE, reason="Phoenix LiveView Server not available")
    def test_lifecycle_patterns_exist(self):
        """Test that lifecycle patterns are defined"""
        kb = LiveViewKnowledgeBase()
        assert hasattr(kb, 'LIFECYCLE_PATTERNS')
        assert "basic" in kb.LIFECYCLE_PATTERNS
        assert "with_params" in kb.LIFECYCLE_PATTERNS

    @pytest.mark.skipif(not PHOENIX_LIVEVIEW_SERVER_AVAILABLE, reason="Phoenix LiveView Server not available")
    def test_event_bindings_exist(self):
        """Test that event bindings are defined"""
        kb = LiveViewKnowledgeBase()
        assert hasattr(kb, 'EVENT_BINDINGS')
        assert "click" in kb.EVENT_BINDINGS
        assert "form" in kb.EVENT_BINDINGS

    @pytest.mark.skipif(not PHOENIX_LIVEVIEW_SERVER_AVAILABLE, reason="Phoenix LiveView Server not available")
    def test_hook_patterns_exist(self):
        """Test that hook patterns are defined"""
        kb = LiveViewKnowledgeBase()
        assert hasattr(kb, 'HOOK_PATTERNS')

    @pytest.mark.skipif(not PHOENIX_LIVEVIEW_SERVER_AVAILABLE, reason="Phoenix LiveView Server not available")
    def test_stream_patterns_exist(self):
        """Test that stream patterns are defined"""
        kb = LiveViewKnowledgeBase()
        assert hasattr(kb, 'STREAM_PATTERNS')


class TestLiveViewAnalysisFunctions:
    """Tests for LiveView Server analysis functions"""

    @pytest.mark.skipif(not PHOENIX_LIVEVIEW_SERVER_AVAILABLE, reason="Phoenix LiveView Server not available")
    @pytest.mark.asyncio
    async def test_analyze_liveview_code_basic(self):
        """Test basic LiveView code analysis"""
        liveview_code = """
        defmodule MyAppWeb.CounterLive do
          use MyAppWeb, :live_view

          @impl true
          def mount(_params, _session, socket) do
            {:ok, assign(socket, count: 0)}
          end

          @impl true
          def handle_event("increment", _params, socket) do
            {:noreply, update(socket, :count, &(&1 + 1))}
          end

          @impl true
          def render(assigns) do
            ~H\"\"\"
            <button phx-click="increment"><%= @count %></button>
            \"\"\"
          end
        end
        """

        result = await analyze_liveview_code(liveview_code)

        assert isinstance(result, dict)
        assert "score" in result
        assert 0 <= result["score"] <= 100
        assert "suggestions" in result

    @pytest.mark.skipif(not PHOENIX_LIVEVIEW_SERVER_AVAILABLE, reason="Phoenix LiveView Server not available")
    @pytest.mark.asyncio
    async def test_analyze_liveview_code_with_streams(self):
        """Test LiveView code analysis with streams"""
        liveview_code = """
        defmodule MyAppWeb.PostsLive do
          use MyAppWeb, :live_view

          @impl true
          def mount(_params, _session, socket) do
            {:ok, stream(socket, :posts, Blog.list_posts())}
          end

          @impl true
          def render(assigns) do
            ~H\"\"\"
            <div id="posts" phx-update="stream">
              <div :for={{dom_id, post} <- @streams.posts} id={dom_id}>
                <%= post.title %>
              </div>
            </div>
            \"\"\"
          end
        end
        """

        result = await analyze_liveview_code(liveview_code)
        assert result["score"] >= 70  # Streams should boost score significantly

    @pytest.mark.skipif(not PHOENIX_LIVEVIEW_SERVER_AVAILABLE, reason="Phoenix LiveView Server not available")
    @pytest.mark.asyncio
    async def test_generate_liveview(self):
        """Test LiveView generation"""
        result = await generate_liveview(name="Dashboard")

        assert isinstance(result, dict)
        assert "module" in result
        assert "template" in result

    @pytest.mark.skipif(not PHOENIX_LIVEVIEW_SERVER_AVAILABLE, reason="Phoenix LiveView Server not available")
    @pytest.mark.asyncio
    async def test_generate_liveview_with_features(self):
        """Test LiveView generation with features"""
        result = await generate_liveview(
            name="Dashboard",
            features=["async", "params"]
        )

        assert isinstance(result, dict)
        assert "template" in result
        assert "async" in result["features"] or "params" in result["features"]

    @pytest.mark.skipif(not PHOENIX_LIVEVIEW_SERVER_AVAILABLE, reason="Phoenix LiveView Server not available")
    @pytest.mark.asyncio
    async def test_generate_live_component(self):
        """Test LiveComponent generation"""
        result = await generate_live_component(name="UserCard")

        assert isinstance(result, dict)
        assert "component" in result
        assert "template" in result

    @pytest.mark.skipif(not PHOENIX_LIVEVIEW_SERVER_AVAILABLE, reason="Phoenix LiveView Server not available")
    @pytest.mark.asyncio
    async def test_generate_js_hook(self):
        """Test JavaScript hook generation"""
        result = await generate_js_hook(name="InfiniteScroll")

        assert isinstance(result, dict)
        assert "hook" in result
        assert "code" in result
        assert "usage" in result
        assert "mounted()" in result["code"]

    @pytest.mark.skipif(not PHOENIX_LIVEVIEW_SERVER_AVAILABLE, reason="Phoenix LiveView Server not available")
    @pytest.mark.asyncio
    async def test_generate_liveview_form(self):
        """Test LiveView form generation"""
        result = await generate_liveview_form(
            resource="user",
            fields=["name:string", "email:string"]
        )

        assert isinstance(result, dict)
        assert "code" in result
        assert "phx-change" in result["code"]
        assert "phx-submit" in result["code"]

    @pytest.mark.skipif(not PHOENIX_LIVEVIEW_SERVER_AVAILABLE, reason="Phoenix LiveView Server not available")
    @pytest.mark.asyncio
    async def test_get_liveview_patterns_all(self):
        """Test getting all LiveView patterns"""
        result = await get_liveview_patterns()

        assert isinstance(result, dict)
        assert "categories" in result
        assert "lifecycle" in result["categories"]
        assert "events" in result["categories"]
        assert "hooks" in result["categories"]

    @pytest.mark.skipif(not PHOENIX_LIVEVIEW_SERVER_AVAILABLE, reason="Phoenix LiveView Server not available")
    @pytest.mark.asyncio
    async def test_get_liveview_patterns_by_category(self):
        """Test getting patterns by category"""
        result = await get_liveview_patterns(category="streams")

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
