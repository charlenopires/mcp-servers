#!/usr/bin/env python3
"""
Axum Web Framework MCP Server
=============================

Advanced MCP server for modern web development with Axum, featuring:
- Axum code analysis following official best practices
- Routing patterns, middleware, and handler optimization
- Idiomatic extractors and responses
- Robust error handling with Tower ecosystem
- State management and testing patterns
- Rust magic patterns for metaprogramming
- Performance optimization with async/await

Based on: tokio-rs/axum, docs.rs/axum, alexpusch/rust-magic-patterns
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

# Initialize FastMCP server (following pattern of other servers)
mcp = FastMCP(
    name="Axum Web Framework Server",
    instructions="""Advanced MCP server for modern web development with Axum framework.

This server provides Axum web framework expertise:
- Code analysis following official Axum patterns
- Routing, handlers, middleware, and extractor optimization
- Tower ecosystem integration and error handling
- State management and testing patterns
- Rust magic patterns for advanced metaprogramming

Use these tools to build high-performance async web services.""",
    version="3.0.0"
)

# ================================
# AXUM KNOWLEDGE BASE & PATTERNS
# ================================

class AxumFeatureType(Enum):
    """Axum feature categories"""
    ROUTING = "routing"
    HANDLERS = "handlers"
    EXTRACTORS = "extractors"
    RESPONSES = "responses"
    MIDDLEWARE = "middleware"
    ERROR_HANDLING = "error_handling"
    STATE_MANAGEMENT = "state_management"
    TESTING = "testing"
    PERFORMANCE = "performance"
    MAGIC_PATTERNS = "magic_patterns"

class ProjectType(Enum):
    """Axum project types"""
    API_SERVER = "api_server"
    WEB_APPLICATION = "web_application"
    MICROSERVICE = "microservice"
    FULL_STACK = "full_stack"
    REAL_TIME = "real_time"

@dataclass
class AxumAnalysisResult:
    """Axum code analysis result"""
    code: str
    score: int
    routing_patterns: Dict[str, bool]
    handler_quality: Dict[str, bool]
    extractor_usage: Dict[str, bool]
    middleware_patterns: Dict[str, bool]
    error_handling: Dict[str, bool]
    performance_issues: List[str]
    security_concerns: List[str]
    best_practices_compliance: Dict[str, bool]
    magic_patterns_detected: List[str]
    recommendations: List[str]

class AxumKnowledgeBase:
    """Axum knowledge base based on tokio-rs/axum and magic patterns"""
    
    VERSION = "0.8.0"
    MSRV = "1.78"  # Minimum Supported Rust Version
    
    # Pattern: Modern Routing
    ROUTING_PATTERNS = {
        "macro_free_routing": {
            "description": "Macro-free routing using Router API",
            "best_practice": "Use Router::new() with chained methods to define routes",
            "example": """
// Idiomatic: declarative routing without macros
use axum::{Router, routing::{get, post}};

fn create_app() -> Router {
    Router::new()
        .route("/", get(root))
        .route("/users", get(list_users).post(create_user))
        .route("/users/:id", get(get_user).put(update_user).delete(delete_user))
        .nest("/api/v1", api_v1_routes())
        .fallback(not_found)
}

fn api_v1_routes() -> Router {
    Router::new()
        .route("/health", get(health_check))
        .route("/metrics", get(metrics))
}""",
            "anti_pattern": """
// Anti-pattern: unorganized routes
let app = Router::new()
    .route("/users", get(users_handler))
    .route("/users/create", post(create_handler))
    .route("/users/update", put(update_handler)); // inconsistent with REST
""",
            "benefits": [
                "Type-safe routing without runtime overhead",
                "Modular route composition",
                "Perfect integration with Tower middleware",
                "Compile-time errors for malformed routes"
            ]
        },
        "nested_routing": {
            "description": "Hierarchical route organization with nest",
            "best_practice": "Use nest() to organize routes in logical modules",
            "example": """
// Modular organization with nest
fn app() -> Router<AppState> {
    Router::new()
        .nest("/api/v1", api_routes())
        .nest("/admin", admin_routes())
        .nest("/auth", auth_routes())
        .fallback(handle_404)
}

fn api_routes() -> Router<AppState> {
    Router::new()
        .route("/users", get(list_users).post(create_user))
        .route("/posts", get(list_posts).post(create_post))
        .layer(auth_middleware())
}

fn admin_routes() -> Router<AppState> {
    Router::new()
        .route("/dashboard", get(admin_dashboard))
        .route("/users", get(admin_users))
        .layer(admin_auth_middleware())
}"""
        }
    }
    
    # Pattern: Idiomatic Handlers
    HANDLER_PATTERNS = {
        "async_handlers": {
            "description": "Async handlers with extractor patterns",
            "best_practice": "Handlers should be async functions with typed extractors",
            "example": """
use axum::{Json, Path, Query, extract::State};
use serde::{Deserialize, Serialize};

#[derive(Deserialize)]
struct CreateUserRequest {
    name: String,
    email: String,
}

#[derive(Serialize)]
struct User {
    id: u32,
    name: String,
    email: String,
}

// Idiomatic handler with multiple extractors
async fn create_user(
    State(db): State<DatabasePool>,
    Json(payload): Json<CreateUserRequest>,
) -> Result<Json<User>, AppError> {
    let user = User {
        id: generate_id(),
        name: payload.name,
        email: payload.email,
    };
    
    db.save_user(&user).await?;
    Ok(Json(user))
}

// Handler with Path and Query extractors
async fn get_user_posts(
    Path(user_id): Path<u32>,
    Query(params): Query<HashMap<String, String>>,
    State(db): State<DatabasePool>,
) -> Result<Json<Vec<Post>>, AppError> {
    let limit = params.get("limit")
        .and_then(|s| s.parse().ok())
        .unwrap_or(10);
        
    let posts = db.get_user_posts(user_id, limit).await?;
    Ok(Json(posts))
}""",
            "anti_pattern": """
// Anti-pattern: untyped handler with manual error handling
async fn bad_handler(req: Request<Body>) -> Response<Body> {
    let body = hyper::body::to_bytes(req.into_body()).await.unwrap();
    let json: serde_json::Value = serde_json::from_slice(&body).unwrap();
    // manual parsing, without type safety
    Response::new(Body::from("ok"))
}"""
        },
        "handler_composition": {
            "description": "Handler composition and reuse",
            "example": """
// Composable and reusable handlers
async fn authenticated_handler<T>(
    auth: AuthExtractor,
    handler: impl Fn(User) -> T,
) -> Result<T, AuthError> 
where
    T: IntoResponse,
{
    let user = auth.authenticate().await?;
    Ok(handler(user))
}

// Middleware-style handler composition
fn with_auth<H, T>(handler: H) -> impl Fn(AuthExtractor) -> Result<T, AuthError>
where
    H: Fn(User) -> T,
    T: IntoResponse,
{
    move |auth: AuthExtractor| async move {
        let user = auth.authenticate().await?;
        Ok(handler(user))
    }
}"""
        }
    }
    
    # Pattern: Advanced Extractors
    EXTRACTOR_PATTERNS = {
        "builtin_extractors": {
            "description": "Built-in Axum extractors",
            "patterns": {
                "Json": "Extract and deserialize JSON from request body",
                "Path": "Extract parameters from URL path",
                "Query": "Extract query parameters",
                "State": "Access to application state",
                "Headers": "Access to HTTP headers",
                "Extension": "Custom request extensions"
            },
            "example": """
use axum::extract::{Path, Query, Json, State, HeaderMap};

// Multiple extractors in one handler
async fn complex_handler(
    Path(id): Path<u32>,
    Query(params): Query<SearchParams>,
    Json(payload): Json<UpdateData>,
    State(app_state): State<AppState>,
    headers: HeaderMap,
) -> Result<Json<Response>, AppError> {
    // All extractors are automatically validated
    let user_agent = headers.get("user-agent");
    let result = app_state.update_item(id, payload, params).await?;
    Ok(Json(result))
}

#[derive(Deserialize)]
struct SearchParams {
    limit: Option<u32>,
    offset: Option<u32>,
    sort: Option<String>,
}"""
        },
        "custom_extractors": {
            "description": "Custom extractors with FromRequest",
            "example": """
use axum::{async_trait, extract::FromRequestParts, http::request::Parts};

// Custom extractor for authentication
struct AuthenticatedUser {
    id: u32,
    email: String,
}

#[async_trait]
impl<S> FromRequestParts<S> for AuthenticatedUser
where
    S: Send + Sync,
{
    type Rejection = AuthError;

    async fn from_request_parts(
        parts: &mut Parts, 
        state: &S
    ) -> Result<Self, Self::Rejection> {
        let auth_header = parts.headers
            .get("Authorization")
            .ok_or(AuthError::MissingToken)?;
            
        let token = auth_header
            .to_str()
            .map_err(|_| AuthError::InvalidToken)?
            .strip_prefix("Bearer ")
            .ok_or(AuthError::InvalidToken)?;
            
        let user = validate_token(token).await?;
        Ok(user)
    }
}

// Using custom extractor
async fn protected_handler(
    auth_user: AuthenticatedUser,
    Json(data): Json<UpdateData>,
) -> Result<Json<Success>, AppError> {
    // auth_user is already validated automatically
    process_authenticated_request(auth_user.id, data).await
}"""
        }
    }
    
    # Pattern: Idiomatic Responses
    RESPONSE_PATTERNS = {
        "into_response": {
            "description": "Response types with IntoResponse trait",
            "example": """
use axum::{response::IntoResponse, http::StatusCode, Json};

// Different response types
async fn json_response() -> Json<User> {
    Json(User { id: 1, name: "John".to_string() })
}

async fn status_response() -> StatusCode {
    StatusCode::NO_CONTENT
}

async fn tuple_response() -> (StatusCode, Json<ErrorResponse>) {
    (StatusCode::BAD_REQUEST, Json(ErrorResponse {
        error: "Invalid input".to_string()
    }))
}

// Custom response type
#[derive(Serialize)]
struct ApiResponse<T> {
    success: bool,
    data: Option<T>,
    error: Option<String>,
}

impl<T> IntoResponse for ApiResponse<T>
where
    T: Serialize,
{
    fn into_response(self) -> axum::response::Response {
        let status = if self.success {
            StatusCode::OK
        } else {
            StatusCode::BAD_REQUEST
        };
        
        (status, Json(self)).into_response()
    }
}"""
        },
        "streaming_responses": {
            "description": "Streaming responses for large data",
            "example": """
use axum::body::StreamBody;
use futures::stream::{self, StreamExt};

async fn stream_data() -> StreamBody<impl Stream<Item = Result<Bytes, io::Error>>> {
    let stream = stream::iter(0..1000)
        .map(|i| Ok(Bytes::from(format!("data chunk {}\\n", i))));
    
    StreamBody::new(stream)
}

async fn sse_handler() -> Sse<impl Stream<Item = Result<Event, Infallible>>> {
    let stream = stream::repeat_with(|| {
        Event::default().data(format!("timestamp: {}", SystemTime::now()))
    })
    .map(Ok);
    
    Sse::new(stream)
}"""
        }
    }
    
    # Pattern: Middleware Patterns
    MIDDLEWARE_PATTERNS = {
        "tower_middleware": {
            "description": "Integration with Tower ecosystem",
            "example": """
use tower::{ServiceBuilder, timeout::TimeoutLayer, limit::RateLimitLayer};
use tower_http::{cors::CorsLayer, trace::TraceLayer};

fn create_app() -> Router {
    let middleware_stack = ServiceBuilder::new()
        .layer(TraceLayer::new_for_http())
        .layer(TimeoutLayer::new(Duration::from_secs(30)))
        .layer(CorsLayer::permissive())
        .layer(RateLimitLayer::new(100, Duration::from_secs(60)));

    Router::new()
        .route("/api/users", get(list_users))
        .layer(middleware_stack)
}"""
        },
        "custom_middleware": {
            "description": "Custom middleware with layer pattern",
            "example": """
use axum::{middleware::Next, http::Request, response::Response};

// Middleware function
async fn auth_middleware<B>(
    req: Request<B>,
    next: Next<B>,
) -> Result<Response, StatusCode> {
    let auth_header = req.headers()
        .get("Authorization")
        .ok_or(StatusCode::UNAUTHORIZED)?;
    
    // Validate token
    if !is_valid_token(auth_header) {
        return Err(StatusCode::UNAUTHORIZED);
    }
    
    Ok(next.run(req).await)
}

// Apply middleware
let app = Router::new()
    .route("/protected", get(protected_handler))
    .layer(axum::middleware::from_fn(auth_middleware));"""
        }
    }
    
    # Pattern: Robust Error Handling
    ERROR_HANDLING_PATTERNS = {
        "custom_error_types": {
            "description": "Custom error types with IntoResponse",
            "example": """
use axum::{response::IntoResponse, http::StatusCode, Json};
use thiserror::Error;

#[derive(Error, Debug)]
pub enum AppError {
    #[error("Database error: {0}")]
    Database(#[from] sqlx::Error),
    
    #[error("Validation error: {0}")]
    Validation(String),
    
    #[error("Not found: {resource}")]
    NotFound { resource: String },
    
    #[error("Unauthorized")]
    Unauthorized,
}

impl IntoResponse for AppError {
    fn into_response(self) -> axum::response::Response {
        let (status, error_message) = match self {
            AppError::Database(_) => {
                (StatusCode::INTERNAL_SERVER_ERROR, "Database error")
            }
            AppError::Validation(msg) => {
                (StatusCode::BAD_REQUEST, msg.as_str())
            }
            AppError::NotFound { .. } => {
                (StatusCode::NOT_FOUND, "Resource not found")
            }
            AppError::Unauthorized => {
                (StatusCode::UNAUTHORIZED, "Unauthorized")
            }
        };

        let body = Json(serde_json::json!({
            "error": error_message,
        }));

        (status, body).into_response()
    }
}

// Usage in handlers
async fn get_user(Path(id): Path<u32>) -> Result<Json<User>, AppError> {
    let user = database::get_user(id)
        .await?
        .ok_or_else(|| AppError::NotFound { 
            resource: format!("User with id {}", id) 
        })?;
    
    Ok(Json(user))
}"""
        },
        "error_layer": {
            "description": "Error handling layer for centralized treatment",
            "example": """
use axum::error_handling::HandleErrorLayer;

let app = Router::new()
    .route("/", get(handler))
    .layer(
        ServiceBuilder::new()
            .layer(HandleErrorLayer::new(|error: BoxError| async move {
                if error.is::<tower::timeout::error::Elapsed>() {
                    Ok(StatusCode::REQUEST_TIMEOUT)
                } else {
                    Err((
                        StatusCode::INTERNAL_SERVER_ERROR,
                        format!("Unhandled internal error: {}", error),
                    ))
                }
            }))
            .layer(TimeoutLayer::new(Duration::from_secs(10)))
    );"""
        }
    }
    
    # Pattern: State Management
    STATE_MANAGEMENT_PATTERNS = {
        "shared_state": {
            "description": "Shared state with Arc and State extractor",
            "example": """
use std::sync::Arc;
use axum::extract::State;

#[derive(Clone)]
struct AppState {
    db: DatabasePool,
    config: AppConfig,
    cache: Arc<Cache>,
}

async fn create_user(
    State(state): State<AppState>,
    Json(user_data): Json<CreateUserRequest>,
) -> Result<Json<User>, AppError> {
    // Access to shared state
    let user = state.db.create_user(user_data).await?;
    state.cache.invalidate("users").await;
    Ok(Json(user))
}

// App setup
let shared_state = AppState {
    db: create_db_pool().await,
    config: load_config(),
    cache: Arc::new(Cache::new()),
};

let app = Router::new()
    .route("/users", post(create_user))
    .with_state(shared_state);"""
        },
        "extension_state": {
            "description": "Per-request state with Extension",
            "example": """
use axum::{Extension, middleware::Next, http::Request};

// Middleware that adds per-request context
async fn add_request_context<B>(
    mut req: Request<B>,
    next: Next<B>,
) -> Result<Response, StatusCode> {
    let request_id = Uuid::new_v4();
    let context = RequestContext {
        id: request_id,
        started_at: Instant::now(),
    };
    
    req.extensions_mut().insert(context);
    Ok(next.run(req).await)
}

async fn handler(Extension(ctx): Extension<RequestContext>) -> Json<Value> {
    Json(json!({
        "request_id": ctx.id,
        "duration": ctx.started_at.elapsed()
    }))
}"""
        }
    }
    
    # Pattern: Testing Patterns
    TESTING_PATTERNS = {
        "integration_tests": {
            "description": "Integration tests with TestClient",
            "example": """
use axum_test::TestServer;
use tower::ServiceExt;

#[tokio::test]
async fn test_create_user() {
    let app = create_test_app().await;
    let server = TestServer::new(app).unwrap();

    let user_data = json!({
        "name": "John Doe",
        "email": "john@example.com"
    });

    let response = server
        .post("/users")
        .json(&user_data)
        .await;

    assert_eq!(response.status_code(), 201);
    
    let user: User = response.json();
    assert_eq!(user.name, "John Doe");
    assert_eq!(user.email, "john@example.com");
}

// Test helpers
async fn create_test_app() -> Router {
    let test_state = create_test_state().await;
    create_app().with_state(test_state)
}

async fn create_test_state() -> AppState {
    AppState {
        db: create_test_db().await,
        config: test_config(),
    }
}"""
        },
        "mock_extractors": {
            "description": "Mock extractors for unit tests",
            "example": """
// Unit test for specific handler
#[tokio::test]
async fn test_get_user_handler() {
    let mock_state = create_mock_state();
    let user_id = 42;
    
    let result = get_user(
        Path(user_id),
        State(mock_state),
    ).await;
    
    assert!(result.is_ok());
    let Json(user) = result.unwrap();
    assert_eq!(user.id, user_id);
}"""
        }
    }
    
    # Pattern: Magic Patterns (based on alexpusch/rust-magic-patterns)
    MAGIC_PATTERNS = {
        "axum_function_parameters": {
            "description": "Magic function parameters like in Axum",
            "explanation": "Axum uses traits and type system to enable handlers with flexible signatures",
            "example": """
// Magic: different handler signatures work
async fn handler1() -> &'static str { "hello" }
async fn handler2(Path(id): Path<u32>) -> String { format!("id: {}", id) }
async fn handler3(
    Path(id): Path<u32>,
    Json(data): Json<Value>
) -> Json<Response> { /* ... */ }

// How it works internally (simplified):
trait Handler<T> {
    fn call(self, extractors: T) -> impl Future<Output = Response>;
}

// Implementation for different arities
impl<F, Fut> Handler<()> for F
where
    F: FnOnce() -> Fut,
    Fut: Future<Output = impl IntoResponse>,
{
    fn call(self, _: ()) -> impl Future<Output = Response> {
        async move { self().await.into_response() }
    }
}

impl<F, Fut, T1> Handler<(T1,)> for F
where
    F: FnOnce(T1) -> Fut,
    Fut: Future<Output = impl IntoResponse>,
    T1: FromRequestParts,
{
    fn call(self, (t1,): (T1,)) -> impl Future<Output = Response> {
        async move { self(t1).await.into_response() }
    }
}"""
        },
        "async_pipeline": {
            "description": "Async pipeline for data processing",
            "example": """
use tokio::sync::mpsc;
use futures::stream::{Stream, StreamExt};

// Async pipeline for request processing
struct RequestPipeline {
    input: mpsc::Receiver<Request>,
    output: mpsc::Sender<Response>,
}

impl RequestPipeline {
    async fn process(mut self) {
        while let Some(request) = self.input.recv().await {
            let response = self.process_request(request).await;
            let _ = self.output.send(response).await;
        }
    }
    
    async fn process_request(&self, req: Request) -> Response {
        // Pipeline stages
        let validated = self.validate(req).await?;
        let enriched = self.enrich(validated).await?;
        let processed = self.business_logic(enriched).await?;
        self.format_response(processed).await
    }
}

// Stream-based processing
fn create_processing_stream() -> impl Stream<Item = ProcessedData> {
    futures::stream::iter(input_data)
        .map(|item| async move { validate(item).await })
        .buffered(10) // Process up to 10 items concurrently
        .filter_map(|result| async move { result.ok() })
        .map(|item| async move { transform(item).await })
        .buffered(5)
}"""
        },
        "type_level_routing": {
            "description": "Type-level routing for type safety",
            "example": """
// Type-safe routing with phantom types
use std::marker::PhantomData;

struct Route<T> {
    path: &'static str,
    _phantom: PhantomData<T>,
}

struct GetUser;
struct CreateUser;
struct UpdateUser;

const GET_USER: Route<GetUser> = Route {
    path: "/users/:id",
    _phantom: PhantomData,
};

const CREATE_USER: Route<CreateUser> = Route {
    path: "/users",
    _phantom: PhantomData,
};

// Handler registration with type safety
trait RouteHandler<T> {
    type Response: IntoResponse;
    fn handle(&self) -> Self::Response;
}

impl RouteHandler<GetUser> for MyHandler {
    type Response = Json<User>;
    fn handle(&self) -> Self::Response {
        // Implementation
    }
}

// Router that ensures type safety
fn register_route<T, H>(route: Route<T>, handler: H) -> RouterBuilder
where
    H: RouteHandler<T>,
{
    // Type-safe route registration
}"""
        }
    }
    
    # Pattern: Performance Optimization
    PERFORMANCE_PATTERNS = {
        "connection_pooling": {
            "description": "Connection pooling for databases",
            "example": """
use sqlx::{PgPool, postgres::PgPoolOptions};

async fn create_db_pool() -> PgPool {
    PgPoolOptions::new()
        .max_connections(20)
        .min_connections(5)
        .acquire_timeout(Duration::from_secs(30))
        .idle_timeout(Duration::from_secs(600))
        .max_lifetime(Duration::from_secs(1800))
        .connect(&database_url)
        .await
        .expect("Failed to create pool")
}

#[derive(Clone)]
struct AppState {
    db: PgPool,
}

async fn get_users(State(state): State<AppState>) -> Result<Json<Vec<User>>, AppError> {
    let users = sqlx::query_as!(User, "SELECT * FROM users")
        .fetch_all(&state.db)
        .await?;
    Ok(Json(users))
}"""
        },
        "caching_layer": {
            "description": "Caching layer for responses",
            "example": """
use moka::future::Cache;
use std::time::Duration;

#[derive(Clone)]
struct CacheState {
    cache: Cache<String, Vec<u8>>,
}

impl CacheState {
    fn new() -> Self {
        let cache = Cache::builder()
            .max_capacity(10_000)
            .time_to_live(Duration::from_secs(300))
            .build();
        Self { cache }
    }
}

async fn cached_handler(
    Path(id): Path<String>,
    State(cache_state): State<CacheState>,
) -> Result<impl IntoResponse, AppError> {
    let cache_key = format!("user:{}", id);
    
    if let Some(cached) = cache_state.cache.get(&cache_key).await {
        return Ok(cached);
    }
    
    let data = expensive_computation(id).await?;
    let serialized = serde_json::to_vec(&data)?;
    
    cache_state.cache.insert(cache_key, serialized.clone()).await;
    Ok(serialized)
}"""
        },
        "streaming_optimization": {
            "description": "Optimizations for streaming large data",
            "example": """
use futures::stream::{Stream, StreamExt};
use tokio_util::io::ReaderStream;

async fn stream_large_file(
    Path(filename): Path<String>
) -> Result<impl IntoResponse, AppError> {
    let file = tokio::fs::File::open(&filename).await?;
    let reader = tokio::io::BufReader::new(file);
    let stream = ReaderStream::new(reader);
    
    let headers = [
        ("content-type", "application/octet-stream"),
        ("content-disposition", &format!("attachment; filename=\\"{}\\"", filename)),
    ];
    
    Ok((headers, StreamBody::new(stream)))
}

// Chunked JSON streaming for APIs
async fn stream_json_array<T>(
    data: impl Stream<Item = T> + Send + 'static
) -> impl IntoResponse 
where
    T: Serialize + Send + 'static,
{
    let stream = data
        .enumerate()
        .map(|(i, item)| {
            let prefix = if i == 0 { "[" } else { "," };
            let json = serde_json::to_string(&item).unwrap();
            Ok::<_, io::Error>(Bytes::from(format!("{}{}", prefix, json)))
        })
        .chain(futures::stream::once(async { Ok(Bytes::from("]")) }));
    
    let headers = [("content-type", "application/json")];
    (headers, StreamBody::new(stream))
}"""
        }
    }

class AxumAnalyzer:
    """Axum code analyzer following official patterns"""
    
    def __init__(self):
        self.knowledge_base = AxumKnowledgeBase()
    
    async def analyze_axum_code(self, code: str) -> AxumAnalysisResult:
        """Analyze Axum code for patterns and best practices"""
        
        score = 70  # Base score
        routing_patterns = {}
        handler_quality = {}
        extractor_usage = {}
        middleware_patterns = {}
        error_handling = {}
        performance_issues = []
        security_concerns = []
        best_practices_compliance = {}
        magic_patterns_detected = []
        recommendations = []
        
        # Analyze routing patterns
        routing_patterns.update(await self._analyze_routing_patterns(code))
        
        # Analyze handlers
        handler_quality.update(await self._analyze_handlers(code))
        
        # Analyze extractors
        extractor_usage.update(await self._analyze_extractors(code))
        
        # Analyze middleware
        middleware_patterns.update(await self._analyze_middleware(code))
        
        # Analyze error handling
        error_handling.update(await self._analyze_error_handling(code))
        
        # Analyze performance
        performance_issues.extend(await self._analyze_performance(code))
        
        # Analyze security
        security_concerns.extend(await self._analyze_security(code))
        
        # Detect magic patterns
        magic_patterns_detected.extend(await self._detect_magic_patterns(code))
        
        # Best practices compliance
        best_practices_compliance.update(await self._analyze_best_practices(code))
        
        # Generate recommendations
        recommendations.extend(await self._generate_recommendations(
            routing_patterns, handler_quality, extractor_usage, error_handling
        ))
        
        # Calculate final score
        score = await self._calculate_score(
            routing_patterns, handler_quality, extractor_usage, 
            middleware_patterns, error_handling, len(performance_issues), len(security_concerns)
        )
        
        return AxumAnalysisResult(
            code=code,
            score=score,
            routing_patterns=routing_patterns,
            handler_quality=handler_quality,
            extractor_usage=extractor_usage,
            middleware_patterns=middleware_patterns,
            error_handling=error_handling,
            performance_issues=performance_issues,
            security_concerns=security_concerns,
            best_practices_compliance=best_practices_compliance,
            magic_patterns_detected=magic_patterns_detected,
            recommendations=recommendations
        )
    
    async def _analyze_routing_patterns(self, code: str) -> Dict[str, bool]:
        """Analyze routing patterns"""
        patterns = {}
        
        # Macro-free routing
        patterns["uses_router_new"] = "Router::new()" in code
        patterns["uses_route_method"] = ".route(" in code
        patterns["uses_nested_routing"] = ".nest(" in code
        patterns["has_fallback"] = ".fallback(" in code
        
        # RESTful patterns
        patterns["restful_design"] = bool(re.search(r'\.route\("[^"]*/:id".*get.*put.*delete', code))
        patterns["organized_routes"] = code.count(".nest(") > 0
        
        return patterns
    
    async def _analyze_handlers(self, code: str) -> Dict[str, bool]:
        """Analyze handler quality"""
        quality = {}
        
        # Async handlers
        quality["async_handlers"] = "async fn" in code and "-> Result<" in code
        quality["proper_extractors"] = any(ext in code for ext in ["Path(", "Query(", "Json(", "State("])
        quality["typed_responses"] = "Json<" in code or "impl IntoResponse" in code
        
        # Error handling
        quality["returns_result"] = "-> Result<" in code
        quality["uses_question_mark"] = "?" in code and "Result<" in code
        
        return quality
    
    async def _analyze_extractors(self, code: str) -> Dict[str, bool]:
        """Analyze extractor usage"""
        usage = {}
        
        # Built-in extractors
        usage["uses_path"] = "Path(" in code
        usage["uses_query"] = "Query(" in code
        usage["uses_json"] = "Json(" in code
        usage["uses_state"] = "State(" in code
        usage["uses_headers"] = "HeaderMap" in code or "headers:" in code
        
        # Custom extractors
        usage["custom_extractors"] = "FromRequestParts" in code
        usage["proper_extractor_order"] = True  # Would need more complex analysis
        
        return usage
    
    async def _analyze_middleware(self, code: str) -> Dict[str, bool]:
        """Analyze middleware patterns"""
        patterns = {}
        
        # Tower middleware
        patterns["uses_tower"] = "tower::" in code or "ServiceBuilder" in code
        patterns["uses_layer"] = ".layer(" in code
        patterns["tower_http"] = "tower_http::" in code
        
        # Custom middleware
        patterns["custom_middleware"] = "middleware::from_fn" in code
        patterns["middleware_composition"] = "ServiceBuilder::new()" in code
        
        return patterns
    
    async def _analyze_error_handling(self, code: str) -> Dict[str, bool]:
        """Analyze error handling"""
        handling = {}
        
        # Custom error types
        handling["custom_error_type"] = "impl IntoResponse" in code and "Error" in code
        handling["uses_thiserror"] = "thiserror::Error" in code or "#[derive(Error)]" in code
        handling["error_conversion"] = "#[from]" in code
        
        # Error responses
        handling["structured_errors"] = "StatusCode::" in code
        handling["error_layer"] = "HandleErrorLayer" in code
        
        return handling
    
    async def _analyze_performance(self, code: str) -> List[str]:
        """Analyze performance issues"""
        issues = []
        
        # Database connections
        if "sqlx::" in code and "PgPool" not in code and "MySqlPool" not in code:
            issues.append("Consider using connection pooling for database operations")
        
        # Blocking operations
        if "std::fs::" in code and "tokio::fs::" not in code:
            issues.append("Use tokio::fs for async file operations instead of std::fs")
        
        # Cloning in hot paths
        if code.count(".clone()") > 5:
            issues.append("Excessive cloning detected - consider using references")
        
        return issues
    
    async def _analyze_security(self, code: str) -> List[str]:
        """Analyze security concerns"""
        concerns = []
        
        # Authentication
        if "password" in code.lower() and "hash" not in code.lower():
            concerns.append("Password handling detected - ensure proper hashing")
        
        # Input validation
        if "Json(" in code and "validate" not in code:
            concerns.append("JSON input without validation - consider input validation")
        
        # CORS
        if "CorsLayer" not in code and "cors" not in code:
            concerns.append("Consider implementing CORS middleware for web APIs")
        
        return concerns
    
    async def _detect_magic_patterns(self, code: str) -> List[str]:
        """Detect magic patterns in code"""
        patterns = []
        
        if "FromRequestParts" in code:
            patterns.append("Custom extractor magic pattern detected")
        
        if re.search(r'async fn \w+\([^)]*\) -> .*IntoResponse', code):
            patterns.append("Axum magic function parameters pattern")
        
        if "ServiceBuilder" in code and ".layer(" in code:
            patterns.append("Tower service composition pattern")
        
        return patterns
    
    async def _analyze_best_practices(self, code: str) -> Dict[str, bool]:
        """Analyze best practices compliance"""
        compliance = {}
        
        # Code organization
        compliance["modular_routing"] = ".nest(" in code
        compliance["proper_error_handling"] = "Result<" in code and "?" in code
        compliance["async_consistency"] = "async fn" in code and ".await" in code
        
        # Type safety
        compliance["typed_extractors"] = any(f"{ext}(" in code for ext in ["Path", "Query", "Json"])
        compliance["typed_responses"] = "Json<" in code or "impl IntoResponse" in code
        
        return compliance
    
    async def _generate_recommendations(
        self,
        routing: Dict[str, bool],
        handlers: Dict[str, bool],
        extractors: Dict[str, bool],
        errors: Dict[str, bool]
    ) -> List[str]:
        """Generate recommendations based on analysis"""
        recommendations = []
        
        if not routing.get("uses_nested_routing", False):
            recommendations.append("🗂️ Consider using .nest() to organize routes modularly")
        
        if not handlers.get("returns_result", False):
            recommendations.append("🛡️ Use Result<T, E> return types for proper error handling")
        
        if not extractors.get("uses_state", False):
            recommendations.append("🔧 Consider using State extractor for shared application state")
        
        if not errors.get("custom_error_type", False):
            recommendations.append("⚠️ Implement custom error types with IntoResponse for better error handling")
        
        return recommendations
    
    async def _calculate_score(
        self,
        routing: Dict[str, bool],
        handlers: Dict[str, bool],
        extractors: Dict[str, bool],
        middleware: Dict[str, bool],
        errors: Dict[str, bool],
        performance_issues: int,
        security_concerns: int
    ) -> int:
        """Calculate final score based on analysis"""
        base_score = 70
        
        # Bonus for good practices
        routing_bonus = sum(routing.values()) * 4
        handler_bonus = sum(handlers.values()) * 5
        extractor_bonus = sum(extractors.values()) * 3
        middleware_bonus = sum(middleware.values()) * 3
        error_bonus = sum(errors.values()) * 4
        
        # Penalties
        performance_penalty = performance_issues * 5
        security_penalty = security_concerns * 8
        
        final_score = (base_score + routing_bonus + handler_bonus + 
                      extractor_bonus + middleware_bonus + error_bonus - 
                      performance_penalty - security_penalty)
        
        return max(0, min(100, final_score))

class AxumProjectGenerator:
    """Axum project generator following best practices"""
    
    def __init__(self):
        self.knowledge_base = AxumKnowledgeBase()
    
    async def generate_axum_project(
        self,
        project_type: str,
        features: List[str] = None,
        include_database: bool = True,
        include_auth: bool = True
    ) -> Dict[str, Any]:
        """Generate complete Axum project"""
        
        if features is None:
            features = ["json", "database", "middleware", "testing"]
        
        templates = {
            "api_server": self._generate_api_server,
            "web_application": self._generate_web_application,
            "microservice": self._generate_microservice,
            "full_stack": self._generate_full_stack
        }
        
        if project_type not in templates:
            return {"error": f"Project type '{project_type}' not supported"}
        
        return await templates[project_type](features, include_database, include_auth)
    
    async def _generate_api_server(self, features: List[str], include_db: bool, include_auth: bool) -> Dict[str, Any]:
        """Generate API server with Axum"""
        
        cargo_toml = f"""[package]
name = "axum-api-server"
version = "0.1.0"
edition = "2021"

[dependencies]
axum = {{ version = "0.8", features = ["json", "query", "macros"] }}
tokio = {{ version = "1.0", features = ["full"] }}
tower = "0.5"
tower-http = {{ version = "0.6", features = ["cors", "trace"] }}
serde = {{ version = "1.0", features = ["derive"] }}
serde_json = "1.0"
thiserror = "1.0"
anyhow = "1.0"
tracing = "0.1"
tracing-subscriber = "0.3"
uuid = {{ version = "1.0", features = ["v4", "serde"] }}
chrono = {{ version = "0.4", features = ["serde"] }}
{self._get_db_dependencies() if include_db else ""}
{self._get_auth_dependencies() if include_auth else ""}

[dev-dependencies]
axum-test = "16.0"
tokio-test = "0.4"
"""
        
        main_rs = """//! Axum API Server
//! 
//! Modern web API server built with Axum framework following best practices.

use axum::{
    extract::{Path, Query, State},
    http::StatusCode,
    middleware,
    response::{IntoResponse, Json},
    routing::{get, post, put, delete},
    Router,
};
use serde::{Deserialize, Serialize};
use std::{collections::HashMap, sync::Arc};
use tower::{ServiceBuilder, timeout::TimeoutLayer};
use tower_http::{cors::CorsLayer, trace::TraceLayer};
use tracing::{info, Level};
use uuid::Uuid;
use std::time::Duration;

mod error;
mod handlers;
mod middleware as app_middleware;
mod models;
mod state;

use error::{AppError, Result};
use state::AppState;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    // Initialize tracing
    tracing_subscriber::fmt()
        .with_max_level(Level::INFO)
        .init();

    // Create application state
    let state = AppState::new().await?;

    // Build application with middleware
    let app = create_app(state);

    // Start server
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await?;
    info!("Server starting on http://0.0.0.0:3000");
    
    axum::serve(listener, app).await?;
    Ok(())
}

fn create_app(state: AppState) -> Router {
    Router::new()
        .nest("/api/v1", api_routes())
        .route("/health", get(health_check))
        .fallback(not_found)
        .layer(
            ServiceBuilder::new()
                .layer(TraceLayer::new_for_http())
                .layer(CorsLayer::permissive())
                .layer(TimeoutLayer::new(Duration::from_secs(30)))
                .layer(middleware::from_fn(app_middleware::request_id))
        )
        .with_state(state)
}

fn api_routes() -> Router<AppState> {
    Router::new()
        .route("/users", get(handlers::list_users).post(handlers::create_user))
        .route("/users/:id", get(handlers::get_user).put(handlers::update_user).delete(handlers::delete_user))
        .route("/posts", get(handlers::list_posts).post(handlers::create_post))
}

async fn health_check() -> Json<serde_json::Value> {
    Json(serde_json::json!({
        "status": "healthy",
        "timestamp": chrono::Utc::now().to_rfc3339(),
        "version": env!("CARGO_PKG_VERSION")
    }))
}

async fn not_found() -> impl IntoResponse {
    (StatusCode::NOT_FOUND, Json(serde_json::json!({
        "error": "Not Found",
        "message": "The requested resource was not found"
    })))
}"""
        
        error_rs = """//! Error handling for the API server

use axum::{
    http::StatusCode,
    response::{IntoResponse, Json},
};
use serde_json::json;
use thiserror::Error;

pub type Result<T> = std::result::Result<T, AppError>;

#[derive(Error, Debug)]
pub enum AppError {
    #[error("Database error: {0}")]
    Database(#[from] sqlx::Error),
    
    #[error("Validation error: {message}")]
    Validation { message: String },
    
    #[error("Not found: {resource}")]
    NotFound { resource: String },
    
    #[error("Unauthorized")]
    Unauthorized,
    
    #[error("Forbidden")]
    Forbidden,
    
    #[error("Internal server error")]
    Internal(#[from] anyhow::Error),
}

impl IntoResponse for AppError {
    fn into_response(self) -> axum::response::Response {
        let (status, error_message, error_code) = match &self {
            AppError::Database(_) => {
                tracing::error!("Database error: {}", self);
                (StatusCode::INTERNAL_SERVER_ERROR, "Database error occurred", "DATABASE_ERROR")
            }
            AppError::Validation { message } => {
                (StatusCode::BAD_REQUEST, message.as_str(), "VALIDATION_ERROR")
            }
            AppError::NotFound { resource } => {
                (StatusCode::NOT_FOUND, "Resource not found", "NOT_FOUND")
            }
            AppError::Unauthorized => {
                (StatusCode::UNAUTHORIZED, "Unauthorized", "UNAUTHORIZED")
            }
            AppError::Forbidden => {
                (StatusCode::FORBIDDEN, "Forbidden", "FORBIDDEN")
            }
            AppError::Internal(_) => {
                tracing::error!("Internal error: {}", self);
                (StatusCode::INTERNAL_SERVER_ERROR, "Internal server error", "INTERNAL_ERROR")
            }
        };

        let body = Json(json!({
            "error": {
                "code": error_code,
                "message": error_message,
            }
        }));

        (status, body).into_response()
    }
}

impl AppError {
    pub fn validation(message: impl Into<String>) -> Self {
        Self::Validation {
            message: message.into(),
        }
    }

    pub fn not_found(resource: impl Into<String>) -> Self {
        Self::NotFound {
            resource: resource.into(),
        }
    }
}"""
        
        handlers_rs = """//! HTTP handlers for the API

use axum::{
    extract::{Path, Query, State},
    response::Json,
};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use uuid::Uuid;

use crate::{error::{AppError, Result}, models::{User, CreateUserRequest, UpdateUserRequest}, state::AppState};

// User handlers
pub async fn list_users(
    Query(params): Query<HashMap<String, String>>,
    State(state): State<AppState>,
) -> Result<Json<Vec<User>>> {
    let limit = params
        .get("limit")
        .and_then(|s| s.parse().ok())
        .unwrap_or(10);
    
    let users = state.user_service.list_users(limit).await?;
    Ok(Json(users))
}

pub async fn get_user(
    Path(id): Path<Uuid>,
    State(state): State<AppState>,
) -> Result<Json<User>> {
    let user = state.user_service
        .get_user(id)
        .await?
        .ok_or_else(|| AppError::not_found(format!("User with id {}", id)))?;
    
    Ok(Json(user))
}

pub async fn create_user(
    State(state): State<AppState>,
    Json(payload): Json<CreateUserRequest>,
) -> Result<Json<User>> {
    // Validate input
    if payload.name.trim().is_empty() {
        return Err(AppError::validation("Name cannot be empty"));
    }
    
    if !payload.email.contains('@') {
        return Err(AppError::validation("Invalid email format"));
    }
    
    let user = state.user_service.create_user(payload).await?;
    Ok(Json(user))
}

pub async fn update_user(
    Path(id): Path<Uuid>,
    State(state): State<AppState>,
    Json(payload): Json<UpdateUserRequest>,
) -> Result<Json<User>> {
    let user = state.user_service.update_user(id, payload).await?;
    Ok(Json(user))
}

pub async fn delete_user(
    Path(id): Path<Uuid>,
    State(state): State<AppState>,
) -> Result<()> {
    state.user_service.delete_user(id).await?;
    Ok(())
}

// Post handlers (placeholder)
pub async fn list_posts(State(_state): State<AppState>) -> Json<Vec<serde_json::Value>> {
    Json(vec![])
}

pub async fn create_post(
    State(_state): State<AppState>,
    Json(_payload): Json<serde_json::Value>,
) -> Json<serde_json::Value> {
    Json(serde_json::json!({"message": "Post created"}))
}"""
        
        return {
            "project_type": "api_server",
            "files": {
                "Cargo.toml": cargo_toml,
                "src/main.rs": main_rs,
                "src/error.rs": error_rs,
                "src/handlers.rs": handlers_rs,
                "src/models.rs": self._generate_models_file(),
                "src/state.rs": self._generate_state_file(include_db),
                "src/middleware.rs": self._generate_middleware_file(),
                "tests/integration_tests.rs": self._generate_integration_tests(),
                "README.md": self._generate_readme("api_server"),
                ".gitignore": self._generate_gitignore(),
            },
            "axum_patterns_used": [
                "✅ Macro-free routing with Router::new()",
                "✅ Typed extractors (Path, Query, Json, State)",
                "✅ Custom error types with IntoResponse",
                "✅ Tower middleware integration",
                "✅ Nested routing for API organization",
                "✅ Proper async handlers with Result types",
                "✅ Request/response type safety",
                "✅ Structured error responses"
            ],
            "magic_patterns_implemented": [
                "🪄 Axum function parameter magic (different handler signatures)",
                "🪄 Tower service composition patterns",
                "🪄 Type-safe extractor system",
                "🪄 Automatic JSON serialization/deserialization"
            ],
            "next_steps": [
                "cargo run # Start the API server",
                "cargo test # Run all tests",
                "cargo clippy # Run linter",
                "curl http://localhost:3000/health # Test health endpoint"
            ]
        }
    
    def _get_db_dependencies(self) -> str:
        return """sqlx = { version = "0.8", features = ["runtime-tokio-rustls", "postgres", "uuid", "chrono"] }"""
    
    def _get_auth_dependencies(self) -> str:
        return """jsonwebtoken = "9.0"
bcrypt = "0.15"
"""
    
    def _generate_models_file(self) -> str:
        return """//! Data models for the API

use serde::{Deserialize, Serialize};
use uuid::Uuid;
use chrono::{DateTime, Utc};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct User {
    pub id: Uuid,
    pub name: String,
    pub email: String,
    pub created_at: DateTime<Utc>,
    pub updated_at: DateTime<Utc>,
}

#[derive(Debug, Deserialize)]
pub struct CreateUserRequest {
    pub name: String,
    pub email: String,
}

#[derive(Debug, Deserialize)]
pub struct UpdateUserRequest {
    pub name: Option<String>,
    pub email: Option<String>,
}"""
    
    def _generate_state_file(self, include_db: bool) -> str:
        if include_db:
            return """//! Application state management

use std::sync::Arc;
use crate::error::Result;

#[derive(Clone)]
pub struct AppState {
    pub user_service: Arc<UserService>,
    pub config: AppConfig,
}

impl AppState {
    pub async fn new() -> Result<Self> {
        let config = AppConfig::from_env();
        let user_service = Arc::new(UserService::new().await?);
        
        Ok(Self {
            user_service,
            config,
        })
    }
}

#[derive(Clone)]
pub struct AppConfig {
    pub database_url: String,
    pub jwt_secret: String,
}

impl AppConfig {
    pub fn from_env() -> Self {
        Self {
            database_url: std::env::var("DATABASE_URL")
                .unwrap_or_else(|_| "postgres://localhost/axum_app".to_string()),
            jwt_secret: std::env::var("JWT_SECRET")
                .unwrap_or_else(|_| "your-secret-key".to_string()),
        }
    }
}

pub struct UserService {
    // Database connection would go here
}

impl UserService {
    pub async fn new() -> Result<Self> {
        Ok(Self {})
    }
    
    pub async fn list_users(&self, _limit: u32) -> Result<Vec<crate::models::User>> {
        // Implement database query
        Ok(vec![])
    }
    
    pub async fn get_user(&self, _id: uuid::Uuid) -> Result<Option<crate::models::User>> {
        // Implement database query
        Ok(None)
    }
    
    pub async fn create_user(&self, _req: crate::models::CreateUserRequest) -> Result<crate::models::User> {
        // Implement user creation
        use uuid::Uuid;
        use chrono::Utc;
        
        Ok(crate::models::User {
            id: Uuid::new_v4(),
            name: "Test User".to_string(),
            email: "test@example.com".to_string(),
            created_at: Utc::now(),
            updated_at: Utc::now(),
        })
    }
    
    pub async fn update_user(&self, _id: uuid::Uuid, _req: crate::models::UpdateUserRequest) -> Result<crate::models::User> {
        // Implement user update
        use uuid::Uuid;
        use chrono::Utc;
        
        Ok(crate::models::User {
            id: Uuid::new_v4(),
            name: "Updated User".to_string(),
            email: "updated@example.com".to_string(),
            created_at: Utc::now(),
            updated_at: Utc::now(),
        })
    }
    
    pub async fn delete_user(&self, _id: uuid::Uuid) -> Result<()> {
        // Implement user deletion
        Ok(())
    }
}"""
        else:
            return """//! Application state management (in-memory)

use std::sync::Arc;

#[derive(Clone)]
pub struct AppState {
    pub config: AppConfig,
}

impl AppState {
    pub async fn new() -> anyhow::Result<Self> {
        let config = AppConfig::from_env();
        Ok(Self { config })
    }
}

#[derive(Clone)]
pub struct AppConfig {
    pub jwt_secret: String,
}

impl AppConfig {
    pub fn from_env() -> Self {
        Self {
            jwt_secret: std::env::var("JWT_SECRET")
                .unwrap_or_else(|_| "your-secret-key".to_string()),
        }
    }
}"""
    
    def _generate_middleware_file(self) -> str:
        return """//! Custom middleware implementations

use axum::{
    extract::Request,
    http::HeaderValue,
    middleware::Next,
    response::Response,
};
use uuid::Uuid;

pub async fn request_id(mut request: Request, next: Next) -> Response {
    let request_id = Uuid::new_v4().to_string();
    
    // Add request ID to request extensions
    request.extensions_mut().insert(request_id.clone());
    
    let mut response = next.run(request).await;
    
    // Add request ID to response headers
    response.headers_mut().insert(
        "x-request-id",
        HeaderValue::from_str(&request_id).unwrap()
    );
    
    response
}"""
    
    def _generate_integration_tests(self) -> str:
        return """//! Integration tests for the API

use axum_test::TestServer;
use serde_json::json;

#[tokio::test]
async fn test_health_check() {
    let app = axum_api_server::create_app(
        axum_api_server::AppState::new().await.unwrap()
    );
    let server = TestServer::new(app).unwrap();

    let response = server.get("/health").await;
    
    assert_eq!(response.status_code(), 200);
    
    let body: serde_json::Value = response.json();
    assert_eq!(body["status"], "healthy");
}

#[tokio::test]
async fn test_create_user() {
    let app = axum_api_server::create_app(
        axum_api_server::AppState::new().await.unwrap()
    );
    let server = TestServer::new(app).unwrap();

    let user_data = json!({
        "name": "John Doe",
        "email": "john@example.com"
    });

    let response = server
        .post("/api/v1/users")
        .json(&user_data)
        .await;

    assert_eq!(response.status_code(), 200);
    
    let user: serde_json::Value = response.json();
    assert_eq!(user["name"], "Test User");
}

#[tokio::test]
async fn test_not_found() {
    let app = axum_api_server::create_app(
        axum_api_server::AppState::new().await.unwrap()
    );
    let server = TestServer::new(app).unwrap();

    let response = server.get("/nonexistent").await;
    assert_eq!(response.status_code(), 404);
}"""
    
    def _generate_readme(self, project_type: str) -> str:
        return f"""# Axum {project_type.title().replace('_', ' ')}

Modern web API server built with Axum framework following best practices.

## Features

- 🦀 **Modern Rust**: Built with Axum 0.8 and latest Rust patterns
- 🚀 **High Performance**: Tokio async runtime with Tower middleware
- 🛡️ **Type Safety**: Full type safety with extractors and responses
- 🧪 **Comprehensive Testing**: Integration tests with axum-test
- 📊 **Observability**: Structured logging with tracing
- 🔧 **Error Handling**: Custom error types with proper HTTP responses

## Quick Start

```bash
# Run the server
cargo run

# Run tests
cargo test

# Check code quality
cargo clippy
cargo fmt
```

## API Endpoints

- `GET /health` - Health check
- `GET /api/v1/users` - List users
- `POST /api/v1/users` - Create user
- `GET /api/v1/users/:id` - Get user by ID
- `PUT /api/v1/users/:id` - Update user
- `DELETE /api/v1/users/:id` - Delete user

## Architecture

This project follows Axum best practices:

- **Modular Routing**: Organized with nested routes
- **Type-Safe Extractors**: Path, Query, Json, State extractors
- **Custom Error Handling**: Structured error responses
- **Middleware Stack**: CORS, tracing, timeouts
- **Async Throughout**: Full async/await support

## Environment Variables

```bash
DATABASE_URL=postgresql://localhost/axum_app
JWT_SECRET=your-secret-key
```

## Development

This project uses Axum magic patterns for ergonomic handler definitions and leverages the Tower ecosystem for middleware composition.
"""
    
    def _generate_gitignore(self) -> str:
        return """/target/
Cargo.lock
.env
.DS_Store
*.log
"""

# ================================
# AXUM MCP TOOLS
# ================================

@mcp.tool(tags=["analysis", "scoring", "best-practices"])
async def analyze_axum_code(code: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Analyzes Axum code following official best practices and magic patterns.
    
    Args:
        code: Axum code for analysis
        
    Returns:
        Complete analysis with score, detected patterns, and recommendations
    """
    try:
        analyzer = AxumAnalyzer()
        analysis = await analyzer.analyze_axum_code(code)
        
        logger.info(f"Analyzed Axum code - score: {analysis.score}")
        
        return {
            "score": analysis.score,
            "routing_patterns": analysis.routing_patterns,
            "handler_quality": analysis.handler_quality,
            "extractor_usage": analysis.extractor_usage,
            "middleware_patterns": analysis.middleware_patterns,
            "error_handling": analysis.error_handling,
            "performance_issues": analysis.performance_issues,
            "security_concerns": analysis.security_concerns,
            "best_practices_compliance": analysis.best_practices_compliance,
            "magic_patterns_detected": analysis.magic_patterns_detected,
            "recommendations": analysis.recommendations,
            "analysis_categories": [
                "routing", "handlers", "extractors", "middleware", 
                "error_handling", "performance", "security"
            ]
        }
        
    except Exception as e:
        logger.error(f"Error analyzing Axum code: {str(e)}")
        raise

@mcp.tool(tags=["generation", "project", "templates"])
async def generate_axum_project(
    project_type: str,
    features: Optional[List[str]] = None,
    include_database: bool = True,
    include_auth: bool = True,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Generates complete Axum project following modern patterns.
    
    Args:
        project_type: Project type (api_server, web_application, microservice, full_stack)
        features: List of desired features
        include_database: Include database support
        include_auth: Include authentication system
        
    Returns:
        Complete project structure with Axum code
    """
    try:
        generator = AxumProjectGenerator()
        
        result = await generator.generate_axum_project(
            project_type=project_type,
            features=features,
            include_database=include_database,
            include_auth=include_auth
        )
        
        logger.info(f"Generated Axum project: {project_type}")
        
        return result
        
    except Exception as e:
        logger.error(f"Error generating Axum project: {str(e)}")
        raise

@mcp.tool(tags=["patterns", "reference", "documentation"])
async def get_axum_patterns(category: str = "all", ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Returns Axum patterns by category with practical examples.
    
    Args:
        category: Specific category or "all" for all categories
        
    Returns:
        Axum patterns with code examples
    """
    try:
        knowledge_base = AxumKnowledgeBase()
        
        categories = {
            "routing": knowledge_base.ROUTING_PATTERNS,
            "handlers": knowledge_base.HANDLER_PATTERNS,
            "extractors": knowledge_base.EXTRACTOR_PATTERNS,
            "responses": knowledge_base.RESPONSE_PATTERNS,
            "middleware": knowledge_base.MIDDLEWARE_PATTERNS,
            "error_handling": knowledge_base.ERROR_HANDLING_PATTERNS,
            "state_management": knowledge_base.STATE_MANAGEMENT_PATTERNS,
            "testing": knowledge_base.TESTING_PATTERNS,
            "magic_patterns": knowledge_base.MAGIC_PATTERNS,
            "performance": knowledge_base.PERFORMANCE_PATTERNS
        }
        
        if category == "all":
            return {
                "source": "tokio-rs/axum + docs.rs/axum + alexpusch/rust-magic-patterns",
                "version": knowledge_base.VERSION,
                "categories": categories,
                "key_principles": [
                    "Macro-free routing API",
                    "Type-safe extractors and responses",
                    "Tower middleware ecosystem integration",
                    "Ergonomic async handlers",
                    "Zero-overhead abstractions",
                    "Composable and modular design"
                ]
            }
        
        if category not in categories:
            return {"error": f"Category '{category}' not found. Available: {list(categories.keys())}"}
        
        return {
            "category": category,
            "patterns": categories[category],
            "source": "Official Axum documentation and magic patterns"
        }
        
    except Exception as e:
        logger.error(f"Error getting Axum patterns: {str(e)}")
        raise

@mcp.tool(tags=["optimization", "handlers", "refactoring"])
async def optimize_axum_handler(
    handler_code: str,
    focus_areas: Optional[List[str]] = None,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Optimizes Axum handler applying best practices and magic patterns.
    
    Args:
        handler_code: Original handler code
        focus_areas: Focus areas for optimization
        
    Returns:
        Optimized handler with explanations of changes
    """
    try:
        if focus_areas is None:
            focus_areas = ["extractors", "error_handling", "type_safety", "performance"]
        
        # Initial analysis
        analyzer = AxumAnalyzer()
        analysis = await analyzer.analyze_axum_code(handler_code)
        
        optimized_code = handler_code
        changes_made = []
        
        # Optimizations based on focus
        if "extractors" in focus_areas:
            # Suggest appropriate extractors
            if "request:" in optimized_code and "Request<" in optimized_code:
                optimized_code += "\n// TODO: Consider using typed extractors (Path, Query, Json) instead of raw Request"
                changes_made.append("🔧 Suggested typed extractors for better ergonomics")
        
        if "error_handling" in focus_areas:
            # Improve error handling
            if "Result<" not in optimized_code:
                optimized_code = re.sub(
                    r'async fn (\w+)\([^)]*\) -> ([^{]+)',
                    r'async fn \1(\2) -> Result<\2, AppError>',
                    optimized_code
                )
                changes_made.append("🛡️ Added Result return type for proper error handling")
        
        if "type_safety" in focus_areas:
            # Improve type safety
            if "Json(" not in optimized_code and "json" in optimized_code.lower():
                optimized_code += "\n// TODO: Use Json<T> extractor for type-safe JSON parsing"
                changes_made.append("🎯 Suggested Json<T> extractor for type safety")
        
        return {
            "original_code": handler_code,
            "optimized_code": optimized_code,
            "changes_made": changes_made,
            "original_score": analysis.score,
            "axum_patterns_applied": [
                "Type-safe extractors",
                "Proper error handling",
                "Async/await consistency",
                "Response type safety"
            ],
            "recommendations": analysis.recommendations
        }
        
    except Exception as e:
        logger.error(f"Error optimizing Axum handler: {str(e)}")
        raise

@mcp.tool(tags=["magic-patterns", "metaprogramming", "advanced"])
async def get_axum_magic_patterns(ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Returns Axum magic patterns based on rust-magic-patterns.
    
    Returns:
        Magic patterns with technical explanations
    """
    try:
        knowledge_base = AxumKnowledgeBase()
        
        return {
            "title": "Axum Magic Patterns - Advanced Rust Techniques",
            "source": "alexpusch/rust-magic-patterns + tokio-rs/axum",
            "patterns": knowledge_base.MAGIC_PATTERNS,
            "key_concepts": {
                "function_parameters": "How Axum enables flexible handler signatures through trait magic",
                "type_system": "Leveraging Rust's type system for compile-time guarantees",
                "async_patterns": "Advanced async patterns for high-performance web services",
                "metaprogramming": "Type-level programming for ergonomic APIs"
            },
            "learning_resources": [
                "Study simplified examples of complex patterns",
                "Build minimal implementations to understand internals",
                "Explore type system mechanics behind the magic",
                "Practice with different handler signatures"
            ]
        }
        
    except Exception as e:
        logger.error(f"Error getting magic patterns: {str(e)}")
        raise

@mcp.tool(tags=["middleware", "tower", "generation"])
async def create_axum_middleware(
    middleware_type: str,
    functionality: str,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Creates custom middleware for Axum.
    
    Args:
        middleware_type: Middleware type (auth, logging, cors, etc.)
        functionality: Description of desired functionality
        
    Returns:
        Middleware code with usage examples
    """
    try:
        middleware_templates = {
            "auth": """
// Authentication middleware
use axum::{
    extract::Request,
    http::{StatusCode, HeaderValue},
    middleware::Next,
    response::Response,
};

pub async fn auth_middleware(
    req: Request,
    next: Next,
) -> Result<Response, StatusCode> {
    let auth_header = req.headers()
        .get("Authorization")
        .and_then(|header| header.to_str().ok())
        .ok_or(StatusCode::UNAUTHORIZED)?;
    
    if !auth_header.starts_with("Bearer ") {
        return Err(StatusCode::UNAUTHORIZED);
    }
    
    let token = &auth_header[7..];
    if !is_valid_token(token).await {
        return Err(StatusCode::UNAUTHORIZED);
    }
    
    Ok(next.run(req).await)
}

async fn is_valid_token(token: &str) -> bool {
    // Implement token validation logic
    !token.is_empty()
}

// Usage
let app = Router::new()
    .route("/protected", get(protected_handler))
    .layer(axum::middleware::from_fn(auth_middleware));
""",
            "logging": """
// Request logging middleware
use axum::{
    extract::Request,
    middleware::Next,
    response::Response,
};
use std::time::Instant;
use tracing::info;

pub async fn logging_middleware(
    req: Request,
    next: Next,
) -> Response {
    let start = Instant::now();
    let method = req.method().clone();
    let uri = req.uri().clone();
    
    let response = next.run(req).await;
    
    let duration = start.elapsed();
    let status = response.status();
    
    info!(
        method = %method,
        uri = %uri,
        status = %status,
        duration_ms = duration.as_millis(),
        "Request processed"
    );
    
    response
}

// Usage with tracing
let app = Router::new()
    .route("/", get(handler))
    .layer(axum::middleware::from_fn(logging_middleware));
""",
            "cors": """
// Custom CORS middleware
use axum::{
    extract::Request,
    http::{HeaderValue, Method},
    middleware::Next,
    response::Response,
};

pub async fn cors_middleware(
    req: Request,
    next: Next,
) -> Response {
    let origin = req.headers()
        .get("Origin")
        .and_then(|v| v.to_str().ok())
        .unwrap_or("*");
    
    let mut response = next.run(req).await;
    
    let headers = response.headers_mut();
    headers.insert(
        "Access-Control-Allow-Origin",
        HeaderValue::from_str(origin).unwrap(),
    );
    headers.insert(
        "Access-Control-Allow-Methods",
        HeaderValue::from_static("GET, POST, PUT, DELETE, OPTIONS"),
    );
    headers.insert(
        "Access-Control-Allow-Headers",
        HeaderValue::from_static("Content-Type, Authorization"),
    );
    
    response
}

// Usage
let app = Router::new()
    .route("/api/*path", get(api_handler))
    .layer(axum::middleware::from_fn(cors_middleware));
"""
        }
        
        template = middleware_templates.get(middleware_type, middleware_templates["auth"])
        
        return {
            "middleware_type": middleware_type,
            "functionality": functionality,
            "code": template,
            "usage_patterns": [
                "Apply to specific routes with .layer()",
                "Combine multiple middleware with ServiceBuilder",
                "Use middleware::from_fn for function-based middleware",
                "Implement custom middleware with Tower Service trait"
            ],
            "best_practices": [
                "Keep middleware focused on single responsibility",
                "Use proper error handling and status codes",
                "Consider performance impact on all requests",
                "Test middleware in isolation"
            ]
        }
        
    except Exception as e:
        logger.error(f"Error creating Axum middleware: {str(e)}")
        raise

# ================================
# MCP PROMPTS
# ================================


@mcp.prompt()
async def design_axum_api(
    api_purpose: str,
    endpoints: List[str] = [],
    features: List[str] = []
) -> List[Dict[str, str]]:
    """
    Generate a prompt to design a complete API with Axum.

    Args:
        api_purpose: Purpose of the API
        endpoints: List of required endpoints
        features: Additional features (auth, database, caching, etc.)
    """
    default_endpoints = ["/users", "/posts", "/health"]
    endpoint_list = endpoints if endpoints else default_endpoints

    default_features = ["authentication", "error handling", "validation"]
    feature_list = features if features else default_features

    return [
        {
            "role": "system",
            "content": """You are an expert in designing web APIs with Axum.

Axum API design principles:
1. **RESTful routing**: Use proper HTTP methods and resource paths
2. **Type-safe handlers**: Use typed extractors (Path, Query, Json, State)
3. **Error handling**: Custom error types with IntoResponse
4. **Middleware**: Tower ecosystem for cross-cutting concerns
5. **State management**: Shared state with Arc and State extractor
6. **Documentation**: OpenAPI/Swagger integration
7. **Testing**: Integration tests with axum-test

API structure best practices:
- Organize routes with nest() for modules
- Use versioned API paths (/api/v1/...)
- Implement proper error responses
- Add health check endpoints
- Use middleware for logging, auth, CORS"""
        },
        {
            "role": "user",
            "content": f"""Design an API with Axum for: {api_purpose}

Required endpoints: {', '.join(endpoint_list)}
Features: {', '.join(feature_list)}

Requirements:
1. Define complete routing structure with Router
2. Create typed handler signatures
3. Implement custom error types with IntoResponse
4. Set up middleware stack (logging, CORS, auth)
5. Configure shared application state
6. Add request validation patterns
7. Include response types and serialization
8. Provide integration test examples"""
        }
    ]


@mcp.prompt()
async def create_axum_handler(
    handler_purpose: str,
    extractors: List[str] = [],
    response_type: str = "Json"
) -> List[Dict[str, str]]:
    """
    Generate a prompt to create an optimized Axum handler.

    Args:
        handler_purpose: What the handler should do
        extractors: Extractors to use (Path, Query, Json, State, etc.)
        response_type: Type of response (Json, StatusCode, Html, etc.)
    """
    default_extractors = ["State", "Json"]
    extractor_list = extractors if extractors else default_extractors

    return [
        {
            "role": "system",
            "content": """You are an expert in writing Axum handlers.

Handler best practices:
1. **Async functions**: All handlers should be async
2. **Typed extractors**: Use proper extractors for type safety
3. **Result return type**: Return Result<T, E> for error handling
4. **Extractor order**: Order matters - body extractors must be last
5. **Response types**: Use IntoResponse or specific types

Extractor patterns:
- Path(id): Path<u32> - Extract from URL path
- Query(params): Query<Params> - Extract query parameters
- Json(body): Json<Body> - Extract JSON body
- State(state): State<AppState> - Access shared state
- HeaderMap - Access HTTP headers

Error handling:
- Return Result<T, AppError>
- AppError implements IntoResponse
- Use ? operator for propagation
- Provide meaningful error messages"""
        },
        {
            "role": "user",
            "content": f"""Create an Axum handler for: {handler_purpose}

Extractors to use: {', '.join(extractor_list)}
Response type: {response_type}

Requirements:
1. Define async handler function
2. Use typed extractors with proper order
3. Return Result<{response_type}<T>, AppError>
4. Implement input validation
5. Add proper error handling
6. Include documentation comments
7. Show usage in router
8. Add unit test example"""
        }
    ]


@mcp.prompt()
async def implement_middleware_stack(
    middleware_needs: List[str] = [],
    custom_middleware: str = ""
) -> List[Dict[str, str]]:
    """
    Generate a prompt to implement a middleware stack for Axum.

    Args:
        middleware_needs: Types of middleware needed (auth, logging, cors, rate-limit)
        custom_middleware: Description of custom middleware if needed
    """
    default_needs = ["logging", "cors", "auth", "timeout"]
    needs = middleware_needs if middleware_needs else default_needs

    return [
        {
            "role": "system",
            "content": """You are an expert in Tower middleware and Axum.

Tower middleware ecosystem:
1. **tower**: Core middleware abstractions
2. **tower-http**: HTTP-specific middleware
3. **axum::middleware**: Axum-specific helpers

Common middleware layers:
- TraceLayer: Request tracing and logging
- CorsLayer: Cross-Origin Resource Sharing
- TimeoutLayer: Request timeouts
- RateLimitLayer: Rate limiting
- CompressionLayer: Response compression

Middleware patterns:
```rust
ServiceBuilder::new()
    .layer(TraceLayer::new_for_http())
    .layer(TimeoutLayer::new(Duration::from_secs(30)))
    .layer(CorsLayer::permissive())
    .layer(middleware::from_fn(custom_middleware))
```

Custom middleware with from_fn:
```rust
async fn custom_middleware(
    req: Request,
    next: Next,
) -> Result<Response, StatusCode> {
    // Before request
    let response = next.run(req).await;
    // After request
    Ok(response)
}
```"""
        },
        {
            "role": "user",
            "content": f"""Implement a middleware stack for Axum with:

Required middleware: {', '.join(needs)}
{f"Custom middleware: {custom_middleware}" if custom_middleware else ""}

Requirements:
1. Use ServiceBuilder for middleware composition
2. Configure each middleware appropriately
3. Set proper ordering (order matters!)
4. Handle middleware errors with HandleErrorLayer
5. Add tracing/logging integration
6. Implement custom middleware if needed
7. Show how to apply to specific routes vs globally
8. Include testing examples"""
        }
    ]


@mcp.prompt()
async def setup_state_management(
    state_components: List[str] = [],
    shared_resources: List[str] = []
) -> List[Dict[str, str]]:
    """
    Generate a prompt to set up state management in Axum.

    Args:
        state_components: Components in app state (config, services, etc.)
        shared_resources: Shared resources (database, cache, etc.)
    """
    default_components = ["config", "database", "cache"]
    components = state_components if state_components else default_components

    default_resources = ["PostgreSQL pool", "Redis connection"]
    resources = shared_resources if shared_resources else default_resources

    return [
        {
            "role": "system",
            "content": """You are an expert in Axum state management.

State management patterns:
1. **AppState struct**: Central state container
2. **State extractor**: Access state in handlers
3. **Extension**: Per-request state
4. **Arc wrapping**: For shared ownership

AppState design:
```rust
#[derive(Clone)]
struct AppState {
    db: PgPool,              // Database pool
    cache: Arc<Cache>,       // Shared cache
    config: AppConfig,       // Configuration
    services: Arc<Services>, // Business services
}

impl AppState {
    async fn new() -> Result<Self> {
        let db = create_db_pool().await?;
        let cache = Arc::new(Cache::new());
        let config = AppConfig::from_env();
        let services = Arc::new(Services::new(db.clone()));

        Ok(Self { db, cache, config, services })
    }
}
```

State access in handlers:
```rust
async fn handler(State(state): State<AppState>) -> Result<Json<T>, AppError> {
    let data = state.services.get_data().await?;
    Ok(Json(data))
}
```"""
        },
        {
            "role": "user",
            "content": f"""Set up state management for Axum with:

State components: {', '.join(components)}
Shared resources: {', '.join(resources)}

Requirements:
1. Design AppState struct with proper Clone
2. Use Arc for shared mutable state
3. Initialize resources properly
4. Handle initialization errors
5. Configure with environment variables
6. Show State extractor usage
7. Add Extension for per-request data
8. Include shutdown/cleanup handling"""
        }
    ]


@mcp.prompt()
async def handle_errors_gracefully(
    error_scenarios: List[str] = [],
    include_recovery: bool = True
) -> List[Dict[str, str]]:
    """
    Generate a prompt to implement graceful error handling in Axum.

    Args:
        error_scenarios: Types of errors to handle
        include_recovery: Whether to include recovery strategies
    """
    default_scenarios = ["database", "validation", "auth", "not_found", "internal"]
    scenarios = error_scenarios if error_scenarios else default_scenarios

    return [
        {
            "role": "system",
            "content": """You are an expert in Axum error handling.

Error handling principles:
1. **Custom error types**: Define domain-specific errors
2. **IntoResponse**: Convert errors to HTTP responses
3. **thiserror**: Derive Error trait easily
4. **HandleErrorLayer**: Handle middleware errors

Error type pattern:
```rust
#[derive(Error, Debug)]
pub enum AppError {
    #[error("Database error: {0}")]
    Database(#[from] sqlx::Error),

    #[error("Validation: {message}")]
    Validation { message: String },

    #[error("Not found: {resource}")]
    NotFound { resource: String },

    #[error("Unauthorized")]
    Unauthorized,
}

impl IntoResponse for AppError {
    fn into_response(self) -> Response {
        let (status, message) = match &self {
            AppError::Database(_) => (StatusCode::INTERNAL_SERVER_ERROR, "Database error"),
            AppError::Validation { message } => (StatusCode::BAD_REQUEST, message.as_str()),
            AppError::NotFound { .. } => (StatusCode::NOT_FOUND, "Not found"),
            AppError::Unauthorized => (StatusCode::UNAUTHORIZED, "Unauthorized"),
        };

        (status, Json(json!({"error": message}))).into_response()
    }
}
```

HandleErrorLayer for middleware:
```rust
.layer(HandleErrorLayer::new(|error: BoxError| async move {
    if error.is::<tower::timeout::error::Elapsed>() {
        Ok(StatusCode::REQUEST_TIMEOUT)
    } else {
        Err((StatusCode::INTERNAL_SERVER_ERROR, "Internal error"))
    }
}))
```"""
        },
        {
            "role": "user",
            "content": f"""Implement graceful error handling for Axum with:

Error scenarios: {', '.join(scenarios)}
Include recovery strategies: {'Yes' if include_recovery else 'No'}

Requirements:
1. Define comprehensive AppError enum
2. Implement IntoResponse with proper status codes
3. Use thiserror for Error trait
4. Add From implementations for conversion
5. Include HandleErrorLayer for middleware
6. Log errors appropriately
7. Return structured JSON error responses
8. {'Add retry and recovery patterns' if include_recovery else 'Focus on error responses'}"""
        }
    ]


# ================================
# ADDITIONAL RESOURCES
# ================================

@mcp.resource(uri="guide://axum-web-development")
async def get_axum_development_guide() -> str:
    """Complete Axum web development guide"""
    return json.dumps({
        "title": "Axum Web Development Guide 2025",
        "based_on": [
            "tokio-rs/axum official repository",
            "docs.rs/axum comprehensive documentation",
            "alexpusch/rust-magic-patterns advanced techniques"
        ],
        "sections": {
            "routing": "Macro-free routing with Router API and nested routes",
            "handlers": "Async handlers with typed extractors",
            "extractors": "Built-in and custom extractors for type safety",
            "responses": "IntoResponse trait and custom response types",
            "middleware": "Tower middleware ecosystem integration",
            "error_handling": "Custom error types with structured responses",
            "state_management": "Shared state with Arc and State extractor",
            "testing": "Integration testing with axum-test",
            "magic_patterns": "Advanced Rust patterns and metaprogramming",
            "performance": "Optimizations for high-performance web services"
        },
        "key_frameworks": {
            "axum": "Ergonomic web framework built on Tokio/Tower/Hyper",
            "tower": "Modular networking components for Rust",
            "tokio": "Asynchronous runtime for Rust",
            "hyper": "Low-level HTTP implementation"
        },
        "features": {
            "code_analysis": "Axum code analysis with detailed scoring",
            "project_generation": "Project generation following best practices",
            "pattern_library": "Complete library of Axum patterns",
            "magic_patterns": "Advanced Rust techniques and metaprogramming",
            "middleware_creation": "Custom middleware generation",
            "handler_optimization": "Automatic handler optimization"
        }
    }, indent=2)

# ================================
# SERVER INITIALIZATION
# ================================

if __name__ == "__main__":
    logger.info("🌐 Axum Web Framework MCP Server starting...")
    logger.info("🚀 Specialized in modern async web development with type safety")
    logger.info("📚 Based on: tokio-rs/axum + docs.rs/axum + alexpusch/rust-magic-patterns")
    logger.info("🔧 Features: Code Analysis | Project Generation | Magic Patterns | Middleware Creation")
    logger.info("\n📝 Available prompts:")
    logger.info("  - design_axum_api: Design complete API with Axum")
    logger.info("  - create_axum_handler: Create optimized handlers")
    logger.info("  - implement_middleware_stack: Implement middleware stack")
    logger.info("  - setup_state_management: Configure state management")
    logger.info("  - handle_errors_gracefully: Implement error handling")

    # Run the MCP server
    mcp.run()