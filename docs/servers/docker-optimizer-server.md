# 🐳 Docker Optimizer Server

**Server ID**: `docker`  
**Port**: 3010  
**Status**: ✅ **FUNCTIONAL**  
**Version**: 1.0.0

## 📖 Overview

The Docker Optimizer Server is an advanced MCP server designed for Docker containerization analysis, optimization, and best practices implementation following 2025 container security standards and multi-stage optimization patterns. It provides comprehensive Docker configuration generation, security assessment, and optimization recommendations for modern containerized applications.

## 🎯 Main Features

### 🔍 **Docker Analysis & Validation**
- **Prompt Analysis**: 0-100 scoring system for Docker creation prompts
- **Dockerfile Validation**: Security and optimization compliance checking
- **Best Practices Assessment**: Comprehensive evaluation against 2025 standards
- **Security Vulnerability Detection**: Identifies common security issues and risks

### 🛡️ **Security Best Practices**
- **Non-root User Execution**: Automatic UID 1000 user creation patterns
- **Minimal Base Images**: Alpine, slim, and distroless image recommendations  
- **Multi-stage Builds**: Intelligent layer optimization for size reduction
- **Vulnerability Scanning**: Integration patterns for security scanning tools

### ⚡ **Performance Optimization**
- **Layer Caching**: Smart command ordering for optimal cache utilization
- **Image Size Reduction**: 60-80% size reduction through multi-stage patterns
- **Build Speed Enhancement**: Dependency caching and parallel build strategies
- **Resource Management**: Memory and CPU optimization recommendations

### 🏗️ **Complete Configuration Generation**
- **Multi-stage Dockerfiles**: Production-ready container definitions
- **Docker Compose**: Service orchestration with health checks
- **Environment Templates**: Comprehensive .env and configuration examples
- **CI/CD Integration**: GitHub Actions and deployment pipeline templates

## 🛠️ Available Tools

### 1. `docker_analyze_prompt`
**Purpose**: Analyze Docker creation prompts and provide detailed feedback with scoring

**Parameters**:
- `prompt` (str): User's Docker creation prompt to analyze

**Returns**:
```json
{
  "analysis": {
    "score": 85,
    "strengths": [
      "Application type identified: PYTHON",
      "Mentions multi-stage builds for optimization",
      "Uses optimized base image"
    ],
    "weaknesses": [
      "Security considerations not mentioned"
    ],
    "missing_elements": [
      "Health check not specified"
    ],
    "recommendations": [
      "Add HEALTHCHECK directive for container monitoring",
      "Run containers as non-root user for enhanced security"
    ],
    "security_issues": [
      "Non-root user execution not specified"
    ]
  },
  "summary": "Score: 85/100 - Strengths: 3, Improvements: 2",
  "grade": "B"
}
```

**Use Cases**:
- Docker prompt quality assessment
- Security compliance validation
- Optimization opportunity identification

### 2. `docker_enhance_prompt`
**Purpose**: Enhance Docker prompts with comprehensive best practices and production-ready specifications

**Parameters**:
- `prompt` (str): Original user prompt to enhance
- `app_type` (str, optional): Application type (python, node, rust, go)
- `include_compose` (bool, optional): Include docker-compose template (default: true)
- `production_ready` (bool, optional): Optimize for production deployment (default: true)

**Returns**:
```json
{
  "original_prompt": "Create a Python app container",
  "enhanced_prompt": "# Original Request\nCreate a Python app container\n\n# ENHANCED REQUIREMENTS - PRODUCTION READY...",
  "dockerfile_template": "# Multi-stage Dockerfile for Python...",
  "docker_compose_template": "version: '3.9'\nservices:...",
  "added_elements": [
    "Multi-stage build architecture",
    "Security hardening practices", 
    "Layer optimization strategies"
  ],
  "app_type": "python",
  "estimated_size_reduction": "60-80% smaller than single-stage build"
}
```

**Use Cases**:
- Basic prompt enhancement with best practices
- Production-ready configuration generation
- Multi-stage build architecture design

### 3. `docker_validate_dockerfile`
**Purpose**: Validate existing Dockerfile against 2025 security and optimization best practices

**Parameters**:
- `dockerfile_content` (str): Dockerfile content to validate

**Returns**:
```json
{
  "valid": true,
  "score": 92,
  "security_grade": "HIGH",
  "issues": [],
  "warnings": [
    "⚠️ No HEALTHCHECK defined - important for container monitoring"
  ],
  "suggestions": [
    "💡 Add LABELs for image metadata and maintainer information"
  ],
  "summary": "Score: 92/100 - Security: HIGH - Issues: 0 - Warnings: 1",
  "lines_analyzed": 45,
  "multi_stage": true,
  "has_healthcheck": false,
  "runs_as_non_root": true
}
```

**Use Cases**:
- Existing Dockerfile security assessment
- Compliance validation before deployment
- Optimization opportunity identification

### 4. `docker_generate_config`
**Purpose**: Generate complete Docker configuration based on project requirements

**Parameters**:
- `project_description` (str): Description of the project and requirements
- `app_type` (str): Application type (python, node, rust, go)
- `features` (list[str], optional): Additional features (database, redis, nginx, monitoring)

**Returns**:
```json
{
  "dockerfile": "# Multi-stage production Dockerfile...",
  "docker_compose": "{\n  \"version\": \"3.9\",\n  \"services\": {...}",
  "dockerignore": "# Git\n.git\n.gitignore...",
  "env_example": "# Application Configuration\nNODE_ENV=production...",
  "setup_instructions": "# PYTHON Docker Setup Instructions...",
  "features_included": ["database", "redis"],
  "app_type": "python",
  "estimated_image_size": "~150MB (optimized multi-stage build)",
  "security_features": [
    "Non-root user execution",
    "Multi-stage builds",
    "Minimal attack surface"
  ]
}
```

**Use Cases**:
- Complete project containerization setup
- Production-ready configuration generation
- Multi-service application orchestration

## 🎯 Supported Technologies

### 📋 **Application Frameworks**
**Python Applications**:
- FastAPI, Django, Flask
- Base Image: `python:3.12-slim`
- Package Manager: pip
- Estimated Size: ~150MB

**Node.js Applications**:
- Express, Next.js, React
- Base Image: `node:22-alpine`
- Package Manager: npm
- Estimated Size: ~120MB

**Rust Applications**:
- Axum, Actix-web, Tokio
- Base Image: `rust:1.82-slim`
- Package Manager: cargo
- Estimated Size: ~50MB

**Go Applications**:
- Gin, Echo, standard library
- Base Image: `golang:1.24-alpine`
- Package Manager: go mod
- Estimated Size: ~30MB

### 🛡️ **Security Standards 2025**
**Container Security**:
- Non-root user execution (UID 1000)
- Minimal base images (Alpine, distroless, slim)
- Specific version tags (never 'latest')
- Comprehensive .dockerignore files

**Build Security**:
- Multi-stage builds for attack surface reduction
- Secrets management via environment variables
- Vulnerability scanning integration
- Layer optimization for security

**Runtime Security**:
- Health checks for monitoring
- Resource limits and constraints
- Network isolation patterns
- Signal handling for graceful shutdown

## 📋 Configuration & Setup

### Installation
```bash
# Install dependencies
uv sync

# Run Docker Optimizer server
uv run python main.py docker

# Alternative direct launch
uv run python -m servers.docker_optimizer_server
```

### Environment Variables
```bash
MCP_SERVER_PORT=3010        # Server port (default: 3010)
MCP_SERVER_PROTOCOL=stdio   # Protocol (default: stdio)
```

### Docker Best Practices Configuration
```json
{
  "security": {
    "non_root_user": "Always run containers as non-root user for security",
    "minimal_base": "Use minimal base images (alpine, distroless, slim)",
    "specific_versions": "Use specific versions instead of 'latest' tag"
  },
  "optimization": {
    "multi_stage": "Use multi-stage builds to reduce final image size",
    "layer_caching": "Order commands to optimize Docker layer caching",
    "clean_cache": "Clean package manager cache after installation"
  }
}
```

## 🧪 Testing & Quality Assurance

### Running Tests
```bash
# Run server-specific tests
uv run python run_tests.py docker_optimizer_server

# Run all tests with coverage
uv run pytest tests/ --cov=servers.docker_optimizer_server
```

### Quality Metrics
- **Prompt Analysis**: 0-100 scoring system with detailed feedback
- **Security Assessment**: HIGH/MEDIUM/LOW security grading
- **Optimization Analysis**: Multi-stage vs single-stage comparisons
- **Best Practices Compliance**: 2025 container standards validation

## 🚀 Performance & Scalability

### Performance Characteristics
- **Prompt Analysis**: ~200ms for typical Docker prompts
- **Dockerfile Validation**: ~150ms for standard Dockerfiles
- **Complete Config Generation**: ~400ms for full project setup
- **Memory Usage**: <50MB typical operation

### Scalability Features
- Async processing for concurrent analysis
- Template caching for faster generation
- Streaming responses for large configurations
- Resource pooling for external validations

## 🔧 Advanced Usage Examples

### Basic Docker Analysis
```python
# Analyze Docker prompt quality
analysis = await docker_analyze_prompt(
    "Create a Python FastAPI app with PostgreSQL database"
)

print(f"Score: {analysis['analysis']['score']}/100")
for recommendation in analysis['analysis']['recommendations']:
    print(f"- {recommendation}")
```

### Complete Project Setup
```python
# Generate full Docker configuration
config = await docker_generate_config(
    project_description="E-commerce API with caching",
    app_type="python",
    features=["database", "redis", "nginx"]
)

# Save generated files
with open("Dockerfile", "w") as f:
    f.write(config["dockerfile"])
with open("docker-compose.yml", "w") as f:
    f.write(config["docker_compose"])
```

### Dockerfile Security Validation
```python
# Validate existing Dockerfile
with open("Dockerfile", "r") as f:
    dockerfile_content = f.read()

validation = await docker_validate_dockerfile(dockerfile_content)

if validation["security_grade"] != "HIGH":
    print("Security improvements needed:")
    for issue in validation["issues"]:
        print(f"- {issue}")
```

## 🤝 Integration with Development Tools

### CI/CD Platforms
- **GitHub Actions**: Docker build and deployment workflows
- **GitLab CI**: Container registry integration patterns
- **Jenkins**: Pipeline templates for containerized applications
- **Azure DevOps**: Container deployment strategies

### Container Orchestration
- **Kubernetes**: Deployment manifest generation
- **Docker Swarm**: Service definition templates
- **Docker Compose**: Multi-service orchestration
- **Nomad**: Container scheduling patterns

### Security Tools
- **Trivy**: Vulnerability scanning integration
- **Docker Bench**: Security benchmark compliance
- **Snyk**: Container security monitoring
- **Clair**: Static analysis integration

## 📚 Related Documentation

- [Python Development Optimizer](python-development-optimizer.md) - Python application patterns
- [FastMCP Server](fastmcp-server.md) - FastMCP development patterns
- [React Optimizer Server](react-optimizer-server.md) - Frontend containerization
- [Rust Idiomatic Server](rust-idiomatic-server.md) - Rust application containers

## 🆕 Recent Updates

### Version 1.0.0 (Latest)
- ✅ **Production Ready**: Complete Docker 2025 standards support
- ✅ **Multi-stage Optimization**: 60-80% size reduction patterns
- ✅ **Security Hardening**: Non-root users, minimal images, vulnerability patterns
- ✅ **Complete Configuration**: Dockerfile + Compose + Environment templates
- ✅ **Framework Support**: Python, Node.js, Rust, Go application templates
- ✅ **Performance**: Optimized analysis and generation algorithms
- ✅ **Documentation**: Comprehensive setup and deployment guides

---

**🐳 Docker Optimizer Server** | **Status**: Production Ready | **Maintained by**: MCP Servers Team