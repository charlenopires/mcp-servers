#!/usr/bin/env python3
"""
Tests for Phoenix Channels Server - MCP server for real-time communication.

Tests cover channels, WebSocket, PubSub, and Presence patterns.
"""

import pytest
from unittest.mock import AsyncMock

try:
    from servers.phoenix_channels_server import (
        analyze_channel_code,
        generate_channel,
        generate_socket,
        generate_presence,
        get_channel_patterns,
        PhoenixChannelsKnowledgeBase
    )
    PHOENIX_CHANNELS_SERVER_AVAILABLE = True
except ImportError as e:
    print(f"Phoenix Channels Server not available: {e}")
    PHOENIX_CHANNELS_SERVER_AVAILABLE = False


class TestPhoenixChannelsKnowledgeBase:
    """Tests for Phoenix Channels knowledge base"""

    @pytest.mark.skipif(not PHOENIX_CHANNELS_SERVER_AVAILABLE, reason="Phoenix Channels Server not available")
    def test_channel_patterns_exist(self):
        """Test that channel patterns are defined"""
        kb = PhoenixChannelsKnowledgeBase()
        assert hasattr(kb, 'CHANNEL_PATTERNS')
        assert "basic" in kb.CHANNEL_PATTERNS
        assert "with_presence" in kb.CHANNEL_PATTERNS

    @pytest.mark.skipif(not PHOENIX_CHANNELS_SERVER_AVAILABLE, reason="Phoenix Channels Server not available")
    def test_socket_patterns_exist(self):
        """Test that socket patterns are defined"""
        kb = PhoenixChannelsKnowledgeBase()
        assert hasattr(kb, 'SOCKET_PATTERNS')

    @pytest.mark.skipif(not PHOENIX_CHANNELS_SERVER_AVAILABLE, reason="Phoenix Channels Server not available")
    def test_pubsub_patterns_exist(self):
        """Test that PubSub patterns are defined"""
        kb = PhoenixChannelsKnowledgeBase()
        assert hasattr(kb, 'PUBSUB_PATTERNS')

    @pytest.mark.skipif(not PHOENIX_CHANNELS_SERVER_AVAILABLE, reason="Phoenix Channels Server not available")
    def test_presence_patterns_exist(self):
        """Test that Presence patterns are defined"""
        kb = PhoenixChannelsKnowledgeBase()
        assert hasattr(kb, 'PRESENCE_PATTERNS')


class TestPhoenixChannelsAnalysisFunctions:
    """Tests for Phoenix Channels Server analysis functions"""

    @pytest.mark.skipif(not PHOENIX_CHANNELS_SERVER_AVAILABLE, reason="Phoenix Channels Server not available")
    @pytest.mark.asyncio
    async def test_analyze_channel_code_basic(self):
        """Test basic channel code analysis"""
        channel_code = """
        defmodule MyAppWeb.RoomChannel do
          use MyAppWeb, :channel

          @impl true
          def join("room:" <> room_id, _payload, socket) do
            {:ok, assign(socket, :room_id, room_id)}
          end

          @impl true
          def handle_in("new_msg", %{"body" => body}, socket) do
            broadcast!(socket, "new_msg", %{body: body})
            {:noreply, socket}
          end
        end
        """

        result = await analyze_channel_code(channel_code)

        assert isinstance(result, dict)
        assert "score" in result
        assert 0 <= result["score"] <= 100
        assert "suggestions" in result

    @pytest.mark.skipif(not PHOENIX_CHANNELS_SERVER_AVAILABLE, reason="Phoenix Channels Server not available")
    @pytest.mark.asyncio
    async def test_analyze_channel_code_with_presence(self):
        """Test channel code analysis with Presence"""
        channel_code = """
        defmodule MyAppWeb.RoomChannel do
          use MyAppWeb, :channel
          alias MyAppWeb.Presence

          @impl true
          def join("room:" <> room_id, _payload, socket) do
            send(self(), :after_join)
            {:ok, socket}
          end

          @impl true
          def handle_info(:after_join, socket) do
            Presence.track(socket, socket.assigns.user_id, %{})
            {:noreply, socket}
          end
        end
        """

        result = await analyze_channel_code(channel_code)
        assert result["score"] >= 60  # Presence should boost score

    @pytest.mark.skipif(not PHOENIX_CHANNELS_SERVER_AVAILABLE, reason="Phoenix Channels Server not available")
    @pytest.mark.asyncio
    async def test_generate_channel(self):
        """Test channel generation"""
        result = await generate_channel(name="RoomChannel", topic="room")

        assert isinstance(result, dict)
        assert "channel" in result
        assert "topic" in result
        assert "template" in result

    @pytest.mark.skipif(not PHOENIX_CHANNELS_SERVER_AVAILABLE, reason="Phoenix Channels Server not available")
    @pytest.mark.asyncio
    async def test_generate_socket(self):
        """Test socket generation"""
        result = await generate_socket()

        assert isinstance(result, dict)
        assert "socket" in result
        assert "template" in result

    @pytest.mark.skipif(not PHOENIX_CHANNELS_SERVER_AVAILABLE, reason="Phoenix Channels Server not available")
    @pytest.mark.asyncio
    async def test_generate_presence(self):
        """Test Presence generation"""
        result = await generate_presence()

        assert isinstance(result, dict)
        assert "setup" in result
        assert "usage" in result

    @pytest.mark.skipif(not PHOENIX_CHANNELS_SERVER_AVAILABLE, reason="Phoenix Channels Server not available")
    @pytest.mark.asyncio
    async def test_get_channel_patterns_all(self):
        """Test getting all channel patterns"""
        result = await get_channel_patterns()

        assert isinstance(result, dict)
        assert "categories" in result
        assert "channel" in result["categories"]
        assert "pubsub" in result["categories"]

    @pytest.mark.skipif(not PHOENIX_CHANNELS_SERVER_AVAILABLE, reason="Phoenix Channels Server not available")
    @pytest.mark.asyncio
    async def test_get_channel_patterns_by_category(self):
        """Test getting patterns by category"""
        result = await get_channel_patterns(category="presence")

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
