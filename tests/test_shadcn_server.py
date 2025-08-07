#!/usr/bin/env python3
"""
Testes para o shadcn/ui Server - Servidor MCP para desenvolvimento com shadcn/ui

Este módulo testa as funcionalidades do servidor shadcn/ui especializado em análise de componentes,
geração de código, criação de temas e otimização de projetos React com shadcn/ui.
"""

import pytest
from unittest.mock import AsyncMock

# Importações condicionais para fallback
try:
    from servers.shadcn_server import (
        analyze_shadcn_component,
        create_shadcn_theme,
        generate_shadcn_component,
        get_shadcn_best_practices,
        get_shadcn_setup_guide,
        optimize_shadcn_project
    )
    SHADCN_SERVER_AVAILABLE = True
except ImportError as e:
    print(f"shadcn/ui Server não disponível: {e}")
    SHADCN_SERVER_AVAILABLE = False


class TestShadcnAnalysisFunctions:
    """Testes para as funções de análise do shadcn/ui Server"""

    @pytest.mark.skipif(not SHADCN_SERVER_AVAILABLE, reason="shadcn/ui Server não disponível")
    @pytest.mark.asyncio
    async def test_analyze_shadcn_component(self):
        """Testa análise de componente shadcn/ui"""
        component_code = """
        import { Button } from "@/components/ui/button"
        import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
        
        export function UserCard({ user }) {
            return (
                <Card className="w-[350px]">
                    <CardHeader>
                        <CardTitle>{user.name}</CardTitle>
                        <CardDescription>{user.email}</CardDescription>
                    </CardHeader>
                    <CardContent>
                        <Button variant="default" size="sm">
                            View Profile
                        </Button>
                    </CardContent>
                </Card>
            )
        }
        """

        result = await analyze_shadcn_component(
            code=component_code,
            component_type="card"
        )

        assert isinstance(result, dict)
        assert "score" in result
        assert "components_detected" in result
        assert "best_practices" in result
        assert "optimization_suggestions" in result
        assert 0 <= result["score"] <= 100

    @pytest.mark.skipif(not SHADCN_SERVER_AVAILABLE, reason="shadcn/ui Server não disponível")
    @pytest.mark.asyncio
    async def test_analyze_advanced_shadcn_component(self):
        """Testa análise de componente shadcn/ui avançado"""
        advanced_code = """
        import * as React from "react"
        import { cn } from "@/lib/utils"
        import { Button } from "@/components/ui/button"
        import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
        import { Badge } from "@/components/ui/badge"
        import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
        import { Separator } from "@/components/ui/separator"
        
        interface UserProfileProps {
            user: {
                id: string
                name: string
                email: string
                avatar?: string
                role: string
                status: "online" | "offline" | "away"
            }
            className?: string
        }
        
        export function UserProfile({ user, className }: UserProfileProps) {
            const statusVariant = {
                online: "default",
                offline: "secondary",
                away: "outline"
            } as const
            
            return (
                <Card className={cn("w-full max-w-md", className)}>
                    <CardHeader className="flex flex-row items-center gap-4">
                        <Avatar className="h-16 w-16">
                            <AvatarImage src={user.avatar} alt={user.name} />
                            <AvatarFallback>
                                {user.name.split(" ").map(n => n[0]).join("")}
                            </AvatarFallback>
                        </Avatar>
                        <div className="flex flex-col gap-1">
                            <CardTitle className="text-lg">{user.name}</CardTitle>
                            <CardDescription>{user.email}</CardDescription>
                            <div className="flex items-center gap-2">
                                <Badge variant={statusVariant[user.status]}>
                                    {user.status}
                                </Badge>
                                <Badge variant="outline">{user.role}</Badge>
                            </div>
                        </div>
                    </CardHeader>
                    <Separator />
                    <CardContent className="pt-4">
                        <div className="flex gap-2">
                            <Button variant="default" size="sm" className="flex-1">
                                Message
                            </Button>
                            <Button variant="outline" size="sm" className="flex-1">
                                View Profile
                            </Button>
                        </div>
                    </CardContent>
                </Card>
            )
        }
        """

        result = await analyze_shadcn_component(
            code=advanced_code,
            component_type="card"
        )

        # Componente avançado deve ter score alto
        assert result["score"] >= 80
        assert len(result["components_detected"]) > 0

        # Verificar componentes shadcn/ui detectados
        components_str = str(result["components_detected"]).lower()
        assert any(component in components_str for component in [
            "card", "button", "badge", "avatar", "separator"
        ])

    @pytest.mark.skipif(not SHADCN_SERVER_AVAILABLE, reason="shadcn/ui Server não disponível")
    @pytest.mark.asyncio
    async def test_create_shadcn_theme(self):
        """Testa criação de tema shadcn/ui"""
        result = await create_shadcn_theme(
            primary_color="#3b82f6",
            secondary_color="#64748b",
            accent_color="#f59e0b",
            theme_name="CustomTheme"
        )

        assert isinstance(result, dict)
        assert "css_variables" in result
        assert "tailwind_config" in result
        assert "theme_preview" in result
        assert "installation_guide" in result

        # Verificar CSS variables
        css_vars = result["css_variables"]
        assert "--primary:" in css_vars
        assert "--secondary:" in css_vars
        assert "--accent:" in css_vars

    @pytest.mark.skipif(not SHADCN_SERVER_AVAILABLE, reason="shadcn/ui Server não disponível")
    @pytest.mark.asyncio
    async def test_generate_shadcn_component(self):
        """Testa geração de componente shadcn/ui"""
        component_types = ["button", "card", "form", "dialog", "table"]

        for comp_type in component_types:
            result = await generate_shadcn_component(
                component_type=comp_type,
                name=f"Custom{comp_type.title()}",
                framework="next",
                features=["typescript", "variants", "accessibility"]
            )

            assert isinstance(result, dict)
            assert "component_code" in result
            assert "usage_examples" in result
            assert "required_dependencies" in result
            assert "installation_steps" in result

            # Verificar código do componente
            component_code = result["component_code"]
            assert "import" in component_code
            assert comp_type.lower() in component_code.lower()
            assert "export" in component_code

    @pytest.mark.skipif(not SHADCN_SERVER_AVAILABLE, reason="shadcn/ui Server não disponível")
    @pytest.mark.asyncio
    async def test_get_shadcn_best_practices(self):
        """Testa obtenção de melhores práticas shadcn/ui"""
        result = await get_shadcn_best_practices()

        assert isinstance(result, dict)
        assert "component_structure" in result
        assert "styling_patterns" in result
        assert "accessibility" in result
        assert "performance" in result
        assert "project_organization" in result

        # Verificar que cada categoria tem práticas
        for category, practices in result.items():
            assert isinstance(practices, list)
            assert len(practices) > 0

    @pytest.mark.skipif(not SHADCN_SERVER_AVAILABLE, reason="shadcn/ui Server não disponível")
    @pytest.mark.asyncio
    async def test_get_shadcn_setup_guide(self):
        """Testa obtenção de guia de configuração"""
        frameworks = ["next", "vite", "remix", "astro"]

        for framework in frameworks:
            result = await get_shadcn_setup_guide(framework)

            assert isinstance(result, dict)
            assert "installation_steps" in result
            assert "configuration_files" in result
            assert "folder_structure" in result
            assert "first_component_example" in result

            # Verificar passos de instalação
            steps = result["installation_steps"]
            assert isinstance(steps, list)
            assert len(steps) > 0

    @pytest.mark.skipif(not SHADCN_SERVER_AVAILABLE, reason="shadcn/ui Server não disponível")
    @pytest.mark.asyncio
    async def test_optimize_shadcn_project(self):
        """Testa otimização de projeto shadcn/ui"""
        project_structure = {
            "components/ui/": ["button.tsx", "card.tsx"],
            "pages/": ["index.tsx", "about.tsx"],
            "lib/": ["utils.ts"],
            "styles/": ["globals.css"]
        }

        result = await optimize_shadcn_project(
            project_structure=project_structure,
            optimization_focus=["bundle_size", "accessibility", "performance"]
        )

        assert isinstance(result, dict)
        assert "optimizations" in result
        assert "bundle_analysis" in result
        assert "recommendations" in result
        assert "implementation_guide" in result


class TestShadcnIntegration:
    """Testes de integração do shadcn/ui Server"""

    @pytest.mark.skipif(not SHADCN_SERVER_AVAILABLE, reason="shadcn/ui Server não disponível")
    @pytest.mark.asyncio
    async def test_full_project_setup_workflow(self):
        """Testa workflow completo de configuração de projeto"""
        # 1. Obter guia de configuração
        setup_guide = await get_shadcn_setup_guide("next")

        # 2. Obter melhores práticas
        best_practices = await get_shadcn_best_practices()

        # 3. Gerar componente personalizado
        custom_component = await generate_shadcn_component(
            component_type="card",
            name="ProjectCard",
            framework="next",
            features=["typescript", "variants"]
        )

        # 4. Analisar componente gerado
        analysis = await analyze_shadcn_component(
            code=custom_component["component_code"],
            component_type="card"
        )

        # 5. Criar tema personalizado
        custom_theme = await create_shadcn_theme(
            primary_color="#2563eb",
            secondary_color="#64748b",
            accent_color="#dc2626"
        )

        # Verificar que todo o workflow funcionou
        assert len(setup_guide["installation_steps"]) > 0
        assert len(best_practices["component_structure"]) > 0
        assert custom_component["component_code"] is not None
        assert analysis["score"] > 0
        assert "--primary:" in custom_theme["css_variables"]

    @pytest.mark.skipif(not SHADCN_SERVER_AVAILABLE, reason="shadcn/ui Server não disponível")
    @pytest.mark.asyncio
    async def test_component_optimization_workflow(self):
        """Testa workflow de otimização de componente"""
        # Componente básico
        basic_component = """
        import { Button } from "@/components/ui/button"
        
        export function SimpleButton({ children, onClick }) {
            return (
                <Button onClick={onClick}>
                    {children}
                </Button>
            )
        }
        """

        # 1. Analisar componente básico
        basic_analysis = await analyze_shadcn_component(
            code=basic_component,
            component_type="button"
        )
        basic_score = basic_analysis["score"]

        # 2. Gerar versão otimizada
        optimized_component = await generate_shadcn_component(
            component_type="button",
            name="OptimizedButton",
            framework="next",
            features=["typescript", "variants",
                      "accessibility", "loading_states"]
        )

        # 3. Analisar componente otimizado
        optimized_analysis = await analyze_shadcn_component(
            code=optimized_component["component_code"],
            component_type="button"
        )
        optimized_score = optimized_analysis["score"]

        # Componente otimizado deve ter score melhor
        assert optimized_score > basic_score
        assert len(optimized_component["usage_examples"]) > 0


# Testes parametrizados para diferentes cenários
@pytest.mark.skipif(not SHADCN_SERVER_AVAILABLE, reason="shadcn/ui Server não disponível")
@pytest.mark.parametrize("component_complexity,expected_min_score", [
    ("""
    import { Button } from "@/components/ui/button"
    export function SimpleButton() { return <Button>Click</Button> }
    """, 40),  # Componente básico
    ("""
    import { Button } from "@/components/ui/button"
    import { Card } from "@/components/ui/card"
    export function ButtonCard({ title, onClick }) {
        return (
            <Card>
                <Button onClick={onClick}>{title}</Button>
            </Card>
        )
    }
    """, 60),  # Componente intermediário
    ("""
    import * as React from "react"
    import { cn } from "@/lib/utils"
    import { Button } from "@/components/ui/button"
    import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
    
    interface ActionCardProps {
        title: string
        description?: string
        onAction: () => void
        variant?: "default" | "destructive"
        disabled?: boolean
        className?: string
    }
    
    export function ActionCard({ 
        title, 
        description, 
        onAction, 
        variant = "default",
        disabled = false,
        className 
    }: ActionCardProps) {
        return (
            <Card className={cn("w-full max-w-sm", className)}>
                <CardHeader>
                    <CardTitle>{title}</CardTitle>
                    {description && <p className="text-sm text-muted-foreground">{description}</p>}
                </CardHeader>
                <CardContent>
                    <Button 
                        variant={variant} 
                        onClick={onAction} 
                        disabled={disabled}
                        className="w-full"
                    >
                        Execute Action
                    </Button>
                </CardContent>
            </Card>
        )
    }
    """, 85),  # Componente avançado
])
@pytest.mark.asyncio
async def test_analyze_component_complexity_levels(component_complexity, expected_min_score):
    """Testa que diferentes complexidades de componente resultam em scores apropriados"""
    result = await analyze_shadcn_component(
        code=component_complexity,
        component_type="card"
    )
    assert result["score"] >= expected_min_score


@pytest.mark.skipif(not SHADCN_SERVER_AVAILABLE, reason="shadcn/ui Server não disponível")
@pytest.mark.parametrize("framework", ["next", "vite", "remix", "astro"])
@pytest.mark.asyncio
async def test_setup_guide_all_frameworks(framework):
    """Testa guia de configuração para todos os frameworks"""
    result = await get_shadcn_setup_guide(framework)

    assert isinstance(result, dict)
    assert "installation_steps" in result
    assert "configuration_files" in result
    assert len(result["installation_steps"]) > 0


# Teste de fallback quando shadcn/ui Server não está disponível
@pytest.mark.skipif(SHADCN_SERVER_AVAILABLE, reason="shadcn/ui Server está disponível")
def test_shadcn_server_fallback():
    """Teste de fallback quando shadcn/ui Server não está disponível"""
    assert not SHADCN_SERVER_AVAILABLE
    print("⚠️ shadcn/ui Server não está disponível - implementação pendente")


# Fixture para mock de contexto
@pytest.fixture
def mock_context():
    """Fixture para criar mock de Context do shadcn/ui Server"""
    context = AsyncMock()
    context.info = AsyncMock()
    context.warning = AsyncMock()
    context.error = AsyncMock()
    return context


if __name__ == "__main__":
    # Execução direta para desenvolvimento
    pytest.main([__file__, "-v"])
