"""
Unified MCP Server for FastMCP Prompt Optimization

This server combines prompt analysis functionalities, template generation
and best practices application for MCP server development with FastMCP.
"""

import logging
import json
import re
import asyncio
from datetime import datetime
from typing import Dict, List, Optional, Any, Union
from pydantic import BaseModel, Field
from fastmcp import FastMCP, Context

# FastMCP server initialization
mcp = FastMCP(
    name="FastMCP Server - Advanced MCP Development Platform",
    instructions="""Complete FastMCP server for MCP server development, analysis and optimization.

FastMCP is a comprehensive platform that offers:
- Rapid MCP server development with Pythonic interface
- Decorators that return original functions for easy testing
- Context injection in tools, resources, and prompts
- Server composition with mount() and import_server()
- Lifespan management with async context managers
- FileSystemProvider for automatic component discovery
- Multiple transport options (stdio, http, sse)
- Proxy servers with FastMCP.as_proxy()
- Automatic server generation from OpenAPI/FastAPI
- Component-level authorization with JWT/OAuth 2.1
- Testing tools and integration with major AI platforms

Use the tools to make the most of the FastMCP ecosystem.""",
    version="3.0.0"
)

# Structured logging configuration


class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_obj = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
        }
        if hasattr(record, 'correlation_id'):
            log_obj['correlation_id'] = record.correlation_id
        return json.dumps(log_obj)


logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Pydantic models for data structuring


class PromptAnalysis(BaseModel):
    """Result of MCP prompt analysis (international model)"""
    score: float = Field(
        description="Score from 0-100 indicating prompt quality")
    strengths: List[str] = Field(
        description="Positive aspects identified")
    weaknesses: List[str] = Field(description="Areas that need improvements")
    recommendations: List[str] = Field(
        description="Specific improvement recommendations")
    has_technical_requirements: bool = Field(
        description="Whether technical requirements are specified")
    has_business_context: bool = Field(
        description="Whether business context is included")
    has_security_considerations: bool = Field(
        description="Whether security considerations are mentioned")


# Removed duplicate Portuguese model - using PromptAnalysis instead


class MCPRequirement(BaseModel):
    """Requirements for an MCP server"""
    tools: List[str] = Field(
        default_factory=list, description="List of required tools")
    resources: List[str] = Field(
        default_factory=list, description="List of required resources")
    transports: List[str] = Field(
        default_factory=list, description="Transport protocols")
    authentication: bool = Field(
        default=False, description="Whether authentication is required")
    scalability: bool = Field(
        default=False, description="Whether scalability is needed")
    external_integration: List[str] = Field(
        default_factory=list, description="Required external APIs")


# FastMCP 3.0 Context and Best Practices
FASTMCP_3_0_CONTEXT = {
    "version": "3.0.0",
    "features": {
        "core": [
            "Decorators return original functions for direct testing",
            "Context injection in tools, resources, and prompts (ctx: Context)",
            "Component-level authorization with auth=require_auth or auth=require_scopes()",
            "Server composition with mount() and namespaces",
            "Lifespan management with async context managers",
            "FileSystemProvider for automatic component discovery",
            "Multiple transport options: stdio, http, sse",
            "Proxy servers with FastMCP.as_proxy()",
            "Automatic generation from OpenAPI/FastAPI specs"
        ],
        "development": [
            "Direct function testing without MCP client setup",
            "Progress reporting with ctx.report_progress()",
            "Logging with ctx.info(), ctx.debug(), ctx.warning()",
            "Tags and metadata for tool organization",
            "Type hints and Pydantic model integration",
            "Async/await native support throughout"
        ],
        "composition": [
            "mount(server, namespace='prefix') for modular architecture",
            "import_server() for static component import",
            "Namespace prefixing for tools: 'namespace_tool_name'",
            "Namespace prefixing for resources: 'scheme://namespace/path'",
            "Cross-server tool discovery and invocation"
        ],
        "production": [
            "JWT authentication with JWTVerifier",
            "OAuth 2.1 integration",
            "Component-level scopes with require_scopes()",
            "HTTP transport with configurable host/port",
            "Health checks and monitoring integration",
            "Rate limiting and security features"
        ]
    },
    "evolution": {
        "v1_0": "Basic server building (now in official MCP SDK)",
        "v2_0": "Complete ecosystem: clients, auth, deployment, testing",
        "v3_0": "Testability, composition, lifespan, component authorization"
    },
    "installation": {
        "recommended": "uv add fastmcp",
        "pip": "pip install fastmcp",
        "requirements": "Python 3.10+, type hints support"
    },
    "patterns": {
        "context_injection": """
@mcp.tool()
async def my_tool(param: str, ctx: Context) -> str:
    await ctx.info("Processing...")
    await ctx.report_progress(0.5, "Halfway done")
    return result
""",
        "lifespan": """
@asynccontextmanager
async def lifespan(mcp: FastMCP):
    db = await Database.connect()
    yield {"db": db}
    await db.disconnect()

mcp = FastMCP("Server", lifespan=lifespan)
""",
        "composition": """
main = FastMCP("Main")
sub = FastMCP("Sub")

@sub.tool()
def hello(): return "hi"

main.mount(sub, namespace="sub")
# Tool accessible as "sub_hello"
""",
        "authorization": """
from fastmcp.server.auth import require_auth, require_scopes

@mcp.tool(auth=require_auth)
def protected_tool(): ...

@mcp.resource("data://secret", auth=require_scopes("read"))
def secret_data(): ...
"""
    }
}

# Best practices knowledge base (unified and expanded version)
BEST_PRACTICES = {
    "fastmcp_2_0": [
        "Use FastMCP 2.0 decorators (@mcp.tool, @mcp.resource) for simplicity",
        "Leverage built-in MCP Inspector for testing during development",
        "Implement proper Pydantic models for all data structures",
        "Use FastMCP's built-in authentication and deployment features",
        "Take advantage of automatic protocol handling",
        "Follow FastMCP's Pythonic patterns with type hints"
    ],
    "architecture": [
        "Use FastMCP 2.0+ with proper tool and resource decorators",
        "Implement modular structure with clear separation of concerns",
        "Choose appropriate transport protocol (STDIO, HTTP, SSE)",
        "Use Pydantic models for data validation and serialization",
        "Implement proper error handling with meaningful messages",
        "Follow async/await patterns for all I/O operations"
    ],
    "security": [
        "Implement OAuth 2.1 authentication with short-lived tokens",
        "Validate all inputs using JSON Schema",
        "Sanitize paths to prevent directory traversal",
        "Use HTTPS with valid TLS certificates",
        "Implement rate limiting to prevent DoS attacks",
        "Validate tool metadata rigorously",
        "Never expose sensitive information in logs"
    ],
    "scalability": [
        "Use Redis for distributed state storage",
        "Implement SSE transport for stateful connections",
        "Use asynchronous processing with async/await",
        "Implement health checks (liveness/readiness)",
        "Use connection pooling for external dependencies",
        "Consider serverless architecture when appropriate",
        "Implement circuit breakers for external APIs"
    ],
    "performance": [
        "Choose appropriate transport (STDIO for local, HTTP for web)",
        "Implement caching when possible",
        "Use parallel processing for independent tasks",
        "Optimize cold start in serverless environments",
        "Minimize latency with persistent connections",
        "Implement semantic chunking for large documents"
    ],
    "observability": [
        "Implement structured logging with JSON",
        "Use correlation IDs for tracing",
        "Integrate with OpenTelemetry for distributed traces",
        "Expose Prometheus metrics",
        "Implement comprehensive health checks",
        "Monitor tool execution times and error rates"
    ],
    "testing": [
        "Write comprehensive unit tests with pytest",
        "Test with fastmcp.Client",
        "Validate with MCP Inspector",
        "Test error scenarios and edge cases",
        "Implement integration tests for external APIs",
        "Use McpSafetyScanner for security testing"
    ]
}


# Keywords for prompt analysis
KEYWORDS = {
    "tools": ["@mcp.tool", "tool", "function", "action", "command"],
    "resources": ["@mcp.resource", "resource", "data", "information"],
    "transport": ["stdio", "http", "sse", "streamable", "transport", "protocol"],
    "security": ["auth", "oauth", "security", "authentication", "validation"],
    "scalability": ["redis", "scale", "distributed", "performance"],
    "business": ["objective", "purpose", "business", "problem", "user"]
}


# Prompt analysis tools


@mcp.tool(tags=["analysis", "validation", "scoring"])
async def fastmcp_analyze_mcp_prompt(
    prompt: str,
    ctx: Optional[Context] = None
) -> PromptAnalysis:
    """
    Analyzes an MCP server creation prompt and provides detailed feedback.

    This tool evaluates prompt quality considering:
    - Clarity and completeness of requirements
    - Adherence to FastMCP best practices  
    - Presence of essential elements
    - Technical and production aspects
    """
    if ctx:
        await ctx.info("Analyzing MCP prompt for quality and completeness...")

    prompt_lower = prompt.lower()
    score = 0.0
    strengths = []
    weaknesses = []
    recommendations = []

    # Structure and clarity analysis (0-25 points)
    if len(prompt) > 100:
        score += 10
        strengths.append(
            "Prompt has adequate length for detailed requirements")
    else:
        weaknesses.append("Prompt is too brief and lacks detail")
        recommendations.append("Expand prompt with more specific requirements")

    if any(word in prompt_lower for word in ["objective", "purpose"]):
        score += 10
        strengths.append("Clear objective or purpose is defined")
    else:
        weaknesses.append("Missing clear objective or purpose")
        recommendations.append(
            "Add a clear statement of what the server should accomplish")

    if prompt.count('\n') > 3:
        score += 5
        strengths.append("Well-structured with multiple sections")
    else:
        weaknesses.append("Lacks clear structure")
        recommendations.append(
            "Organize into clear sections (Objective, Requirements, Technical, etc.)")

    # Technical analysis (0-30 points)
    has_tools = any(word in prompt_lower for word in KEYWORDS["tools"])
    has_resources = any(word in prompt_lower for word in KEYWORDS["resources"])

    if has_tools:
        score += 15
        strengths.append("Specifies tools/functions needed")
    else:
        weaknesses.append("Missing tool specifications")
        recommendations.append(
            "Define specific tools using @mcp.tool() pattern")

    if has_resources:
        score += 10
        strengths.append("Defines resources to expose")
    else:
        weaknesses.append("No resource specifications")
        recommendations.append(
            "Consider what data should be exposed via @mcp.resource()")

    if any(word in prompt_lower for word in KEYWORDS["transport"]):
        score += 5
        strengths.append("Mentions transport protocol")
    else:
        recommendations.append("Specify transport protocol (STDIO/HTTP/SSE)")

    # Best practices analysis (0-25 points)
    has_security = any(word in prompt_lower for word in KEYWORDS["security"])
    has_scalability = any(
        word in prompt_lower for word in KEYWORDS["scalability"])

    if has_security:
        score += 10
        strengths.append("Considers security requirements")
    else:
        weaknesses.append("Missing security considerations")
        recommendations.append(
            "Add authentication and validation requirements")

    if has_scalability:
        score += 10
        strengths.append("Addresses scalability concerns")
    else:
        recommendations.append(
            "Consider scalability requirements for production use")

    if any(word in prompt_lower for word in ["async", "asynchronous", "await"]):
        score += 5
        strengths.append("Mentions asynchronous processing")

    # Business context analysis (0-20 points)
    has_business_context = any(
        word in prompt_lower for word in KEYWORDS["business"])

    if has_business_context:
        score += 15
        strengths.append("Includes business context and objectives")
    else:
        weaknesses.append("Lacks business context")
        recommendations.append(
            "Explain the business problem this server will solve")

    if any(word in prompt_lower for word in ["example", "usage"]):
        score += 5
        strengths.append("Includes usage examples")
    else:
        recommendations.append("Add concrete usage examples")

    return PromptAnalysis(
        score=min(100.0, score),
        strengths=strengths,
        weaknesses=weaknesses,
        recommendations=recommendations,
        has_technical_requirements=has_tools or has_resources,
        has_business_context=has_business_context,
        has_security_considerations=has_security
    )



# Prompt optimization tools


@mcp.tool(tags=["optimization", "improvement", "suggestions"])
async def fastmcp_suggest_prompt_improvements(
    original_prompt: str,
    focus_area: Optional[str] = None,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Suggests specific improvements for an MCP server creation prompt.

    Returns an improved prompt and explains the applied changes.
    """
    if ctx:
        await ctx.info(f"Generating improvement suggestions for prompt...")

    # Analyze the original prompt first
    analysis = await fastmcp_analyze_mcp_prompt(original_prompt, ctx) if ctx else PromptAnalysis(
        score=50.0, strengths=[], weaknesses=["Simplified analysis"], recommendations=[]
    )

    # Base of the improved prompt
    improved_sections = []

    # Context and purpose section
    if ("create" in original_prompt.lower() and "server" in original_prompt.lower()):
        purpose_section = """## Context and Objective
I need to create an MCP server with FastMCP in Python that [DESCRIBE SPECIFIC PURPOSE].

### Use Case
[DESCRIBE WHEN AND HOW THE SERVER WILL BE USED]"""
        improved_sections.append(purpose_section)

    # Functional requirements section
    functional_section = """## Functional Requirements

### Tools (@mcp.tool())
1. **[TOOL_NAME_1]**
   - Description: [WHAT IT DOES]
   - Parameters: [TYPE AND DESCRIPTION]
   - Return: [TYPE AND FORMAT]
   - Example: [USAGE EXAMPLE]

### Resources (@mcp.resource())
1. **[RESOURCE_URI_1]**
   - Description: [EXPOSED DATA]
   - Format: [JSON/TEXT/OTHER]"""
    improved_sections.append(functional_section)

    # Technical section if focus is technical
    if focus_area == "technical" or focus_area is None:
        technical_section = """## Technical Requirements

- **Asynchronous Operations**: [LIST OPERATIONS THAT NEED TO BE ASYNC]
- **External Integrations**: [APIs, DATABASES, SERVICES]
- **Error Handling**: [HOW TO HANDLE FAILURES]
- **Data Validation**: [USE PYDANTIC MODELS]"""
        improved_sections.append(technical_section)

    # Production section if relevant
    if focus_area == "production":
        production_section = """## Production Requirements

- **Security**: [AUTHENTICATION, AUTHORIZATION, VALIDATION]
- **Scalability**: [STATE CONSIDERATIONS, REDIS]
- **Observability**: [LOGGING, METRICS, TRACES]
- **Health Checks**: [HEALTH ENDPOINTS]"""
        improved_sections.append(production_section)

    # Add examples
    example_section = """## Usage Examples

```python
# Example of main tool call
result = await client.call_tool("tool_name", {
    "param1": "value",
    "param2": 123
})
```"""
    improved_sections.append(example_section)

    improved_prompt = "\n\n".join(improved_sections)

    # Explain changes
    changes_explanation = [
        "Structured the prompt into clear and well-defined sections",
        "Added templates to specify tools and resources",
        "Included fields for concrete usage examples",
        "Added technical requirements section when relevant",
        f"Applied focus: {focus_area or 'general'}"
    ]

    return {
        "improved_prompt": improved_prompt,
        "changes_explanation": changes_explanation,
        "improvement_score": min(100.0, analysis.score + 30.0),
        "next_steps": [
            "Fill in template fields with specific information",
            "Add more details about usage context",
            "Review and validate technical requirements"
        ]
    }



# Validation tools


@mcp.tool(tags=["validation", "requirements", "checklist"])
async def fastmcp_validate_requirements(
    requirements: str,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Validates MCP server requirements against best practices checklist.

    Checks completeness and adequacy of specified requirements.
    """
    if ctx:
        await ctx.info("Validating requirements against best practices...")

    validation_results: Dict[str, Any] = {
        "is_valid": True,
        "completeness_score": 0.0,
        "issues": [],
        "missing_requirements": [],
        "suggestions": []
    }

    # Essential requirements checklist
    essential_checklist = {
        "purpose_defined": "purpose" in requirements.lower() or "objective" in requirements.lower(),
        "tools_specified": "tool" in requirements.lower() or "function" in requirements.lower(),
        "data_types_defined": "type" in requirements.lower() or "data type" in requirements.lower(),
        "error_handling": "error" in requirements.lower() or "exception" in requirements.lower(),
        "examples_included": "example" in requirements.lower(),
        "async_considered": "async" in requirements.lower() or "asynchronous" in requirements.lower()
    }

    # Calculate completeness
    checked_items = sum(essential_checklist.values())
    validation_results["completeness_score"] = (
        checked_items / len(essential_checklist)) * 100

    # Identify issues
    for requirement, is_present in essential_checklist.items():
        if not is_present:
            validation_results["missing_requirements"].append(requirement)
            validation_results["issues"].append(
                f"Missing requirement: {requirement}")

    # Validate if there are sufficient requirements
    if validation_results["completeness_score"] < 60:
        validation_results["is_valid"] = False
        validation_results["suggestions"].append(
            "Add more details to requirements. Use the template suggested by the improvement tool."
        )

    # Check production requirements if mentioned
    if "production" in requirements.lower():
        production_checks = {
            "security": any(word in requirements.lower() for word in ["security", "authentication"]),
            "scalability": any(word in requirements.lower() for word in ["scale", "redis", "state"]),
            "monitoring": any(word in requirements.lower() for word in ["log", "metrics", "observability"])
        }

        for check, is_present in production_checks.items():
            if not is_present:
                validation_results["suggestions"].append(
                    f"For production, consider adding {check} requirements"
                )

    if ctx:
        await ctx.info(f"Validation completed. Score: {validation_results['completeness_score']:.0f}%")

    return validation_results



# Template generation tools


@mcp.tool(tags=["generation", "templates", "server-creation"])
async def fastmcp_generate_server_template(
    server_type: str,
    name: str,
    description: str,
    ctx: Optional[Context] = None
) -> str:
    """
    Generates an optimized prompt template for creating a specific MCP server.

    Available templates:
    - basic: Simple server with basic tools and resources
    - api_integration: Server that integrates with external APIs
    - data_processing: Server focused on data processing
    - production_ready: Server with all production practices
    """
    if ctx:
        await ctx.info(f"Generating template for server type '{server_type}'...")

    # Common base template
    base_template = f"""# MCP Server Creation: {name}

## Objective
Create an MCP server with FastMCP in Python for {description}.

## Technical Specifications
- **Framework**: FastMCP 3.0+
- **Python**: 3.10+
- **Style**: Pythonic, with type hints and detailed docstrings
- **Features**: Context injection, tags, lifespan management
"""

    # Specific templates by type
    if server_type == "basic":
        specific_template = f"""
## Functional Requirements

### Tools
1. **main_tool**
   - Function: [DESCRIBE MAIN FUNCTION]
   - Parameters:
     - param1 (str): [DESCRIPTION]
     - param2 (int): [DESCRIPTION]
   - Return: Dict with processed result
   - Error handling: Validate input and return clear messages

### Resources
1. **info://status**
   - Returns current server status
   - Format: JSON
   
2. **config://settings**
   - Exposes current configuration
   - Format: JSON

### Code Structure
```python
from fastmcp import FastMCP, Context
from pydantic import BaseModel, Field
from typing import Dict, Any

mcp = FastMCP(name="{name}")

@mcp.tool()
async def main_tool(param1: str, param2: int, ctx: Context) -> Dict[str, Any]:
    '''Detailed docstring'''
    # Implementation
    pass
```
"""

    elif server_type == "api_integration":
        specific_template = f"""
## Integration Requirements

### External APIs
- **Main API**: [NAME AND DOCUMENTATION]
- **Authentication**: [METHOD - Bearer Token, API Key, etc]
- **Rate Limiting**: [LIMITS AND STRATEGY]

### Integration Tools
1. **fetch_data**
   - Fetch data from external API
   - Implement retry logic and circuit breaker
   - Cache responses when appropriate

2. **process_and_send**
   - Process data and send to API
   - Robust validation with Pydantic
   - Network error handling

### Technical Requirements
- Use httpx for asynchronous calls
- Implement configurable timeout and retry
- Detailed logging of all interactions
- Secure credential management (environment variables)

### Implementation Example
```python
import httpx
from fastmcp import FastMCP, Context

mcp = FastMCP(name="{name}")

@mcp.tool()
async def fetch_data(endpoint: str, ctx: Context) -> Dict[str, Any]:
    async with httpx.AsyncClient() as client:
        # Implement logic with retry
        pass
```
"""

    elif server_type == "data_processing":
        specific_template = """
## Data Processing Requirements

### Processing Tools
1. **process_file**
   - Accepts: CSV, JSON, Excel
   - Asynchronous processing with progress reporting
   - Schema validation with Pydantic

2. **analyze_data**
   - Statistical analysis or ML
   - Returns structured insights
   - Support for large datasets (streaming)

### Data Resources
1. **data://processed/{{id}}**
   - Access to processed data
   - Pagination for large volumes

### Technical Requirements
- Use pandas/polars for efficient processing
- Implement chunk processing for large files
- Progress reporting via ctx.report_progress()
- Temporary storage with automatic cleanup

### Performance Considerations
- CPU-intensive operations in thread pool
- Limit memory usage
- Implement intelligent cache
"""

    elif server_type == "production_ready":
        specific_template = f"""
## Complete Production Requirements

### Architecture
- **State**: Distributed via Redis
- **Transport**: HTTP Streamable with fallback
- **Deployment**: Docker + Kubernetes ready

### Security
- Authentication via Bearer tokens
- Rate limiting per client
- Complete input validation
- Sensitive data sanitization in logs

### Observability
- Structured logging (JSON)
- Prometheus metrics
- Tracing with OpenTelemetry
- Health checks (liveness/readiness)

### Scalability
- Stateless server
- Connection pooling
- Distributed cache
- Graceful shutdown

### Main Tools
[DEFINE TOOLS WITH ALL THE ABOVE ASPECTS]

### Structure Example
```python
from fastmcp import FastMCP
import redis.asyncio as redis
import structlog

logger = structlog.get_logger()

mcp = FastMCP(
    name="{name}",
    dependencies=["redis", "prometheus-client", "opentelemetry-api"]
)

# Configure Redis for distributed state
# Implement authentication middleware
# Configure metrics and tracing
```

### Required Tests
- Unit tests with pytest
- Integration tests
- Load tests
- Security tests
"""

    else:
        specific_template = "\n## Server type not recognized. Use: basic, api_integration, data_processing, or production_ready"

    full_template = base_template + specific_template

    # Add best practices section
    best_practices = """
## Best Practices to Follow

1. **Clean Code**
   - Type hints in all functions
   - Descriptive docstrings
   - Meaningful variable names
   
2. **Error Handling**
   - Never leave exceptions unhandled
   - Useful error messages for debugging
   - Appropriate error logging
   
3. **Performance**
   - Async for all I/O operations
   - Avoid unnecessary blocking
   - Implement appropriate timeouts
   
4. **Security**
   - Validate all user input
   - Don't expose sensitive information
   - Use HTTPS in production
"""

    full_template += best_practices

    if ctx:
        await ctx.info(f"Template generated successfully for '{server_type}' server")

    return full_template.format(name=name)

# Server resources


@mcp.resource("mcp://best-practices")
async def get_mcp_best_practices() -> Dict[str, List[str]]:
    """
    Returns a summary of best practices for MCP server development.

    Includes structural, technical and production practices.
    """
    return BEST_PRACTICES




@mcp.resource("mcp://prompt-examples/{quality_level}")
async def get_prompt_examples(quality_level: str) -> Dict[str, Any]:
    """
    Provides prompt examples of different quality levels.

    Levels: bad, good, excellent
    """
    examples = {
        "bad": {
            "prompt": "create mcp server that does things with data",
            "issues": [
                "Too vague and generic",
                "Does not specify tools or resources",
                "No technical details",
                "No usage examples"
            ]
        },
        "good": {
            "prompt": """Create an MCP server with FastMCP to process CSV files.
            
The server should have a tool to read CSVs and return data in JSON format.
It should handle errors and validate the file format.""",
            "strengths": [
                "Clear purpose",
                "Mentions input/output format",
                "Considers error handling"
            ]
        },
        "excellent": {
            "prompt": """Create an MCP server with FastMCP in Python for sales data analysis.

## Functional Requirements
- Tool 'analyze_sales': accepts CSV with columns (date, product, quantity, price)
- Returns statistics: total sales, best-selling product, monthly trends
- Resource 'reports://latest': exposes latest generated report in JSON

## Technical Requirements  
- Asynchronous processing for large files (>100MB)
- Schema validation with Pydantic
- Cache results for 1 hour
- Structured logging of all operations

## Usage Example
```python
result = await client.call_tool("analyze_sales", {
    "file_path": "sales_2024.csv",
    "group_by": "month"
})
```""",
            "strengths": [
                "Complete and detailed specification",
                "Clearly defines tools and resources",
                "Includes important technical requirements",
                "Provides concrete usage example",
                "Considers performance and caching"
            ]
        }
    }

    if quality_level not in examples:
        return {"error": f"Level '{quality_level}' not found. Use: bad, good, or excellent"}

    return examples[quality_level]


@mcp.resource("mcp://frameworks")
async def get_prompt_frameworks() -> Dict[str, Any]:
    """
    Returns prompt engineering frameworks applicable to MCP server creation.
    """
    return {
        "frameworks": {
            "CRISP": {
                "name": "Context, Requirements, Instructions, Specifications, Prompts",
                "description": "Structured framework for complex prompts",
                "application": "Ideal for specifying complete MCP servers",
                "template": """[Context] I need to create an MCP server for...
[Requirements] The server should have the following capabilities...
[Instructions] Use FastMCP 2.0 with Python 3.8+...
[Specifications] Tools: [...], Resources: [...], Types: [...]
[Prompts/Examples] Usage example: ..."""
            },
            "STAR": {
                "name": "Situation, Task, Action, Result",
                "description": "Framework for results-oriented prompts",
                "application": "Good for servers with specific objectives",
                "template": """[Situation] We have sales data in multiple formats...
[Task] We need an MCP server that unifies and analyzes...
[Action] Implement tools to import, process and generate reports...
[Result] The server should return analyses in JSON format..."""
            },
            "Chain-of-Thought": {
                "name": "Step-by-step thinking",
                "description": "Breaks down the problem into logical steps",
                "application": "Useful for servers with complex logic",
                "template": """Step 1: Identify the data the server will process
Step 2: Define necessary transformations
Step 3: Specify tools for each transformation
Step 4: Determine resources to expose
Step 5: Add error and security requirements"""
            }
        },
        "recommendation": "For MCP servers, the CRISP framework is generally more effective due to its complete structure"
    }


@mcp.resource("template://basic-server")
async def get_basic_template() -> str:
    """Get basic template for creating a FastMCP server."""
    return '''"""
MCP Server for [DESCRIBE PURPOSE]

This server [DESCRIBE WHAT IT DOES].
"""

from fastmcp import FastMCP, Context
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
import asyncio

# Initialize server
mcp = FastMCP(
    name="my-mcp-server",
    description="[SERVER DESCRIPTION]",
    version="1.0.0"
)

# Data models
class MyModel(BaseModel):
    """Model for [DESCRIBE]"""
    field: str = Field(description="Field description")

# Tools
@mcp.tool()
async def my_tool(parameter: str) -> str:
    """
    [DESCRIBE WHAT THE TOOL DOES]
    
    Args:
        parameter: [DESCRIBE THE PARAMETER]
        
    Returns:
        [DESCRIBE THE RETURN VALUE]
    """
    # Implement logic here
    return f"Processed: {parameter}"

# Resources
@mcp.resource("data://example")
async def my_resource() -> Dict[str, Any]:
    """[DESCRIBE THE RESOURCE]"""
    return {"example": "data"}

# To run locally
if __name__ == "__main__":
    import asyncio
    from fastmcp.cli import main
    asyncio.run(main(mcp))
'''


@mcp.resource("checklist://development")
async def get_development_checklist() -> Dict[str, List[str]]:
    """Get complete checklist for MCP server development."""
    return {
        "planning": [
            "Define server objective and scope",
            "Identify necessary tools",
            "Map resources to expose",
            "Choose transport protocol",
            "Define security requirements",
            "Plan scalability strategy"
        ],
        "development": [
            "Set up Python 3.8+ environment",
            "Install FastMCP via pip/uv",
            "Create modular directory structure",
            "Implement tools with @mcp.tool()",
            "Implement resources with @mcp.resource()",
            "Add type hints and docstrings",
            "Implement input validation",
            "Add error handling",
            "Configure structured logging"
        ],
        "testing": [
            "Write unit tests with pytest",
            "Test with fastmcp.Client",
            "Validate with MCP Inspector",
            "Test error scenarios",
            "Check performance",
            "Test external integrations"
        ],
        "security": [
            "Implement authentication if needed",
            "Validate all inputs",
            "Sanitize sensitive data",
            "Configure HTTPS in production",
            "Implement rate limiting",
            "Review code for vulnerabilities",
            "Test with McpSafetyScanner"
        ],
        "deployment": [
            "Configure CI/CD pipeline",
            "Create Dockerfile if needed",
            "Configure health checks",
            "Implement monitoring",
            "Configure backups",
            "Document deployment process",
            "Create operational runbook"
        ],
        "documentation": [
            "Write complete README",
            "Document tools API",
            "Create usage examples",
            "Document configuration",
            "Add troubleshooting guide",
            "Maintain updated changelog"
        ]
    }

# Server prompts


@mcp.prompt("optimize_mcp_prompt")
async def optimize_mcp_prompt_template(
    user_context: str,
    requirements: str
) -> List[Dict[str, str]]:
    """
    Prompt template for MCP prompt optimization.
    """
    return [
        {
            "role": "system",
            "content": """You are an expert in creating prompts for MCP server development with FastMCP.
            
Your specialties include:
- Clear structuring of requirements
- Application of FastMCP best practices
- Production and scalability considerations
- Advanced prompt engineering techniques

When optimizing prompts, you always:
1. Add clear structure with well-defined sections
2. Specify tools and resources with details
3. Include data types and examples
4. Consider production aspects when relevant
5. Suggest incremental and practical improvements"""
        },
        {
            "role": "user",
            "content": f"""Context: {user_context}

Current requirements: {requirements}

Please optimize this prompt to create an MCP server, following best practices and making it clearer, more complete and effective."""
        }
    ]


@mcp.prompt("mcp_code_review")
async def mcp_code_review_template(code: str) -> List[Dict[str, str]]:
    """
    Template for MCP server code review.
    """
    return [
        {
            "role": "system",
            "content": """You are a reviewer specialized in FastMCP code.
            
When reviewing, you check:
- Correct use of decorators @mcp.tool(), @mcp.resource(), @mcp.prompt()
- Adequate type hints and docstrings
- Appropriate error handling
- Use of async/await for I/O operations
- Security and validation patterns
- Code structure and organization"""
        },
        {
            "role": "user",
            "content": f"""Review this MCP server code and suggest improvements:

```python
{code}
```

Identify problems and provide specific improvement suggestions."""
        }
    ]


@mcp.prompt("create_mcp_server")
async def create_server_prompt(
    objective: str,
    required_tools: List[str],
    has_external_integration: bool = False,
    needs_scaling: bool = False
) -> List[Dict[str, str]]:
    """
    Generate an optimized prompt for creating MCP server.

    Args:
        objective: What the server should do
        required_tools: List of required tools
        has_external_integration: If it needs to integrate with external APIs
        needs_scaling: If it needs to support high load

    Returns:
        List of messages for the prompt
    """
    prompt_parts = [
        f"Create an MCP server with FastMCP in Python that {objective}.",
        "\nTechnical requirements:",
        f"- Required tools: {', '.join(required_tools)}",
        "- Use type hints and detailed docstrings",
        "- Implement input validation with Pydantic",
        "- Add appropriate error handling",
        "- Follow modular structure with clear separation"
    ]

    if has_external_integration:
        prompt_parts.extend([
            "\nIntegrations:",
            "- Configure asynchronous HTTP clients for external APIs",
            "- Implement retry logic and circuit breakers",
            "- Use environment variables for credentials"
        ])

    if needs_scaling:
        prompt_parts.extend([
            "\nScalability:",
            "- Use Redis for distributed state",
            "- Implement connection pooling",
            "- Configure appropriate health checks",
            "- Use asynchronous processing"
        ])

    prompt_parts.extend([
        "\nSecurity:",
        "- Validate all inputs with JSON Schema",
        "- Sanitize paths and user data",
        "- Implement rate limiting if appropriate",
        "\nAlso include:",
        "- Complete usage example",
        "- Configuration instructions",
        "- Basic tests with pytest"
    ])

    return [
        {"role": "user", "content": "\n".join(prompt_parts)}
    ]

@mcp.prompt("design_server_composition")
async def design_server_composition_prompt(
    main_server_purpose: str,
    sub_servers: List[str],
    shared_state: bool = False
) -> List[Dict[str, str]]:
    """
    Generate prompt for designing MCP server composition with mount().

    Args:
        main_server_purpose: Purpose of the main orchestrating server
        sub_servers: List of sub-server names/purposes to compose
        shared_state: Whether servers need to share state

    Returns:
        List of messages for designing server composition
    """
    sub_servers_text = "\n".join([f"- {s}" for s in sub_servers])
    state_text = """
### Shared State
- Use lifespan to initialize shared resources
- Pass context through lifespan_context
- Consider Redis for distributed state""" if shared_state else ""

    return [
        {
            "role": "system",
            "content": """You are an expert in FastMCP 3.0 server composition.

Your expertise includes:
- Designing modular server architectures with mount()
- Namespace management for avoiding tool/resource conflicts
- Lifespan coordination between composed servers
- State sharing patterns between mounted servers
- Cross-server communication patterns"""
        },
        {
            "role": "user",
            "content": f"""Design a composed MCP server architecture.

## Main Server Purpose
{main_server_purpose}

## Sub-Servers to Compose
{sub_servers_text}
{state_text}

## Requirements
- Use FastMCP 3.0 mount() for composition
- Define clear namespaces for each sub-server
- Handle lifespan properly for all servers
- Ensure tools are discoverable with proper naming

## Expected Output
1. Architecture diagram (text-based)
2. Main server code with mount() calls
3. Sub-server interfaces
4. Namespace conventions
5. State sharing strategy (if applicable)"""
        }
    ]


@mcp.prompt("create_authenticated_server")
async def create_authenticated_server_prompt(
    server_purpose: str,
    auth_type: str = "jwt",
    scopes: List[str] = None
) -> List[Dict[str, str]]:
    """
    Generate prompt for creating an authenticated MCP server.

    Args:
        server_purpose: What the server should do
        auth_type: Authentication type (jwt, oauth)
        scopes: List of authorization scopes needed

    Returns:
        List of messages for creating authenticated server
    """
    scopes_text = ", ".join(scopes) if scopes else "read, write, admin"

    return [
        {
            "role": "system",
            "content": """You are an expert in FastMCP 3.0 authentication and authorization.

Your expertise includes:
- JWT authentication with JWTVerifier
- OAuth 2.1 integration patterns
- Component-level authorization with require_auth and require_scopes
- Secure token handling and validation
- Role-based access control (RBAC) implementation"""
        },
        {
            "role": "user",
            "content": f"""Create an authenticated MCP server with FastMCP 3.0.

## Server Purpose
{server_purpose}

## Authentication Requirements
- **Type**: {auth_type.upper()}
- **Scopes**: {scopes_text}

## Security Requirements
- Implement component-level authorization
- Use auth=require_auth for protected tools
- Use auth=require_scopes() for scope-based access
- Handle authentication errors gracefully
- Never expose tokens in logs

## Expected Output
1. Server initialization with auth configuration
2. Protected tools with appropriate decorators
3. Public tools (if any)
4. Token verification setup
5. Error handling for auth failures
6. Usage example with authentication"""
        }
    ]


@mcp.prompt("generate_from_openapi")
async def generate_from_openapi_prompt(
    api_description: str,
    openapi_url: str = "",
    selected_endpoints: List[str] = None
) -> List[Dict[str, str]]:
    """
    Generate prompt for creating MCP server from OpenAPI specification.

    Args:
        api_description: Description of the API to wrap
        openapi_url: URL to OpenAPI spec (optional)
        selected_endpoints: Specific endpoints to include (optional)

    Returns:
        List of messages for generating server from OpenAPI
    """
    endpoints_text = "\n".join([f"- {e}" for e in selected_endpoints]) if selected_endpoints else "All endpoints"

    return [
        {
            "role": "system",
            "content": """You are an expert in generating FastMCP servers from OpenAPI specifications.

Your expertise includes:
- Parsing OpenAPI 3.0/3.1 specifications
- Using FastMCP.from_openapi() for automatic generation
- Customizing generated tools and resources
- Handling authentication from OpenAPI securitySchemes
- Mapping OpenAPI operations to MCP tools"""
        },
        {
            "role": "user",
            "content": f"""Generate an MCP server from an OpenAPI specification.

## API Description
{api_description}

## OpenAPI Source
{openapi_url if openapi_url else "[Provide OpenAPI spec inline or URL]"}

## Endpoints to Include
{endpoints_text}

## Requirements
- Use FastMCP.from_openapi() when applicable
- Map each endpoint to an appropriate MCP tool
- Preserve parameter types and validation
- Handle authentication from securitySchemes
- Add proper error handling for API calls

## Expected Output
1. Analysis of OpenAPI spec
2. Generated MCP server code
3. Tool mappings for each endpoint
4. Authentication configuration
5. Usage examples for key tools"""
        }
    ]


# Server initialization function


async def main():
    """Initialize and run the MCP server."""
    logger.info(f"Starting {mcp.name}...")
    logger.info("Unified FastMCP server configured and ready for use")

if __name__ == "__main__":
    # For local development/testing
    import sys
    if "--test" in sys.argv:
        # Test mode - run some validations
        asyncio.run(main())
    else:
        # Normal mode - FastMCP manages execution
        logger.info("Server ready for execution via FastMCP CLI")
        # Start the FastMCP server
        mcp.run()
