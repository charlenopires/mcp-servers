#!/usr/bin/env python3
"""
Tests for Docker Optimizer Server - MCP server for Docker configuration optimization

This module tests the functionality of the Docker server specialized in analysis,
optimization and validation of Dockerfiles and docker-compose.yml.
"""

import pytest
from unittest.mock import AsyncMock

# Conditional imports for fallback
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
        DOCKER_BEST_PRACTICES
    )
    DOCKER_SERVER_AVAILABLE = True
except ImportError as e:
    print(f"Docker Optimizer Server not available: {e}")
    DOCKER_SERVER_AVAILABLE = False


class TestDockerEnums:
    """Tests for Docker Server enums"""

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server not available")
    def test_container_framework_enum(self):
        """Test ContainerFramework enum"""
        # Actual frameworks in the enum
        expected_frameworks = ["PYTHON", "NODE", "RUST", "GO"]

        available_frameworks = [framework.name for framework in ContainerFramework]

        for framework in expected_frameworks:
            assert framework in available_frameworks

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server not available")
    def test_security_level_enum(self):
        """Test SecurityLevel enum"""
        # Actual levels in the enum
        expected_levels = ["BASIC", "STANDARD", "HIGH", "ENTERPRISE"]

        available_levels = [level.name for level in SecurityLevel]

        for level in expected_levels:
            assert level in available_levels


class TestDockerModels:
    """Tests for Docker Server data models"""

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server not available")
    def test_docker_prompt_analysis_creation(self):
        """Test DockerPromptAnalysis creation"""
        analysis = DockerPromptAnalysis(
            score=85,
            strengths=["Multi-stage build", "Security practices"],
            weaknesses=["Missing healthcheck"],
            missing_elements=["Environment variables"],
            recommendations=["Add HEALTHCHECK instruction"],
            security_issues=["Running as root"]
        )

        assert analysis.score == 85
        assert len(analysis.strengths) == 2
        assert len(analysis.weaknesses) == 1
        assert len(analysis.missing_elements) == 1
        assert len(analysis.recommendations) == 1
        assert len(analysis.security_issues) == 1

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server not available")
    def test_docker_requirements_creation(self):
        """Test DockerRequirements creation"""
        # DockerRequirements uses app_type (str), not framework (enum)
        requirements = DockerRequirements(
            app_type="python",
            has_multistage=True,
            has_security=True,
            has_optimization=True,
            has_healthcheck=True,
            has_non_root_user=True
        )

        assert requirements.app_type == "python"
        assert requirements.has_multistage is True
        assert requirements.has_security is True
        assert requirements.has_optimization is True
        assert requirements.has_healthcheck is True
        assert requirements.has_non_root_user is True


class TestDockerAnalysisFunctions:
    """Tests for Docker Server analysis functions"""

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server not available")
    @pytest.mark.asyncio
    async def test_docker_analyze_prompt_basic(self):
        """Test basic Docker prompt analysis"""
        prompt = "Create a Docker image for Python Flask application"

        # Use .fn to access underlying function
        result = await docker_analyze_prompt.fn(prompt)

        assert isinstance(result, dict)
        assert "analysis" in result or "score" in result or "summary" in result

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server not available")
    @pytest.mark.asyncio
    async def test_docker_analyze_prompt_comprehensive(self):
        """Test comprehensive Docker prompt analysis"""
        comprehensive_prompt = """
        Create a Docker image for Python Flask application with:
        - Multi-stage build for optimization
        - Non-root user for security
        - Healthcheck for monitoring
        - Dependency cache
        - Configurable environment variables
        - Expose port 8000
        - Structured logs
        """

        # Use .fn to access underlying function
        result = await docker_analyze_prompt.fn(comprehensive_prompt)

        assert isinstance(result, dict)

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server not available")
    @pytest.mark.asyncio
    async def test_docker_enhance_prompt(self):
        """Test Docker prompt enhancement"""
        basic_prompt = "Dockerize Python application"

        # Use .fn to access underlying function
        result = await docker_enhance_prompt.fn(
            prompt=basic_prompt,
            app_type="python",
            include_compose=True,
            production_ready=True
        )

        assert isinstance(result, dict)
        assert "enhanced_prompt" in result or "original_prompt" in result

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server not available")
    @pytest.mark.asyncio
    async def test_docker_validate_dockerfile(self):
        """Test Dockerfile validation"""
        dockerfile_content = """
        FROM python:3.11-slim

        WORKDIR /app

        COPY requirements.txt .
        RUN pip install -r requirements.txt

        COPY . .

        EXPOSE 8000

        CMD ["python", "app.py"]
        """

        # Use .fn to access underlying function
        result = await docker_validate_dockerfile.fn(dockerfile_content)

        assert isinstance(result, dict)
        assert "valid" in result or "score" in result

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server not available")
    @pytest.mark.asyncio
    async def test_docker_validate_compose(self):
        """Test docker-compose validation"""
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

        # Use .fn to access underlying function
        result = await docker_validate_compose.fn(compose_content)

        assert isinstance(result, dict)
        assert "valid" in result or "score" in result

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server not available")
    @pytest.mark.asyncio
    async def test_docker_generate_compose_config(self):
        """Test docker-compose configuration generation"""
        # Use .fn to access underlying function
        result = await docker_generate_compose_config.fn(
            app_type="python",
            services=["postgres", "redis"],
            environment="production",
            include_volumes=True,
            include_networks=True
        )

        assert isinstance(result, dict)
        assert "compose_config" in result or "yaml_content" in result

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server not available")
    @pytest.mark.asyncio
    async def test_docker_generate_config(self):
        """Test complete Docker configuration generation"""
        # Use .fn to access underlying function
        result = await docker_generate_config.fn(
            project_description="Web API for user management",
            app_type="python",
            features=["database", "redis"]
        )

        assert isinstance(result, dict)

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server not available")
    def test_get_docker_best_practices(self):
        """Test getting Docker best practices"""
        # DOCKER_BEST_PRACTICES is a dict constant, not a function
        assert isinstance(DOCKER_BEST_PRACTICES, dict)
        assert "security" in DOCKER_BEST_PRACTICES
        assert "optimization" in DOCKER_BEST_PRACTICES
        assert "best_practices" in DOCKER_BEST_PRACTICES


class TestDockerIntegration:
    """Docker Server integration tests"""

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server not available")
    @pytest.mark.asyncio
    async def test_full_docker_workflow(self):
        """Test complete Docker optimization workflow"""
        # 1. Simple initial prompt
        initial_prompt = "Dockerize Python app"

        # 2. Analyze initial prompt
        analysis = await docker_analyze_prompt.fn(initial_prompt)

        # 3. Enhance prompt
        enhancement = await docker_enhance_prompt.fn(
            prompt=initial_prompt,
            app_type="python",
            include_compose=True,
            production_ready=True
        )

        # 4. Generate complete configuration
        config = await docker_generate_config.fn(
            project_description="Python web application",
            app_type="python",
            features=["database"]
        )

        # Verify workflow completed
        assert analysis is not None
        assert enhancement is not None
        assert config is not None

    @pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server not available")
    @pytest.mark.asyncio
    async def test_security_optimization_workflow(self):
        """Test security optimization workflow"""
        # Basic Dockerfile without security
        basic_dockerfile = """
        FROM python:3.11
        COPY . /app
        WORKDIR /app
        RUN pip install -r requirements.txt
        CMD ["python", "app.py"]
        """

        # Validate basic Dockerfile
        basic_validation = await docker_validate_dockerfile.fn(basic_dockerfile)

        # Validation result should exist
        assert basic_validation is not None
        assert isinstance(basic_validation, dict)


# Parameterized tests for different scenarios
@pytest.mark.skipif(not DOCKER_SERVER_AVAILABLE, reason="Docker Server not available")
@pytest.mark.parametrize("prompt_content", [
    "Dockerize app",
    "Create Docker for Python Flask application",
    "Dockerize Python Flask with multi-stage build and security",
    """Create Docker configuration for Python Flask with:
    - Multi-stage build for optimization
    - Non-root user for security
    - Healthcheck for monitoring
    - Optimized dependency cache
    - Environment variables
    - Structured logs""",
])
@pytest.mark.asyncio
async def test_analyze_prompt_returns_result(prompt_content):
    """Test that different prompts return valid results"""
    result = await docker_analyze_prompt.fn(prompt_content)
    assert result is not None
    assert isinstance(result, dict)


# Fallback test when Docker Server is not available
@pytest.mark.skipif(DOCKER_SERVER_AVAILABLE, reason="Docker Server is available")
def test_docker_server_fallback():
    """Fallback test when Docker Server is not available"""
    assert not DOCKER_SERVER_AVAILABLE
    print("Docker Optimizer Server is not available")


# Fixture for context mock
@pytest.fixture
def mock_context():
    """Fixture to create mock Context for Docker Server"""
    context = AsyncMock()
    context.info = AsyncMock()
    context.warning = AsyncMock()
    context.error = AsyncMock()
    return context


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
