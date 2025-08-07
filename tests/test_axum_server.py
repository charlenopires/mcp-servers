#!/usr/bin/env python3
"""
Testes para o Axum Web Framework Server - Servidor MCP para desenvolvimento web moderno com Axum

Este módulo testa as funcionalidades do servidor Axum especializado em análise de código,
otimização de handlers, criação de middleware e geração de projetos.
"""

import pytest
from unittest.mock import AsyncMock

# Importações condicionais para fallback
try:
    from servers.axum_server import (
        AxumFeatureType,
        analyze_axum_code,
        create_axum_middleware,
        generate_axum_project,
        optimize_axum_handler,
        get_axum_best_practices
    )
    AXUM_SERVER_AVAILABLE = True
except ImportError as e:
    print(f"Axum Server não disponível: {e}")
    AXUM_SERVER_AVAILABLE = False


class TestAxumFeatureType:
    """Testes para enum AxumFeatureType"""

    @pytest.mark.skipif(not AXUM_SERVER_AVAILABLE, reason="Axum Server não disponível")
    def test_axum_feature_types(self):
        """Testa que todos os tipos de features estão definidos"""
        expected_features = [
            "routing", "handlers", "extractors", "responses",
            "middleware", "error_handling", "state_management",
            "testing", "performance", "magic_patterns"
        ]

        available_features = [feature.value for feature in AxumFeatureType]

        for feature in expected_features:
            assert feature in available_features


class TestAxumAnalysisFunctions:
    """Testes para as funções de análise do Axum Server"""

    @pytest.mark.skipif(not AXUM_SERVER_AVAILABLE, reason="Axum Server não disponível")
    @pytest.mark.asyncio
    async def test_analyze_axum_code_basic(self):
        """Testa análise básica de código Axum"""
        rust_code = """
        use axum::{Router, routing::get};
        
        async fn hello() -> &'static str {
            "Hello, World!"
        }
        
        fn app() -> Router {
            Router::new().route("/", get(hello))
        }
        """

        result = await analyze_axum_code(rust_code)

        assert isinstance(result, dict)
        assert "score" in result
        assert "patterns_detected" in result
        assert "recommendations" in result
        assert 0 <= result["score"] <= 100

    @pytest.mark.skipif(not AXUM_SERVER_AVAILABLE, reason="Axum Server não disponível")
    @pytest.mark.asyncio
    async def test_analyze_axum_code_advanced(self):
        """Testa análise de código Axum avançado"""
        rust_code = """
        use axum::{
            Router, Json, extract::{State, Path}, 
            response::{IntoResponse, Result},
            middleware::{from_fn},
            http::StatusCode
        };
        use serde::{Deserialize, Serialize};
        use std::sync::Arc;
        
        #[derive(Clone)]
        struct AppState {
            db: Arc<Database>,
        }
        
        #[derive(Deserialize)]
        struct CreateUser {
            name: String,
            email: String,
        }
        
        #[derive(Serialize)]
        struct User {
            id: u64,
            name: String,
            email: String,
        }
        
        async fn create_user(
            State(state): State<AppState>,
            Json(payload): Json<CreateUser>,
        ) -> Result<Json<User>, StatusCode> {
            // Implementação com tratamento de erro adequado
            match state.db.create_user(payload).await {
                Ok(user) => Ok(Json(user)),
                Err(_) => Err(StatusCode::INTERNAL_SERVER_ERROR),
            }
        }
        
        fn app() -> Router {
            Router::new()
                .route("/users", axum::routing::post(create_user))
                .with_state(AppState { db: Arc::new(Database::new()) })
                .layer(from_fn(logging_middleware))
        }
        """

        result = await analyze_axum_code(rust_code)

        # Código avançado deve ter score alto
        assert result["score"] >= 70
        assert len(result["patterns_detected"]) > 0

        # Verificar padrões detectados
        patterns_str = str(result["patterns_detected"]).lower()
        assert any(keyword in patterns_str for keyword in [
            "state", "extractor", "handler", "middleware"
        ])

    @pytest.mark.skipif(not AXUM_SERVER_AVAILABLE, reason="Axum Server não disponível")
    @pytest.mark.asyncio
    async def test_create_axum_middleware(self):
        """Testa criação de middleware Axum"""
        middleware_types = ["authentication",
                            "logging", "cors", "rate_limiting"]

        for middleware_type in middleware_types:
            result = await create_axum_middleware(
                middleware_type=middleware_type,
                name=f"Test{middleware_type.title()}Middleware"
            )

            assert isinstance(result, dict)
            assert "code" in result
            assert "usage_example" in result
            assert "dependencies" in result

            # Verificar que o código contém elementos esperados
            code = result["code"]
            assert "async fn" in code
            assert "middleware" in code.lower()
            assert middleware_type.replace("_", "") in code.lower()

    @pytest.mark.skipif(not AXUM_SERVER_AVAILABLE, reason="Axum Server não disponível")
    @pytest.mark.asyncio
    async def test_generate_axum_project(self):
        """Testa geração de projeto Axum"""
        project_types = ["api", "web_app", "microservice", "fullstack"]

        for project_type in project_types:
            result = await generate_axum_project(
                project_type=project_type,
                name="TestProject",
                features=["database", "authentication"]
            )

            assert isinstance(result, dict)
            assert "structure" in result
            assert "main_code" in result
            assert "cargo_toml" in result
            assert "dependencies" in result

            # Verificar estrutura do projeto
            structure = result["structure"]
            assert "src/" in structure
            assert "Cargo.toml" in structure

            # Verificar código principal
            main_code = result["main_code"]
            assert "use axum" in main_code
            assert "async fn main" in main_code

    @pytest.mark.skipif(not AXUM_SERVER_AVAILABLE, reason="Axum Server não disponível")
    @pytest.mark.asyncio
    async def test_optimize_axum_handler(self):
        """Testa otimização de handler Axum"""
        basic_handler = """
        async fn get_user(id: String) -> String {
            format!("User {}", id)
        }
        """

        result = await optimize_axum_handler(
            handler_code=basic_handler,
            optimization_focus=["error_handling", "performance"]
        )

        assert isinstance(result, dict)
        assert "optimized_code" in result
        assert "improvements" in result
        assert "explanation" in result

        optimized_code = result["optimized_code"]

        # Código otimizado deve ter melhorias
        assert len(optimized_code) > len(basic_handler)
        assert "extract::" in optimized_code or "Path" in optimized_code
        assert "Result" in optimized_code or "impl IntoResponse" in optimized_code

    @pytest.mark.skipif(not AXUM_SERVER_AVAILABLE, reason="Axum Server não disponível")
    @pytest.mark.asyncio
    async def test_get_axum_best_practices(self):
        """Testa obtenção de melhores práticas Axum"""
        result = await get_axum_best_practices()

        assert isinstance(result, dict)
        assert "routing" in result
        assert "handlers" in result
        assert "middleware" in result
        assert "error_handling" in result

        # Verificar que cada categoria tem práticas
        for category, practices in result.items():
            assert isinstance(practices, list)
            assert len(practices) > 0


class TestAxumIntegration:
    """Testes de integração do Axum Server"""

    @pytest.mark.skipif(not AXUM_SERVER_AVAILABLE, reason="Axum Server não disponível")
    @pytest.mark.asyncio
    async def test_full_development_workflow(self):
        """Testa workflow completo de desenvolvimento Axum"""
        # 1. Gerar projeto
        project = await generate_axum_project(
            project_type="api",
            name="TestAPI",
            features=["database"]
        )

        # 2. Analisar código gerado
        analysis = await analyze_axum_code(project["main_code"])

        # 3. Otimizar um handler
        sample_handler = """
        async fn get_items() -> String {
            "items".to_string()
        }
        """

        optimization = await optimize_axum_handler(
            handler_code=sample_handler,
            optimization_focus=["error_handling"]
        )

        # 4. Criar middleware
        middleware = await create_axum_middleware(
            middleware_type="logging",
            name="RequestLogger"
        )

        # Verificar que todo o workflow funcionou
        assert project["main_code"] is not None
        assert analysis["score"] > 0
        assert len(optimization["optimized_code"]) > 0
        assert len(middleware["code"]) > 0

    @pytest.mark.skipif(not AXUM_SERVER_AVAILABLE, reason="Axum Server não disponível")
    @pytest.mark.asyncio
    async def test_code_improvement_cycle(self):
        """Testa ciclo de melhoria de código"""
        # Código inicial simples
        initial_code = """
        use axum::{Router, routing::get};
        
        async fn hello() -> &'static str {
            "Hello"
        }
        
        fn app() -> Router {
            Router::new().route("/", get(hello))
        }
        """

        # 1. Analisar código inicial
        initial_analysis = await analyze_axum_code(initial_code)
        initial_score = initial_analysis["score"]

        # 2. Otimizar o handler
        optimization = await optimize_axum_handler(
            handler_code=initial_code,
            optimization_focus=["error_handling", "extractors"]
        )

        # 3. Analisar código otimizado
        optimized_analysis = await analyze_axum_code(optimization["optimized_code"])
        optimized_score = optimized_analysis["score"]

        # Verificar melhoria
        assert optimized_score >= initial_score
        assert len(optimization["improvements"]) > 0


# Testes parametrizados para diferentes cenários
@pytest.mark.skipif(not AXUM_SERVER_AVAILABLE, reason="Axum Server não disponível")
@pytest.mark.parametrize("code_quality,expected_min_score", [
    ("""
    use axum::Router;
    fn app() -> Router { Router::new() }
    """, 20),  # Código muito básico
    ("""
    use axum::{Router, routing::get, extract::Path};
    async fn handler(Path(id): Path<u32>) -> String {
        format!("ID: {}", id)
    }
    fn app() -> Router {
        Router::new().route("/users/:id", get(handler))
    }
    """, 50),  # Código intermediário
    ("""
    use axum::{
        Router, Json, extract::{State, Path}, 
        response::{Result, IntoResponse},
        http::StatusCode
    };
    use serde::{Deserialize, Serialize};
    
    #[derive(Clone)]
    struct AppState { db: Database }
    
    async fn handler(
        State(state): State<AppState>,
        Path(id): Path<u32>
    ) -> Result<Json<User>, StatusCode> {
        match state.db.get_user(id).await {
            Ok(user) => Ok(Json(user)),
            Err(_) => Err(StatusCode::NOT_FOUND)
        }
    }
    """, 75),  # Código avançado
])
@pytest.mark.asyncio
async def test_analyze_code_quality_levels(code_quality, expected_min_score):
    """Testa que diferentes qualidades de código resultam em scores apropriados"""
    result = await analyze_axum_code(code_quality)
    assert result["score"] >= expected_min_score


# Teste de fallback quando Axum Server não está disponível
@pytest.mark.skipif(AXUM_SERVER_AVAILABLE, reason="Axum Server está disponível")
def test_axum_server_fallback():
    """Teste de fallback quando Axum Server não está disponível"""
    assert not AXUM_SERVER_AVAILABLE
    print("⚠️ Axum Server não está disponível - implementação pendente")


# Fixture para mock de contexto
@pytest.fixture
def mock_context():
    """Fixture para criar mock de Context do Axum Server"""
    context = AsyncMock()
    context.info = AsyncMock()
    context.warning = AsyncMock()
    context.error = AsyncMock()
    return context


if __name__ == "__main__":
    # Execução direta para desenvolvimento
    pytest.main([__file__, "-v"])
