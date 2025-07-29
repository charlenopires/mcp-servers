"""
React 19 Advanced MCP Server - Servidor MCP para desenvolvimento React moderno
==============================================================================

Servidor MCP avançado para desenvolvimento com React 19, incluindo:
- Server Components estáveis
- Actions e form handling modernos
- Hook `use` para recursos assíncronos
- Ref as prop e melhorias de performance
- Concurrent rendering e transitions
- Integração com frameworks modernos (Next.js 15+, Vite 6+)

Baseado nas últimas funcionalidades do React 19 (December 2024) e melhores práticas 2025.
"""

from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass
from enum import Enum
from fastmcp import FastMCP, Context
from pydantic import BaseModel, Field
import re
import json
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializar servidor MCP
mcp = FastMCP(
    name="react-19-advanced",
    version="19.0.0",
    description="Servidor MCP avançado para desenvolvimento React 19 com funcionalidades modernas"
)


# ================================
# REACT 19 CONTEXT AND KNOWLEDGE BASE
# ================================

class ReactFeatureType(Enum):
    ACTIONS = "actions"
    SERVER_COMPONENTS = "server_components"
    USE_HOOK = "use_hook"
    FORM_HANDLING = "form_handling"
    CONCURRENT = "concurrent"
    PERFORMANCE = "performance"

class ReactFramework(Enum):
    NEXTJS = "nextjs"
    VITE = "vite"
    REMIX = "remix"
    GATSBY = "gatsby"
    CREATE_REACT_APP = "cra"

@dataclass
class AnalisePrompt:
    """Resultado da análise de um prompt React"""
    prompt_original: str
    pontuacao: float
    areas_fortes: List[str]
    areas_fracas: List[str]
    sugestoes: List[str]
    prompt_melhorado: str
    react_19_features: List[str]
    recommended_patterns: List[str]

class React19Context:
    """Base de conhecimento do React 19 e funcionalidades modernas"""
    
    VERSION = "19.0.0"
    RELEASE_DATE = "2024-12-05"
    
    FEATURES = {
        "actions": {
            "description": "Actions para handling de async operations com form states",
            "benefits": [
                "Automatic pending states management",
                "Optimistic updates built-in", 
                "Improved error handling for async calls",
                "Better form submission patterns"
            ],
            "use_cases": ["Form submissions", "Data mutations", "Async operations"],
            "example": """
// React 19 Actions example
function SubmitForm() {
  async function submitAction(formData) {
    // Actions automatically handle pending states
    const result = await submitToServer(formData);
    return result;
  }

  return (
    <form action={submitAction}>
      <input name="email" type="email" required />
      <button type="submit">Submit</button>
    </form>
  );
}"""
        },
        "server_components": {
            "description": "Server Components estáveis para rendering no servidor",
            "benefits": [
                "Reduced JavaScript bundle size",
                "Faster initial page loads",
                "Better SEO performance",
                "Direct database access capabilities"
            ],
            "use_cases": ["Static content", "Data fetching", "Server-side rendering"],
            "example": """
// React 19 Server Component
async function UserProfile({ userId }) {
  // Direct database access in Server Components
  const user = await db.user.findUnique({ where: { id: userId } });
  
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}"""
        },
        "use_hook": {
            "description": "Novo hook `use` para consumir recursos assíncronos",
            "benefits": [
                "Simplified async data fetching",
                "Better integration with Suspense",
                "Cleaner component code",
                "Promise-based resource consumption"
            ],
            "use_cases": ["Data fetching", "Resource loading", "Async operations"],
            "example": """
// React 19 use hook
import { use } from 'react';

function UserComponent({ userPromise }) {
  const user = use(userPromise);
  
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}"""
        },
        "ref_as_prop": {
            "description": "Ref como prop direta em function components",
            "benefits": [
                "No more forwardRef needed",
                "Simpler component APIs",
                "Better TypeScript support",
                "Cleaner component definitions"
            ],
            "use_cases": ["Component libraries", "Input components", "DOM access"],
            "example": """
// React 19 - Ref as prop (no forwardRef needed)
function MyInput({ ref, ...props }) {
  return <input ref={ref} {...props} />;
}

// Usage
function App() {
  const inputRef = useRef();
  return <MyInput ref={inputRef} />;
}"""
        },
        "enhanced_forms": {
            "description": "Melhorias nativas em formulários com Actions integration",
            "benefits": [
                "Automatic form validation",
                "Built-in loading states",
                "Better error handling",
                "Progressive enhancement support"
            ],
            "use_cases": ["Forms", "User input", "Data submission"],
            "example": """
// React 19 Enhanced Forms
function ContactForm() {
  const [error, setError] = useState(null);
  
  async function handleSubmit(formData) {
    try {
      await submitContact(formData);
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <form action={handleSubmit}>
      <input name="name" required />
      <input name="email" type="email" required />
      <textarea name="message" required />
      <button type="submit">Send Message</button>
      {error && <div className="error">{error}</div>}
    </form>
  );
}"""
        }
    }
    
    FRAMEWORKS_SUPPORT = {
        ReactFramework.NEXTJS: {
            "version": "15.0+",
            "features": ["App Router with React 19", "Server Components", "Server Actions", "Streaming"],
            "setup": "npx create-next-app@latest --typescript --tailwind"
        },
        ReactFramework.VITE: {
            "version": "6.0+", 
            "features": ["Fast HMR", "React 19 support", "TypeScript", "Plugin ecosystem"],
            "setup": "npm create vite@latest my-app -- --template react-ts"
        },
        ReactFramework.REMIX: {
            "version": "2.0+",
            "features": ["Server-side rendering", "Forms", "Data loading", "React 19 integration"],
            "setup": "npx create-remix@latest"
        }
    }

# Base de conhecimento de melhores práticas React 19
MELHORES_PRATICAS = {
    "arquitetura": {
        "keywords": ["componente", "component", "estrutura", "arquitetura", "organização"],
        "praticas": [
            "Usar componentes pequenos, focados e reutilizáveis",
            "Aplicar o Princípio da Responsabilidade Única",
            "Organizar componentes em estrutura modular",
            "Separar lógica de apresentação"
        ]
    },
    "typescript": {
        "keywords": ["typescript", "tipos", "types", "interface", "tipagem"],
        "praticas": [
            "Definir interfaces para props e estado",
            "Usar tipos genéricos para componentes reutilizáveis",
            "Aplicar strict mode no tsconfig.json",
            "Tipar manipuladores de eventos corretamente"
        ]
    },
    "hooks": {
        "keywords": ["hooks", "useState", "useEffect", "custom hook"],
        "praticas": [
            "Preferir componentes funcionais com Hooks",
            "Criar custom hooks para lógica reutilizável",
            "Gerenciar arrays de dependências corretamente",
            "Evitar useEffect desnecessários"
        ]
    },
    "performance": {
        "keywords": ["performance", "otimização", "memoização", "lazy", "virtual"],
        "praticas": [
            "Implementar React.memo para componentes puros",
            "Usar useMemo e useCallback estrategicamente",
            "Aplicar code splitting com React.lazy",
            "Virtualizar listas grandes com react-window"
        ]
    },
    "estado": {
        "keywords": ["estado", "state", "redux", "zustand", "context"],
        "praticas": [
            "Escolher a solução de estado apropriada",
            "Evitar estado redundante e duplicado",
            "Estruturar estado de forma plana",
            "Elevar estado apenas quando necessário"
        ]
    },
    "ui_ux": {
        "keywords": ["ui", "ux", "interface", "design", "responsivo", "acessibilidade"],
        "praticas": [
            "Implementar design responsivo mobile-first",
            "Garantir acessibilidade com ARIA labels",
            "Usar sistemas de design consistentes",
            "Aplicar feedback visual para ações do usuário"
        ]
    },
    "testes": {
        "keywords": ["teste", "test", "jest", "testing library"],
        "praticas": [
            "Escrever testes unitários para componentes",
            "Implementar testes de integração",
            "Usar React Testing Library",
            "Manter cobertura de testes adequada"
        ]
    },
    "codigo_limpo": {
        "keywords": ["clean", "limpo", "legível", "manutenível"],
        "praticas": [
            "Seguir convenções de nomenclatura (PascalCase para componentes)",
            "Usar ESLint e Prettier para consistência",
            "Documentar componentes complexos",
            "Aplicar princípios DRY e SOLID"
        ]
    }
}

# Templates de prompts otimizados
TEMPLATES_PROMPTS = {
    "componente_basico": """
Crie um componente React com TypeScript seguindo estas especificações:

**Requisitos Funcionais:**
{requisitos_funcionais}

**Requisitos Técnicos:**
- TypeScript com tipos explícitos para props e estado
- Componente funcional usando Hooks modernos
- Seguir convenções de nomenclatura (PascalCase para componente, camelCase para funções)
- Implementar tratamento de erros apropriado
- Adicionar comentários JSDoc para props

**Estrutura e Organização:**
- Organizar em pasta própria com arquivo de teste
- Separar tipos/interfaces em arquivo próprio se complexo
- Usar barrel exports (index.ts) para exportação limpa

**Performance:**
- Aplicar React.memo se o componente for puro
- Usar useMemo/useCallback onde apropriado
- Implementar lazy loading se aplicável

**UI/UX e Acessibilidade:**
- Design responsivo mobile-first
- Incluir atributos ARIA apropriados
- Implementar navegação por teclado
- Fornecer feedback visual para estados (loading, erro, sucesso)

**Qualidade de Código:**
- Seguir princípios SOLID e DRY
- Código limpo e autoexplicativo
- Configuração ESLint/Prettier aplicada
""",

    "aplicacao_completa": """
Desenvolva uma aplicação React completa com TypeScript incluindo:

**Arquitetura e Estrutura:**
- Estrutura de pastas escalável e modular
- Separação clara de concerns (componentes, hooks, utils, types)
- Configuração de roteamento com React Router
- Setup de ferramentas (ESLint, Prettier, Husky)

**Gestão de Estado:**
- Implementar solução apropriada (Context API, Zustand, ou Redux Toolkit)
- Estado local vs global bem definido
- Evitar prop drilling
- Estado estruturado sem redundâncias

**Componentes e Reutilização:**
- Biblioteca de componentes reutilizáveis
- Sistema de design consistente
- Componentes compostos para UI complexa
- Custom hooks para lógica compartilhada

**Performance e Otimização:**
- Code splitting por rotas
- Lazy loading de componentes pesados
- Virtualização para listas grandes
- Otimização de re-renderizações

**UI/UX Excellence:**
- Design system implementado
- Tema claro/escuro
- Animações e transições suaves
- Padrões de interação intuitivos

**Acessibilidade (a11y):**
- Conformidade WCAG nível AA
- Navegação completa por teclado
- Leitores de tela suportados
- Contraste de cores adequado

**Testes e Qualidade:**
- Testes unitários com Jest e React Testing Library
- Testes de integração para fluxos críticos
- Configuração de CI/CD
- Documentação abrangente
"""
}


def analisar_areas_cobertas(prompt: str) -> Dict[str, bool]:
    """Analisa quais áreas de melhores práticas o prompt cobre"""
    areas_cobertas = {}
    prompt_lower = prompt.lower()

    for area, info in MELHORES_PRATICAS.items():
        # Verifica se alguma keyword da área está presente
        coberta = any(keyword in prompt_lower for keyword in info["keywords"])
        areas_cobertas[area] = coberta

    return areas_cobertas


def calcular_pontuacao(areas_cobertas: Dict[str, bool]) -> float:
    """Calcula pontuação baseada nas áreas cobertas"""
    total_areas = len(areas_cobertas)
    areas_cobertas_count = sum(areas_cobertas.values())

    # Pontuação base
    pontuacao = (areas_cobertas_count / total_areas) * 100

    # Bônus por áreas críticas
    areas_criticas = ["typescript", "performance",
                      "codigo_limpo", "arquitetura"]
    bonus = sum(10 for area in areas_criticas if areas_cobertas.get(area, False))

    return min(100, pontuacao + bonus)


def gerar_sugestoes(areas_cobertas: Dict[str, bool]) -> List[str]:
    """Gera sugestões baseadas nas áreas não cobertas"""
    sugestoes = []

    for area, coberta in areas_cobertas.items():
        if not coberta:
            info = MELHORES_PRATICAS[area]
            sugestao = f"Adicione requisitos sobre {area.replace('_', ' ')}: "
            sugestao += ", ".join(info["praticas"][:2])
            sugestoes.append(sugestao)

    return sugestoes


def melhorar_prompt(prompt_original: str, areas_cobertas: Dict[str, bool]) -> str:
    """Melhora o prompt adicionando aspectos faltantes"""
    prompt_melhorado = prompt_original.strip()

    # Adiciona seções faltantes
    secoes_adicionar = []

    if not areas_cobertas.get("typescript"):
        secoes_adicionar.append("""
**Requisitos TypeScript:**
- Use TypeScript com tipos explícitos para todas as props, estado e funções
- Defina interfaces claras para estruturas de dados
- Configure strict mode no tsconfig.json""")

    if not areas_cobertas.get("performance"):
        secoes_adicionar.append("""
**Otimização de Performance:**
- Implemente memoização onde apropriado (React.memo, useMemo, useCallback)
- Use lazy loading para componentes não críticos
- Considere virtualização para listas grandes""")

    if not areas_cobertas.get("ui_ux"):
        secoes_adicionar.append("""
**UI/UX e Acessibilidade:**
- Design responsivo que funcione bem em mobile e desktop
- Implemente acessibilidade seguindo padrões WCAG
- Forneça feedback visual claro para todas as interações""")

    if not areas_cobertas.get("codigo_limpo"):
        secoes_adicionar.append("""
**Qualidade de Código:**
- Siga convenções de nomenclatura do React (PascalCase para componentes)
- Configure ESLint e Prettier
- Escreva código limpo e autoexplicativo com comentários onde necessário""")

    if secoes_adicionar:
        prompt_melhorado += "\n\n" + "\n".join(secoes_adicionar)

    return prompt_melhorado


@mcp.tool()
async def analisar_prompt_react(prompt: str) -> AnalisePrompt:
    """
    Analisa um prompt para criação de código React e fornece feedback detalhado

    Args:
        prompt: O prompt a ser analisado

    Returns:
        Análise completa com pontuação, pontos fortes/fracos e sugestões
    """
    # Analisar áreas cobertas
    areas_cobertas = analisar_areas_cobertas(prompt)

    # Calcular pontuação
    pontuacao = calcular_pontuacao(areas_cobertas)

    # Identificar pontos fortes
    areas_fortes = [
        area.replace('_', ' ').title()
        for area, coberta in areas_cobertas.items()
        if coberta
    ]

    # Identificar pontos fracos
    areas_fracas = [
        area.replace('_', ' ').title()
        for area, coberta in areas_cobertas.items()
        if not coberta
    ]

    # Gerar sugestões
    sugestoes = gerar_sugestoes(areas_cobertas)

    # Melhorar prompt
    prompt_melhorado = melhorar_prompt(prompt, areas_cobertas)

    return AnalisePrompt(
        prompt_original=prompt,
        pontuacao=pontuacao,
        areas_fortes=areas_fortes,
        areas_fracas=areas_fracas,
        sugestoes=sugestoes,
        prompt_melhorado=prompt_melhorado
    )


@mcp.tool()
async def obter_template_prompt(tipo: str = "componente_basico") -> Dict[str, str]:
    """
    Obtém um template de prompt otimizado para React

    Args:
        tipo: Tipo de template ('componente_basico' ou 'aplicacao_completa')

    Returns:
        Template de prompt com estrutura otimizada
    """
    template = TEMPLATES_PROMPTS.get(
        tipo, TEMPLATES_PROMPTS["componente_basico"])

    return {
        "tipo": tipo,
        "template": template,
        "instrucoes": "Substitua {requisitos_funcionais} pelos requisitos específicos do seu projeto"
    }


@mcp.tool()
async def sugerir_melhorias_contextuais(
    prompt: str,
    contexto: str = "componente"
) -> Dict[str, Any]:
    """
    Sugere melhorias específicas baseadas no contexto do desenvolvimento

    Args:
        prompt: Prompt original
        contexto: Tipo de desenvolvimento ('componente', 'hook', 'aplicacao', 'biblioteca')

    Returns:
        Sugestões contextualizadas e prompt melhorado
    """
    melhorias_por_contexto = {
        "componente": [
            "Especifique se o componente deve ser controlado ou não-controlado",
            "Defina claramente as props obrigatórias e opcionais",
            "Inclua requisitos de acessibilidade específicos",
            "Mencione se deve suportar refs (forwardRef)"
        ],
        "hook": [
            "Defina o tipo de retorno do hook claramente",
            "Especifique se o hook deve ser síncrono ou assíncrono",
            "Inclua tratamento de cleanup/unmount",
            "Mencione se deve ter memoização interna"
        ],
        "aplicacao": [
            "Especifique a estratégia de roteamento desejada",
            "Defina requisitos de autenticação/autorização",
            "Inclua necessidades de internacionalização",
            "Mencione requisitos de PWA se aplicável"
        ],
        "biblioteca": [
            "Defina a API pública claramente",
            "Especifique compatibilidade de versões React",
            "Inclua requisitos de tree-shaking",
            "Mencione se deve suportar SSR"
        ]
    }

    melhorias = melhorias_por_contexto.get(
        contexto, melhorias_por_contexto["componente"])

    # Adicionar melhorias ao prompt
    prompt_melhorado = prompt + "\n\n**Requisitos Adicionais:**\n"
    prompt_melhorado += "\n".join(f"- {melhoria}" for melhoria in melhorias)

    return {
        "contexto": contexto,
        "melhorias_sugeridas": melhorias,
        "prompt_melhorado": prompt_melhorado
    }


@mcp.tool()
async def validar_requisitos_react(requisitos: str) -> Dict[str, Any]:
    """
    Valida se os requisitos incluem aspectos essenciais para desenvolvimento React

    Args:
        requisitos: String com os requisitos do projeto

    Returns:
        Validação detalhada com checklist e requisitos faltantes
    """
    checklist = {
        "tipagem_typescript": bool(re.search(r"typescript|tipos?|types?|interface", requisitos, re.I)),
        "gestao_estado": bool(re.search(r"estado|state|redux|context|zustand", requisitos, re.I)),
        "componentes_funcionais": bool(re.search(r"funcional|functional|hooks?", requisitos, re.I)),
        "performance": bool(re.search(r"performance|otimiza|memo|lazy", requisitos, re.I)),
        "acessibilidade": bool(re.search(r"acessib|a11y|aria|wcag", requisitos, re.I)),
        "responsividade": bool(re.search(r"responsiv|mobile|breakpoint", requisitos, re.I)),
        "testes": bool(re.search(r"test|jest|testing.library", requisitos, re.I)),
        "estrutura_pastas": bool(re.search(r"estrutura|folder|organiza|arquitetura", requisitos, re.I)),
        "codigo_limpo": bool(re.search(r"clean|limpo|eslint|prettier", requisitos, re.I)),
        "tratamento_erros": bool(re.search(r"erro|error|exception|boundary", requisitos, re.I))
    }

    requisitos_faltantes = [
        req.replace('_', ' ').title()
        for req, presente in checklist.items()
        if not presente
    ]

    validacao_completa = all(checklist.values())
    percentual_cobertura = (sum(checklist.values()) / len(checklist)) * 100

    recomendacoes = []
    if not checklist["tipagem_typescript"]:
        recomendacoes.append(
            "Adicione requisitos explícitos sobre uso de TypeScript com tipos bem definidos")
    if not checklist["acessibilidade"]:
        recomendacoes.append(
            "Inclua requisitos de acessibilidade seguindo padrões WCAG")
    if not checklist["performance"]:
        recomendacoes.append(
            "Especifique requisitos de performance e otimização")

    return {
        "validacao_completa": validacao_completa,
        "percentual_cobertura": percentual_cobertura,
        "checklist": checklist,
        "requisitos_faltantes": requisitos_faltantes,
        "recomendacoes": recomendacoes
    }


@mcp.tool()
async def gerar_prompt_otimizado(
    descricao_projeto: str,
    tipo_projeto: str = "componente",
    nivel_detalhe: str = "completo"
) -> str:
    """
    Gera um prompt otimizado completo baseado na descrição do projeto

    Args:
        descricao_projeto: Descrição básica do que precisa ser desenvolvido
        tipo_projeto: Tipo do projeto ('componente', 'aplicacao', 'biblioteca')
        nivel_detalhe: Nível de detalhe desejado ('basico', 'intermediario', 'completo')

    Returns:
        Prompt otimizado e estruturado
    """
    # Base do prompt
    prompt = f"Desenvolva {descricao_projeto} usando React com TypeScript.\n\n"

    # Adicionar seções baseadas no nível de detalhe
    if nivel_detalhe in ["intermediario", "completo"]:
        prompt += """**Arquitetura e Estrutura:**
- Componentes pequenos, focados e reutilizáveis
- Princípio da Responsabilidade Única
- Estrutura de pastas modular e escalável
- Separação clara entre lógica e apresentação

"""

    prompt += """**TypeScript e Tipagem:**
- Tipos explícitos para todas as props, estado e retornos de função
- Interfaces bem definidas para estruturas de dados
- Uso de genéricos para componentes reutilizáveis
- Strict mode habilitado

"""

    if tipo_projeto == "aplicacao":
        prompt += """**Gestão de Estado:**
- Escolha apropriada entre Context API, Zustand ou Redux Toolkit
- Estado estruturado sem redundâncias
- Separação clara entre estado local e global
- Evitar prop drilling

"""

    prompt += """**Performance e Otimização:**
- Memoização estratégica com React.memo, useMemo e useCallback
- Code splitting e lazy loading onde apropriado
- Virtualização para listas grandes
- Análise e prevenção de re-renderizações desnecessárias

"""

    if nivel_detalhe == "completo":
        prompt += """**UI/UX e Design:**
- Design responsivo mobile-first
- Sistema de design consistente
- Feedback visual para todas as interações
- Animações suaves e não intrusivas
- Modo claro/escuro se aplicável

**Acessibilidade (a11y):**
- Conformidade com WCAG nível AA
- Navegação completa por teclado
- ARIA labels apropriados
- Suporte para leitores de tela
- Contraste de cores adequado

**Qualidade de Código:**
- Convenções de nomenclatura React (PascalCase, camelCase)
- ESLint e Prettier configurados
- Princípios SOLID e DRY aplicados
- Código limpo e autoexplicativo
- Documentação JSDoc para componentes públicos

**Testes:**
- Testes unitários para componentes e hooks
- Testes de integração para fluxos principais
- Uso de React Testing Library
- Cobertura mínima de 80%

"""

    prompt += f"\n**Requisitos Específicos:**\n{descricao_projeto}"

    return prompt

# Configuração de recursos do servidor


@mcp.tool()
async def obter_recursos_servidor() -> Dict[str, Any]:
    """
    Retorna informações sobre os recursos disponíveis neste servidor MCP

    Returns:
        Dicionário com descrição dos recursos e como usá-los
    """
    return {
        "nome": "React Prompt Enhancer MCP",
        "versao": "1.0.0",
        "descricao": "Servidor MCP para aprimorar prompts de desenvolvimento React/TypeScript",
        "ferramentas_disponiveis": {
            "analisar_prompt_react": "Analisa e pontua um prompt, fornecendo sugestões de melhoria",
            "obter_template_prompt": "Fornece templates otimizados para diferentes tipos de projeto",
            "sugerir_melhorias_contextuais": "Sugere melhorias específicas baseadas no contexto",
            "validar_requisitos_react": "Valida se os requisitos cobrem aspectos essenciais",
            "gerar_prompt_otimizado": "Gera um prompt completo e otimizado a partir de uma descrição"
        },
        "melhores_praticas_cobertas": list(MELHORES_PRATICAS.keys()),
        "exemplo_uso": {
            "1_analise": "Use 'analisar_prompt_react' para avaliar seu prompt atual",
            "2_melhoria": "Aplique as sugestões fornecidas",
            "3_validacao": "Use 'validar_requisitos_react' para garantir cobertura completa",
            "4_otimizacao": "Use 'gerar_prompt_otimizado' para criar prompts estruturados"
        }
    }

if __name__ == "__main__":
    mcp.run()
