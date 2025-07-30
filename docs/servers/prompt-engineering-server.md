# Prompt Engineering Server

The Prompt Engineering Server provides advanced prompt optimization techniques to enhance the effectiveness of AI interactions. It implements proven frameworks like RACE, TRACE, CRISPE, and advanced reasoning techniques to improve prompt quality and output reliability.

## Overview

This server helps users create better prompts by applying established prompt engineering methodologies. It analyzes prompts, suggests improvements, detects biases, and applies advanced reasoning techniques to enhance AI interactions.

**Port**: 3001  
**Protocol**: stdio  
**Module**: `servers.prompt_server`

## Features

### 🔧 Prompt Optimization
- **Automatic Enhancement**: Applies multiple optimization techniques
- **Framework Integration**: RACE, TRACE, CRISPE, CORE, COAST frameworks
- **Task Type Detection**: Automatically identifies prompt intent
- **Quality Scoring**: 0-100 scale evaluation with detailed feedback

### 🧠 Advanced Reasoning Techniques
- **Chain-of-Thought (CoT)**: Step-by-step reasoning guidance
- **Self-Consistency**: Multiple reasoning paths for reliability
- **ReAct**: Reason + Act iterative approach
- **Tree of Thoughts**: Multi-path exploration

### 🔍 Quality Analysis
- **Bias Detection**: Identifies potential biases and suggests mitigations
- **Clarity Assessment**: Evaluates specificity and clarity
- **Context Analysis**: Checks for adequate context provision
- **Framework Recommendations**: Suggests optimal frameworks per task type

## Available Tools

### `optimize_prompt(prompt, task_type?, target_audience?, desired_length?, tone?)`
Optimizes a prompt by applying prompt engineering best practices.

**Parameters:**
- `prompt` (string): The original prompt to optimize
- `task_type` (string, optional): Task type (auto-detected if not provided)
- `target_audience` (string, optional): Target audience for the response
- `desired_length` (string, optional): Desired response length
- `tone` (string, optional): Desired tone (formal, informal, technical, etc.)

**Returns:**
- `original_prompt` (string): The original prompt
- `optimized_prompt` (string): Enhanced version with applied techniques
- `techniques_applied` (array): List of techniques used
- `task_type` (string): Detected or specified task type
- `suggestions` (array): Additional improvement suggestions

**Example:**
```python
result = optimize_prompt(
    "Create a function", 
    target_audience="developers",
    tone="technical"
)
# Returns optimized prompt with role, context, and examples
```

### `analyze_prompt(prompt: str)`
Analyzes a prompt and provides detailed feedback on its quality.

**Parameters:**
- `prompt` (string): The prompt to analyze

**Returns:**
- `prompt` (string): Original prompt
- `length` (number): Character count
- `task_type` (string): Detected task type
- `quality_score` (number): Quality score (0-100)
- `strengths` (array): Identified strong points
- `weaknesses` (array): Areas needing improvement
- `recommendations` (array): Specific improvement suggestions

**Example:**
```python
analysis = analyze_prompt("Explain machine learning")
# Returns: quality_score: 45, weaknesses: ["Lacks context", "Unclear objective"]
```

### `suggest_framework(task_description: str)`
Suggests the optimal prompt framework for a specific task type.

**Parameters:**
- `task_description` (string): Description of the task to be performed

**Returns:**
- `task_type` (string): Detected task type
- `recommended_framework` (string): Best framework for the task
- `framework_components` (array): Components of the framework
- `example_application` (object): Practical application example
- `usage_tip` (string): How to apply the framework

**Task Type → Framework Mapping:**
- Text Generation → TRACE
- Code Generation → RACE  
- Image Generation → CRISPE
- Analysis → COAST
- Creative → CRISPE
- Problem Solving → CORE
- Question Answering → RACE

**Example:**
```python
framework = suggest_framework("Generate Python code for data analysis")
# Returns: recommended_framework: "RACE", components: ["Role", "Action", "Context", "Expectation"]
```

### `apply_advanced_technique(prompt: str, technique: str = "chain_of_thought")`
Applies advanced reasoning techniques to enhance prompt effectiveness.

**Parameters:**
- `prompt` (string): The original prompt
- `technique` (string): Technique to apply

**Available Techniques:**
- `chain_of_thought`: Step-by-step reasoning guidance
- `self_consistency`: Multiple reasoning paths approach
- `react`: Reason + Act iterative methodology
- `tree_of_thoughts`: Multi-path exploration technique

**Returns:**
- `original_prompt` (string): Original prompt
- `enhanced_prompt` (string): Prompt with technique applied
- `technique_applied` (string): Name of applied technique
- `technique_description` (string): Explanation of the technique
- `best_for` (string): Optimal use cases

**Example:**
```python
enhanced = apply_advanced_technique(
    "Solve this complex optimization problem",
    "tree_of_thoughts"
)
# Returns prompt with multi-path exploration guidance
```

### `check_bias(prompt: str)`
Detects potential biases in prompts and suggests mitigations.

**Parameters:**
- `prompt` (string): The prompt to check for biases

**Returns:**
- `biases_found` (array): List of detected biases
- `bias_score` (number): Overall bias risk score
- `mitigations` (array): Suggested mitigation strategies
- `inclusive_alternatives` (array): More inclusive phrasing options

**Bias Types Detected:**
- Gender bias (masculine/feminine language imbalance)
- Cultural assumptions
- Age-related stereotypes
- Professional stereotyping
- Geographical bias

**Example:**
```python
bias_check = check_bias("Ask the businessman to review this")
# Returns: biases_found: ["Gender bias"], mitigations: ["Use gender-neutral terms"]
```

## Supported Frameworks

### RACE Framework
- **Role**: Define the AI's role/persona
- **Action**: Specify what action to take
- **Context**: Provide relevant context
- **Expectation**: Set clear expectations for output

### TRACE Framework  
- **Task**: Define the specific task
- **Request**: Make a clear request
- **Action**: Specify required actions
- **Context**: Provide necessary context
- **Example**: Include relevant examples

### CRISPE Framework
- **Capacity/Role**: Define AI capability and role
- **Insight**: Provide relevant insights/background
- **Statement**: Clear problem statement
- **Personality**: Define desired tone/style
- **Experiment**: Encourage creative exploration

### CORE Framework
- **Context**: Essential background information
- **Objective**: Clear goal definition
- **Role**: AI's role in the task
- **Example**: Demonstrative examples

### COAST Framework
- **Context**: Situational background
- **Objective**: Clear objectives
- **Actions**: Required actions
- **Scenario**: Specific scenarios
- **Task**: Defined tasks

## Usage Examples

### Basic Optimization
```bash
# Start the server
python main.py prompt

# Optimize a simple prompt
optimize_prompt("Write code") 
# Returns enhanced prompt with role, context, and specific requirements
```

### Framework-Based Enhancement
```python
# Get framework recommendation
framework = suggest_framework("Create a marketing campaign for a SaaS product")
# Returns: CRISPE framework with creative components

# Apply the framework
optimized = optimize_prompt(
    "Create a marketing campaign for a SaaS product",
    task_type="creative",
    target_audience="marketing professionals"
)
```

### Advanced Reasoning Application
```python
# Apply Chain-of-Thought to complex problem
enhanced = apply_advanced_technique(
    "Design a distributed system architecture",
    "chain_of_thought"
)
# Returns prompt with step-by-step reasoning structure
```

### Bias Detection Workflow
```python
# Check for biases before using
bias_check = check_bias("Ask the developer to code this")
if bias_check["biases_found"]:
    print("Biases detected:", bias_check["biases_found"])
    print("Suggestions:", bias_check["mitigations"])
```

## Task Type Detection

The server automatically detects task types based on keywords:

- **Code Generation**: "code", "program", "function", "implement"
- **Analysis**: "analyze", "evaluate", "examine", "compare"
- **Creative**: "create", "invent", "story", "poem", "design"
- **Problem Solving**: "solve", "solution", "how to", "fix"
- **Question Answering**: "what is", "explain", "define", "describe"
- **Translation**: "translate", "to english", "convert language"
- **Summarization**: "summarize", "main points", "overview"

## Quality Metrics

The server evaluates prompts based on:

- **Clarity** (25 points): Specific language, adequate length
- **Context** (25 points): Background information, situational details
- **Objective** (25 points): Clear action verbs, defined goals
- **Structure** (25 points): Logical organization, framework adherence

## Configuration

Environment variables:
- `MCP_SERVER_PORT`: Server port (default: 3001)
- `MCP_SERVER_PROTOCOL`: Communication protocol (default: stdio)

## Dependencies

- **FastMCP**: 2.4.0+
- **Pydantic**: For data validation
- **Python**: 3.12+

## Performance

- **Optimization Speed**: < 50ms per prompt
- **Framework Detection**: Real-time task type identification
- **Bias Analysis**: Comprehensive scanning in < 100ms
- **Memory Efficient**: Minimal resource usage

---

*This server is part of the MCP Servers Collection developed by Charleno Pires*