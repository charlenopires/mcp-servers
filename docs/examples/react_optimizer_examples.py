#!/usr/bin/env python3
"""
Exemplos Práticos - React Development Optimizer Server
=====================================================

Este arquivo demonstra como utilizar o React Development Optimizer Server
para análise de código React, otimização baseada em tendências 2025,
e otimização de prompts para ferramentas AI.
"""

import asyncio
import json
from typing import Dict, Any

# Simulação do cliente MCP (em uso real, seria através do protocolo MCP)


class MockMCPClient:
    """Simulação de cliente MCP para demonstração dos exemplos"""

    async def call_tool(self, tool_name: str, **kwargs) -> Dict[str, Any]:
        """Simula chamada de ferramenta MCP"""
        print(f"🔧 Chamando ferramenta: {tool_name}")
        print(
            f"📝 Parâmetros: {json.dumps(kwargs, indent=2, ensure_ascii=False)}")

        # Aqui seria a chamada real para o servidor MCP
        # Por agora, retornamos dados simulados para demonstração
        if tool_name == "analyze_react_code":
            return self._mock_analyze_result()
        elif tool_name == "optimize_react_code":
            return self._mock_optimize_result()
        elif tool_name == "analyze_prompt_for_react":
            return self._mock_prompt_analysis()
        elif tool_name == "optimize_prompt_for_react":
            return self._mock_prompt_optimization()
        elif tool_name == "generate_react_workflow":
            return self._mock_workflow_generation()
        else:
            return {"status": "success", "message": f"Ferramenta {tool_name} executada"}

    def _mock_analyze_result(self) -> Dict[str, Any]:
        return {
            "quality_score": 45,
            "trends_compliance": {
                "glassmorphism": False,
                "dark_mode_first": False,
                "micro_interactions": False,
                "accessibility_first": True
            },
            "issues_found": [
                "Falta implementação de dark mode",
                "Ausência de micro-interações",
                "Estilos não seguem tendências 2025"
            ],
            "recommendations": [
                "Implementar dark mode como padrão",
                "Adicionar animações de hover e click",
                "Aplicar glassmorphism nos elementos visuais"
            ]
        }

    def _mock_optimize_result(self) -> Dict[str, Any]:
        return {
            "optimized_code": '''
function ModernButton({ children, onClick, variant = "primary" }) {
    const [isHovered, setIsHovered] = useState(false);
    
    return (
        <button 
            onClick={onClick}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
            className={`
                modern-btn modern-btn--${variant}
                ${isHovered ? 'modern-btn--hovered' : ''}
                backdrop-blur-md bg-white/10 dark:bg-black/20
                border border-white/20 rounded-xl
                transition-all duration-300 ease-out
                hover:scale-105 hover:bg-white/20
                focus:outline-none focus:ring-2 focus:ring-blue-500
                active:scale-95
            `}
            aria-label={typeof children === 'string' ? children : 'Button'}
        >
            <span className="relative z-10 font-semibold">
                {children}
            </span>
            <div className="absolute inset-0 rounded-xl bg-gradient-to-r from-blue-500/20 to-purple-500/20 opacity-0 hover:opacity-100 transition-opacity duration-300" />
        </button>
    );
}
            ''',
            "trends_applied": [
                "glassmorphism",
                "micro_interactions",
                "dark_mode_first",
                "accessibility_first"
            ],
            "improvements": [
                "Adicionado efeito glassmorphism com backdrop-blur",
                "Implementadas micro-interações com hover e active states",
                "Suporte completo a dark mode",
                "Melhorada acessibilidade com aria-label e focus states"
            ]
        }

    def _mock_prompt_analysis(self) -> Dict[str, Any]:
        return {
            "prompt_score": 25,
            "issues": [
                "Muito vago e genérico",
                "Não especifica funcionalidades",
                "Falta contexto sobre design"
            ],
            "suggestions": [
                "Especificar tipo de dashboard (analytics, admin, user)",
                "Definir funcionalidades principais",
                "Incluir preferências de design e tendências"
            ],
            "adequacy_analysis": {
                "claude": "Inadequado - precisa mais contexto",
                "chatgpt": "Inadequado - muito genérico",
                "v0": "Inadequado - falta especificação visual"
            }
        }

    def _mock_prompt_optimization(self) -> Dict[str, Any]:
        return {
            "optimized_prompt": '''
Crie um dashboard analytics moderno seguindo as tendências UI/UX 2025:

FUNCIONALIDADES PRINCIPAIS:
- Visão geral de métricas em tempo real (KPIs, gráficos, tabelas)
- Sistema de filtros avançados com range de datas
- Widgets customizáveis e redimensionáveis pelo usuário
- Notificações e alertas contextuais
- Exportação de relatórios (PDF, Excel, CSV)

DESIGN & UI/UX 2025:
- Dark mode como padrão primário
- Glassmorphism em cards e modais
- Typography bold e capitalizada para títulos
- Micro-interações em botões e elementos interativos
- Formas orgânicas e cantos arredondados
- Grid layout responsivo mobile-first

ESPECIFICAÇÕES TÉCNICAS:
- React 18 com TypeScript
- Tailwind CSS para styling
- Framer Motion para animações
- Recharts ou D3.js para gráficos
- Zustand para gerenciamento de estado
- React Query para cache de dados

ACESSIBILIDADE:
- Navegação por teclado completa
- Screen reader compatible
- Contraste WCAG 2.1 AA
- Foco visível em elementos interativos

EXEMPLO DE ESTRUTURA:
```
DashboardLayout
├── Header (user menu, notifications, search)
├── Sidebar (navigation, filters panel)
└── MainContent
    ├── KPICards (glassmorphism style)
    ├── ChartsGrid (responsive grid)
    └── DataTable (sortable, filterable)
```

Priorize performance, acessibilidade e experiência do usuário moderna.
            ''',
            "structure_improvements": [
                "Adicionado contexto específico sobre funcionalidades",
                "Incluídas tendências UI/UX 2025 detalhadas",
                "Especificações técnicas claras",
                "Exemplo de estrutura de componentes"
            ],
            "context_added": [
                "Funcionalidades específicas do dashboard",
                "Padrões de design 2025",
                "Stack técnico recomendado",
                "Requisitos de acessibilidade"
            ]
        }

    def _mock_workflow_generation(self) -> Dict[str, Any]:
        return {
            "workflow_steps": [
                {
                    "order": 1,
                    "title": "Layout e Estrutura Base",
                    "description": "Criar estrutura principal com navegação",
                    "estimated_time": "2-3 horas",
                    "optimized_prompt": "Crie um layout base para e-commerce com header responsivo, navegação principal, sidebar de filtros e footer. Use Tailwind CSS com design system moderno 2025...",
                    "ai_tool": "claude"
                },
                {
                    "order": 2,
                    "title": "Componentes de Produto",
                    "description": "ProductCard, ProductGrid, ProductDetails",
                    "estimated_time": "3-4 horas",
                    "optimized_prompt": "Desenvolva componentes de produto para e-commerce seguindo tendências 2025: ProductCard com glassmorphism, hover effects, quick actions...",
                    "ai_tool": "v0"
                },
                {
                    "order": 3,
                    "title": "Sistema de Carrinho",
                    "description": "CartItem, CartSummary, Checkout",
                    "estimated_time": "4-5 horas",
                    "optimized_prompt": "Implemente sistema de carrinho completo com animações, validação em tempo real, integração de pagamento...",
                    "ai_tool": "claude"
                }
            ],
            "integration_notes": [
                "Usar Context API para estado global do carrinho",
                "Implementar React Query para cache de produtos",
                "Configurar Zustand para preferências do usuário"
            ],
            "estimated_total_time": "9-12 horas",
            "recommended_order": "sequential"
        }

# ================================
# EXEMPLOS PRÁTICOS DE USO
# ================================


async def exemplo_1_analise_componente():
    """
    Exemplo 1: Análise de Componente React Existente
    Demonstra como analisar um componente simples para identificar
    oportunidades de modernização.
    """
    print("\n" + "="*60)
    print("📊 EXEMPLO 1: Análise de Componente React")
    print("="*60)

    client = MockMCPClient()

    # Código de exemplo - botão simples e básico
    codigo_button_basico = '''
function Button({ children, onClick }) {
    return (
        <button onClick={onClick} className="btn">
            {children}
        </button>
    );
}
    '''

    print("🔍 Analisando componente Button básico...")
    print(f"Código original:\n{codigo_button_basico}")

    # Chamar ferramenta de análise
    resultado = await client.call_tool(
        "analyze_react_code",
        code=codigo_button_basico,
        component_type="component"
    )

    print(f"\n📈 Resultado da Análise:")
    print(f"Score de Qualidade: {resultado['quality_score']}/100")
    print(f"\n⚠️  Problemas Identificados:")
    for issue in resultado['issues_found']:
        print(f"  • {issue}")

    print(f"\n💡 Recomendações:")
    for rec in resultado['recommendations']:
        print(f"  • {rec}")

    print(f"\n✅ Conformidade com Tendências 2025:")
    for trend, compliant in resultado['trends_compliance'].items():
        status = "✅" if compliant else "❌"
        print(f"  {status} {trend}")


async def exemplo_2_otimizacao_codigo():
    """
    Exemplo 2: Otimização de Código React
    Demonstra como aplicar tendências 2025 automaticamente
    """
    print("\n" + "="*60)
    print("⚡ EXEMPLO 2: Otimização de Código React")
    print("="*60)

    client = MockMCPClient()

    codigo_original = '''
function Button({ children, onClick }) {
    return (
        <button onClick={onClick} className="btn">
            {children}
        </button>
    );
}
    '''

    print("🎨 Otimizando código com tendências 2025...")

    resultado = await client.call_tool(
        "optimize_react_code",
        code=codigo_original,
        target_trends=["glassmorphism",
                       "micro_interactions", "dark_mode_first"],
        complexity_level="intermediate"
    )

    print(f"\n🚀 Código Otimizado:")
    print(resultado['optimized_code'])

    print(f"\n✨ Tendências Aplicadas:")
    for trend in resultado['trends_applied']:
        print(f"  • {trend}")

    print(f"\n🔧 Melhorias Implementadas:")
    for improvement in resultado['improvements']:
        print(f"  • {improvement}")


async def exemplo_3_analise_prompt():
    """
    Exemplo 3: Análise de Prompt
    Demonstra como analisar um prompt para identificar problemas
    """
    print("\n" + "="*60)
    print("🔍 EXEMPLO 3: Análise de Prompt")
    print("="*60)

    client = MockMCPClient()

    prompt_basico = "Criar um dashboard"

    print(f"📝 Analisando prompt básico: '{prompt_basico}'")

    resultado = await client.call_tool(
        "analyze_prompt_for_react",
        prompt=prompt_basico,
        target_component="dashboard",
        ai_tool="claude"
    )

    print(f"\n📊 Score do Prompt: {resultado['prompt_score']}/100")

    print(f"\n⚠️  Problemas Identificados:")
    for issue in resultado['issues']:
        print(f"  • {issue}")

    print(f"\n💡 Sugestões de Melhoria:")
    for suggestion in resultado['suggestions']:
        print(f"  • {suggestion}")

    print(f"\n🤖 Adequação para Ferramentas AI:")
    for tool, adequacy in resultado['adequacy_analysis'].items():
        print(f"  • {tool}: {adequacy}")


async def exemplo_4_otimizacao_prompt():
    """
    Exemplo 4: Otimização de Prompt
    Demonstra como transformar um prompt básico em estruturado
    """
    print("\n" + "="*60)
    print("📝 EXEMPLO 4: Otimização de Prompt")
    print("="*60)

    client = MockMCPClient()

    prompt_original = "Criar um dashboard"

    print(f"✨ Otimizando prompt: '{prompt_original}'")

    resultado = await client.call_tool(
        "optimize_prompt_for_react",
        prompt=prompt_original,
        component_type="dashboard",
        target_ai_tool="claude",
        include_trends=True
    )

    print(f"\n🚀 Prompt Otimizado:")
    print(resultado['optimized_prompt'])

    print(f"\n🔧 Melhorias na Estrutura:")
    for improvement in resultado['structure_improvements']:
        print(f"  • {improvement}")


async def exemplo_5_workflow_completo():
    """
    Exemplo 5: Geração de Workflow Completo
    Demonstra como gerar um workflow estruturado para projeto
    """
    print("\n" + "="*60)
    print("🚀 EXEMPLO 5: Workflow de Desenvolvimento")
    print("="*60)

    client = MockMCPClient()

    print("🏗️ Gerando workflow para e-commerce moderno...")

    resultado = await client.call_tool(
        "generate_react_workflow",
        project_description="E-commerce moderno com design 2025",
        component_types=["landing", "product_catalog", "cart", "checkout"],
        target_ai_tools=["claude", "v0"]
    )

    print(f"\n📋 Workflow Gerado ({resultado['estimated_total_time']}):")

    for step in resultado['workflow_steps']:
        print(f"\n{step['order']}. {step['title']}")
        print(f"   ⏱️  Tempo estimado: {step['estimated_time']}")
        print(f"   🤖 Ferramenta AI: {step['ai_tool']}")
        print(f"   📝 Descrição: {step['description']}")
        print(f"   🔧 Prompt otimizado: {step['optimized_prompt'][:100]}...")

    print(f"\n🔗 Notas de Integração:")
    for note in resultado['integration_notes']:
        print(f"  • {note}")


async def exemplo_6_uso_integrado():
    """
    Exemplo 6: Uso Integrado - Análise → Otimização → Validação
    Demonstra um workflow completo de análise e otimização
    """
    print("\n" + "="*60)
    print("🔄 EXEMPLO 6: Workflow Integrado")
    print("="*60)

    client = MockMCPClient()

    # Código inicial
    codigo_inicial = '''
function ProductCard({ product }) {
    return (
        <div className="card">
            <img src={product.image} alt={product.name} />
            <h3>{product.name}</h3>
            <p>{product.price}</p>
            <button>Add to Cart</button>
        </div>
    );
}
    '''

    print("🔄 Executando workflow integrado:")
    print("1️⃣ Análise → 2️⃣ Otimização → 3️⃣ Validação")

    # Etapa 1: Análise
    print(f"\n1️⃣ Analisando código inicial...")
    analise = await client.call_tool(
        "analyze_react_code",
        code=codigo_inicial,
        component_type="component"
    )
    print(f"   📊 Score inicial: {analise['quality_score']}/100")

    # Etapa 2: Otimização
    print(f"\n2️⃣ Otimizando código...")
    otimizacao = await client.call_tool(
        "optimize_react_code",
        code=codigo_inicial,
        target_trends=["glassmorphism", "micro_interactions"],
        complexity_level="advanced"
    )
    print(
        f"   ✨ Tendências aplicadas: {', '.join(otimizacao['trends_applied'])}")

    # Etapa 3: Validação
    print(f"\n3️⃣ Validando código otimizado...")
    validacao = await client.call_tool(
        "analyze_react_code",
        code=otimizacao['optimized_code'],
        component_type="component"
    )
    print(f"   📈 Score final: {validacao['quality_score']}/100")
    print(
        f"   🎯 Melhoria: +{validacao['quality_score'] - analise['quality_score']} pontos")


async def main():
    """
    Função principal que executa todos os exemplos
    """
    print("🌟 React Development Optimizer Server - Exemplos Práticos")
    print("=" * 80)
    print("Este demo mostra como utilizar o servidor para análise e otimização")
    print("de código React seguindo as tendências UI/UX 2025.")
    print("=" * 80)

    # Executar todos os exemplos
    await exemplo_1_analise_componente()
    await exemplo_2_otimizacao_codigo()
    await exemplo_3_analise_prompt()
    await exemplo_4_otimizacao_prompt()
    await exemplo_5_workflow_completo()
    await exemplo_6_uso_integrado()

    print("\n" + "="*60)
    print("🎉 Todos os exemplos executados com sucesso!")
    print("="*60)
    print("\n💡 Próximos passos:")
    print("1. Integre o servidor com Claude Desktop")
    print("2. Use as ferramentas em seus projetos React")
    print("3. Experimente diferentes combinações de tendências")
    print("4. Crie workflows personalizados para sua equipe")

if __name__ == "__main__":
    asyncio.run(main())
