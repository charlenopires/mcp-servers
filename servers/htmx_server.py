#!/usr/bin/env python3
"""
HTMX with Axum MCP Server
=========================

Advanced MCP server for HTMX development with Axum (Rust) integration, featuring:
- HTMX attribute patterns (hx-get, hx-post, hx-swap, hx-trigger)
- Axum handler generation for HTMX responses
- HTML-driven AJAX patterns without JavaScript
- Progressive enhancement best practices
- Swap strategies and out-of-band updates
- Event handling and WebSocket support

Based on: htmx.org documentation, Axum web framework
"""

import asyncio
import json
import re
import logging
from dataclasses import dataclass
from typing import Dict, List, Optional, Any, Tuple, Union
from enum import Enum
from fastmcp import FastMCP, Context
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP(
    name="HTMX with Axum Server",
    instructions="""Advanced MCP server for HTMX development with Axum (Rust) backend integration.

This server provides HTMX development expertise:
- HTMX attribute patterns and best practices
- Axum handler generation for HTML responses
- Progressive enhancement patterns
- Swap strategies and OOB updates
- Event handling and triggers
- HTML fragment generation

Use these tools to build modern, hypermedia-driven web applications.""",
    version="3.0.0"
)

# ================================
# HTMX PATTERNS & KNOWLEDGE BASE
# ================================

class HTMXCategory(Enum):
    """HTMX pattern categories"""
    REQUESTS = "requests"
    SWAP = "swap"
    TRIGGERS = "triggers"
    TARGETS = "targets"
    HEADERS = "headers"
    EVENTS = "events"
    EXTENSIONS = "extensions"
    AXUM_INTEGRATION = "axum_integration"

class HTMXComplexity(Enum):
    """Complexity levels"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

@dataclass
class HTMXAnalysisResult:
    """Result of HTMX code analysis"""
    code: str
    score: int
    category_scores: Dict[str, int]
    patterns_found: List[str]
    anti_patterns_found: List[str]
    suggestions: List[str]
    axum_handlers: Dict[str, str]

class HTMXKnowledgeBase:
    """HTMX knowledge base with Axum integration patterns"""

    VERSION = "2.0.x"
    AXUM_VERSION = "0.7.x"

    # Core HTMX Attributes
    REQUEST_ATTRIBUTES = {
        "hx-get": {
            "description": "Issues a GET request to the specified URL",
            "syntax": 'hx-get="/api/endpoint"',
            "example": '''<button hx-get="/api/users" hx-target="#user-list">
    Load Users
</button>''',
            "axum_handler": '''async fn get_users(State(state): State<AppState>) -> Html<String> {
    let users = state.db.get_users().await.unwrap_or_default();
    Html(render_user_list(&users))
}'''
        },
        "hx-post": {
            "description": "Issues a POST request to the specified URL",
            "syntax": 'hx-post="/api/endpoint"',
            "example": '''<form hx-post="/api/users" hx-target="#user-list" hx-swap="beforeend">
    <input name="name" type="text" required />
    <input name="email" type="email" required />
    <button type="submit">Add User</button>
</form>''',
            "axum_handler": '''async fn create_user(
    State(state): State<AppState>,
    Form(input): Form<CreateUserInput>,
) -> Html<String> {
    let user = state.db.create_user(input).await.unwrap();
    Html(render_user_row(&user))
}'''
        },
        "hx-put": {
            "description": "Issues a PUT request to the specified URL",
            "syntax": 'hx-put="/api/endpoint"',
            "example": '''<form hx-put="/api/users/123" hx-target="#user-123" hx-swap="outerHTML">
    <input name="name" type="text" value="John" />
    <button type="submit">Update</button>
</form>''',
            "axum_handler": '''async fn update_user(
    State(state): State<AppState>,
    Path(id): Path<u32>,
    Form(input): Form<UpdateUserInput>,
) -> Html<String> {
    let user = state.db.update_user(id, input).await.unwrap();
    Html(render_user_row(&user))
}'''
        },
        "hx-patch": {
            "description": "Issues a PATCH request to the specified URL",
            "syntax": 'hx-patch="/api/endpoint"',
            "example": '''<button hx-patch="/api/users/123/toggle-active" hx-target="#user-123-status">
    Toggle Active
</button>''',
            "axum_handler": '''async fn toggle_user_active(
    State(state): State<AppState>,
    Path(id): Path<u32>,
) -> Html<String> {
    let user = state.db.toggle_active(id).await.unwrap();
    Html(render_status_badge(&user))
}'''
        },
        "hx-delete": {
            "description": "Issues a DELETE request to the specified URL",
            "syntax": 'hx-delete="/api/endpoint"',
            "example": '''<button
    hx-delete="/api/users/123"
    hx-target="#user-123"
    hx-swap="delete"
    hx-confirm="Delete this user?">
    Delete
</button>''',
            "axum_handler": '''async fn delete_user(
    State(state): State<AppState>,
    Path(id): Path<u32>,
) -> impl IntoResponse {
    state.db.delete_user(id).await.unwrap();
    StatusCode::OK
}'''
        }
    }

    # Swap Strategies
    SWAP_PATTERNS = {
        "innerHTML": {
            "description": "Replace the inner HTML of the target element (default)",
            "syntax": 'hx-swap="innerHTML"',
            "example": '''<div id="content" hx-get="/api/content" hx-swap="innerHTML">
    <!-- Old content replaced -->
</div>''',
            "use_case": "Updating container content without affecting the container itself"
        },
        "outerHTML": {
            "description": "Replace the entire target element",
            "syntax": 'hx-swap="outerHTML"',
            "example": '''<div id="user-card" hx-put="/api/users/123" hx-swap="outerHTML">
    <!-- Entire element replaced -->
</div>''',
            "use_case": "Replacing an element completely, including its attributes"
        },
        "beforebegin": {
            "description": "Insert before the target element",
            "syntax": 'hx-swap="beforebegin"',
            "example": '''<ul id="list">
    <li hx-get="/api/new-item" hx-swap="beforebegin">First Item</li>
</ul>''',
            "use_case": "Adding items before a reference element"
        },
        "afterbegin": {
            "description": "Insert as the first child of the target",
            "syntax": 'hx-swap="afterbegin"',
            "example": '''<ul id="notifications" hx-get="/api/latest" hx-swap="afterbegin">
    <li>Older notification</li>
</ul>''',
            "use_case": "Prepending new content to a container"
        },
        "beforeend": {
            "description": "Insert as the last child of the target",
            "syntax": 'hx-swap="beforeend"',
            "example": '''<ul id="messages" hx-get="/api/more" hx-swap="beforeend">
    <li>Message 1</li>
    <!-- New messages added here -->
</ul>''',
            "use_case": "Appending new content (infinite scroll, chat messages)"
        },
        "afterend": {
            "description": "Insert after the target element",
            "syntax": 'hx-swap="afterend"',
            "example": '''<div hx-get="/api/details" hx-swap="afterend">
    Click for details
</div>''',
            "use_case": "Adding content after an element"
        },
        "delete": {
            "description": "Remove the target element",
            "syntax": 'hx-swap="delete"',
            "example": '''<tr id="row-123" hx-delete="/api/items/123" hx-swap="delete">
    <td>Item to delete</td>
    <td><button>Delete</button></td>
</tr>''',
            "use_case": "Removing elements after successful deletion"
        },
        "none": {
            "description": "Don't swap, just trigger events",
            "syntax": 'hx-swap="none"',
            "example": '''<button hx-post="/api/trigger-job" hx-swap="none">
    Start Background Job
</button>''',
            "use_case": "Fire-and-forget requests, triggering server-side actions"
        }
    }

    # Trigger Patterns
    TRIGGER_PATTERNS = {
        "click": {
            "description": "Trigger on click (default for buttons)",
            "syntax": 'hx-trigger="click"',
            "example": '<button hx-get="/api/data" hx-trigger="click">Click me</button>'
        },
        "change": {
            "description": "Trigger on value change (default for inputs)",
            "syntax": 'hx-trigger="change"',
            "example": '''<select hx-get="/api/filter" hx-trigger="change" name="category">
    <option value="all">All</option>
    <option value="active">Active</option>
</select>'''
        },
        "submit": {
            "description": "Trigger on form submission (default for forms)",
            "syntax": 'hx-trigger="submit"',
            "example": '''<form hx-post="/api/search" hx-trigger="submit">
    <input name="q" type="search" />
    <button type="submit">Search</button>
</form>'''
        },
        "keyup": {
            "description": "Trigger on key up with debounce",
            "syntax": 'hx-trigger="keyup changed delay:500ms"',
            "example": '''<input
    name="search"
    hx-get="/api/search"
    hx-trigger="keyup changed delay:500ms"
    hx-target="#results"
    placeholder="Search..."/>'''
        },
        "load": {
            "description": "Trigger on element load",
            "syntax": 'hx-trigger="load"',
            "example": '''<div hx-get="/api/dashboard" hx-trigger="load">
    Loading dashboard...
</div>'''
        },
        "revealed": {
            "description": "Trigger when element is scrolled into view",
            "syntax": 'hx-trigger="revealed"',
            "example": '''<div hx-get="/api/more" hx-trigger="revealed" hx-swap="afterend">
    Loading more...
</div>'''
        },
        "intersect": {
            "description": "Trigger when element intersects viewport (lazy loading)",
            "syntax": 'hx-trigger="intersect once"',
            "example": '''<img
    hx-get="/api/image/123"
    hx-trigger="intersect once"
    hx-swap="outerHTML"
    src="placeholder.jpg" />'''
        },
        "every": {
            "description": "Trigger periodically (polling)",
            "syntax": 'hx-trigger="every 5s"',
            "example": '''<div hx-get="/api/status" hx-trigger="every 5s">
    Status: <span id="status">Unknown</span>
</div>'''
        }
    }

    # Axum Integration Patterns
    AXUM_PATTERNS = {
        "html_response": {
            "description": "Return HTML fragments from Axum handlers",
            "example": '''use axum::{response::Html, extract::State};

async fn get_users(State(state): State<AppState>) -> Html<String> {
    let users = state.db.get_users().await.unwrap_or_default();
    let html = users.iter()
        .map(|u| format!(r#"<tr id="user-{}"><td>{}</td><td>{}</td></tr>"#, u.id, u.name, u.email))
        .collect::<String>();
    Html(html)
}'''
        },
        "form_extraction": {
            "description": "Extract form data in Axum handlers",
            "example": '''use axum::extract::Form;
use serde::Deserialize;

#[derive(Deserialize)]
struct CreateUserInput {
    name: String,
    email: String,
}

async fn create_user(
    State(state): State<AppState>,
    Form(input): Form<CreateUserInput>,
) -> Html<String> {
    let user = User {
        id: state.next_id(),
        name: input.name,
        email: input.email,
    };
    state.db.insert_user(&user).await;
    Html(render_user_row(&user))
}'''
        },
        "hx_headers": {
            "description": "Handle HTMX-specific headers in Axum",
            "example": '''use axum::http::HeaderMap;

async fn handle_request(headers: HeaderMap) -> impl IntoResponse {
    let is_htmx = headers.get("HX-Request").is_some();
    let trigger = headers.get("HX-Trigger").map(|v| v.to_str().unwrap_or(""));
    let target = headers.get("HX-Target").map(|v| v.to_str().unwrap_or(""));

    if is_htmx {
        // Return HTML fragment
        Html(render_fragment())
    } else {
        // Return full page
        Html(render_full_page())
    }
}'''
        },
        "response_headers": {
            "description": "Set HTMX response headers from Axum",
            "example": '''use axum::{response::IntoResponse, http::{HeaderMap, HeaderValue}};

async fn create_and_redirect() -> impl IntoResponse {
    let mut headers = HeaderMap::new();

    // Trigger client-side event
    headers.insert("HX-Trigger", HeaderValue::from_static("userCreated"));

    // Redirect after swap
    headers.insert("HX-Redirect", HeaderValue::from_static("/users"));

    // Refresh page
    // headers.insert("HX-Refresh", HeaderValue::from_static("true"));

    // Retarget response
    // headers.insert("HX-Retarget", HeaderValue::from_static("#message"));

    (headers, Html("<p>User created!</p>"))
}'''
        },
        "oob_swap": {
            "description": "Out-of-band swaps from Axum",
            "example": '''async fn update_with_notification() -> Html<String> {
    Html(r#"
        <div id="main-content">
            Updated content here
        </div>

        <!-- Out-of-band swap: updates #notification without being the target -->
        <div id="notification" hx-swap-oob="true" class="alert alert-success">
            Update successful!
        </div>

        <!-- Multiple OOB swaps -->
        <span id="counter" hx-swap-oob="innerHTML">42</span>
    "#.to_string())
}'''
        },
        "router_setup": {
            "description": "Complete Axum router setup for HTMX",
            "example": '''use axum::{
    Router,
    routing::{get, post, put, delete},
    extract::State,
    response::Html,
};
use std::sync::Arc;
use tokio::sync::RwLock;

#[derive(Clone)]
struct AppState {
    db: Arc<RwLock<Database>>,
}

async fn app() -> Router {
    let state = AppState {
        db: Arc::new(RwLock::new(Database::new())),
    };

    Router::new()
        .route("/", get(index))
        .route("/api/users", get(list_users).post(create_user))
        .route("/api/users/:id", get(get_user).put(update_user).delete(delete_user))
        .route("/api/search", get(search))
        .with_state(state)
}'''
        }
    }

    # HTMX Events
    EVENTS = {
        "htmx:beforeRequest": "Triggered before a request is made",
        "htmx:afterRequest": "Triggered after a request completes",
        "htmx:beforeSwap": "Triggered before content is swapped",
        "htmx:afterSwap": "Triggered after content is swapped",
        "htmx:afterSettle": "Triggered after the settle step",
        "htmx:responseError": "Triggered on HTTP error responses",
        "htmx:sendError": "Triggered on network errors",
        "htmx:timeout": "Triggered on request timeout",
        "htmx:confirm": "Triggered when hx-confirm is used"
    }

    # Common UI Patterns
    UI_PATTERNS = {
        "infinite_scroll": {
            "description": "Load more content when scrolling",
            "html": '''<div id="feed">
    <!-- Existing items -->
    <div hx-get="/api/items?page=2"
         hx-trigger="revealed"
         hx-swap="afterend"
         hx-indicator="#loading">
        Loading more...
    </div>
</div>
<div id="loading" class="htmx-indicator">Loading...</div>''',
            "axum": '''async fn get_items(
    State(state): State<AppState>,
    Query(params): Query<PaginationParams>,
) -> Html<String> {
    let items = state.db.get_items(params.page, 20).await;
    let has_more = items.len() == 20;

    let mut html = items.iter()
        .map(|item| render_item(item))
        .collect::<String>();

    if has_more {
        html.push_str(&format!(r#"
            <div hx-get="/api/items?page={}"
                 hx-trigger="revealed"
                 hx-swap="afterend">
                Loading more...
            </div>
        "#, params.page + 1));
    }

    Html(html)
}'''
        },
        "search_as_you_type": {
            "description": "Live search with debounce",
            "html": '''<input
    type="search"
    name="q"
    hx-get="/api/search"
    hx-trigger="keyup changed delay:300ms, search"
    hx-target="#search-results"
    hx-indicator="#search-spinner"
    placeholder="Search..." />

<span id="search-spinner" class="htmx-indicator">Searching...</span>
<div id="search-results"></div>''',
            "axum": '''async fn search(
    State(state): State<AppState>,
    Query(params): Query<SearchParams>,
) -> Html<String> {
    let results = state.db.search(&params.q).await;

    if results.is_empty() {
        Html("<p class=\"text-gray-500\">No results found</p>".to_string())
    } else {
        let html = results.iter()
            .map(|r| format!(r#"<div class="p-2 hover:bg-gray-100">{}</div>"#, r.title))
            .collect::<String>();
        Html(html)
    }
}'''
        },
        "modal_dialog": {
            "description": "Load modal content via HTMX",
            "html": '''<!-- Trigger button -->
<button hx-get="/api/users/123/edit"
        hx-target="#modal-content"
        hx-trigger="click">
    Edit User
</button>

<!-- Modal container -->
<div id="modal" class="hidden">
    <div class="modal-backdrop" onclick="closeModal()"></div>
    <div id="modal-content" class="modal-body">
        <!-- Content loaded here -->
    </div>
</div>''',
            "axum": '''async fn edit_user_modal(
    State(state): State<AppState>,
    Path(id): Path<u32>,
) -> Html<String> {
    let user = state.db.get_user(id).await.unwrap();

    Html(format!(r#"
        <h2>Edit User</h2>
        <form hx-put="/api/users/{}" hx-target="#user-{}" hx-swap="outerHTML">
            <input name="name" value="{}" required />
            <input name="email" value="{}" type="email" required />
            <button type="submit">Save</button>
            <button type="button" onclick="closeModal()">Cancel</button>
        </form>
    "#, user.id, user.id, user.name, user.email))
}'''
        },
        "inline_editing": {
            "description": "Click to edit in place",
            "html": '''<span id="user-name-123"
      hx-get="/api/users/123/edit-name"
      hx-trigger="click"
      hx-swap="outerHTML"
      class="cursor-pointer hover:bg-yellow-100">
    John Doe
</span>''',
            "axum": '''// GET handler: return edit form
async fn edit_name_form(Path(id): Path<u32>, State(state): State<AppState>) -> Html<String> {
    let user = state.db.get_user(id).await.unwrap();
    Html(format!(r#"
        <form hx-put="/api/users/{}/name" hx-swap="outerHTML" class="inline">
            <input name="name" value="{}" autofocus
                   hx-on:keydown="if(event.key==='Escape') htmx.ajax('GET', '/api/users/{}/name-display', {{target:'#user-name-{}', swap:'outerHTML'}})" />
            <button type="submit">Save</button>
        </form>
    "#, id, user.name, id, id))
}

// PUT handler: update and return display
async fn update_name(
    Path(id): Path<u32>,
    State(state): State<AppState>,
    Form(input): Form<NameInput>,
) -> Html<String> {
    state.db.update_name(id, &input.name).await;
    Html(format!(r#"
        <span id="user-name-{}" hx-get="/api/users/{}/edit-name" hx-trigger="click" hx-swap="outerHTML">
            {}
        </span>
    "#, id, id, input.name))
}'''
        },
        "tabs": {
            "description": "Tab navigation with HTMX",
            "html": '''<div class="tabs">
    <button hx-get="/api/tabs/overview"
            hx-target="#tab-content"
            hx-push-url="true"
            class="tab active">Overview</button>
    <button hx-get="/api/tabs/details"
            hx-target="#tab-content"
            hx-push-url="true"
            class="tab">Details</button>
    <button hx-get="/api/tabs/settings"
            hx-target="#tab-content"
            hx-push-url="true"
            class="tab">Settings</button>
</div>

<div id="tab-content">
    <!-- Tab content loaded here -->
</div>''',
            "axum": '''async fn tab_overview() -> Html<String> {
    Html("<h2>Overview</h2><p>Overview content here...</p>".to_string())
}

async fn tab_details() -> Html<String> {
    Html("<h2>Details</h2><p>Details content here...</p>".to_string())
}

async fn tab_settings() -> Html<String> {
    Html("<h2>Settings</h2><p>Settings form here...</p>".to_string())
}'''
        }
    }


class HTMXAnalyzer:
    """HTMX code analyzer"""

    def __init__(self):
        self.knowledge_base = HTMXKnowledgeBase()

    async def analyze_htmx_code(self, code: str) -> HTMXAnalysisResult:
        """Analyze HTMX code for patterns and best practices"""

        score = 50
        category_scores = {}
        patterns_found = []
        anti_patterns = []
        suggestions = []
        axum_handlers = {}

        # Analyze request attributes
        request_score = await self._analyze_requests(code)
        category_scores["requests"] = request_score
        score += (request_score - 50) * 0.25

        # Analyze swap usage
        swap_score = await self._analyze_swap(code)
        category_scores["swap"] = swap_score
        score += (swap_score - 50) * 0.15

        # Analyze trigger patterns
        trigger_score = await self._analyze_triggers(code)
        category_scores["triggers"] = trigger_score
        score += (trigger_score - 50) * 0.15

        # Analyze target usage
        target_score = await self._analyze_targets(code)
        category_scores["targets"] = target_score
        score += (target_score - 50) * 0.15

        # Analyze progressive enhancement
        pe_score = await self._analyze_progressive_enhancement(code)
        category_scores["progressive_enhancement"] = pe_score
        score += (pe_score - 50) * 0.15

        # Analyze accessibility
        a11y_score = await self._analyze_accessibility(code)
        category_scores["accessibility"] = a11y_score
        score += (a11y_score - 50) * 0.15

        # Generate suggestions
        suggestions.extend(await self._generate_suggestions(category_scores, code))

        # Generate Axum handlers
        axum_handlers = await self._suggest_axum_handlers(code)

        final_score = max(0, min(100, int(score)))

        return HTMXAnalysisResult(
            code=code,
            score=final_score,
            category_scores=category_scores,
            patterns_found=patterns_found,
            anti_patterns_found=anti_patterns,
            suggestions=suggestions,
            axum_handlers=axum_handlers
        )

    async def _analyze_requests(self, code: str) -> int:
        """Analyze request attribute usage"""
        score = 50

        # Check for hx-get, hx-post, etc.
        request_attrs = ['hx-get', 'hx-post', 'hx-put', 'hx-patch', 'hx-delete']
        for attr in request_attrs:
            if attr in code:
                score += 5

        # Check for proper URL patterns
        if re.search(r'hx-(?:get|post|put|patch|delete)="[^"]*"', code):
            score += 10

        # Check for hx-include for additional data
        if 'hx-include' in code:
            score += 5

        return min(100, max(0, score))

    async def _analyze_swap(self, code: str) -> int:
        """Analyze swap strategy usage"""
        score = 50

        # Check for explicit swap strategy
        if 'hx-swap=' in code:
            score += 15

        # Check for swap modifiers
        if any(mod in code for mod in ['settle:', 'swap:', 'scroll:', 'show:']):
            score += 10

        # Check for OOB swaps
        if 'hx-swap-oob' in code:
            score += 10

        return min(100, max(0, score))

    async def _analyze_triggers(self, code: str) -> int:
        """Analyze trigger patterns"""
        score = 50

        # Check for custom triggers
        if 'hx-trigger=' in code:
            score += 10

        # Check for debounce/throttle
        if any(mod in code for mod in ['delay:', 'throttle:']):
            score += 15

        # Check for changed modifier
        if 'changed' in code and 'hx-trigger' in code:
            score += 10

        # Check for event filters
        if any(evt in code for evt in ['keyup', 'keydown', 'change', 'submit']):
            score += 5

        return min(100, max(0, score))

    async def _analyze_targets(self, code: str) -> int:
        """Analyze target patterns"""
        score = 50

        # Check for explicit targets
        if 'hx-target=' in code:
            score += 15

        # Check for CSS selectors in target
        if re.search(r'hx-target="#[^"]+"|hx-target="\.[^"]+"', code):
            score += 10

        # Check for this/closest/find selectors
        if any(sel in code for sel in ['this', 'closest', 'find', 'next', 'previous']):
            score += 10

        return min(100, max(0, score))

    async def _analyze_progressive_enhancement(self, code: str) -> int:
        """Analyze progressive enhancement patterns"""
        score = 50

        # Check for form fallbacks
        if '<form' in code and ('action=' in code or 'method=' in code):
            score += 15

        # Check for anchor fallbacks
        if '<a ' in code and 'href=' in code:
            score += 10

        # Check for hx-boost
        if 'hx-boost' in code:
            score += 15

        # Check for noscript fallbacks
        if '<noscript' in code:
            score += 10

        return min(100, max(0, score))

    async def _analyze_accessibility(self, code: str) -> int:
        """Analyze accessibility patterns"""
        score = 50

        # Check for aria attributes
        if any(attr in code for attr in ['aria-', 'role=', 'aria-live']):
            score += 20

        # Check for loading indicators
        if 'hx-indicator' in code or 'htmx-indicator' in code:
            score += 15

        # Check for confirmation dialogs
        if 'hx-confirm' in code:
            score += 10

        # Check for semantic HTML
        semantic_tags = ['<button', '<form', '<input', '<label', '<nav', '<main', '<article']
        score += sum(5 for tag in semantic_tags if tag in code)

        return min(100, max(0, score))

    async def _generate_suggestions(self, scores: Dict[str, int], code: str) -> List[str]:
        """Generate improvement suggestions"""
        suggestions = []

        if scores.get("requests", 50) < 70:
            suggestions.append("Add explicit hx-get, hx-post, etc. attributes for AJAX requests")

        if scores.get("swap", 50) < 70:
            suggestions.append("Consider using hx-swap to control how content is inserted")

        if scores.get("triggers", 50) < 70:
            suggestions.append("Use hx-trigger with delay: for search inputs to debounce requests")

        if scores.get("targets", 50) < 70:
            suggestions.append("Always specify hx-target to make swap behavior explicit")

        if scores.get("progressive_enhancement", 50) < 70:
            suggestions.append("Add form action/method attributes for non-JS fallback")
            suggestions.append("Consider using hx-boost for progressive enhancement")

        if scores.get("accessibility", 50) < 70:
            suggestions.append("Add hx-indicator for loading states")
            suggestions.append("Use aria-live regions for dynamic content updates")

        return suggestions

    async def _suggest_axum_handlers(self, code: str) -> Dict[str, str]:
        """Suggest Axum handlers for HTMX endpoints"""
        handlers = {}

        # Find all hx-get endpoints
        for match in re.finditer(r'hx-get="([^"]+)"', code):
            endpoint = match.group(1)
            handlers[f"GET {endpoint}"] = f'''async fn handle_get() -> Html<String> {{
    Html("<div>Response HTML</div>".to_string())
}}'''

        # Find all hx-post endpoints
        for match in re.finditer(r'hx-post="([^"]+)"', code):
            endpoint = match.group(1)
            handlers[f"POST {endpoint}"] = '''async fn handle_post(
    Form(input): Form<FormInput>,
) -> Html<String> {
    Html("<div>Created</div>".to_string())
}'''

        # Find all hx-put endpoints
        for match in re.finditer(r'hx-put="([^"]+)"', code):
            endpoint = match.group(1)
            handlers[f"PUT {endpoint}"] = '''async fn handle_put(
    Path(id): Path<u32>,
    Form(input): Form<FormInput>,
) -> Html<String> {
    Html("<div>Updated</div>".to_string())
}'''

        # Find all hx-delete endpoints
        for match in re.finditer(r'hx-delete="([^"]+)"', code):
            endpoint = match.group(1)
            handlers[f"DELETE {endpoint}"] = '''async fn handle_delete(
    Path(id): Path<u32>,
) -> impl IntoResponse {
    StatusCode::OK
}'''

        return handlers


class HTMXGenerator:
    """HTMX code generator"""

    def __init__(self):
        self.knowledge_base = HTMXKnowledgeBase()

    async def generate_component(
        self,
        component_type: str,
        options: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Generate HTMX component with Axum handler"""

        if options is None:
            options = {}

        generators = {
            "form": self._generate_form,
            "list": self._generate_list,
            "search": self._generate_search,
            "modal": self._generate_modal,
            "tabs": self._generate_tabs,
            "infinite_scroll": self._generate_infinite_scroll,
            "inline_edit": self._generate_inline_edit,
        }

        if component_type not in generators:
            return {"error": f"Unknown component type: {component_type}"}

        return await generators[component_type](options)

    async def _generate_form(self, options: Dict[str, Any]) -> Dict[str, Any]:
        """Generate HTMX form"""
        endpoint = options.get("endpoint", "/api/items")
        target = options.get("target", "#item-list")
        swap = options.get("swap", "beforeend")
        fields = options.get("fields", [{"name": "name", "type": "text"}])

        field_html = "\n    ".join([
            f'<input name="{f["name"]}" type="{f.get("type", "text")}" placeholder="{f["name"].title()}" required />'
            for f in fields
        ])

        html = f'''<form
    hx-post="{endpoint}"
    hx-target="{target}"
    hx-swap="{swap}"
    hx-indicator="#form-spinner">
    {field_html}
    <button type="submit">Submit</button>
    <span id="form-spinner" class="htmx-indicator">Saving...</span>
</form>'''

        rust = f'''#[derive(Deserialize)]
struct FormInput {{
    {chr(10).join([f'{f["name"]}: String,' for f in fields])}
}}

async fn create_item(
    State(state): State<AppState>,
    Form(input): Form<FormInput>,
) -> Html<String> {{
    // Create item in database
    let item = state.db.create_item(input).await.unwrap();
    Html(render_item(&item))
}}'''

        return {
            "component_type": "form",
            "html": html,
            "axum_handler": rust,
            "patterns_used": ["hx-post", "hx-target", "hx-swap", "hx-indicator"]
        }

    async def _generate_list(self, options: Dict[str, Any]) -> Dict[str, Any]:
        """Generate HTMX list with CRUD operations"""
        endpoint = options.get("endpoint", "/api/items")

        html = f'''<div id="item-list">
    <div hx-get="{endpoint}" hx-trigger="load" hx-swap="innerHTML">
        Loading items...
    </div>
</div>

<!-- Item template -->
<template id="item-template">
    <div id="item-{{id}}" class="item">
        <span class="item-name">{{name}}</span>
        <button hx-delete="{endpoint}/{{id}}"
                hx-target="#item-{{id}}"
                hx-swap="delete"
                hx-confirm="Delete this item?">
            Delete
        </button>
    </div>
</template>'''

        rust = '''async fn list_items(State(state): State<AppState>) -> Html<String> {
    let items = state.db.get_items().await.unwrap_or_default();
    let html = items.iter()
        .map(|item| format!(r#"
            <div id="item-{}" class="item">
                <span class="item-name">{}</span>
                <button hx-delete="/api/items/{}"
                        hx-target="#item-{}"
                        hx-swap="delete"
                        hx-confirm="Delete this item?">
                    Delete
                </button>
            </div>
        "#, item.id, item.name, item.id, item.id))
        .collect::<String>();
    Html(html)
}

async fn delete_item(
    State(state): State<AppState>,
    Path(id): Path<u32>,
) -> impl IntoResponse {
    state.db.delete_item(id).await.unwrap();
    StatusCode::OK
}'''

        return {
            "component_type": "list",
            "html": html,
            "axum_handler": rust,
            "patterns_used": ["hx-get", "hx-delete", "hx-trigger", "hx-swap", "hx-confirm"]
        }

    async def _generate_search(self, options: Dict[str, Any]) -> Dict[str, Any]:
        """Generate search-as-you-type component"""
        endpoint = options.get("endpoint", "/api/search")
        delay = options.get("delay", "300ms")

        html = f'''<div class="search-container">
    <input
        type="search"
        name="q"
        hx-get="{endpoint}"
        hx-trigger="keyup changed delay:{delay}, search"
        hx-target="#search-results"
        hx-indicator="#search-spinner"
        placeholder="Search..." />

    <span id="search-spinner" class="htmx-indicator">
        <svg class="animate-spin h-5 w-5" viewBox="0 0 24 24">...</svg>
    </span>

    <div id="search-results" aria-live="polite">
        <!-- Results loaded here -->
    </div>
</div>'''

        rust = '''#[derive(Deserialize)]
struct SearchParams {
    q: Option<String>,
}

async fn search(
    State(state): State<AppState>,
    Query(params): Query<SearchParams>,
) -> Html<String> {
    let query = params.q.unwrap_or_default();

    if query.is_empty() {
        return Html(String::new());
    }

    let results = state.db.search(&query).await.unwrap_or_default();

    if results.is_empty() {
        return Html(r#"<p class="no-results">No results found</p>"#.to_string());
    }

    let html = results.iter()
        .map(|r| format!(r#"
            <div class="search-result">
                <a href="/items/{}">{}</a>
                <p>{}</p>
            </div>
        "#, r.id, r.title, r.description))
        .collect::<String>();

    Html(html)
}'''

        return {
            "component_type": "search",
            "html": html,
            "axum_handler": rust,
            "patterns_used": ["hx-get", "hx-trigger", "delay", "hx-indicator", "aria-live"]
        }

    async def _generate_modal(self, options: Dict[str, Any]) -> Dict[str, Any]:
        """Generate modal dialog component"""

        html = '''<!-- Trigger Button -->
<button
    hx-get="/api/modal/edit/123"
    hx-target="#modal-content"
    hx-trigger="click"
    onclick="document.getElementById('modal').classList.remove('hidden')">
    Edit Item
</button>

<!-- Modal Container -->
<div id="modal" class="hidden fixed inset-0 z-50">
    <!-- Backdrop -->
    <div class="fixed inset-0 bg-black/50"
         onclick="document.getElementById('modal').classList.add('hidden')">
    </div>

    <!-- Modal Content -->
    <div class="fixed inset-x-4 top-[50%] translate-y-[-50%] max-w-lg mx-auto bg-white rounded-lg shadow-xl p-6">
        <div id="modal-content">
            <!-- Content loaded here -->
        </div>
    </div>
</div>

<script>
function closeModal() {
    document.getElementById('modal').classList.add('hidden');
}
</script>'''

        rust = '''async fn modal_edit(
    State(state): State<AppState>,
    Path(id): Path<u32>,
) -> Html<String> {
    let item = state.db.get_item(id).await.unwrap();

    Html(format!(r#"
        <h2 class="text-xl font-bold mb-4">Edit Item</h2>
        <form hx-put="/api/items/{}"
              hx-target="#item-{}"
              hx-swap="outerHTML"
              hx-on::after-request="closeModal()">
            <div class="mb-4">
                <label class="block mb-1">Name</label>
                <input name="name" value="{}" class="w-full border rounded p-2" required />
            </div>
            <div class="flex gap-2 justify-end">
                <button type="button" onclick="closeModal()" class="px-4 py-2 border rounded">
                    Cancel
                </button>
                <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded">
                    Save
                </button>
            </div>
        </form>
    "#, item.id, item.id, item.name))
}'''

        return {
            "component_type": "modal",
            "html": html,
            "axum_handler": rust,
            "patterns_used": ["hx-get", "hx-target", "hx-put", "hx-swap", "hx-on"]
        }

    async def _generate_tabs(self, options: Dict[str, Any]) -> Dict[str, Any]:
        """Generate tab navigation"""
        tabs = options.get("tabs", [
            {"id": "overview", "label": "Overview"},
            {"id": "details", "label": "Details"},
            {"id": "settings", "label": "Settings"}
        ])

        tab_buttons = "\n    ".join([
            f'''<button
        hx-get="/api/tabs/{tab['id']}"
        hx-target="#tab-content"
        hx-push-url="true"
        class="tab-btn {'active' if i == 0 else ''}"
        hx-on::after-request="setActiveTab(this)">
        {tab['label']}
    </button>'''
            for i, tab in enumerate(tabs)
        ])

        html = f'''<div class="tabs">
    <div class="tab-list" role="tablist">
    {tab_buttons}
    </div>

    <div id="tab-content" class="tab-panel" role="tabpanel">
        <!-- Tab content loaded here -->
        <div hx-get="/api/tabs/{tabs[0]['id']}" hx-trigger="load"></div>
    </div>
</div>

<script>
function setActiveTab(btn) {{
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
}}
</script>'''

        rust = "\n\n".join([
            f'''async fn tab_{tab['id']}() -> Html<String> {{
    Html("<div><h2>{tab['label']}</h2><p>{tab['label']} content here...</p></div>".to_string())
}}'''
            for tab in tabs
        ])

        return {
            "component_type": "tabs",
            "html": html,
            "axum_handler": rust,
            "patterns_used": ["hx-get", "hx-target", "hx-push-url", "hx-trigger", "hx-on"]
        }

    async def _generate_infinite_scroll(self, options: Dict[str, Any]) -> Dict[str, Any]:
        """Generate infinite scroll component"""
        endpoint = options.get("endpoint", "/api/items")

        html = f'''<div id="item-feed">
    <div hx-get="{endpoint}?page=1" hx-trigger="load" hx-swap="innerHTML">
        Loading...
    </div>
</div>'''

        rust = '''#[derive(Deserialize)]
struct PaginationParams {
    page: Option<u32>,
}

async fn get_items_paginated(
    State(state): State<AppState>,
    Query(params): Query<PaginationParams>,
) -> Html<String> {
    let page = params.page.unwrap_or(1);
    let per_page = 20;
    let items = state.db.get_items_paginated(page, per_page).await.unwrap_or_default();
    let has_more = items.len() == per_page as usize;

    let mut html = items.iter()
        .map(|item| format!(r#"
            <div class="item-card">
                <h3>{}</h3>
                <p>{}</p>
            </div>
        "#, item.title, item.description))
        .collect::<String>();

    if has_more {
        html.push_str(&format!(r#"
            <div hx-get="/api/items?page={}"
                 hx-trigger="revealed"
                 hx-swap="afterend"
                 class="loading-indicator">
                Loading more...
            </div>
        "#, page + 1));
    }

    Html(html)
}'''

        return {
            "component_type": "infinite_scroll",
            "html": html,
            "axum_handler": rust,
            "patterns_used": ["hx-get", "hx-trigger", "revealed", "hx-swap"]
        }

    async def _generate_inline_edit(self, options: Dict[str, Any]) -> Dict[str, Any]:
        """Generate inline edit component"""

        html = '''<!-- Inline editable field -->
<span id="name-123"
      hx-get="/api/items/123/edit-name"
      hx-trigger="click"
      hx-swap="outerHTML"
      class="editable cursor-pointer hover:bg-yellow-100 px-1 rounded"
      title="Click to edit">
    John Doe
</span>'''

        rust = '''// Return edit form
async fn edit_name_form(
    State(state): State<AppState>,
    Path(id): Path<u32>,
) -> Html<String> {
    let item = state.db.get_item(id).await.unwrap();

    Html(format!(r#"
        <form hx-put="/api/items/{}/name"
              hx-swap="outerHTML"
              class="inline-flex gap-1">
            <input name="name"
                   value="{}"
                   autofocus
                   class="border rounded px-1"
                   hx-on:keydown="if(event.key==='Escape') this.form.reset()" />
            <button type="submit" class="text-green-600">Save</button>
        </form>
    "#, id, item.name))
}

// Update and return display
async fn update_name(
    State(state): State<AppState>,
    Path(id): Path<u32>,
    Form(input): Form<NameInput>,
) -> Html<String> {
    state.db.update_name(id, &input.name).await.unwrap();

    Html(format!(r#"
        <span id="name-{}"
              hx-get="/api/items/{}/edit-name"
              hx-trigger="click"
              hx-swap="outerHTML"
              class="editable cursor-pointer hover:bg-yellow-100 px-1 rounded"
              title="Click to edit">
            {}
        </span>
    "#, id, id, input.name))
}'''

        return {
            "component_type": "inline_edit",
            "html": html,
            "axum_handler": rust,
            "patterns_used": ["hx-get", "hx-put", "hx-trigger", "hx-swap", "hx-on"]
        }


# ================================
# MCP TOOLS
# ================================

@mcp.tool(tags=["analysis", "htmx", "scoring"])
async def analyze_htmx_code(code: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Analyzes HTMX code for patterns and best practices.

    Args:
        code: HTMX HTML code for analysis

    Returns:
        Complete analysis with score and suggestions
    """
    try:
        analyzer = HTMXAnalyzer()
        analysis = await analyzer.analyze_htmx_code(code)

        logger.info(f"Analyzed HTMX code - score: {analysis.score}")

        return {
            "score": analysis.score,
            "grade": (
                "Excellent" if analysis.score >= 90 else
                "Good" if analysis.score >= 75 else
                "Needs Improvement" if analysis.score >= 60 else
                "Poor"
            ),
            "category_scores": analysis.category_scores,
            "patterns_found": analysis.patterns_found,
            "anti_patterns": analysis.anti_patterns_found,
            "suggestions": analysis.suggestions,
            "suggested_axum_handlers": analysis.axum_handlers
        }

    except Exception as e:
        logger.error(f"Error analyzing HTMX code: {str(e)}")
        raise


@mcp.tool(tags=["generation", "component", "htmx"])
async def generate_htmx_component(
    component_type: str,
    endpoint: Optional[str] = None,
    options: Optional[Dict[str, Any]] = None,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Generates HTMX component with Axum handler.

    Args:
        component_type: Component type (form, list, search, modal, tabs, infinite_scroll, inline_edit)
        endpoint: API endpoint for the component
        options: Additional options for component generation

    Returns:
        Generated HTML and Axum handler code
    """
    try:
        generator = HTMXGenerator()

        if options is None:
            options = {}
        if endpoint:
            options["endpoint"] = endpoint

        result = await generator.generate_component(component_type, options)

        logger.info(f"Generated HTMX component: {component_type}")

        return result

    except Exception as e:
        logger.error(f"Error generating HTMX component: {str(e)}")
        raise


@mcp.tool(tags=["generation", "axum", "rust"])
async def generate_axum_handler(
    method: str,
    endpoint: str,
    response_type: str = "html",
    has_form: bool = False,
    has_path_params: bool = False,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Generates Axum handler for HTMX endpoint.

    Args:
        method: HTTP method (GET, POST, PUT, PATCH, DELETE)
        endpoint: API endpoint path
        response_type: Response type (html, status, redirect)
        has_form: Whether handler expects form data
        has_path_params: Whether handler has path parameters

    Returns:
        Generated Axum handler code
    """
    try:
        method = method.upper()

        # Build extractors
        extractors = ["State(state): State<AppState>"]

        if has_path_params:
            # Extract param names from endpoint
            params = re.findall(r':(\w+)', endpoint)
            if params:
                if len(params) == 1:
                    extractors.append(f"Path({params[0]}): Path<u32>")
                else:
                    extractors.append(f"Path(({', '.join(params)})): Path<({', '.join(['u32'] * len(params))})>")

        if has_form and method in ["POST", "PUT", "PATCH"]:
            extractors.append("Form(input): Form<FormInput>")

        # Build return type
        return_type = {
            "html": "Html<String>",
            "status": "impl IntoResponse",
            "redirect": "impl IntoResponse"
        }.get(response_type, "Html<String>")

        # Build function body
        if response_type == "html":
            body = '''    // Process request and return HTML fragment
    Html("<div>Response HTML</div>".to_string())'''
        elif response_type == "status":
            body = '''    // Process request and return status
    StatusCode::OK'''
        else:
            body = '''    // Process request and redirect
    Redirect::to("/success")'''

        # Generate handler
        handler_name = endpoint.replace("/", "_").replace(":", "").strip("_")
        handler = f'''async fn {handler_name}(
    {(',\n    '.join(extractors))}
) -> {return_type} {{
{body}
}}'''

        # Generate router line
        route_method = method.lower()
        router_line = f'.route("{endpoint}", {route_method}({handler_name}))'

        return {
            "method": method,
            "endpoint": endpoint,
            "handler": handler,
            "router_line": router_line,
            "imports": [
                "use axum::{extract::{State, Path, Form}, response::Html};",
                "use axum::http::StatusCode;" if response_type == "status" else None,
                "use axum::response::Redirect;" if response_type == "redirect" else None,
            ]
        }

    except Exception as e:
        logger.error(f"Error generating Axum handler: {str(e)}")
        raise


@mcp.tool(tags=["patterns", "reference", "htmx"])
async def get_htmx_patterns(category: str = "all", ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Returns HTMX patterns by category.

    Args:
        category: Pattern category (requests, swap, triggers, targets, events, axum_integration, ui_patterns, all)

    Returns:
        HTMX patterns with examples
    """
    try:
        kb = HTMXKnowledgeBase()

        categories = {
            "requests": kb.REQUEST_ATTRIBUTES,
            "swap": kb.SWAP_PATTERNS,
            "triggers": kb.TRIGGER_PATTERNS,
            "events": kb.EVENTS,
            "axum_integration": kb.AXUM_PATTERNS,
            "ui_patterns": kb.UI_PATTERNS,
        }

        if category == "all":
            return {
                "htmx_version": kb.VERSION,
                "axum_version": kb.AXUM_VERSION,
                "categories": categories,
                "core_attributes": [
                    "hx-get, hx-post, hx-put, hx-patch, hx-delete",
                    "hx-target, hx-swap, hx-trigger",
                    "hx-include, hx-select, hx-indicator",
                    "hx-push-url, hx-boost, hx-confirm"
                ]
            }

        if category not in categories:
            return {"error": f"Category '{category}' not found. Available: {list(categories.keys())}"}

        return {
            "category": category,
            "patterns": categories[category]
        }

    except Exception as e:
        logger.error(f"Error getting HTMX patterns: {str(e)}")
        raise


@mcp.tool(tags=["prompt", "analysis", "htmx"])
async def analyze_htmx_prompt(prompt: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Analyzes a prompt for HTMX development.

    Args:
        prompt: User prompt to analyze

    Returns:
        Analysis with suggestions and improvements
    """
    try:
        score = 50
        suggestions = []
        missing_elements = []

        # Check for component type specification
        if any(word in prompt.lower() for word in ["form", "list", "search", "modal", "tabs", "table"]):
            score += 10
        else:
            missing_elements.append("Specify the UI component type (form, list, search, modal, etc.)")

        # Check for endpoint specification
        if any(word in prompt.lower() for word in ["endpoint", "api", "/api", "route", "url"]):
            score += 10
        else:
            missing_elements.append("Specify API endpoints for HTMX requests")

        # Check for swap strategy mention
        if any(word in prompt.lower() for word in ["swap", "innerhtml", "outerhtml", "replace"]):
            score += 10
        else:
            suggestions.append("Consider specifying swap strategy (innerHTML, outerHTML, beforeend, etc.)")

        # Check for trigger specification
        if any(word in prompt.lower() for word in ["trigger", "click", "change", "submit", "keyup", "load"]):
            score += 10
        else:
            suggestions.append("Specify trigger events (click, change, keyup, load, etc.)")

        # Check for Axum/backend mention
        if any(word in prompt.lower() for word in ["axum", "handler", "rust", "backend", "server"]):
            score += 10
        else:
            suggestions.append("Mention Axum handler requirements for backend integration")

        # Check for UX considerations
        if any(word in prompt.lower() for word in ["loading", "indicator", "feedback", "error", "validation"]):
            score += 10
        else:
            suggestions.append("Consider loading indicators and error handling")

        return {
            "score": min(100, score),
            "quality": (
                "Excellent" if score >= 90 else
                "Good" if score >= 70 else
                "Needs Details" if score >= 50 else
                "Incomplete"
            ),
            "suggestions": suggestions,
            "missing_elements": missing_elements,
            "enhanced_prompt": f"""{prompt}

Additional requirements:
- Use appropriate hx-swap strategy
- Add loading indicators with hx-indicator
- Include error handling for failed requests
- Generate corresponding Axum handlers
- Follow progressive enhancement principles"""
        }

    except Exception as e:
        logger.error(f"Error analyzing HTMX prompt: {str(e)}")
        raise


@mcp.tool(tags=["optimization", "requests", "htmx"])
async def optimize_htmx_requests(code: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Optimizes HTMX code for better performance and UX.

    Args:
        code: HTMX code to optimize

    Returns:
        Optimized code with explanations
    """
    try:
        optimized = code
        changes = []

        # Add debounce to search inputs
        if 'type="search"' in code and 'delay:' not in code:
            optimized = re.sub(
                r'hx-trigger="keyup"',
                'hx-trigger="keyup changed delay:300ms"',
                optimized
            )
            changes.append("Added 300ms debounce to search input to reduce requests")

        # Add loading indicators
        if 'hx-indicator' not in code and ('hx-get' in code or 'hx-post' in code):
            optimized = optimized.replace('>', ' hx-indicator=".htmx-indicator">', 1)
            changes.append("Added loading indicator reference")

        # Add confirmation for delete actions
        if 'hx-delete' in code and 'hx-confirm' not in code:
            optimized = re.sub(
                r'hx-delete="([^"]+)"',
                r'hx-delete="\1" hx-confirm="Are you sure?"',
                optimized
            )
            changes.append("Added confirmation dialog for delete actions")

        # Ensure targets are specified
        if ('hx-get' in code or 'hx-post' in code) and 'hx-target' not in code:
            changes.append("Warning: Consider adding explicit hx-target for predictable updates")

        return {
            "original": code,
            "optimized": optimized,
            "changes": changes,
            "recommendations": [
                "Use hx-trigger with delay for search/filter inputs",
                "Always specify hx-target for clarity",
                "Add hx-indicator for loading states",
                "Use hx-confirm for destructive actions",
                "Consider hx-push-url for navigation state"
            ]
        }

    except Exception as e:
        logger.error(f"Error optimizing HTMX code: {str(e)}")
        raise


# ================================
# MCP PROMPTS
# ================================

@mcp.prompt()
async def design_htmx_app(
    app_description: str,
    features: List[str] = []
) -> List[Dict[str, str]]:
    """
    Generate a prompt to design an HTMX application with Axum.

    Args:
        app_description: Description of the application
        features: Required features
    """
    default_features = ["CRUD operations", "Search", "Pagination"]
    features_list = features if features else default_features

    return [
        {
            "role": "system",
            "content": """You are an expert in HTMX and Axum web development.

Key principles:
1. **Hypermedia-driven**: HTML is the hypermedia
2. **Progressive enhancement**: Works without JavaScript
3. **Server-rendered**: HTML fragments from server
4. **Minimal JavaScript**: Only for enhanced interactions
5. **RESTful endpoints**: Clean API design

HTMX patterns:
- hx-get/post/put/delete for requests
- hx-target for response placement
- hx-swap for content replacement strategy
- hx-trigger for event handling
- hx-indicator for loading states

Axum patterns:
- Html<String> for HTML responses
- Form/Path extractors for input
- State for shared state
- Tower middleware for cross-cutting concerns"""
        },
        {
            "role": "user",
            "content": f"""Design an HTMX application with Axum backend:

Application: {app_description}

Required features:
{chr(10).join(f"- {f}" for f in features_list)}

Please provide:
1. Application architecture overview
2. Route definitions for Axum
3. HTMX templates for each feature
4. Axum handlers for each endpoint
5. State management approach
6. Error handling patterns
7. Loading/progress indicators
8. Accessibility considerations"""
        }
    ]


@mcp.prompt()
async def implement_htmx_feature(
    feature_name: str,
    description: str = ""
) -> List[Dict[str, str]]:
    """
    Generate a prompt to implement an HTMX feature.

    Args:
        feature_name: Name of the feature
        description: Feature description
    """
    return [
        {
            "role": "system",
            "content": """You are an HTMX expert building features with Axum.

Implementation checklist:
1. Define HTML structure with HTMX attributes
2. Create Axum handler returning HTML
3. Add loading indicators
4. Handle errors gracefully
5. Consider accessibility
6. Test progressive enhancement

Common patterns:
- Inline editing: hx-get to load form, hx-put to save
- Infinite scroll: hx-trigger="revealed"
- Search: hx-trigger="keyup changed delay:300ms"
- Modal: hx-target for modal content"""
        },
        {
            "role": "user",
            "content": f"""Implement the following HTMX feature:

Feature: {feature_name}
{f"Description: {description}" if description else ""}

Requirements:
1. Complete HTML with all HTMX attributes
2. Axum handler(s) for all endpoints
3. Loading state handling
4. Error handling
5. Accessibility attributes
6. CSS classes for styling hooks
7. Example of the feature in action"""
        }
    ]


# ================================
# MCP RESOURCES
# ================================

@mcp.resource(uri="guide://htmx-axum-development")
async def get_htmx_axum_guide() -> str:
    """Complete HTMX with Axum development guide"""
    return json.dumps({
        "title": "HTMX with Axum Development Guide 2025",
        "versions": {
            "htmx": "2.0.x",
            "axum": "0.7.x"
        },
        "sections": {
            "core_concepts": "HTMX attributes and hypermedia patterns",
            "axum_integration": "Building HTML-returning handlers",
            "ui_patterns": "Common UI components with HTMX",
            "state_management": "Managing state between requests",
            "error_handling": "Graceful error handling patterns",
            "accessibility": "Building accessible HTMX applications",
            "performance": "Optimizing HTMX applications"
        },
        "key_attributes": {
            "requests": "hx-get, hx-post, hx-put, hx-patch, hx-delete",
            "targeting": "hx-target, hx-swap, hx-select",
            "triggering": "hx-trigger, hx-indicator",
            "history": "hx-push-url, hx-replace-url",
            "enhancement": "hx-boost, hx-confirm"
        },
        "features": {
            "code_analysis": "Analyze HTMX code for best practices",
            "component_generation": "Generate HTMX components with Axum handlers",
            "pattern_library": "Common HTMX + Axum patterns",
            "optimization": "Performance and UX optimization"
        }
    }, indent=2)


# ================================
# SERVER INITIALIZATION
# ================================

if __name__ == "__main__":
    logger.info("HTMX with Axum MCP Server starting...")
    logger.info("Version: HTMX 2.0.x + Axum 0.7.x")
    logger.info("Features: Code Analysis | Component Generation | Axum Integration")
    logger.info("\nAvailable prompts:")
    logger.info("  - design_htmx_app: Design HTMX application architecture")
    logger.info("  - implement_htmx_feature: Implement specific HTMX feature")

    mcp.run()
