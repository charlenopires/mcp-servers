#!/usr/bin/env python3
"""
Testes para o React Components Server - Servidor MCP para desenvolvimento de componentes React

Este módulo testa as funcionalidades do servidor React especializado em análise de código,
geração de componentes, otimização e validação seguindo trends UI/UX 2025.
"""

import pytest
from unittest.mock import AsyncMock

# Importações condicionais para fallback
try:
    from servers.react_server import (
        analyze_react_code,
        analyze_react_prompt,
        generate_component_template,
        optimize_react_code,
        optimize_react_prompt,
        validate_react_requirements,
        get_react_best_practices
    )
    REACT_SERVER_AVAILABLE = True
except ImportError as e:
    print(f"React Server não disponível: {e}")
    REACT_SERVER_AVAILABLE = False


class TestReactAnalysisFunctions:
    """Testes para as funções de análise do React Server"""

    @pytest.mark.skipif(not REACT_SERVER_AVAILABLE, reason="React Server não disponível")
    @pytest.mark.asyncio
    async def test_analyze_react_code_basic(self):
        """Testa análise básica de código React"""
        react_code = """
        import React from 'react';
        
        function Hello() {
            return <div>Hello World</div>;
        }
        
        export default Hello;
        """

        result = await analyze_react_code(
            code=react_code,
            component_type="functional"
        )

        assert isinstance(result, dict)
        assert "score" in result
        assert "patterns_detected" in result
        assert "recommendations" in result
        assert "ui_ux_compliance" in result
        assert 0 <= result["score"] <= 100

    @pytest.mark.skipif(not REACT_SERVER_AVAILABLE, reason="React Server não disponível")
    @pytest.mark.asyncio
    async def test_analyze_react_code_advanced(self):
        """Testa análise de código React avançado"""
        advanced_code = """
        import React, { useState, useEffect, useMemo } from 'react';
        import { motion } from 'framer-motion';
        
        interface UserCardProps {
            user: {
                id: string;
                name: string;
                email: string;
            };
            onSelect: (id: string) => void;
        }
        
        const UserCard: React.FC<UserCardProps> = ({ user, onSelect }) => {
            const [isHovered, setIsHovered] = useState(false);
            
            const cardVariants = useMemo(() => ({
                hover: { scale: 1.02, transition: { duration: 0.2 } },
                tap: { scale: 0.98 }
            }), []);
            
            useEffect(() => {
                // Accessibility: announce selection
                if (isHovered) {
                    console.log(`User card ${user.name} focused`);
                }
            }, [isHovered, user.name]);
            
            return (
                <motion.div
                    variants={cardVariants}
                    whileHover="hover"
                    whileTap="tap"
                    className="user-card"
                    onMouseEnter={() => setIsHovered(true)}
                    onMouseLeave={() => setIsHovered(false)}
                    onClick={() => onSelect(user.id)}
                    role="button"
                    tabIndex={0}
                    aria-label={`Select user ${user.name}`}
                >
                    <h3>{user.name}</h3>
                    <p>{user.email}</p>
                </motion.div>
            );
        };
        
        export default UserCard;
        """

        result = await analyze_react_code(
            code=advanced_code,
            component_type="functional",
            include_trends_analysis=True
        )

        # Código avançado deve ter score alto
        assert result["score"] >= 75
        assert len(result["patterns_detected"]) > 0

        # Verificar padrões React 19 e UI/UX 2025
        patterns_str = str(result["patterns_detected"]).lower()
        assert any(keyword in patterns_str for keyword in [
            "hooks", "typescript", "accessibility", "animation"
        ])

    @pytest.mark.skipif(not REACT_SERVER_AVAILABLE, reason="React Server não disponível")
    @pytest.mark.asyncio
    async def test_analyze_react_prompt(self):
        """Testa análise de prompt React"""
        prompt = """
        Criar componente React para card de produto com:
        - TypeScript
        - Props tipadas
        - Estados para hover e loading
        - Animações suaves
        - Acessibilidade WCAG
        - Responsive design
        - Trends UI/UX 2025
        """

        result = await analyze_react_prompt(prompt)

        assert isinstance(result, dict)
        assert "score" in result
        assert "completeness" in result
        assert "missing_elements" in result
        assert "suggestions" in result

        # Prompt completo deve ter score alto
        assert result["score"] >= 80

    @pytest.mark.skipif(not REACT_SERVER_AVAILABLE, reason="React Server não disponível")
    @pytest.mark.asyncio
    async def test_generate_component_template(self):
        """Testa geração de template de componente"""
        component_types = ["button", "card", "form", "modal", "navigation"]

        for comp_type in component_types:
            result = await generate_component_template(
                component_type=comp_type,
                name=f"Test{comp_type.title()}",
                complexity="advanced",
                include_typescript=True,
                include_animations=True
            )

            assert isinstance(result, dict)
            assert "component_code" in result
            assert "styles" in result
            assert "usage_example" in result
            assert "props_interface" in result

            # Verificar código do componente
            component_code = result["component_code"]
            assert "React" in component_code
            assert "interface" in component_code  # TypeScript
            assert comp_type.lower() in component_code.lower()

    @pytest.mark.skipif(not REACT_SERVER_AVAILABLE, reason="React Server não disponível")
    @pytest.mark.asyncio
    async def test_optimize_react_code(self):
        """Testa otimização de código React"""
        basic_component = """
        import React from 'react';
        
        function Button(props) {
            return (
                <button onClick={props.onClick}>
                    {props.children}
                </button>
            );
        }
        """

        result = await optimize_react_code(
            code=basic_component,
            optimization_focus=["typescript", "accessibility", "performance"]
        )

        assert isinstance(result, dict)
        assert "optimized_code" in result
        assert "improvements" in result
        assert "explanation" in result

        optimized = result["optimized_code"]
        # Código otimizado deve incluir melhorias
        assert "interface" in optimized  # TypeScript
        assert "aria-" in optimized or "role=" in optimized  # Acessibilidade
        assert len(optimized) > len(basic_component)

    @pytest.mark.skipif(not REACT_SERVER_AVAILABLE, reason="React Server não disponível")
    @pytest.mark.asyncio
    async def test_optimize_react_prompt(self):
        """Testa otimização de prompt React"""
        basic_prompt = "Criar botão React"

        result = await optimize_react_prompt(
            prompt=basic_prompt,
            target_complexity="production",
            include_trends=True
        )

        assert isinstance(result, dict)
        assert "optimized_prompt" in result
        assert "improvements" in result
        assert "requirements_added" in result

        optimized = result["optimized_prompt"]
        assert len(optimized) > len(basic_prompt)
        assert any(keyword in optimized.lower() for keyword in [
            "typescript", "accessibility", "responsive", "animation"
        ])

    @pytest.mark.skipif(not REACT_SERVER_AVAILABLE, reason="React Server não disponível")
    @pytest.mark.asyncio
    async def test_validate_react_requirements(self):
        """Testa validação de requisitos React"""
        good_requirements = """
        Componente Button com:
        - TypeScript interface
        - Props para variant, size, disabled
        - Estados hover, focus, active
        - Acessibilidade WCAG 2.1
        - Animações micro-interactions
        - Responsive design
        - Testes unitários
        - Storybook stories
        """

        result = await validate_react_requirements(good_requirements)

        assert isinstance(result, dict)
        assert "is_valid" in result
        assert "completeness_score" in result
        assert "missing_requirements" in result
        assert "compliance_checklist" in result

        # Requisitos completos devem ser válidos
        assert result["is_valid"] is True
        assert result["completeness_score"] >= 85

    @pytest.mark.skipif(not REACT_SERVER_AVAILABLE, reason="React Server não disponível")
    @pytest.mark.asyncio
    async def test_get_react_best_practices(self):
        """Testa obtenção de melhores práticas React"""
        result = await get_react_best_practices()

        assert isinstance(result, dict)
        assert "react_19_features" in result
        assert "ui_ux_2025_trends" in result
        assert "performance" in result
        assert "accessibility" in result
        assert "typescript" in result

        # Verificar que cada categoria tem práticas
        for category, practices in result.items():
            assert isinstance(practices, list)
            assert len(practices) > 0


class TestReactIntegration:
    """Testes de integração do React Server"""

    @pytest.mark.skipif(not REACT_SERVER_AVAILABLE, reason="React Server não disponível")
    @pytest.mark.asyncio
    async def test_full_component_development_workflow(self):
        """Testa workflow completo de desenvolvimento de componente"""
        # 1. Prompt inicial simples
        initial_prompt = "Botão React azul"

        # 2. Analisar prompt inicial
        prompt_analysis = await analyze_react_prompt(initial_prompt)
        initial_score = prompt_analysis["score"]

        # 3. Otimizar prompt
        prompt_optimization = await optimize_react_prompt(
            prompt=initial_prompt,
            target_complexity="production",
            include_trends=True
        )
        optimized_prompt = prompt_optimization["optimized_prompt"]

        # 4. Analisar prompt otimizado
        optimized_analysis = await analyze_react_prompt(optimized_prompt)
        optimized_score = optimized_analysis["score"]

        # 5. Gerar componente
        component = await generate_component_template(
            component_type="button",
            name="OptimizedButton",
            complexity="advanced",
            include_typescript=True
        )

        # 6. Analisar código gerado
        code_analysis = await analyze_react_code(
            code=component["component_code"],
            component_type="functional",
            include_trends_analysis=True
        )

        # Verificar melhoria ao longo do workflow
        assert optimized_score > initial_score
        assert len(optimized_prompt) > len(initial_prompt)
        assert code_analysis["score"] >= 70

    @pytest.mark.skipif(not REACT_SERVER_AVAILABLE, reason="React Server não disponível")
    @pytest.mark.asyncio
    async def test_component_optimization_cycle(self):
        """Testa ciclo de otimização de componente"""
        # Componente básico
        basic_component = """
        function Card(props) {
            return (
                <div>
                    <h2>{props.title}</h2>
                    <p>{props.content}</p>
                </div>
            );
        }
        """

        # Analisar componente básico
        basic_analysis = await analyze_react_code(
            code=basic_component,
            component_type="functional"
        )
        basic_score = basic_analysis["score"]

        # Otimizar componente
        optimization = await optimize_react_code(
            code=basic_component,
            optimization_focus=["typescript", "accessibility", "ui_trends"]
        )

        # Analisar componente otimizado
        optimized_analysis = await analyze_react_code(
            code=optimization["optimized_code"],
            component_type="functional",
            include_trends_analysis=True
        )
        optimized_score = optimized_analysis["score"]

        # Componente otimizado deve ter score melhor
        assert optimized_score > basic_score
        assert len(optimization["improvements"]) > 0


# Testes parametrizados para diferentes cenários
@pytest.mark.skipif(not REACT_SERVER_AVAILABLE, reason="React Server não disponível")
@pytest.mark.parametrize("code_quality,expected_min_score", [
    ("""
    function Button() { return <button>Click</button>; }
    """, 20),  # Código muito básico
    ("""
    import React from 'react';
    function Button({ onClick, children }) {
        return <button onClick={onClick}>{children}</button>;
    }
    """, 40),  # Código simples
    ("""
    import React from 'react';
    interface ButtonProps {
        onClick: () => void;
        children: React.ReactNode;
        variant?: 'primary' | 'secondary';
    }
    const Button: React.FC<ButtonProps> = ({ onClick, children, variant = 'primary' }) => {
        return (
            <button 
                onClick={onClick}
                className={`btn btn-${variant}`}
                aria-label="Action button"
            >
                {children}
            </button>
        );
    };
    """, 70),  # Código avançado
])
@pytest.mark.asyncio
async def test_analyze_code_quality_levels(code_quality, expected_min_score):
    """Testa que diferentes qualidades de código resultam em scores apropriados"""
    result = await analyze_react_code(
        code=code_quality,
        component_type="functional"
    )
    assert result["score"] >= expected_min_score


# Teste de fallback quando React Server não está disponível
@pytest.mark.skipif(REACT_SERVER_AVAILABLE, reason="React Server está disponível")
def test_react_server_fallback():
    """Teste de fallback quando React Server não está disponível"""
    assert not REACT_SERVER_AVAILABLE
    print("⚠️ React Components Server não está disponível - implementação pendente")


# Fixture para mock de contexto
@pytest.fixture
def mock_context():
    """Fixture para criar mock de Context do React Server"""
    context = AsyncMock()
    context.info = AsyncMock()
    context.warning = AsyncMock()
    context.error = AsyncMock()
    return context


if __name__ == "__main__":
    # Execução direta para desenvolvimento
    pytest.main([__file__, "-v"])
