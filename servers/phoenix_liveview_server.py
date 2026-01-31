#!/usr/bin/env python3
"""
Phoenix LiveView MCP Server
===========================

MCP server for Phoenix LiveView real-time UI patterns, hooks, and HEEx templates.
"""

import json
import logging
from typing import Dict, List, Optional, Any
from fastmcp import FastMCP, Context

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP(
    name="Phoenix LiveView Server",
    instructions="""MCP server for Phoenix LiveView real-time UI development.

Features:
- LiveView lifecycle patterns
- Event handling and bindings
- JavaScript hooks
- Live components and slots
- Streams and optimizations
- HEEx template patterns

Use these tools to build real-time Phoenix LiveView applications.""",
    version="3.0.0"
)

class LiveViewKnowledgeBase:
    VERSION = "0.20.x"

    LIFECYCLE_PATTERNS = {
        "basic": '''defmodule MyAppWeb.CounterLive do
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
    ~H"""
    <div>
      <h1>Count: <%= @count %></h1>
      <button phx-click="increment">+</button>
    </div>
    """
  end
end''',
        "with_params": '''defmodule MyAppWeb.UserLive.Show do
  use MyAppWeb, :live_view

  alias MyApp.Accounts

  @impl true
  def mount(_params, _session, socket) do
    {:ok, socket}
  end

  @impl true
  def handle_params(%{"id" => id}, _uri, socket) do
    user = Accounts.get_user!(id)
    {:noreply, assign(socket, user: user, page_title: user.name)}
  end

  @impl true
  def render(assigns) do
    ~H"""
    <div>
      <h1><%= @user.name %></h1>
      <p><%= @user.email %></p>
    </div>
    """
  end
end''',
        "with_async": '''defmodule MyAppWeb.DashboardLive do
  use MyAppWeb, :live_view

  @impl true
  def mount(_params, _session, socket) do
    {:ok,
     socket
     |> assign(:stats, nil)
     |> start_async(:load_stats, fn -> load_expensive_stats() end)}
  end

  @impl true
  def handle_async(:load_stats, {:ok, stats}, socket) do
    {:noreply, assign(socket, :stats, stats)}
  end

  @impl true
  def handle_async(:load_stats, {:exit, reason}, socket) do
    {:noreply, put_flash(socket, :error, "Failed to load stats")}
  end

  defp load_expensive_stats do
    # Expensive operation
    %{users: 100, orders: 500}
  end
end'''
    }

    EVENT_BINDINGS = {
        "click": '''<!-- Basic click -->
<button phx-click="action">Click me</button>

<!-- Click with value -->
<button phx-click="delete" phx-value-id={@item.id}>Delete</button>

<!-- Click with confirmation -->
<button phx-click="delete" data-confirm="Are you sure?">Delete</button>''',
        "form": '''<!-- Form submission -->
<.form for={@form} phx-submit="save" phx-change="validate">
  <.input field={@form[:name]} label="Name" />
  <.input field={@form[:email]} type="email" label="Email" />
  <button type="submit" phx-disable-with="Saving...">Save</button>
</.form>

<!-- Handle in LiveView -->
@impl true
def handle_event("validate", %{"user" => params}, socket) do
  changeset = Accounts.change_user(socket.assigns.user, params)
  {:noreply, assign(socket, form: to_form(changeset, action: :validate))}
end

@impl true
def handle_event("save", %{"user" => params}, socket) do
  case Accounts.update_user(socket.assigns.user, params) do
    {:ok, user} ->
      {:noreply,
       socket
       |> put_flash(:info, "Updated!")
       |> push_navigate(to: ~p"/users/#{user}")}

    {:error, changeset} ->
      {:noreply, assign(socket, form: to_form(changeset))}
  end
end''',
        "key": '''<!-- Key events -->
<div phx-window-keydown="keydown" phx-key="Escape">
  Press Escape to close
</div>

<!-- Key with target -->
<input phx-keyup="search" phx-debounce="300" />''',
        "focus": '''<!-- Focus events -->
<input phx-focus="focus" phx-blur="blur" />

<!-- Focus within -->
<div phx-focus="focus" phx-blur="blur" phx-window-focus="window_focus">
  Focusable area
</div>'''
    }

    HOOK_PATTERNS = {
        "basic": '''// assets/js/hooks.js
let Hooks = {}

Hooks.InfiniteScroll = {
  mounted() {
    this.observer = new IntersectionObserver(entries => {
      const entry = entries[0]
      if (entry.isIntersecting) {
        this.pushEvent("load-more", {})
      }
    })
    this.observer.observe(this.el)
  },
  destroyed() {
    this.observer.disconnect()
  }
}

Hooks.LocalTime = {
  mounted() {
    this.updated()
  },
  updated() {
    const dt = new Date(this.el.textContent)
    this.el.textContent = dt.toLocaleString()
  }
}

export default Hooks''',
        "server_events": '''// Handling server events
Hooks.Chart = {
  mounted() {
    this.chart = new Chart(this.el, this.chartConfig())

    this.handleEvent("update-chart", ({data}) => {
      this.chart.data = data
      this.chart.update()
    })
  },
  destroyed() {
    this.chart.destroy()
  },
  chartConfig() {
    return JSON.parse(this.el.dataset.config)
  }
}''',
        "push_event": '''// Push events to server
Hooks.Clipboard = {
  mounted() {
    this.el.addEventListener("click", () => {
      const text = this.el.dataset.copy
      navigator.clipboard.writeText(text).then(() => {
        this.pushEvent("copied", {text: text})
      })
    })
  }
}'''
    }

    COMPONENT_PATTERNS = {
        "live_component": '''defmodule MyAppWeb.Components.UserCard do
  use MyAppWeb, :live_component

  @impl true
  def update(assigns, socket) do
    {:ok, assign(socket, assigns)}
  end

  @impl true
  def handle_event("follow", _params, socket) do
    # Handle follow action
    send(self(), {:followed, socket.assigns.user})
    {:noreply, socket}
  end

  @impl true
  def render(assigns) do
    ~H"""
    <div class="user-card" id={@id}>
      <h3><%= @user.name %></h3>
      <button phx-click="follow" phx-target={@myself}>Follow</button>
    </div>
    """
  end
end

<!-- Usage -->
<.live_component module={MyAppWeb.Components.UserCard} id={@user.id} user={@user} />''',
        "function_component": '''# In core_components.ex or components.ex
attr :type, :string, default: "info"
attr :flash, :map, required: true
slot :inner_block

def alert(assigns) do
  ~H"""
  <div class={"alert alert-#{@type}"} role="alert">
    <%= render_slot(@inner_block) || @flash[@type] %>
  </div>
  """
end

# With slots
slot :header
slot :inner_block, required: true
slot :footer

def card(assigns) do
  ~H"""
  <div class="card">
    <div :if={@header != []} class="card-header">
      <%= render_slot(@header) %>
    </div>
    <div class="card-body">
      <%= render_slot(@inner_block) %>
    </div>
    <div :if={@footer != []} class="card-footer">
      <%= render_slot(@footer) %>
    </div>
  </div>
  """
end''',
        "slots_advanced": '''# Slot with attributes
slot :col, required: true do
  attr :label, :string, required: true
  attr :class, :string
end

def table(assigns) do
  ~H"""
  <table>
    <thead>
      <tr>
        <th :for={col <- @col} class={col[:class]}><%= col.label %></th>
      </tr>
    </thead>
    <tbody>
      <tr :for={row <- @rows}>
        <td :for={col <- @col} class={col[:class]}>
          <%= render_slot(col, row) %>
        </td>
      </tr>
    </tbody>
  </table>
  """
end

<!-- Usage -->
<.table rows={@users}>
  <:col :let={user} label="Name"><%= user.name %></:col>
  <:col :let={user} label="Email" class="text-muted"><%= user.email %></:col>
</.table>'''
    }

    STREAM_PATTERNS = {
        "basic": '''defmodule MyAppWeb.PostsLive do
  use MyAppWeb, :live_view

  @impl true
  def mount(_params, _session, socket) do
    {:ok, stream(socket, :posts, Blog.list_posts())}
  end

  @impl true
  def handle_event("delete", %{"id" => id}, socket) do
    post = Blog.get_post!(id)
    {:ok, _} = Blog.delete_post(post)
    {:noreply, stream_delete(socket, :posts, post)}
  end

  @impl true
  def render(assigns) do
    ~H"""
    <div id="posts" phx-update="stream">
      <div :for={{dom_id, post} <- @streams.posts} id={dom_id}>
        <h2><%= post.title %></h2>
        <button phx-click="delete" phx-value-id={post.id}>Delete</button>
      </div>
    </div>
    """
  end
end''',
        "infinite_scroll": '''@impl true
def mount(_params, _session, socket) do
  {:ok,
   socket
   |> assign(page: 1)
   |> stream(:items, fetch_items(1))}
end

@impl true
def handle_event("load-more", _params, socket) do
  page = socket.assigns.page + 1
  items = fetch_items(page)

  {:noreply,
   socket
   |> assign(page: page)
   |> stream(:items, items, at: -1)}
end''',
        "prepend": '''@impl true
def handle_info({:new_message, message}, socket) do
  {:noreply, stream_insert(socket, :messages, message, at: 0)}
end'''
    }

    HEEX_PATTERNS = {
        "conditionals": '''<!-- if/else -->
<div :if={@user}>
  Welcome, <%= @user.name %>
</div>

<!-- else clause -->
<%= if @loading do %>
  <.spinner />
<% else %>
  <.content data={@data} />
<% end %>

<!-- Ternary in attributes -->
<div class={@active && "active" || ""}>Content</div>

<!-- Dynamic classes -->
<div class={["base-class", @highlight && "highlighted", @size == :large && "text-lg"]}>
  Content
</div>''',
        "loops": '''<!-- for with index -->
<ul>
  <li :for={{item, index} <- Enum.with_index(@items)}>
    <%= index + 1 %>. <%= item.name %>
  </li>
</ul>

<!-- for with filter -->
<div :for={item <- @items, item.active?}>
  <%= item.name %>
</div>''',
        "special_attrs": '''<!-- Spread attributes -->
<.input {@rest} />

<!-- Data attributes -->
<div data-id={@item.id} data-action="edit">Content</div>

<!-- Boolean attributes -->
<input type="checkbox" checked={@checked} disabled={@disabled} />

<!-- Navigate -->
<.link navigate={~p"/users/#{@user}"}>View Profile</.link>
<.link patch={~p"/users?page=#{@page + 1}"}>Next Page</.link>'''
    }


class LiveViewAnalyzer:
    async def analyze(self, code: str) -> Dict[str, Any]:
        score = 50
        suggestions = []

        # Lifecycle callbacks
        if 'use MyAppWeb, :live_view' in code: score += 10
        if 'def mount(' in code: score += 10
        if 'def handle_event(' in code: score += 10
        if 'def render(' in code: score += 10
        if '@impl true' in code: score += 5

        # Components
        if 'live_component' in code or ':live_component' in code: score += 10
        if 'slot ' in code or ':slot' in code: score += 5

        # Streams (efficient list handling)
        if 'stream(' in code or 'stream_insert' in code: score += 15

        # HEEx quality
        if '~H"""' in code: score += 5
        if ':if={' in code or ':for={' in code: score += 5

        # Suggestions
        if 'stream(' not in code and '@items' in code:
            suggestions.append("Consider using streams for large collections")

        if 'phx-target' not in code and 'live_component' in code:
            suggestions.append("Use phx-target={@myself} in live components")

        if 'assign(' in code and 'assign_new(' not in code:
            suggestions.append("Consider assign_new/3 for conditional assigns")

        return {
            "score": min(100, score),
            "suggestions": suggestions,
            "grade": "Excellent" if score >= 90 else "Good" if score >= 75 else "Needs Improvement"
        }


@mcp.tool(tags=["analysis", "liveview", "scoring"])
async def analyze_liveview_code(code: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Analyzes Phoenix LiveView code for patterns and best practices."""
    analyzer = LiveViewAnalyzer()
    return await analyzer.analyze(code)


@mcp.tool(tags=["generation", "liveview", "phoenix"])
async def generate_liveview(name: str, features: Optional[List[str]] = None, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Generates Phoenix LiveView module with specified features."""
    if features is None:
        features = []

    module_name = name.title().replace(" ", "")
    kb = LiveViewKnowledgeBase()

    template = "with_async" if "async" in features else "with_params" if "params" in features else "basic"

    return {
        "module": f"MyAppWeb.{module_name}Live",
        "template": kb.LIFECYCLE_PATTERNS[template],
        "features": features,
        "tips": [
            "Add @impl true before all callbacks",
            "Use streams for large collections",
            "Consider async assigns for expensive operations"
        ]
    }


@mcp.tool(tags=["generation", "component", "phoenix"])
async def generate_live_component(name: str, with_slots: bool = False, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Generates Phoenix LiveComponent module."""
    kb = LiveViewKnowledgeBase()

    template_key = "slots_advanced" if with_slots else "live_component"

    return {
        "component": name,
        "template": kb.COMPONENT_PATTERNS[template_key],
        "tips": [
            "Use @myself for event targeting",
            "Implement update/2 for assign handling",
            "Send messages to parent with send(self(), ...)"
        ]
    }


@mcp.tool(tags=["generation", "hooks", "javascript"])
async def generate_js_hook(name: str, features: Optional[List[str]] = None, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Generates JavaScript hook for Phoenix LiveView."""
    if features is None:
        features = []

    kb = LiveViewKnowledgeBase()

    hook_code = f'''Hooks.{name} = {{
  mounted() {{
    // Called when element is added to DOM
    console.log("{name} mounted", this.el)
    {"this.handleEvent('update', (data) => { console.log(data) })" if "server_events" in features else ""}
  }},
  updated() {{
    // Called when element's data changes
  }},
  destroyed() {{
    // Called when element is removed
  }},
  disconnected() {{
    // Called when socket disconnects
  }},
  reconnected() {{
    // Called when socket reconnects
  }}
}}'''

    return {
        "hook": name,
        "code": hook_code,
        "usage": f'<div phx-hook="{name}" id="unique-id">Content</div>',
        "patterns": kb.HOOK_PATTERNS
    }


@mcp.tool(tags=["patterns", "reference", "liveview"])
async def get_liveview_patterns(category: str = "all", ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Returns Phoenix LiveView patterns by category."""
    kb = LiveViewKnowledgeBase()

    categories = {
        "lifecycle": kb.LIFECYCLE_PATTERNS,
        "events": kb.EVENT_BINDINGS,
        "hooks": kb.HOOK_PATTERNS,
        "components": kb.COMPONENT_PATTERNS,
        "streams": kb.STREAM_PATTERNS,
        "heex": kb.HEEX_PATTERNS,
    }

    if category == "all":
        return {"version": kb.VERSION, "categories": categories}

    return {"category": category, "patterns": categories.get(category, {})}


@mcp.tool(tags=["generation", "form", "liveview"])
async def generate_liveview_form(resource: str, fields: Optional[List[str]] = None, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """Generates LiveView form with validation."""
    if fields is None:
        fields = ["name:string", "email:string"]

    field_inputs = "\n  ".join([
        f'<.input field={{@form[:{f.split(":")[0]}]}} label="{f.split(":")[0].title()}" />'
        for f in fields
    ])

    code = f'''defmodule MyAppWeb.{resource.title()}Live.Form do
  use MyAppWeb, :live_view

  alias MyApp.{resource.title()}s

  @impl true
  def mount(_params, _session, socket) do
    changeset = {resource.title()}s.change_{resource}(%{resource.title()}s.{resource.title()}{{}}
)
    {{:ok, assign(socket, form: to_form(changeset))}}
  end

  @impl true
  def handle_event("validate", %{{"{resource}" => params}}, socket) do
    changeset =
      %{resource.title()}s.{resource.title()}{{}}
      |> {resource.title()}s.change_{resource}(params)
      |> Map.put(:action, :validate)

    {{:noreply, assign(socket, form: to_form(changeset))}}
  end

  @impl true
  def handle_event("save", %{{"{resource}" => params}}, socket) do
    case {resource.title()}s.create_{resource}(params) do
      {{:ok, {resource}}} ->
        {{:noreply,
         socket
         |> put_flash(:info, "{resource.title()} created!")
         |> push_navigate(to: ~p"/{resource}s/#{{{{resource}}}}"}})

      {{:error, changeset}} ->
        {{:noreply, assign(socket, form: to_form(changeset))}}
    end
  end

  @impl true
  def render(assigns) do
    ~H"""
    <div>
      <.form for={{@form}} phx-change="validate" phx-submit="save">
        {field_inputs}
        <button type="submit" phx-disable-with="Saving...">Save</button>
      </.form>
    </div>
    """
  end
end'''

    return {
        "resource": resource,
        "code": code,
        "fields": fields
    }


@mcp.prompt()
async def design_liveview_interface(description: str, features: List[str] = []) -> List[Dict[str, str]]:
    """Generate prompt to design LiveView interface."""
    return [
        {"role": "system", "content": "You are a Phoenix LiveView expert for real-time UI development."},
        {"role": "user", "content": f"Design LiveView interface: {description}\nFeatures: {', '.join(features)}"}
    ]


@mcp.resource(uri="guide://phoenix-liveview")
async def get_liveview_guide() -> str:
    return json.dumps({"title": "Phoenix LiveView Guide", "version": LiveViewKnowledgeBase.VERSION})


if __name__ == "__main__":
    logger.info("Phoenix LiveView MCP Server starting...")
    mcp.run()
