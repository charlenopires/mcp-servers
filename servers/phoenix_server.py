#!/usr/bin/env python3
"""
Phoenix Framework MCP Server
============================

MCP server for Phoenix web framework development with controllers,
routing, plugs, and contexts.
"""

import json
import re
import logging
from typing import Dict, List, Optional, Any
from fastmcp import FastMCP, Context

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP(
    name="Phoenix Framework Server",
    instructions="""MCP server for Phoenix web framework development.

Features:
- Controller and routing patterns
- Context and domain design
- Plug pipeline patterns
- Ecto integration
- REST API design

Use these tools to build Phoenix web applications.""",
    version="3.0.0"
)

class PhoenixKnowledgeBase:
    VERSION = "1.7.x"

    CONTROLLER_PATTERNS = {
        "basic": '''defmodule MyAppWeb.UserController do
  use MyAppWeb, :controller

  alias MyApp.Accounts
  alias MyApp.Accounts.User

  def index(conn, _params) do
    users = Accounts.list_users()
    render(conn, :index, users: users)
  end

  def show(conn, %{"id" => id}) do
    user = Accounts.get_user!(id)
    render(conn, :show, user: user)
  end

  def create(conn, %{"user" => user_params}) do
    case Accounts.create_user(user_params) do
      {:ok, user} ->
        conn
        |> put_flash(:info, "User created successfully.")
        |> redirect(to: ~p"/users/#{user}")

      {:error, %Ecto.Changeset{} = changeset} ->
        render(conn, :new, changeset: changeset)
    end
  end

  def update(conn, %{"id" => id, "user" => user_params}) do
    user = Accounts.get_user!(id)

    case Accounts.update_user(user, user_params) do
      {:ok, user} ->
        conn
        |> put_flash(:info, "User updated.")
        |> redirect(to: ~p"/users/#{user}")

      {:error, %Ecto.Changeset{} = changeset} ->
        render(conn, :edit, user: user, changeset: changeset)
    end
  end

  def delete(conn, %{"id" => id}) do
    user = Accounts.get_user!(id)
    {:ok, _user} = Accounts.delete_user(user)

    conn
    |> put_flash(:info, "User deleted.")
    |> redirect(to: ~p"/users")
  end
end''',
        "api": '''defmodule MyAppWeb.API.UserController do
  use MyAppWeb, :controller

  alias MyApp.Accounts

  action_fallback MyAppWeb.FallbackController

  def index(conn, _params) do
    users = Accounts.list_users()
    render(conn, :index, users: users)
  end

  def create(conn, %{"user" => user_params}) do
    with {:ok, user} <- Accounts.create_user(user_params) do
      conn
      |> put_status(:created)
      |> put_resp_header("location", ~p"/api/users/#{user}")
      |> render(:show, user: user)
    end
  end
end'''
    }

    ROUTER_PATTERNS = {
        "basic": '''defmodule MyAppWeb.Router do
  use MyAppWeb, :router

  pipeline :browser do
    plug :accepts, ["html"]
    plug :fetch_session
    plug :fetch_live_flash
    plug :put_root_layout, html: {MyAppWeb.Layouts, :root}
    plug :protect_from_forgery
    plug :put_secure_browser_headers
  end

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/", MyAppWeb do
    pipe_through :browser

    get "/", PageController, :home
    resources "/users", UserController
  end

  scope "/api", MyAppWeb.API do
    pipe_through :api

    resources "/users", UserController, except: [:new, :edit]
  end
end''',
        "nested": '''scope "/admin", MyAppWeb.Admin, as: :admin do
  pipe_through [:browser, :require_admin]

  resources "/users", UserController
  resources "/settings", SettingsController, only: [:index, :update]
end'''
    }

    CONTEXT_PATTERNS = {
        "basic": '''defmodule MyApp.Accounts do
  @moduledoc """
  The Accounts context - boundary for user management.
  """

  import Ecto.Query
  alias MyApp.Repo
  alias MyApp.Accounts.User

  def list_users do
    Repo.all(User)
  end

  def get_user!(id), do: Repo.get!(User, id)

  def get_user_by_email(email) do
    Repo.get_by(User, email: email)
  end

  def create_user(attrs \\\\ %{}) do
    %User{}
    |> User.changeset(attrs)
    |> Repo.insert()
  end

  def update_user(%User{} = user, attrs) do
    user
    |> User.changeset(attrs)
    |> Repo.update()
  end

  def delete_user(%User{} = user) do
    Repo.delete(user)
  end

  def change_user(%User{} = user, attrs \\\\ %{}) do
    User.changeset(user, attrs)
  end
end'''
    }

    PLUG_PATTERNS = {
        "function": '''defmodule MyAppWeb.UserController do
  use MyAppWeb, :controller

  plug :authenticate when action in [:edit, :update, :delete]

  defp authenticate(conn, _opts) do
    if conn.assigns[:current_user] do
      conn
    else
      conn
      |> put_flash(:error, "You must be logged in")
      |> redirect(to: ~p"/login")
      |> halt()
    end
  end
end''',
        "module": '''defmodule MyAppWeb.Plugs.RequireAuth do
  import Plug.Conn
  import Phoenix.Controller

  def init(opts), do: opts

  def call(conn, _opts) do
    if conn.assigns[:current_user] do
      conn
    else
      conn
      |> put_flash(:error, "Authentication required")
      |> redirect(to: "/login")
      |> halt()
    end
  end
end'''
    }


class PhoenixAnalyzer:
    async def analyze(self, code: str) -> Dict[str, Any]:
        score = 50
        suggestions = []

        if 'use MyAppWeb, :controller' in code: score += 10
        if 'alias ' in code: score += 5
        if 'action_fallback' in code: score += 10
        if 'pipe_through' in code: score += 10
        if 'resources ' in code: score += 10
        if 'defmodule ' in code and 'Context' in code or 'Accounts' in code: score += 15
        if 'Repo.' in code: score += 5
        if 'changeset' in code: score += 10

        if 'plug :' not in code and ':controller' in code:
            suggestions.append("Consider using plugs for cross-cutting concerns")

        return {
            "score": min(100, score),
            "suggestions": suggestions,
            "grade": "Excellent" if score >= 90 else "Good" if score >= 75 else "Needs Improvement"
        }


@mcp.tool(tags=["analysis", "phoenix", "scoring"])
async def analyze_phoenix_code(code: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Analyzes Phoenix code for patterns and best practices."""
    analyzer = PhoenixAnalyzer()
    return await analyzer.analyze(code)


@mcp.tool(tags=["generation", "resource", "phoenix"])
async def generate_phoenix_resource(name: str, fields: Optional[List[str]] = None, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Generates Phoenix resource (context, schema, controller)."""
    if fields is None:
        fields = ["name:string", "email:string"]

    singular = name.lower()
    plural = f"{singular}s"
    module = name.title()

    return {
        "commands": {
            "generate": f"mix phx.gen.html Accounts {module} {plural} {' '.join(fields)}",
            "api": f"mix phx.gen.json Accounts {module} {plural} {' '.join(fields)}"
        },
        "files_created": [
            f"lib/my_app/accounts/{singular}.ex",
            f"lib/my_app/accounts.ex",
            f"lib/my_app_web/controllers/{singular}_controller.ex",
            f"lib/my_app_web/controllers/{singular}_html.ex",
            f"priv/repo/migrations/*_create_{plural}.exs"
        ]
    }


@mcp.tool(tags=["generation", "context", "phoenix"])
async def generate_context(name: str, schema: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Generates Phoenix context module."""
    kb = PhoenixKnowledgeBase()
    return {
        "context": name,
        "schema": schema,
        "template": kb.CONTEXT_PATTERNS["basic"]
    }


@mcp.tool(tags=["patterns", "reference", "phoenix"])
async def get_phoenix_patterns(category: str = "all", ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Returns Phoenix patterns by category."""
    kb = PhoenixKnowledgeBase()

    categories = {
        "controller": kb.CONTROLLER_PATTERNS,
        "router": kb.ROUTER_PATTERNS,
        "context": kb.CONTEXT_PATTERNS,
        "plug": kb.PLUG_PATTERNS,
    }

    if category == "all":
        return {"phoenix_version": kb.VERSION, "categories": categories}

    return {"category": category, "patterns": categories.get(category, {})}


@mcp.prompt()
async def design_phoenix_application(name: str, features: List[str] = []) -> List[Dict[str, str]]:
    """Generate prompt to design Phoenix application."""
    return [
        {"role": "system", "content": "You are a Phoenix expert focused on web development best practices."},
        {"role": "user", "content": f"Design a Phoenix application: {name}\nFeatures: {', '.join(features)}"}
    ]


@mcp.resource(uri="guide://phoenix-development")
async def get_phoenix_guide() -> str:
    return json.dumps({"title": "Phoenix Development Guide", "version": PhoenixKnowledgeBase.VERSION})


if __name__ == "__main__":
    logger.info("Phoenix Framework MCP Server starting...")
    mcp.run()
