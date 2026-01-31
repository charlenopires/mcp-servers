#!/usr/bin/env python3
"""
Elixir MCP Server
=================

Advanced MCP server for Elixir development with functional programming,
OTP patterns, and concurrency best practices.
"""

import json
import re
import logging
from typing import Dict, List, Optional, Any
from enum import Enum
from fastmcp import FastMCP, Context

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP(
    name="Elixir Development Server",
    instructions="""Advanced MCP server for Elixir development.

Features:
- Functional programming patterns (pipe, pattern matching, guards)
- OTP behaviors (GenServer, Supervisor, Agent, Task)
- Concurrency and process patterns
- Mix project generation
- ExDoc documentation patterns

Use these tools to build robust Elixir applications.""",
    version="3.0.0"
)

class ElixirKnowledgeBase:
    VERSION = "1.17"
    OTP_VERSION = "27"

    GENSERVER_PATTERNS = {
        "basic": '''defmodule MyApp.Worker do
  use GenServer

  # Client API
  def start_link(init_arg) do
    GenServer.start_link(__MODULE__, init_arg, name: __MODULE__)
  end

  def get_state, do: GenServer.call(__MODULE__, :get_state)
  def update(data), do: GenServer.cast(__MODULE__, {:update, data})

  # Server Callbacks
  @impl true
  def init(init_arg) do
    {:ok, %{data: init_arg, started_at: DateTime.utc_now()}}
  end

  @impl true
  def handle_call(:get_state, _from, state) do
    {:reply, state, state}
  end

  @impl true
  def handle_cast({:update, data}, state) do
    {:noreply, %{state | data: data}}
  end
end''',
        "with_timeout": '''@impl true
def handle_info(:timeout, state) do
  perform_periodic_task()
  {:noreply, state, 5000}  # Schedule next timeout
end''',
        "with_continue": '''@impl true
def init(arg) do
  {:ok, initial_state(arg), {:continue, :load_data}}
end

@impl true
def handle_continue(:load_data, state) do
  data = load_expensive_data()
  {:noreply, %{state | data: data}}
end'''
    }

    SUPERVISOR_PATTERNS = {
        "basic": '''defmodule MyApp.Supervisor do
  use Supervisor

  def start_link(init_arg) do
    Supervisor.start_link(__MODULE__, init_arg, name: __MODULE__)
  end

  @impl true
  def init(_init_arg) do
    children = [
      {MyApp.Worker, []},
      {MyApp.Cache, []},
      {Task.Supervisor, name: MyApp.TaskSupervisor}
    ]

    Supervisor.init(children, strategy: :one_for_one)
  end
end''',
        "dynamic": '''defmodule MyApp.DynamicSupervisor do
  use DynamicSupervisor

  def start_link(init_arg) do
    DynamicSupervisor.start_link(__MODULE__, init_arg, name: __MODULE__)
  end

  def start_child(args) do
    spec = {MyApp.Worker, args}
    DynamicSupervisor.start_child(__MODULE__, spec)
  end

  @impl true
  def init(_init_arg) do
    DynamicSupervisor.init(strategy: :one_for_one)
  end
end'''
    }

    FUNCTIONAL_PATTERNS = {
        "pipe": '''# Pipe operator for data transformation
result =
  data
  |> Enum.map(&process/1)
  |> Enum.filter(&valid?/1)
  |> Enum.sort_by(& &1.name)
  |> Enum.take(10)''',
        "pattern_matching": '''# Pattern matching in function heads
def process(%{type: :user} = data), do: process_user(data)
def process(%{type: :admin} = data), do: process_admin(data)
def process(_), do: {:error, :unknown_type}

# Pattern matching in case
case fetch_data(id) do
  {:ok, %{status: :active} = user} -> handle_active(user)
  {:ok, %{status: :inactive}} -> {:error, :inactive}
  {:error, reason} -> {:error, reason}
end''',
        "with": '''# with for happy path
with {:ok, user} <- fetch_user(id),
     {:ok, permissions} <- fetch_permissions(user),
     :ok <- validate_access(permissions, resource) do
  {:ok, access_resource(user, resource)}
else
  {:error, :not_found} -> {:error, "User not found"}
  {:error, :unauthorized} -> {:error, "Access denied"}
  error -> error
end''',
        "comprehensions": '''# List comprehension with filters
for user <- users,
    user.active?,
    role <- user.roles,
    role.admin?,
    do: {user.id, role.name}

# Comprehension with into
for {key, val} <- map, into: %{}, do: {key, transform(val)}'''
    }

    CONCURRENCY_PATTERNS = {
        "task_async": '''# Async task with await
task = Task.async(fn -> expensive_computation() end)
# ... do other work ...
result = Task.await(task, 5000)

# Multiple async tasks
tasks = Enum.map(items, fn item ->
  Task.async(fn -> process(item) end)
end)
results = Task.await_many(tasks, 10_000)''',
        "task_supervisor": '''# Supervised tasks (won't crash caller)
Task.Supervisor.async_nolink(MyApp.TaskSupervisor, fn ->
  risky_operation()
end)

# Fire and forget
Task.Supervisor.start_child(MyApp.TaskSupervisor, fn ->
  send_email(user, message)
end)''',
        "agent": '''# Simple state management
{:ok, pid} = Agent.start_link(fn -> %{} end)
Agent.update(pid, &Map.put(&1, :key, value))
Agent.get(pid, &Map.get(&1, :key))'''
    }


class ElixirAnalyzer:
    def __init__(self):
        self.kb = ElixirKnowledgeBase()

    async def analyze(self, code: str) -> Dict[str, Any]:
        score = 50
        categories = {}
        suggestions = []

        # Functional patterns
        if '|>' in code:
            score += 15
        if 'with ' in code and '<-' in code:
            score += 10
        categories["functional"] = min(100, score)

        # OTP patterns
        if 'use GenServer' in code:
            score += 15
        if '@impl true' in code:
            score += 10
        if 'use Supervisor' in code:
            score += 10
        categories["otp"] = min(100, score - 50 + 50)

        # Documentation
        if '@doc' in code:
            score += 5
        if '@spec' in code:
            score += 10
        if '@moduledoc' in code:
            score += 5
        categories["documentation"] = min(100, score - 70 + 50)

        # Pattern matching
        if re.search(r'def \w+\(%\{', code):
            score += 10
        if 'case ' in code and '->' in code:
            score += 5

        if '@spec' not in code:
            suggestions.append("Add @spec for function type documentation")
        if '@moduledoc' not in code:
            suggestions.append("Add @moduledoc for module documentation")
        if '|>' not in code:
            suggestions.append("Consider using pipe operator for data transformations")

        return {
            "score": min(100, max(0, score)),
            "category_scores": categories,
            "suggestions": suggestions,
            "grade": "Excellent" if score >= 90 else "Good" if score >= 75 else "Needs Improvement"
        }


@mcp.tool(tags=["analysis", "elixir", "scoring"])
async def analyze_elixir_code(code: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Analyzes Elixir code for patterns and best practices."""
    analyzer = ElixirAnalyzer()
    return await analyzer.analyze(code)


@mcp.tool(tags=["generation", "mix", "templates"])
async def generate_elixir_project(name: str, type: str = "application", ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Generates Elixir Mix project structure."""
    app_name = name.lower().replace(" ", "_")

    files = {
        f"lib/{app_name}.ex": f'''defmodule {name.title().replace(" ", "")} do
  @moduledoc """
  {name} main module.
  """
end''',
        f"lib/{app_name}/application.ex": f'''defmodule {name.title().replace(" ", "")}.Application do
  use Application

  @impl true
  def start(_type, _args) do
    children = [
      # {{MyApp.Worker, arg}}
    ]

    opts = [strategy: :one_for_one, name: {name.title().replace(" ", "")}.Supervisor]
    Supervisor.start_link(children, opts)
  end
end''',
        "mix.exs": f'''defmodule {name.title().replace(" ", "")}.MixProject do
  use Mix.Project

  def project do
    [
      app: :{app_name},
      version: "0.1.0",
      elixir: "~> 1.17",
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end

  def application do
    [
      extra_applications: [:logger],
      mod: {{{name.title().replace(" ", "")}.Application, []}}
    ]
  end

  defp deps do
    []
  end
end'''
    }

    return {
        "project_name": app_name,
        "files": files,
        "commands": {
            "create": f"mix new {app_name} --sup",
            "compile": "mix compile",
            "test": "mix test",
            "format": "mix format"
        }
    }


@mcp.tool(tags=["generation", "genserver", "elixir"])
async def generate_genserver_elixir(name: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Generates Elixir GenServer module."""
    module_name = name.title().replace(" ", "")

    code = f'''defmodule {module_name} do
  @moduledoc """
  {name} GenServer implementation.
  """
  use GenServer

  # Client API

  def start_link(opts \\\\ []) do
    GenServer.start_link(__MODULE__, opts, name: __MODULE__)
  end

  def get_state do
    GenServer.call(__MODULE__, :get_state)
  end

  def update(data) do
    GenServer.cast(__MODULE__, {{:update, data}})
  end

  # Server Callbacks

  @impl true
  def init(_opts) do
    {{:ok, %{{data: nil, updated_at: nil}}}}
  end

  @impl true
  def handle_call(:get_state, _from, state) do
    {{:reply, state, state}}
  end

  @impl true
  def handle_cast({{:update, data}}, state) do
    {{:noreply, %{{state | data: data, updated_at: DateTime.utc_now()}}}}
  end

  @impl true
  def handle_info(_msg, state) do
    {{:noreply, state}}
  end
end'''

    return {"module": module_name, "code": code}


@mcp.tool(tags=["patterns", "reference", "elixir"])
async def get_elixir_patterns(category: str = "all", ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Returns Elixir patterns by category."""
    kb = ElixirKnowledgeBase()

    categories = {
        "genserver": kb.GENSERVER_PATTERNS,
        "supervisor": kb.SUPERVISOR_PATTERNS,
        "functional": kb.FUNCTIONAL_PATTERNS,
        "concurrency": kb.CONCURRENCY_PATTERNS,
    }

    if category == "all":
        return {"elixir_version": kb.VERSION, "categories": categories}

    return {"category": category, "patterns": categories.get(category, {})}


@mcp.prompt()
async def design_elixir_application(name: str, features: List[str] = []) -> List[Dict[str, str]]:
    """Generate prompt to design Elixir application."""
    return [
        {"role": "system", "content": "You are an Elixir expert focused on OTP and functional programming."},
        {"role": "user", "content": f"Design an Elixir application: {name}\nFeatures: {', '.join(features)}"}
    ]


@mcp.resource(uri="guide://elixir-development")
async def get_elixir_guide() -> str:
    return json.dumps({"title": "Elixir Development Guide", "version": ElixirKnowledgeBase.VERSION})


if __name__ == "__main__":
    logger.info("Elixir MCP Server starting...")
    mcp.run()
