#!/usr/bin/env python3
"""
Servidor MCP para contextualização de prompts do Tailwind CSS v4.1
Ajuda a gerar código atualizado com as novas funcionalidades do Tailwind CSS
"""

from fastmcp import FastMCP
from typing import Dict, Any, List
import json

# Inicializa o servidor MCP
mcp = FastMCP("tailwind-v4-assistant")

# Base de conhecimento sobre Tailwind CSS v4.1
TAILWIND_V4_CONTEXT = {
    "version": "4.1.7",
    "release_date": "2025-05-15",
    "major_changes": {
        "configuration": {
            "location": "CSS file instead of tailwind.config.js",
            "import": '@import "tailwindcss";',
            "theme_syntax": "@theme inline { --color-primary: #007bff; }",
            "plugin_syntax": '@plugin "tailwindcss-animate";'
        },
        "new_utilities": {
            "text-shadow": ["text-shadow-xs", "text-shadow-sm", "text-shadow", "text-shadow-lg", "text-shadow-xl"],
            "mask": ["mask-b-from-50%", "mask-t-to-80%", "mask-image-gradient-to-b"],
            "drop-shadow-color": "drop-shadow-{color}-{opacity}",
            "overflow-wrap": ["wrap-break-word", "wrap-anywhere"]
        },
        "new_variants": {
            "user-valid": "Aplica estilos quando campo é válido após interação",
            "user-invalid": "Aplica estilos quando campo é inválido após interação",
            "noscript": "Aplica estilos quando JavaScript está desabilitado",
            "inverted-colors": "Aplica estilos quando cores invertidas estão ativas",
            "details-content": "Visa conteúdo de elementos <details>"
        },
        "directives": {
            "@source": "Controla escaneamento de arquivos",
            "@source not": "Exclui caminhos do escaneamento",
            "@source inline": "Funciona como safelist",
            "@utility": "Define utilitários customizados",
            "@theme": "Define variáveis de tema no CSS"
        },
        "performance": {
            "full_build": "3.5x a 5x mais rápido",
            "incremental": "8.8x mais rápido com novo CSS",
            "no_changes": "182x mais rápido sem mudanças"
        }
    }
}

# Templates de código atualizado
CODE_TEMPLATES = {
    "basic_setup": """/* Configuração básica do Tailwind CSS v4.1 */
@import "tailwindcss";

/* Definir tema customizado */
@theme inline {
  --color-primary: #007bff;
  --color-secondary: #6c757d;
  --color-background: #f8f9fa;
}

/* Configurar escaneamento de arquivos */
@source "./src/**/*.{js,jsx,ts,tsx,vue}";
@source "./components/**/*.{js,jsx,ts,tsx}";
@source not "./node_modules";

/* Adicionar plugins se necessário */
@plugin "@tailwindcss/forms";
@plugin "@tailwindcss/typography";""",
    
    "text_shadow_example": """<!-- Exemplo de sombra de texto -->
<h1 class="text-4xl font-bold text-shadow-lg text-shadow-black/50">
  Título com Sombra
</h1>

<!-- Sombra colorida -->
<h2 class="text-2xl text-shadow-sm text-shadow-blue-500/30">
  Subtítulo com Sombra Azul
</h2>""",
    
    "mask_example": """<!-- Máscara de gradiente em imagem -->
<div class="relative">
  <img src="hero.jpg" alt="Hero" class="w-full h-96 object-cover">
  <div class="absolute inset-0 mask-b-from-transparent mask-b-to-black/80"></div>
</div>""",
    
    "form_validation": """<!-- Validação de formulário com novas variantes -->
<form>
  <input 
    type="email" 
    class="border-2 border-gray-300 
           user-valid:border-green-500 
           user-invalid:border-red-500
           focus:outline-none px-4 py-2 rounded"
    placeholder="Digite seu email"
  >
  
  <!-- Mensagem para quando JS está desabilitado -->
  <div class="hidden noscript:block p-4 bg-yellow-100 text-yellow-800 mt-4">
    JavaScript é necessário para validação em tempo real
  </div>
</form>""",
    
    "responsive_text": """<!-- Texto responsivo com quebra inteligente -->
<p class="wrap-anywhere max-w-prose">
  Este texto pode conter URLs muito longas como 
  https://exemplo.com/caminho/muito/longo/que/poderia/quebrar/o/layout
  e ainda assim manterá o layout intacto.
</p>""",
    
    "custom_utility": """/* Definir utilitário customizado */
@utility flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

@utility margin-auto {
  margin: auto;
}

<!-- Uso no HTML -->
<div class="flex-center min-h-screen">
  <div class="margin-auto p-8">
    Conteúdo centralizado
  </div>
</div>"""
}

@mcp.tool()
async def contextualize_tailwind_prompt(prompt: str) -> Dict[str, Any]:
    """
    Contextualiza um prompt sobre Tailwind CSS com informações da v4.1
    
    Args:
        prompt: O prompt original do usuário
        
    Returns:
        Prompt enriquecido com contexto do Tailwind CSS v4.1
    """
    
    # Detecta menções ao Tailwind
    tailwind_keywords = ["tailwind", "tailwindcss", "tw", "utility-first"]
    is_tailwind_related = any(keyword in prompt.lower() for keyword in tailwind_keywords)
    
    if not is_tailwind_related:
        return {
            "original_prompt": prompt,
            "contextualized": False,
            "message": "Prompt não parece estar relacionado ao Tailwind CSS"
        }
    
    # Analisa o tipo de solicitação
    request_type = analyze_request_type(prompt)
    
    # Constrói o contexto apropriado
    context_parts = []
    
    # Adiciona informação sobre a versão
    context_parts.append(f"IMPORTANTE: Use Tailwind CSS v{TAILWIND_V4_CONTEXT['version']} (última versão estável).")
    
    # Adiciona contexto específico baseado no tipo de solicitação
    if "config" in request_type or "setup" in request_type:
        context_parts.append("\nCONFIGURAÇÃO ATUALIZADA:")
        context_parts.append("- A configuração agora é feita diretamente no arquivo CSS, não mais em tailwind.config.js")
        context_parts.append("- Use @theme inline para definir variáveis de tema")
        context_parts.append("- Use @source para configurar escaneamento de arquivos")
        context_parts.append(f"\nEXEMPLO:\n{CODE_TEMPLATES['basic_setup']}")
    
    if "shadow" in request_type or "text-shadow" in prompt.lower():
        context_parts.append("\nNOVAS UTILIDADES DE SOMBRA:")
        context_parts.append("- text-shadow-* agora disponível (xs, sm, base, lg, xl)")
        context_parts.append("- Suporta cores e opacidade: text-shadow-black/50")
        context_parts.append("- drop-shadow colorido: drop-shadow-blue-500/30")
        context_parts.append(f"\nEXEMPLO:\n{CODE_TEMPLATES['text_shadow_example']}")
    
    if "mask" in request_type or "gradient" in request_type:
        context_parts.append("\nNOVAS UTILIDADES DE MÁSCARA:")
        context_parts.append("- mask-* para efeitos de gradiente e transparência")
        context_parts.append("- Suporta direções: mask-b-from-*, mask-t-to-*")
        context_parts.append(f"\nEXEMPLO:\n{CODE_TEMPLATES['mask_example']}")
    
    if "form" in request_type or "validation" in request_type:
        context_parts.append("\nNOVAS VARIANTES DE VALIDAÇÃO:")
        context_parts.append("- user-valid: e user-invalid: para validação após interação")
        context_parts.append("- Evita mostrar erros antes do usuário interagir")
        context_parts.append(f"\nEXEMPLO:\n{CODE_TEMPLATES['form_validation']}")
    
    if "text" in request_type or "wrap" in request_type:
        context_parts.append("\nNOVAS UTILIDADES DE TEXTO:")
        context_parts.append("- wrap-anywhere e wrap-break-word para quebra de texto")
        context_parts.append("- Útil para URLs longas e conteúdo dinâmico")
        context_parts.append(f"\nEXEMPLO:\n{CODE_TEMPLATES['responsive_text']}")
    
    # Adiciona informações gerais importantes
    context_parts.append("\nOUTRAS MUDANÇAS IMPORTANTES:")
    context_parts.append("- Performance: builds até 5x mais rápidos")
    context_parts.append("- Novas variantes: noscript:, inverted-colors:")
    context_parts.append("- @utility para criar utilitários customizados")
    context_parts.append("- Compatibilidade melhorada com navegadores antigos")
    
    # Constrói o prompt contextualizado
    contextualized_prompt = f"{prompt}\n\n{chr(10).join(context_parts)}"
    
    return {
        "original_prompt": prompt,
        "contextualized": True,
        "contextualized_prompt": contextualized_prompt,
        "detected_features": request_type,
        "version": TAILWIND_V4_CONTEXT["version"],
        "relevant_examples": get_relevant_examples(request_type)
    }

@mcp.tool()
async def get_tailwind_v4_info(feature: str = "") -> Dict[str, Any]:
    """
    Obtém informações específicas sobre features do Tailwind CSS v4.1
    
    Args:
        feature: Feature específica para consultar (opcional)
        
    Returns:
        Informações detalhadas sobre a feature ou visão geral
    """
    
    if not feature:
        return {
            "version": TAILWIND_V4_CONTEXT["version"],
            "overview": TAILWIND_V4_CONTEXT,
            "installation": {
                "steps": [
                    "npm install tailwindcss @tailwindcss/postcss",
                    "Adicionar plugin ao postcss.config.js",
                    'Importar no CSS: @import "tailwindcss";'
                ]
            }
        }
    
    feature_lower = feature.lower()
    
    # Retorna informações específicas da feature
    feature_info = {}
    
    if "shadow" in feature_lower:
        feature_info = {
            "feature": "Text Shadows",
            "utilities": TAILWIND_V4_CONTEXT["major_changes"]["new_utilities"]["text-shadow"],
            "usage": "text-shadow-{size} text-shadow-{color}/{opacity}",
            "example": CODE_TEMPLATES["text_shadow_example"]
        }
    elif "mask" in feature_lower:
        feature_info = {
            "feature": "Masks",
            "utilities": TAILWIND_V4_CONTEXT["major_changes"]["new_utilities"]["mask"],
            "usage": "mask-{direction}-from-{value} mask-{direction}-to-{value}",
            "example": CODE_TEMPLATES["mask_example"]
        }
    elif "config" in feature_lower:
        feature_info = {
            "feature": "Configuration",
            "location": "CSS file",
            "directives": TAILWIND_V4_CONTEXT["major_changes"]["directives"],
            "example": CODE_TEMPLATES["basic_setup"]
        }
    elif "variant" in feature_lower:
        feature_info = {
            "feature": "New Variants",
            "variants": TAILWIND_V4_CONTEXT["major_changes"]["new_variants"],
            "example": CODE_TEMPLATES["form_validation"]
        }
    
    return feature_info

@mcp.tool()
async def generate_tailwind_v4_code(
    component_type: str,
    requirements: str = ""
) -> Dict[str, Any]:
    """
    Gera código Tailwind CSS v4.1 baseado no tipo de componente
    
    Args:
        component_type: Tipo de componente (card, form, hero, etc.)
        requirements: Requisitos específicos
        
    Returns:
        Código gerado com Tailwind CSS v4.1
    """
    
    code_snippets = {
        "card": f"""<!-- Card moderno com Tailwind CSS v4.1 -->
<div class="bg-white rounded-xl shadow-lg overflow-hidden group hover:shadow-xl transition-shadow">
  <!-- Imagem com máscara de gradiente -->
  <div class="relative h-48">
    <img src="produto.jpg" alt="Produto" class="w-full h-full object-cover">
    <div class="absolute inset-0 mask-b-from-transparent mask-b-to-black/60"></div>
  </div>
  
  <!-- Conteúdo -->
  <div class="p-6">
    <h3 class="text-xl font-bold text-shadow-sm text-shadow-black/20 mb-2">
      Título do Card
    </h3>
    <p class="text-gray-600 wrap-anywhere">
      {requirements or 'Descrição do card com suporte para textos longos'}
    </p>
    
    <!-- Botão com drop-shadow colorido -->
    <button class="mt-4 bg-blue-500 text-white px-6 py-2 rounded-lg 
                   drop-shadow-lg drop-shadow-blue-500/25 
                   hover:bg-blue-600 transition-colors">
      Saiba Mais
    </button>
  </div>
</div>""",
        
        "form": f"""<!-- Formulário com validação Tailwind CSS v4.1 -->
<form class="max-w-md mx-auto p-6 bg-white rounded-lg shadow-md">
  <h2 class="text-2xl font-bold mb-6 text-shadow text-shadow-gray-500/20">
    {requirements or 'Formulário de Contato'}
  </h2>
  
  <!-- Campo de email com validação -->
  <div class="mb-4">
    <label class="block text-gray-700 mb-2">Email</label>
    <input 
      type="email" 
      required
      class="w-full px-4 py-2 border-2 border-gray-200 rounded-lg
             user-valid:border-green-500 user-valid:bg-green-50
             user-invalid:border-red-500 user-invalid:bg-red-50
             focus:outline-none focus:ring-2 focus:ring-blue-500
             transition-colors"
      placeholder="seu@email.com"
    >
  </div>
  
  <!-- Campo de mensagem -->
  <div class="mb-6">
    <label class="block text-gray-700 mb-2">Mensagem</label>
    <textarea 
      rows="4"
      class="w-full px-4 py-2 border-2 border-gray-200 rounded-lg
             focus:outline-none focus:ring-2 focus:ring-blue-500
             wrap-anywhere"
      placeholder="Digite sua mensagem..."
    ></textarea>
  </div>
  
  <!-- Aviso noscript -->
  <div class="hidden noscript:block p-3 bg-amber-100 text-amber-800 rounded mb-4">
    JavaScript desabilitado: validação básica apenas
  </div>
  
  <!-- Botão submit -->
  <button 
    type="submit"
    class="w-full bg-gradient-to-r from-blue-500 to-blue-600 
           text-white font-semibold py-3 rounded-lg
           drop-shadow-lg drop-shadow-blue-500/30
           hover:from-blue-600 hover:to-blue-700
           transition-all duration-200">
    Enviar
  </button>
</form>""",
        
        "hero": f"""<!-- Hero Section com Tailwind CSS v4.1 -->
<section class="relative min-h-screen flex items-center justify-center overflow-hidden">
  <!-- Background com máscara -->
  <div class="absolute inset-0">
    <img src="hero-bg.jpg" alt="Background" class="w-full h-full object-cover">
    <div class="absolute inset-0 bg-gradient-to-b from-black/20 to-black/60"></div>
    <div class="absolute inset-0 mask-b-from-50% mask-b-to-black"></div>
  </div>
  
  <!-- Conteúdo -->
  <div class="relative z-10 text-center text-white px-6">
    <h1 class="text-5xl md:text-7xl font-bold mb-6 
               text-shadow-lg text-shadow-black/75">
      {requirements or 'Título Impactante'}
    </h1>
    <p class="text-xl md:text-2xl mb-8 max-w-3xl mx-auto
              text-shadow-sm text-shadow-black/50">
      Subtítulo com sombra sutil para melhor legibilidade
    </p>
    
    <!-- CTAs -->
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <button class="px-8 py-4 bg-white text-black font-semibold rounded-lg
                     drop-shadow-xl drop-shadow-white/20
                     hover:bg-gray-100 transition-colors">
        Começar Agora
      </button>
      <button class="px-8 py-4 border-2 border-white text-white font-semibold rounded-lg
                     hover:bg-white hover:text-black transition-colors">
        Saiba Mais
      </button>
    </div>
  </div>
</section>"""
    }
    
    # Retorna o código apropriado ou um template genérico
    if component_type.lower() in code_snippets:
        code = code_snippets[component_type.lower()]
    else:
        code = f"""<!-- Componente {component_type} com Tailwind CSS v4.1 -->
<div class="p-6 bg-white rounded-lg shadow-md">
  <h3 class="text-xl font-bold text-shadow text-shadow-gray-400/30 mb-4">
    {component_type.title()}
  </h3>
  <p class="text-gray-600 wrap-anywhere">
    {requirements or f'Conteúdo do {component_type}'}
  </p>
</div>"""
    
    return {
        "component_type": component_type,
        "code": code,
        "features_used": [
            "text-shadow",
            "mask utilities",
            "user-valid/invalid variants",
            "drop-shadow colorido",
            "wrap-anywhere"
        ],
        "version": TAILWIND_V4_CONTEXT["version"]
    }

# Funções auxiliares
def analyze_request_type(prompt: str) -> List[str]:
    """Analisa o tipo de solicitação no prompt"""
    prompt_lower = prompt.lower()
    request_types = []
    
    keyword_map = {
        "config": ["config", "configurar", "setup", "instalar", "installation"],
        "shadow": ["shadow", "sombra", "text-shadow", "drop-shadow"],
        "mask": ["mask", "máscara", "gradient", "fade", "transparência"],
        "form": ["form", "formulário", "input", "validation", "validação"],
        "text": ["text", "texto", "typography", "wrap", "quebra"],
        "variant": ["variant", "variante", "state", "estado", "hover", "focus"]
    }
    
    for request_type, keywords in keyword_map.items():
        if any(keyword in prompt_lower for keyword in keywords):
            request_types.append(request_type)
    
    return request_types

def get_relevant_examples(request_types: List[str]) -> List[str]:
    """Retorna exemplos relevantes baseados nos tipos de solicitação"""
    examples = []
    
    example_map = {
        "config": "basic_setup",
        "shadow": "text_shadow_example",
        "mask": "mask_example",
        "form": "form_validation",
        "text": "responsive_text"
    }
    
    for request_type in request_types:
        if request_type in example_map:
            example_key = example_map[request_type]
            if example_key in CODE_TEMPLATES:
                examples.append(CODE_TEMPLATES[example_key])
    
    return examples

# Configuração e execução do servidor
if __name__ == "__main__":
    # Adiciona informações sobre o servidor
    mcp.add_resource(
        "tailwind_v4_docs",
        "Documentação resumida do Tailwind CSS v4.1",
        json.dumps(TAILWIND_V4_CONTEXT, indent=2),
        "application/json"
    )
    
    mcp.add_resource(
        "tailwind_v4_examples",
        "Exemplos de código Tailwind CSS v4.1",
        json.dumps(CODE_TEMPLATES, indent=2),
        "application/json"
    )
    
    # Inicia o servidor
    print("🎨 Servidor MCP Tailwind CSS v4.1 Assistant iniciado!")
    print("📚 Ferramentas disponíveis:")
    print("  - contextualize_tailwind_prompt: Enriquece prompts com contexto v4.1")
    print("  - get_tailwind_v4_info: Obtém informações sobre features específicas")
    print("  - generate_tailwind_v4_code: Gera código com as novas funcionalidades")
    
    mcp.run()