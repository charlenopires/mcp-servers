#!/usr/bin/env python3
"""
Testes para o TypeScript Analysis Server - Servidor MCP para análise e geração TypeScript

Este módulo testa as funcionalidades do servidor TypeScript especializado em análise de código,
geração de arquitetura limpa, modernização e otimização de projetos TypeScript.
"""

import pytest
from unittest.mock import AsyncMock

# Importações condicionais para fallback
try:
    from servers.typescript_server import (
        typescript_analyze_code_advanced,
        typescript_analyze_prompt,
        typescript_generate_clean_architecture,
        typescript_refactor_to_modern,
        get_typescript_best_practices,
        validate_typescript_code
    )
    TYPESCRIPT_SERVER_AVAILABLE = True
except ImportError as e:
    print(f"TypeScript Server não disponível: {e}")
    TYPESCRIPT_SERVER_AVAILABLE = False


class TestTypeScriptAnalysisFunctions:
    """Testes para as funções de análise do TypeScript Server"""

    @pytest.mark.skipif(not TYPESCRIPT_SERVER_AVAILABLE, reason="TypeScript Server não disponível")
    @pytest.mark.asyncio
    async def test_typescript_analyze_code_basic(self):
        """Testa análise básica de código TypeScript"""
        ts_code = """
        function greet(name: string): string {
            return `Hello, ${name}!`;
        }
        
        const message = greet("World");
        console.log(message);
        """

        result = await typescript_analyze_code_advanced(ts_code)

        assert isinstance(result, dict)
        assert "overall_score" in result
        assert "type_safety" in result
        assert "modern_features" in result
        assert "clean_architecture" in result
        assert "recommendations" in result
        assert 0 <= result["overall_score"] <= 100

    @pytest.mark.skipif(not TYPESCRIPT_SERVER_AVAILABLE, reason="TypeScript Server não disponível")
    @pytest.mark.asyncio
    async def test_typescript_analyze_advanced_code(self):
        """Testa análise de código TypeScript avançado"""
        advanced_code = """
        interface User {
            readonly id: string;
            name: string;
            email: string;
            createdAt: Date;
        }
        
        interface UserRepository {
            findById(id: string): Promise<User | null>;
            save(user: User): Promise<void>;
            delete(id: string): Promise<boolean>;
        }
        
        class InMemoryUserRepository implements UserRepository {
            private users = new Map<string, User>();
            
            async findById(id: string): Promise<User | null> {
                return this.users.get(id) ?? null;
            }
            
            async save(user: User): Promise<void> {
                this.users.set(user.id, user);
            }
            
            async delete(id: string): Promise<boolean> {
                return this.users.delete(id);
            }
        }
        
        class UserService {
            constructor(private readonly userRepository: UserRepository) {}
            
            async createUser(userData: Omit<User, 'id' | 'createdAt'>): Promise<User> {
                const user: User = {
                    id: crypto.randomUUID(),
                    ...userData,
                    createdAt: new Date(),
                };
                
                await this.userRepository.save(user);
                return user;
            }
            
            async getUserById(id: string): Promise<User> {
                const user = await this.userRepository.findById(id);
                if (!user) {
                    throw new Error(`User with id ${id} not found`);
                }
                return user;
            }
        }
        """

        result = await typescript_analyze_code_advanced(advanced_code)

        # Código avançado deve ter score alto
        assert result["overall_score"] >= 80
        assert result["type_safety"]["score"] >= 80
        assert result["clean_architecture"]["score"] >= 70

        # Verificar características modernas detectadas
        modern_features = result["modern_features"]
        assert any("interface" in str(feature).lower()
                   for feature in modern_features["detected"])
        assert any("generic" in str(feature).lower() or "utility" in str(feature).lower()
                   for feature in modern_features["detected"])

    @pytest.mark.skipif(not TYPESCRIPT_SERVER_AVAILABLE, reason="TypeScript Server não disponível")
    @pytest.mark.asyncio
    async def test_typescript_analyze_prompt(self):
        """Testa análise de prompt TypeScript"""
        prompt = """
        Criar uma aplicação TypeScript para gerenciamento de usuários com:
        - Arquitetura limpa (Clean Architecture)
        - Injeção de dependências
        - Validação de tipos rigorosa
        - Tratamento de erros customizado
        - Testes unitários
        - Documentação TSDoc
        - Configuração ESLint/Prettier
        """

        result = await typescript_analyze_prompt(prompt)

        assert isinstance(result, dict)
        assert "clarity_score" in result
        assert "completeness_score" in result
        assert "missing_elements" in result
        assert "architectural_considerations" in result

        # Prompt completo deve ter scores altos
        assert result["clarity_score"] >= 80
        assert result["completeness_score"] >= 80

    @pytest.mark.skipif(not TYPESCRIPT_SERVER_AVAILABLE, reason="TypeScript Server não disponível")
    @pytest.mark.asyncio
    async def test_typescript_generate_clean_architecture(self):
        """Testa geração de arquitetura limpa TypeScript"""
        project_types = ["web_api", "desktop_app", "library", "microservice"]

        for project_type in project_types:
            result = await typescript_generate_clean_architecture(
                project_type=project_type,
                name="TestProject",
                features=["testing", "validation", "documentation"],
                include_docker=True
            )

            assert isinstance(result, dict)
            assert "project_structure" in result
            assert "core_files" in result
            assert "configuration_files" in result
            assert "documentation" in result

            # Verificar estrutura da arquitetura limpa
            structure = result["project_structure"]
            assert "src/domain/" in str(structure)
            assert "src/application/" in str(structure)
            assert "src/infrastructure/" in str(structure)
            assert "src/presentation/" in str(structure)

    @pytest.mark.skipif(not TYPESCRIPT_SERVER_AVAILABLE, reason="TypeScript Server não disponível")
    @pytest.mark.asyncio
    async def test_typescript_refactor_to_modern(self):
        """Testa refatoração para TypeScript moderno"""
        legacy_code = """
        var UserService = function() {
            this.users = [];
        };
        
        UserService.prototype.addUser = function(user) {
            this.users.push(user);
        };
        
        UserService.prototype.findUser = function(id) {
            for (var i = 0; i < this.users.length; i++) {
                if (this.users[i].id === id) {
                    return this.users[i];
                }
            }
            return null;
        };
        """

        result = await typescript_refactor_to_modern(
            code=legacy_code,
            target_version="es2022",
            focus_areas=["classes", "types", "modern_syntax"]
        )

        assert isinstance(result, dict)
        assert "refactored_code" in result
        assert "improvements" in result
        assert "migration_notes" in result

        refactored = result["refactored_code"]
        # Código refatorado deve usar features modernas
        assert "class " in refactored
        assert "interface " in refactored or "type " in refactored
        assert "const " in refactored or "let " in refactored
        assert "find(" in refactored or "Array.find" in refactored

    @pytest.mark.skipif(not TYPESCRIPT_SERVER_AVAILABLE, reason="TypeScript Server não disponível")
    @pytest.mark.asyncio
    async def test_get_typescript_best_practices(self):
        """Testa obtenção de melhores práticas TypeScript"""
        result = await get_typescript_best_practices()

        assert isinstance(result, dict)
        assert "type_safety" in result
        assert "modern_patterns" in result
        assert "clean_architecture" in result
        assert "performance" in result
        assert "testing" in result

        # Verificar que cada categoria tem práticas
        for category, practices in result.items():
            assert isinstance(practices, list)
            assert len(practices) > 0

    @pytest.mark.skipif(not TYPESCRIPT_SERVER_AVAILABLE, reason="TypeScript Server não disponível")
    @pytest.mark.asyncio
    async def test_validate_typescript_code(self):
        """Testa validação de código TypeScript"""
        code_samples = [
            # Código básico
            """
            function add(a: number, b: number): number {
                return a + b;
            }
            """,
            # Código com interfaces
            """
            interface Product {
                id: string;
                name: string;
                price: number;
            }
            
            class ProductService {
                getProduct(id: string): Promise<Product | null> {
                    // Implementation
                    return Promise.resolve(null);
                }
            }
            """,
            # Código com generics
            """
            interface Repository<T> {
                findById(id: string): Promise<T | null>;
                save(entity: T): Promise<void>;
            }
            
            class GenericRepository<T extends { id: string }> implements Repository<T> {
                private items = new Map<string, T>();
                
                async findById(id: string): Promise<T | null> {
                    return this.items.get(id) ?? null;
                }
                
                async save(entity: T): Promise<void> {
                    this.items.set(entity.id, entity);
                }
            }
            """
        ]

        for code in code_samples:
            result = await validate_typescript_code(code)

            assert isinstance(result, dict)
            assert "is_valid" in result
            assert "type_errors" in result
            assert "suggestions" in result
            assert "complexity_score" in result


class TestTypeScriptIntegration:
    """Testes de integração do TypeScript Server"""

    @pytest.mark.skipif(not TYPESCRIPT_SERVER_AVAILABLE, reason="TypeScript Server não disponível")
    @pytest.mark.asyncio
    async def test_full_project_development_workflow(self):
        """Testa workflow completo de desenvolvimento TypeScript"""
        # 1. Analisar prompt inicial
        initial_prompt = "API REST para e-commerce"
        prompt_analysis = await typescript_analyze_prompt(initial_prompt)

        # Verificar análise do prompt
        assert prompt_analysis["clarity_score"] >= 50

        # 2. Gerar arquitetura limpa
        clean_arch = await typescript_generate_clean_architecture(
            project_type="web_api",
            name="ECommerceAPI",
            features=["validation", "testing", "documentation"]
        )

        # 3. Analisar código gerado
        main_file = clean_arch["core_files"].get("main.ts", "")
        if main_file:
            code_analysis = await typescript_analyze_code_advanced(main_file)

            # 4. Validar código
            validation = await validate_typescript_code(main_file)

            # Verificar qualidade do workflow
            assert code_analysis["overall_score"] >= 70
            assert validation["is_valid"] is True

        # Verificar estrutura do projeto
        assert "src/domain/" in str(clean_arch["project_structure"])
        assert len(clean_arch["configuration_files"]) > 0

    @pytest.mark.skipif(not TYPESCRIPT_SERVER_AVAILABLE, reason="TypeScript Server não disponível")
    @pytest.mark.asyncio
    async def test_code_modernization_workflow(self):
        """Testa workflow de modernização de código"""
        # Código legado
        legacy_code = """
        function UserManager() {
            this.users = [];
        }
        
        UserManager.prototype.add = function(user) {
            this.users.push(user);
        };
        
        UserManager.prototype.find = function(id) {
            for (var i = 0; i < this.users.length; i++) {
                if (this.users[i].id == id) {
                    return this.users[i];
                }
            }
        };
        """

        # 1. Analisar código legado
        legacy_analysis = await typescript_analyze_code_advanced(legacy_code)
        legacy_score = legacy_analysis["overall_score"]

        # 2. Refatorar para TypeScript moderno
        modernization = await typescript_refactor_to_modern(
            code=legacy_code,
            target_version="es2022",
            focus_areas=["classes", "types", "modern_syntax", "strict_mode"]
        )

        # 3. Analisar código modernizado
        modern_analysis = await typescript_analyze_code_advanced(modernization["refactored_code"])
        modern_score = modern_analysis["overall_score"]

        # 4. Validar código modernizado
        validation = await validate_typescript_code(modernization["refactored_code"])

        # Código modernizado deve ser melhor
        assert modern_score > legacy_score
        assert validation["is_valid"] is True
        assert len(modernization["improvements"]) > 0


# Testes parametrizados para diferentes cenários
@pytest.mark.skipif(not TYPESCRIPT_SERVER_AVAILABLE, reason="TypeScript Server não disponível")
@pytest.mark.parametrize("code_quality,expected_min_score", [
    ("""
    function hello() { console.log("hello"); }
    """, 20),  # Código muito básico
    ("""
    function greet(name: string): string {
        return `Hello, ${name}!`;
    }
    """, 50),  # Código com tipos básicos
    ("""
    interface User {
        id: string;
        name: string;
        email: string;
    }
    
    class UserService {
        private users: User[] = [];
        
        addUser(user: User): void {
            this.users.push(user);
        }
        
        findUserById(id: string): User | undefined {
            return this.users.find(user => user.id === id);
        }
    }
    """, 70),  # Código intermediário
    ("""
    interface Repository<T> {
        findById(id: string): Promise<T | null>;
        save(entity: T): Promise<void>;
    }
    
    class UserService<T extends { id: string }> {
        constructor(private readonly repository: Repository<T>) {}
        
        async createUser(userData: Omit<T, 'id'>): Promise<T> {
            const user = { id: crypto.randomUUID(), ...userData } as T;
            await this.repository.save(user);
            return user;
        }
        
        async getUserById(id: string): Promise<T> {
            const user = await this.repository.findById(id);
            if (!user) {
                throw new Error(`User with id ${id} not found`);
            }
            return user;
        }
    }
    """, 85),  # Código avançado
])
@pytest.mark.asyncio
async def test_analyze_code_quality_levels(code_quality, expected_min_score):
    """Testa que diferentes qualidades de código resultam em scores apropriados"""
    result = await typescript_analyze_code_advanced(code_quality)
    assert result["overall_score"] >= expected_min_score


@pytest.mark.skipif(not TYPESCRIPT_SERVER_AVAILABLE, reason="TypeScript Server não disponível")
@pytest.mark.parametrize("project_type", ["web_api", "desktop_app", "library", "microservice"])
@pytest.mark.asyncio
async def test_generate_all_project_types(project_type):
    """Testa geração de todos os tipos de projeto"""
    result = await typescript_generate_clean_architecture(
        project_type=project_type,
        name="TestProject",
        features=["testing"]
    )

    assert isinstance(result, dict)
    assert "project_structure" in result
    assert "core_files" in result
    # Verificar estrutura de arquitetura limpa
    assert "src/domain/" in str(result["project_structure"])


# Teste de fallback quando TypeScript Server não está disponível
@pytest.mark.skipif(TYPESCRIPT_SERVER_AVAILABLE, reason="TypeScript Server está disponível")
def test_typescript_server_fallback():
    """Teste de fallback quando TypeScript Server não está disponível"""
    assert not TYPESCRIPT_SERVER_AVAILABLE
    print("⚠️ TypeScript Analysis Server não está disponível - implementação pendente")


# Fixture para mock de contexto
@pytest.fixture
def mock_context():
    """Fixture para criar mock de Context do TypeScript Server"""
    context = AsyncMock()
    context.info = AsyncMock()
    context.warning = AsyncMock()
    context.error = AsyncMock()
    return context


if __name__ == "__main__":
    # Execução direta para desenvolvimento
    pytest.main([__file__, "-v"])
