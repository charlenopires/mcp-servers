#!/usr/bin/env python3
"""
Phoenix Channels MCP Server
===========================

MCP server for Phoenix Channels, WebSocket, and PubSub patterns.
"""

import json
import logging
from typing import Dict, List, Optional, Any
from fastmcp import FastMCP, Context

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP(
    name="Phoenix Channels Server",
    instructions="""MCP server for Phoenix Channels and real-time communication.

Features:
- Channel and socket patterns
- PubSub broadcast patterns
- Presence tracking
- WebSocket integration

Use these tools to build real-time Phoenix applications.""",
    version="3.0.0"
)

class PhoenixChannelsKnowledgeBase:
    VERSION = "1.7.x"

    CHANNEL_PATTERNS = {
        "basic": '''defmodule MyAppWeb.RoomChannel do
  use MyAppWeb, :channel

  @impl true
  def join("room:" <> room_id, _payload, socket) do
    if authorized?(socket, room_id) do
      {:ok, assign(socket, :room_id, room_id)}
    else
      {:error, %{reason: "unauthorized"}}
    end
  end

  @impl true
  def handle_in("new_msg", %{"body" => body}, socket) do
    broadcast!(socket, "new_msg", %{body: body, user: socket.assigns.user_id})
    {:noreply, socket}
  end

  @impl true
  def handle_in("typing", _payload, socket) do
    broadcast_from!(socket, "typing", %{user: socket.assigns.user_id})
    {:noreply, socket}
  end

  defp authorized?(socket, room_id) do
    # Check if user can access this room
    true
  end
end''',
        "with_presence": '''defmodule MyAppWeb.RoomChannel do
  use MyAppWeb, :channel
  alias MyAppWeb.Presence

  @impl true
  def join("room:" <> room_id, _payload, socket) do
    send(self(), :after_join)
    {:ok, assign(socket, :room_id, room_id)}
  end

  @impl true
  def handle_info(:after_join, socket) do
    {:ok, _} = Presence.track(socket, socket.assigns.user_id, %{
      online_at: inspect(System.system_time(:second)),
      typing: false
    })
    push(socket, "presence_state", Presence.list(socket))
    {:noreply, socket}
  end
end'''
    }

    SOCKET_PATTERNS = {
        "user_socket": '''defmodule MyAppWeb.UserSocket do
  use Phoenix.Socket

  channel "room:*", MyAppWeb.RoomChannel
  channel "user:*", MyAppWeb.UserChannel

  @impl true
  def connect(%{"token" => token}, socket, _connect_info) do
    case Phoenix.Token.verify(MyAppWeb.Endpoint, "user socket", token, max_age: 86400) do
      {:ok, user_id} ->
        {:ok, assign(socket, :user_id, user_id)}
      {:error, _} ->
        :error
    end
  end

  @impl true
  def id(socket), do: "user_socket:#{socket.assigns.user_id}"
end'''
    }

    PUBSUB_PATTERNS = {
        "broadcast": '''# From anywhere in your application
MyAppWeb.Endpoint.broadcast("room:123", "new_msg", %{body: "Hello!"})

# From within a channel
broadcast!(socket, "new_msg", %{body: body})

# Broadcast except sender
broadcast_from!(socket, "typing", %{user: user_id})''',
        "subscribe": '''# Subscribe to topic
Phoenix.PubSub.subscribe(MyApp.PubSub, "room:123")

# Handle in GenServer
def handle_info(%{event: "new_msg", payload: payload}, state) do
  # Handle the message
  {:noreply, state}
end'''
    }

    PRESENCE_PATTERNS = {
        "setup": '''# lib/my_app_web/channels/presence.ex
defmodule MyAppWeb.Presence do
  use Phoenix.Presence,
    otp_app: :my_app,
    pubsub_server: MyApp.PubSub
end''',
        "usage": '''# Track user
Presence.track(socket, user_id, %{online_at: DateTime.utc_now()})

# List presences
Presence.list(socket)

# Get presence diff
def handle_info(%{event: "presence_diff", payload: diff}, socket) do
  {:noreply, socket}
end'''
    }


class ChannelsAnalyzer:
    async def analyze(self, code: str) -> Dict[str, Any]:
        score = 50
        suggestions = []

        if 'use MyAppWeb, :channel' in code: score += 15
        if 'def join(' in code: score += 10
        if 'handle_in(' in code: score += 10
        if 'broadcast!' in code or 'broadcast_from!' in code: score += 10
        if 'Presence' in code: score += 15
        if ':error' in code and 'unauthorized' in code: score += 10

        if 'authorized?' not in code and 'def join' in code:
            suggestions.append("Add authorization check in join/3")

        return {
            "score": min(100, score),
            "suggestions": suggestions,
            "grade": "Excellent" if score >= 90 else "Good" if score >= 75 else "Needs Improvement"
        }


@mcp.tool(tags=["analysis", "channels", "scoring"])
async def analyze_channel_code(code: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Analyzes Phoenix Channel code for patterns and best practices."""
    analyzer = ChannelsAnalyzer()
    return await analyzer.analyze(code)


@mcp.tool(tags=["generation", "channel", "phoenix"])
async def generate_channel(name: str, topic: str = "room", ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Generates Phoenix Channel module."""
    kb = PhoenixChannelsKnowledgeBase()
    return {
        "channel": name,
        "topic": f"{topic}:*",
        "template": kb.CHANNEL_PATTERNS["basic"]
    }


@mcp.tool(tags=["generation", "socket", "phoenix"])
async def generate_socket(name: str = "UserSocket", ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Generates Phoenix Socket module."""
    kb = PhoenixChannelsKnowledgeBase()
    return {"socket": name, "template": kb.SOCKET_PATTERNS["user_socket"]}


@mcp.tool(tags=["generation", "presence", "phoenix"])
async def generate_presence(ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Generates Phoenix Presence module."""
    kb = PhoenixChannelsKnowledgeBase()
    return {"setup": kb.PRESENCE_PATTERNS["setup"], "usage": kb.PRESENCE_PATTERNS["usage"]}


@mcp.tool(tags=["patterns", "reference", "channels"])
async def get_channel_patterns(category: str = "all", ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Returns Phoenix Channels patterns by category."""
    kb = PhoenixChannelsKnowledgeBase()

    categories = {
        "channel": kb.CHANNEL_PATTERNS,
        "socket": kb.SOCKET_PATTERNS,
        "pubsub": kb.PUBSUB_PATTERNS,
        "presence": kb.PRESENCE_PATTERNS,
    }

    if category == "all":
        return {"version": kb.VERSION, "categories": categories}

    return {"category": category, "patterns": categories.get(category, {})}


@mcp.prompt()
async def design_realtime_system(description: str, features: List[str] = []) -> List[Dict[str, str]]:
    """Generate prompt to design real-time Phoenix system."""
    return [
        {"role": "system", "content": "You are a Phoenix Channels expert for real-time systems."},
        {"role": "user", "content": f"Design real-time system: {description}\nFeatures: {', '.join(features)}"}
    ]


@mcp.resource(uri="guide://phoenix-channels")
async def get_channels_guide() -> str:
    return json.dumps({"title": "Phoenix Channels Guide", "version": PhoenixChannelsKnowledgeBase.VERSION})


if __name__ == "__main__":
    logger.info("Phoenix Channels MCP Server starting...")
    mcp.run()
