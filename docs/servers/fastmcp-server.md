# FastMCP Server

The FastMCP Server is a meta-server designed to analyze, improve, and generate MCP servers using the FastMCP 2.0 framework. It provides advanced prompt analysis, server template generation, and comprehensive validation tools for creating high-quality MCP servers.

## Overview

This server specializes in MCP server development workflows, offering intelligent analysis of server creation prompts, automated template generation, and validation against FastMCP best practices. It's the perfect companion for developers building MCP servers with the FastMCP framework.

**Port**: 3003  
**Protocol**: stdio  
**Module**: `servers.fastmcp_server`

## Features

### 🔍 Advanced Prompt Analysis
- **Quality Scoring**: Comprehensive 0-100 scoring system
- **Best Practices Validation**: Alignment with FastMCP 2.0 standards
- **Structure Analysis**: Requirements clarity and completeness evaluation
- **Context Assessment**: Technical and functional requirement coverage

### 🚀 Server Generation
- **Template-Based Generation**: Pre-built templates for different server types
- **Custom Configuration**: Tailored generation based on specific requirements
- **Best Practices Integration**: Automatic application of FastMCP patterns
- **Production-Ready Code**: Complete server implementations

### 📋 Requirements Validation
- **Checklist Validation**: Comprehensive requirement coverage analysis
- **Missing Elements Detection**: Identification of critical gaps
- **Critical Issue Flagging**: Security and performance concern identification
- **Improvement Recommendations**: Actionable enhancement suggestions

## Available Tools

### `analyze_mcp_prompt(prompt: str)`
Analyzes an MCP server creation prompt and provides detailed feedback.

**Parameters:**
- `prompt` (string): The prompt text to analyze for MCP server creation

**Returns:**
- `score` (number): Overall quality score (0-100)
- `strengths` (array): Identified strong points
- `weaknesses` (array): Areas needing improvement
- `recommendations` (array): Specific improvement suggestions
- `categories` (object): Breakdown by analysis categories

**Analysis Categories:**
- **Structure & Clarity** (25 points): Length, objective definition, organization
- **FastMCP Adherence** (25 points): Framework-specific requirements
- **Technical Requirements** (25 points): Error handling, validation, security
- **Production Readiness** (25 points): Testing, documentation, deployment

**Example:**
```python
analysis = analyze_mcp_prompt("""
Create an MCP server for file management with FastMCP.
Include tools for reading, writing, and deleting files.
Add proper error handling and input validation.
Include comprehensive testing and documentation.
""")
# Returns: score: 85, strengths: ["Clear objective", "Security considerations"]
```

### `suggest_mcp_prompt_improvements(original_prompt: str, focus_area?: str)`
Suggests specific improvements for an MCP server creation prompt.

**Parameters:**
- `original_prompt` (string): The original prompt to improve
- `focus_area` (string, optional): Specific area to focus on

**Focus Areas:**
- `"technical"` - Technical implementation details
- `"documentation"` - Documentation and examples
- `"security"` - Security and validation aspects
- `"testing"` - Testing strategies and approaches
- `"deployment"` - Production deployment considerations

**Returns:**
- `original_prompt` (string): The original prompt
- `improved_prompt` (string): Enhanced version with structured sections
- `improvements_made` (array): List of applied improvements
- `explanation` (string): Description of changes made
- `score_improvement` (string): Expected quality improvement

**Example:**
```python
improvements = suggest_mcp_prompt_improvements(
    "Create a database MCP server",
    focus_area="technical"
)
# Returns structured prompt with technical requirements, error handling, etc.
```

### `validate_mcp_requirements(requirements: str)`
Validates MCP server requirements against FastMCP best practices checklist.

**Parameters:**
- `requirements` (string): The requirements specification to validate

**Returns:**
- `overall_score` (number): Overall validation score (0-100)
- `validation_passed` (boolean): Whether validation passed (≥70 score)
- `requirements_coverage` (object): Coverage analysis by category
- `missing_requirements` (array): Critical missing elements
- `critical_issues` (array): Issues that must be addressed
- `warnings` (array): Recommendations for improvement
- `next_steps` (array): Actionable next steps

**Validation Categories:**
- **Purpose & Scope**: Clear objectives and boundaries
- **Tool Design**: Well-defined tools with proper signatures
- **Error Handling**: Comprehensive error management
- **Security**: Input validation and sanitization
- **Documentation**: Clear usage examples and API docs
- **Testing**: Testing strategy and implementation
- **Performance**: Scalability and optimization considerations

**Example:**
```python
validation = validate_mcp_requirements("""
Purpose: File management server for development workflows
Tools: read_file, write_file, delete_file, list_directory
Security: Input path validation, access control
Testing: Unit tests for all tools, integration tests
""")
# Returns: validation_passed: true, score: 78
```

### `generate_mcp_server_template(server_type: str, name: str, description: str)`
Generates an optimized prompt template for creating a specific MCP server.

**Parameters:**
- `server_type` (string): Type of server to generate
- `name` (string): Name of the server
- `description` (string): Brief description of server purpose

**Server Types:**
- `"basic"` - Simple server with basic tools and resources
- `"api_integration"` - Server that integrates with external APIs
- `"data_processing"` - Server focused on data manipulation and analysis
- `"production_ready"` - Enterprise-ready server with all best practices

**Returns:**
- `server_type` (string): Type of server generated
- `template_prompt` (string): Complete structured prompt template
- `features_included` (array): List of included features
- `customization_points` (array): Areas for customization
- `implementation_notes` (array): Development guidance

**Example:**
```python
template = generate_mcp_server_template(
    "api_integration",
    "GitHub Integration Server", 
    "Server for GitHub API operations"
)
# Returns complete template with API patterns, error handling, rate limiting
```

## Template Types

### Basic Server Template
- **Core Tools**: 3-5 essential tools
- **Error Handling**: Basic validation and error responses
- **Documentation**: Usage examples for each tool
- **Testing**: Unit tests for core functionality

### API Integration Template
- **HTTP Client**: Configured API client with authentication
- **Rate Limiting**: Built-in request throttling
- **Response Caching**: Intelligent caching strategies
- **Error Recovery**: Retry logic and fallback mechanisms
- **Webhook Support**: Optional webhook endpoint handling

### Data Processing Template
- **Input Validation**: Schema-based data validation
- **Processing Pipeline**: Configurable data transformation steps
- **Batch Operations**: Support for bulk data processing
- **Progress Tracking**: Long-running operation monitoring
- **Export Capabilities**: Multiple output format support

### Production Ready Template
- **Complete Error Handling**: Comprehensive error management
- **Security Framework**: Authentication, authorization, input sanitization
- **Monitoring**: Logging, metrics, health checks
- **Documentation**: API docs, usage guides, deployment instructions
- **Testing Suite**: Unit, integration, and performance tests
- **Deployment**: Docker, CI/CD pipeline configurations

## Best Practices Validation

The server validates against these FastMCP 2.0 best practices:

### 🎯 Purpose & Design
- Clear, specific server purpose
- Well-defined scope and boundaries
- Appropriate tool granularity
- Consistent naming conventions

### 🔧 Technical Implementation
- Proper use of FastMCP decorators (`@mcp.tool()`, `@mcp.resource()`)
- Type hints for all parameters and returns
- Pydantic models for complex data structures
- Async/await patterns for I/O operations

### 🛡️ Security & Validation
- Input parameter validation
- Path traversal protection
- Rate limiting considerations
- Error message sanitization

### 📚 Documentation & Testing
- Comprehensive docstrings
- Usage examples for all tools
- Unit test coverage
- Integration test scenarios

### 🚀 Production Readiness
- Error handling and recovery
- Logging and monitoring
- Performance considerations
- Deployment documentation

## Usage Examples

### Basic Analysis Workflow
```bash
# Start the server
python main.py fastmcp

# Analyze a prompt
analyze_mcp_prompt("Create a file management server")
# Returns detailed analysis with suggestions
```

### Improvement Workflow
```python
# Get improvement suggestions
improvements = suggest_mcp_prompt_improvements("""
Create a weather server that gets weather data.
""")

# Apply suggestions and re-analyze
improved_prompt = improvements["improved_prompt"]
new_analysis = analyze_mcp_prompt(improved_prompt)
print(f"Score improved from 30 to {new_analysis['score']}")
```

### Template Generation Workflow
```python
# Generate a production-ready template
template = generate_mcp_server_template(
    server_type="production_ready",
    name="E-commerce Analytics Server",
    description="Server for e-commerce data analysis and reporting"
)

# Use the generated template for development
print(template["template_prompt"])
# Contains complete structured requirements with all best practices
```

### Validation Workflow
```python
# Validate requirements before implementation
requirements = """
Server: Social Media Integration
Purpose: Connect with Twitter, LinkedIn, Facebook APIs
Tools: post_tweet, get_profile, fetch_posts, schedule_content
Security: OAuth 2.0, rate limiting, content validation
Testing: Mock API responses, integration tests
Documentation: API reference, usage examples
"""

validation = validate_mcp_requirements(requirements)
if not validation["validation_passed"]:
    print("Issues to resolve:")
    for issue in validation["critical_issues"]:
        print(f"• {issue}")
```

## Quality Scoring System

### Score Ranges
- **90-100**: Excellent - Production ready with comprehensive requirements
- **80-89**: Good - Well-structured with minor gaps
- **70-79**: Acceptable - Solid foundation, some improvements needed
- **60-69**: Needs Work - Major gaps in requirements or structure
- **Below 60**: Poor - Significant rework required

### Scoring Breakdown
- **Structure & Clarity** (25%): Organization, length, objective clarity
- **FastMCP Adherence** (25%): Framework-specific patterns and practices
- **Technical Requirements** (25%): Error handling, validation, security
- **Production Readiness** (25%): Testing, documentation, deployment

## Configuration

Environment variables:
- `MCP_SERVER_PORT`: Server port (default: 3003)
- `MCP_SERVER_PROTOCOL`: Communication protocol (default: stdio)
- `FASTMCP_LOG_LEVEL`: Logging level (INFO, DEBUG, WARNING)

## Dependencies

- **FastMCP**: 2.4.0+
- **Pydantic**: For data validation and serialization
- **Python**: 3.12+
- **Typing Extensions**: For advanced type hints

## Performance

- **Analysis Speed**: < 200ms for comprehensive prompt analysis
- **Template Generation**: < 500ms for production-ready templates
- **Memory Usage**: Minimal footprint with efficient caching
- **Concurrent Operations**: Supports multiple simultaneous analyses

---

*This server is part of the MCP Servers Collection developed by Charleno Pires*