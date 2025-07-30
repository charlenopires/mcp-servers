# Rust Idiomatic Server

The Rust Idiomatic Server provides comprehensive analysis and guidance for writing idiomatic Rust code based on the `mre/idiomatic-rust` repository and official Rust API guidelines. It helps developers write more maintainable, performant, and community-accepted Rust code.

## Overview

This server specializes in Rust code analysis and improvement, offering tools to evaluate code against idiomatic patterns, generate well-structured Rust projects, and provide refactoring suggestions that align with the Rust community's best practices.

**Port**: 3008  
**Protocol**: stdio  
**Module**: `servers.rust_server`

## Features

### 🦀 Idiomatic Analysis
- **Pattern Recognition**: Identifies idiomatic and non-idiomatic Rust patterns
- **API Guidelines Compliance**: Validation against rust-lang/api-guidelines
- **Performance Analysis**: Memory safety and performance optimization suggestions
- **Community Standards**: Alignment with established Rust conventions

### 🏗️ Project Generation
- **Template Creation**: Complete Rust project scaffolding
- **Cargo Configuration**: Optimized Cargo.toml setup
- **Best Practices**: Integrated testing, documentation, and CI/CD
- **Multiple Project Types**: Library, binary, web API, CLI applications

### 🔧 Code Refactoring
- **Pattern Improvement**: Automatic application of idiomatic patterns
- **Performance Optimization**: Memory and CPU efficiency improvements
- **Safety Enhancement**: Ownership and borrowing optimization
- **Style Consistency**: Rust formatting and naming conventions

## Available Tools

### `analyze_idiomatic_rust(code: str)`
Analyzes Rust code for idiomatic patterns and provides comprehensive feedback.

**Parameters:**
- `code` (string): Rust code to analyze

**Returns:**
- `idiomaticity_score` (number): Overall score (0-100)
- `pattern_analysis` (object): Breakdown by pattern categories
- `violations` (array): Non-idiomatic patterns found
- `recommendations` (array): Specific improvement suggestions
- `examples` (object): Code examples showing proper patterns

**Analysis Categories:**
- **Ownership & Borrowing**: Proper use of ownership system
- **Error Handling**: Result/Option usage patterns
- **Type Design**: Struct, enum, and trait design
- **Iterator Usage**: Functional programming patterns
- **Memory Safety**: Safe memory management practices

### `generate_idiomatic_project(project_type: str, options?)`
Generates complete Rust projects following idiomatic patterns.

**Parameters:**
- `project_type` (string): Type of project to generate
- `features` (array, optional): Additional features to include
- `complexity` (string): Project complexity level

**Project Types:**
- `"library"` - Rust library crate
- `"binary"` - Executable application
- `"web-api"` - Web API server (using Axum/Warp)
- `"cli"` - Command-line interface tool

**Complexity Levels:**
- `"beginner"` - Simple structure with essential patterns
- `"intermediate"` - Balanced complexity with common patterns
- `"advanced"` - Complex architecture with advanced patterns

**Returns:**
- `project_structure` (object): Complete file structure
- `cargo_toml` (string): Optimized Cargo.toml configuration
- `source_files` (object): All source code files
- `documentation` (string): README and API documentation
- `tests` (object): Comprehensive test suite

### `get_idiomatic_patterns(category: str = "all")`
Returns idiomatic Rust patterns organized by category.

**Parameters:**
- `category` (string): Specific pattern category or "all"

**Categories:**
- `"ownership"` - Ownership and borrowing patterns
- `"error_handling"` - Error handling best practices
- `"iterators"` - Iterator and functional patterns
- `"types"` - Type design and implementation
- `"concurrency"` - Safe concurrency patterns
- `"performance"` - Performance optimization patterns

**Returns:**
- Comprehensive pattern library with examples and explanations
- Good vs. bad pattern comparisons
- Performance implications and trade-offs

### `refactor_to_idiomatic(code: str, focus_areas?: string[])`
Refactors Rust code to follow idiomatic patterns.

**Parameters:**
- `code` (string): Original Rust code
- `focus_areas` (array, optional): Specific areas to focus on

**Focus Areas:**
- `"error_handling"` - Improve Result/Option usage
- `"iterators"` - Replace loops with iterator chains
- `"ownership"` - Optimize borrowing and ownership
- `"performance"` - Memory and CPU optimizations
- `"safety"` - Enhance memory safety

**Returns:**
- `original_code` (string): Original code
- `refactored_code` (string): Improved version
- `changes_made` (array): List of applied refactorings
- `explanations` (array): Detailed explanations for each change
- `performance_impact` (string): Expected performance improvement

### `get_rust_api_guidelines()`
Returns the official Rust API design guidelines.

**Returns:**
- **Naming**: Conventions for types, functions, modules
- **Interoperability**: C FFI and cross-language patterns
- **Macros**: Macro design and implementation guidelines
- **Documentation**: Rustdoc best practices
- **Versioning**: Semantic versioning for Rust crates

## Idiomatic Patterns

### Ownership & Borrowing
```rust
// Non-idiomatic: Unnecessary cloning
fn process_data(data: Vec<String>) -> Vec<String> {
    data.clone().into_iter().map(|s| s.to_uppercase()).collect()
}

// Idiomatic: Proper borrowing
fn process_data(data: &[String]) -> Vec<String> {
    data.iter().map(|s| s.to_uppercase()).collect()
}
```

### Error Handling
```rust
// Non-idiomatic: Panic on error
fn read_config() -> Config {
    fs::read_to_string("config.toml").unwrap().parse().unwrap()
}

// Idiomatic: Proper error propagation
fn read_config() -> Result<Config, Box<dyn std::error::Error>> {
    let content = fs::read_to_string("config.toml")?;
    Ok(content.parse()?)
}
```

### Iterator Patterns
```rust
// Non-idiomatic: Manual loops
let mut result = Vec::new();
for item in items {
    if item.is_valid() {
        result.push(item.process());
    }
}

// Idiomatic: Iterator chains
let result: Vec<_> = items
    .into_iter()
    .filter(|item| item.is_valid())
    .map(|item| item.process())
    .collect();
```

### Type Design
```rust
// Idiomatic: Strong typing with newtypes
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct UserId(pub u64);

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct UserName(pub String);

impl std::fmt::Display for UserName {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.0)
    }
}
```

## Performance Patterns

### Memory Efficiency
- **Zero-Cost Abstractions**: Leverage Rust's zero-cost abstractions
- **Stack Allocation**: Prefer stack over heap when possible
- **Lazy Evaluation**: Use iterators for deferred computation
- **Memory Pools**: Custom allocators for specific use cases

### CPU Optimization
- **SIMD**: Utilize SIMD instructions for parallel operations
- **Branch Prediction**: Write branch-predictor-friendly code
- **Cache Locality**: Structure data for better cache usage
- **Inline Functions**: Strategic use of `#[inline]` attribute

### Concurrency
- **Fearless Concurrency**: Safe concurrent programming patterns
- **Message Passing**: Channel-based communication
- **Shared State**: Mutex and RwLock best practices
- **Async/Await**: Modern asynchronous programming

## Project Templates

### Library Template
```toml
[package]
name = "my-library"
version = "0.1.0"
edition = "2021"
authors = ["Your Name <email@example.com>"]
license = "MIT OR Apache-2.0"
description = "A brief description"
repository = "https://github.com/user/repo"
keywords = ["keyword1", "keyword2"]
categories = ["category"]

[dependencies]
thiserror = "1.0"
serde = { version = "1.0", features = ["derive"], optional = true }

[dev-dependencies]
criterion = "0.5"

[features]
default = []
serde = ["dep:serde"]

[[bench]]
name = "benchmarks"
harness = false
```

### Binary Template
```toml
[package]
name = "my-cli"
version = "0.1.0"
edition = "2021"

[dependencies]
clap = { version = "4.0", features = ["derive"] }
anyhow = "1.0"
tokio = { version = "1.0", features = ["full"] }

[[bin]]
name = "my-cli"
path = "src/main.rs"
```

## Best Practices

### Code Organization
- **Module Structure**: Logical module hierarchy
- **Visibility**: Appropriate use of `pub` and `pub(crate)`
- **Re-exports**: Clean public API surface
- **Documentation**: Comprehensive rustdoc comments

### Testing
- **Unit Tests**: Test individual functions and methods
- **Integration Tests**: Test public API contracts
- **Property Tests**: Use proptest for property-based testing
- **Benchmarks**: Performance regression testing

### Documentation
- **API Documentation**: Complete rustdoc coverage
- **Examples**: Runnable code examples
- **README**: Clear project description and usage
- **CHANGELOG**: Semantic versioning changelog

## Usage Examples

### Code Analysis
```python
analysis = analyze_idiomatic_rust("""
fn process_items(items: Vec<String>) -> Vec<String> {
    let mut result = Vec::new();
    for item in items {
        result.push(item.to_uppercase());
    }
    result
}
""")
# Returns: score: 60, suggestions: ["Use iterator patterns", "Consider borrowing"]
```

### Project Generation
```python
project = generate_idiomatic_project(
    "web-api",
    features=["database", "authentication"],
    complexity="intermediate"
)
# Returns complete Axum web API project structure
```

### Code Refactoring
```python
refactored = refactor_to_idiomatic(code, ["iterators", "error_handling"])
# Returns improved code with iterator chains and proper error handling
```

## Configuration

Environment variables:
- `MCP_SERVER_PORT`: Server port (default: 3008)
- `MCP_SERVER_PROTOCOL`: Communication protocol (default: stdio)
- `RUST_VERSION`: Target Rust version (default: latest stable)

## Dependencies

- **Rust Knowledge Base**: Built-in idiomatic patterns library
- **API Guidelines**: Official Rust API design guidelines
- **Pattern Examples**: Comprehensive example collection
- **FastMCP**: 2.4.0+

---

*This server is part of the MCP Servers Collection developed by Charleno Pires*