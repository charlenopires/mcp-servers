#!/usr/bin/env python3
"""
Rust Idiomatic MCP Server
==========================

Advanced MCP server based on Rust idiomatic patterns, featuring:
- Code analysis following rust-lang/api-guidelines
- Idiomatic patterns from mre/idiomatic-rust repository
- Ergonomic error handling with Result/Option
- Traits and generics for flexible and reusable code
- Async/await patterns with Tokio
- Immutability by default and zero-cost abstractions
- Type safety and compile-time guarantees

Based on: rust-lang/api-guidelines, mre/idiomatic-rust, and blessed.rs
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
    name="Rust Idiomatic Patterns Server",
    instructions="""Advanced MCP server for idiomatic Rust development based on mre/idiomatic-rust and rust-lang/api-guidelines.

This server provides Rust development expertise:
- Code analysis for idiomatic patterns (immutability, error handling, ownership)
- Project generation following API guidelines
- Refactoring to idiomatic Rust patterns
- Pattern library from mre/idiomatic-rust repository
- API guidelines compliance checking

Use these tools to write clean, idiomatic Rust code.""",
    version="3.0.0"
)

# ================================
# RUST IDIOMATIC PATTERNS & KNOWLEDGE BASE
# ================================

class IdiomaticCategory(Enum):
    """Rust idiomatic pattern categories"""
    IMMUTABILITY = "immutability"
    ERROR_HANDLING = "error_handling"
    TYPE_CONVERSIONS = "type_conversions"
    OWNERSHIP = "ownership"
    ENUMS_OVER_BOOLS = "enums_over_bools"
    ASYNC_PATTERNS = "async_patterns"
    TRAITS_GENERICS = "traits_generics"
    ITERATORS = "iterators"
    API_DESIGN = "api_design"
    DOCUMENTATION = "documentation"
    PERFORMANCE = "performance"

class RustComplexity(Enum):
    """Complexity levels for analysis"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"

@dataclass
class IdiomaticAnalysisResult:
    """Result of Rust idiomatic code analysis"""
    code: str
    idiomaticity_score: int
    category_scores: Dict[str, int]
    idiomatic_patterns_found: List[str]
    anti_patterns_found: List[str]
    suggestions: List[str]
    refactored_examples: Dict[str, str]
    compliance_with_api_guidelines: Dict[str, bool]

class RustIdiomaticKnowledgeBase:
    """Rust idiomatic knowledge base based on mre/idiomatic-rust"""
    
    VERSION = "1.82.0"
    EDITION = "2021"
    
    # Pattern: Immutability by Default
    IMMUTABILITY_PATTERNS = {
        "default_immutable": {
            "principle": "Aim For Immutability in Rust",
            "description": "Variables are immutable by default - use mut only when necessary",
            "good_example": """
// Idiomatic: immutable by default
let data = vec![1, 2, 3, 4, 5];
let sum: i32 = data.iter().sum();

// Use mut only when necessary
let mut counter = 0;
for item in &data {
    if item % 2 == 0 {
        counter += 1;
    }
}""",
            "anti_pattern": """
// Anti-pattern: unnecessary mut
let mut data = vec![1, 2, 3, 4, 5]; // data never changes
let mut sum = data.iter().sum(); // sum never changes""",
            "benefits": [
                "Prevents accidental mutations",
                "Makes code easier to reason about",
                "Enables compiler optimizations",
                "Communicates intent clearly"
            ]
        },
        "structural_immutability": {
            "description": "Use immutable data structures and functional patterns",
            "good_example": """
use std::collections::HashMap;

// Idiomatic: return new state instead of mutating
fn add_user(mut users: HashMap<u32, String>, id: u32, name: String) -> HashMap<u32, String> {
    users.insert(id, name);
    users
}

// Or use builder pattern for complex construction
#[derive(Debug, Clone)]
pub struct Config {
    pub host: String,
    pub port: u16,
    pub timeout: std::time::Duration,
}

impl Config {
    pub fn builder() -> ConfigBuilder {
        ConfigBuilder::default()
    }
}""",
            "benefits": [
                "Reduces bugs from shared mutable state",
                "Enables safe concurrent programming",
                "Makes testing easier"
            ]
        }
    }
    
    # Pattern: Ergonomic Error Handling
    ERROR_HANDLING_PATTERNS = {
        "result_over_panic": {
            "principle": "Use Result<T, E> instead of panicking",
            "description": "Return errors instead of panicking to allow callers to handle failures",
            "good_example": """
use std::fs::File;
use std::io::Result;

// Idiomatic: return Result for recoverable errors
fn read_config(path: &str) -> Result<Config> {
    let file = File::open(path)?;
    let config = serde_json::from_reader(file)?;
    Ok(config)
}

// Custom error types for better error handling
#[derive(Debug, thiserror::Error)]
pub enum ConfigError {
    #[error("Failed to read config file: {0}")]
    Io(#[from] std::io::Error),
    
    #[error("Invalid config format: {0}")]
    InvalidFormat(#[from] serde_json::Error),
    
    #[error("Missing required field: {field}")]
    MissingField { field: String },
}""",
            "anti_pattern": """
// Anti-pattern: panicking instead of error handling
fn read_config(path: &str) -> Config {
    let file = File::open(path).expect("Config file must exist");
    serde_json::from_reader(file).expect("Config must be valid JSON")
}""",
            "benefits": [
                "Allows callers to handle errors appropriately",
                "Makes errors part of the API contract",
                "Improves program robustness"
            ]
        },
        "question_mark_operator": {
            "description": "Use ? operator for ergonomic error propagation",
            "good_example": """
use std::fs;
use std::io::Result;

// Idiomatic: use ? for clean error propagation
fn process_file(path: &str) -> Result<String> {
    let content = fs::read_to_string(path)?;
    let processed = content.trim().to_uppercase();
    Ok(processed)
}

// Chain operations with ?
fn complex_operation() -> Result<String> {
    let config = read_config("config.json")?;
    let data = fetch_data(&config.url)?;
    let result = process_data(data)?;
    Ok(result)
}""",
            "anti_pattern": """
// Anti-pattern: manual error handling
fn process_file(path: &str) -> Result<String> {
    match fs::read_to_string(path) {
        Ok(content) => {
            let processed = content.trim().to_uppercase();
            Ok(processed)
        }
        Err(e) => Err(e),
    }
}"""
        },
        "option_for_nullable": {
            "description": "Use Option<T> instead of null pointers",
            "good_example": """
// Idiomatic: use Option for potentially missing values
fn find_user_by_id(users: &[User], id: u32) -> Option<&User> {
    users.iter().find(|user| user.id == id)
}

// Chain Option operations
fn get_user_email(users: &[User], id: u32) -> Option<String> {
    find_user_by_id(users, id)
        .map(|user| user.email.clone())
}

// Use combinators for complex logic
fn process_optional_data(data: Option<String>) -> Option<String> {
    data.filter(|s| !s.is_empty())
        .map(|s| s.to_uppercase())
}""",
            "benefits": [
                "Eliminates null pointer exceptions",
                "Makes nullable values explicit",
                "Provides rich combinator API"
            ]
        }
    }
    
    # Pattern: Smart Type Conversions
    TYPE_CONVERSION_PATTERNS = {
        "from_into_traits": {
            "description": "Use From/Into traits for type conversions",
            "good_example": """
// Idiomatic: implement From trait
#[derive(Debug)]
pub struct UserId(u32);

impl From<u32> for UserId {
    fn from(id: u32) -> Self {
        UserId(id)
    }
}

// Into is automatically implemented
fn create_user(id: impl Into<UserId>, name: String) -> User {
    User {
        id: id.into(),
        name,
    }
}

// Use for error type conversions
impl From<std::io::Error> for MyError {
    fn from(err: std::io::Error) -> Self {
        MyError::Io(err)
    }
}""",
            "anti_pattern": """
// Anti-pattern: custom conversion methods
impl UserId {
    pub fn from_u32(id: u32) -> Self {
        UserId(id)
    }
}""",
            "benefits": [
                "Follows Rust conventions",
                "Works with generic code",
                "Enables ? operator with different error types"
            ]
        },
        "try_from_for_fallible": {
            "description": "Use TryFrom for fallible conversions",
            "good_example": """
use std::convert::TryFrom;

#[derive(Debug)]
pub struct PositiveNumber(u32);

impl TryFrom<i32> for PositiveNumber {
    type Error = &'static str;
    
    fn try_from(value: i32) -> Result<Self, Self::Error> {
        if value >= 0 {
            Ok(PositiveNumber(value as u32))
        } else {
            Err("Number must be positive")
        }
    }
}

// Usage with ? operator
fn process_number(input: i32) -> Result<PositiveNumber, Box<dyn std::error::Error>> {
    let positive = PositiveNumber::try_from(input)?;
    Ok(positive)
}"""
        }
    }
    
    # Pattern: Ownership and Borrowing
    OWNERSHIP_PATTERNS = {
        "borrow_by_default": {
            "description": "Take references by default, owned values when needed",
            "good_example": """
// Idiomatic: take references for read-only access
fn process_data(data: &[String]) -> usize {
    data.iter().map(|s| s.len()).sum()
}

// Take owned values when you need to store or transform
fn collect_long_strings(data: Vec<String>) -> Vec<String> {
    data.into_iter()
        .filter(|s| s.len() > 10)
        .collect()
}

// Use Cow for flexibility
use std::borrow::Cow;

fn ensure_https(url: Cow<str>) -> Cow<str> {
    if url.starts_with("https://") {
        url
    } else {
        Cow::Owned(format!("https://{}", url))
    }
}""",
            "anti_pattern": """
// Anti-pattern: always taking owned values
fn process_data(data: Vec<String>) -> usize {
    data.iter().map(|s| s.len()).sum()
}""",
            "benefits": [
                "Reduces unnecessary allocations",
                "Makes ownership clear",
                "Enables zero-copy optimizations"
            ]
        },
        "clone_when_needed": {
            "description": "Clone explicitly and only when necessary",
            "good_example": """
// Idiomatic: avoid cloning when possible
fn process_users(users: &[User]) -> Vec<String> {
    users.iter()
        .map(|user| &user.name)
        .cloned() // Only clone the strings we need
        .collect()
}

// Use Rc/Arc for shared ownership
use std::rc::Rc;

fn share_data(data: Vec<String>) -> (Rc<Vec<String>>, Rc<Vec<String>>) {
    let shared = Rc::new(data);
    (shared.clone(), shared)
}"""
        }
    }
    
    # Pattern: Enums Over Booleans
    ENUM_PATTERNS = {
        "expressive_enums": {
            "description": "Use enums instead of boolean flags for better expressiveness",
            "good_example": """
// Idiomatic: expressive enum
#[derive(Debug, Clone, Copy)]
pub enum CachePolicy {
    NoCache,
    CacheForever,
    CacheForDuration(std::time::Duration),
}

fn fetch_data(url: &str, policy: CachePolicy) -> Result<String> {
    match policy {
        CachePolicy::NoCache => fetch_fresh(url),
        CachePolicy::CacheForever => fetch_cached_or_fresh(url, None),
        CachePolicy::CacheForDuration(duration) => fetch_cached_or_fresh(url, Some(duration)),
    }
}

// State machines with enums
#[derive(Debug)]
pub enum ConnectionState {
    Disconnected,
    Connecting { attempt: u32 },
    Connected { since: std::time::Instant },
    Failed { error: String },
}""",
            "anti_pattern": """
// Anti-pattern: boolean flags
fn fetch_data(url: &str, use_cache: bool, cache_forever: bool) -> Result<String> {
    // Confusing combinations of boolean flags
    if use_cache && cache_forever {
        // ...
    } else if use_cache && !cache_forever {
        // ...
    } else {
        // ...
    }
}""",
            "benefits": [
                "Self-documenting code",
                "Impossible to represent invalid states",
                "Compiler-enforced exhaustive matching"
            ]
        },
        "discriminated_unions": {
            "description": "Use enums for discriminated unions",
            "good_example": """
// Idiomatic: rich data modeling with enums
#[derive(Debug)]
pub enum DatabaseConfig {
    Sqlite { path: String },
    Postgres { host: String, port: u16, database: String },
    InMemory,
}

impl DatabaseConfig {
    pub fn connection_string(&self) -> Option<String> {
        match self {
            DatabaseConfig::Sqlite { path } => Some(format!("sqlite://{}", path)),
            DatabaseConfig::Postgres { host, port, database } => {
                Some(format!("postgres://{}:{}/{}", host, port, database))
            }
            DatabaseConfig::InMemory => None,
        }
    }
}"""
        }
    }
    
    # Pattern: Async Patterns
    ASYNC_PATTERNS = {
        "async_await_idiomatic": {
            "description": "Use async/await for asynchronous programming",
            "good_example": """
use tokio::time::{sleep, Duration};
use std::future::Future;

// Idiomatic: async functions
async fn fetch_user(id: u32) -> Result<User, ApiError> {
    let response = reqwest::get(&format!("https://api.example.com/users/{}", id)).await?;
    let user = response.json().await?;
    Ok(user)
}

// Concurrent operations
async fn fetch_multiple_users(ids: &[u32]) -> Result<Vec<User>, ApiError> {
    let futures = ids.iter().map(|&id| fetch_user(id));
    let results = futures_util::future::try_join_all(futures).await?;
    Ok(results)
}

// Stream processing
use tokio_stream::{Stream, StreamExt};

async fn process_user_stream<S>(stream: S) -> Result<Vec<ProcessedUser>, ProcessingError>
where
    S: Stream<Item = User>,
{
    stream
        .map(process_user)
        .buffer_unordered(10) // Process up to 10 concurrently
        .try_collect()
        .await
}""",
            "benefits": [
                "Natural async programming model",
                "Efficient resource utilization",
                "Composable async operations"
            ]
        },
        "cancellation_safety": {
            "description": "Design async functions to be cancellation-safe",
            "good_example": """
// Idiomatic: cancellation-safe async function
async fn save_data_safely(data: &Data, path: &Path) -> Result<(), SaveError> {
    let temp_path = path.with_extension("tmp");
    
    // Write to temporary file first
    tokio::fs::write(&temp_path, serde_json::to_string(data)?).await?;
    
    // Atomically move to final location
    tokio::fs::rename(&temp_path, path).await?;
    
    Ok(())
}

// Use select! for timeout handling
use tokio::time::timeout;

async fn fetch_with_timeout(url: &str) -> Result<String, FetchError> {
    timeout(Duration::from_secs(30), reqwest::get(url)).await
        .map_err(|_| FetchError::Timeout)?
        .text()
        .await
        .map_err(FetchError::Network)
}"""
        }
    }
    
    # Pattern: Traits and Generics
    TRAIT_PATTERNS = {
        "trait_bounds": {
            "description": "Use trait bounds for flexible generic code",
            "good_example": """
// Idiomatic: trait bounds for generic functions
fn serialize_to_string<T>(value: &T) -> Result<String, serde_json::Error>
where
    T: serde::Serialize,
{
    serde_json::to_string(value)
}

// Associated types for cleaner APIs
trait Iterator {
    type Item;
    fn next(&mut self) -> Option<Self::Item>;
}

// Higher-order trait bounds
fn process_items<I, F, R>(items: I, processor: F) -> Vec<R>
where
    I: IntoIterator,
    F: Fn(I::Item) -> R,
{
    items.into_iter().map(processor).collect()
}""",
            "benefits": [
                "Compile-time polymorphism",
                "Zero-cost abstractions",
                "Type-safe generic programming"
            ]
        },
        "impl_trait": {
            "description": "Use impl Trait for return types and parameters",
            "good_example": """
// Idiomatic: impl Trait for return types
fn get_numbers() -> impl Iterator<Item = u32> {
    (0..10).filter(|&x| x % 2 == 0)
}

// impl Trait for parameters
fn process_items(items: impl IntoIterator<Item = String>) -> Vec<String> {
    items.into_iter().map(|s| s.to_uppercase()).collect()
}

// Combined with async
async fn fetch_users() -> impl Stream<Item = Result<User, ApiError>> {
    // Return async stream
    stream::iter(user_ids).then(|id| async move { fetch_user(id).await })
}"""
        }
    }
    
    # Pattern: Iterator Patterns
    ITERATOR_PATTERNS = {
        "iterator_over_loops": {
            "description": "Prefer iterators over manual loops",
            "good_example": """
// Idiomatic: use iterators
let even_squares: Vec<u32> = (0..10)
    .filter(|&x| x % 2 == 0)
    .map(|x| x * x)
    .collect();

// Chain operations naturally
let result: Result<Vec<_>, _> = file_paths
    .iter()
    .map(|path| std::fs::read_to_string(path))
    .collect();

// Custom iterators
struct Counter {
    current: u32,
    max: u32,
}

impl Counter {
    fn new(max: u32) -> Counter {
        Counter { current: 0, max }
    }
}

impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        if self.current < self.max {
            let current = self.current;
            self.current += 1;
            Some(current)
        } else {
            None
        }
    }
}""",
            "anti_pattern": """
// Anti-pattern: manual loops when iterators would be clearer
let mut even_squares = Vec::new();
for i in 0..10 {
    if i % 2 == 0 {
        even_squares.push(i * i);
    }
}""",
            "benefits": [
                "More expressive and functional style",
                "Better composability",
                "Potential performance benefits"
            ]
        }
    }
    
    # Pattern: API Design Guidelines
    API_DESIGN_PATTERNS = {
        "rust_naming_conventions": {
            "description": "Follow Rust naming conventions",
            "good_example": """
// Types: PascalCase
pub struct UserConfig {}
pub enum DatabaseType {}

// Functions and variables: snake_case
pub fn create_user_account() {}
let user_name = "Alice";

// Constants: SCREAMING_SNAKE_CASE
pub const MAX_RETRY_ATTEMPTS: u32 = 3;

// Modules: snake_case
mod user_management {}

// Traits: descriptive names, often ending in -able or -er
pub trait Serializable {}
pub trait EventHandler {}""",
            "benefits": [
                "Consistency with Rust ecosystem",
                "Better readability",
                "Follows community conventions"
            ]
        },
        "builder_pattern": {
            "description": "Use builder pattern for complex construction",
            "good_example": """
// Idiomatic: builder pattern for complex types
#[derive(Debug)]
pub struct HttpClient {
    base_url: String,
    timeout: Duration,
    headers: HashMap<String, String>,
    retry_attempts: u32,
}

pub struct HttpClientBuilder {
    base_url: Option<String>,
    timeout: Duration,
    headers: HashMap<String, String>,
    retry_attempts: u32,
}

impl HttpClientBuilder {
    pub fn new() -> Self {
        Self {
            base_url: None,
            timeout: Duration::from_secs(30),
            headers: HashMap::new(),
            retry_attempts: 3,
        }
    }
    
    pub fn base_url(mut self, url: impl Into<String>) -> Self {
        self.base_url = Some(url.into());
        self
    }
    
    pub fn timeout(mut self, timeout: Duration) -> Self {
        self.timeout = timeout;
        self
    }
    
    pub fn header(mut self, key: impl Into<String>, value: impl Into<String>) -> Self {
        self.headers.insert(key.into(), value.into());
        self
    }
    
    pub fn build(self) -> Result<HttpClient, BuilderError> {
        let base_url = self.base_url.ok_or(BuilderError::MissingBaseUrl)?;
        
        Ok(HttpClient {
            base_url,
            timeout: self.timeout,
            headers: self.headers,
            retry_attempts: self.retry_attempts,
        })
    }
}

// Usage
let client = HttpClient::builder()
    .base_url("https://api.example.com")
    .timeout(Duration::from_secs(60))
    .header("User-Agent", "MyApp/1.0")
    .build()?;"""
        }
    }
    
    # Pattern: Documentation Best Practices
    DOCUMENTATION_PATTERNS = {
        "doc_comments": {
            "description": "Write comprehensive documentation",
            "good_example": """
/// Represents a user in the system.
///
/// A user has a unique ID, name, and email address. Users can be
/// created, updated, and deleted through the user management API.
///
/// # Examples
///
/// ```
/// use myapp::User;
///
/// let user = User::new(1, "Alice", "alice@example.com")?;
/// assert_eq!(user.name(), "Alice");
/// ```
///
/// # Errors
///
/// This function will return an error if the email address is invalid.
#[derive(Debug, Clone)]
pub struct User {
    id: u32,
    name: String,
    email: String,
}

impl User {
    /// Creates a new user with the given ID, name, and email.
    ///
    /// # Arguments
    ///
    /// * `id` - The unique identifier for the user
    /// * `name` - The user's display name
    /// * `email` - The user's email address
    ///
    /// # Errors
    ///
    /// Returns [`UserError::InvalidEmail`] if the email format is invalid.
    ///
    /// # Examples
    ///
    /// ```
    /// # use myapp::{User, UserError};
    /// let user = User::new(1, "Alice", "alice@example.com")?;
    /// # Ok::<(), UserError>(())
    /// ```
    pub fn new(id: u32, name: impl Into<String>, email: impl Into<String>) -> Result<Self, UserError> {
        let email = email.into();
        if !email.contains('@') {
            return Err(UserError::InvalidEmail);
        }
        
        Ok(User {
            id,
            name: name.into(),
            email,
        })
    }
}""",
            "benefits": [
                "Self-documenting code",
                "Better IDE support",
                "Testable documentation examples"
            ]
        }
    }

class RustIdiomaticAnalyzer:
    """Rust code analyzer for idiomatic patterns"""
    
    def __init__(self):
        self.knowledge_base = RustIdiomaticKnowledgeBase()
    
    async def analyze_idiomatic_rust(self, code: str) -> IdiomaticAnalysisResult:
        """Analyze Rust code for idiomatic patterns and anti-patterns"""
        
        score = 50  # Base idiomaticity score
        category_scores = {}
        idiomatic_patterns = []
        anti_patterns = []
        suggestions = []
        refactored_examples = {}
        api_compliance = {}
        
        # Analyze immutability patterns
        immutability_score = await self._analyze_immutability(code)
        category_scores["immutability"] = immutability_score
        score += (immutability_score - 50) * 0.2
        
        # Analyze error handling
        error_score = await self._analyze_error_handling(code)
        category_scores["error_handling"] = error_score
        score += (error_score - 50) * 0.25
        
        # Analyze type conversions
        conversion_score = await self._analyze_type_conversions(code)
        category_scores["type_conversions"] = conversion_score
        score += (conversion_score - 50) * 0.15
        
        # Analyze ownership patterns
        ownership_score = await self._analyze_ownership(code)
        category_scores["ownership"] = ownership_score
        score += (ownership_score - 50) * 0.2
        
        # Analyze enum usage
        enum_score = await self._analyze_enum_usage(code)
        category_scores["enum_usage"] = enum_score
        score += (enum_score - 50) * 0.1
        
        # Analyze async patterns
        async_score = await self._analyze_async_patterns(code)
        category_scores["async_patterns"] = async_score
        score += (async_score - 50) * 0.1
        
        # Generate suggestions and refactoring examples
        suggestions.extend(await self._generate_suggestions(category_scores))
        refactored_examples.update(await self._generate_refactoring_examples(code, category_scores))
        
        # Check API guideline compliance
        api_compliance.update(await self._check_api_guidelines(code))
        
        final_score = max(0, min(100, int(score)))
        
        return IdiomaticAnalysisResult(
            code=code,
            idiomaticity_score=final_score,
            category_scores=category_scores,
            idiomatic_patterns_found=idiomatic_patterns,
            anti_patterns_found=anti_patterns,
            suggestions=suggestions,
            refactored_examples=refactored_examples,
            compliance_with_api_guidelines=api_compliance
        )
    
    async def _analyze_immutability(self, code: str) -> int:
        """Analyze immutability patterns"""
        score = 50
        
        # Count mut usage
        mut_count = len(re.findall(r'\bmut\s+\w+', code))
        total_bindings = len(re.findall(r'\blet\s+(?:mut\s+)?\w+', code))
        
        if total_bindings > 0:
            mut_ratio = mut_count / total_bindings
            if mut_ratio < 0.2:  # Less than 20% mutable
                score += 20
            elif mut_ratio > 0.5:  # More than 50% mutable
                score -= 15
        
        # Check for immutable data structure usage
        if any(pattern in code for pattern in ["Vec::new()", ".iter().map", ".iter().filter"]):
            score += 10
        
        # Check for builder patterns
        if re.search(r'\.builder\(\)', code):
            score += 10
        
        return min(100, max(0, score))
    
    async def _analyze_error_handling(self, code: str) -> int:
        """Analyze error handling patterns"""
        score = 50
        
        # Check for Result usage
        result_usage = len(re.findall(r'Result<[^>]+>', code))
        if result_usage > 0:
            score += 15
        
        # Check for ? operator
        question_marks = code.count('?')
        if question_marks > 0:
            score += 10
        
        # Check for proper error types
        if 'thiserror::Error' in code or '#[derive(Error)]' in code:
            score += 15
        
        # Penalize panic usage
        panic_count = len(re.findall(r'panic!\(|\.expect\(|\.unwrap\(', code))
        if panic_count > 0:
            score -= panic_count * 5
        
        # Check for Option usage
        option_usage = len(re.findall(r'Option<[^>]+>', code))
        if option_usage > 0:
            score += 10
        
        return min(100, max(0, score))
    
    async def _analyze_type_conversions(self, code: str) -> int:
        """Analyze type conversion patterns"""
        score = 50
        
        # Check for From/Into trait implementations
        if 'impl From<' in code or 'impl Into<' in code:
            score += 20
        
        # Check for TryFrom usage
        if 'impl TryFrom<' in code or 'TryFrom::try_from' in code:
            score += 15
        
        # Check for proper conversion function usage
        if any(pattern in code for pattern in ['.into()', '.from()', 'TryInto::try_into']):
            score += 10
        
        return min(100, max(0, score))
    
    async def _analyze_ownership(self, code: str) -> int:
        """Analyze ownership and borrowing patterns"""
        score = 50
        
        # Check for proper reference usage
        ref_params = len(re.findall(r'&\w+', code))
        owned_params = len(re.findall(r'fn \w+\([^)]*[^&]\w+:', code))
        
        if ref_params > owned_params:
            score += 15
        
        # Check for Cow usage
        if 'Cow<' in code:
            score += 10
        
        # Check for Rc/Arc usage for shared ownership
        if any(pattern in code for pattern in ['Rc<', 'Arc<']):
            score += 10
        
        # Penalize unnecessary clones
        clone_count = code.count('.clone()')
        if clone_count > 3:
            score -= (clone_count - 3) * 2
        
        return min(100, max(0, score))
    
    async def _analyze_enum_usage(self, code: str) -> int:
        """Analyze enum vs boolean usage"""
        score = 50
        
        # Check for enum definitions
        enum_count = len(re.findall(r'enum \w+', code))
        if enum_count > 0:
            score += 15
        
        # Check for match expressions
        match_count = len(re.findall(r'match \w+', code))
        if match_count > 0:
            score += 10
        
        # Penalize excessive boolean parameters
        bool_params = len(re.findall(r'bool(?:,|\))', code))
        if bool_params > 2:
            score -= (bool_params - 2) * 5
        
        return min(100, max(0, score))
    
    async def _analyze_async_patterns(self, code: str) -> int:
        """Analyze async/await patterns"""
        score = 50
        
        # Check for proper async function usage
        if 'async fn' in code:
            score += 15
        
        # Check for .await usage
        await_count = code.count('.await')
        if await_count > 0:
            score += 10
        
        # Check for proper error propagation in async
        if 'async fn' in code and '?' in code:
            score += 10
        
        # Check for concurrent operations
        if any(pattern in code for pattern in ['join!', 'try_join!', 'future::join_all']):
            score += 15
        
        return min(100, max(0, score))
    
    async def _generate_suggestions(self, category_scores: Dict[str, int]) -> List[str]:
        """Generate improvement suggestions based on scores"""
        suggestions = []
        
        if category_scores.get("error_handling", 50) < 70:
            suggestions.append("🛡️ Use Result<T, E> instead of panicking for recoverable errors")
            suggestions.append("❓ Use the ? operator for cleaner error propagation")
        
        if category_scores.get("immutability", 50) < 70:
            suggestions.append("🔒 Prefer immutable bindings - only use 'mut' when necessary")
            suggestions.append("🏗️ Consider using builder patterns for complex object construction")
        
        if category_scores.get("ownership", 50) < 70:
            suggestions.append("📚 Take references (&T) by default, owned values (T) when needed")
            suggestions.append("🐄 Consider using Cow<str> for flexible string handling")
        
        if category_scores.get("enum_usage", 50) < 70:
            suggestions.append("🎭 Use enums instead of boolean flags for better expressiveness")
            suggestions.append("🔀 Use match expressions for exhaustive pattern matching")
        
        return suggestions
    
    async def _generate_refactoring_examples(self, code: str, scores: Dict[str, int]) -> Dict[str, str]:
        """Generate refactoring examples based on common patterns"""
        examples = {}
        
        # Error handling refactoring
        if "unwrap()" in code or "expect(" in code:
            examples["error_handling"] = """
// Instead of:
let data = fs::read_to_string(path).unwrap();

// Use:
let data = fs::read_to_string(path)?;
// or
let data = fs::read_to_string(path).map_err(|e| MyError::FileRead(e))?;
"""
        
        # Immutability refactoring
        if re.search(r'let mut \w+ = [^;]+;\s*(?!//)(?![^;]*=)', code):
            examples["immutability"] = """
// Instead of unnecessary mut:
let mut data = Vec::new();
data.push(1);

// Consider:
let data = vec![1];
// or use builder pattern for complex construction
"""
        
        return examples
    
    async def _check_api_guidelines(self, code: str) -> Dict[str, bool]:
        """Check compliance with Rust API guidelines"""
        compliance = {}
        
        # Check naming conventions
        has_snake_case_functions = bool(re.search(r'fn [a-z][a-z0-9_]*', code))
        has_pascal_case_types = bool(re.search(r'struct [A-Z][A-Za-z0-9]*', code))
        
        compliance["proper_naming"] = has_snake_case_functions and has_pascal_case_types
        compliance["uses_result_for_errors"] = "Result<" in code
        compliance["has_documentation"] = "///" in code
        compliance["uses_standard_traits"] = any(trait in code for trait in ["Debug", "Clone", "PartialEq"])
        
        return compliance

class RustProjectGenerator:
    """Generate Rust projects following idiomatic patterns"""
    
    def __init__(self):
        self.knowledge_base = RustIdiomaticKnowledgeBase()
    
    async def generate_idiomatic_project(
        self,
        project_type: str,
        features: Optional[List[str]] = None,
        complexity: str = "intermediate"
    ) -> Dict[str, Any]:
        """Generate complete idiomatic Rust project"""
        
        if features is None:
            features = ["error_handling", "async", "serialization"]
        
        project_templates = {
            "library": self._generate_library_project,
            "binary": self._generate_binary_project,
            "web_api": self._generate_web_api_project,
            "cli": self._generate_cli_project,
        }
        
        if project_type not in project_templates:
            return {"error": f"Project type '{project_type}' not supported"}
        
        return await project_templates[project_type](features, complexity)
    
    async def _generate_library_project(self, features: List[str], complexity: str) -> Dict[str, Any]:
        """Generate idiomatic Rust library"""
        
        cargo_toml = f"""[package]
name = "my-rust-library"
version = "0.1.0"
edition = "2021"
rust-version = "1.70"
description = "An idiomatic Rust library"
license = "MIT OR Apache-2.0"
repository = "https://github.com/user/my-rust-library"
keywords = ["rust", "library"]
categories = ["development-tools"]

[dependencies]
{self._get_feature_dependencies(features)}

[dev-dependencies]
tokio-test = "0.4"
proptest = "1.0"

[[example]]
name = "basic_usage"
required-features = []
"""
        
        lib_rs = '''//! # My Rust Library
//!
//! An idiomatic Rust library demonstrating best practices.
//!
//! ## Examples
//!
//! ```rust
//! use my_rust_library::Calculator;
//!
//! let calc = Calculator::new();
//! let result = calc.add(2, 3)?;
//! assert_eq!(result, 5);
//! # Ok::<(), Box<dyn std::error::Error>>(())
//! ```

#![deny(missing_docs)]
#![warn(rust_2018_idioms, unused_lifetimes, unused_qualifications)]

use std::fmt;

pub use self::calculator::Calculator;
pub use self::error::{Error, Result};

mod calculator;
mod error;

/// Configuration for the library
#[derive(Debug, Clone)]
pub struct Config {
    /// Maximum precision for calculations
    pub precision: u32,
    /// Whether to enable debugging
    pub debug: bool,
}

impl Default for Config {
    fn default() -> Self {
        Self {
            precision: 10,
            debug: false,
        }
    }
}

impl Config {
    /// Creates a new configuration builder
    pub fn builder() -> ConfigBuilder {
        ConfigBuilder::default()
    }
}

/// Builder for creating configurations
#[derive(Debug, Default)]
pub struct ConfigBuilder {
    precision: Option<u32>,
    debug: bool,
}

impl ConfigBuilder {
    /// Sets the precision
    pub fn precision(mut self, precision: u32) -> Self {
        self.precision = Some(precision);
        self
    }
    
    /// Enables debug mode
    pub fn debug(mut self) -> Self {
        self.debug = true;
        self
    }
    
    /// Builds the configuration
    pub fn build(self) -> Config {
        Config {
            precision: self.precision.unwrap_or(10),
            debug: self.debug,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_config_builder() {
        let config = Config::builder()
            .precision(20)
            .debug()
            .build();
            
        assert_eq!(config.precision, 20);
        assert!(config.debug);
    }
}
'''
        
        error_rs = '''//! Error types for the library

use std::fmt;

/// The main error type for this library
#[derive(Debug, Clone)]
pub enum Error {
    /// Invalid input was provided
    InvalidInput {
        /// Description of what was invalid
        message: String,
    },
    /// Calculation overflow occurred
    Overflow,
    /// Division by zero attempted
    DivisionByZero,
}

impl fmt::Display for Error {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Error::InvalidInput { message } => write!(f, "Invalid input: {}", message),
            Error::Overflow => write!(f, "Calculation overflow"),
            Error::DivisionByZero => write!(f, "Division by zero"),
        }
    }
}

impl std::error::Error for Error {}

/// A specialized Result type for this library
pub type Result<T> = std::result::Result<T, Error>;

impl From<std::num::ParseIntError> for Error {
    fn from(_: std::num::ParseIntError) -> Self {
        Error::InvalidInput {
            message: "Failed to parse integer".to_string(),
        }
    }
}
'''
        
        calculator_rs = '''//! Calculator implementation

use crate::{Config, Error, Result};

/// A calculator that performs arithmetic operations
#[derive(Debug)]
pub struct Calculator {
    config: Config,
}

impl Calculator {
    /// Creates a new calculator with default configuration
    pub fn new() -> Self {
        Self::with_config(Config::default())
    }
    
    /// Creates a calculator with the given configuration
    pub fn with_config(config: Config) -> Self {
        Self { config }
    }
    
    /// Adds two numbers
    /// 
    /// # Examples
    /// 
    /// ```
    /// # use my_rust_library::Calculator;
    /// let calc = Calculator::new();
    /// let result = calc.add(2, 3)?;
    /// assert_eq!(result, 5);
    /// # Ok::<(), my_rust_library::Error>(())
    /// ```
    pub fn add(&self, a: i64, b: i64) -> Result<i64> {
        a.checked_add(b).ok_or(Error::Overflow)
    }
    
    /// Subtracts two numbers
    pub fn subtract(&self, a: i64, b: i64) -> Result<i64> {
        a.checked_sub(b).ok_or(Error::Overflow)
    }
    
    /// Multiplies two numbers
    pub fn multiply(&self, a: i64, b: i64) -> Result<i64> {
        a.checked_mul(b).ok_or(Error::Overflow)
    }
    
    /// Divides two numbers
    pub fn divide(&self, a: i64, b: i64) -> Result<f64> {
        if b == 0 {
            return Err(Error::DivisionByZero);
        }
        Ok(a as f64 / b as f64)
    }
}

impl Default for Calculator {
    fn default() -> Self {
        Self::new()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        let calc = Calculator::new();
        assert_eq!(calc.add(2, 3).unwrap(), 5);
    }

    #[test]
    fn test_add_overflow() {
        let calc = Calculator::new();
        let result = calc.add(i64::MAX, 1);
        assert!(matches!(result, Err(Error::Overflow)));
    }

    #[test]
    fn test_divide_by_zero() {
        let calc = Calculator::new();
        let result = calc.divide(10, 0);
        assert!(matches!(result, Err(Error::DivisionByZero)));
    }
}
'''
        
        return {
            "project_type": "library",
            "files": {
                "Cargo.toml": cargo_toml,
                "src/lib.rs": lib_rs,
                "src/error.rs": error_rs,
                "src/calculator.rs": calculator_rs,
                "README.md": self._generate_readme("library"),
                ".gitignore": self._generate_gitignore(),
            },
            "idiomatic_patterns_used": [
                "✅ Comprehensive error handling with custom Error types",
                "✅ Builder pattern for complex configuration",
                "✅ Result<T, E> for fallible operations",
                "✅ Proper documentation with examples",
                "✅ Following Rust naming conventions",
                "✅ Using #![deny(missing_docs)] for documentation completeness",
                "✅ Implementing standard traits (Debug, Clone, Default)",
                "✅ Checked arithmetic to prevent overflow"
            ],
            "api_guidelines_compliance": [
                "📚 C-SMART: Smart constructor patterns",
                "🛡️ C-GOOD-ERR: Good error messages",
                "📖 C-EXAMPLE: Documentation includes examples",
                "🏗️ C-BUILDER: Builder pattern for complex types",
                "🔧 C-CONV-TRAITS: Implements standard conversion traits"
            ],
            "next_steps": [
                "cargo build # Build the library",
                "cargo test # Run all tests",  
                "cargo doc --open # Generate and view documentation",
                "cargo clippy # Run linter",
                "cargo fmt # Format code"
            ]
        }
    
    def _get_feature_dependencies(self, features: List[str]) -> str:
        """Generate dependencies based on features"""
        deps = []
        
        if "async" in features:
            deps.append('tokio = { version = "1.0", features = ["full"] }')
        
        if "serialization" in features:
            deps.append('serde = { version = "1.0", features = ["derive"] }')
            deps.append('serde_json = "1.0"')
        
        if "error_handling" in features:
            deps.append('thiserror = "1.0"')
            deps.append('anyhow = "1.0"')
        
        return "\n".join(deps)
    
    def _generate_readme(self, project_type: str) -> str:
        return f"""# My Rust {project_type.title()}

An idiomatic Rust {project_type} following best practices and API guidelines.

## Features

- 🦀 **Idiomatic Rust**: Follows rust-lang/api-guidelines
- 🛡️ **Robust Error Handling**: Custom error types with detailed messages  
- 📚 **Comprehensive Documentation**: Examples and detailed API docs
- 🧪 **Well Tested**: Unit tests and property-based testing
- ⚡ **Performance**: Zero-cost abstractions and efficient algorithms

## Usage

```rust
use my_rust_library::Calculator;

let calc = Calculator::new();
let result = calc.add(2, 3)?;
assert_eq!(result, 5);
```

## Development

This project follows Rust idiomatic patterns from:
- [rust-lang/api-guidelines](https://rust-lang.github.io/api-guidelines/)
- [mre/idiomatic-rust](https://github.com/mre/idiomatic-rust)

### Commands

```bash
cargo build          # Build the project
cargo test           # Run tests
cargo clippy         # Lint code
cargo fmt           # Format code
cargo doc --open    # Generate and view docs
```

## Contributing

Please ensure your code follows the established patterns and passes all checks.
"""
    
    def _generate_gitignore(self) -> str:
        return """/target/
Cargo.lock
.env
.DS_Store
*.log
.vscode/
.idea/
"""

# ================================
# RUST MCP TOOLS
# ================================

@mcp.tool(tags=["analysis", "idiomatic", "scoring"])
async def analyze_idiomatic_rust(code: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Analyzes Rust code for idiomatic patterns based on mre/idiomatic-rust.
    
    Args:
        code: Rust code for analysis
        
    Returns:
        Complete analysis with idiomaticity score and suggestions
    """
    try:
        analyzer = RustIdiomaticAnalyzer()
        analysis = await analyzer.analyze_idiomatic_rust(code)
        
        logger.info(f"Analyzed Rust code - idiomaticity score: {analysis.idiomaticity_score}")
        
        return {
            "idiomaticity_score": analysis.idiomaticity_score,
            "category_scores": analysis.category_scores,
            "idiomatic_patterns_found": analysis.idiomatic_patterns_found,
            "anti_patterns_found": analysis.anti_patterns_found,
            "suggestions": analysis.suggestions,
            "refactored_examples": analysis.refactored_examples,
            "api_guidelines_compliance": analysis.compliance_with_api_guidelines,
            "overall_grade": (
                "Excellent" if analysis.idiomaticity_score >= 90 else
                "Good" if analysis.idiomaticity_score >= 75 else
                "Needs Improvement" if analysis.idiomaticity_score >= 60 else
                "Poor"
            )
        }
        
    except Exception as e:
        logger.error(f"Error analyzing Rust code: {str(e)}")
        raise

@mcp.tool(tags=["generation", "project", "templates"])
async def generate_idiomatic_project(
    project_type: str,
    features: Optional[List[str]] = None,
    complexity: str = "intermediate",
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Generates idiomatic Rust project following mre/idiomatic-rust patterns.
    
    Args:
        project_type: Project type (library, binary, web-api, cli)
        features: List of desired features
        complexity: Complexity level (beginner, intermediate, advanced)
        
    Returns:
        Complete project structure with idiomatic code
    """
    try:
        generator = RustProjectGenerator()
        
        result = await generator.generate_idiomatic_project(
            project_type=project_type,
            features=features,
            complexity=complexity
        )
        
        logger.info(f"Generated idiomatic Rust project: {project_type}")
        
        return result
        
    except Exception as e:
        logger.error(f"Error generating Rust project: {str(e)}")
        raise

@mcp.tool(tags=["patterns", "reference", "documentation"])
async def get_idiomatic_patterns(category: str = "all", ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Returns idiomatic Rust patterns by category based on mre/idiomatic-rust.
    
    Args:
        category: Specific category or "all" for all categories
        
    Returns:
        Idiomatic patterns with practical examples
    """
    try:
        knowledge_base = RustIdiomaticKnowledgeBase()
        
        categories = {
            "immutability": knowledge_base.IMMUTABILITY_PATTERNS,
            "error_handling": knowledge_base.ERROR_HANDLING_PATTERNS,
            "type_conversions": knowledge_base.TYPE_CONVERSION_PATTERNS,
            "ownership": knowledge_base.OWNERSHIP_PATTERNS,
            "enum_patterns": knowledge_base.ENUM_PATTERNS,
            "async_patterns": knowledge_base.ASYNC_PATTERNS,
            "trait_patterns": knowledge_base.TRAIT_PATTERNS,
            "iterator_patterns": knowledge_base.ITERATOR_PATTERNS,
            "api_design": knowledge_base.API_DESIGN_PATTERNS,
            "documentation": knowledge_base.DOCUMENTATION_PATTERNS,
        }
        
        if category == "all":
            return {
                "source": "mre/idiomatic-rust + rust-lang/api-guidelines",
                "version": knowledge_base.VERSION,
                "edition": knowledge_base.EDITION,
                "categories": categories,
                "key_principles": [
                    "Immutability by default",
                    "Explicit error handling with Result/Option",
                    "Zero-cost abstractions",
                    "Memory safety without garbage collection",
                    "Concurrent programming without data races",
                    "Trait-based generics for flexibility"
                ]
            }
        
        if category not in categories:
            return {"error": f"Category '{category}' not found. Available: {list(categories.keys())}"}
        
        return {
            "category": category,
            "patterns": categories[category],
            "source": "mre/idiomatic-rust patterns collection"
        }
        
    except Exception as e:
        logger.error(f"Error getting idiomatic patterns: {str(e)}")
        raise

@mcp.tool(tags=["refactoring", "improvement", "optimization"])
async def refactor_to_idiomatic(
    code: str,
    focus_areas: Optional[List[str]] = None,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Refactors Rust code to follow idiomatic patterns.
    
    Args:
        code: Original Rust code
        focus_areas: Specific areas to focus refactoring on
        
    Returns:
        Refactored code with explanations of changes
    """
    try:
        if focus_areas is None:
            focus_areas = ["error_handling", "immutability", "ownership", "type_safety"]
        
        # Analyze original code
        analyzer = RustIdiomaticAnalyzer()
        original_analysis = await analyzer.analyze_idiomatic_rust(code)
        
        refactored_code = code
        changes_made = []
        
        # Apply refactoring based on focus areas
        if "error_handling" in focus_areas:
            # Replace unwrap() with proper error handling
            if ".unwrap()" in refactored_code:
                refactored_code = refactored_code.replace(".unwrap()", "?")
                changes_made.append("🛡️ Replaced .unwrap() calls with ? operator for better error propagation")
            
            # Add Result return types where missing
            if "-> Result<" not in refactored_code and "?" in refactored_code:
                refactored_code = re.sub(
                    r'fn (\w+)\([^)]*\) {',
                    r'fn \1([^)]*) -> Result<(), Box<dyn std::error::Error>> {',
                    refactored_code
                )
                changes_made.append("📋 Added Result return type for functions using ? operator")
        
        if "immutability" in focus_areas:
            # Suggest removing unnecessary mut
            mut_suggestions = []
            for match in re.finditer(r'let mut (\w+) = ([^;]+);(?!\s*\1\s*=)', refactored_code):
                var_name = match.group(1)
                if not re.search(f'{var_name}\\s*=', refactored_code[match.end():]):
                    mut_suggestions.append(f"Consider removing 'mut' from '{var_name}' if it's not modified")
            
            if mut_suggestions:
                changes_made.extend([f"🔒 {suggestion}" for suggestion in mut_suggestions])
        
        if "ownership" in focus_areas:
            # Suggest taking references instead of owned values
            if re.search(r'fn \w+\([^)]*\w+: String', refactored_code):
                changes_made.append("📚 Consider taking &str instead of String for parameters that don't need ownership")
            
            if re.search(r'fn \w+\([^)]*\w+: Vec<', refactored_code):
                changes_made.append("📚 Consider taking &[T] instead of Vec<T> for parameters that only read")
        
        # Analyze refactored code
        refactored_analysis = await analyzer.analyze_idiomatic_rust(refactored_code)
        
        return {
            "original_code": code,
            "refactored_code": refactored_code,
            "changes_made": changes_made,
            "original_score": original_analysis.idiomaticity_score,
            "refactored_score": refactored_analysis.idiomaticity_score,
            "improvement": refactored_analysis.idiomaticity_score - original_analysis.idiomaticity_score,
            "patterns_applied": [
                "Ergonomic error handling with ?",
                "Immutability by default",
                "Optimal ownership and borrowing",
                "Type safety improvements"
            ],
            "suggestions": refactored_analysis.suggestions
        }
        
    except Exception as e:
        logger.error(f"Error refactoring Rust code: {str(e)}")
        raise

@mcp.tool(tags=["api-guidelines", "best-practices", "reference"])
async def get_rust_api_guidelines(ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Returns official Rust API guidelines (rust-lang/api-guidelines).
    
    Returns:
        Guidelines organized by category
    """
    try:
        return {
            "title": "Rust API Guidelines (rust-lang/api-guidelines)",
            "source": "https://rust-lang.github.io/api-guidelines/",
            "categories": {
                "naming": {
                    "C-CASE": "Follow Rust naming conventions",
                    "C-WORD-ORDER": "Use consistent word order in names",
                    "C-FEATURE": "Names use a consistent vocabulary",
                },
                "interoperability": {
                    "C-COMMON-TRAITS": "Types eagerly implement common traits",
                    "C-CONV-TRAITS": "Conversions use the standard traits From, AsRef, AsMut",
                    "C-COLLECT": "Collections implement FromIterator and Extend",
                },
                "macros": {
                    "C-EVOCATIVE": "Item names are evocative of their functionality", 
                    "C-MACRO-VIS": "Public macros document visibility rules",
                },
                "documentation": {
                    "C-EXAMPLE": "Examples use ?, not try!, not unwrap",
                    "C-QUESTION-MARK": "Examples use ?, not try!, not unwrap",
                    "C-FAILURE": "Function docs include error conditions in \"Errors\" section",
                },
                "predictability": {
                    "C-SMART-PTR": "Smart pointers do not add inherent methods",
                    "C-CONV-SPECIFIC": "Conversions live on the most specific type involved",
                    "C-GENERIC": "Functions expose intermediate results to avoid duplicate work",
                },
                "flexibility": {
                    "C-INTERMEDIATE": "Caller decides where to copy and place data",
                    "C-CALLER-CONTROL": "Functions minimize assumptions about parameters by using generics",
                    "C-ACCEPT": "Traits are object-safe if they may be useful as trait objects",
                },
                "type_safety": {
                    "C-NEWTYPE": "Newtypes provide static distinctions",
                    "C-CUSTOM-TYPE": "Arguments potentially involvingside effects use custom types",
                    "C-BITFLAG": "Bitflags are represented by a newtype",
                },
                "dependability": {
                    "C-VALIDATE": "Destructors never fail",
                    "C-DTOR-FAIL": "Destructors that may block have alternatives",
                    "C-DTOR-BLOCK": "Destructors never block",
                },
                "debuggability": {
                    "C-DEBUG": "All public types implement Debug",
                    "C-DEBUG-NONEMPTY": "Debug representations are never empty",
                },
                "future_proofing": {
                    "C-SEALED": "Sealed traits protect against downstream implementations",
                    "C-STRUCT-PRIVATE": "Structs have private fields",
                    "C-NEWTYPE-HIDE": "Newtypes encapsulate implementation details",
                },
                "necessities": {
                    "C-STABLE": "Public dependencies of a stable crate are stable",
                    "C-PERMISSIVE": "Crate and its dependencies have a permissive license",
                }
            },
            "key_principles": [
                "Make the right thing easy and the wrong thing hard",
                "APIs should be unsurprising",
                "APIs should be flexible and composable",
                "APIs should use types to prevent errors",
                "Documentation should be comprehensive and include examples"
            ]
        }
        
    except Exception as e:
        logger.error(f"Error getting API guidelines: {str(e)}")
        raise

# ================================
# MCP PROMPTS
# ================================


@mcp.prompt()
async def refactor_rust_to_idiomatic(
    code: str,
    focus_areas: List[str] = []
) -> List[Dict[str, str]]:
    """
    Generate a prompt to refactor Rust code to idiomatic patterns.

    Args:
        code: Rust code to refactor
        focus_areas: Areas to focus on (error_handling, ownership, immutability, etc.)
    """
    default_areas = ["error_handling", "ownership", "immutability", "type_safety"]
    areas = focus_areas if focus_areas else default_areas

    return [
        {
            "role": "system",
            "content": """You are a Rust expert specializing in idiomatic code patterns.

Key idiomatic Rust principles:
1. **Immutability by default**: Use `let` instead of `let mut` unless mutation is needed
2. **Error handling**: Use Result<T, E> instead of panicking, propagate with ?
3. **Ownership**: Take references (&T) by default, owned values when needed
4. **Type conversions**: Use From/Into traits, TryFrom for fallible conversions
5. **Enums over booleans**: Use expressive enums for state machines
6. **Iterators over loops**: Use .iter().map().filter().collect()
7. **Builder pattern**: For complex type construction
8. **Newtype pattern**: For type-safe wrappers

Anti-patterns to avoid:
- .unwrap() and .expect() in library code
- Unnecessary .clone() calls
- Excessive mut bindings
- Boolean flags instead of enums
- Manual loops instead of iterators"""
        },
        {
            "role": "user",
            "content": f"""Refactor this Rust code to be more idiomatic:

```rust
{code}
```

Focus areas: {', '.join(areas)}

Requirements:
1. Identify and fix anti-patterns
2. Apply idiomatic Rust patterns
3. Use proper error handling with Result/Option
4. Optimize ownership and borrowing
5. Add appropriate documentation
6. Explain each change made
7. Show before/after comparison"""
        }
    ]


@mcp.prompt()
async def design_rust_api(
    api_purpose: str,
    entities: List[str] = [],
    operations: List[str] = []
) -> List[Dict[str, str]]:
    """
    Generate a prompt to design a Rust API following api-guidelines.

    Args:
        api_purpose: Purpose of the API
        entities: Main entities/types in the API
        operations: Operations the API should support
    """
    default_entities = ["Config", "Client", "Error"]
    entities_list = entities if entities else default_entities

    default_operations = ["create", "read", "update", "delete"]
    ops_list = operations if operations else default_operations

    return [
        {
            "role": "system",
            "content": """You are an expert in Rust API design following rust-lang/api-guidelines.

Key API Guidelines:
1. **Naming (C-CASE)**: snake_case for functions, PascalCase for types, SCREAMING_CASE for constants
2. **Common Traits (C-COMMON-TRAITS)**: Implement Debug, Clone, PartialEq where appropriate
3. **Conversions (C-CONV-TRAITS)**: Use From/Into, AsRef/AsMut, TryFrom/TryInto
4. **Documentation (C-EXAMPLE)**: Include examples using ? not unwrap()
5. **Errors (C-FAILURE)**: Document error conditions, use custom error types
6. **Flexibility (C-GENERIC)**: Use generics and impl Trait for flexibility
7. **Type Safety (C-NEWTYPE)**: Use newtypes for type-safe distinctions
8. **Builder Pattern**: For types with many optional parameters

Design principles:
- Make the right thing easy, wrong thing hard
- APIs should be unsurprising
- Flexible and composable
- Use types to prevent errors
- Comprehensive documentation"""
        },
        {
            "role": "user",
            "content": f"""Design a Rust API for: {api_purpose}

Main entities: {', '.join(entities_list)}
Operations: {', '.join(ops_list)}

Requirements:
1. Define public API with proper visibility
2. Create custom error types with thiserror
3. Use builder pattern for complex configuration
4. Implement common traits (Debug, Clone, etc.)
5. Add comprehensive documentation with examples
6. Use Result<T, E> for fallible operations
7. Apply newtype pattern for type safety
8. Include module organization structure"""
        }
    ]


@mcp.prompt()
async def implement_error_handling(
    error_scenarios: List[str] = [],
    use_thiserror: bool = True,
    recoverable: bool = True
) -> List[Dict[str, str]]:
    """
    Generate a prompt to implement proper Rust error handling.

    Args:
        error_scenarios: Types of errors to handle
        use_thiserror: Whether to use thiserror crate
        recoverable: Whether errors should be recoverable
    """
    default_scenarios = ["io", "parsing", "validation", "network"]
    scenarios = error_scenarios if error_scenarios else default_scenarios

    return [
        {
            "role": "system",
            "content": """You are an expert in Rust error handling patterns.

Error handling strategies:
1. **Custom Error Types**: Define domain-specific errors
2. **thiserror**: For library error types with #[derive(Error)]
3. **anyhow**: For application-level error handling
4. **Result<T, E>**: For all fallible operations
5. **Option<T>**: For values that may not exist
6. **? operator**: For ergonomic error propagation

Error type patterns:
```rust
#[derive(Debug, thiserror::Error)]
pub enum MyError {
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),

    #[error("Parse error: {message}")]
    Parse { message: String },

    #[error("Validation failed: {field}")]
    Validation { field: String },
}
```

Best practices:
- Never panic in library code
- Provide context with error chains
- Make errors actionable
- Use From trait for error conversion
- Document all error conditions"""
        },
        {
            "role": "user",
            "content": f"""Implement error handling for these scenarios:

Error types: {', '.join(scenarios)}
Use thiserror: {'Yes' if use_thiserror else 'No - use manual implementation'}
Recoverable: {'Yes - provide recovery strategies' if recoverable else 'No - fatal errors'}

Requirements:
1. Define comprehensive error enum
2. Implement Display and Error traits
3. Add From implementations for conversion
4. Create helper functions for common errors
5. Show usage examples with ? operator
6. Include error context/chaining
7. Document error handling patterns
8. Provide recovery strategies where applicable"""
        }
    ]


@mcp.prompt()
async def create_async_rust(
    async_operations: List[str] = [],
    runtime: str = "tokio",
    concurrency_pattern: str = "concurrent"
) -> List[Dict[str, str]]:
    """
    Generate a prompt to create idiomatic async Rust code.

    Args:
        async_operations: Types of async operations needed
        runtime: Async runtime (tokio, async-std)
        concurrency_pattern: Concurrency pattern (concurrent, sequential, streaming)
    """
    default_ops = ["http_request", "file_io", "database"]
    operations = async_operations if async_operations else default_ops

    return [
        {
            "role": "system",
            "content": """You are an expert in async Rust programming.

Async Rust patterns:
1. **async fn**: Define async functions that return impl Future
2. **.await**: Await futures at yield points
3. **? operator**: Works with async for error propagation
4. **tokio::spawn**: Spawn concurrent tasks
5. **join!**: Await multiple futures concurrently
6. **select!**: Race multiple futures
7. **Streams**: Async iterators for data processing

Concurrency patterns:
```rust
// Concurrent execution
let (result1, result2) = tokio::join!(
    fetch_data_1(),
    fetch_data_2()
);

// Concurrent with error handling
let results = futures::future::try_join_all(
    urls.iter().map(|url| fetch_url(url))
).await?;

// Stream processing
stream
    .map(|item| process(item))
    .buffer_unordered(10)
    .try_collect()
    .await?
```

Best practices:
- Use async/await over manual Future implementations
- Prefer structured concurrency with join!/select!
- Handle cancellation properly
- Use timeouts for network operations
- Consider backpressure in streams"""
        },
        {
            "role": "user",
            "content": f"""Create async Rust code for these operations:

Operations: {', '.join(operations)}
Runtime: {runtime}
Concurrency pattern: {concurrency_pattern}

Requirements:
1. Define async functions with proper signatures
2. Use {runtime} runtime appropriately
3. Implement {concurrency_pattern} execution pattern
4. Handle errors with Result and ?
5. Add timeouts where appropriate
6. Include cancellation handling
7. Show stream processing if applicable
8. Add documentation and examples"""
        }
    ]


@mcp.prompt()
async def apply_ownership_patterns(
    code: str = "",
    use_case: str = "general"
) -> List[Dict[str, str]]:
    """
    Generate a prompt to apply proper ownership patterns in Rust.

    Args:
        code: Existing code to analyze (optional)
        use_case: Use case (general, performance, shared_state, concurrent)
    """
    return [
        {
            "role": "system",
            "content": """You are an expert in Rust ownership and borrowing patterns.

Ownership patterns:
1. **Take references by default**: &T for read, &mut T for write
2. **Owned values when storing**: Vec<String> not Vec<&str> for collections
3. **Cow<str>**: When you might need to modify borrowed data
4. **Arc/Rc**: For shared ownership (Arc for threads, Rc for single-thread)
5. **Clone when needed**: Be explicit about copies
6. **Into<T>**: Accept owned or convertible values

Function signature patterns:
```rust
// Read-only access - take reference
fn process(data: &[String]) -> usize { ... }

// Need ownership - take owned value
fn consume(data: Vec<String>) -> Vec<String> { ... }

// Flexible input - use Into
fn create(name: impl Into<String>) -> User { ... }

// Maybe modify - use Cow
fn normalize(text: Cow<str>) -> Cow<str> { ... }

// Shared state - use Arc
fn share(data: Arc<Data>) -> Handle { ... }
```

Anti-patterns to avoid:
- Taking String when &str would work
- Unnecessary .clone() calls
- Returning references to local data
- Holding references longer than needed"""
        },
        {
            "role": "user",
            "content": f"""Apply proper ownership patterns for this use case: {use_case}

{f"Existing code to analyze:{chr(10)}```rust{chr(10)}{code}{chr(10)}```" if code else "Create examples for common scenarios"}

Requirements:
1. Analyze or demonstrate ownership patterns
2. Show when to use references vs owned values
3. Demonstrate Cow<T> usage
4. Show Arc/Rc for shared ownership
5. Optimize for {'performance' if use_case == 'performance' else 'clarity'}
6. Avoid unnecessary allocations
7. Handle lifetime annotations if needed
8. Include before/after examples"""
        }
    ]


# ================================
# MCP RESOURCES
# ================================

@mcp.resource(uri="guide://rust-idiomatic-development")
async def get_rust_idiomatic_guide() -> str:
    """Complete Rust idiomatic development guide"""
    return json.dumps({
        "title": "Rust Idiomatic Development Guide 2025",
        "based_on": [
            "mre/idiomatic-rust patterns collection",
            "rust-lang/api-guidelines official guidelines",
            "blessed.rs community recommendations"
        ],
        "sections": {
            "immutability": "Immutability by default and smart mutability",
            "error_handling": "Ergonomic error handling with Result and Option",
            "type_conversions": "From/Into traits and TryFrom patterns",
            "ownership": "Ownership, borrowing, and zero-copy techniques", 
            "enum_patterns": "Expressive enums and pattern matching",
            "async_patterns": "Modern async/await and concurrency patterns",
            "trait_patterns": "Traits, generics, and associated types",
            "iterator_patterns": "Functional programming with iterators",
            "api_design": "API design following rust-lang guidelines",
            "documentation": "Comprehensive documentation with examples"
        },
        "key_crates": {
            "thiserror": "Ergonomic error handling",
            "serde": "Serialization and deserialization",
            "tokio": "Async runtime and utilities",
            "rayon": "Data parallelism",
            "clap": "Command line argument parsing"
        },
        "features": {
            "code_analysis": "Deep analysis of Rust code for idiomatic patterns",
            "project_generation": "Generate complete idiomatic projects",
            "pattern_library": "Comprehensive idiomatic patterns collection",
            "refactoring": "Automatic refactoring to idiomatic Rust",
            "api_compliance": "rust-lang/api-guidelines compliance checking"
        }
    }, indent=2)

# ================================
# SERVER INITIALIZATION
# ================================

if __name__ == "__main__":
    logger.info("🦀 Rust Idiomatic Patterns MCP Server starting...")
    logger.info("📚 Specialized in idiomatic Rust development following mre/idiomatic-rust")
    logger.info("✅ Based on: rust-lang/api-guidelines + mre/idiomatic-rust + blessed.rs")
    logger.info("🔧 Features: Code Analysis | Project Generation | Pattern Library | Refactoring")
    logger.info("\n📝 Available prompts:")
    logger.info("  - refactor_rust_to_idiomatic: Refactor code to idiomatic patterns")
    logger.info("  - design_rust_api: Design API following api-guidelines")
    logger.info("  - implement_error_handling: Implement proper error handling")
    logger.info("  - create_async_rust: Create idiomatic async code")
    logger.info("  - apply_ownership_patterns: Apply ownership patterns correctly")

    # Run the MCP server
    mcp.run()