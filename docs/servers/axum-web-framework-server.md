# Axum Web Framework Server

The Axum Web Framework Server provides specialized support for developing high-performance web applications using Axum, the modern async web framework built on tokio. It offers code analysis, project generation, and optimization guidance following Axum best practices and magic patterns.

## Overview

This server focuses on Axum web development, providing intelligent analysis of Axum code, automated project scaffolding, and advanced patterns for building scalable, performant web APIs and applications using the tokio ecosystem.

**Port**: 3009  
**Protocol**: stdio  
**Module**: `servers.axum_server`

## Features

### 🚀 Axum Expertise
- **Framework Analysis**: Deep understanding of Axum patterns and best practices
- **Magic Patterns**: Advanced patterns from rust-magic-patterns
- **tokio Integration**: Optimal tokio runtime usage
- **Performance Optimization**: High-throughput web server patterns

### 🏗️ Project Scaffolding
- **Complete Applications**: Full-stack Axum project generation
- **API Servers**: RESTful API with OpenAPI documentation
- **Microservices**: Distributed system patterns
- **Real-time Features**: WebSocket and SSE implementations

### 🔧 Code Enhancement
- **Handler Optimization**: Efficient request handler patterns
- **Middleware Design**: Custom middleware implementation
- **Error Handling**: Robust error management strategies
- **Database Integration**: SQLx, Diesel, and Sea-ORM patterns

## Available Tools

### `analyze_axum_code(code: str)`
Analyzes Axum code following official best practices and magic patterns.

**Parameters:**
- `code` (string): Axum code to analyze

**Returns:**
- `quality_score` (number): Code quality score (0-100)
- `patterns_detected` (array): Identified Axum patterns
- `performance_issues` (array): Performance bottlenecks
- `security_concerns` (array): Security-related issues
- `recommendations` (array): Improvement suggestions
- `magic_patterns` (array): Advanced patterns that could be applied

**Analysis Areas:**
- **Handler Design**: Request handler implementation quality
- **Middleware Usage**: Proper middleware composition
- **Error Handling**: Robust error management
- **State Management**: Application state patterns
- **Route Organization**: Route structure and grouping

### `generate_axum_project(project_type: str, options?)`
Generates complete Axum projects with modern patterns.

**Parameters:**
- `project_type` (string): Type of project to generate
- `features` (array, optional): Additional features to include
- `include_database` (boolean): Include database integration
- `include_auth` (boolean): Include authentication system

**Project Types:**
- `"api_server"` - RESTful API server
- `"web_application"` - Full-stack web application
- `"microservice"` - Microservice architecture
- `"full_stack"` - Complete application with frontend

**Features:**
- `"database"` - SQLx/Diesel database integration
- `"authentication"` - JWT/OAuth authentication
- `"websockets"` - WebSocket support
- `"openapi"` - OpenAPI documentation
- `"metrics"` - Prometheus metrics
- `"tracing"` - Structured logging

**Returns:**
- `project_structure` (object): Complete file structure
- `cargo_toml` (string): Cargo.toml with dependencies
- `source_files` (object): All source code files
- `configuration` (object): Environment and config files
- `documentation` (string): README and API docs

### `get_axum_patterns(category: str = "all")`
Returns Axum patterns organized by category with practical examples.

**Parameters:**
- `category` (string): Specific pattern category

**Categories:**
- `"handlers"` - Request handler patterns
- `"middleware"` - Middleware implementation patterns
- `"routing"` - Route organization and nesting
- `"state"` - Application state management
- `"errors"` - Error handling strategies
- `"testing"` - Testing patterns and utilities

**Returns:**
- Comprehensive pattern library with code examples
- Performance implications and trade-offs
- Security considerations for each pattern

### `optimize_axum_handler(handler_code: str, focus_areas?: string[])`
Optimizes Axum handlers applying best practices and magic patterns.

**Parameters:**
- `handler_code` (string): Original handler code
- `focus_areas` (array, optional): Specific optimization areas

**Focus Areas:**
- `"performance"` - Memory and CPU optimization
- `"error_handling"` - Robust error management
- `"validation"` - Input validation improvements
- `"async"` - Async/await pattern optimization
- `"security"` - Security enhancement

**Returns:**
- `original_code` (string): Original handler code
- `optimized_code` (string): Improved version
- `optimizations_applied` (array): List of applied improvements
- `performance_impact` (string): Expected performance gain
- `explanation` (string): Detailed explanation of changes

### `get_axum_magic_patterns()`
Returns advanced Axum patterns based on rust-magic-patterns.

**Returns:**
- **Zero-Copy Patterns**: Efficient data handling without cloning
- **Type-State Patterns**: Compile-time state management
- **Extension Patterns**: Flexible handler extension mechanisms
- **Performance Patterns**: High-throughput optimization techniques
- **Safety Patterns**: Memory-safe concurrent patterns

### `create_axum_middleware(middleware_type: str, functionality: str)`
Creates custom Axum middleware with best practices.

**Parameters:**
- `middleware_type` (string): Type of middleware
- `functionality` (string): Specific functionality description

**Middleware Types:**
- `"auth"` - Authentication and authorization
- `"logging"` - Request/response logging
- `"cors"` - Cross-origin resource sharing
- `"rate_limiting"` - Request rate limiting
- `"compression"` - Response compression
- `"metrics"` - Performance metrics collection

**Returns:**
- Complete middleware implementation
- Usage examples and integration guide
- Performance considerations and best practices

## Axum Patterns

### Handler Patterns
```rust
// Basic handler
async fn get_user(Path(id): Path<u32>) -> Result<Json<User>, AppError> {
    let user = fetch_user(id).await?;
    Ok(Json(user))
}

// Handler with state and validation
async fn create_user(
    State(db): State<DatabasePool>,
    ValidatedJson(payload): ValidatedJson<CreateUser>,
) -> Result<Json<User>, AppError> {
    let user = db.create_user(payload).await?;
    Ok(Json(user))
}
```

### Middleware Patterns
```rust
// Custom middleware
pub fn auth_middleware() -> Middleware<Request<Body>, Response<Body>, Infallible> {
    middleware::from_fn(|req: Request<Body>, next: Next<Body>| async move {
        // Authentication logic
        let response = next.run(req).await;
        response
    })
}
```

### Route Organization
```rust
// Modular routing
fn api_routes() -> Router<AppState> {
    Router::new()
        .nest("/users", user_routes())
        .nest("/posts", post_routes())
        .layer(auth_middleware())
}

fn user_routes() -> Router<AppState> {
    Router::new()
        .route("/", get(list_users).post(create_user))
        .route("/:id", get(get_user).put(update_user).delete(delete_user))
}
```

### Error Handling
```rust
// Custom error type
#[derive(Debug)]
pub enum AppError {
    Database(sqlx::Error),
    Validation(validator::ValidationErrors),
    NotFound,
    Unauthorized,
}

impl IntoResponse for AppError {
    fn into_response(self) -> Response {
        let (status, error_message) = match self {
            AppError::Database(_) => (StatusCode::INTERNAL_SERVER_ERROR, "Database error"),
            AppError::Validation(_) => (StatusCode::BAD_REQUEST, "Validation error"),
            AppError::NotFound => (StatusCode::NOT_FOUND, "Resource not found"),
            AppError::Unauthorized => (StatusCode::UNAUTHORIZED, "Unauthorized"),
        };

        let body = Json(json!({
            "error": error_message,
        }));

        (status, body).into_response()
    }
}
```

## Magic Patterns

### Zero-Copy JSON
```rust
// Efficient JSON handling without cloning
use axum::extract::RawBody;
use serde_json::from_slice;

async fn efficient_json_handler(
    RawBody(body): RawBody,
) -> Result<Json<ProcessedData>, AppError> {
    let data: InputData = from_slice(&body).map_err(AppError::InvalidJson)?;
    let processed = process_data_zero_copy(&data);
    Ok(Json(processed))
}
```

### Type-State Builder
```rust
// Compile-time validated API builder
pub struct ApiBuilder<S> {
    state: PhantomData<S>,
    router: Router,
}

impl ApiBuilder<Uninitialized> {
    pub fn new() -> Self {
        Self {
            state: PhantomData,
            router: Router::new(),
        }
    }
    
    pub fn with_auth(self) -> ApiBuilder<WithAuth> {
        // Add authentication middleware
    }
}
```

### Performance Patterns
```rust
// High-performance connection pooling
pub struct OptimizedPool {
    pool: bb8::Pool<bb8_postgres::PostgresConnectionManager<tokio_postgres::NoTls>>,
    metrics: Arc<Metrics>,
}

impl OptimizedPool {
    pub async fn get_connection(&self) -> Result<PooledConnection, PoolError> {
        let start = Instant::now();
        let conn = self.pool.get().await?;
        self.metrics.record_connection_time(start.elapsed());
        Ok(conn)
    }
}
```

## Project Templates

### API Server Template
```toml
[package]
name = "axum-api"
version = "0.1.0"
edition = "2021"

[dependencies]
axum = { version = "0.7", features = ["macros"] }
tokio = { version = "1.0", features = ["full"] }
tower = "0.4"
tower-http = { version = "0.5", features = ["fs", "trace", "cors"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
sqlx = { version = "0.7", features = ["runtime-tokio-rustls", "postgres", "uuid"] }
uuid = { version = "1.0", features = ["v4", "serde"] }
tracing = "0.1"
tracing-subscriber = "0.3"
thiserror = "1.0"
anyhow = "1.0"
```

### Microservice Template
```rust
use axum::{
    extract::State,
    http::StatusCode,
    response::Json,
    routing::{get, post},
    Router,
};
use std::sync::Arc;
use tokio::net::TcpListener;
use tower_http::{
    cors::CorsLayer,
    trace::TraceLayer,
};

#[derive(Clone)]
pub struct AppState {
    database: Arc<Database>,
    cache: Arc<Cache>,
    metrics: Arc<Metrics>,
}

pub fn create_app(state: AppState) -> Router {
    Router::new()
        .route("/health", get(health_check))
        .route("/api/v1/users", post(create_user))
        .route("/api/v1/users/:id", get(get_user))
        .with_state(state)
        .layer(CorsLayer::permissive())
        .layer(TraceLayer::new_for_http())
}

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let state = AppState::new().await?;
    let app = create_app(state);
    
    let listener = TcpListener::bind("0.0.0.0:3000").await?;
    axum::serve(listener, app).await?;
    
    Ok(())
}
```

## Performance Optimization

### High-Throughput Patterns
- **Connection Pooling**: Efficient database connection management
- **Async Batching**: Batch multiple requests for better throughput
- **Memory Pools**: Custom allocators for hot paths
- **Zero-Copy**: Minimize data copying in request/response cycle

### Concurrent Patterns
- **Shared State**: Arc + RwLock for read-heavy workloads
- **Message Passing**: Channel-based communication
- **Actor Pattern**: Lightweight actor system with tokio
- **Work Stealing**: Efficient task distribution

## Usage Examples

### Code Analysis
```python
analysis = analyze_axum_code("""
async fn get_users() -> Json<Vec<User>> {
    let users = fetch_all_users().await;
    Json(users)
}
""")
# Returns: score: 45, issues: ["Missing error handling", "No input validation"]
```

### Project Generation
```python
project = generate_axum_project(
    "api_server",
    features=["database", "authentication", "metrics"],
    include_auth=True
)
# Returns complete API server with JWT auth and PostgreSQL
```

### Handler Optimization
```python
optimized = optimize_axum_handler(handler_code, ["error_handling", "performance"])
# Returns optimized handler with proper error handling and performance improvements
```

## Configuration

Environment variables:
- `MCP_SERVER_PORT`: Server port (default: 3009)
- `MCP_SERVER_PROTOCOL`: Communication protocol (default: stdio)
- `AXUM_VERSION`: Target Axum version (default: latest)

## Dependencies

- **Axum Framework**: 0.7+
- **tokio Runtime**: 1.0+
- **Tower Ecosystem**: Middleware and services
- **FastMCP**: 2.4.0+

---

*This server is part of the MCP Servers Collection developed by Charleno Pires*