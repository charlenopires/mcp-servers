#!/usr/bin/env python3
"""
Docker Optimizer MCP Server
===============================

Advanced MCP server for Docker containerization analysis, optimization, and best practices
implementation following 2025 container security standards and multi-stage optimization patterns.

Key Features:
- Docker prompt analysis with 0-100 scoring system
- Automatic prompt enhancement with production-ready specifications
- Security best practices: non-root users, minimal images, vulnerability scanning
- Multi-stage optimization: intelligent layer caching and size reduction
- Complete configuration generation: Dockerfile + docker-compose + .dockerignore
- Docker Compose orchestration with modern Compose Specification
- Health checks, networking, volumes, and service dependencies
- Production-ready configurations with security hardening

Supported Technologies:
- Python (FastAPI, Django, Flask, uv)
- Node.js (Express, Next.js, React, Bun)
- Rust (Axum, Actix, Tokio)
- Go (Gin, Echo, Fiber)
- Additional: PHP, Java, C#/.NET

Based on: Docker 2025 security standards, Compose Specification v3.9+, multi-stage build patterns, and container orchestration best practices
"""

import json
import logging
from enum import Enum
from typing import Any

from typing import Optional

from fastmcp import FastMCP, Context
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP(
    name="Docker Optimizer Server",
    instructions="""Advanced MCP server for Docker containerization analysis, optimization,
and best practices implementation following 2025 container security standards.

Features:
- Docker prompt analysis with 0-100 scoring system
- Automatic prompt enhancement with production-ready specifications
- Security best practices: non-root users, minimal images, vulnerability scanning
- Multi-stage optimization: intelligent layer caching and size reduction
- Complete configuration generation: Dockerfile + docker-compose + .dockerignore
- Docker Compose orchestration with modern Compose Specification

Use these tools for:
- docker_analyze_prompt: Analyze Docker creation prompts for quality
- docker_enhance_prompt: Transform basic prompts into production-ready specs
- docker_validate_compose: Validate docker-compose.yml files
- docker_validate_dockerfile: Validate Dockerfile against best practices
- docker_generate_compose_config: Generate Docker Compose configurations
- docker_generate_config: Generate complete Docker configuration

Use these prompts for:
- optimize_dockerfile: Get guidance on optimizing existing Dockerfiles
- design_compose_stack: Design multi-service Docker Compose stacks
- implement_multi_stage: Implement multi-stage builds for size reduction
- harden_security: Apply security hardening to containers
- setup_production_ready: Configure containers for production deployment""",
    version="3.0.0"
)

# ================================
# ENUMS & TYPES
# ================================

class ContainerFramework(Enum):
    """Supported container frameworks"""
    PYTHON = "python"
    NODE = "node"
    RUST = "rust"
    GO = "go"

class SecurityLevel(Enum):
    """Container security levels"""
    BASIC = "basic"
    STANDARD = "standard"
    HIGH = "high"
    ENTERPRISE = "enterprise"

# ================================
# PYDANTIC MODELS
# ================================

class DockerPromptAnalysis(BaseModel):
    """Model for Docker prompt analysis results"""

    score: int = Field(..., ge=0, le=100, description="Quality score from 0-100")
    strengths: list[str] = Field(default_factory=list, description="Identified strong points")
    weaknesses: list[str] = Field(default_factory=list, description="Identified weak points")
    missing_elements: list[str] = Field(default_factory=list, description="Missing essential elements")
    recommendations: list[str] = Field(default_factory=list, description="Improvement recommendations")
    security_issues: list[str] = Field(default_factory=list, description="Security-related issues")

class DockerRequirements(BaseModel):
    """Model for Docker requirements analysis"""

    app_type: str = Field(description="Application type (node, python, rust, etc)")
    base_image: str | None = Field(None, description="Specified base image")
    has_multistage: bool = Field(default=False, description="Uses multi-stage build")
    has_security: bool = Field(default=False, description="Mentions security practices")
    has_optimization: bool = Field(default=False, description="Mentions optimization")
    has_healthcheck: bool = Field(default=False, description="Includes healthcheck")
    has_non_root_user: bool = Field(default=False, description="Uses non-root user")

class EnhancedDockerPrompt(BaseModel):
    """Model for enhanced Docker prompt results"""

    original_prompt: str = Field(description="Original user prompt")
    enhanced_prompt: str = Field(description="Enhanced prompt with best practices")
    added_elements: list[str] = Field(description="Elements added during enhancement")
    dockerfile_template: str = Field(description="Generated Dockerfile template")
    docker_compose_template: str | None = Field(None, description="Generated docker-compose template")

# ================================
# KNOWLEDGE BASE - DOCKER BEST PRACTICES 2025
# ================================

DOCKER_BEST_PRACTICES = {
    "security": {
        "non_root_user": "Always run containers as non-root user for security",
        "minimal_base": "Use minimal base images (alpine, distroless, slim)",
        "no_secrets": "Never include secrets or tokens in Dockerfile",
        "scan_vulnerabilities": "Scan images for vulnerabilities regularly",
        "specific_versions": "Use specific versions instead of 'latest' tag",
        "dockerignore": "Always use .dockerignore to exclude unnecessary files",
    },
    "optimization": {
        "multi_stage": "Use multi-stage builds to reduce final image size",
        "layer_caching": "Order commands to optimize Docker layer caching",
        "combine_run": "Combine RUN commands when possible to reduce layers",
        "clean_cache": "Clean package manager cache after installation",
        "minimal_deps": "Install only necessary dependencies",
    },
    "best_practices": {
        "healthcheck": "Always include HEALTHCHECK directive",
        "labels": "Use LABEL for metadata and documentation",
        "workdir": "Use WORKDIR instead of cd commands",
        "copy_vs_add": "Prefer COPY over ADD for better predictability",
        "entrypoint_cmd": "Use ENTRYPOINT + CMD appropriately",
    },
}

# Application-specific templates with 2025 updates
APP_TEMPLATES = {
    "python": {
        "base_image": "python:3.12-slim",
        "builder_image": "python:3.12-slim",
        "runtime_image": "python:3.12-slim",
        "dev_deps": ["gcc", "python3-dev", "pkg-config"],
        "package_manager": "uv",  # Modern Python package manager
        "package_file": "pyproject.toml",
        "port": 8000,
        "health_endpoint": "/health",
        "user": "appuser",
        "workdir": "/app",
    },
    "node": {
        "base_image": "node:22-alpine",
        "builder_image": "node:22-alpine",
        "runtime_image": "node:22-alpine",
        "dev_deps": ["build-base", "python3", "make"],
        "package_manager": "npm",
        "package_file": "package*.json",
        "port": 3000,
        "health_endpoint": "/health",
        "user": "node",
        "workdir": "/app",
    },
    "rust": {
        "base_image": "rust:1.83-slim-bookworm",
        "builder_image": "rust:1.83-slim-bookworm",
        "runtime_image": "debian:bookworm-slim",
        "dev_deps": ["gcc", "pkg-config", "libssl-dev", "ca-certificates"],
        "package_manager": "cargo",
        "package_file": "Cargo.toml",
        "port": 8080,
        "health_endpoint": "/health",
        "user": "appuser",
        "workdir": "/app",
    },
    "go": {
        "base_image": "golang:1.23-alpine",
        "builder_image": "golang:1.23-alpine",
        "runtime_image": "alpine:latest",
        "dev_deps": ["gcc", "musl-dev", "ca-certificates"],
        "package_manager": "go mod",
        "package_file": "go.mod",
        "port": 8080,
        "health_endpoint": "/health",
        "user": "appuser",
        "workdir": "/app",
    },
}

# ================================
# MCP TOOLS
# ================================

@mcp.tool(tags=["analysis", "prompt", "scoring"])
async def docker_analyze_prompt(prompt: str, ctx: Optional[Context] = None) -> dict[str, Any]:
    """
    Analyze a Docker creation prompt and provide detailed feedback with scoring.

    Evaluates prompts based on:
    - Application type identification and clarity
    - Security considerations and best practices
    - Multi-stage build patterns and optimization
    - Health checks and monitoring setup
    - Production readiness indicators

    Args:
        prompt: User's Docker creation prompt to analyze

    Returns:
        Comprehensive analysis with score, strengths, weaknesses, and recommendations
    """
    logger.info(f"Analyzing Docker prompt: {prompt[:100]}...")

    score = 0
    strengths = []
    weaknesses = []
    missing_elements = []
    recommendations = []
    security_issues = []

    prompt_lower = prompt.lower()

    # Application type detection
    app_type = None
    app_keywords = {
        "python": ["python", "django", "flask", "fastapi", "pip", "requirements.txt"],
        "node": ["node", "npm", "yarn", "react", "next", "express", "javascript"],
        "rust": ["rust", "cargo", "axum", "actix", "tokio"],
        "go": ["golang", "go ", "gin", "echo", "go.mod"],
    }

    for app, keywords in app_keywords.items():
        if any(kw in prompt_lower for kw in keywords):
            app_type = app
            strengths.append(f"Application type identified: {app.upper()}")
            score += 10
            break

    if not app_type:
        weaknesses.append("Application type not clearly specified")
        recommendations.append("Specify the application type (Python, Node.js, Rust, Go)")

    # Multi-stage build analysis
    if any(term in prompt_lower for term in ["multi-stage", "multistage", "multi stage"]):
        strengths.append("Mentions multi-stage builds for optimization")
        score += 15
    else:
        missing_elements.append("Multi-stage builds not mentioned")
        recommendations.append("Use multi-stage builds to reduce final image size by 60-80%")

    # Base image optimization
    minimal_images = ["alpine", "slim", "distroless"]
    if any(img in prompt_lower for img in minimal_images):
        strengths.append("Uses optimized base image")
        score += 10
    else:
        recommendations.append("Consider using minimal base images (alpine, slim, distroless)")

    # Security considerations
    if any(term in prompt_lower for term in ["security", "secure", "non-root", "user"]):
        strengths.append("Considers security aspects")
        score += 10
    else:
        security_issues.append("Security considerations not mentioned")

    if any(term in prompt_lower for term in ["non-root", "user ", "uid ", "gid "]):
        strengths.append("Mentions non-root user execution")
        score += 10
    else:
        security_issues.append("Non-root user execution not specified")
        recommendations.append("Run containers as non-root user for enhanced security")

    # Health check analysis
    if any(term in prompt_lower for term in ["healthcheck", "health check", "health"]):
        strengths.append("Includes health check configuration")
        score += 10
    else:
        missing_elements.append("Health check not specified")
        recommendations.append("Add HEALTHCHECK directive for container monitoring")

    # Optimization indicators
    if any(term in prompt_lower for term in ["optimize", "cache", "layer", "size"]):
        strengths.append("Considers optimization and caching")
        score += 10

    # Docker Compose integration
    if any(term in prompt_lower for term in ["docker-compose", "compose", "orchestration"]):
        strengths.append("Includes Docker Compose for orchestration")
        score += 10
    else:
        recommendations.append("Consider including docker-compose.yml for service orchestration")

    # Modern Docker features
    modern_features = ["buildkit", "multi-platform", "secrets", "configs", "networks"]
    if any(feat in prompt_lower for feat in modern_features):
        strengths.append("Uses modern Docker features")
        score += 5

    # Compose Specification features
    compose_features = ["profiles", "depends_on", "healthcheck", "volumes", "networks"]
    compose_score = sum(1 for feat in compose_features if feat in prompt_lower)
    if compose_score > 2:
        strengths.append("Good Docker Compose feature coverage")
        score += compose_score * 2

    # Production readiness
    if any(term in prompt_lower for term in ["production", "prod", "deploy"]):
        strengths.append("Production-oriented approach")
        score += 15

    # Environment variables and configuration
    if any(term in prompt_lower for term in [".env", "environment", "config"]):
        strengths.append("Considers environment configuration")
        score += 5

    # Adjust final score
    score = min(100, max(20, score))  # Keep between 20-100

    analysis = DockerPromptAnalysis(
        score=score,
        strengths=strengths,
        weaknesses=weaknesses,
        missing_elements=missing_elements,
        recommendations=recommendations,
        security_issues=security_issues,
    )

    return {
        "analysis": analysis.model_dump(),
        "summary": f"Score: {score}/100 - Strengths: {len(strengths)}, Improvements: {len(recommendations)}",
        "grade": "A" if score >= 90 else "B" if score >= 75 else "C" if score >= 60 else "D",
    }

@mcp.tool(tags=["enhancement", "generation", "production"])
async def docker_enhance_prompt(
    prompt: str,
    app_type: str | None = None,
    include_compose: bool = True,
    production_ready: bool = True,
    ctx: Optional[Context] = None,
) -> dict[str, Any]:
    """
    Enhance a Docker prompt with comprehensive best practices and production-ready specifications.

    Transforms basic prompts into detailed specifications including:
    - Multi-stage build architecture
    - Security hardening practices
    - Performance optimization techniques
    - Health monitoring and logging
    - Production deployment considerations

    Args:
        prompt: Original user prompt to enhance
        app_type: Application type (python, node, rust, go)
        include_compose: Include docker-compose template
        production_ready: Optimize for production deployment

    Returns:
        Enhanced prompt with templates and implementation guide
    """
    logger.info(f"Enhancing Docker prompt for {app_type or 'auto-detect'}")

    # Auto-detect application type if not specified
    if not app_type:
        prompt_lower = prompt.lower()
        for app in ["python", "node", "rust", "go"]:
            if app in prompt_lower:
                app_type = app
                break
        if not app_type:
            app_type = "python"  # Default fallback

    # Build enhanced prompt sections
    enhanced_sections = [
        f"# Original Request\n{prompt}\n",
        "\n# ENHANCED REQUIREMENTS - PRODUCTION READY\n",
        f"## Application Type: {app_type.upper()}\n",

        "\n## Multi-Stage Dockerfile Architecture:\n",
        "### Stage 1 (Builder):\n",
        "- Install build dependencies and compile/build application\n",
        "- Cache dependencies for faster rebuilds\n",
        "- Compile assets and prepare production artifacts\n",

        "\n### Stage 2 (Production):\n",
        "- Use minimal production base image\n",
        "- Copy only production artifacts from builder\n",
        "- Configure non-root user execution\n",
        "- Set up health checks and monitoring\n",

        "\n## Security Requirements:\n",
        "- ✅ Execute as non-root user (UID 1000)\n",
        "- ✅ Use specific version tags, never 'latest'\n",
        "- ✅ Minimal attack surface with slim/alpine images\n",
        "- ✅ No secrets or credentials in image layers\n",
        "- ✅ Comprehensive .dockerignore file\n",
        "- ✅ Security scanning integration\n",

        "\n## Optimization Strategies:\n",
        "- ✅ Layer ordering for maximum cache efficiency\n",
        "- ✅ Combined RUN commands to minimize layers\n",
        "- ✅ Package manager cache cleanup\n",
        "- ✅ Multi-stage builds for 60-80% size reduction\n",
        "- ✅ Dependency caching strategies\n",

        "\n## Production Best Practices:\n",
        "- ✅ Health check endpoints and Docker HEALTHCHECK\n",
        "- ✅ Proper signal handling for graceful shutdown\n",
        "- ✅ Resource limits and monitoring\n",
        "- ✅ Logging configuration and structured output\n",
        "- ✅ Environment-based configuration\n",
    ]

    # Generate Dockerfile template
    dockerfile_template = generate_dockerfile_template(app_type, production_ready)

    # Generate docker-compose if requested
    docker_compose_template = None
    if include_compose:
        docker_compose_template = generate_docker_compose_template(app_type)
        enhanced_sections.extend([
            "\n## Docker Compose Architecture (Compose Specification):\n",
            "- ✅ Service orchestration with dependency management\n",
            "- ✅ Custom networks for service isolation\n",
            "- ✅ Named volumes for data persistence\n",
            "- ✅ Environment variable configuration\n",
            "- ✅ Health checks and restart policies\n",
            "- ✅ Resource limits and logging configuration\n",
            "- ✅ Development and production profiles\n",
            "- ✅ Modern Compose Specification (no version field)\n"
        ])

    enhanced_prompt = "".join(enhanced_sections)

    return {
        "original_prompt": prompt,
        "enhanced_prompt": enhanced_prompt,
        "dockerfile_template": dockerfile_template,
        "docker_compose_template": docker_compose_template,
        "added_elements": [
            "Multi-stage build architecture",
            "Security hardening practices",
            "Build cache optimization with --mount",
            "Health check configuration",
            "Non-root user setup",
            "OCI-compliant metadata labels",
            "Production monitoring setup",
            "Modern Compose Specification",
        ],
        "app_type": app_type,
        "estimated_size_reduction": "60-80% smaller than single-stage build",
        "compose_specification_compliant": True,
        "dockerfile_syntax_version": "1.7"
    }

@mcp.tool(tags=["validation", "compose", "security"])
async def docker_validate_compose(
    compose_content: str,
    check_security: bool = True,
    check_performance: bool = True,
    ctx: Optional[Context] = None,
) -> dict[str, Any]:
    """
    Validate a docker-compose.yml file against modern best practices and Compose Specification.

    Performs comprehensive validation including:
    - Compose Specification compliance
    - Service configuration best practices
    - Security hardening validation
    - Performance optimization checks
    - Network and volume configuration
    - Health check validation

    Args:
        compose_content: docker-compose.yml content to validate
        check_security: Enable security validation rules
        check_performance: Enable performance optimization checks

    Returns:
        Validation report with issues, warnings, suggestions, and compliance score
    """
    logger.info("Validating docker-compose.yml against modern best practices")

    import yaml

    issues = []
    warnings = []
    suggestions = []
    score = 100

    try:
        compose_data = yaml.safe_load(compose_content)
    except yaml.YAMLError as e:
        return {
            "valid": False,
            "score": 0,
            "issues": [f"❌ YAML parsing error: {str(e)}"],
            "warnings": [],
            "suggestions": [],
            "summary": "Invalid YAML format"
        }

    # Check for required top-level elements
    if not isinstance(compose_data, dict):
        issues.append("❌ Root element must be a dictionary")
        score -= 30

    if "services" not in compose_data:
        issues.append("❌ CRITICAL: No 'services' section found")
        score -= 50

    # Compose Specification version check
    if "version" in compose_data:
        version = compose_data["version"]
        if isinstance(version, str) and version.startswith("2."):
            warnings.append("⚠️ Using legacy Compose v2.x format - consider upgrading to Compose Specification")
            score -= 5

    # Check for modern Compose Specification features
    if "name" not in compose_data:
        suggestions.append("💡 Add 'name' field for project naming (Compose Specification)")

    services = compose_data.get("services", {})

    for service_name, service_config in services.items():
        if not isinstance(service_config, dict):
            issues.append(f"❌ Service '{service_name}' configuration must be a dictionary")
            score -= 10
            continue

        # Health check validation
        if "healthcheck" not in service_config:
            warnings.append(f"⚠️ Service '{service_name}' missing healthcheck")
            score -= 3

        # Resource limits
        if "deploy" not in service_config or "resources" not in service_config.get("deploy", {}):
            warnings.append(f"⚠️ Service '{service_name}' missing resource limits")
            score -= 5

        # Security checks
        if check_security:
            # Check for privileged mode
            if service_config.get("privileged") is True:
                issues.append(f"❌ SECURITY: Service '{service_name}' running in privileged mode")
                score -= 20

            # Check user specification
            if "user" not in service_config and service_config.get("image", "").startswith(("ubuntu", "debian", "centos")):
                warnings.append(f"⚠️ SECURITY: Service '{service_name}' may be running as root")
                score -= 5

            # Check for exposed sensitive ports
            ports = service_config.get("ports", [])
            sensitive_ports = ["22", "3389", "5432", "3306", "27017", "6379"]
            for port_mapping in ports:
                if isinstance(port_mapping, str) and any(sp in port_mapping for sp in sensitive_ports):
                    warnings.append(f"⚠️ SECURITY: Service '{service_name}' exposing sensitive port {port_mapping}")
                    score -= 3

        # Performance checks
        if check_performance:
            # Check for restart policy
            if "restart" not in service_config:
                suggestions.append(f"💡 Service '{service_name}' should specify restart policy")

            # Check for logging configuration
            if "logging" not in service_config:
                suggestions.append(f"💡 Service '{service_name}' should configure logging limits")

            # Check for build cache optimization
            if "build" in service_config:
                build_config = service_config["build"]
                if isinstance(build_config, dict):
                    if "cache_from" not in build_config:
                        suggestions.append(f"💡 Service '{service_name}' build could benefit from cache optimization")

    # Network configuration validation
    networks = compose_data.get("networks", {})
    if not networks and len(services) > 1:
        suggestions.append("💡 Consider defining custom networks for service isolation")

    for network_name, network_config in networks.items():
        if isinstance(network_config, dict) and network_config.get("driver") == "bridge":
            if "ipam" not in network_config:
                suggestions.append(f"💡 Network '{network_name}' could benefit from explicit IPAM configuration")

    # Volume validation
    volumes = compose_data.get("volumes", {})
    for volume_name, volume_config in volumes.items():
        if volume_config is None:
            suggestions.append(f"💡 Volume '{volume_name}' using default local driver - consider explicit configuration")

    # Profile usage check
    has_profiles = any("profiles" in service for service in services.values())
    if not has_profiles and len(services) > 2:
        suggestions.append("💡 Consider using profiles for different deployment scenarios")

    # Final score adjustment
    score = max(0, score)

    # Determine validation status
    is_valid = len(issues) == 0
    compliance_grade = "HIGH" if score >= 90 else "MEDIUM" if score >= 70 else "LOW"

    return {
        "valid": is_valid,
        "score": score,
        "compliance_grade": compliance_grade,
        "issues": issues,
        "warnings": warnings,
        "suggestions": suggestions,
        "summary": f"Score: {score}/100 - Compliance: {compliance_grade} - Issues: {len(issues)} - Warnings: {len(warnings)}",
        "services_analyzed": len(services),
        "has_healthchecks": sum(1 for s in services.values() if "healthcheck" in s),
        "has_resource_limits": sum(1 for s in services.values() if "deploy" in s and "resources" in s.get("deploy", {})),
        "uses_profiles": has_profiles,
        "compose_specification_compliant": "name" in compose_data and "version" not in compose_data
    }

@mcp.tool(tags=["validation", "dockerfile", "security"])
async def docker_validate_dockerfile(dockerfile_content: str, ctx: Optional[Context] = None) -> dict[str, Any]:
    """
    Validate an existing Dockerfile against 2025 security and optimization best practices.

    Performs comprehensive analysis including:
    - Security vulnerability assessment
    - Layer optimization evaluation
    - Best practices compliance check
    - Performance optimization opportunities
    - Production readiness validation

    Args:
        dockerfile_content: Dockerfile content to validate

    Returns:
        Validation report with issues, warnings, and improvement suggestions
    """
    logger.info("Validating Dockerfile against 2025 best practices")

    issues = []
    warnings = []
    suggestions = []
    score = 100

    lines = dockerfile_content.split("\n")
    stripped_lines = [line.strip() for line in lines if line.strip()]

    # Critical security checks
    has_user = any("USER" in line and "root" not in line for line in stripped_lines)
    if not has_user:
        issues.append("❌ CRITICAL: Container running as root - major security risk")
        score -= 25

    # Check for latest tags
    for line in stripped_lines:
        if line.startswith("FROM") and ":latest" in line:
            issues.append("❌ Using ':latest' tag - use specific versions for reproducibility")
            score -= 15

    # Multi-stage build analysis
    from_count = sum(1 for line in stripped_lines if line.startswith("FROM"))
    if from_count < 2:
        warnings.append("⚠️ Single-stage build detected - consider multi-stage for size optimization")
        score -= 10
    else:
        suggestions.append("✅ Multi-stage build detected - good for optimization")

    # Health check validation
    if not any("HEALTHCHECK" in line for line in stripped_lines):
        warnings.append("⚠️ No HEALTHCHECK defined - important for container monitoring")
        score -= 10

    # Security best practices
    if any("ADD " in line for line in stripped_lines):
        warnings.append("⚠️ Using ADD instead of COPY - COPY is more predictable")
        score -= 5

    # Package manager cache cleanup
    apt_installs = [line for line in stripped_lines if "apt-get install" in line]
    for line in apt_installs:
        if "rm -rf /var/lib/apt/lists/*" not in line:
            warnings.append("⚠️ apt cache not cleaned after installation")
            score -= 5

    # Layer optimization
    run_count = sum(1 for line in stripped_lines if line.startswith("RUN"))
    if run_count > 5:
        suggestions.append("💡 Consider combining some RUN commands to reduce layers")

    # Non-root user validation
    if has_user:
        user_lines = [line for line in stripped_lines if line.startswith("USER")]
        if user_lines:
            user_line = user_lines[0]
            if "0" in user_line or "root" in user_line:
                issues.append("❌ USER directive specifies root user")
                score -= 20

    # Working directory check
    if not any(line.startswith("WORKDIR") for line in stripped_lines):
        warnings.append("⚠️ No WORKDIR specified - consider setting explicit working directory")
        score -= 3

    # Port exposure
    if not any(line.startswith("EXPOSE") for line in stripped_lines):
        suggestions.append("💡 Consider adding EXPOSE directive for documentation")

    # Label usage for metadata
    if not any(line.startswith("LABEL") for line in stripped_lines):
        suggestions.append("💡 Add LABELs for image metadata and maintainer information")

    # Final score adjustment
    score = max(0, score)

    # Determine validation status
    is_valid = len(issues) == 0
    security_grade = "HIGH" if score >= 90 else "MEDIUM" if score >= 70 else "LOW"

    return {
        "valid": is_valid,
        "score": score,
        "security_grade": security_grade,
        "issues": issues,
        "warnings": warnings,
        "suggestions": suggestions,
        "summary": f"Score: {score}/100 - Security: {security_grade} - Issues: {len(issues)} - Warnings: {len(warnings)}",
        "lines_analyzed": len(stripped_lines),
        "multi_stage": from_count > 1,
        "has_healthcheck": any("HEALTHCHECK" in line for line in stripped_lines),
        "runs_as_non_root": has_user
    }

@mcp.tool(tags=["generation", "compose", "production"])
async def docker_generate_compose_config(
    app_type: str,
    services: list[str] | None = None,
    environment: str = "production",
    include_volumes: bool = True,
    include_networks: bool = True,
    ctx: Optional[Context] = None,
) -> dict[str, Any]:
    """
    Generate comprehensive Docker Compose configuration with modern Compose Specification.

    Creates production-ready docker-compose.yml including:
    - Service definitions with health checks
    - Custom networks with proper isolation
    - Named volumes for data persistence
    - Environment variable configuration
    - Development and production profiles
    - Service dependencies and startup order

    Args:
        app_type: Application type (python, node, rust, go)
        services: Additional services (postgres, redis, nginx, monitoring)
        environment: Target environment (development, production, testing)
        include_volumes: Include volume definitions
        include_networks: Include custom network configuration

    Returns:
        Complete Docker Compose configuration with best practices
    """
    logger.info(f"Generating Docker Compose configuration for {app_type}")

    services = services or []
    template = APP_TEMPLATES.get(app_type, APP_TEMPLATES["python"])

    # Base compose structure following Compose Specification
    compose_config = {
        "name": f"{app_type}-stack",
        "services": {},
        "networks": {},
        "volumes": {},
        "configs": {},
        "secrets": {}
    }

    # Main application service
    compose_config["services"]["app"] = {
        "build": {
            "context": ".",
            "dockerfile": "Dockerfile",
            "target": "production",
            "args": {
                "BUILDKIT_INLINE_CACHE": "1"
            }
        },
        "image": f"{app_type}-app:latest",
        "container_name": f"{app_type}_app",
        "restart": "unless-stopped",
        "user": template["user"],
        "working_dir": template["workdir"],
        "ports": [
            f"${{{app_type.upper()}_PORT:-{template['port']}}}:{template['port']}"
        ],
        "environment": {
            "NODE_ENV": "${NODE_ENV:-production}",
            "LOG_LEVEL": "${LOG_LEVEL:-info}",
            "APP_ENV": environment
        },
        "env_file": [".env"],
        "networks": ["app-network"],
        "volumes": [
            "./logs:/app/logs"
        ] if include_volumes else [],
        "healthcheck": {
            "test": ["CMD", "curl", "-f", f"http://localhost:{template['port']}{template['health_endpoint']}"],
            "interval": "30s",
            "timeout": "10s",
            "retries": 3,
            "start_period": "40s"
        },
        "logging": {
            "driver": "json-file",
            "options": {
                "max-size": "10m",
                "max-file": "3",
                "compress": "true"
            }
        },
        "deploy": {
            "resources": {
                "limits": {
                    "cpus": "0.50",
                    "memory": "512M"
                },
                "reservations": {
                    "cpus": "0.25",
                    "memory": "256M"
                }
            },
            "restart_policy": {
                "condition": "on-failure",
                "delay": "5s",
                "max_attempts": 3,
                "window": "120s"
            }
        },
        "profiles": [environment]
    }

    # Add additional services
    if "postgres" in services or "database" in services:
        compose_config["services"]["postgres"] = {
            "image": "postgres:16-alpine",
            "container_name": "postgres_db",
            "restart": "unless-stopped",
            "environment": {
                "POSTGRES_DB": "${DB_NAME:-appdb}",
                "POSTGRES_USER": "${DB_USER:-appuser}",
                "POSTGRES_PASSWORD": "${DB_PASSWORD}",
                "POSTGRES_INITDB_ARGS": "--auth-host=scram-sha-256",
                "POSTGRES_HOST_AUTH_METHOD": "scram-sha-256"
            },
            "volumes": [
                "postgres_data:/var/lib/postgresql/data",
                "./docker/postgres/init.sql:/docker-entrypoint-initdb.d/init.sql:ro"
            ] if include_volumes else [],
            "networks": ["app-network"],
            "healthcheck": {
                "test": ["CMD-SHELL", "pg_isready -U ${DB_USER:-appuser} -d ${DB_NAME:-appdb}"],
                "interval": "10s",
                "timeout": "5s",
                "retries": 5,
                "start_period": "30s"
            },
            "deploy": {
                "resources": {
                    "limits": {
                        "memory": "256M"
                    }
                }
            },
            "profiles": [environment]
        }

        # Add database volume
        if include_volumes:
            compose_config["volumes"]["postgres_data"] = {"driver": "local"}

        # Add dependency to main app
        compose_config["services"]["app"]["depends_on"] = {
            "postgres": {
                "condition": "service_healthy",
                "restart": True
            }
        }

    if "redis" in services:
        compose_config["services"]["redis"] = {
            "image": "redis:7-alpine",
            "container_name": "redis_cache",
            "restart": "unless-stopped",
            "command": "redis-server --appendonly yes --requirepass ${REDIS_PASSWORD:-}",
            "volumes": [
                "redis_data:/data",
                "./docker/redis/redis.conf:/etc/redis/redis.conf:ro"
            ] if include_volumes else [],
            "networks": ["app-network"],
            "healthcheck": {
                "test": ["CMD", "redis-cli", "--raw", "incr", "ping"],
                "interval": "10s",
                "timeout": "3s",
                "retries": 5
            },
            "deploy": {
                "resources": {
                    "limits": {
                        "memory": "128M"
                    }
                }
            },
            "profiles": [environment]
        }

        if include_volumes:
            compose_config["volumes"]["redis_data"] = {"driver": "local"}

    if "nginx" in services:
        compose_config["services"]["nginx"] = {
            "image": "nginx:alpine",
            "container_name": "nginx_proxy",
            "restart": "unless-stopped",
            "ports": ["80:80", "443:443"],
            "volumes": [
                "./docker/nginx/nginx.conf:/etc/nginx/nginx.conf:ro",
                "./docker/nginx/conf.d:/etc/nginx/conf.d:ro",
                "./docker/nginx/ssl:/etc/nginx/ssl:ro",
                "nginx_logs:/var/log/nginx"
            ] if include_volumes else [],
            "networks": ["app-network"],
            "depends_on": {
                "app": {
                    "condition": "service_healthy",
                    "restart": True
                }
            },
            "healthcheck": {
                "test": ["CMD", "curl", "-f", "http://localhost:80/nginx-health"],
                "interval": "30s",
                "timeout": "10s",
                "retries": 3
            },
            "profiles": [environment]
        }

        if include_volumes:
            compose_config["volumes"]["nginx_logs"] = {"driver": "local"}

    # Add monitoring stack
    if "monitoring" in services:
        # Prometheus
        compose_config["services"]["prometheus"] = {
            "image": "prom/prometheus:latest",
            "container_name": "prometheus",
            "restart": "unless-stopped",
            "ports": ["9090:9090"],
            "volumes": [
                "./docker/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml:ro",
                "prometheus_data:/prometheus"
            ] if include_volumes else [],
            "networks": ["monitoring-network"],
            "command": [
                "--config.file=/etc/prometheus/prometheus.yml",
                "--storage.tsdb.path=/prometheus",
                "--web.console.libraries=/etc/prometheus/console_libraries",
                "--web.console.templates=/etc/prometheus/consoles",
                "--storage.tsdb.retention.time=200h",
                "--web.enable-lifecycle"
            ],
            "profiles": ["monitoring", environment]
        }

        # Grafana
        compose_config["services"]["grafana"] = {
            "image": "grafana/grafana:latest",
            "container_name": "grafana",
            "restart": "unless-stopped",
            "ports": ["3001:3000"],
            "environment": {
                "GF_SECURITY_ADMIN_PASSWORD": "${GRAFANA_PASSWORD:-admin}"
            },
            "volumes": [
                "grafana_data:/var/lib/grafana",
                "./docker/grafana/provisioning:/etc/grafana/provisioning"
            ] if include_volumes else [],
            "networks": ["monitoring-network"],
            "depends_on": ["prometheus"],
            "profiles": ["monitoring", environment]
        }

        if include_volumes:
            compose_config["volumes"]["prometheus_data"] = {"driver": "local"}
            compose_config["volumes"]["grafana_data"] = {"driver": "local"}

    # Network configuration
    if include_networks:
        compose_config["networks"]["app-network"] = {
            "driver": "bridge",
            "ipam": {
                "config": [
                    {"subnet": "172.20.0.0/16"}
                ]
            },
            "labels": {
                "com.example.description": "Main application network"
            }
        }

        if "monitoring" in services:
            compose_config["networks"]["monitoring-network"] = {
                "driver": "bridge",
                "ipam": {
                    "config": [
                        {"subnet": "172.21.0.0/16"}
                    ]
                }
            }

    # Clean up empty sections
    if not compose_config["volumes"]:
        del compose_config["volumes"]
    if not compose_config["configs"]:
        del compose_config["configs"]
    if not compose_config["secrets"]:
        del compose_config["secrets"]

    return {
        "compose_config": compose_config,
        "yaml_content": generate_compose_yaml(compose_config),
        "services_included": list(compose_config["services"].keys()),
        "features": {
            "health_checks": True,
            "resource_limits": True,
            "logging_config": True,
            "restart_policies": True,
            "profiles": True,
            "networks": include_networks,
            "volumes": include_volumes
        },
        "environment": environment,
        "compose_version": "3.9+"
    }

@mcp.tool(tags=["generation", "complete", "production"])
async def docker_generate_config(
    project_description: str,
    app_type: str,
    features: list[str] | None = None,
    ctx: Optional[Context] = None,
) -> dict[str, Any]:
    """
    Generate complete Docker configuration based on project requirements.

    Creates production-ready configuration including:
    - Optimized multi-stage Dockerfile
    - Docker Compose with service orchestration
    - Environment configuration templates
    - Security-hardened setup
    - Development and production profiles

    Args:
        project_description: Description of the project and requirements
        app_type: Application type (python, node, rust, go)
        features: Additional features (database, redis, nginx, monitoring)

    Returns:
        Complete Docker configuration with setup instructions
    """
    logger.info(f"Generating comprehensive Docker configuration for {app_type}")

    features = features or []

    # Generate optimized Dockerfile
    dockerfile = generate_dockerfile_template(app_type, production_ready=True)

    # Build docker-compose services
    services = {
        "app": {
            "build": {
                "context": ".",
                "dockerfile": "Dockerfile",
                "target": "production"
            },
            "container_name": f"{app_type}_app",
            "restart": "unless-stopped",
            "environment": [
                "NODE_ENV=${NODE_ENV:-production}",
                "LOG_LEVEL=${LOG_LEVEL:-info}",
            ],
            "networks": ["app-network"],
            "healthcheck": {
                "test": ["CMD", "curl", "-f", f"http://localhost:{APP_TEMPLATES[app_type]['port']}/health"],
                "interval": "30s",
                "timeout": "10s",
                "retries": 3,
                "start_period": "40s",
            },
            "logging": {
                "driver": "json-file",
                "options": {
                    "max-size": "10m",
                    "max-file": "3"
                }
            }
        }
    }

    # Add feature-specific services
    if "database" in features or "postgres" in features:
        services["postgres"] = {
            "image": "postgres:17-alpine",
            "container_name": "postgres_db",
            "restart": "unless-stopped",
            "environment": [
                "POSTGRES_DB=${DB_NAME:-appdb}",
                "POSTGRES_USER=${DB_USER:-appuser}",
                "POSTGRES_PASSWORD=${DB_PASSWORD}",
            ],
            "volumes": [
                "postgres_data:/var/lib/postgresql/data",
                "./docker/postgres/init.sql:/docker-entrypoint-initdb.d/init.sql:ro"
            ],
            "networks": ["app-network"],
            "healthcheck": {
                "test": ["CMD-SHELL", "pg_isready -U ${DB_USER:-appuser}"],
                "interval": "10s",
                "timeout": "5s",
                "retries": 5,
            },
        }
        services["app"]["depends_on"] = {
            "postgres": {"condition": "service_healthy"}
        }

    if "redis" in features:
        services["redis"] = {
            "image": "redis:7-alpine",
            "container_name": "redis_cache",
            "restart": "unless-stopped",
            "command": "redis-server --appendonly yes --requirepass ${REDIS_PASSWORD}",
            "volumes": ["redis_data:/data"],
            "networks": ["app-network"],
            "healthcheck": {
                "test": ["CMD", "redis-cli", "--raw", "incr", "ping"],
                "interval": "10s",
                "timeout": "5s",
                "retries": 5,
            },
        }

    if "nginx" in features:
        services["nginx"] = {
            "image": "nginx:alpine",
            "container_name": "nginx_proxy",
            "restart": "unless-stopped",
            "ports": ["80:80", "443:443"],
            "volumes": [
                "./docker/nginx/nginx.conf:/etc/nginx/nginx.conf:ro",
                "./docker/nginx/ssl:/etc/nginx/ssl:ro",
                "./docker/nginx/logs:/var/log/nginx",
            ],
            "networks": ["app-network"],
            "depends_on": ["app"],
        }

    # Docker compose structure
    docker_compose = {
        "version": "3.9",
        "services": services,
        "networks": {
            "app-network": {
                "driver": "bridge",
                "ipam": {
                    "config": [{"subnet": "172.20.0.0/16"}]
                }
            }
        },
        "volumes": {}
    }

    # Add volumes if needed
    if "postgres" in services:
        docker_compose["volumes"]["postgres_data"] = {"driver": "local"}
    if "redis" in services:
        docker_compose["volumes"]["redis_data"] = {"driver": "local"}

    # Generate supporting files
    dockerignore = generate_dockerignore(app_type)
    env_example = generate_env_example(app_type, features)
    setup_instructions = generate_setup_instructions(app_type, features)

    # Convert docker-compose to YAML string
    compose_yaml = generate_compose_yaml(docker_compose)

    return {
        "dockerfile": dockerfile,
        "docker_compose_yaml": compose_yaml,
        "dockerignore": dockerignore,
        "env_example": env_example,
        "setup_instructions": setup_instructions,
        "features_included": features,
        "app_type": app_type,
        "estimated_image_size": estimate_image_size(app_type),
        "security_features": [
            "Non-root user execution",
            "Multi-stage builds",
            "Minimal attack surface",
            "Health checks",
            "Resource limits",
        ]
    }

# ================================
# MCP RESOURCES
# ================================

@mcp.resource("docker://best-practices")
async def get_docker_best_practices() -> str:
    """Docker 2025 best practices guide"""
    return json.dumps(DOCKER_BEST_PRACTICES, indent=2)

@mcp.resource("docker://templates/{app_type}")
async def get_app_template(app_type: str) -> str:
    """Docker template for specific application type"""
    if app_type not in APP_TEMPLATES:
        raise ValueError(f"Application type '{app_type}' not supported")

    template = APP_TEMPLATES[app_type]
    dockerfile = generate_dockerfile_template(app_type, production_ready=True)

    return json.dumps({
        "app_type": app_type,
        "template_config": template,
        "dockerfile": dockerfile,
    }, indent=2)

# ================================
# HELPER FUNCTIONS
# ================================

def generate_dockerfile_template(app_type: str, production_ready: bool = True) -> str:
    """Generate optimized Dockerfile template with 2025 best practices"""

    template = APP_TEMPLATES.get(app_type, APP_TEMPLATES["python"])

    if app_type == "python":
        return f"""# syntax=docker/dockerfile:1.7
# Multi-stage build for Python application with uv package manager

# Stage 1: Builder
FROM {template['builder_image']} AS builder

# Install system dependencies and uv
RUN apt-get update && apt-get install -y --no-install-recommends \\
    ca-certificates \\
    curl \\
    && curl -LsSf https://astral.sh/uv/install.sh | sh \\
    && rm -rf /var/lib/apt/lists/*

# Add uv to PATH
ENV PATH="/root/.local/bin:$PATH"

WORKDIR {template['workdir']}

# Copy Python project files
COPY pyproject.toml uv.lock* ./

# Create virtual environment and install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \\
    uv venv /opt/venv && \\
    uv pip install --python /opt/venv/bin/python -r pyproject.toml

# Stage 2: Production
FROM {template['runtime_image']} AS production

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \\
    ca-certificates \\
    curl \\
    && rm -rf /var/lib/apt/lists/* \\
    && apt-get clean

# Create non-root user
RUN groupadd -r {template['user']} && useradd -r -g {template['user']} -u 1000 {template['user']} \\
    && mkdir -p {template['workdir']} \\
    && chown -R {template['user']}:{template['user']} {template['workdir']}

WORKDIR {template['workdir']}

# Copy virtual environment from builder
COPY --from=builder --chown={template['user']}:{template['user']} /opt/venv /opt/venv

# Copy application code
COPY --chown={template['user']}:{template['user']} . .

# Switch to non-root user
USER {template['user']}

# Set environment variables
ENV PATH="/opt/venv/bin:$PATH" \\
    PYTHONUNBUFFERED=1 \\
    PYTHONDONTWRITEBYTECODE=1 \\
    PIP_NO_CACHE_DIR=1 \\
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Health check using built-in endpoint
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:{template['port']}{template['health_endpoint']} || exit 1

# Expose port
EXPOSE {template['port']}

# Security and metadata labels
LABEL org.opencontainers.image.title="{app_type}-app" \\
      org.opencontainers.image.description="Production {app_type.title()} application" \\
      org.opencontainers.image.version="1.0.0" \\
      org.opencontainers.image.source="https://github.com/company/app" \\
      org.opencontainers.image.licenses="MIT" \\
      maintainer="developer@company.com"

# Use exec form for better signal handling
CMD ["python", "-m", "app"]
"""

    elif app_type == "node":
        return f"""# syntax=docker/dockerfile:1.7
# Multi-stage build for Node.js application with modern practices

# Stage 1: Dependencies
FROM {template['builder_image']} AS deps

WORKDIR {template['workdir']}

# Install dependencies for building native modules
RUN apk add --no-cache python3 make g++

# Copy package files first (optimal caching)
COPY package*.json ./
COPY yarn.lock* pnpm-lock.yaml* ./

# Install dependencies using appropriate package manager
RUN --mount=type=cache,target=/root/.npm \\
    if [ -f yarn.lock ]; then yarn install --frozen-lockfile --production; \\
    elif [ -f pnpm-lock.yaml ]; then corepack enable pnpm && pnpm install --frozen-lockfile --prod; \\
    else npm ci --only=production --no-audit --no-fund; fi

# Stage 2: Builder (for build step if needed)
FROM deps AS builder

WORKDIR {template['workdir']}

# Copy source code
COPY . .

# Build application if needed
RUN if [ -f "package.json" ] && grep -q '"build":' package.json; then \\
    npm run build; fi

# Stage 3: Production
FROM {template['runtime_image']} AS production

# Install runtime dependencies
RUN apk add --no-cache \\
    ca-certificates \\
    curl \\
    dumb-init \\
    && addgroup -g 1000 {template['user']} \\
    && adduser -D -u 1000 -G {template['user']} {template['user']}

WORKDIR {template['workdir']}

# Copy node_modules and built application
COPY --from=deps --chown={template['user']}:{template['user']} {template['workdir']}/node_modules ./node_modules
COPY --from=builder --chown={template['user']}:{template['user']} {template['workdir']} .

# Switch to non-root user
USER {template['user']}

# Set environment variables
ENV NODE_ENV=production \\
    NODE_OPTIONS="--max-old-space-size=256" \\
    NPM_CONFIG_LOGLEVEL=warn

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:{template['port']}{template['health_endpoint']} || exit 1

# Expose port
EXPOSE {template['port']}

# Security and metadata labels
LABEL org.opencontainers.image.title="{app_type}-app" \\
      org.opencontainers.image.description="Production Node.js application" \\
      org.opencontainers.image.version="1.0.0" \\
      org.opencontainers.image.source="https://github.com/company/app" \\
      org.opencontainers.image.licenses="MIT" \\
      maintainer="developer@company.com"

# Use dumb-init for proper signal handling
ENTRYPOINT ["dumb-init", "--"]
CMD ["node", "server.js"]
"""

    elif app_type == "rust":
        return f"""# syntax=docker/dockerfile:1.7
# Multi-stage build for Rust application with optimal caching

# Stage 1: Chef for dependency caching
FROM {template['builder_image']} AS chef
RUN cargo install cargo-chef
WORKDIR {template['workdir']}

# Stage 2: Planner
FROM chef AS planner
COPY Cargo.toml Cargo.lock ./
COPY src ./src
RUN cargo chef prepare --recipe-path recipe.json

# Stage 3: Builder
FROM chef AS builder

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \\
    pkg-config \\
    libssl-dev \\
    ca-certificates \\
    && rm -rf /var/lib/apt/lists/*

# Cache dependencies
COPY --from=planner {template['workdir']}/recipe.json recipe.json
RUN --mount=type=cache,target=/usr/local/cargo/registry \\
    --mount=type=cache,target={template['workdir']}/target \\
    cargo chef cook --release --recipe-path recipe.json

# Build application
COPY . .
RUN --mount=type=cache,target=/usr/local/cargo/registry \\
    --mount=type=cache,target={template['workdir']}/target \\
    cargo build --release && \\
    cp target/release/* /usr/local/bin/ || true

# Stage 4: Production
FROM {template['runtime_image']} AS production

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \\
    ca-certificates \\
    curl \\
    libssl3 \\
    && rm -rf /var/lib/apt/lists/* \\
    && apt-get clean

# Create non-root user
RUN groupadd -r {template['user']} && useradd -r -g {template['user']} -u 1000 {template['user']} \\
    && mkdir -p {template['workdir']} \\
    && chown -R {template['user']}:{template['user']} {template['workdir']}

WORKDIR {template['workdir']}

# Copy binary from builder
COPY --from=builder --chown={template['user']}:{template['user']} /usr/local/bin/* /usr/local/bin/

# Switch to non-root user
USER {template['user']}

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:{template['port']}{template['health_endpoint']} || exit 1

# Expose port
EXPOSE {template['port']}

# Security and metadata labels
LABEL org.opencontainers.image.title="{app_type}-app" \\
      org.opencontainers.image.description="Production Rust application" \\
      org.opencontainers.image.version="1.0.0" \\
      org.opencontainers.image.source="https://github.com/company/app" \\
      org.opencontainers.image.licenses="MIT" \\
      maintainer="developer@company.com"

# Use exec form with proper binary name (adjust as needed)
CMD ["app"]
"""

    elif app_type == "go":
        return f"""# syntax=docker/dockerfile:1.7
# Multi-stage build for Go application with CGO disabled

# Stage 1: Builder
FROM {template['builder_image']} AS builder

# Install ca-certificates and git for private repos
RUN apk add --no-cache ca-certificates git

WORKDIR {template['workdir']}

# Copy go mod files first for better caching
COPY go.mod go.sum ./
RUN --mount=type=cache,target=/go/pkg/mod \\
    go mod download && go mod verify

# Copy source code
COPY . .

# Build with optimizations
RUN --mount=type=cache,target=/go/pkg/mod \\
    --mount=type=cache,target=/root/.cache/go-build \\
    CGO_ENABLED=0 GOOS=linux GOARCH=amd64 \\
    go build -ldflags='-w -s -extldflags "-static"' \\
    -a -installsuffix cgo -o app .

# Stage 2: Production
FROM {template['runtime_image']} AS production

# Install ca-certificates and create user
RUN apk --no-cache add ca-certificates \\
    && addgroup -g 1000 {template['user']} \\
    && adduser -D -u 1000 -G {template['user']} {template['user']}

WORKDIR {template['workdir']}

# Copy ca-certificates and binary
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder --chown={template['user']}:{template['user']} {template['workdir']}/app ./app

# Switch to non-root user
USER {template['user']}

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \\
    CMD wget --no-verbose --tries=1 --spider http://localhost:{template['port']}{template['health_endpoint']} || exit 1

# Expose port
EXPOSE {template['port']}

# Security and metadata labels
LABEL org.opencontainers.image.title="{app_type}-app" \\
      org.opencontainers.image.description="Production Go application" \\
      org.opencontainers.image.version="1.0.0" \\
      org.opencontainers.image.source="https://github.com/company/app" \\
      org.opencontainers.image.licenses="MIT" \\
      maintainer="developer@company.com"

# Use exec form
CMD ["./app"]
"""

    # Fallback for other languages
    else:
        return generate_generic_dockerfile(app_type)

def generate_docker_compose_template(app_type: str) -> str:
    """Generate modern docker-compose.yml template using Compose Specification"""
    template = APP_TEMPLATES[app_type]

    return f"""# Docker Compose file following Compose Specification
# https://docs.docker.com/compose/compose-file/

name: {app_type}-stack

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
      target: production
      args:
        BUILDKIT_INLINE_CACHE: 1
    image: {app_type}-app:latest
    container_name: {app_type}_app
    restart: unless-stopped
    user: {template['user']}
    working_dir: {template['workdir']}
    ports:
      - "${{APP_PORT:-{template['port']}}}:{template['port']}"
    environment:
      NODE_ENV: ${{NODE_ENV:-production}}
      LOG_LEVEL: ${{LOG_LEVEL:-info}}
    env_file:
      - .env
    networks:
      - app-network
    volumes:
      - ./logs:/app/logs
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:{template['port']}{template['health_endpoint']}"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
        compress: "true"
    deploy:
      resources:
        limits:
          cpus: '0.50'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
        window: 120s
    profiles:
      - production

networks:
  app-network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/16
    labels:
      com.example.description: "Main application network"

volumes:
  logs:
    driver: local
"""

def generate_dockerignore(app_type: str) -> str:
    """Generate .dockerignore file"""

    common = """# Git
.git
.gitignore
.gitattributes

# CI/CD
.github/
.gitlab-ci.yml
.travis.yml
.circleci/

# Documentation
README.md
LICENSE
CHANGELOG.md
docs/

# Testing
tests/
test/
*.test.js
*.spec.js
coverage/
.coverage

# Environment
.env
.env.*
!.env.example

# IDE
.vscode/
.idea/
*.swp
*.swo
.DS_Store

# Logs
*.log
logs/

# Temp files
tmp/
temp/
*.tmp
"""

    specific = {
        "python": """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
.venv/
pip-log.txt
.pytest_cache/
.mypy_cache/
.ruff_cache/
*.egg-info/
dist/
build/
""",
        "node": """
# Node
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.npm
.yarn/
.next/
out/
build/
dist/
""",
        "rust": """
# Rust
target/
Cargo.lock
**/*.rs.bk
*.pdb
""",
        "go": """
# Go
*.exe
*.dll
*.so
*.dylib
*.test
*.out
vendor/
""",
    }

    return common + specific.get(app_type, "")

def generate_env_example(app_type: str, features: list[str]) -> str:
    """Generate .env.example file"""
    template = APP_TEMPLATES[app_type]

    env_vars = [
        "# Application Configuration",
        "NODE_ENV=production",
        f"APP_PORT={template['port']}",
        "LOG_LEVEL=info",
        "",
    ]

    if "database" in features or "postgres" in features:
        env_vars.extend([
            "# Database Configuration",
            "DB_HOST=postgres",
            "DB_PORT=5432",
            "DB_NAME=appdb",
            "DB_USER=appuser",
            "DB_PASSWORD=changeme_secure_password",
            "DATABASE_URL=postgresql://appuser:changeme_secure_password@postgres:5432/appdb",
            "",
        ])

    if "redis" in features:
        env_vars.extend([
            "# Redis Configuration",
            "REDIS_HOST=redis",
            "REDIS_PORT=6379",
            "REDIS_PASSWORD=changeme_redis_password",
            "REDIS_URL=redis://redis:6379",
            "",
        ])

    return "\\n".join(env_vars)

def generate_setup_instructions(app_type: str, features: list[str]) -> str:
    """Generate setup and deployment instructions"""

    return f"""# {app_type.upper()} Docker Setup Instructions

## 🚀 Quick Start

1. **Environment Setup:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

2. **Build and Run:**
   ```bash
   # Development
   docker compose up --build -d

   # Production
   docker compose -f docker-compose.yml up --build -d
   ```

3. **Verify Health:**
   ```bash
   curl http://localhost:8000/health
   ```

## 🔧 Development Commands

```bash
# View logs
docker compose logs -f app

# Shell access
docker compose exec app sh

# Rebuild without cache
docker compose build --no-cache

# Stop services
docker compose down
```

## 🛡️ Security Features

- ✅ Non-root user execution (UID 1000)
- ✅ Multi-stage builds for minimal attack surface
- ✅ Health checks for monitoring
- ✅ Resource limits and logging
- ✅ Network isolation
- ✅ Secrets management via environment variables

## 📊 Monitoring

Check container health:
```bash
docker compose ps
docker inspect app_container --format='{{.State.Health.Status}}'
```

## 🎯 Features Included

{chr(10).join(f"- {feature.title()}" for feature in features) if features else "- Base application container"}

## 📈 Performance Optimization

- Multi-stage builds reduce image size by 60-80%
- Layer caching for faster rebuilds
- Health checks for automated monitoring
- Resource limits prevent resource exhaustion
- Optimized base images for security and size
"""

def generate_generic_dockerfile(app_type: str) -> str:
    """Generate generic Dockerfile for unsupported app types"""
    return f"""# Generic Dockerfile for {app_type}
FROM alpine:latest

# Install basic dependencies
RUN apk add --no-cache ca-certificates

# Create non-root user
RUN addgroup -g 1000 appgroup && \\
    adduser -D -u 1000 -G appgroup appuser

WORKDIR /app

# Copy application
COPY --chown=appuser:appgroup . .

# Switch to non-root user
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \\
    CMD echo "Health check needed for {app_type}" || exit 1

EXPOSE 8080

CMD ["echo", "Configure your {app_type} application startup command"]
"""

def generate_compose_yaml(compose_config: dict) -> str:
    """Convert compose configuration dictionary to YAML string"""
    import yaml

    # Custom YAML representer for clean output
    def str_presenter(dumper, data):
        if '\n' in data:
            return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
        return dumper.represent_scalar('tag:yaml.org,2002:str', data)

    yaml.add_representer(str, str_presenter)

    return yaml.dump(compose_config, default_flow_style=False, indent=2, sort_keys=False)

def estimate_image_size(app_type: str) -> str:
    """Estimate final image size with 2025 optimizations"""
    sizes = {
        "python": "~120MB (with uv optimization)",
        "node": "~80MB (Alpine + multi-stage)",
        "rust": "~15MB (static binary)",
        "go": "~10MB (static binary)",
    }
    return sizes.get(app_type, "~100MB") + " (optimized multi-stage build)"

# ================================
# MCP PROMPTS - FastMCP 3.0
# ================================

@mcp.prompt()
async def optimize_dockerfile(
    current_dockerfile: str = "",
    app_type: str = "python",
    target_size: str = "minimal",
) -> list[dict[str, str]]:
    """Generate guidance for optimizing existing Dockerfiles with multi-stage builds and best practices."""
    return [
        {
            "role": "system",
            "content": """You are a Docker optimization expert specializing in 2025 container best practices.

Your expertise includes:
- Multi-stage builds for 60-80% size reduction
- Layer caching strategies for faster builds
- Security hardening (non-root users, minimal images)
- BuildKit features (--mount=type=cache, --mount=type=secret)
- Distroless and scratch images for minimal attack surface
- OCI-compliant metadata and labels

Apply these optimization patterns:
- Order COPY commands: dependencies first, then source code
- Combine RUN commands to reduce layers
- Clean package manager caches in same layer
- Use .dockerignore to exclude unnecessary files
- Pin versions explicitly (never use :latest)"""
        },
        {
            "role": "user",
            "content": f"""Optimize this Dockerfile for {app_type} application with target: {target_size}

Current Dockerfile:
{current_dockerfile if current_dockerfile else "[Provide your current Dockerfile]"}

Requirements:
1. Implement multi-stage build if not present
2. Reduce final image size using minimal base images
3. Apply security best practices (non-root user)
4. Optimize layer caching for faster rebuilds
5. Add health check configuration
6. Include proper metadata labels

Provide:
- Optimized Dockerfile with detailed comments
- Size reduction estimates
- Build time improvements
- Security enhancements applied"""
        }
    ]


@mcp.prompt()
async def design_compose_stack(
    services: list[str] = [],
    app_type: str = "python",
    environment: str = "production",
) -> list[dict[str, str]]:
    """Generate guidance for designing multi-service Docker Compose stacks."""
    services_list = ", ".join(services) if services else "web app, database"
    return [
        {
            "role": "system",
            "content": """You are a Docker Compose architect expert in modern Compose Specification.

Your expertise includes:
- Compose Specification (no version field needed)
- Service orchestration and dependency management
- Custom networks for service isolation
- Named volumes for data persistence
- Health checks with startup dependencies
- Resource limits and logging configuration
- Development and production profiles
- Secrets and configs management

Best practices:
- Use depends_on with condition: service_healthy
- Configure restart policies appropriately
- Set resource limits for all services
- Use profiles for environment-specific services
- Implement proper logging with size limits"""
        },
        {
            "role": "user",
            "content": f"""Design a Docker Compose stack for {app_type} application.

Services needed: {services_list}
Target environment: {environment}

Requirements:
1. Follow modern Compose Specification (no version field)
2. Include health checks for all services
3. Configure proper networking and isolation
4. Set up named volumes for persistence
5. Add resource limits and logging
6. Include development and production profiles

Provide:
- Complete docker-compose.yml
- Environment variable templates (.env.example)
- Network architecture explanation
- Volume management strategy
- Startup and shutdown procedures"""
        }
    ]


@mcp.prompt()
async def implement_multi_stage(
    app_type: str = "python",
    build_requirements: list[str] = [],
    runtime_only: bool = True,
) -> list[dict[str, str]]:
    """Generate guidance for implementing multi-stage Docker builds for size optimization."""
    build_reqs = ", ".join(build_requirements) if build_requirements else "compilation tools"
    return [
        {
            "role": "system",
            "content": """You are a Docker multi-stage build expert optimizing for minimal image size.

Multi-stage patterns by language:
- Python: Build wheel in builder, copy to slim runtime with uv
- Node.js: Build in full node, copy dist to alpine runtime
- Rust: Compile in rust image, copy binary to distroless/scratch
- Go: Build with CGO_ENABLED=0, copy binary to scratch

Key techniques:
- Named stages: FROM ... AS builder, FROM ... AS runtime
- Copy only artifacts: COPY --from=builder /app/dist /app
- Use --mount=type=cache for package managers
- Separate build-time and runtime dependencies
- Consider distroless images for minimal attack surface"""
        },
        {
            "role": "user",
            "content": f"""Implement multi-stage build for {app_type} application.

Build-time requirements: {build_reqs}
Copy only runtime artifacts: {runtime_only}

Requirements:
1. Design optimal stage structure
2. Maximize layer caching efficiency
3. Minimize final image size (target: <100MB for interpreted, <20MB for compiled)
4. Exclude build tools from final image
5. Include security hardening

Provide:
- Multi-stage Dockerfile with named stages
- Build arguments for flexibility
- Cache mount configurations
- Estimated size comparisons (single vs multi-stage)
- Build command examples with BuildKit"""
        }
    ]


@mcp.prompt()
async def harden_security(
    app_type: str = "python",
    security_level: str = "high",
    compliance_requirements: list[str] = [],
) -> list[dict[str, str]]:
    """Generate guidance for applying security hardening to Docker containers."""
    compliance = ", ".join(compliance_requirements) if compliance_requirements else "general security best practices"
    return [
        {
            "role": "system",
            "content": """You are a container security expert specializing in Docker hardening.

Security measures by priority:
1. Non-root execution: USER directive with specific UID
2. Minimal base images: distroless, alpine, slim variants
3. No secrets in layers: use --mount=type=secret or runtime injection
4. Read-only filesystem: --read-only flag where possible
5. Drop capabilities: --cap-drop=ALL, then add only needed
6. Security scanning: Trivy, Snyk, or Docker Scout integration

Compliance considerations:
- CIS Docker Benchmark requirements
- OWASP Container Security guidelines
- SOC2/HIPAA specific requirements
- Supply chain security (SBOM generation)"""
        },
        {
            "role": "user",
            "content": f"""Apply security hardening to {app_type} container at {security_level} level.

Compliance requirements: {compliance}

Requirements:
1. Implement non-root user execution
2. Select appropriate minimal base image
3. Configure secrets management (no hardcoded credentials)
4. Set up read-only filesystem where possible
5. Drop unnecessary Linux capabilities
6. Add vulnerability scanning integration

Provide:
- Security-hardened Dockerfile
- docker-compose.yml with security options
- Runtime security flags
- Vulnerability scanning CI/CD integration
- Security checklist for verification"""
        }
    ]


@mcp.prompt()
async def setup_production_ready(
    app_type: str = "python",
    features: list[str] = [],
    scale_requirements: str = "medium",
) -> list[dict[str, str]]:
    """Generate guidance for setting up production-ready Docker configurations."""
    features_list = ", ".join(features) if features else "logging, monitoring, health checks"
    return [
        {
            "role": "system",
            "content": """You are a production Docker deployment expert.

Production requirements:
- Health checks with proper intervals and retries
- Graceful shutdown handling (SIGTERM)
- Structured logging with size limits
- Resource limits (CPU, memory)
- Restart policies (unless-stopped, on-failure)
- Environment-based configuration
- Secrets management
- Monitoring integration (Prometheus metrics)

Orchestration considerations:
- Docker Swarm mode deployment
- Kubernetes compatibility
- Rolling update strategies
- Blue-green deployment support"""
        },
        {
            "role": "user",
            "content": f"""Set up production-ready Docker configuration for {app_type} application.

Required features: {features_list}
Scale requirements: {scale_requirements}

Requirements:
1. Complete Dockerfile with all production optimizations
2. docker-compose.yml with production configuration
3. Health check endpoints and Docker HEALTHCHECK
4. Logging configuration with rotation
5. Resource limits and monitoring
6. Deployment scripts and procedures

Provide:
- Production Dockerfile
- docker-compose.prod.yml
- .env.production template
- Deployment checklist
- Monitoring and alerting setup
- Backup and recovery procedures"""
        }
    ]


# ================================
# SERVER STARTUP
# ================================

if __name__ == "__main__":
    logger.info("Docker Optimizer MCP Server starting...")
    logger.info("Specialized in containerization best practices and security optimization (2025 Edition)")
    logger.info(f"Supported frameworks: {', '.join(APP_TEMPLATES.keys())}")
    logger.info("Features: Dockerfile analysis, Compose validation, prompt enhancement, complete config generation")
    logger.info("New in 3.0: Context injection, MCP Prompts, Tags for discovery")
    logger.info("")
    logger.info("Available MCP Prompts:")
    logger.info("  - optimize_dockerfile: Optimize existing Dockerfiles")
    logger.info("  - design_compose_stack: Design multi-service Docker Compose stacks")
    logger.info("  - implement_multi_stage: Implement multi-stage builds")
    logger.info("  - harden_security: Apply security hardening")
    logger.info("  - setup_production_ready: Configure for production deployment")
    mcp.run()
