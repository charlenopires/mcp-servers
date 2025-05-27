#!/usr/bin/env python3
"""
React Development Optimizer - Servidor MCP Unificado
===================================================

Servidor MCP completo que combina análise/otimização de código React existente 
com otimização de prompts para gerar código React moderno. Duas funcionalidades 
principais integradas:

1. CODE ANALYSIS & OPTIMIZATION
   - Analisa componentes React existentes
   - Aplica tendências UI/UX 2025
   - Otimiza performance e acessibilidade

2. PROMPT OPTIMIZATION  
   - Transforma prompts básicos em solicitações estruturadas
   - Gera código React moderno via ferramentas AI
   - Templates otimizados para diferentes componentes

Baseado em pesquisa de:
- 25+ templates React opensource populares
- Tendências UI/UX 2025 do Awwwards
- Padrões React modernos da comunidade
- Melhores práticas de prompting para AI
"""

import asyncio
import json
import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Any, Tuple, Union
from enum import Enum
import logging
from fastmcp import FastMCP
from pydantic import BaseModel, Field

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializar servidor MCP
mcp = FastMCP(
    name="react-development-optimizer",
    version="2.0.0",
    description="Servidor MCP completo para análise de código React e otimização de prompts"
)

# ================================
# KNOWLEDGE BASE - TENDÊNCIAS E PADRÕES 2025
# ================================


class UIUXTrends2025:
    """Tendências de UI/UX para 2025 baseadas na pesquisa Awwwards"""

    TYPOGRAPHY_TRENDS = {
        "bold_capitalized": "Typography bold e capitalizada para impacto visual",
        "variable_fonts": "Fontes variáveis para flexibilidade e performance",
        "serif_revival": "Retorno das serifas em design digital",
        "maximalist_typography": "Typography oversized e layered"
    }

    DESIGN_TRENDS = {
        "interactive_3d": "Elementos 3D interativos e immersivos",
        "ai_personalization": "Personalização impulsionada por IA",
        "real_time_content": "Conteúdo em tempo real e atualizações live",
        "sustainable_design": "Design sustentável com foco em performance",
        "voice_ui": "Interfaces de voz e interações multimodais",
        "glassmorphism": "Efeitos de vidro e multi-layering",
        "organic_shapes": "Formas orgânicas e asymétricas",
        "dark_mode_first": "Dark mode como padrão primário"
    }

    UX_PATTERNS = {
        "progressive_disclosure": "Revelação progressiva de informações",
        "anticipatory_design": "Design antecipatório baseado em comportamento",
        "micro_interactions": "Micro-animações e feedback contextual",
        "accessibility_first": "Acessibilidade como prioridade principal",
        "mobile_first_advanced": "Mobile-first com gestos avançados",
        "customizable_dashboards": "Dashboards personalizáveis pelo usuário"
    }


class ReactModernPatterns:
    """Padrões React modernos baseados em templates opensource e comunidade"""

    COMPONENT_PATTERNS = {
        "compound_components": {
            "description": "Componentes que trabalham juntos compartilhando estado",
            "use_case": "Formulários, menus dropdown, tabs complexos",
            "keywords": ["modal", "form", "accordion", "tabs", "dropdown"],
            "implementation": "Context API + children composition"
        },
        "custom_hooks": {
            "description": "Lógica reutilizável encapsulada em hooks",
            "use_case": "Fetch de dados, gerenciamento de estado, validação",
            "keywords": ["fetch", "api", "state", "validation", "logic"],
            "implementation": "useState + useEffect + cleanup"
        },
        "render_props": {
            "description": "Compartilhamento de lógica através de props funcionais",
            "use_case": "Componentes que precisam de diferentes UIs",
            "keywords": ["dynamic", "flexible", "configurable"],
            "implementation": "Function as children pattern"
        },
        "hoc_patterns": {
            "description": "Higher-Order Components para funcionalidades transversais",
            "use_case": "Autenticação, logging, analytics",
            "keywords": ["auth", "protected", "analytics", "logging"],
            "implementation": "Component wrapper com props injection"
        }
    }

    PERFORMANCE_PATTERNS = {
        "memoization": {
            "description": "React.memo, useMemo, useCallback para otimização",
            "prompt_addition": "Otimize performance com memoização apropriada",
            "keywords": ["performance", "optimization", "large list", "expensive"],
            "implementation": "Strategic memoization sem over-optimization"
        },
        "lazy_loading": {
            "description": "Carregamento sob demanda de componentes",
            "prompt_addition": "Implemente lazy loading para melhor performance",
            "keywords": ["route", "large", "heavy", "slow"],
            "implementation": "React.lazy + Suspense boundaries"
        },
        "virtualization": {
            "description": "Virtualização para listas grandes",
            "prompt_addition": "Use virtualização para listas grandes",
            "keywords": ["large list", "thousand", "scroll", "infinite"],
            "implementation": "react-window ou react-virtualized"
        }
    }


class AIToolsIntegration:
    """Integração com ferramentas AI populares para React em 2025"""

    TOOLS_OPTIMIZATION = {
        "v0_dev": {
            "description": "Vercel v0 - text-to-UI especializado",
            "prompt_structure": "Seja específico sobre layout, funcionalidade e styling",
            "best_practices": [
                "Descreva o propósito do componente",
                "Mencione interações esperadas",
                "Especifique responsive behavior",
                "Inclua estados (loading, error, success)"
            ]
        },
        "visual_copilot": {
            "description": "Figma to React code generation",
            "prompt_structure": "Foque em estrutura semântica e acessibilidade",
            "best_practices": [
                "Mencione design tokens",
                "Especifique component hierarchy",
                "Inclua props interface",
                "Defina responsive breakpoints"
            ]
        },
        "cursor_copilot": {
            "description": "Context-aware code completion",
            "prompt_structure": "Forneça contexto do projeto e arquitetura",
            "best_practices": [
                "Mencione tech stack usado",
                "Descreva padrões do projeto",
                "Inclua naming conventions",
                "Especifique folder structure"
            ]
        }
    }

# ================================
# MODELOS DE DADOS UNIFICADOS
# ================================


class ComponentType(Enum):
    LAYOUT = "layout"
    FORM = "form"
    NAVIGATION = "navigation"
    DATA_DISPLAY = "data_display"
    FEEDBACK = "feedback"
    INTERACTION = "interaction"
    MEDIA = "media"


class ComplexityLevel(Enum):
    SIMPLE = "simple"
    INTERMEDIATE = "intermediate"
    COMPLEX = "complex"


class AITool(Enum):
    V0_DEV = "v0_dev"
    CURSOR = "cursor"
    VISUAL_COPILOT = "visual_copilot"
    GENERIC = "generic"


class AnalysisType(Enum):
    CODE_ANALYSIS = "code_analysis"
    PROMPT_ANALYSIS = "prompt_analysis"


@dataclass
class CodeAnalysisResult:
    """Resultado da análise de código React existente"""
    score: int
    trends_compliance: Dict[str, bool]
    design_patterns: Dict[str, bool]
    performance_issues: List[str]
    accessibility_issues: List[str]
    recommendations: List[str]
    modern_alternatives: List[str]


@dataclass
class CodeOptimizationResult:
    """Resultado da otimização de código React"""
    original_code: str
    optimized_code: str
    changes_made: List[str]
    performance_improvements: List[str]
    accessibility_improvements: List[str]
    trend_alignments: List[str]


@dataclass
class PromptAnalysisResult:
    """Resultado da análise de prompt"""
    original_prompt: str
    detected_component_type: ComponentType
    complexity_level: ComplexityLevel
    missing_elements: List[str]
    potential_patterns: List[str]
    ui_trends_applicable: List[str]


@dataclass
class PromptOptimizationResult:
    """Resultado da otimização de prompt"""
    original_prompt: str
    optimized_prompt: str
    ai_tool_specific: Dict[str, str]
    enhancements_applied: List[str]
    modern_patterns_included: List[str]
    ui_trends_integrated: List[str]
    accessibility_features: List[str]
    performance_considerations: List[str]

# ================================
# ANALISADOR UNIFICADO
# ================================


class ReactUnifiedAnalyzer:
    """Analisador unificado para código React e prompts"""

    def __init__(self):
        self.trends = UIUXTrends2025()
        self.patterns = ReactModernPatterns()
        self.ai_tools = AIToolsIntegration()

    async def analyze_react_code(self, code: str, component_type: str = "component") -> CodeAnalysisResult:
        """Analisa código React existente para conformidade com tendências 2025"""

        score = 70  # Score base
        trends_compliance = {}
        design_patterns = {}
        performance_issues = []
        accessibility_issues = []
        recommendations = []
        modern_alternatives = []

        # Análise de tendências de design
        trends_compliance.update(await self._analyze_design_trends(code))

        # Análise de padrões React
        design_patterns.update(await self._analyze_react_patterns(code))

        # Análise de performance
        performance_issues.extend(await self._analyze_performance_issues(code))

        # Análise de acessibilidade
        accessibility_issues.extend(await self._analyze_accessibility_issues(code))

        # Gerar recomendações
        recommendations.extend(await self._generate_code_recommendations(
            code, trends_compliance, design_patterns,
            performance_issues, accessibility_issues
        ))

        # Sugerir alternativas modernas
        modern_alternatives.extend(await self._suggest_modern_code_alternatives(
            code, component_type
        ))

        # Calcular score final
        score = await self._calculate_code_score(
            trends_compliance, design_patterns,
            performance_issues, accessibility_issues
        )

        return CodeAnalysisResult(
            score=score,
            trends_compliance=trends_compliance,
            design_patterns=design_patterns,
            performance_issues=performance_issues,
            accessibility_issues=accessibility_issues,
            recommendations=recommendations,
            modern_alternatives=modern_alternatives
        )

    async def analyze_prompt_quality(self, prompt: str) -> PromptAnalysisResult:
        """Analisa qualidade de um prompt para geração de código React"""

        # Detectar tipo de componente
        component_type = await self._detect_component_type(prompt)

        # Avaliar complexidade
        complexity = await self._assess_prompt_complexity(prompt)

        # Identificar elementos faltantes
        missing_elements = await self._identify_missing_prompt_elements(prompt, component_type)

        # Identificar padrões aplicáveis
        potential_patterns = await self._identify_applicable_patterns(prompt, component_type)

        # Identificar tendências UI aplicáveis
        ui_trends = await self._identify_applicable_trends(prompt, component_type)

        return PromptAnalysisResult(
            original_prompt=prompt,
            detected_component_type=component_type,
            complexity_level=complexity,
            missing_elements=missing_elements,
            potential_patterns=potential_patterns,
            ui_trends_applicable=ui_trends
        )

    # ================================
    # MÉTODOS DE ANÁLISE DE CÓDIGO
    # ================================

    async def _analyze_design_trends(self, code: str) -> Dict[str, bool]:
        """Analisa conformidade com tendências de design 2025"""
        compliance = {}

        # Typography trends
        compliance["bold_typography"] = bool(
            re.search(r'font-weight:\s*(bold|[6-9]00)', code, re.IGNORECASE))
        compliance["variable_fonts"] = "'font-variation-settings'" in code
        compliance["serif_fonts"] = bool(
            re.search(r'serif|Times|Georgia', code, re.IGNORECASE))

        # Design trends
        compliance["dark_mode"] = bool(
            re.search(r'dark:|dark-|darkMode|dark\s*theme', code, re.IGNORECASE))
        compliance["glassmorphism"] = bool(
            re.search(r'backdrop-blur|glass|rgba\([^)]*,\s*0\.[0-9]', code))
        compliance["organic_shapes"] = bool(
            re.search(r'border-radius:\s*[0-9]+%|rounded-full|organic', code))
        compliance["animations"] = bool(
            re.search(r'@keyframes|animation:|transition:|framer-motion', code))
        compliance["interactive_3d"] = bool(
            re.search(r'transform.*rotate|perspective|three\.js|@react-three', code))

        # Modern UI libraries
        compliance["modern_ui_lib"] = bool(
            re.search(r'@mui|tailwind|styled-components|framer-motion|shadcn', code))

        return compliance

    async def _analyze_react_patterns(self, code: str) -> Dict[str, bool]:
        """Analisa padrões de design React modernos"""
        patterns = {}

        # Component patterns
        patterns["custom_hooks"] = bool(
            re.search(r'const\s+use[A-Z][a-zA-Z]*\s*=', code))
        patterns["memo_usage"] = "React.memo" in code or "memo(" in code
        patterns["context_usage"] = "useContext" in code or "createContext" in code
        patterns["suspense_usage"] = "Suspense" in code
        patterns["error_boundary"] = "ErrorBoundary" in code or "componentDidCatch" in code

        # Modern React features
        patterns["hooks_usage"] = bool(re.search(r'use[A-Z][a-zA-Z]*', code))
        patterns["functional_components"] = bool(
            re.search(r'const\s+[A-Z][a-zA-Z]*\s*=.*=>', code))
        patterns["typescript_usage"] = bool(
            re.search(r':\s*(React\.FC|JSX\.Element|React\.ReactElement)', code))

        # Performance patterns
        patterns["lazy_loading"] = "React.lazy" in code or "import(" in code
        patterns["use_callback"] = "useCallback" in code
        patterns["use_memo"] = "useMemo" in code

        # Compound components
        patterns["compound_components"] = bool(
            re.search(r'\w+\.\w+', code)) and "children" in code

        return patterns

    async def _analyze_performance_issues(self, code: str) -> List[str]:
        """Identifica problemas de performance no código"""
        issues = []

        # Problemas comuns de performance
        if re.search(r'\.map\([^)]*\.map\(', code):
            issues.append("Nested maps detectados - considere otimização")

        if "useEffect(() =>" in code and "[]" not in code:
            issues.append(
                "useEffect sem dependências pode causar re-renders desnecessários")

        if re.search(r'new Date\(\)|Date\.now\(\)', code) and "useMemo" not in code:
            issues.append(
                "Operações de data sem memoização podem impactar performance")

        if re.search(r'find\(|filter\(|sort\(', code) and "useMemo" not in code:
            issues.append(
                "Operações de array sem memoização podem causar re-computação")

        if re.search(r'onClick=\{.*=>', code):
            issues.append(
                "Funções inline podem causar re-renders desnecessários")

        if re.search(r'<img(?![^>]*loading=)', code):
            issues.append("Imagens sem lazy loading detectadas")

        if code.count("useState") > 5 and "useReducer" not in code:
            issues.append("Muitos estados locais - considere useReducer")

        return issues

    async def _analyze_accessibility_issues(self, code: str) -> List[str]:
        """Analisa problemas de acessibilidade no código"""
        issues = []

        # Verificações básicas de a11y
        if re.search(r'<img(?![^>]*alt=)', code):
            issues.append("Imagens sem atributo alt detectadas")

        if re.search(r'<button(?![^>]*aria-label)(?![^>]*>.*[a-zA-Z])', code):
            issues.append("Botões sem texto ou aria-label detectados")

        if re.search(r'onClick.*<div|onClick.*<span', code):
            issues.append(
                "Elementos não-interativos com onClick - use botões apropriados")

        if "tabIndex" not in code and re.search(r'onClick|onKeyDown', code):
            issues.append(
                "Elementos interativos podem precisar de gerenciamento de foco")

        if re.search(r'color:\s*#(?:fff|ffffff|000|000000)', code):
            issues.append(
                "Cores de alto contraste detectadas - verifique readabilidade")

        if not re.search(r'<h[1-6]', code) and len(code) > 500:
            issues.append(
                "Componente grande sem estrutura de headings adequada")

        if "aria-" not in code and len(code) > 200:
            issues.append(
                "Ausência de atributos ARIA para melhor acessibilidade")

        return issues

    async def _generate_code_recommendations(
        self, code: str, trends: Dict[str, bool],
        patterns: Dict[str, bool], performance: List[str],
        accessibility: List[str]
    ) -> List[str]:
        """Gera recomendações para melhorar o código"""
        recommendations = []

        # Recomendações baseadas em tendências
        if not trends.get("dark_mode", False):
            recommendations.append(
                "💡 Adicione suporte a dark mode seguindo tendências 2025")

        if not trends.get("bold_typography", False):
            recommendations.append(
                "🔤 Use typography bold e capitalizada para maior impacto visual")

        if not trends.get("animations", False):
            recommendations.append(
                "✨ Adicione micro-animações para melhor UX (considere framer-motion)")

        if not trends.get("glassmorphism", False):
            recommendations.append(
                "🌫️ Considere efeitos glassmorphism com backdrop-blur")

        # Recomendações baseadas em padrões React
        if not patterns.get("custom_hooks", False):
            recommendations.append(
                "🔧 Extraia lógica repetitiva para custom hooks")

        if not patterns.get("memo_usage", False) and len(code) > 300:
            recommendations.append(
                "⚡ Use React.memo para componentes que não mudam frequentemente")

        if not patterns.get("typescript_usage", False):
            recommendations.append(
                "🛡️ Migre para TypeScript para melhor type safety")

        if not patterns.get("compound_components", False) and any(word in code.lower() for word in ["modal", "form", "accordion"]):
            recommendations.append(
                "🧩 Considere compound components pattern para maior flexibilidade")

        # Recomendações de bibliotecas modernas
        if not trends.get("modern_ui_lib", False):
            recommendations.append(
                "📚 Considere usar Tailwind CSS + shadcn/ui para UI components modernos")

        # Recomendações baseadas em performance
        if len(performance) > 3:
            recommendations.append(
                "🚀 Foque em otimizações de performance - muitos problemas detectados")

        # Recomendações baseadas em acessibilidade
        if len(accessibility) > 2:
            recommendations.append(
                "♿ Priorize melhorias de acessibilidade para inclusão")

        return recommendations

    async def _suggest_modern_code_alternatives(self, code: str, component_type: str) -> List[str]:
        """Sugere alternativas modernas para o código"""
        alternatives = []

        # Sugestões baseadas no tipo de componente
        if "form" in component_type.lower() or "form" in code.lower():
            alternatives.extend([
                "📝 Use React Hook Form + Zod para validação type-safe",
                "🎯 Implemente compound components (Form.Root, Form.Field, Form.Submit)",
                "✅ Adicione validação em tempo real com feedback visual"
            ])

        if "modal" in code.lower() or "dialog" in code.lower():
            alternatives.extend([
                "🪟 Use Radix UI ou Headless UI para base acessível",
                "🎭 Implemente compound pattern (Modal.Root, Modal.Content, Modal.Trigger)",
                "🎬 Adicione animações com Framer Motion variants"
            ])

        if "button" in code.lower():
            alternatives.extend([
                "🎨 Use shadcn/ui Button com variants system",
                "⚡ Adicione loading states e disabled handling",
                "🎯 Implemente size variants (sm, md, lg, xl)"
            ])

        # Sugestões gerais de modernização
        alternatives.extend([
            "🌙 Implemente dark mode nativo com 'dark:' classes",
            "📱 Garanta responsive design mobile-first",
            "🎪 Use Framer Motion para micro-animações contextuais",
            "🔧 Extraia lógica para custom hooks reutilizáveis",
            "📦 Considere code splitting com React.lazy",
            "♿ Adicione comprehensive accessibility (WCAG 2.1 AA)"
        ])

        return alternatives

    async def _calculate_code_score(
        self, trends: Dict[str, bool], patterns: Dict[str, bool],
        performance_issues: List[str], accessibility_issues: List[str]
    ) -> int:
        """Calcula score final do código baseado em todos os fatores"""
        base_score = 70

        # Bonus por tendências implementadas
        trends_bonus = sum(trends.values()) * 3

        # Bonus por padrões React modernos
        patterns_bonus = sum(patterns.values()) * 2

        # Penalidade por problemas
        performance_penalty = len(performance_issues) * 5
        accessibility_penalty = len(accessibility_issues) * 7

        final_score = base_score + trends_bonus + patterns_bonus - \
            performance_penalty - accessibility_penalty

        return max(0, min(100, final_score))

    # ================================
    # MÉTODOS DE ANÁLISE DE PROMPT
    # ================================

    async def _detect_component_type(self, prompt: str) -> ComponentType:
        """Detecta o tipo de componente baseado no prompt"""
        prompt_lower = prompt.lower()

        # Layout components
        if any(word in prompt_lower for word in ["header", "footer", "sidebar", "layout", "grid", "container"]):
            return ComponentType.LAYOUT

        # Form components
        if any(word in prompt_lower for word in ["form", "input", "submit", "validation", "field"]):
            return ComponentType.FORM

        # Navigation components
        if any(word in prompt_lower for word in ["nav", "menu", "breadcrumb", "tab", "pagination"]):
            return ComponentType.NAVIGATION

        # Data display
        if any(word in prompt_lower for word in ["table", "list", "card", "chart", "dashboard"]):
            return ComponentType.DATA_DISPLAY

        # Feedback components
        if any(word in prompt_lower for word in ["modal", "toast", "alert", "notification", "loading"]):
            return ComponentType.FEEDBACK

        # Media components
        if any(word in prompt_lower for word in ["image", "video", "gallery", "carousel", "slider"]):
            return ComponentType.MEDIA

        # Default para interaction
        return ComponentType.INTERACTION

    async def _assess_prompt_complexity(self, prompt: str) -> ComplexityLevel:
        """Avalia a complexidade do componente solicitado"""
        complexity_indicators = {
            "simple": ["button", "icon", "text", "label"],
            "intermediate": ["form", "card", "modal", "dropdown", "tabs"],
            "complex": ["dashboard", "table", "chart", "editor", "calendar", "multi-step"]
        }

        prompt_lower = prompt.lower()

        # Verificar indicadores de complexidade
        for level, indicators in complexity_indicators.items():
            if any(indicator in prompt_lower for indicator in indicators):
                return ComplexityLevel(level)

        # Avaliar por tamanho e detalhes do prompt
        if len(prompt.split()) > 20:
            return ComplexityLevel.COMPLEX
        elif len(prompt.split()) > 10:
            return ComplexityLevel.INTERMEDIATE
        else:
            return ComplexityLevel.SIMPLE

    async def _identify_missing_prompt_elements(self, prompt: str, component_type: ComponentType) -> List[str]:
        """Identifica elementos essenciais que podem estar faltando no prompt"""
        missing = []
        prompt_lower = prompt.lower()

        # Elementos básicos que sempre devem ser considerados
        essential_elements = {
            "responsive": ["responsive", "mobile", "tablet", "breakpoint"],
            "accessibility": ["accessible", "a11y", "aria", "screen reader", "keyboard"],
            "styling": ["style", "design", "theme", "color", "tailwind", "css"],
            "state_management": ["state", "useState", "loading", "error", "success"],
            "typescript": ["typescript", "types", "interface", "props"],
            "performance": ["performance", "memo", "lazy", "optimization"]
        }

        for element, keywords in essential_elements.items():
            if not any(keyword in prompt_lower for keyword in keywords):
                missing.append(element)

        return missing

    async def _identify_applicable_patterns(self, prompt: str, component_type: ComponentType) -> List[str]:
        """Identifica padrões React que podem ser aplicados"""
        applicable = []
        prompt_lower = prompt.lower()

        # Verificar padrões baseados em keywords
        for pattern_name, pattern_info in self.patterns.COMPONENT_PATTERNS.items():
            if any(keyword in prompt_lower for keyword in pattern_info["keywords"]):
                applicable.append(pattern_name)

        # Padrões de performance baseados em contexto
        for pattern_name, pattern_info in self.patterns.PERFORMANCE_PATTERNS.items():
            if any(keyword in prompt_lower for keyword in pattern_info["keywords"]):
                applicable.append(pattern_name)

        return applicable

    async def _identify_applicable_trends(self, prompt: str, component_type: ComponentType) -> List[str]:
        """Identifica tendências UI 2025 aplicáveis"""
        applicable = []
        prompt_lower = prompt.lower()

        # Sempre aplicar algumas tendências básicas
        applicable.extend(
            ["dark_mode_first", "accessibility_first", "glassmorphism"])

        # Tendências específicas baseadas em keywords
        if any(word in prompt_lower for word in ["card", "modal", "hero", "premium"]):
            applicable.append("glassmorphism")

        if any(word in prompt_lower for word in ["button", "hover", "click", "feedback"]):
            applicable.append("micro_interactions")

        if any(word in prompt_lower for word in ["complex", "form", "step", "wizard"]):
            applicable.append("progressive_disclosure")

        return list(set(applicable))  # Remove duplicatas

# ================================
# OTIMIZADOR UNIFICADO
# ================================


class ReactUnifiedOptimizer:
    """Otimizador unificado para código React e prompts"""

    def __init__(self):
        self.patterns = ReactModernPatterns()
        self.trends = UIUXTrends2025()
        self.ai_tools = AIToolsIntegration()

    async def optimize_react_code(
        self,
        code: str,
        focus_areas: Optional[List[str]] = None
    ) -> CodeOptimizationResult:
        """Otimiza código React existente aplicando tendências 2025"""

        if focus_areas is None:
            focus_areas = ["performance",
                           "accessibility", "trends", "patterns"]

        optimized_code = code
        changes_made = []
        performance_improvements = []
        accessibility_improvements = []
        trend_alignments = []

        # Aplicar otimizações baseadas nas áreas de foco
        for area in focus_areas:
            if area == "performance":
                optimized_code, perf_changes = await self._optimize_code_performance(optimized_code)
                performance_improvements.extend(perf_changes)
                changes_made.extend(
                    [f"Performance: {change}" for change in perf_changes])

            elif area == "accessibility":
                optimized_code, a11y_changes = await self._optimize_code_accessibility(optimized_code)
                accessibility_improvements.extend(a11y_changes)
                changes_made.extend(
                    [f"Accessibility: {change}" for change in a11y_changes])

            elif area == "trends":
                optimized_code, trend_changes = await self._apply_2025_trends_to_code(optimized_code)
                trend_alignments.extend(trend_changes)
                changes_made.extend(
                    [f"Trends 2025: {change}" for change in trend_changes])

            elif area == "patterns":
                optimized_code, pattern_changes = await self._apply_modern_patterns_to_code(optimized_code)
                changes_made.extend(
                    [f"Patterns: {change}" for change in pattern_changes])

        return CodeOptimizationResult(
            original_code=code,
            optimized_code=optimized_code,
            changes_made=changes_made,
            performance_improvements=performance_improvements,
            accessibility_improvements=accessibility_improvements,
            trend_alignments=trend_alignments
        )

    async def optimize_prompt(
        self,
        original_prompt: str,
        target_ai_tool: AITool = AITool.GENERIC,
        component_type: Optional[ComponentType] = None,
        include_accessibility: bool = True,
        include_performance: bool = True
    ) -> PromptOptimizationResult:
        """Otimiza um prompt para gerar código React moderno"""

        analyzer = ReactUnifiedAnalyzer()
        analysis = await analyzer.analyze_prompt_quality(original_prompt)

        if component_type is None:
            component_type = analysis.detected_component_type

        # Construir prompt otimizado
        optimized_sections = []
        enhancements_applied = []
        modern_patterns = []
        ui_trends = []
        accessibility_features = []
        performance_considerations = []

        # 1. Contextualização inicial
        context_section = await self._build_context_section(component_type, analysis.complexity_level)
        optimized_sections.append(context_section)
        enhancements_applied.append("Contexto detalhado adicionado")

        # 2. Requisitos funcionais aprimorados
        functional_section = await self._enhance_functional_requirements(
            original_prompt, analysis, component_type
        )
        optimized_sections.append(functional_section)
        enhancements_applied.append("Requisitos funcionais expandidos")

        # 3. Padrões React modernos
        if analysis.potential_patterns:
            patterns_section = await self._add_react_patterns_to_prompt(analysis.potential_patterns)
            optimized_sections.append(patterns_section)
            modern_patterns.extend(analysis.potential_patterns)
            enhancements_applied.append("Padrões React modernos incluídos")

        # 4. Tendências UI 2025
        if analysis.ui_trends_applicable:
            trends_section = await self._add_ui_trends_to_prompt(analysis.ui_trends_applicable, component_type)
            optimized_sections.append(trends_section)
            ui_trends.extend(analysis.ui_trends_applicable)
            enhancements_applied.append("Tendências UI 2025 integradas")

        # 5. Acessibilidade
        if include_accessibility:
            a11y_section = await self._add_accessibility_to_prompt(component_type)
            optimized_sections.append(a11y_section)
            accessibility_features.extend(
                ["ARIA attributes", "Keyboard navigation", "Screen reader support"])
            enhancements_applied.append(
                "Requisitos de acessibilidade adicionados")

        # 6. Performance
        if include_performance:
            perf_section = await self._add_performance_to_prompt(analysis.complexity_level)
            optimized_sections.append(perf_section)
            performance_considerations.extend(
                ["Memoization", "Lazy loading", "Optimized rendering"])
            enhancements_applied.append("Otimizações de performance incluídas")

        # 7. Especificações técnicas
        tech_section = await self._add_technical_specifications_to_prompt()
        optimized_sections.append(tech_section)
        enhancements_applied.append("Especificações técnicas detalhadas")

        # Construir prompt final
        optimized_prompt = "\n\n".join(optimized_sections)

        # Gerar versões específicas para diferentes ferramentas AI
        ai_tool_specific = await self._generate_tool_specific_versions(
            optimized_prompt, target_ai_tool
        )

        return PromptOptimizationResult(
            original_prompt=original_prompt,
            optimized_prompt=optimized_prompt,
            ai_tool_specific=ai_tool_specific,
            enhancements_applied=enhancements_applied,
            modern_patterns_included=modern_patterns,
            ui_trends_integrated=ui_trends,
            accessibility_features=accessibility_features,
            performance_considerations=performance_considerations
        )

    # ================================
    # MÉTODOS DE OTIMIZAÇÃO DE CÓDIGO
    # ================================

    async def _optimize_code_performance(self, code: str) -> Tuple[str, List[str]]:
        """Aplica otimizações de performance ao código"""
        optimized = code
        changes = []

        # Adicionar React.memo se necessário
        if "export default" in code and "React.memo" not in code and len(code) > 200:
            optimized = re.sub(
                r'export default (\w+)',
                r'export default React.memo(\1)',
                optimized
            )
            changes.append(
                "Adicionado React.memo para otimização de re-renders")

        # Otimizar useEffect
        effect_pattern = r'useEffect\(\(\) => \{([^}]+)\}\)'
        if re.search(effect_pattern, optimized) and ", [])" not in optimized:
            optimized = re.sub(
                effect_pattern,
                r'useEffect(() => {\1}, [])',
                optimized
            )
            changes.append(
                "Adicionado array de dependências vazio ao useEffect")

        # Adicionar lazy loading para imagens
        if '<img' in optimized and 'loading="lazy"' not in optimized:
            optimized = re.sub(
                r'<img ([^>]*?)>',
                r'<img \1 loading="lazy">',
                optimized
            )
            changes.append("Adicionado lazy loading às imagens")

        # Sugerir memoização para operações pesadas
        if re.search(r'\.map\(|\.filter\(|\.sort\(', optimized) and "useMemo" not in optimized:
            changes.append(
                "Considere usar useMemo para operações de array computacionalmente pesadas")

        return optimized, changes

    async def _optimize_code_accessibility(self, code: str) -> Tuple[str, List[str]]:
        """Aplica melhorias de acessibilidade ao código"""
        optimized = code
        changes = []

        # Adicionar alt text às imagens
        img_pattern = r'<img ([^>]*?)(?<!alt=")(?<!alt="[^"]*")>'
        if re.search(img_pattern, optimized):
            optimized = re.sub(img_pattern, r'<img \1 alt="">', optimized)
            changes.append("Adicionado atributo alt às imagens")

        # Melhorar botões
        button_pattern = r'<div([^>]*)onClick'
        if re.search(button_pattern, optimized):
            changes.append(
                "Considere converter divs clicáveis para elementos button semânticos")

        # Adicionar roles ARIA
        if "role=" not in optimized and any(word in optimized.lower() for word in ["navigation", "menu", "dialog"]):
            changes.append("Considere adicionar roles ARIA apropriados")

        # Verificar headings
        if not re.search(r'<h[1-6]', optimized) and len(optimized) > 300:
            changes.append(
                "Adicione estrutura de headings (h1-h6) para melhor navegação")

        return optimized, changes

    async def _apply_2025_trends_to_code(self, code: str) -> Tuple[str, List[str]]:
        """Aplica tendências de design 2025 ao código"""
        optimized = code
        changes = []

        # Adicionar suporte a dark mode
        if "dark:" not in code and "darkMode" not in code:
            changes.append(
                "Considere adicionar suporte a dark mode com classes 'dark:'")

        # Melhorar typography
        if "font-bold" not in code and "font-weight" not in code:
            changes.append(
                "Considere aplicar typography bold para maior impacto visual")

        # Adicionar micro-animations
        if "transition" not in code and "framer-motion" not in code:
            changes.append(
                "Adicione micro-animações com transitions ou Framer Motion")

        # Glassmorphism effects
        if "backdrop-blur" not in code:
            changes.append("Considere efeitos glassmorphism com backdrop-blur")

        return optimized, changes

    async def _apply_modern_patterns_to_code(self, code: str) -> Tuple[str, List[str]]:
        """Aplica padrões React modernos ao código"""
        optimized = code
        changes = []

        # Sugerir custom hook se houver lógica repetitiva
        if "useState" in code and "useEffect" in code and "use" not in code[:50]:
            changes.append(
                "Considere extrair lógica para custom hook reutilizável")

        # Sugerir TypeScript
        if "React.FC" not in code and "interface" not in code:
            changes.append(
                "Considere migrar para TypeScript para melhor type safety")

        # Sugerir compound components
        if any(word in code.lower() for word in ["modal", "form", "accordion"]) and code.count(".") < 3:
            changes.append(
                "Considere compound components pattern para maior flexibilidade")

        return optimized, changes

    # ================================
    # MÉTODOS DE OTIMIZAÇÃO DE PROMPT
    # ================================

    async def _build_context_section(self, component_type: ComponentType, complexity: ComplexityLevel) -> str:
        """Constrói seção de contexto detalhado para o prompt"""
        context_templates = {
            ComponentType.FORM: "Crie um componente de formulário React moderno e acessível",
            ComponentType.LAYOUT: "Desenvolva um componente de layout React responsivo e flexível",
            ComponentType.NAVIGATION: "Implemente um componente de navegação React intuitivo",
            ComponentType.DATA_DISPLAY: "Construa um componente de exibição de dados React eficiente",
            ComponentType.FEEDBACK: "Crie um componente de feedback React com UX otimizada",
            ComponentType.INTERACTION: "Desenvolva um componente interativo React engajante",
            ComponentType.MEDIA: "Implemente um componente de mídia React performático"
        }

        base_context = context_templates.get(
            component_type, "Crie um componente React moderno")

        complexity_additions = {
            ComplexityLevel.SIMPLE: "focado em simplicidade e usabilidade",
            ComplexityLevel.INTERMEDIATE: "com funcionalidades equilibradas e boa UX",
            ComplexityLevel.COMPLEX: "com arquitetura robusta e recursos avançados"
        }

        return f"🎯 **Objetivo:** {base_context} {complexity_additions[complexity]}."

    async def _enhance_functional_requirements(
        self, original_prompt: str, analysis: PromptAnalysisResult, component_type: ComponentType
    ) -> str:
        """Aprimora os requisitos funcionais do prompt original"""

        enhanced_prompt = f"**Requisitos Funcionais:**\n{original_prompt}"

        # Adicionar elementos faltantes identificados na análise
        if analysis.missing_elements:
            missing_text = []
            if "responsive" in analysis.missing_elements:
                missing_text.append(
                    "- Implemente design totalmente responsivo (mobile-first approach)")
            if "accessibility" in analysis.missing_elements:
                missing_text.append(
                    "- Garanta acessibilidade completa (WCAG 2.1 AA)")
            if "styling" in analysis.missing_elements:
                missing_text.append(
                    "- Use Tailwind CSS para styling moderno e consistente")
            if "state_management" in analysis.missing_elements:
                missing_text.append(
                    "- Gerencie estado de forma eficiente com hooks apropriados")
            if "typescript" in analysis.missing_elements:
                missing_text.append(
                    "- Use TypeScript com interfaces bem definidas")
            if "performance" in analysis.missing_elements:
                missing_text.append(
                    "- Otimize performance com técnicas modernas React")

            if missing_text:
                enhanced_prompt += "\n\n**Requisitos Adicionais:**\n" + \
                    "\n".join(missing_text)

        return enhanced_prompt

    async def _add_react_patterns_to_prompt(self, patterns: List[str]) -> str:
        """Adiciona padrões React modernos ao prompt"""
        patterns_text = "**Padrões React Modernos a Implementar:**\n"

        pattern_instructions = {
            "compound_components": "Use compound components pattern para componentes flexíveis que trabalham juntos",
            "custom_hooks": "Extraia lógica em custom hooks reutilizáveis (ex: useForm, useFetch, useToggle)",
            "render_props": "Implemente render props para máxima flexibilidade de UI",
            "hoc_patterns": "Use Higher-Order Components para funcionalidades transversais",
            "memoization": "Aplique React.memo, useMemo e useCallback estrategicamente",
            "lazy_loading": "Implemente React.lazy e Suspense para carregamento otimizado"
        }

        instructions = []
        for pattern in patterns:
            if pattern in pattern_instructions:
                instructions.append(f"- {pattern_instructions[pattern]}")

        return patterns_text + "\n".join(instructions)

    async def _add_ui_trends_to_prompt(self, trends: List[str], component_type: ComponentType) -> str:
        """Adiciona tendências UI 2025 ao prompt"""
        trends_text = "**Tendências UI/UX 2025 a Integrar:**\n"

        trend_instructions = {
            "dark_mode_first": "- Implemente dark mode nativo: use 'dark:' classes, toggle suave, persistência",
            "glassmorphism": "- Aplique efeitos glassmorphism: backdrop-blur, transparências sutis, bordas suaves",
            "micro_interactions": "- Adicione micro-animações com Framer Motion: hover effects, transitions suaves",
            "progressive_disclosure": "- Use progressive disclosure: revelar informações gradualmente",
            "accessibility_first": "- Priorize acessibilidade: semântica HTML, ARIA, contraste adequado"
        }

        instructions = []
        for trend in trends:
            if trend in trend_instructions:
                instructions.append(trend_instructions[trend])

        # Sempre incluir Tailwind como base
        instructions.insert(
            0, "- Use Tailwind CSS como base: classes utilitárias, responsive design, utility-first")

        return trends_text + "\n".join(instructions)

    async def _add_accessibility_to_prompt(self, component_type: ComponentType) -> str:
        """Adiciona requisitos específicos de acessibilidade"""
        base_a11y = """**Requisitos de Acessibilidade (WCAG 2.1 AA):**
- Use HTML semântico apropriado (nav, main, section, article, etc.)
- Implemente ARIA labels, roles e properties onde necessário
- Garanta navegação por teclado completa (Tab, Enter, Escape, Arrow keys)
- Mantenha contraste mínimo de 4.5:1 para texto normal, 3:1 para texto grande
- Adicione indicadores visuais de foco claros e distintos
- Forneça texto alternativo para elementos não-textuais
- Implemente landmarks para navegação por screen readers"""

        return base_a11y

    async def _add_performance_to_prompt(self, complexity: ComplexityLevel) -> str:
        """Adiciona requisitos de performance baseados na complexidade"""
        base_perf = """**Otimizações de Performance:**
- Use React.memo para componentes puros que re-renderizam frequentemente
- Implemente useMemo para cálculos computacionalmente pesados
- Use useCallback para funções passadas como props
- Otimize imagens com loading="lazy" e tamanhos responsivos"""

        complexity_specific = {
            ComplexityLevel.SIMPLE: """
- Mantenha bundle size mínimo
- Evite dependências desnecessárias""",
            ComplexityLevel.INTERMEDIATE: """
- Implemente code splitting por componente se necessário
- Use React.Suspense para loading states
- Considere virtualization para listas > 100 items""",
            ComplexityLevel.COMPLEX: """
- Implemente code splitting agressivo
- Use React.Suspense com error boundaries
- Implemente virtualization para performance
- Considere Web Workers para processamento pesado
- Use service workers para caching estratégico"""
        }

        return base_perf + complexity_specific[complexity]

    async def _add_technical_specifications_to_prompt(self) -> str:
        """Adiciona especificações técnicas modernas"""
        return """**Especificações Técnicas:**
- **Framework:** React 18+ com hooks modernos
- **TypeScript:** Interfaces bem definidas, props tipadas, generic types quando apropriado
- **Styling:** Tailwind CSS 3.x + shadcn/ui components quando apropriado
- **State:** useState/useReducer para estado local, Context API para estado global
- **Effects:** useEffect com cleanup apropriado, dependency arrays otimizadas
- **Animation:** Framer Motion para micro-animações e transitions
- **Testing:** Prepare componente para testing (data-testid, semantic HTML)
- **Build:** Compatible com Next.js 14+, Vite, ou Create React App
- **Browser Support:** Compatível com browsers modernos (ES2020+)"""

    async def _generate_tool_specific_versions(
        self, optimized_prompt: str, target_tool: AITool
    ) -> Dict[str, str]:
        """Gera versões específicas para diferentes ferramentas AI"""

        versions = {}

        # Versão para v0.dev (Vercel)
        v0_prefix = """🎯 **Para v0.dev (Vercel):** Gere um componente React completo e funcional seguindo exatamente estas especificações:

"""
        v0_suffix = """

**Saída Esperada:**
- Componente React funcional com TypeScript
- Styling completo com Tailwind CSS
- Responsivo para mobile/tablet/desktop
- Estados de loading/error/success quando aplicável
- Pronto para uso em Next.js 14+"""

        versions["v0_dev"] = v0_prefix + optimized_prompt + v0_suffix

        # Versão para Cursor/Copilot
        cursor_prefix = """🤖 **Context for Cursor/Copilot:** Generate modern React component following current project patterns:

"""
        cursor_suffix = """

**Code Requirements:**
- Use existing project conventions and imports
- Follow established file structure and naming
- Include comprehensive JSDoc comments
- Add proper error boundaries where needed
- Ensure compatibility with existing codebase"""

        versions["cursor"] = cursor_prefix + optimized_prompt + cursor_suffix

        # Versão para Visual Copilot (Figma to Code)
        visual_prefix = """🎨 **For Visual Copilot (Figma to React):** Transform this design into semantic, accessible React code:

"""
        visual_suffix = """

**Code Generation Focus:**
- Semantic HTML structure with proper hierarchy
- Component props interface matching design tokens
- Responsive behavior for all breakpoints
- Pixel-perfect implementation with Tailwind utilities
- Component composition following React best practices"""

        versions["visual_copilot"] = visual_prefix + \
            optimized_prompt + visual_suffix

        # Versão genérica otimizada
        versions["generic"] = optimized_prompt

        return versions

# ================================
# FERRAMENTAS MCP UNIFICADAS
# ================================


@mcp.tool()
async def analyze_react_code(
    code: str,
    component_type: str = "component"
) -> Dict[str, Any]:
    """
    Analisa código React existente para conformidade com melhores práticas de UI/UX 2025.

    Args:
        code: Código do componente React existente
        component_type: Tipo do componente (component, dashboard, portfolio, landing)

    Returns:
        Análise completa com score, conformidade com tendências, e recomendações
    """
    try:
        analyzer = ReactUnifiedAnalyzer()
        analysis = await analyzer.analyze_react_code(code, component_type)

        logger.info(
            f"React code analyzed - component_type: {component_type}, score: {analysis.score}")

        return {
            'score': analysis.score,
            'trends_compliance': analysis.trends_compliance,
            'design_patterns': analysis.design_patterns,
            'performance_issues': analysis.performance_issues,
            'accessibility_issues': analysis.accessibility_issues,
            'recommendations': analysis.recommendations,
            'modern_alternatives': analysis.modern_alternatives
        }

    except Exception as e:
        logger.error(f"Error analyzing React code: {str(e)}")
        raise


@mcp.tool()
async def optimize_react_code(
    code: str,
    focus_areas: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Otimiza código React existente aplicando melhores práticas modernas.

    Args:
        code: Código do componente React existente
        focus_areas: Áreas de foco (performance, accessibility, trends, patterns)

    Returns:
        Código otimizado com explicação das mudanças
    """
    try:
        optimizer = ReactUnifiedOptimizer()
        optimization = await optimizer.optimize_react_code(code, focus_areas)

        logger.info(
            f"React code optimized - changes_count: {len(optimization.changes_made)}")

        return {
            'original_code': optimization.original_code,
            'optimized_code': optimization.optimized_code,
            'changes_made': optimization.changes_made,
            'performance_improvements': optimization.performance_improvements,
            'accessibility_improvements': optimization.accessibility_improvements,
            'trend_alignments': optimization.trend_alignments
        }

    except Exception as e:
        logger.error(f"Error optimizing React code: {str(e)}")
        raise


@mcp.tool()
async def analyze_react_prompt(prompt: str) -> Dict[str, Any]:
    """
    Analisa um prompt básico para React e identifica oportunidades de melhoria.

    Args:
        prompt: Prompt original do usuário

    Returns:
        Análise detalhada com sugestões de melhorias
    """
    try:
        analyzer = ReactUnifiedAnalyzer()
        analysis = await analyzer.analyze_prompt_quality(prompt)

        logger.info(
            f"React prompt analyzed - component_type: {analysis.detected_component_type.value}, complexity: {analysis.complexity_level.value}")

        return {
            'original_prompt': analysis.original_prompt,
            'detected_component_type': analysis.detected_component_type.value,
            'complexity_level': analysis.complexity_level.value,
            'missing_elements': analysis.missing_elements,
            'potential_patterns': analysis.potential_patterns,
            'ui_trends_applicable': analysis.ui_trends_applicable
        }

    except Exception as e:
        logger.error(f"Error analyzing React prompt: {str(e)}")
        raise


@mcp.tool()
async def optimize_react_prompt(
    prompt: str,
    target_ai_tool: str = "generic",
    component_type: Optional[str] = None,
    include_accessibility: bool = True,
    include_performance: bool = True
) -> Dict[str, Any]:
    """
    Otimiza um prompt para gerar código React moderno e intuitivo.

    Args:
        prompt: Prompt original do usuário
        target_ai_tool: Ferramenta AI alvo (v0_dev, cursor, visual_copilot, generic)
        component_type: Tipo de componente (layout, form, navigation, etc.)
        include_accessibility: Incluir requisitos de acessibilidade
        include_performance: Incluir otimizações de performance

    Returns:
        Prompt otimizado com enhancements aplicados
    """
    try:
        optimizer = ReactUnifiedOptimizer()

        # Converter strings para enums
        ai_tool = AITool(
            target_ai_tool) if target_ai_tool != "generic" else AITool.GENERIC
        comp_type = ComponentType(component_type) if component_type else None

        optimization = await optimizer.optimize_prompt(
            original_prompt=prompt,
            target_ai_tool=ai_tool,
            component_type=comp_type,
            include_accessibility=include_accessibility,
            include_performance=include_performance
        )

        logger.info(
            f"React prompt optimized - enhancements_count: {len(optimization.enhancements_applied)}, target_tool: {target_ai_tool}")

        return {
            'original_prompt': optimization.original_prompt,
            'optimized_prompt': optimization.optimized_prompt,
            'ai_tool_specific': optimization.ai_tool_specific,
            'enhancements_applied': optimization.enhancements_applied,
            'modern_patterns_included': optimization.modern_patterns_included,
            'ui_trends_integrated': optimization.ui_trends_integrated,
            'accessibility_features': optimization.accessibility_features,
            'performance_considerations': optimization.performance_considerations
        }

    except Exception as e:
        logger.error(f"Error optimizing React prompt: {str(e)}")
        raise


@mcp.tool()
async def validate_prompt_quality(prompt: str) -> Dict[str, Any]:
    """
    Valida a qualidade de um prompt para geração de código React com score 0-100.

    Args:
        prompt: Prompt a ser validado

    Returns:
        Score de qualidade e checklist de melhorias
    """

    # Critérios simples de validação
    score = 50  # Score base
    improvements = []

    # Verificações básicas
    words = prompt.split()

    if len(words) >= 10:
        score += 10
    else:
        improvements.append("Adicione mais contexto - prompt muito curto")

    if "react" in prompt.lower():
        score += 15
    else:
        improvements.append("Mencione React explicitamente")

    if any(word in prompt.lower() for word in ["component", "form", "button", "modal"]):
        score += 10
    else:
        improvements.append("Especifique o tipo de componente")

    if any(word in prompt.lower() for word in ["responsive", "mobile"]):
        score += 10
    else:
        improvements.append("Considere mencionar responsividade")

    if any(word in prompt.lower() for word in ["accessible", "a11y"]):
        score += 15
    else:
        improvements.append("Considere requisitos de acessibilidade")

    # Determinar classificação
    if score >= 90:
        grade = "Excelente"
        recommendation = "Prompt pronto para uso com ferramentas AI avançadas"
    elif score >= 75:
        grade = "Bom"
        recommendation = "Prompt sólido, pequenos ajustes podem melhorar resultados"
    elif score >= 60:
        grade = "Adequado"
        recommendation = "Prompt funcional, mas se beneficiaria de mais detalhes"
    else:
        grade = "Básico"
        recommendation = "Prompt precisa de melhorias significativas"

    return {
        "overall_score": score,
        "grade": grade,
        "recommendation": recommendation,
        "improvements_needed": improvements,
        "prompt_length": len(words)
    }


@mcp.tool()
async def generate_component_template(
    component_type: str,
    complexity: str = "intermediate",
    target_ai_tool: str = "generic",
    include_examples: bool = True
) -> Dict[str, Any]:
    """
    Gera um template de prompt otimizado para tipo específico de componente React.

    Args:
        component_type: Tipo do componente (form, modal, card, dashboard, etc.)
        complexity: Nível de complexidade (simple, intermediate, complex)
        target_ai_tool: Ferramenta AI alvo (v0_dev, cursor, visual_copilot, generic)
        include_examples: Incluir exemplos de uso

    Returns:
        Template de prompt estruturado e otimizado
    """

    templates = {
        "form": {
            "base": "Crie um formulário React moderno e acessível",
            "requirements": [
                "Validação em tempo real com feedback visual",
                "Estados de loading, success e error",
                "Campos responsivos com labels apropriados",
                "Suporte a keyboard navigation completo"
            ],
            "patterns": ["custom_hooks", "compound_components"],
            "example": "Formulário de contato com nome, email, mensagem e botão submit"
        },
        "modal": {
            "base": "Desenvolva um modal React flexível e acessível",
            "requirements": [
                "Backdrop com glassmorphism effect",
                "Animações de entrada e saída suaves",
                "Focus trap para acessibilidade",
                "Fechamento com Escape key e click outside"
            ],
            "patterns": ["compound_components", "render_props"],
            "example": "Modal de confirmação com título, corpo e botões de ação"
        },
        "card": {
            "base": "Construa um componente Card React versátil",
            "requirements": [
                "Variants para diferentes estilos",
                "Suporte a imagem, header, body e footer",
                "Hover effects e micro-animações",
                "Grid responsivo quando usado em listas"
            ],
            "patterns": ["compound_components"],
            "example": "Card de produto com imagem, título, descrição e preço"
        },
        "dashboard": {
            "base": "Desenvolva um dashboard React escalável e intuitivo",
            "requirements": [
                "Cards métricas com visualizações dinâmicas",
                "Filtros e pesquisa em tempo real",
                "Estados de loading skeleton",
                "Responsividade total (mobile-first)"
            ],
            "patterns": ["custom_hooks", "context_api", "lazy_loading"],
            "example": "Dashboard de vendas com métricas, gráficos e filtros"
        }
    }

    if component_type not in templates:
        return {"error": f"Tipo de componente '{component_type}' não suportado. Use: {', '.join(templates.keys())}"}

    template = templates[component_type]

    # Construir prompt baseado no template
    sections = []

    # Seção base
    sections.append(f"🎯 **Objetivo:** {template['base']}")

    # Requisitos específicos
    sections.append("**Requisitos Específicos:**")
    for req in template["requirements"]:
        sections.append(f"- {req}")

    # Padrões React recomendados
    sections.append("**Padrões React a Implementar:**")
    pattern_descriptions = {
        "custom_hooks": "Custom hooks para lógica reutilizável (ex: useForm, useValidation)",
        "compound_components": "Compound components para máxima flexibilidade",
        "render_props": "Render props para customização de UI",
        "context_api": "Context API para compartilhamento de estado",
        "lazy_loading": "Lazy loading para otimização de performance"
    }

    for pattern in template["patterns"]:
        if pattern in pattern_descriptions:
            sections.append(f"- {pattern_descriptions[pattern]}")

    # Especificações técnicas modernas
    tech_specs = [
        "TypeScript com interfaces bem definidas",
        "Tailwind CSS + shadcn/ui para styling consistente",
        "Framer Motion para animações suaves",
        "Suporte completo a dark mode",
        "Acessibilidade WCAG 2.1 AA",
        "Performance otimizada com memoização"
    ]

    sections.append("**Especificações Técnicas:**")
    for spec in tech_specs:
        sections.append(f"- {spec}")

    # Exemplo de uso
    if include_examples:
        sections.append(f"**Exemplo de Uso:** {template['example']}")

    # Versões específicas para ferramentas AI
    base_prompt = "\n\n".join(sections)

    optimizer = ReactUnifiedOptimizer()
    ai_versions = await optimizer._generate_tool_specific_versions(
        base_prompt, AITool(
            target_ai_tool) if target_ai_tool != "generic" else AITool.GENERIC
    )

    return {
        "component_type": component_type,
        "template_prompt": base_prompt,
        "ai_tool_versions": ai_versions,
        "recommended_patterns": template["patterns"],
        "complexity_level": complexity,
        "target_ai_tool": target_ai_tool
    }


@mcp.tool()
async def get_react_trends_2025() -> Dict[str, Any]:
    """
    Retorna as principais tendências React e UI/UX para 2025.

    Returns:
        Guia completo de tendências atualizadas
    """
    trends = UIUXTrends2025()
    patterns = ReactModernPatterns()

    return {
        "ui_ux_trends": {
            "typography": trends.TYPOGRAPHY_TRENDS,
            "design": trends.DESIGN_TRENDS,
            "ux_patterns": trends.UX_PATTERNS
        },

        "react_patterns": {
            "component_patterns": patterns.COMPONENT_PATTERNS,
            "performance_patterns": patterns.PERFORMANCE_PATTERNS
        },

        "styling_recommendations": {
            "primary": "Tailwind CSS como base utility-first",
            "components": "shadcn/ui para componentes acessíveis",
            "animations": "Framer Motion para micro-animações",
            "themes": "Dark mode nativo com persistência"
        },

        "development_stack": {
            "framework": "React 18+ com hooks modernos",
            "typescript": "Type safety como padrão",
            "building": "Next.js 14+ ou Vite para performance",
            "testing": "React Testing Library + Jest"
        },

        "ai_integration": {
            "v0_dev": "Prompts específicos para Vercel's v0",
            "cursor": "Context-aware development",
            "visual_copilot": "Figma to React conversion",
            "best_practices": "Structured prompting para melhores resultados"
        },

        "summary": "Tendências baseadas em pesquisa de 25+ templates React opensource e sites premiados pelo Awwwards"
    }

# ================================
# RECURSOS E RECURSOS ADICIONAIS
# ================================


@mcp.resource(uri="guide://react-development-2025")
async def get_react_development_guide() -> str:
    """Guia completo de desenvolvimento React 2025"""
    return json.dumps({
        "title": "Guia Completo de Desenvolvimento React 2025",
        "sections": {
            "code_analysis": "Análise de código React existente com score e recomendações",
            "code_optimization": "Otimização automática seguindo tendências 2025",
            "prompt_analysis": "Análise de qualidade de prompts para geração de código",
            "prompt_optimization": "Transformação de prompts básicos em versões otimizadas",
            "modern_patterns": ReactModernPatterns.COMPONENT_PATTERNS,
            "ui_trends": UIUXTrends2025.DESIGN_TRENDS,
            "ai_tools_integration": AIToolsIntegration.TOOLS_OPTIMIZATION
        }
    }, indent=2)


@mcp.resource(uri="templates://component-library")
async def get_component_templates() -> str:
    """Biblioteca de templates para diferentes tipos de componentes"""

    library = {
        "forms": {
            "contact_form": "Formulário de contato com validação completa",
            "signup_form": "Formulário de cadastro com validação de senha",
            "search_form": "Formulário de pesquisa com autocomplete"
        },
        "layouts": {
            "header": "Header responsivo com navegação e tema toggle",
            "sidebar": "Sidebar colapsível com navegação hierárquica",
            "footer": "Footer completo com links e informações"
        },
        "data_display": {
            "data_table": "Tabela de dados com sorting, filtering e paginação",
            "card_grid": "Grid de cards responsivo com loading states",
            "dashboard": "Dashboard com métricas e gráficos interativos"
        },
        "feedback": {
            "modal": "Modal acessível com compound components",
            "toast": "Sistema de notificações toast",
            "loading": "Componentes de loading (skeleton, spinner)"
        }
    }

    return json.dumps(library, indent=2)

# ================================
# INICIALIZAÇÃO DO SERVIDOR
# ================================

if __name__ == "__main__":
    import uvicorn

    logger.info("Starting React Development Optimizer MCP Server")
    logger.info(
        "Features: Code Analysis + Optimization | Prompt Analysis + Optimization")
    logger.info(
        "Based on: 25+ React templates + UI/UX trends 2025 + AI prompting best practices")

    # Executar o servidor MCP
    mcp.run()
