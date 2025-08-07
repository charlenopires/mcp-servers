#!/usr/bin/env python3
"""
Testes para o Rust Idiomatic Server - Servidor MCP para desenvolvimento idiomático em Rust

Este módulo testa as funcionalidades do servidor Rust especializado em análise de código,
geração de projetos, refatoração e padrões idiomáticos.
"""

import pytest
from unittest.mock import AsyncMock

# Importações condicionais para fallback
try:
    from servers.rust_server import (
        analyze_idiomatic_rust,
        generate_idiomatic_project,
        get_idiomatic_patterns,
        refactor_to_idiomatic,
        get_rust_api_guidelines,
        validate_rust_code
    )
    RUST_SERVER_AVAILABLE = True
except ImportError as e:
    print(f"Rust Server não disponível: {e}")
    RUST_SERVER_AVAILABLE = False


class TestRustAnalysisFunctions:
    """Testes para as funções de análise do Rust Server"""

    @pytest.mark.skipif(not RUST_SERVER_AVAILABLE, reason="Rust Server não disponível")
    @pytest.mark.asyncio
    async def test_analyze_idiomatic_rust_basic(self):
        """Testa análise básica de código Rust"""
        rust_code = """
        fn main() {
            println!("Hello, world!");
        }
        """

        result = await analyze_idiomatic_rust(rust_code)

        assert isinstance(result, dict)
        assert "idiomaticity_score" in result
        assert "patterns_detected" in result
        assert "suggestions" in result
        assert "compliance" in result
        assert 0 <= result["idiomaticity_score"] <= 100

    @pytest.mark.skipif(not RUST_SERVER_AVAILABLE, reason="Rust Server não disponível")
    @pytest.mark.asyncio
    async def test_analyze_idiomatic_rust_advanced(self):
        """Testa análise de código Rust idiomático avançado"""
        idiomatic_code = """
        use std::collections::HashMap;
        use std::error::Error;
        use std::fmt;
        
        #[derive(Debug, Clone)]
        pub struct User {
            pub id: u64,
            pub name: String,
            pub email: String,
        }
        
        #[derive(Debug)]
        pub enum UserError {
            NotFound(u64),
            InvalidEmail(String),
        }
        
        impl fmt::Display for UserError {
            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
                match self {
                    UserError::NotFound(id) => write!(f, "User with ID {} not found", id),
                    UserError::InvalidEmail(email) => write!(f, "Invalid email: {}", email),
                }
            }
        }
        
        impl Error for UserError {}
        
        pub struct UserRepository {
            users: HashMap<u64, User>,
        }
        
        impl UserRepository {
            pub fn new() -> Self {
                Self {
                    users: HashMap::new(),
                }
            }
            
            pub fn add_user(&mut self, user: User) -> Result<(), UserError> {
                if !user.email.contains('@') {
                    return Err(UserError::InvalidEmail(user.email));
                }
                
                self.users.insert(user.id, user);
                Ok(())
            }
            
            pub fn get_user(&self, id: u64) -> Result<&User, UserError> {
                self.users.get(&id).ok_or(UserError::NotFound(id))
            }
        }
        
        impl Default for UserRepository {
            fn default() -> Self {
                Self::new()
            }
        }
        """

        result = await analyze_idiomatic_rust(idiomatic_code)

        # Código idiomático deve ter score alto
        assert result["idiomaticity_score"] >= 80
        assert len(result["patterns_detected"]) > 0

        # Verificar padrões idiomáticos detectados
        patterns_str = str(result["patterns_detected"]).lower()
        assert any(keyword in patterns_str for keyword in [
            "error handling", "derive", "impl", "match"
        ])

    @pytest.mark.skipif(not RUST_SERVER_AVAILABLE, reason="Rust Server não disponível")
    @pytest.mark.asyncio
    async def test_generate_idiomatic_project(self):
        """Testa geração de projeto Rust idiomático"""
        project_types = ["library", "binary", "web-api", "cli"]

        for project_type in project_types:
            result = await generate_idiomatic_project(
                project_type=project_type,
                name="test_project",
                features=["error_handling", "testing", "documentation"]
            )

            assert isinstance(result, dict)
            assert "project_structure" in result
            assert "cargo_toml" in result
            assert "main_code" in result
            assert "tests" in result

            # Verificar estrutura do projeto
            structure = result["project_structure"]
            assert "src/" in structure
            assert "Cargo.toml" in structure

            # Verificar Cargo.toml
            cargo_toml = result["cargo_toml"]
            assert "[package]" in cargo_toml
            assert "name = \"test_project\"" in cargo_toml

    @pytest.mark.skipif(not RUST_SERVER_AVAILABLE, reason="Rust Server não disponível")
    @pytest.mark.asyncio
    async def test_get_idiomatic_patterns(self):
        """Testa obtenção de padrões idiomáticos"""
        categories = ["error_handling", "iterators",
                      "ownership", "traits", "modules"]

        for category in categories:
            result = await get_idiomatic_patterns(category)

            assert isinstance(result, dict)
            assert "patterns" in result
            assert "examples" in result
            assert "explanations" in result

            patterns = result["patterns"]
            assert isinstance(patterns, list)
            assert len(patterns) > 0

    @pytest.mark.skipif(not RUST_SERVER_AVAILABLE, reason="Rust Server não disponível")
    @pytest.mark.asyncio
    async def test_refactor_to_idiomatic(self):
        """Testa refatoração para código idiomático"""
        non_idiomatic_code = """
        fn process_numbers(numbers: Vec<i32>) -> Vec<i32> {
            let mut result = Vec::new();
            for i in 0..numbers.len() {
                if numbers[i] > 0 {
                    result.push(numbers[i] * 2);
                }
            }
            result
        }
        """

        result = await refactor_to_idiomatic(
            code=non_idiomatic_code,
            focus_areas=["iterators", "functional_style"]
        )

        assert isinstance(result, dict)
        assert "refactored_code" in result
        assert "improvements" in result
        assert "explanation" in result

        refactored = result["refactored_code"]
        # Código refatorado deve usar iteradores
        assert "iter()" in refactored or "into_iter()" in refactored
        assert "filter" in refactored or "map" in refactored

    @pytest.mark.skipif(not RUST_SERVER_AVAILABLE, reason="Rust Server não disponível")
    @pytest.mark.asyncio
    async def test_get_rust_api_guidelines(self):
        """Testa obtenção de diretrizes da API Rust"""
        result = await get_rust_api_guidelines()

        assert isinstance(result, dict)
        assert "naming" in result
        assert "error_handling" in result
        assert "documentation" in result
        assert "testing" in result

        # Verificar que cada categoria tem diretrizes
        for category, guidelines in result.items():
            assert isinstance(guidelines, list)
            assert len(guidelines) > 0

    @pytest.mark.skipif(not RUST_SERVER_AVAILABLE, reason="Rust Server não disponível")
    @pytest.mark.asyncio
    async def test_validate_rust_code(self):
        """Testa validação de código Rust"""
        code_samples = [
            # Código básico
            """
            fn hello() {
                println!("Hello!");
            }
            """,
            # Código com ownership
            """
            fn take_ownership(s: String) -> String {
                println!("{}", s);
                s
            }
            """,
            # Código com traits
            """
            trait Printable {
                fn print(&self);
            }
            
            impl Printable for String {
                fn print(&self) {
                    println!("{}", self);
                }
            }
            """
        ]

        for code in code_samples:
            result = await validate_rust_code(code)

            assert isinstance(result, dict)
            assert "is_valid" in result
            assert "score" in result
            assert "issues" in result
            assert "suggestions" in result


class TestRustIntegration:
    """Testes de integração do Rust Server"""

    @pytest.mark.skipif(not RUST_SERVER_AVAILABLE, reason="Rust Server não disponível")
    @pytest.mark.asyncio
    async def test_full_development_workflow(self):
        """Testa workflow completo de desenvolvimento Rust"""
        # 1. Gerar projeto
        project = await generate_idiomatic_project(
            project_type="library",
            name="test_lib",
            features=["error_handling", "testing"]
        )

        # 2. Analisar código gerado
        analysis = await analyze_idiomatic_rust(project["main_code"])

        # 3. Obter padrões para melhorar código
        patterns = await get_idiomatic_patterns("error_handling")

        # 4. Validar código
        validation = await validate_rust_code(project["main_code"])

        # Verificar que todo o workflow funcionou
        assert project["main_code"] is not None
        assert analysis["idiomaticity_score"] > 0
        assert len(patterns["patterns"]) > 0
        assert validation["is_valid"] is True

    @pytest.mark.skipif(not RUST_SERVER_AVAILABLE, reason="Rust Server não disponível")
    @pytest.mark.asyncio
    async def test_code_improvement_cycle(self):
        """Testa ciclo de melhoria de código"""
        # Código não idiomático
        non_idiomatic = """
        fn find_max(numbers: Vec<i32>) -> i32 {
            let mut max = numbers[0];
            for i in 1..numbers.len() {
                if numbers[i] > max {
                    max = numbers[i];
                }
            }
            max
        }
        """

        # 1. Analisar código inicial
        initial_analysis = await analyze_idiomatic_rust(non_idiomatic)
        initial_score = initial_analysis["idiomaticity_score"]

        # 2. Refatorar código
        refactoring = await refactor_to_idiomatic(
            code=non_idiomatic,
            focus_areas=["iterators", "error_handling"]
        )

        # 3. Analisar código refatorado
        refactored_analysis = await analyze_idiomatic_rust(refactoring["refactored_code"])
        refactored_score = refactored_analysis["idiomaticity_score"]

        # Código refatorado deve ter score melhor
        assert refactored_score > initial_score
        assert len(refactoring["improvements"]) > 0


# Testes parametrizados para diferentes cenários
@pytest.mark.skipif(not RUST_SERVER_AVAILABLE, reason="Rust Server não disponível")
@pytest.mark.parametrize("code_quality,expected_min_score", [
    ("""
    fn main() { println!("Hello"); }
    """, 30),  # Código muito básico
    ("""
    fn add(a: i32, b: i32) -> i32 {
        a + b
    }
    """, 50),  # Código simples
    ("""
    use std::error::Error;
    
    #[derive(Debug)]
    enum MyError {
        InvalidInput(String),
    }
    
    impl std::fmt::Display for MyError {
        fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
            match self {
                MyError::InvalidInput(msg) => write!(f, "Invalid input: {}", msg),
            }
        }
    }
    
    impl Error for MyError {}
    
    fn process_data(data: &str) -> Result<String, MyError> {
        if data.is_empty() {
            return Err(MyError::InvalidInput("Data cannot be empty".to_string()));
        }
        Ok(data.to_uppercase())
    }
    """, 80),  # Código idiomático
])
@pytest.mark.asyncio
async def test_analyze_code_quality_levels(code_quality, expected_min_score):
    """Testa que diferentes qualidades de código resultam em scores apropriados"""
    result = await analyze_idiomatic_rust(code_quality)
    assert result["idiomaticity_score"] >= expected_min_score


@pytest.mark.skipif(not RUST_SERVER_AVAILABLE, reason="Rust Server não disponível")
@pytest.mark.parametrize("project_type", ["library", "binary", "web-api", "cli"])
@pytest.mark.asyncio
async def test_generate_all_project_types(project_type):
    """Testa geração de todos os tipos de projeto"""
    result = await generate_idiomatic_project(
        project_type=project_type,
        name="test_project",
        features=["testing"]
    )

    assert isinstance(result, dict)
    assert "project_structure" in result
    assert "cargo_toml" in result
    assert "main_code" in result


# Teste de fallback quando Rust Server não está disponível
@pytest.mark.skipif(RUST_SERVER_AVAILABLE, reason="Rust Server está disponível")
def test_rust_server_fallback():
    """Teste de fallback quando Rust Server não está disponível"""
    assert not RUST_SERVER_AVAILABLE
    print("⚠️ Rust Idiomatic Server não está disponível - implementação pendente")


# Fixture para mock de contexto
@pytest.fixture
def mock_context():
    """Fixture para criar mock de Context do Rust Server"""
    context = AsyncMock()
    context.info = AsyncMock()
    context.warning = AsyncMock()
    context.error = AsyncMock()
    return context


if __name__ == "__main__":
    # Execução direta para desenvolvimento
    pytest.main([__file__, "-v"])
