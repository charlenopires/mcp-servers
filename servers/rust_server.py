#!/usr/bin/env python3
"""
Rust Idiomatic MCP Server - Servidor MCP para desenvolvimento Rust idiomático
============================================================================

Servidor MCP avançado baseado nos padrões idiomáticos de Rust, incluindo:
- Análise de código seguindo rust-lang/api-guidelines
- Padrões idiomáticos do repositório mre/idiomatic-rust
- Error handling ergonômico com Result/Option
- Traits e generics para código flexível e reutilizável
- Async/await patterns com Tokio
- Immutability por padrão e zero-cost abstractions
- Type safety e compile-time guarantees

Baseado em: rust-lang/api-guidelines, mre/idiomatic-rust, e blessed.rs
"""

import asyncio
import json
import re
import logging
from dataclasses import dataclass
from typing import Dict, List, Optional, Any, Tuple, Union
from enum import Enum
from fastmcp import FastMCP
from pydantic import BaseModel, Field

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializar servidor MCP
mcp = FastMCP(
    name="rust-idiomatic-server",
    version="1.80.0",
    description="Servidor MCP para desenvolvimento Rust idiomático seguindo api-guidelines e mre/idiomatic-rust"
)

# ================================
# RUST IDIOMATIC PATTERNS & KNOWLEDGE BASE
# ================================

class IdiomaticCategory(Enum):
    """Categorias de padrões idiomáticos Rust"""
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
    """Níveis de complexidade para análise"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"

@dataclass
class IdiomaticAnalysisResult:
    """Resultado da análise de código Rust idiomático"""
    code: str
    idiomaticity_score: int
    category_scores: Dict[str, int]
    idiomatic_patterns_found: List[str]
    anti_patterns_found: List[str]
    suggestions: List[str]
    refactored_examples: Dict[str, str]
    compliance_with_api_guidelines: Dict[str, bool]

class RustIdiomaticKnowledgeBase:
    """Base de conhecimento Rust idiomático baseada em mre/idiomatic-rust"""
    
    VERSION = "1.80.0"
    EDITION = "2021"
    
    # Padrão: Immutability por padrão
    IMMUTABILITY_PATTERNS = {
        "default_immutable": {
            "principle": "Aim For Immutability in Rust",
            "description": "Variables são imutáveis por padrão - use mut apenas quando necessário",
            "good_example": """
// Idiomático: imutável por padrão
let data = vec![1, 2, 3, 4, 5];
let sum: i32 = data.iter().sum();

// Use mut apenas quando necessário
let mut counter = 0;
for item in &data {
    if item % 2 == 0 {
        counter += 1;
    }
}""",
            "anti_pattern": """
// Anti-padrão: mut desnecessário
let mut data = vec![1, 2, 3, 4, 5]; // não precisa ser mut
let mut sum: i32 = data.iter().sum(); // não precisa ser mut
""",
            "benefits": [
                "Código mais seguro e previsível",
                "Easier to reason about",
                "Concorrência sem data races",
                "Otimizações do compilador"
            ]
        },
        "immutable_collections": {
            "description": "Use coleções imutáveis quando possível",
            "good_example": """
// Idiomático: construção imutável
fn create_lookup_table() -> HashMap<String, u32> {
    [
        ("one".to_string(), 1),
        ("two".to_string(), 2),
        ("three".to_string(), 3),
    ].into_iter().collect()
}

// Ou usando lazy_static para dados constantes
lazy_static! {
    static ref CONSTANTS: HashMap<&'static str, u32> = {
        let mut m = HashMap::new();
        m.insert("one", 1);
        m.insert("two", 2);
        m
    };
}""",
            "anti_pattern": """
// Anti-padrão: mutabilidade desnecessária
fn create_lookup_table() -> HashMap<String, u32> {
    let mut map = HashMap::new();
    map.insert("one".to_string(), 1);
    map.insert("two".to_string(), 2);
    map.insert("three".to_string(), 3);
    map // poderia ser construído de forma imutável
}"""
        }
    }
    
    # Padrão: Error Handling Idiomático
    ERROR_HANDLING_PATTERNS = {
        "result_over_panic": {
            "principle": "Return Result instead of panicking",
            "description": "Use Result<T, E> para errors recuperáveis, panic apenas para bugs",
            "good_example": """
use thiserror::Error;

#[derive(Error, Debug)]
pub enum ConfigError {
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
    #[error("Parse error: {message}")]
    Parse { message: String },
    #[error("Missing required field: {field}")]
    MissingField { field: String },
}

pub type Result<T> = std::result::Result<T, ConfigError>;

// Idiomático: retorna Result
pub fn load_config(path: &Path) -> Result<Config> {
    let content = std::fs::read_to_string(path)?;
    let config: Config = toml::from_str(&content)
        .map_err(|e| ConfigError::Parse { 
            message: e.to_string() 
        })?;
    
    validate_config(&config)?;
    Ok(config)
}""",
            "anti_pattern": """
// Anti-padrão: panic em situações recuperáveis
pub fn load_config(path: &Path) -> Config {
    let content = std::fs::read_to_string(path)
        .expect("Config file must exist"); // panic!
    
    toml::from_str(&content)
        .expect("Config must be valid") // panic!
}"""
        },
        "context_preserving_errors": {
            "description": "Preserve error context using thiserror or anyhow",
            "good_example": """
use anyhow::{Context, Result};

fn process_file(path: &Path) -> Result<ProcessedData> {
    let content = std::fs::read_to_string(path)
        .with_context(|| format!("Failed to read file: {}", path.display()))?;
    
    let parsed = parse_content(&content)
        .with_context(|| "Failed to parse file content")?;
    
    let processed = transform_data(parsed)
        .with_context(|| "Failed to transform parsed data")?;
    
    Ok(processed)
}""",
            "anti_pattern": """
// Anti-padrão: perda de contexto
fn process_file(path: &Path) -> Result<ProcessedData, Box<dyn Error>> {
    let content = std::fs::read_to_string(path)?; // contexto perdido
    let parsed = parse_content(&content)?; // contexto perdido  
    let processed = transform_data(parsed)?; // contexto perdido
    Ok(processed)
}"""
        }
    }
    
    # Padrão: Type Conversions Idiomáticas
    TYPE_CONVERSION_PATTERNS = {
        "from_into_traits": {
            "principle": "Use From/Into for convenient conversions",
            "description": "Implemente From para conversões infallible, TryFrom para fallible",
            "good_example": """
use std::convert::{From, TryFrom};

#[derive(Debug)]
pub struct UserId(u32);

#[derive(Debug)]
pub struct UserName(String);

// Idiomático: From para conversões simples
impl From<u32> for UserId {
    fn from(id: u32) -> Self {
        UserId(id)
    }
}

impl From<String> for UserName {
    fn from(name: String) -> Self {
        UserName(name)
    }
}

// TryFrom para conversões que podem falhar
impl TryFrom<&str> for UserName {
    type Error = ValidationError;
    
    fn try_from(name: &str) -> Result<Self, Self::Error> {
        if name.len() < 3 {
            return Err(ValidationError::TooShort);
        }
        if name.len() > 50 {
            return Err(ValidationError::TooLong);
        }
        Ok(UserName(name.to_string()))
    }
}

// Uso ergonômico
fn create_user(id: u32, name: &str) -> Result<User, ValidationError> {
    Ok(User {
        id: id.into(),           // From<u32>
        name: name.try_into()?,  // TryFrom<&str>
    })
}""",
            "anti_pattern": """
// Anti-padrão: constructors manuais
impl UserId {
    pub fn new(id: u32) -> Self {
        UserId(id)
    }
}

impl UserName {
    pub fn new(name: String) -> Self {
        UserName(name)
    }
    
    pub fn from_str(name: &str) -> Result<Self, ValidationError> {
        // validação...
        Ok(UserName(name.to_string()))
    }
}

// Uso menos ergonômico
fn create_user(id: u32, name: &str) -> Result<User, ValidationError> {
    Ok(User {
        id: UserId::new(id),
        name: UserName::from_str(name)?,
    })
}"""
        },
        "string_handling": {
            "principle": "Taking string arguments in Rust",
            "description": "Use &str para parâmetros, String para ownership",
            "good_example": """
// Idiomático: aceita qualquer string-like type
fn process_name(name: &str) -> String {
    name.trim().to_lowercase()
}

// Flexível para diferentes tipos
fn process_user_data(name: impl AsRef<str>, email: impl AsRef<str>) -> UserData {
    UserData {
        name: process_name(name.as_ref()),
        email: email.as_ref().to_lowercase(),
    }
}

// Pode ser chamado com &str, String, Cow<str>, etc.
let result1 = process_user_data("John Doe", "john@example.com");
let result2 = process_user_data(owned_string, email_string);""",
            "anti_pattern": """
// Anti-padrão: força ownership desnecessário
fn process_name(name: String) -> String {
    name.trim().to_lowercase()
}

// Ou muito específico
fn process_user_data(name: &String, email: &String) -> UserData {
    UserData {
        name: process_name(name.clone()), // clone desnecessário
        email: email.to_lowercase(),
    }
}"""
        }
    }
    
    # Padrão: Enums ao invés de Booleans
    ENUMS_OVER_BOOLS_PATTERNS = {
        "expressive_enums": {
            "principle": "Rust Patterns: Enums Instead Of Booleans",
            "description": "Use enums para expressar intenção, não booleans",
            "good_example": """
// Idiomático: enum expressivo
#[derive(Debug, Clone, Copy)]
pub enum ConnectionState {
    Connected,
    Disconnected,
    Reconnecting,
}

#[derive(Debug, Clone, Copy)]
pub enum SortOrder {
    Ascending,
    Descending,
}

// API clara e expressiva
impl Database {
    pub fn connect(&mut self) -> Result<(), Error> {
        // lógica de conexão
        self.state = ConnectionState::Connected;
        Ok(())
    }
    
    pub fn query_users(&self, order: SortOrder) -> Result<Vec<User>, Error> {
        match order {
            SortOrder::Ascending => self.query("SELECT * FROM users ORDER BY name ASC"),
            SortOrder::Descending => self.query("SELECT * FROM users ORDER BY name DESC"),
        }
    }
}

// Uso claro
db.query_users(SortOrder::Ascending)?;""",
            "anti_pattern": """
// Anti-padrão: boolean flags confusos
impl Database {
    pub fn connect(&mut self, auto_reconnect: bool) -> Result<(), Error> {
        // O que significa auto_reconnect aqui?
    }
    
    pub fn query_users(&self, ascending: bool) -> Result<Vec<User>, Error> {
        if ascending {
            self.query("SELECT * FROM users ORDER BY name ASC")
        } else {
            self.query("SELECT * FROM users ORDER BY name DESC")
        }
    }
}

// Uso confuso
db.query_users(true)?; // true significa o quê?"""
        },
        "state_machines": {
            "description": "Use enums para state machines type-safe",
            "good_example": """
// State machine idiomático
pub enum RequestState {
    Pending,
    InProgress { started_at: SystemTime },
    Completed { result: String, duration: Duration },
    Failed { error: String, retry_count: u32 },
}

impl RequestState {
    pub fn start(self) -> Self {
        match self {
            RequestState::Pending => RequestState::InProgress { 
                started_at: SystemTime::now() 
            },
            other => other, // Invalid transition, keep current state
        }
    }
    
    pub fn complete(self, result: String) -> Self {
        match self {
            RequestState::InProgress { started_at } => {
                RequestState::Completed { 
                    result, 
                    duration: started_at.elapsed().unwrap_or_default() 
                }
            },
            other => other,
        }
    }
}"""
        }
    }
    
    # Padrão: Async Patterns Idiomáticos
    ASYNC_PATTERNS = {
        "ergonomic_async": {
            "principle": "Prefer async/await over raw futures",
            "description": "Use async/await para código assíncrono legível",
            "good_example": """
use tokio::{fs, io::Result};
use serde::{Deserialize, Serialize};

#[derive(Deserialize, Serialize)]
pub struct Config {
    pub database_url: String,
    pub port: u16,
}

// Idiomático: async/await clean
pub async fn load_config(path: &str) -> Result<Config> {
    let content = fs::read_to_string(path).await?;
    let config: Config = toml::from_str(&content)
        .map_err(|e| std::io::Error::new(std::io::ErrorKind::InvalidData, e))?;
    Ok(config)
}

pub async fn start_server(config: Config) -> Result<()> {
    let listener = tokio::net::TcpListener::bind(("0.0.0.0", config.port)).await?;
    println!("Server listening on port {}", config.port);
    
    loop {
        let (stream, addr) = listener.accept().await?;
        println!("New connection from {}", addr);
        
        // Spawn concurrent handler
        tokio::spawn(async move {
            if let Err(e) = handle_connection(stream).await {
                eprintln!("Error handling connection: {}", e);
            }
        });
    }
}""",
            "anti_pattern": """
// Anti-padrão: futures complexos
use std::future::Future;
use std::pin::Pin;

pub fn load_config(path: String) -> Pin<Box<dyn Future<Output = Result<Config>> + Send>> {
    Box::pin(async move {
        let content = fs::read_to_string(path).await?;
        // código complexo com futures manuais
        Ok(config)
    })
}"""
        },
        "error_handling_async": {
            "description": "Error handling ergonômico em contexts async",
            "good_example": """
use anyhow::{Context, Result};

pub async fn process_requests(urls: Vec<String>) -> Result<Vec<Response>> {
    let mut results = Vec::new();
    
    for url in urls {
        let response = reqwest::get(&url)
            .await
            .with_context(|| format!("Failed to fetch URL: {}", url))?;
            
        let data = response
            .json::<ResponseData>()
            .await
            .with_context(|| format!("Failed to parse response from: {}", url))?;
            
        results.push(data.into());
    }
    
    Ok(results)
}

// Ou usando try_join para processamento paralelo
pub async fn process_requests_parallel(urls: Vec<String>) -> Result<Vec<Response>> {
    let futures: Vec<_> = urls.into_iter()
        .map(|url| async move {
            let response = reqwest::get(&url).await?;
            let data: ResponseData = response.json().await?;
            Ok::<Response, reqwest::Error>(data.into())
        })
        .collect();
    
    let results = futures::future::try_join_all(futures).await?;
    Ok(results)
}"""
        }
    }
    
    # Padrão: Traits e Generics Idiomáticos
    TRAITS_GENERICS_PATTERNS = {
        "flexible_apis": {
            "principle": "Use generics and traits for flexible, reusable code",
            "description": "Crie APIs que funcionam com múltiplos tipos",
            "good_example": """
use std::fmt::Display;
use serde::Serialize;

// Trait para logging flexível
pub trait Logger {
    fn log(&self, level: LogLevel, message: &str);
}

// Generic function que aceita qualquer logger
pub fn process_items<T, L>(items: Vec<T>, logger: &L) -> Vec<String> 
where
    T: Display + Serialize,
    L: Logger,
{
    let mut results = Vec::new();
    
    for (i, item) in items.iter().enumerate() {
        logger.log(LogLevel::Info, &format!("Processing item {}: {}", i, item));
        
        let serialized = serde_json::to_string(item)
            .unwrap_or_else(|e| {
                logger.log(LogLevel::Error, &format!("Serialization failed: {}", e));
                format!("Error: {}", e)
            });
            
        results.push(serialized);
    }
    
    logger.log(LogLevel::Info, &format!("Processed {} items", results.len()));
    results
}

// Implementações específicas
struct ConsoleLogger;

impl Logger for ConsoleLogger {
    fn log(&self, level: LogLevel, message: &str) {
        println!("[{}] {}", level, message);
    }
}""",
            "anti_pattern": """
// Anti-padrão: código específico demais
pub fn process_items_console(items: Vec<String>) -> Vec<String> {
    let mut results = Vec::new();
    
    for (i, item) in items.iter().enumerate() {
        println!("Processing item {}: {}", i, item); // hardcoded logging
        results.push(item.clone()); // específico para String
    }
    
    println!("Processed {} items", results.len());
    results
}

pub fn process_items_file(items: Vec<i32>) -> Vec<String> {
    // código duplicado para tipos diferentes
}"""
        },
        "trait_bounds": {
            "description": "Use trait bounds para APIs expressivas",
            "good_example": """
use std::hash::Hash;
use std::collections::HashMap;

// Bounds expressivos e úteis
pub fn count_occurrences<T>(items: impl IntoIterator<Item = T>) -> HashMap<T, usize>
where
    T: Hash + Eq,
{
    let mut counts = HashMap::new();
    for item in items {
        *counts.entry(item).or_insert(0) += 1;
    }
    counts
}

// Trait object para dynamic dispatch quando necessário
pub trait Drawable {
    fn draw(&self, canvas: &mut Canvas);
    fn area(&self) -> f64;
}

pub fn draw_shapes(shapes: &[Box<dyn Drawable>], canvas: &mut Canvas) {
    let total_area: f64 = shapes.iter().map(|s| s.area()).sum();
    println!("Drawing {} shapes with total area: {:.2}", shapes.len(), total_area);
    
    for shape in shapes {
        shape.draw(canvas);
    }
}"""
        }
    }
    
    # Padrão: Iterators Idiomáticos
    ITERATOR_PATTERNS = {
        "functional_style": {
            "principle": "Leverage iterator methods for concise code",
            "description": "Use métodos de iterator para código funcional e eficiente",
            "good_example": """
use std::collections::HashMap;

// Idiomático: iterator chains
pub fn analyze_text(text: &str) -> TextAnalysis {
    let words: Vec<&str> = text
        .split_whitespace()
        .filter(|word| !word.is_empty())
        .collect();
    
    let word_count = words.len();
    
    let word_lengths: Vec<usize> = words
        .iter()
        .map(|word| word.len())
        .collect();
    
    let average_length = word_lengths
        .iter()
        .sum::<usize>() as f64 / word_lengths.len() as f64;
    
    let word_frequency: HashMap<&str, usize> = words
        .iter()
        .fold(HashMap::new(), |mut acc, &word| {
            *acc.entry(word).or_insert(0) += 1;
            acc
        });
    
    let unique_words = word_frequency.len();
    
    TextAnalysis {
        word_count,
        unique_words,
        average_length,
        most_common: word_frequency
            .iter()
            .max_by_key(|(_, &count)| count)
            .map(|(&word, &count)| (word.to_string(), count)),
    }
}

pub fn filter_and_process<T, F, U>(items: Vec<T>, predicate: F, processor: fn(T) -> U) -> Vec<U>
where
    F: Fn(&T) -> bool,
{
    items
        .into_iter()
        .filter(predicate)
        .map(processor)
        .collect()
}""",
            "anti_pattern": """
// Anti-padrão: loops imperativos desnecessários
pub fn analyze_text(text: &str) -> TextAnalysis {
    let mut words = Vec::new();
    for word in text.split_whitespace() {
        if !word.is_empty() {
            words.push(word);
        }
    }
    
    let word_count = words.len();
    
    let mut word_lengths = Vec::new();
    for word in &words {
        word_lengths.push(word.len());
    }
    
    let mut sum = 0;
    for length in &word_lengths {
        sum += length;
    }
    let average_length = sum as f64 / word_lengths.len() as f64;
    
    // etc... código muito verboso
}"""
        }
    }
    
    # Padrão: API Design Guidelines
    API_DESIGN_PATTERNS = {
        "naming_conventions": {
            "principle": "Follow Rust naming conventions",
            "description": "Use snake_case para functions/variables, PascalCase para types",
            "good_example": """
pub mod user_management {
    use std::collections::HashMap;
    
    pub struct UserManager {
        users: HashMap<UserId, User>,
    }
    
    pub enum UserRole {
        Admin,
        Moderator,
        RegularUser,
    }
    
    impl UserManager {
        pub fn new() -> Self {
            Self {
                users: HashMap::new(),
            }
        }
        
        pub fn add_user(&mut self, user: User) -> Result<(), UserError> {
            if self.users.contains_key(&user.id) {
                return Err(UserError::UserExists);
            }
            self.users.insert(user.id, user);
            Ok(())
        }
        
        pub fn find_user_by_email(&self, email: &str) -> Option<&User> {
            self.users.values().find(|user| user.email == email)
        }
        
        pub fn get_users_by_role(&self, role: UserRole) -> Vec<&User> {
            self.users
                .values()
                .filter(|user| user.role == role)
                .collect()
        }
    }
}""",
            "anti_pattern": """
pub mod UserManagement { // PascalCase para módulo (incorreto)
    pub struct userManager { // camelCase para struct (incorreto)
        Users: HashMap<UserId, User>, // PascalCase para field (incorreto)
    }
    
    impl userManager {
        pub fn AddUser(&mut self, User: User) -> Result<(), UserError> { // PascalCase para method (incorreto)
            // implementation
        }
        
        pub fn findUserByEmail(&self, Email: &str) -> Option<&User> { // camelCase para method (incorreto)
            // implementation  
        }
    }    
}"""
        },
        "builder_pattern": {
            "description": "Use builder pattern para constructors complexos",
            "good_example": """
#[derive(Debug)]
pub struct ServerConfig {
    pub host: String,
    pub port: u16,
    pub max_connections: usize,
    pub timeout: Duration,
    pub tls_enabled: bool,
    pub log_level: LogLevel,
}

impl ServerConfig {
    pub fn builder() -> ServerConfigBuilder {
        ServerConfigBuilder::default()
    }
}

#[derive(Default)]
pub struct ServerConfigBuilder {
    host: Option<String>,
    port: Option<u16>,
    max_connections: Option<usize>,
    timeout: Option<Duration>,
    tls_enabled: bool,
    log_level: Option<LogLevel>,
}

impl ServerConfigBuilder {
    pub fn host(mut self, host: impl Into<String>) -> Self {
        self.host = Some(host.into());
        self
    }
    
    pub fn port(mut self, port: u16) -> Self {
        self.port = Some(port);
        self
    }
    
    pub fn max_connections(mut self, max: usize) -> Self {
        self.max_connections = Some(max);
        self
    }
    
    pub fn timeout(mut self, timeout: Duration) -> Self {
        self.timeout = Some(timeout);
        self
    }
    
    pub fn enable_tls(mut self) -> Self {
        self.tls_enabled = true;
        self
    }
    
    pub fn log_level(mut self, level: LogLevel) -> Self {
        self.log_level = Some(level);
        self
    }
    
    pub fn build(self) -> Result<ServerConfig, ConfigError> {
        Ok(ServerConfig {
            host: self.host.unwrap_or_else(|| "localhost".to_string()),
            port: self.port.unwrap_or(8080),
            max_connections: self.max_connections.unwrap_or(100),
            timeout: self.timeout.unwrap_or(Duration::from_secs(30)),
            tls_enabled: self.tls_enabled,
            log_level: self.log_level.unwrap_or(LogLevel::Info),
        })
    }
}

// Uso ergonômico
let config = ServerConfig::builder()
    .host("0.0.0.0")
    .port(3000)
    .max_connections(500)
    .enable_tls()
    .log_level(LogLevel::Debug)
    .build()?;"""
        }
    }
    
    # Padrão: Performance Idiomático
    PERFORMANCE_PATTERNS = {
        "zero_cost_abstractions": {
            "principle": "Aim for zero-cost abstractions",
            "description": "Use abstractions que não custam performance runtime",
            "good_example": """
// Zero-cost iterator abstraction
pub fn process_numbers(numbers: &[i32]) -> Vec<i32> {
    numbers
        .iter()
        .filter(|&&x| x > 0)
        .map(|&x| x * 2)
        .collect()
}

// Generic zero-cost abstraction
pub trait Processor<T> {
    type Output;
    fn process(&self, input: T) -> Self::Output;
}

pub fn batch_process<T, P>(items: Vec<T>, processor: P) -> Vec<P::Output>
where
    P: Processor<T>,
{
    items.into_iter().map(|item| processor.process(item)).collect()
}

// Newtype pattern for type safety sem overhead
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct UserId(u32);

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]  
pub struct OrderId(u32);

impl UserId {
    pub fn new(id: u32) -> Self {
        Self(id)
    }
    
    pub fn get(self) -> u32 {
        self.0
    }
}

// Compile-time garantees sem runtime cost
pub fn get_user_orders(user_id: UserId) -> Vec<Order> {
    // Impossível passar OrderId por engano
    query_orders_by_user(user_id.get())
}""",
            "anti_pattern": """
// Anti-padrão: abstractions custosas
pub fn process_numbers(numbers: &[i32]) -> Vec<i32> {
    let mut result = Vec::new();
    for i in 0..numbers.len() {
        if numbers[i] > 0 {
            result.push(numbers[i] * 2);
        }
    }
    result
}

// Ou usando Box desnecessariamente
pub fn process_with_callback(
    numbers: &[i32], 
    callback: Box<dyn Fn(i32) -> i32>
) -> Vec<i32> {
    numbers.iter().map(|&x| callback(x)).collect()
}"""
        },
        "memory_efficiency": {
            "description": "Otimize uso de memória com patterns idiomáticos",
            "good_example": """
use std::borrow::Cow;

// Use Cow para evitar clones desnecessários
pub fn normalize_string(input: &str) -> Cow<str> {
    if needs_normalization(input) {
        Cow::Owned(input.to_lowercase().replace(' ', "_"))
    } else {
        Cow::Borrowed(input)
    }
}

// Pre-allocate quando souber o tamanho
pub fn create_lookup_table(capacity_hint: usize) -> HashMap<String, Value> {
    HashMap::with_capacity(capacity_hint)
}

// Use referencias quando possível
pub fn analyze_logs(logs: &[LogEntry]) -> LogAnalysis {
    let error_count = logs.iter().filter(|log| log.level == LogLevel::Error).count();
    let warning_count = logs.iter().filter(|log| log.level == LogLevel::Warning).count();
    
    LogAnalysis {
        total_entries: logs.len(),
        error_count,
        warning_count,
        most_common_message: find_most_common_message(logs),
    }
}

fn find_most_common_message(logs: &[LogEntry]) -> Option<String> {
    let mut message_counts: HashMap<&str, usize> = HashMap::new();
    
    for log in logs {
        *message_counts.entry(&log.message).or_insert(0) += 1;
    }
    
    message_counts
        .into_iter()
        .max_by_key(|(_, count)| *count)
        .map(|(message, _)| message.to_string())
}"""
        }
    }

class RustIdiomaticAnalyzer:
    """Analisador de código Rust idiomático baseado em mre/idiomatic-rust"""
    
    def __init__(self):
        self.knowledge_base = RustIdiomaticKnowledgeBase()
    
    async def analyze_idiomatic_rust(self, code: str) -> IdiomaticAnalysisResult:
        """Analisa código Rust para padrões idiomáticos"""
        
        category_scores = {}
        idiomatic_patterns_found = []
        anti_patterns_found = []
        suggestions = []
        refactored_examples = {}
        compliance_with_api_guidelines = {}
        
        # Análise de immutability
        immutability_analysis = await self._analyze_immutability(code)
        category_scores["immutability"] = immutability_analysis["score"]
        idiomatic_patterns_found.extend(immutability_analysis["patterns"])
        anti_patterns_found.extend(immutability_analysis["anti_patterns"])
        suggestions.extend(immutability_analysis["suggestions"])
        
        # Análise de error handling
        error_analysis = await self._analyze_error_handling(code)
        category_scores["error_handling"] = error_analysis["score"]
        idiomatic_patterns_found.extend(error_analysis["patterns"])
        anti_patterns_found.extend(error_analysis["anti_patterns"])
        suggestions.extend(error_analysis["suggestions"])
        
        # Análise de type conversions
        conversion_analysis = await self._analyze_type_conversions(code)
        category_scores["type_conversions"] = conversion_analysis["score"]
        idiomatic_patterns_found.extend(conversion_analysis["patterns"])
        
        # Análise de enums vs booleans
        enum_analysis = await self._analyze_enums_over_bools(code)
        category_scores["enums_over_bools"] = enum_analysis["score"]
        idiomatic_patterns_found.extend(enum_analysis["patterns"])
        anti_patterns_found.extend(enum_analysis["anti_patterns"])
        
        # Análise de async patterns
        async_analysis = await self._analyze_async_patterns(code)
        category_scores["async_patterns"] = async_analysis["score"]
        idiomatic_patterns_found.extend(async_analysis["patterns"])
        
        # Análise de API design
        api_analysis = await self._analyze_api_design(code)
        category_scores["api_design"] = api_analysis["score"]
        compliance_with_api_guidelines = api_analysis["compliance"]
        
        # Calcular score geral
        idiomaticity_score = await self._calculate_idiomaticity_score(category_scores)
        
        # Gerar exemplos refatorados
        refactored_examples = await self._generate_refactored_examples(code, anti_patterns_found)
        
        return IdiomaticAnalysisResult(
            code=code,
            idiomaticity_score=idiomaticity_score,
            category_scores=category_scores,
            idiomatic_patterns_found=idiomatic_patterns_found,
            anti_patterns_found=anti_patterns_found,
            suggestions=suggestions,
            refactored_examples=refactored_examples,
            compliance_with_api_guidelines=compliance_with_api_guidelines
        )
    
    async def _analyze_immutability(self, code: str) -> Dict[str, Any]:
        """Analisa padrões de immutability"""
        score = 80  # Base score
        patterns = []
        anti_patterns = []
        suggestions = []
        
        # Padrões positivos
        if "let " in code and "let mut " not in code:
            patterns.append("✅ Variables imutáveis por padrão")
            score += 10
        
        if ".iter()" in code:
            patterns.append("✅ Uso de iterators imutáveis")
            score += 5
        
        if "const " in code or "static " in code:
            patterns.append("✅ Constantes definidas apropriadamente")
            score += 5
        
        # Anti-padrões
        excessive_mut = code.count("let mut ")
        total_let = code.count("let ")
        if total_let > 0 and (excessive_mut / total_let) > 0.5:
            anti_patterns.append("❌ Uso excessivo de mut - considere immutability")
            score -= 15
            suggestions.append("🔧 Reduza uso de 'mut' - use immutable por padrão")
        
        if ".clone()" in code and code.count(".clone()") > 3:
            anti_patterns.append("❌ Muitos clones - revise ownership patterns")
            score -= 10
            suggestions.append("⚡ Use borrowing (&) ao invés de clone quando possível")
        
        return {
            "score": max(0, min(100, score)),
            "patterns": patterns,
            "anti_patterns": anti_patterns,
            "suggestions": suggestions
        }
    
    async def _analyze_error_handling(self, code: str) -> Dict[str, Any]:
        """Analisa padrões idiomáticos de error handling"""
        score = 70
        patterns = []
        anti_patterns = []
        suggestions = []
        
        # Padrões positivos
        if "Result<" in code:
            patterns.append("✅ Uso de Result<T, E> para errors")
            score += 15
        
        if "?" in code and "Result<" in code:
            patterns.append("✅ Uso do ? operator para propagação")
            score += 10
        
        if "thiserror::" in code or "#[derive(Error)]" in code:
            patterns.append("✅ Custom error types com thiserror")
            score += 10
        
        if "anyhow::" in code or ".with_context(" in code:
            patterns.append("✅ Context preservation com anyhow")
            score += 10
        
        # Anti-padrões
        if ".unwrap()" in code:
            anti_patterns.append("❌ Uso de .unwrap() pode causar panic")
            score -= 20
            suggestions.append("🛡️ Use ? operator ou pattern matching ao invés de .unwrap()")
        
        if ".expect(" not in code and ".unwrap()" in code:
            anti_patterns.append("❌ Use .expect() com mensagem ao invés de .unwrap()")
            score -= 10
            suggestions.append("📝 Adicione mensagens descritivas com .expect()")
        
        if "panic!" in code:
            anti_patterns.append("❌ panic! deve ser usado apenas para bugs irrecuperáveis")
            score -= 15
            suggestions.append("🔄 Considere retornar Result ao invés de panic!")
        
        return {
            "score": max(0, min(100, score)),
            "patterns": patterns,
            "anti_patterns": anti_patterns,
            "suggestions": suggestions
        }
    
    async def _analyze_type_conversions(self, code: str) -> Dict[str, Any]:
        """Analisa padrões de type conversions"""
        score = 75
        patterns = []
        
        if "impl From<" in code:
            patterns.append("✅ Implementação de From trait para conversões")
            score += 10
        
        if "impl TryFrom<" in code:
            patterns.append("✅ TryFrom para conversões falíveis")
            score += 10
        
        if ".into()" in code:
            patterns.append("✅ Uso ergonômico de .into()")
            score += 5
        
        if "impl AsRef<" in code or "AsRef<str>" in code:
            patterns.append("✅ AsRef para APIs flexíveis")
            score += 10
        
        return {
            "score": max(0, min(100, score)),
            "patterns": patterns,
            "anti_patterns": [],
            "suggestions": []
        }
    
    async def _analyze_enums_over_bools(self, code: str) -> Dict[str, Any]:
        """Analisa uso de enums ao invés de booleans"""
        score = 80
        patterns = []
        anti_patterns = []
        
        if "enum " in code:
            patterns.append("✅ Uso de enums para estados expressivos")
            score += 15
        
        if "#[derive(" in code and "enum " in code:
            patterns.append("✅ Derives apropriados para enums")
            score += 5
        
        # Anti-padrão: muitos booleans como parâmetros
        bool_params = re.findall(r'fn\s+\w+\([^)]*bool[^)]*\)', code)
        if len(bool_params) > 2:
            anti_patterns.append("❌ Muitos parâmetros boolean - considere enums")
            score -= 15
        
        return {
            "score": max(0, min(100, score)),
            "patterns": patterns,
            "anti_patterns": anti_patterns,
            "suggestions": []
        }
    
    async def _analyze_async_patterns(self, code: str) -> Dict[str, Any]:
        """Analisa padrões async idiomáticos"""
        score = 75
        patterns = []
        
        if "async fn" in code and ".await" in code:
            patterns.append("✅ Uso de async/await")
            score += 10
        
        if "tokio::" in code:
            patterns.append("✅ Tokio runtime para async")
            score += 10
        
        if "try_join" in code or "join!" in code:
            patterns.append("✅ Concorrência estruturada")
            score += 10
        
        if "spawn(" in code:
            patterns.append("✅ Task spawning para concorrência")
            score += 5
        
        return {
            "score": max(0, min(100, score)),
            "patterns": patterns,
            "anti_patterns": [],
            "suggestions": []
        }
    
    async def _analyze_api_design(self, code: str) -> Dict[str, Any]:
        """Analisa conformidade com API guidelines"""
        score = 80
        compliance = {}
        
        # Naming conventions
        has_snake_case_functions = bool(re.search(r'fn\s+[a-z][a-z0-9_]*', code))
        has_pascal_case_types = bool(re.search(r'(struct|enum)\s+[A-Z][A-Za-z0-9]*', code))
        
        compliance["snake_case_functions"] = has_snake_case_functions
        compliance["pascal_case_types"] = has_pascal_case_types
        
        if has_snake_case_functions:
            score += 10
        if has_pascal_case_types:
            score += 10
        
        # Documentation
        has_doc_comments = "///" in code
        compliance["documentation"] = has_doc_comments
        if has_doc_comments:
            score += 5
        
        return {
            "score": max(0, min(100, score)),
            "compliance": compliance,
            "patterns": [],
            "anti_patterns": [],
            "suggestions": []
        }
    
    async def _calculate_idiomaticity_score(self, category_scores: Dict[str, int]) -> int:
        """Calcula score geral de idiomaticidade"""
        if not category_scores:
            return 0
        
        # Peso das categorias
        weights = {
            "immutability": 0.2,
            "error_handling": 0.25,
            "type_conversions": 0.15,
            "enums_over_bools": 0.1,
            "async_patterns": 0.15,
            "api_design": 0.15
        }
        
        weighted_sum = sum(
            category_scores.get(category, 0) * weight
            for category, weight in weights.items()
        )
        
        return int(weighted_sum)
    
    async def _generate_refactored_examples(self, code: str, anti_patterns: List[str]) -> Dict[str, str]:
        """Gera exemplos refatorados baseados nos anti-patterns encontrados"""
        examples = {}
        
        if any("unwrap" in pattern for pattern in anti_patterns):
            examples["error_handling"] = """
// Antes (anti-padrão):
let value = some_operation().unwrap();

// Depois (idiomático):
let value = some_operation()
    .expect("Operation should succeed in this context");

// Ou melhor ainda:
let value = match some_operation() {
    Ok(val) => val,
    Err(e) => {
        log::error!("Operation failed: {}", e);
        return Err(e.into());
    }
};"""
        
        if any("mut" in pattern for pattern in anti_patterns):
            examples["immutability"] = """
// Antes (anti-padrão):
let mut data = vec![1, 2, 3];
let mut result = Vec::new();
for item in data {
    result.push(item * 2);
}

// Depois (idiomático):
let data = vec![1, 2, 3];
let result: Vec<i32> = data
    .into_iter()
    .map(|item| item * 2)
    .collect();"""
        
        if any("boolean" in pattern for pattern in anti_patterns):
            examples["enums_over_bools"] = """
// Antes (anti-padrão):
fn connect(auto_retry: bool, secure: bool) -> Result<Connection> {
    // confuso: o que cada boolean significa?
}

// Depois (idiomático):
#[derive(Debug, Clone, Copy)]
enum RetryPolicy { Auto, Manual }

#[derive(Debug, Clone, Copy)]  
enum ConnectionSecurity { Secure, Insecure }

fn connect(retry: RetryPolicy, security: ConnectionSecurity) -> Result<Connection> {
    // claro e expressivo
}"""
        
        return examples

class RustProjectGenerator:
    """Gerador de projetos Rust idiomáticos"""
    
    def __init__(self):
        self.knowledge_base = RustIdiomaticKnowledgeBase()
    
    async def generate_idiomatic_project(
        self,
        project_type: str,
        features: List[str] = None,
        complexity: RustComplexity = RustComplexity.INTERMEDIATE
    ) -> Dict[str, Any]:
        """Gera projeto Rust seguindo padrões idiomáticos"""
        
        if features is None:
            features = ["error-handling", "async", "serde"]
        
        templates = {
            "library": self._generate_idiomatic_library,
            "binary": self._generate_idiomatic_binary,
            "web-api": self._generate_idiomatic_web_api,
            "cli": self._generate_idiomatic_cli
        }
        
        if project_type not in templates:
            return {"error": f"Project type '{project_type}' not supported"}
        
        return await templates[project_type](features, complexity)
    
    async def _generate_idiomatic_library(self, features: List[str], complexity: RustComplexity) -> Dict[str, Any]:
        """Gera biblioteca Rust idiomática"""
        
        cargo_toml = """[package]
name = "my-idiomatic-lib"
version = "0.1.0"
edition = "2021"
authors = ["Your Name <you@example.com>"]
description = "An idiomatic Rust library following best practices"
license = "MIT OR Apache-2.0"
repository = "https://github.com/username/my-idiomatic-lib"
keywords = ["rust", "idiomatic", "library"]
categories = ["development-tools"]
readme = "README.md"

[dependencies]
thiserror = "1.0"
serde = { version = "1.0", features = ["derive"], optional = true }
tokio = { version = "1.0", features = ["rt-multi-thread"], optional = true }

[dev-dependencies]
tokio-test = "0.4"
criterion = "0.5"

[features]
default = []
serde = ["dep:serde"]
async = ["dep:tokio"]

[[bench]]
name = "benchmarks"
harness = false

[profile.release]
lto = true
codegen-units = 1
panic = "abort"
strip = true

[profile.dev]
debug = true
"""
        
        lib_rs = """//! My Idiomatic Library
//! 
//! An idiomatic Rust library following best practices from:
//! - rust-lang/api-guidelines
//! - mre/idiomatic-rust  
//! - blessed.rs recommendations

#![warn(missing_docs)]
#![warn(clippy::all, clippy::pedantic)]

pub mod error;
pub mod config;

pub use error::{Error, Result};

/// Main library functionality following idiomatic patterns
#[derive(Debug)]
pub struct Library {
    config: config::Config,
}

impl Library {
    /// Creates a new library instance
    /// 
    /// # Errors
    /// 
    /// Returns error if configuration is invalid
    pub fn new(config: config::Config) -> Result<Self> {
        config.validate()?;
        Ok(Self { config })
    }
    
    /// Process data using idiomatic patterns
    /// 
    /// # Errors
    /// 
    /// Returns error if processing fails
    pub async fn process(&self, data: &str) -> Result<String> {
        if data.is_empty() {
            return Err(Error::InvalidInput { 
                reason: "Input cannot be empty".to_string() 
            });
        }
        
        // Idiomatic: immutable transformation
        let processed = data
            .lines()
            .filter(|line| !line.trim().is_empty())
            .map(|line| line.trim().to_uppercase())
            .collect::<Vec<_>>()
            .join("\\n");
        
        Ok(processed)
    }
    
    /// Batch process multiple items idiomatically
    pub fn batch_process<T>(&self, items: impl IntoIterator<Item = T>) -> Vec<ProcessedItem<T>>
    where
        T: Clone + std::fmt::Debug,
    {
        items
            .into_iter()
            .enumerate()
            .map(|(index, item)| ProcessedItem {
                index,
                original: item.clone(),
                processed_at: std::time::SystemTime::now(),
                item,
            })
            .collect()
    }
}

/// Represents a processed item with metadata
#[derive(Debug, Clone)]
pub struct ProcessedItem<T> {
    /// Index in the original batch
    pub index: usize,
    /// Original item reference
    pub original: T,
    /// Processing timestamp
    pub processed_at: std::time::SystemTime,
    /// The processed item
    pub item: T,
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[tokio::test]
    async fn test_library_creation() -> Result<()> {
        let config = config::Config::default();
        let lib = Library::new(config)?;
        
        let result = lib.process("hello\\nworld").await?;
        assert_eq!(result, "HELLO\\nWORLD");
        
        Ok(())
    }
    
    #[test]
    fn test_batch_processing() {
        let config = config::Config::default();
        let lib = Library::new(config).unwrap();
        
        let items = vec!["a", "b", "c"];
        let processed = lib.batch_process(items);
        
        assert_eq!(processed.len(), 3);
        assert_eq!(processed[0].index, 0);
        assert_eq!(processed[0].original, "a");
    }
}
"""
        
        error_rs = """//! Idiomatic error handling using thiserror

use thiserror::Error;

/// Main error type following idiomatic patterns
#[derive(Error, Debug)]
pub enum Error {
    /// IO operation failed
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
    
    /// Configuration is invalid
    #[error("Configuration error: {message}")]
    Config { 
        /// Specific error message
        message: String 
    },
    
    /// Input validation failed
    #[error("Invalid input: {reason}")]
    InvalidInput { 
        /// Reason for validation failure
        reason: String 
    },
    
    /// Processing operation failed
    #[error("Processing failed: {operation} - {reason}")]
    Processing { 
        /// Which operation failed
        operation: String,
        /// Why it failed
        reason: String 
    },
}

/// Result type alias following Rust conventions
pub type Result<T> = std::result::Result<T, Error>;

impl Error {
    /// Create a configuration error
    pub fn config(message: impl Into<String>) -> Self {
        Self::Config { 
            message: message.into() 
        }
    }
    
    /// Create an input validation error
    pub fn invalid_input(reason: impl Into<String>) -> Self {
        Self::InvalidInput { 
            reason: reason.into() 
        }
    }
    
    /// Create a processing error
    pub fn processing(operation: impl Into<String>, reason: impl Into<String>) -> Self {
        Self::Processing { 
            operation: operation.into(),
            reason: reason.into() 
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_error_creation() {
        let err = Error::config("Invalid port");
        assert!(matches!(err, Error::Config { .. }));
        
        let err = Error::invalid_input("Empty string");
        assert!(matches!(err, Error::InvalidInput { .. }));
    }
    
    #[test]
    fn test_error_display() {
        let err = Error::config("Invalid configuration");
        assert_eq!(err.to_string(), "Configuration error: Invalid configuration");
    }
}
"""
        
        config_rs = """//! Configuration module following idiomatic patterns

use crate::{Error, Result};
use std::path::Path;

/// Application configuration using builder pattern
#[derive(Debug, Clone, PartialEq)]
pub struct Config {
    /// Application name
    pub app_name: String,
    /// Debug mode enabled
    pub debug: bool,  
    /// Maximum items to process
    pub max_items: usize,
    /// Processing timeout in seconds
    pub timeout_secs: u64,
}

impl Default for Config {
    fn default() -> Self {
        Self {
            app_name: "my-idiomatic-lib".to_string(),
            debug: false,
            max_items: 1000,
            timeout_secs: 30,
        }
    }
}

impl Config {
    /// Create a new configuration builder
    pub fn builder() -> ConfigBuilder {
        ConfigBuilder::default()
    }
    
    /// Load configuration from file
    /// 
    /// # Errors
    /// 
    /// Returns error if file cannot be read or parsed
    pub fn from_file(path: impl AsRef<Path>) -> Result<Self> {
        let content = std::fs::read_to_string(path)
            .map_err(Error::from)?;
        
        let config: Config = toml::from_str(&content)
            .map_err(|e| Error::config(format!("Failed to parse config: {}", e)))?;
        
        config.validate()?;
        Ok(config)
    }
    
    /// Validate configuration
    /// 
    /// # Errors
    /// 
    /// Returns error if configuration is invalid
    pub fn validate(&self) -> Result<()> {
        if self.app_name.is_empty() {
            return Err(Error::config("App name cannot be empty"));
        }
        
        if self.max_items == 0 {
            return Err(Error::config("Max items must be greater than 0"));
        }
        
        if self.timeout_secs == 0 {
            return Err(Error::config("Timeout must be greater than 0"));
        }
        
        Ok(())
    }
}

/// Builder for idiomatic configuration construction
#[derive(Default)]
pub struct ConfigBuilder {
    app_name: Option<String>,
    debug: bool,
    max_items: Option<usize>,
    timeout_secs: Option<u64>,
}

impl ConfigBuilder {
    /// Set application name
    pub fn app_name(mut self, name: impl Into<String>) -> Self {
        self.app_name = Some(name.into());
        self
    }
    
    /// Enable debug mode
    pub fn debug(mut self) -> Self {
        self.debug = true;
        self
    }
    
    /// Set maximum items to process
    pub fn max_items(mut self, max: usize) -> Self {
        self.max_items = Some(max);
        self
    }
    
    /// Set timeout in seconds
    pub fn timeout_secs(mut self, secs: u64) -> Self {
        self.timeout_secs = Some(secs);
        self
    }
    
    /// Build the configuration
    /// 
    /// # Errors
    /// 
    /// Returns error if configuration is invalid
    pub fn build(self) -> Result<Config> {
        let config = Config {
            app_name: self.app_name.unwrap_or_else(|| "my-app".to_string()),
            debug: self.debug,
            max_items: self.max_items.unwrap_or(1000),
            timeout_secs: self.timeout_secs.unwrap_or(30),
        };
        
        config.validate()?;
        Ok(config)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_default_config() {
        let config = Config::default();
        assert!(config.validate().is_ok());
    }
    
    #[test]
    fn test_builder_pattern() -> Result<()> {
        let config = Config::builder()
            .app_name("test-app")
            .debug()
            .max_items(500)
            .timeout_secs(60)
            .build()?;
        
        assert_eq!(config.app_name, "test-app");
        assert!(config.debug);
        assert_eq!(config.max_items, 500);
        assert_eq!(config.timeout_secs, 60);
        
        Ok(())
    }
    
    #[test]
    fn test_validation() {
        let invalid_config = Config {
            app_name: "".to_string(),
            debug: false,
            max_items: 0,
            timeout_secs: 0,
        };
        
        assert!(invalid_config.validate().is_err());
    }
}
"""
        
        return {
            "project_type": "idiomatic_library",
            "files": {
                "Cargo.toml": cargo_toml,
                "src/lib.rs": lib_rs,
                "src/error.rs": error_rs,
                "src/config.rs": config_rs,
                "README.md": """# My Idiomatic Rust Library

An idiomatic Rust library following best practices from:
- [rust-lang/api-guidelines](https://rust-lang.github.io/api-guidelines/)
- [mre/idiomatic-rust](https://github.com/mre/idiomatic-rust)
- [blessed.rs](https://blessed.rs/) recommendations

## Features

- 🦀 **Idiomatic Rust**: Follows official API guidelines
- 🛡️ **Error Handling**: Comprehensive error types with thiserror
- ⚡ **Performance**: Zero-cost abstractions and efficient iterators
- 🔧 **Builder Pattern**: Ergonomic configuration construction
- 📚 **Documentation**: Comprehensive docs with examples
- 🧪 **Testing**: Unit tests and benchmarks included

## Usage

```rust
use my_idiomatic_lib::{Library, Config, Result};

#[tokio::main]
async fn main() -> Result<()> {
    let config = Config::builder()
        .app_name("my-app")
        .debug()
        .max_items(1000)
        .build()?;
    
    let lib = Library::new(config)?;
    let result = lib.process("hello\\nworld").await?;
    
    println!("Processed: {}", result);
    Ok(())
}
```

## Contributing

Please follow Rust idioms and API guidelines when contributing.
""",
                "LICENSE": "MIT OR Apache-2.0 license text here",
                ".gitignore": """# Generated by Cargo
/target/
Cargo.lock

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
""",
            },
            "idiomatic_patterns_used": [
                "✅ Immutability by default",
                "✅ Result-based error handling with thiserror", 
                "✅ Builder pattern for complex construction",
                "✅ Iterator chains for functional style",
                "✅ Comprehensive documentation with examples",
                "✅ From/Into traits for type conversions",
                "✅ API guidelines compliance (naming, structure)",
                "✅ Zero-cost abstractions with generics"
            ],
            "structure": """
my-idiomatic-lib/
├── Cargo.toml          # Package configuration with idiomatic metadata
├── src/
│   ├── lib.rs          # Library root with comprehensive docs
│   ├── error.rs        # Idiomatic error handling with thiserror
│   └── config.rs       # Builder pattern configuration
├── tests/              # Integration tests
├── benches/            # Performance benchmarks
├── examples/           # Usage examples
├── README.md           # Comprehensive documentation
└── LICENSE             # MIT OR Apache-2.0 dual license
""",
            "next_steps": [
                "cargo build --release # Build with optimizations",
                "cargo test # Run all tests", 
                "cargo clippy # Run linter for idiomatic suggestions",
                "cargo doc --open # Generate and view documentation",
                "cargo bench # Run performance benchmarks"
            ]
        }

# ================================
# FERRAMENTAS MCP IDIOMÁTICAS
# ================================

@mcp.tool()
async def analyze_idiomatic_rust(code: str) -> Dict[str, Any]:
    """
    Analisa código Rust para padrões idiomáticos baseado em mre/idiomatic-rust.
    
    Args:
        code: Código Rust para análise
        
    Returns:
        Análise completa com score de idiomaticidade e sugestões
    """
    try:
        analyzer = RustIdiomaticAnalyzer()
        analysis = await analyzer.analyze_idiomatic_rust(code)
        
        logger.info(f"Analyzed Rust code for idiomatic patterns - score: {analysis.idiomaticity_score}")
        
        return {
            "idiomaticity_score": analysis.idiomaticity_score,
            "category_scores": analysis.category_scores,
            "idiomatic_patterns_found": analysis.idiomatic_patterns_found,
            "anti_patterns_found": analysis.anti_patterns_found,
            "suggestions": analysis.suggestions,
            "refactored_examples": analysis.refactored_examples,
            "compliance_with_api_guidelines": analysis.compliance_with_api_guidelines,
            "analysis_categories": [
                "immutability", "error_handling", "type_conversions",
                "enums_over_bools", "async_patterns", "api_design"
            ]
        }
        
    except Exception as e:
        logger.error(f"Error analyzing idiomatic Rust: {str(e)}")
        raise

@mcp.tool()
async def generate_idiomatic_project(
    project_type: str,
    features: Optional[List[str]] = None,
    complexity: str = "intermediate"
) -> Dict[str, Any]:
    """
    Gera projeto Rust idiomático seguindo mre/idiomatic-rust patterns.
    
    Args:
        project_type: Tipo do projeto (library, binary, web-api, cli)
        features: Lista de features desejadas
        complexity: Nível de complexidade (beginner, intermediate, advanced)
        
    Returns:
        Estrutura completa do projeto com código idiomático
    """
    try:
        generator = RustProjectGenerator()
        
        # Converter string para enum
        complexity_enum = RustComplexity.INTERMEDIATE
        if complexity == "beginner":
            complexity_enum = RustComplexity.BEGINNER
        elif complexity == "advanced":
            complexity_enum = RustComplexity.ADVANCED
        elif complexity == "expert":
            complexity_enum = RustComplexity.EXPERT
        
        result = await generator.generate_idiomatic_project(
            project_type=project_type,
            features=features,
            complexity=complexity_enum
        )
        
        logger.info(f"Generated idiomatic Rust project: {project_type}")
        
        return result
        
    except Exception as e:
        logger.error(f"Error generating idiomatic project: {str(e)}")
        raise

@mcp.tool()
async def get_idiomatic_patterns(category: str = "all") -> Dict[str, Any]:
    """
    Retorna padrões idiomáticos Rust por categoria baseado em mre/idiomatic-rust.
    
    Args:
        category: Categoria específica ou "all" para todas
        
    Returns:
        Padrões idiomáticos com exemplos práticos
    """
    try:
        knowledge_base = RustIdiomaticKnowledgeBase()
        
        categories = {
            "immutability": knowledge_base.IMMUTABILITY_PATTERNS,
            "error_handling": knowledge_base.ERROR_HANDLING_PATTERNS,
            "type_conversions": knowledge_base.TYPE_CONVERSION_PATTERNS,
            "enums_over_bools": knowledge_base.ENUMS_OVER_BOOLS_PATTERNS,
            "async_patterns": knowledge_base.ASYNC_PATTERNS,
            "traits_generics": knowledge_base.TRAITS_GENERICS_PATTERNS,
            "iterators": knowledge_base.ITERATOR_PATTERNS,
            "api_design": knowledge_base.API_DESIGN_PATTERNS,
            "performance": knowledge_base.PERFORMANCE_PATTERNS
        }
        
        if category == "all":
            return {
                "source": "mre/idiomatic-rust + rust-lang/api-guidelines",
                "categories": categories,
                "principles": [
                    "Aim for immutability by default",
                    "Return Result instead of panicking",
                    "Use From/Into for convenient conversions", 
                    "Prefer enums over boolean flags",
                    "Leverage iterator methods for concise code",
                    "Use generics and traits for flexible APIs",
                    "Follow Rust naming conventions",
                    "Aim for zero-cost abstractions"
                ]
            }
        
        if category not in categories:
            return {"error": f"Category '{category}' not found. Available: {list(categories.keys())}"}
        
        return {
            "category": category,
            "patterns": categories[category],
            "source": "mre/idiomatic-rust repository"
        }
        
    except Exception as e:
        logger.error(f"Error getting idiomatic patterns: {str(e)}")
        raise

@mcp.tool()
async def refactor_to_idiomatic(
    code: str,
    focus_areas: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Refatora código Rust para seguir padrões idiomáticos.
    
    Args:
        code: Código Rust original
        focus_areas: Áreas específicas para refatoração
        
    Returns:
        Código refatorado com explicações das mudanças
    """
    try:
        if focus_areas is None:
            focus_areas = ["immutability", "error_handling", "iterators", "api_design"]
        
        # Análise inicial
        analyzer = RustIdiomaticAnalyzer()
        analysis = await analyzer.analyze_idiomatic_rust(code)
        
        refactored_code = code
        changes_made = []
        
        # Refatorações baseadas no foco
        if "immutability" in focus_areas:
            # Remover mut desnecessários
            if "let mut " in refactored_code:
                # Simplificação: marcar para revisão
                refactored_code = re.sub(
                    r'let mut (\w+) = ([^;]+);(\s*//.*)?',
                    r'let \1 = \2; // TODO: Review if mut is needed\3',
                    refactored_code
                )
                changes_made.append("🔧 Marked unnecessary mut for review")
        
        if "error_handling" in focus_areas:
            # Substituir unwrap por expect ou ?
            refactored_code = re.sub(
                r'\.unwrap\(\)',
                '.expect("TODO: Add meaningful error message")',
                refactored_code
            )
            if ".expect(" in refactored_code:
                changes_made.append("🛡️ Replaced .unwrap() with .expect() for better error messages")
        
        if "iterators" in focus_areas:
            # Sugerir uso de iterators (marcação)
            if "for " in refactored_code and ".collect()" not in refactored_code:
                refactored_code += "\n// TODO: Consider using iterator methods (.map, .filter, .collect) for functional style"
                changes_made.append("⚡ Suggested iterator methods for functional style")
        
        return {
            "original_code": code,
            "refactored_code": refactored_code,
            "changes_made": changes_made,
            "original_idiomaticity_score": analysis.idiomaticity_score,
            "idiomatic_principles_applied": [
                "Immutability by default",
                "Ergonomic error handling", 
                "Functional programming with iterators",
                "API design guidelines compliance"
            ],
            "suggestions": analysis.suggestions
        }
        
    except Exception as e:
        logger.error(f"Error refactoring to idiomatic Rust: {str(e)}")
        raise

@mcp.tool()
async def get_rust_api_guidelines() -> Dict[str, Any]:
    """
    Retorna diretrizes de API do Rust oficial (rust-lang/api-guidelines).
    
    Returns:
        Diretrizes organizadas por categoria
    """
    try:
        return {
            "source": "https://rust-lang.github.io/api-guidelines/",
            "categories": {
                "naming": {
                    "description": "Convenções de nomenclatura",
                    "guidelines": [
                        "Use snake_case for functions and variables",
                        "Use PascalCase for types and traits", 
                        "Use SCREAMING_SNAKE_CASE for constants",
                        "Use descriptive names that explain purpose"
                    ]
                },
                "interoperability": {
                    "description": "Interoperabilidade entre crates",
                    "guidelines": [
                        "Use standard traits when possible",
                        "Implement Display and Debug for public types",
                        "Use From/Into for type conversions",
                        "Support serde when appropriate"
                    ]
                },
                "type_safety": {
                    "description": "Segurança de tipos",
                    "guidelines": [
                        "Use newtype pattern for type safety",
                        "Make impossible states unrepresentable",
                        "Use enums instead of boolean flags",
                        "Leverage the type system for invariants"
                    ]
                },
                "error_handling": {
                    "description": "Tratamento de erros",
                    "guidelines": [
                        "Return Result for recoverable errors",
                        "Use thiserror for error types",
                        "Provide meaningful error messages",
                        "Support error chaining with From"
                    ]
                },
                "documentation": {
                    "description": "Documentação",
                    "guidelines": [
                        "Document all public APIs",
                        "Include examples in documentation",
                        "Use doc tests to verify examples",
                        "Explain errors and edge cases"
                    ]
                },
                "flexibility": {
                    "description": "Flexibilidade de API",
                    "guidelines": [
                        "Accept borrowed types in parameters",
                        "Use generics for reusable code",
                        "Provide both owned and borrowed variants",
                        "Use trait objects for dynamic dispatch"
                    ]
                }
            },
            "key_principles": [
                "APIs should be easy to use correctly",
                "APIs should be hard to use incorrectly", 
                "APIs should be consistent with std library",
                "APIs should compose well with other APIs"
            ]
        }
        
    except Exception as e:
        logger.error(f"Error getting API guidelines: {str(e)}")
        raise

# ================================  
# RECURSOS ADICIONAIS
# ================================

@mcp.resource(uri="guide://rust-idiomatic-development")
async def get_idiomatic_development_guide() -> str:
    """Guia completo de desenvolvimento Rust idiomático"""
    return json.dumps({
        "title": "Guia de Desenvolvimento Rust Idiomático 2025",
        "based_on": [
            "mre/idiomatic-rust repository",
            "rust-lang/api-guidelines",
            "blessed.rs recommendations"
        ],
        "sections": {
            "immutability": "Immutability by default - use mut apenas quando necessário",
            "error_handling": "Result-based error handling com thiserror/anyhow",
            "type_conversions": "From/Into traits para conversões ergonômicas",
            "enums_over_bools": "Enums expressivos ao invés de boolean flags",
            "async_patterns": "Async/await idiomático com Tokio",
            "traits_generics": "Traits e generics para APIs flexíveis",
            "iterators": "Iterator methods para estilo funcional",
            "api_design": "API design seguindo rust-lang guidelines",
            "performance": "Zero-cost abstractions e otimizações"
        },
        "key_resources": {
            "idiomatic_rust": "https://github.com/mre/idiomatic-rust",
            "api_guidelines": "https://rust-lang.github.io/api-guidelines/",
            "blessed_rs": "https://blessed.rs/",
            "cheats_rs": "https://cheats.rs/",
            "rust_by_example": "https://doc.rust-lang.org/rust-by-example/"
        },
        "features": {
            "code_analysis": "Análise de idiomaticidade com scoring detalhado",
            "project_generation": "Geração de projetos seguindo best practices",
            "refactoring": "Refatoração automática para padrões idiomáticos", 
            "pattern_library": "Biblioteca completa de padrões idiomáticos",
            "api_compliance": "Verificação de conformidade com API guidelines"
        }
    }, indent=2)

# ================================
# INICIALIZAÇÃO DO SERVIDOR  
# ================================

if __name__ == "__main__":
    logger.info("Starting Rust Idiomatic MCP Server")
    logger.info("Based on: mre/idiomatic-rust + rust-lang/api-guidelines")
    logger.info("Features: Idiomatic Analysis | Project Generation | Refactoring | API Guidelines")
    
    # Executar o servidor MCP
    mcp.run()