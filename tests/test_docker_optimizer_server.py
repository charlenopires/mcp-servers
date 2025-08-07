#!/usr/bin/env python3
"""
Testes para o Docker Optimizer Server - Servidor MCP para otimização de configurações Docker

Este módulo testa as funcionalidades do servidor Docker especializado em análise,
otimização e validação de Dockerfiles e docker-compose.yml.
"""

import pytest
from unittest.mock import AsyncMock

# Importações condicionais para fallback
try:
    from servers.docker_optimizer_server import (
        ContainerFramework,
        SecurityLevel,
        DockerPromptAnalysis,
        DockerRequirements,
        docker_analyze_prompt,
        docker_enhance_prompt,
        docker_validate_compose,
        docker_validate_dockerfile,
        docker_generate_compose_config,
        docker_generate_config,
        get_docker_best_practices
    )
    DOCKER_SERVER_AVAILABLE = True
except ImportError as e:
    print(f"Docker Optimizer Server não disponível: {e}")
    DOCKER_SERVER_AVAILABLE = False


class TestDockerEnums:
    """Testes para enums do Docker Server"""

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server não disponível")
    def test_container_framework_enum(self):
        """Testa enum ContainerFramework"""
        expected_frameworks = ["NODE", "PYTHON",
                               "JAVA", "GO", "RUST", "PHP", "NGINX"]

        available_frameworks = [
            framework.name for framework in ContainerFramework]

        for framework in expected_frameworks:
            assert framework in available_frameworks

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server não disponível")
    def test_security_level_enum(self):
        """Testa enum SecurityLevel"""
        expected_levels = ["BASIC", "ENHANCED", "PRODUCTION", "HARDENED"]

        available_levels = [level.name for level in SecurityLevel]

        for level in expected_levels:
            assert level in available_levels


class TestDockerModels:
    """Testes para modelos de dados do Docker Server"""

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server não disponível")
    def test_docker_prompt_analysis_creation(self):
        """Testa criação de DockerPromptAnalysis"""
        analysis = DockerPromptAnalysis(
            score=85.0,
            strengths=["Multi-stage build", "Security practices"],
            weaknesses=["Missing healthcheck"],
            missing_elements=["Environment variables"],
            recommendations=["Add HEALTHCHECK instruction"],
            security_issues=["Running as root"]
        )

        assert analysis.score == 85.0
        assert len(analysis.strengths) == 2
        assert len(analysis.weaknesses) == 1
        assert len(analysis.missing_elements) == 1
        assert len(analysis.recommendations) == 1
        assert len(analysis.security_issues) == 1

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server não disponível")
    def test_docker_requirements_creation(self):
        """Testa criação de DockerRequirements"""
        requirements = DockerRequirements(
            framework=ContainerFramework.PYTHON,
            has_multistage=True,
            has_security=True,
            has_optimization=True,
            has_healthcheck=True,
            has_non_root_user=True
        )

        assert requirements.framework == ContainerFramework.PYTHON
        assert requirements.has_multistage is True
        assert requirements.has_security is True
        assert requirements.has_optimization is True
        assert requirements.has_healthcheck is True
        assert requirements.has_non_root_user is True


class TestDockerAnalysisFunctions:
    """Testes para as funções de análise do Docker Server"""

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server não disponível")
    @pytest.mark.asyncio
    async def test_docker_analyze_prompt_basic(self):
        """Testa análise básica de prompt Docker"""
        prompt = "Criar uma imagem Docker para aplicação Python Flask"

        result = await docker_analyze_prompt(prompt)

        assert isinstance(result, dict)
        assert "score" in result
        assert "strengths" in result
        assert "weaknesses" in result
        assert "recommendations" in result
        assert 0 <= result["score"] <= 100

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server não disponível")
    @pytest.mark.asyncio
    async def test_docker_analyze_prompt_comprehensive(self):
        """Testa análise de prompt Docker abrangente"""
        comprehensive_prompt = """
        Criar uma imagem Docker para aplicação Python Flask com:
        - Build multi-stage para otimização
        - Usuário não-root para segurança
        - Healthcheck para monitoramento
        - Cache de dependências
        - Variáveis de ambiente configuráveis
        - Exposição da porta 8000
        - Logs estruturados
        """

        result = await docker_analyze_prompt(comprehensive_prompt)

        # Prompt abrangente deve ter score alto
        assert result["score"] >= 70
        assert len(result["strengths"]) > 0

        # Verificar elementos identificados
        strengths_text = " ".join(result["strengths"]).lower()
        assert any(keyword in strengths_text for keyword in [
            "multi-stage", "security", "optimization", "healthcheck"
        ])

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server não disponível")
    @pytest.mark.asyncio
    async def test_docker_enhance_prompt(self):
        """Testa melhoria de prompt Docker"""
        basic_prompt = "Dockerizar aplicação Python"

        result = await docker_enhance_prompt(
            prompt=basic_prompt,
            target_framework="python",
            security_level="production"
        )

        assert isinstance(result, dict)
        assert "enhanced_prompt" in result
        assert "improvements" in result
        assert "technical_requirements" in result

        enhanced = result["enhanced_prompt"]
        assert len(enhanced) > len(basic_prompt)
        assert "python" in enhanced.lower()
        assert any(keyword in enhanced.lower() for keyword in [
            "multi-stage", "security", "optimization"
        ])

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server não disponível")
    @pytest.mark.asyncio
    async def test_docker_validate_dockerfile(self):
        """Testa validação de Dockerfile"""
        dockerfile_content = """
        FROM python:3.11-slim
        
        WORKDIR /app
        
        COPY requirements.txt .
        RUN pip install -r requirements.txt
        
        COPY . .
        
        EXPOSE 8000
        
        CMD ["python", "app.py"]
        """

        result = await docker_validate_dockerfile(dockerfile_content)

        assert isinstance(result, dict)
        assert "is_valid" in result
        assert "score" in result
        assert "issues" in result
        assert "suggestions" in result
        assert "security_warnings" in result

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server não disponível")
    @pytest.mark.asyncio
    async def test_docker_validate_compose(self):
        """Testa validação de docker-compose"""
        compose_content = """
        version: '3.8'
        
        services:
          web:
            build: .
            ports:
              - "8000:8000"
            environment:
              - ENV=production
            healthcheck:
              test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
              interval: 30s
              timeout: 10s
              retries: 3
        """

        result = await docker_validate_compose(compose_content)

        assert isinstance(result, dict)
        assert "is_valid" in result
        assert "score" in result
        assert "issues" in result
        assert "suggestions" in result

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server não disponível")
    @pytest.mark.asyncio
    async def test_docker_generate_compose_config(self):
        """Testa geração de configuração docker-compose"""
        result = await docker_generate_compose_config(
            services=["web", "database"],
            framework="python",
            include_monitoring=True,
            include_volumes=True
        )

        assert isinstance(result, dict)
        assert "compose_yaml" in result
        assert "explanation" in result
        assert "best_practices" in result

        compose_yaml = result["compose_yaml"]
        assert "version:" in compose_yaml
        assert "services:" in compose_yaml
        assert "web:" in compose_yaml
        assert "database:" in compose_yaml

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server não disponível")
    @pytest.mark.asyncio
    async def test_docker_generate_config(self):
        """Testa geração de configuração Docker completa"""
        result = await docker_generate_config(
            app_type="web_api",
            framework="python",
            security_level="production",
            include_compose=True
        )

        assert isinstance(result, dict)
        assert "dockerfile" in result
        assert "compose_yaml" in result
        assert "docker_ignore" in result
        assert "documentation" in result

        dockerfile = result["dockerfile"]
        assert "FROM" in dockerfile
        assert "WORKDIR" in dockerfile
        assert "COPY" in dockerfile
        assert "CMD" in dockerfile or "ENTRYPOINT" in dockerfile

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server não disponível")
    @pytest.mark.asyncio
    async def test_get_docker_best_practices(self):
        """Testa obtenção de melhores práticas Docker"""
        result = await get_docker_best_practices()

        assert isinstance(result, str)
        assert len(result) > 100
        assert "multi-stage" in result.lower()
        assert "security" in result.lower()
        assert "optimization" in result.lower()


class TestDockerIntegration:
    """Testes de integração do Docker Server"""

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server não disponível")
    @pytest.mark.asyncio
    async def test_full_docker_workflow(self):
        """Testa workflow completo de otimização Docker"""
        # 1. Prompt inicial simples
        initial_prompt = "Dockerizar app Python"

        # 2. Analisar prompt inicial
        analysis = await docker_analyze_prompt(initial_prompt)
        initial_score = analysis["score"]

        # 3. Melhorar prompt
        enhancement = await docker_enhance_prompt(
            prompt=initial_prompt,
            target_framework="python",
            security_level="production"
        )
        enhanced_prompt = enhancement["enhanced_prompt"]

        # 4. Analisar prompt melhorado
        enhanced_analysis = await docker_analyze_prompt(enhanced_prompt)
        enhanced_score = enhanced_analysis["score"]

        # 5. Gerar configuração completa
        config = await docker_generate_config(
            app_type="web_api",
            framework="python",
            security_level="production"
        )

        # 6. Validar Dockerfile gerado
        dockerfile_validation = await docker_validate_dockerfile(config["dockerfile"])

        # Verificar melhoria ao longo do workflow
        assert enhanced_score > initial_score
        assert len(enhanced_prompt) > len(initial_prompt)
        assert dockerfile_validation["is_valid"] is True
        assert dockerfile_validation["score"] >= 70

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server não disponível")
    @pytest.mark.asyncio
    async def test_security_optimization_workflow(self):
        """Testa workflow de otimização de segurança"""
        # Dockerfile básico sem segurança
        basic_dockerfile = """
        FROM python:3.11
        COPY . /app
        WORKDIR /app
        RUN pip install -r requirements.txt
        CMD ["python", "app.py"]
        """

        # Validar Dockerfile básico
        basic_validation = await docker_validate_dockerfile(basic_dockerfile)
        basic_security_issues = len(basic_validation["security_warnings"])

        # Gerar configuração com foco em segurança
        secure_config = await docker_generate_config(
            app_type="web_api",
            framework="python",
            security_level="hardened"
        )

        # Validar Dockerfile seguro
        secure_validation = await docker_validate_dockerfile(secure_config["dockerfile"])
        secure_security_issues = len(secure_validation["security_warnings"])

        # Configuração segura deve ter menos problemas de segurança
        assert secure_security_issues < basic_security_issues
        assert secure_validation["score"] > basic_validation["score"]


# Testes parametrizados para diferentes cenários
@pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server não disponível")
@pytest.mark.parametrize("prompt_content,expected_min_score", [
    ("Dockerizar app", 10),  # Prompt muito básico
    ("Criar Docker para aplicação Python Flask", 30),  # Prompt simples
    ("Dockerizar Python Flask com multi-stage build e segurança", 60),  # Prompt médio
    ("""Criar configuração Docker para Python Flask com:
    - Multi-stage build para otimização
    - Usuário não-root para segurança
    - Healthcheck para monitoramento
    - Cache de dependências otimizado
    - Variáveis de ambiente
    - Logs estruturados""", 80),  # Prompt completo
])
@pytest.mark.asyncio
async def test_analyze_prompt_quality_levels(prompt_content, expected_min_score):
    """Testa que diferentes qualidades de prompt resultam em scores apropriados"""
    result = await docker_analyze_prompt(prompt_content)
    assert result["score"] >= expected_min_score


# Teste de fallback quando Docker Server não está disponível
@pytest.mark.skipif(DOCKER_SERVER_AVAILABLE, reason="Docker Server está disponível")
def test_docker_server_fallback():
    """Teste de fallback quando Docker Server não está disponível"""
    assert not DOCKER_SERVER_AVAILABLE
    print("⚠️ Docker Optimizer Server não está disponível - implementação pendente")


# Fixture para mock de contexto
@pytest.fixture
def mock_context():
    """Fixture para criar mock de Context do Docker Server"""
    context = AsyncMock()
    context.info = AsyncMock()
    context.warning = AsyncMock()
    context.error = AsyncMock()
    return context


if __name__ == "__main__":
    # Execução direta para desenvolvimento
    pytest.main([__file__, "-v"])
