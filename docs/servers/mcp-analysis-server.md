# MCP Analysis Server

The MCP Analysis Server provides intelligent analysis and feedback on prompts designed for creating MCP (Model Context Protocol) servers. It evaluates prompt quality based on MCP documentation best practices and provides detailed recommendations for improvement.

## Overview

This server helps developers create better MCP servers by analyzing their creation prompts and ensuring they follow established best practices. It provides scoring, identifies strengths and weaknesses, and offers specific recommendations.

**Port**: 3000  
**Protocol**: stdio  
**Module**: `servers.mcp_server`

## Features

### 🔍 Prompt Analysis
- **Quality Scoring**: 1-10 scale evaluation of prompt quality
- **Best Practices Alignment**: Checks against 10 key MCP development practices
- **Pattern Recognition**: Identifies positive and negative patterns in prompts
- **Missing Elements Detection**: Highlights critical components that are missing

### 📊 Comprehensive Reporting
- **Strengths Identification**: Lists strong points in the prompt
- **Weakness Analysis**: Identifies areas needing improvement
- **Specific Recommendations**: Actionable suggestions for enhancement
- **Validation Reports**: Detailed compliance reports with pass/fail status

## Available Tools

### `mcp_analyze_server_prompt(prompt: str)`
Analyzes an MCP server creation prompt for quality and alignment with best practices.

**Parameters:**
- `prompt` (string): The prompt text to analyze

**Returns:**
- `score` (1-10): Overall quality score
- `strengths` (array): Strong points identified
- `weaknesses` (array): Areas for improvement  
- `recommendations` (array): Specific improvement suggestions
- `best_practices_alignment` (object): Alignment with each best practice
- `missing_elements` (array): Important missing elements

**Example:**
```python
analysis = mcp_analyze_server_prompt("""
Create an MCP server for file management with tools to read, write, 
and delete files. Include proper error handling and security validation.
""")
# Returns detailed analysis with score and recommendations
```

### `mcp_get_best_practices()`
Returns a summary of MCP server development best practices.

**Returns:**
- Dictionary of best practices with descriptions

**Example:**
```python
practices = mcp_get_best_practices()
# Returns: {"clear_purpose": "Define a specific...", "tool_design": "Design tools..."}
```

### `mcp_suggest_prompt_improvements(original_prompt: str)`
Suggests specific improvements for an MCP server creation prompt.

**Parameters:**
- `original_prompt` (string): The original prompt to improve

**Returns:**
- `original_prompt` (string): The original prompt
- `improved_prompt` (string): Enhanced version with additions
- `improvements_made` (array): List of improvements applied
- `score_improvement` (string): Expected score improvement

**Example:**
```python
improvements = mcp_suggest_prompt_improvements("Create a simple MCP server")
# Returns enhanced prompt with additional requirements
```

### `mcp_validate_requirements(requirements: str)`
Validates MCP server requirements against best practices checklist.

**Parameters:**
- `requirements` (string): The requirements specification to validate

**Returns:**
- `overall_score` (number): Overall validation score
- `validation_passed` (boolean): Whether validation passed (≥7 score)
- `requirements_coverage` (object): Coverage of each requirement
- `missing_requirements` (array): Missing requirements
- `recommendations` (array): Recommendations for improvement
- `critical_issues` (array): Critical issues that must be addressed
- `warnings` (array): Non-critical warnings

## Best Practices Evaluated

The server evaluates prompts against these key areas:

1. **Clear Purpose**: Well-defined and specific server objectives
2. **Adequate Tool Design**: Focused, well-documented tools with proper naming
3. **Error Handling**: Comprehensive error handling and validation strategies
4. **Security Considerations**: Input validation, sanitization, and security measures
5. **Resource Management**: Proper resource handling and cleanup procedures
6. **Documentation**: Clear documentation and usage examples
7. **Schema Validation**: Proper schema definitions and data validation
8. **Transport Protocol**: Appropriate transport protocol selection
9. **Testing Strategy**: Testing and debugging considerations
10. **Performance**: Performance and scalability considerations

## Usage Examples

### Basic Analysis
```bash
# Start the server
python main.py mcp

# Use with Claude Desktop or other MCP clients
# The server will be available on stdio protocol
```

### Integration with Development Workflow
```python
# Analyze a prompt before implementing
prompt = """
Create an MCP server for database operations with PostgreSQL.
Include CRUD operations, connection pooling, and transaction support.
Implement proper error handling, input validation, and logging.
Add schema definitions for all data types.
Include comprehensive testing and documentation.
"""

analysis = mcp_analyze_server_prompt(prompt)
print(f"Quality Score: {analysis.score}/10")
for recommendation in analysis.recommendations:
    print(f"• {recommendation}")
```

### Validation Workflow
```python
# Validate requirements before development
requirements = """
Server Purpose: API integration helper
Tools: fetch_data, process_response, cache_results  
Security: Input validation, rate limiting
Documentation: API examples and usage guide
"""

validation = mcp_validate_requirements(requirements)
if validation.validation_passed:
    print("✅ Requirements meet MCP best practices")
else:
    print("❌ Issues found:")
    for issue in validation.critical_issues:
        print(f"  • {issue}")
```

## Configuration

The server can be configured through environment variables:

- `MCP_SERVER_PORT`: Server port (default: 3000)
- `MCP_SERVER_PROTOCOL`: Communication protocol (default: stdio)

## Dependencies

- **FastMCP**: 2.4.0+
- **Pydantic**: For data validation and serialization
- **Python**: 3.12+

## Error Handling

The server includes comprehensive error handling:
- Input validation for all parameters
- Graceful handling of malformed prompts
- Detailed error messages with context
- Logging for debugging and monitoring

## Performance

- **Analysis Speed**: < 100ms for typical prompts
- **Memory Usage**: Minimal memory footprint
- **Concurrent Analysis**: Supports multiple simultaneous analyses
- **Caching**: Pattern matching results are optimized for performance

---

*This server is part of the MCP Servers Collection developed by Charleno Pires*