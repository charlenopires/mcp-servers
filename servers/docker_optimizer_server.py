"""
Docker Optimizer MCP Server
Servidor MCP para análise e otimização de prompts Docker
Fornecer ferramentas para gerar Dockerfiles otimizados e docker-compose.yml seguindo best practices
"""

import json
import logging
from typing import Any

from fastmcp import FastMCP
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP(
    name="Docker Optimizer MCP Server",
    description="Servidor MCP especializado em otimização de prompts Docker e geração de configurações containerizadas",
    version="1.0.0",
)

# ================================
# MODELOS DE DADOS
# ================================


class DockerPromptAnalysis(BaseModel):
    """Modelo para análise de prompts Docker"""

    score: int = Field(description="Score de qualidade de 0-100")
    strengths: list[str] = Field(description="Pontos fortes identificados")
    weaknesses: list[str] = Field(description="Pontos fracos identificados")
    missing_elements: list[str] = Field(description="Elementos ausentes")
    recommendations: list[str] = Field(description="Recomendações de melhoria")
    security_issues: list[str] = Field(description="Problemas de segurança")


class DockerRequirements(BaseModel):
    """Modelo para requisitos Docker"""

    app_type: str = Field(description="Tipo de aplicação (node, python, rust, etc)")
    base_image: str | None = Field(None, description="Imagem base especificada")
    has_multistage: bool = Field(default=False, description="Usa multi-stage build")
    has_security: bool = Field(default=False, description="Menciona segurança")
    has_optimization: bool = Field(default=False, description="Menciona otimização")
    has_healthcheck: bool = Field(default=False, description="Inclui healthcheck")
    has_non_root_user: bool = Field(default=False, description="Usa usuário não-root")


class EnhancedDockerPrompt(BaseModel):
    """Modelo para prompt aprimorado"""

    original_prompt: str
    enhanced_prompt: str
    added_elements: list[str]
    dockerfile_template: str
    docker_compose_template: str | None = None


# ================================
# BASE DE CONHECIMENTO - MELHORES PRÁTICAS 2025
# ================================

DOCKER_BEST_PRACTICES = {
    "security": {
        "non_root_user": "Sempre execute containers como usuário não-root",
        "minimal_base": "Use imagens base mínimas (alpine, distroless)",
        "no_secrets": "Nunca inclua secrets no Dockerfile",
        "scan_vulnerabilities": "Escaneie imagens para vulnerabilidades",
        "specific_versions": "Use versões específicas de imagens base",
        "dockerignore": "Sempre use .dockerignore",
    },
    "optimization": {
        "multi_stage": "Use multi-stage builds para reduzir tamanho",
        "layer_caching": "Ordene comandos para otimizar cache",
        "combine_run": "Combine comandos RUN quando possível",
        "clean_apt": "Limpe cache do apt após instalação",
        "minimal_deps": "Instale apenas dependências necessárias",
    },
    "best_practices": {
        "healthcheck": "Sempre inclua HEALTHCHECK",
        "labels": "Use LABEL para metadata",
        "workdir": "Use WORKDIR ao invés de cd",
        "copy_vs_add": "Prefira COPY ao invés de ADD",
        "entrypoint_cmd": "Use ENTRYPOINT + CMD apropriadamente",
    },
}

# Templates por tipo de aplicação
APP_TEMPLATES = {
    "python": {
        "base_image": "python:3.12-slim",
        "dev_deps": ["gcc", "python3-dev"],
        "package_manager": "pip",
        "package_file": "requirements.txt",
        "run_command": "python",
    },
    "node": {
        "base_image": "node:22-alpine",
        "dev_deps": ["build-base"],
        "package_manager": "npm",
        "package_file": "package*.json",
        "run_command": "node",
    },
    "rust": {
        "base_image": "rust:1.82-slim",
        "dev_deps": ["gcc", "pkg-config", "libssl-dev"],
        "package_manager": "cargo",
        "package_file": "Cargo.toml",
        "run_command": "./target/release/",
    },
    "go": {
        "base_image": "golang:1.24-alpine",
        "dev_deps": ["gcc", "musl-dev"],
        "package_manager": "go mod",
        "package_file": "go.mod",
        "run_command": "./app",
    },
}

# ================================
# FERRAMENTAS MCP
# ================================


@mcp.tool()
async def analyze_docker_prompt(prompt: str) -> dict[str, Any]:
    """
    Analisa um prompt de criação Docker e fornece feedback detalhado

    Args:
        prompt: Prompt do usuário para análise

    Returns:
        Análise completa com score, pontos fortes/fracos e sugestões
    """
    logger.info(f"Analisando prompt Docker: {prompt[:100]}...")

    score = 0
    strengths = []
    weaknesses = []
    missing_elements = []
    recommendations = []
    security_issues = []

    # Análise de elementos presentes
    prompt_lower = prompt.lower()

    # Verificar tipo de aplicação
    app_type = None
    for app, keywords in {
        "python": ["python", "django", "flask", "fastapi", "pip"],
        "node": ["node", "npm", "react", "next", "express"],
        "rust": ["rust", "cargo", "axum", "actix"],
        "go": ["golang", "go ", "gin", "echo"],
    }.items():
        if any(kw in prompt_lower for kw in keywords):
            app_type = app
            strengths.append(f"Tipo de aplicação identificado: {app}")
            score += 10
            break

    if not app_type:
        weaknesses.append("Tipo de aplicação não especificado claramente")
        recommendations.append(
            "Especifique o tipo de aplicação (Python, Node.js, Rust, etc.)"
        )

    # Verificar menções a best practices
    if "multi-stage" in prompt_lower or "multistage" in prompt_lower:
        strengths.append("Menciona multi-stage builds")
        score += 15
    else:
        missing_elements.append("Multi-stage builds não mencionado")
        recommendations.append("Use multi-stage builds para reduzir tamanho da imagem")

    if (
        "alpine" in prompt_lower
        or "slim" in prompt_lower
        or "distroless" in prompt_lower
    ):
        strengths.append("Usa imagem base otimizada")
        score += 10
    else:
        recommendations.append("Considere usar imagens base mínimas (alpine, slim)")

    if "security" in prompt_lower or "segurança" in prompt_lower:
        strengths.append("Considera aspectos de segurança")
        score += 10
    else:
        security_issues.append("Segurança não mencionada")

    if "non-root" in prompt_lower or "user" in prompt_lower:
        strengths.append("Menciona usuário não-root")
        score += 10
    else:
        security_issues.append("Não menciona execução como usuário não-root")
        recommendations.append("Execute containers como usuário não-root por segurança")

    if "healthcheck" in prompt_lower or "health check" in prompt_lower:
        strengths.append("Inclui healthcheck")
        score += 10
    else:
        missing_elements.append("Healthcheck não especificado")
        recommendations.append("Adicione HEALTHCHECK para monitoramento")

    if "cache" in prompt_lower or "otimiz" in prompt_lower:
        strengths.append("Considera otimização")
        score += 10

    if "docker-compose" in prompt_lower or "compose" in prompt_lower:
        strengths.append("Inclui Docker Compose")
        score += 10
    else:
        recommendations.append("Considere incluir docker-compose.yml para orquestração")

    # Verificar elementos de produção
    if (
        "production" in prompt_lower
        or "produção" in prompt_lower
        or "prod" in prompt_lower
    ):
        strengths.append("Orientado para produção")
        score += 15

    # Ajustar score final
    if score > 100:
        score = 100
    elif score < 20:
        score = 20  # Score mínimo

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
        "summary": f"Score: {score}/100 - "
        f"Pontos fortes: {len(strengths)}, "
        f"Melhorias sugeridas: {len(recommendations)}",
    }


@mcp.tool()
async def enhance_docker_prompt(
    prompt: str,
    app_type: str | None = None,
    include_compose: bool = True,
    production_ready: bool = True,
) -> dict[str, Any]:
    """
    Aprimora um prompt Docker com melhores práticas e detalhes essenciais

    Args:
        prompt: Prompt original do usuário
        app_type: Tipo de aplicação (python, node, rust, go)
        include_compose: Incluir template docker-compose
        production_ready: Otimizar para produção

    Returns:
        Prompt aprimorado com templates Dockerfile e docker-compose
    """
    logger.info(f"Aprimorando prompt Docker para {app_type or 'auto-detect'}")

    # Auto-detectar tipo se não especificado
    if not app_type:
        prompt_lower = prompt.lower()
        for app in ["python", "node", "rust", "go"]:
            if app in prompt_lower:
                app_type = app
                break
        if not app_type:
            app_type = "python"  # Default

    # Construir prompt aprimorado
    enhanced_parts = [
        f"# Requisição Original\n{prompt}\n",
        "\n# REQUISITOS APRIMORADOS\n",
        f"## Tipo de Aplicação: {app_type.upper()}\n",
        "\n## Dockerfile Requirements:\n",
        "### Multi-Stage Build Structure:\n",
        "- **Stage 1 (builder)**: Compilação e build\n",
        "- **Stage 2 (production)**: Imagem final otimizada\n",
        "\n### Segurança:\n",
        "- ✅ Executar como usuário não-root (UID 1000)\n",
        "- ✅ Usar imagem base mínima e específica\n",
        "- ✅ Não incluir secrets ou tokens\n",
        "- ✅ Implementar .dockerignore adequado\n",
        "\n### Otimizações:\n",
        "- ✅ Ordenar layers para cache eficiente\n",
        "- ✅ Combinar comandos RUN quando possível\n",
        "- ✅ Limpar caches de package managers\n",
        "- ✅ Copiar apenas arquivos necessários\n",
        "\n### Best Practices:\n",
        "- ✅ Incluir HEALTHCHECK\n",
        "- ✅ Usar LABEL para metadata\n",
        "- ✅ Definir WORKDIR apropriado\n",
        "- ✅ Usar COPY ao invés de ADD\n",
    ]

    # Gerar template Dockerfile
    dockerfile_template = generate_dockerfile_template(app_type, production_ready)

    # Gerar docker-compose se solicitado
    docker_compose_template = None
    if include_compose:
        docker_compose_template = generate_docker_compose_template(app_type)
        enhanced_parts.append("\n## Docker Compose Requirements:\n")
        enhanced_parts.append("- ✅ Definir networks customizadas\n")
        enhanced_parts.append("- ✅ Configurar volumes para persistência\n")
        enhanced_parts.append("- ✅ Definir restart policy\n")
        enhanced_parts.append("- ✅ Configurar health checks\n")
        enhanced_parts.append("- ✅ Usar variáveis de ambiente\n")

    enhanced_prompt = "".join(enhanced_parts)

    return {
        "original_prompt": prompt,
        "enhanced_prompt": enhanced_prompt,
        "dockerfile_template": dockerfile_template,
        "docker_compose_template": docker_compose_template,
        "added_elements": [
            "Multi-stage build structure",
            "Security best practices",
            "Layer optimization",
            "Health check configuration",
            "Non-root user setup",
            "Production optimizations",
        ],
        "app_type": app_type,
    }


@mcp.tool()
async def validate_dockerfile(dockerfile_content: str) -> dict[str, Any]:
    """
    Valida um Dockerfile existente contra best practices

    Args:
        dockerfile_content: Conteúdo do Dockerfile para validação

    Returns:
        Relatório de validação com issues e sugestões
    """
    logger.info("Validando Dockerfile contra best practices")

    issues = []
    warnings = []
    suggestions = []
    score = 100

    lines = dockerfile_content.split("\n")

    # Verificações de segurança
    if not any("USER" in line and "root" not in line for line in lines):
        issues.append("❌ Container executando como root - grave problema de segurança")
        score -= 20

    if any("ADD " in line for line in lines):
        warnings.append(
            "⚠️ Usando ADD ao invés de COPY - pode causar comportamento inesperado"
        )
        score -= 5

    if not any("HEALTHCHECK" in line for line in lines):
        warnings.append("⚠️ Sem HEALTHCHECK definido")
        score -= 10

    # Verificar multi-stage
    from_count = sum(1 for line in lines if line.strip().startswith("FROM"))
    if from_count < 2:
        suggestions.append("💡 Considere usar multi-stage builds para reduzir tamanho")
        score -= 10

    # Verificar otimizações
    if any(
        "apt-get install" in line and "rm -rf /var/lib/apt/lists/*" not in line
        for line in lines
    ):
        warnings.append("⚠️ Cache do apt não limpo após instalação")
        score -= 5

    # Verificar uso de versões específicas
    for line in lines:
        if line.startswith("FROM") and ":latest" in line:
            issues.append("❌ Usando tag :latest - use versões específicas")
            score -= 10

    return {
        "valid": len(issues) == 0,
        "score": max(0, score),
        "issues": issues,
        "warnings": warnings,
        "suggestions": suggestions,
        "summary": f"Score: {score}/100 - Issues: {len(issues)}, Warnings: {len(warnings)}",
    }


@mcp.tool()
async def generate_docker_config(
    project_description: str, app_type: str, features: list[str] | None = None
) -> dict[str, Any]:
    """
    Gera configuração Docker completa baseada na descrição do projeto

    Args:
        project_description: Descrição do projeto
        app_type: Tipo de aplicação (python, node, rust, go)
        features: Features adicionais (database, redis, nginx, etc)

    Returns:
        Configuração completa com Dockerfile, docker-compose e instruções
    """
    logger.info(f"Gerando configuração Docker para {app_type}")

    features = features or []

    # Gerar Dockerfile
    dockerfile = generate_dockerfile_template(app_type, production_ready=True)

    # Gerar docker-compose com features
    services = {
        "app": {
            "build": ".",
            "container_name": f"{app_type}_app",
            "restart": "unless-stopped",
            "environment": [],
            "networks": ["app-network"],
            "healthcheck": {
                "test": ["CMD", "curl", "-f", "http://localhost:8000/health"],
                "interval": "30s",
                "timeout": "10s",
                "retries": 3,
            },
        }
    }

    # Adicionar features
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
            "volumes": ["postgres_data:/var/lib/postgresql/data"],
            "networks": ["app-network"],
            "healthcheck": {
                "test": ["CMD-SHELL", "pg_isready -U ${DB_USER:-appuser}"],
                "interval": "10s",
                "timeout": "5s",
                "retries": 5,
            },
        }
        services["app"]["depends_on"] = {"postgres": {"condition": "service_healthy"}}

    if "redis" in features:
        services["redis"] = {
            "image": "redis:7-alpine",
            "container_name": "redis_cache",
            "restart": "unless-stopped",
            "networks": ["app-network"],
            "healthcheck": {
                "test": ["CMD", "redis-cli", "ping"],
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
                "./nginx.conf:/etc/nginx/nginx.conf:ro",
                "./ssl:/etc/nginx/ssl:ro",
            ],
            "networks": ["app-network"],
            "depends_on": ["app"],
        }

    docker_compose = {
        "services": services,
        "networks": {"app-network": {"driver": "bridge"}},
    }

    if any(svc.get("volumes") for svc in services.values()):
        docker_compose["volumes"] = {}
        if "postgres" in services:
            docker_compose["volumes"]["postgres_data"] = {}

    # Gerar .dockerignore
    dockerignore = generate_dockerignore(app_type)

    # Gerar instruções de uso
    instructions = generate_usage_instructions(app_type, features)

    return {
        "dockerfile": dockerfile,
        "docker_compose": yaml_dump(docker_compose),
        "dockerignore": dockerignore,
        "env_example": generate_env_example(features),
        "instructions": instructions,
        "features_included": features,
        "estimated_image_size": estimate_image_size(app_type, features),
    }


# ================================
# RECURSOS MCP
# ================================


@mcp.resource("docker://best-practices")
async def get_docker_best_practices() -> str:
    """Retorna guia de melhores práticas Docker 2025"""
    return json.dumps(DOCKER_BEST_PRACTICES, indent=2)


@mcp.resource("docker://templates/{app_type}")
async def get_app_template(app_type: str) -> str:
    """Retorna template Docker para tipo de aplicação específico"""
    if app_type not in APP_TEMPLATES:
        raise ValueError(f"Tipo de aplicação '{app_type}' não suportado")

    template = APP_TEMPLATES[app_type]
    dockerfile = generate_dockerfile_template(app_type, production_ready=True)

    return json.dumps(
        {"app_type": app_type, "template_config": template, "dockerfile": dockerfile},
        indent=2,
    )


# ================================
# FUNÇÕES AUXILIARES
# ================================


def generate_dockerfile_template(app_type: str, production_ready: bool = True) -> str:
    """Gera template de Dockerfile otimizado"""

    template = APP_TEMPLATES.get(app_type, APP_TEMPLATES["python"])

    if app_type == "python":
        return f"""# syntax=docker/dockerfile:1
# Multi-stage build para Python

# Stage 1: Builder
FROM {template['base_image']} AS builder

# Instalar dependências de build
RUN apt-get update && apt-get install -y --no-install-recommends \\
    gcc \\
    python3-dev \\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar arquivos de dependências primeiro (cache eficiente)
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Production
FROM {template['base_image']}

# Criar usuário não-root
RUN useradd -m -u 1000 appuser && \\
    mkdir -p /app && \\
    chown -R appuser:appuser /app

WORKDIR /app

# Copiar dependências do builder
COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local

# Copiar código da aplicação
COPY --chown=appuser:appuser . .

# Trocar para usuário não-root
USER appuser

# Adicionar .local/bin ao PATH
ENV PATH=/home/appuser/.local/bin:$PATH

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \\
    CMD python -c "import requests; requests.get('http://localhost:8000/health')" || exit 1

# Expor porta
EXPOSE 8000

# Comando para executar a aplicação
CMD ["python", "app.py"]
"""

    elif app_type == "node":
        return f"""# syntax=docker/dockerfile:1
# Multi-stage build para Node.js

# Stage 1: Builder
FROM {template['base_image']} AS builder

WORKDIR /app

# Copiar package files primeiro (cache eficiente)
COPY package*.json ./
RUN npm ci --only=production

# Stage 2: Development (opcional)
FROM {template['base_image']} AS development

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
CMD ["npm", "run", "dev"]

# Stage 3: Production
FROM {template['base_image']} AS production

# Criar usuário não-root
RUN addgroup -g 1000 appgroup && \\
    adduser -D -u 1000 -G appgroup appuser

WORKDIR /app

# Copiar dependências do builder
COPY --from=builder --chown=appuser:appgroup /app/node_modules ./node_modules

# Copiar código da aplicação
COPY --chown=appuser:appgroup . .

# Trocar para usuário não-root
USER appuser

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \\
    CMD node healthcheck.js || exit 1

# Expor porta
EXPOSE 3000

# Comando para executar a aplicação
CMD ["node", "server.js"]
"""

    elif app_type == "rust":
        return f"""# syntax=docker/dockerfile:1
# Multi-stage build para Rust

# Stage 1: Builder
FROM {template['base_image']} AS builder

# Instalar dependências de build
RUN apt-get update && apt-get install -y \\
    pkg-config \\
    libssl-dev \\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar arquivos de dependências primeiro
COPY Cargo.toml Cargo.lock ./

# Build de dependências (cache eficiente)
RUN mkdir src && \\
    echo "fn main() {{}}" > src/main.rs && \\
    cargo build --release && \\
    rm -rf src

# Copiar código fonte e build final
COPY src ./src
RUN touch src/main.rs && \\
    cargo build --release

# Stage 2: Production
FROM debian:bookworm-slim

# Instalar dependências runtime
RUN apt-get update && apt-get install -y \\
    ca-certificates \\
    libssl3 \\
    && rm -rf /var/lib/apt/lists/*

# Criar usuário não-root
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Copiar binário do builder
COPY --from=builder --chown=appuser:appuser /app/target/release/app /app/app

# Trocar para usuário não-root
USER appuser

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:8080/health || exit 1

# Expor porta
EXPOSE 8080

# Comando para executar a aplicação
CMD ["./app"]
"""

    else:  # Go
        return f"""# syntax=docker/dockerfile:1
# Multi-stage build para Go

# Stage 1: Builder
FROM {template['base_image']} AS builder

WORKDIR /app

# Copiar go.mod e go.sum primeiro (cache eficiente)
COPY go.mod go.sum ./
RUN go mod download

# Copiar código fonte
COPY . .

# Build da aplicação
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

# Stage 2: Production
FROM alpine:latest

# Instalar ca-certificates para HTTPS
RUN apk --no-cache add ca-certificates

# Criar usuário não-root
RUN addgroup -g 1000 appgroup && \\
    adduser -D -u 1000 -G appgroup appuser

WORKDIR /app

# Copiar binário do builder
COPY --from=builder --chown=appuser:appgroup /app/app .

# Trocar para usuário não-root
USER appuser

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \\
    CMD wget --no-verbose --tries=1 --spider http://localhost:8080/health || exit 1

# Expor porta
EXPOSE 8080

# Comando para executar a aplicação
CMD ["./app"]
"""


def generate_docker_compose_template(app_type: str) -> str:
    """Gera template de docker-compose.yml"""

    return f"""version: '3.9'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
      target: production
    container_name: {app_type}_app
    restart: unless-stopped
    ports:
      - "${{APP_PORT:-8000}}:8000"
    environment:
      - NODE_ENV=${{NODE_ENV:-production}}
      - DATABASE_URL=${{DATABASE_URL}}
      - REDIS_URL=${{REDIS_URL:-redis://redis:6379}}
    volumes:
      - ./data:/app/data
    networks:
      - app-network
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  postgres:
    image: postgres:17-alpine
    container_name: postgres_db
    restart: unless-stopped
    environment:
      - POSTGRES_DB=${{DB_NAME:-appdb}}
      - POSTGRES_USER=${{DB_USER:-appuser}}
      - POSTGRES_PASSWORD=${{DB_PASSWORD}}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    networks:
      - app-network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${{DB_USER:-appuser}}"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    container_name: redis_cache
    restart: unless-stopped
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    networks:
      - app-network
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

networks:
  app-network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/16

volumes:
  postgres_data:
    driver: local
  redis_data:
    driver: local
"""


def generate_dockerignore(app_type: str) -> str:
    """Gera arquivo .dockerignore apropriado"""

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
pip-delete-this-directory.txt
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
.pnp.*
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


def generate_env_example(features: list[str]) -> str:
    """Gera arquivo .env.example"""

    env_vars = [
        "# Application",
        "NODE_ENV=production",
        "APP_PORT=8000",
        "LOG_LEVEL=info",
        "",
    ]

    if "database" in features or "postgres" in features:
        env_vars.extend(
            [
                "# Database",
                "DB_HOST=postgres",
                "DB_PORT=5432",
                "DB_NAME=appdb",
                "DB_USER=appuser",
                "DB_PASSWORD=changeme",
                "DATABASE_URL=postgresql://appuser:changeme@postgres:5432/appdb",
                "",
            ]
        )

    if "redis" in features:
        env_vars.extend(
            [
                "# Redis",
                "REDIS_HOST=redis",
                "REDIS_PORT=6379",
                "REDIS_URL=redis://redis:6379",
                "",
            ]
        )

    if "nginx" in features:
        env_vars.extend(["# Nginx", "NGINX_HOST=localhost", "NGINX_PORT=80", ""])

    return "\n".join(env_vars)


def generate_usage_instructions(app_type: str, features: list[str]) -> str:
    """Gera instruções de uso"""

    return f"""# Instruções de Uso - {app_type.upper()} Docker Setup

## 📋 Pré-requisitos
- Docker Engine 27.0+
- Docker Compose 2.30+

## 🚀 Quick Start

1. **Clone o repositório e configure o ambiente:**
   ```bash
   cp .env.example .env
   # Edite o .env com suas configurações
   ```

2. **Build da imagem:**
   ```bash
   docker compose build
   ```

3. **Executar em desenvolvimento:**
   ```bash
   docker compose up -d
   ```

4. **Executar em produção:**
   ```bash
   docker compose -f docker-compose.yml up -d
   ```

## 📊 Comandos Úteis

### Logs
```bash
docker compose logs -f app
```

### Shell no container
```bash
docker compose exec app sh
```

### Rebuild com no-cache
```bash
docker compose build --no-cache
```

### Verificar saúde dos serviços
```bash
docker compose ps
docker inspect app --format='{{{{.State.Health.Status}}}}'
```

## 🔒 Segurança

- ✅ Container executa como usuário não-root (UID 1000)
- ✅ Secrets gerenciados via variáveis de ambiente
- ✅ Imagens base mínimas e atualizadas
- ✅ Healthchecks configurados

## 📦 Features Incluídas
{chr(10).join(f'- {feature}' for feature in features) if features else '- Nenhuma feature adicional'}

## 🎯 Otimizações Aplicadas

1. **Multi-stage build** - Reduz tamanho da imagem em ~60-80%
2. **Layer caching** - Build mais rápido em rebuilds
3. **Healthchecks** - Monitoramento automático
4. **Non-root user** - Segurança aprimorada
5. **.dockerignore** - Evita arquivos desnecessários

## 📈 Monitoramento

Verifique a saúde da aplicação:
```bash
curl http://localhost:8000/health
```

## 🛠️ Troubleshooting

Se encontrar problemas:
1. Verifique os logs: `docker compose logs`
2. Verifique se as portas estão disponíveis
3. Confirme as variáveis de ambiente no .env
4. Execute `docker system prune` para limpar cache
"""


def estimate_image_size(app_type: str, features: list[str]) -> str:
    """Estima tamanho da imagem final"""

    base_sizes = {
        "python": 150,  # MB
        "node": 120,
        "rust": 50,
        "go": 30,
    }

    size = base_sizes.get(app_type, 100)

    # Adicionar overhead de features
    for feature in features:
        if feature in ["database", "postgres"]:
            size += 0  # Serviço separado
        elif feature == "redis":
            size += 0  # Serviço separado
        elif feature == "nginx":
            size += 0  # Serviço separado

    return f"~{size}MB (imagem final otimizada)"


def yaml_dump(data: dict) -> str:
    """Converte dict para formato YAML simples"""

    # Implementação simplificada de YAML para docker-compose
    def dict_to_yaml(obj, indent=0):
        yaml_str = ""
        spaces = "  " * indent

        if isinstance(obj, dict):
            for key, value in obj.items():
                yaml_str += f"{spaces}{key}:\n"
                if isinstance(value, dict | list):
                    yaml_str += dict_to_yaml(value, indent + 1)
                else:
                    yaml_str += f"{spaces}  {value}\n"
        elif isinstance(obj, list):
            for item in obj:
                if isinstance(item, dict):
                    yaml_str += f"{spaces}-\n"
                    yaml_str += dict_to_yaml(item, indent + 1)
                else:
                    yaml_str += f"{spaces}- {item}\n"

        return yaml_str

    return dict_to_yaml(data)


if __name__ == "__main__":
    logger.info("🐳 Docker Optimizer MCP Server iniciado")
    logger.info("Disponível para análise e otimização de prompts Docker")
    mcp.run()
