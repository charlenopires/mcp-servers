# Tailwind CSS v4.1 Server - Exemplos Detalhados

## 📋 Visão Geral

O Tailwind CSS Server fornece contextualização e assistência para desenvolvimento com Tailwind CSS v4.1, incluindo as mais recentes funcionalidades, mudanças de configuração e otimizações de performance. Este documento apresenta exemplos práticos para todas as funcionalidades.

## 🎯 Funcionalidades Principais

- **Contextualização v4.1**: Informações atualizadas sobre mudanças e novas funcionalidades
- **Migração Assistida**: Guias para migrar de versões anteriores
- **Geração de Código**: Templates otimizados com as novas features
- **Análise de Performance**: Otimizações específicas da v4.1
- **Componentes Modernos**: Exemplos usando as novas utilities

## 🚀 Configuração Básica v4.1

### 1. Setup Inicial Completo

```python
from servers.tailwind_server import TailwindContextualizer

# Inicializar o contextualizador
tailwind = TailwindContextualizer()

# Obter configuração básica para um novo projeto
config = tailwind.gerar_configuracao_basica(
    tipo_projeto="next-js",
    plugins=["@tailwindcss/forms", "@tailwindcss/typography"],
    tema_customizado=True
)

print("=== CONFIGURAÇÃO TAILWIND CSS V4.1 ===")
print(config['css_config'])
```

**Resultado Esperado:**

```css
/* styles/globals.css - Configuração Tailwind CSS v4.1 */
@import "tailwindcss";

/* Configuração de escaneamento de arquivos */
@source "./src/**/*.{js,jsx,ts,tsx}";
@source "./components/**/*.{js,jsx,ts,tsx}";
@source "./pages/**/*.{js,jsx,ts,tsx}";
@source "./app/**/*.{js,jsx,ts,tsx}";
@source not "./node_modules/**/*";

/* Tema customizado inline */
@theme inline {
  /* Cores principais */
  --color-primary: #3b82f6;
  --color-secondary: #64748b;
  --color-accent: #f59e0b;
  --color-success: #10b981;
  --color-warning: #f59e0b;
  --color-error: #ef4444;

  /* Espaçamentos customizados */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;

  /* Tipografia */
  --font-family-display: "Poppins", sans-serif;
  --font-family-body: "Inter", sans-serif;

  /* Bordas e sombras */
  --border-radius-sm: 0.25rem;
  --border-radius-md: 0.5rem;
  --border-radius-lg: 0.75rem;
  --border-radius-xl: 1rem;
}

/* Plugins */
@plugin "@tailwindcss/forms";
@plugin "@tailwindcss/typography";

/* Utilitários customizados */
@utility .text-balance {
  text-wrap: balance;
}

@utility .grid-auto-fit {
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}
```

### 2. Migração de v3.x para v4.1

```python
# Análise de migração
codigo_v3 = """
// tailwind.config.js (v3.x)
module.exports = {
  content: ['./src/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#3b82f6',
        secondary: '#64748b'
      }
    }
  },
  plugins: [require('@tailwindcss/forms')]
}
"""

migracao = tailwind.analisar_migracao(codigo_v3)

print("=== ANÁLISE DE MIGRAÇÃO ===")
print(f"Compatibilidade: {migracao['compatibility_score']}%")
print(f"\nMudanças Necessárias:")
for mudanca in migracao['required_changes']:
    print(f"  • {mudanca}")

print(f"\nCódigo Migrado:")
print(migracao['migrated_code'])
```

**Resultado Esperado:**

````
=== ANÁLISE DE MIGRAÇÃO ===
Compatibilidade: 85%

Mudanças Necessárias:
  • Remover tailwind.config.js e mover configuração para CSS
  • Usar @theme inline em vez de theme.extend
  • Adicionar @source directives para escaneamento
  • Atualizar importação para @import "tailwindcss"

Código Migrado:
```css
/* Substitui tailwind.config.js */
@import "tailwindcss";

@source "./src/**/*.{js,jsx,ts,tsx}";

@theme inline {
  --color-primary: #3b82f6;
  --color-secondary: #64748b;
}

@plugin "@tailwindcss/forms";
````

## 🎨 Novas Funcionalidades v4.1

### 3. Text Shadow e Drop Shadow com Cores

```python
# Gerar exemplos de sombras avançadas
exemplos_sombras = tailwind.gerar_exemplos_sombras()

print("=== EXEMPLOS DE SOMBRAS V4.1 ===")
for categoria, exemplos in exemplos_sombras.items():
    print(f"\n{categoria.upper()}:")
    for exemplo in exemplos:
        print(f"  {exemplo}")
```

**Resultado Esperado:**

```html
=== EXEMPLOS DE SOMBRAS V4.1 === TEXT SHADOW:
<!-- Sombra básica -->
<h1 class="text-4xl font-bold text-shadow-lg">Título Principal</h1>

<!-- Sombra colorida -->
<h2 class="text-2xl text-shadow-md text-shadow-blue-500/30">
  Subtítulo com Sombra Azul
</h2>

<!-- Sombra responsiva -->
<h3 class="text-xl text-shadow-sm md:text-shadow-lg lg:text-shadow-xl">
  Sombra Responsiva
</h3>

<!-- Combinação com gradientes -->
<div
  class="bg-gradient-to-r from-purple-500 to-pink-500 text-white text-shadow-xl"
>
  Texto com Gradiente e Sombra
</div>

DROP SHADOW COLOR:
<!-- Drop shadow com cor específica -->
<div class="drop-shadow-lg drop-shadow-red-500/25 bg-white p-6 rounded-lg">
  Card com Sombra Vermelha
</div>

<!-- Sombra animada -->
<button
  class="drop-shadow-md drop-shadow-blue-500/20 hover:drop-shadow-xl hover:drop-shadow-blue-500/40 transition-all"
>
  Botão com Hover Effect
</button>
```

### 4. Mask Utilities Avançadas

```python
# Exemplos de máscaras CSS
exemplos_mask = tailwind.gerar_exemplos_mask()

print("=== MASK UTILITIES V4.1 ===")
for exemplo in exemplos_mask:
    print(exemplo)
```

**Resultado Esperado:**

```html
=== MASK UTILITIES V4.1 ===

<!-- Gradiente de fade -->
<div class="mask-image-gradient-to-b mask-from-black mask-to-transparent">
  <img src="hero.jpg" alt="Hero" class="w-full h-96 object-cover" />
</div>

<!-- Máscara de fade bottom -->
<div class="relative">
  <div
    class="mask-b-from-50% absolute inset-0 bg-gradient-to-t from-black/80"
  ></div>
  <img src="background.jpg" alt="Background" />
  <div class="absolute bottom-4 left-4 text-white">
    <h2>Título sobre imagem</h2>
  </div>
</div>

<!-- Máscara top com fade -->
<section
  class="mask-t-to-80% bg-cover bg-center"
  style="background-image: url('header-bg.jpg')"
>
  <div class="py-20 px-4">
    <h1 class="text-white text-center">Hero Section</h1>
  </div>
</section>

<!-- Máscara circular responsiva -->
<div
  class="mask-image-radial-gradient mask-from-black mask-to-transparent mask-at-center"
>
  <div class="grid grid-cols-3 gap-4 p-8">
    <!-- Conteúdo que fade nas bordas -->
  </div>
</div>
```

### 5. Novas Variantes de Estado

```python
# Exemplos das novas variantes
exemplos_variantes = tailwind.gerar_exemplos_variantes()

print("=== NOVAS VARIANTES V4.1 ===")
for variante, codigo in exemplos_variantes.items():
    print(f"\n{variante.upper()}:")
    print(codigo)
```

**Resultado Esperado:**

```html
=== NOVAS VARIANTES V4.1 === USER-VALID / USER-INVALID:
<!-- Validação apenas após interação do usuário -->
<form class="space-y-4">
  <input
    type="email"
    required
    class="w-full px-3 py-2 border border-gray-300 rounded-md
           user-invalid:border-red-500 user-invalid:ring-red-500
           user-valid:border-green-500 user-valid:ring-green-500
           focus:ring-2 focus:outline-none"
    placeholder="Digite seu email"
  />

  <input
    type="password"
    minlength="8"
    class="w-full px-3 py-2 border border-gray-300 rounded-md
           user-invalid:border-red-500 user-invalid:bg-red-50
           user-valid:border-green-500 user-valid:bg-green-50"
    placeholder="Senha (mín. 8 caracteres)"
  />
</form>

NOSCRIPT:
<!-- Estilos quando JavaScript está desabilitado -->
<div
  class="hidden noscript:block bg-yellow-100 border border-yellow-400 text-yellow-700 px-4 py-3 rounded"
>
  <p>Este site funciona melhor com JavaScript habilitado.</p>
</div>

<nav class="noscript:hidden">
  <!-- Menu interativo que só funciona com JS -->
</nav>

<nav class="hidden noscript:block">
  <!-- Menu alternativo estático -->
  <ul>
    <li><a href="/home">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>

INVERTED-COLORS:
<!-- Adaptação para modo de cores invertidas (acessibilidade) -->
<div
  class="bg-white text-black inverted-colors:bg-black inverted-colors:text-white"
>
  <p>Conteúdo que se adapta a cores invertidas</p>
</div>

DETAILS-CONTENT:
<!-- Estilização específica para conteúdo de <details> -->
<details class="border border-gray-300 rounded-lg">
  <summary class="px-4 py-2 cursor-pointer hover:bg-gray-50">
    Clique para expandir
  </summary>
  <div
    class="details-content:px-4 details-content:py-3 details-content:border-t details-content:bg-gray-50"
  >
    <p>Este conteúdo só é estilizado quando dentro de details expandido</p>
  </div>
</details>
```

## 🏗️ Componentes Modernos com v4.1

### 6. Card de Produto Avançado

```python
# Gerar componente de card moderno
card_produto = tailwind.gerar_componente_card_produto()

print("=== CARD DE PRODUTO V4.1 ===")
print(card_produto['jsx_code'])
print(f"\nFuncionalidades v4.1 utilizadas:")
for feature in card_produto['v4_features']:
    print(f"  • {feature}")
```

**Resultado Esperado:**

```jsx
=== CARD DE PRODUTO V4.1 ===

export default function ProductCard({ product }) {
  return (
    <div className="group relative overflow-hidden rounded-xl bg-white shadow-md
                    drop-shadow-lg drop-shadow-gray-200/25
                    hover:drop-shadow-xl hover:drop-shadow-gray-300/30
                    transition-all duration-300">

      {/* Badge com nova text-shadow */}
      <div className="absolute right-3 top-3 z-10">
        <span className="rounded-full bg-gradient-to-r from-blue-500 to-purple-600
                         px-3 py-1 text-xs font-medium text-white
                         text-shadow-sm text-shadow-black/50">
          {product.category}
        </span>
      </div>

      {/* Container de imagem com mask */}
      <div className="relative aspect-square overflow-hidden">
        <div className="absolute inset-0 mask-b-from-90% bg-gradient-to-t from-black/20 to-transparent z-10"></div>
        <img
          src={product.image}
          alt={product.name}
          className="h-full w-full object-cover transition duration-500
                     group-hover:scale-110 group-hover:rotate-1"
        />
      </div>

      {/* Conteúdo com novas utilities */}
      <div className="p-6 space-y-4">
        <h3 className="text-lg font-semibold text-gray-900 text-balance">
          {product.name}
        </h3>

        <p className="text-sm text-gray-600 line-clamp-2">
          {product.description}
        </p>

        {/* Rating com validação user-valid */}
        <div className="flex items-center gap-2">
          <div className="flex text-yellow-400">
            {'★'.repeat(product.rating)}{'☆'.repeat(5-product.rating)}
          </div>
          <span className="text-sm text-gray-500">({product.reviews})</span>
        </div>

        {/* Preço e botão */}
        <div className="flex items-center justify-between pt-2">
          <div className="flex items-baseline gap-2">
            <span className="text-2xl font-bold text-gray-900">
              ${product.price}
            </span>
            {product.originalPrice && (
              <span className="text-sm text-gray-500 line-through">
                ${product.originalPrice}
              </span>
            )}
          </div>

          <button className="rounded-lg bg-gradient-to-r from-blue-600 to-purple-600
                           px-4 py-2 text-sm font-medium text-white
                           text-shadow-sm text-shadow-black/25
                           hover:from-blue-700 hover:to-purple-700
                           focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2
                           transition-all duration-200">
            Add to Cart
          </button>
        </div>
      </div>
    </div>
  );
}

Funcionalidades v4.1 utilizadas:
  • drop-shadow-color para sombras coloridas personalizadas
  • text-shadow com cores e opacidade
  • mask utilities para efeitos de gradiente
  • text-balance para melhor quebra de linha
  • Variantes de estado aprimoradas
```

### 7. Dashboard Layout Responsivo

```python
# Gerar layout de dashboard moderno
dashboard = tailwind.gerar_dashboard_layout()

print("=== DASHBOARD RESPONSIVO V4.1 ===")
print(dashboard['html_code'])
```

**Resultado Esperado:**

```html
=== DASHBOARD RESPONSIVO V4.1 ===

<div class="min-h-screen bg-gray-50">
  <!-- Sidebar -->
  <aside
    class="fixed inset-y-0 left-0 z-50 w-64 bg-white 
               drop-shadow-lg drop-shadow-gray-200/25
               transform -translate-x-full lg:translate-x-0 transition-transform"
  >
    <!-- Logo com text-shadow -->
    <div class="flex h-16 items-center justify-center border-b border-gray-200">
      <h1 class="text-xl font-bold text-gray-900 text-shadow-sm">Dashboard</h1>
    </div>

    <!-- Navigation com novas variantes -->
    <nav class="mt-8 space-y-1 px-4">
      <a
        href="#"
        class="group flex items-center px-3 py-2 rounded-lg
                         text-gray-700 hover:bg-blue-50 hover:text-blue-700
                         user-valid:bg-blue-100"
      >
        <svg class="mr-3 h-5 w-5">...</svg>
        Overview
      </a>
      <!-- Mais items de navegação -->
    </nav>
  </aside>

  <!-- Main Content -->
  <main class="lg:ml-64">
    <!-- Header -->
    <header
      class="bg-white drop-shadow-sm drop-shadow-gray-100/50 border-b border-gray-200"
    >
      <div class="flex h-16 items-center justify-between px-6">
        <h2 class="text-lg font-semibold text-gray-900">Analytics Overview</h2>

        <!-- User menu com mask effect -->
        <div class="relative">
          <button
            class="flex items-center space-x-3 rounded-full p-1
                         hover:drop-shadow-md hover:drop-shadow-blue-200/30"
          >
            <div
              class="h-8 w-8 rounded-full bg-gradient-to-br from-blue-500 to-purple-600
                        mask-image-radial-gradient"
            ></div>
          </button>
        </div>
      </div>
    </header>

    <!-- Content Grid -->
    <div class="p-6">
      <div class="grid-auto-fit gap-6 mb-8">
        <!-- Stat Cards -->
        <div
          class="bg-white rounded-xl p-6 
                    drop-shadow-md drop-shadow-blue-100/20
                    hover:drop-shadow-lg hover:drop-shadow-blue-200/30
                    transition-all"
        >
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm text-gray-600">Total Revenue</p>
              <p class="text-3xl font-bold text-gray-900">$45,231</p>
            </div>
            <div class="rounded-full bg-green-100 p-3">
              <svg class="h-6 w-6 text-green-600">...</svg>
            </div>
          </div>
        </div>

        <!-- Mais cards estatísticos -->
      </div>

      <!-- Charts Section -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div
          class="bg-white rounded-xl p-6 
                    drop-shadow-lg drop-shadow-gray-200/25"
        >
          <h3 class="text-lg font-semibold text-gray-900 mb-4">
            Revenue Trend
          </h3>
          <!-- Chart placeholder com mask para fade -->
          <div
            class="h-64 bg-gradient-to-t from-blue-50 to-white rounded-lg
                      mask-t-to-90% flex items-center justify-center"
          >
            <p class="text-gray-500">Chart Component</p>
          </div>
        </div>

        <div
          class="bg-white rounded-xl p-6 
                    drop-shadow-lg drop-shadow-gray-200/25"
        >
          <h3 class="text-lg font-semibold text-gray-900 mb-4">
            User Activity
          </h3>
          <div
            class="h-64 bg-gradient-to-b from-purple-50 to-white rounded-lg
                      mask-b-from-80% flex items-center justify-center"
          >
            <p class="text-gray-500">Activity Chart</p>
          </div>
        </div>
      </div>
    </div>
  </main>
</div>
```

## 🚀 Otimizações de Performance v4.1

### 8. Análise de Performance

```python
# Analisar performance do build
performance = tailwind.analisar_performance_build(
    projeto_path="./src",
    config_type="v4.1"
)

print("=== ANÁLISE DE PERFORMANCE V4.1 ===")
print(f"Tempo de build: {performance['build_time']}ms")
print(f"Tamanho do CSS: {performance['css_size']}KB")
print(f"Classes detectadas: {performance['classes_found']}")
print(f"Performance vs v3.x: {performance['improvement']}x mais rápido")

print(f"\nOtimizações aplicadas:")
for otimizacao in performance['optimizations']:
    print(f"  • {otimizacao}")
```

**Resultado Esperado:**

```
=== ANÁLISE DE PERFORMANCE V4.1 ===
Tempo de build: 127ms
Tamanho do CSS: 45.2KB
Classes detectadas: 1,247
Performance vs v3.x: 4.2x mais rápido

Otimizações aplicadas:
  • Escaneamento incremental de arquivos
  • Cache de classes detectadas
  • Compilação Just-in-Time aprimorada
  • Remoção automática de CSS não utilizado
  • Compressão avançada de classes
```

### 9. Configuração de Produção Otimizada

```python
# Gerar configuração otimizada para produção
config_prod = tailwind.gerar_config_producao()

print("=== CONFIGURAÇÃO DE PRODUÇÃO ===")
print(config_prod['css_config'])
```

**Resultado Esperado:**

```css
=== CONFIGURAÇÃO DE PRODUÇÃO ===

/* Configuração de produção Tailwind CSS v4.1 */
@import "tailwindcss";

/* Escaneamento otimizado para produção */
@source "./dist/**/*.{js,jsx,ts,tsx}";
@source "./build/**/*.{js,jsx,ts,tsx}";
@source not "./node_modules/**/*";
@source not "./src/**/*";  /* Exclui arquivos fonte em produção */

/* Tema minificado */
@theme inline {
  --color-primary: #3b82f6;
  --color-secondary: #64748b;
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;
}

/* Apenas plugins essenciais */
@plugin "@tailwindcss/forms";

/* Utilitários críticos apenas */
@utility .text-balance {
  text-wrap: balance;
}

/* Configurações de purge avançadas */
@source inline "
  /* Classes críticas que devem sempre estar presentes */
  btn primary secondary
  text-primary bg-primary
  grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3
";
```

## 🔧 Casos de Uso Avançados

### 10. Migração Automatizada

```python
def migrar_projeto_completo(pasta_projeto):
    """Migração completa de um projeto para Tailwind CSS v4.1"""

    # 1. Análise do projeto atual
    analise = tailwind.analisar_projeto(pasta_projeto)

    # 2. Backup dos arquivos atuais
    backup_path = tailwind.criar_backup(pasta_projeto)

    # 3. Conversão da configuração
    nova_config = tailwind.converter_config_v4(analise['config_atual'])

    # 4. Atualização das classes obsoletas
    classes_atualizadas = tailwind.atualizar_classes_obsoletas(
        analise['arquivos_html_jsx']
    )

    # 5. Aplicação das novas funcionalidades
    melhorias = tailwind.aplicar_melhorias_v4(classes_atualizadas)

    return {
        'status': 'sucesso',
        'backup_path': backup_path,
        'arquivos_modificados': len(melhorias['arquivos']),
        'novas_funcionalidades': melhorias['features_aplicadas'],
        'config_nova': nova_config
    }

# Exemplo de uso
resultado = migrar_projeto_completo('./meu-projeto')
print(f"Migração concluída: {resultado['arquivos_modificados']} arquivos atualizados")
```

### 11. Geração de Tema Automática

```python
def gerar_tema_personalizado(especificacoes):
    """Gera tema Tailwind personalizado baseado em especificações"""

    tema = tailwind.gerar_tema_automatico(
        cores_primarias=especificacoes['cores'],
        tipografia=especificacoes['fontes'],
        espacamentos=especificacoes['espacos'],
        componentes=especificacoes['componentes_necessarios']
    )

    return tema

# Especificações do tema
specs = {
    'cores': {
        'primary': '#6366f1',
        'secondary': '#ec4899',
        'accent': '#f59e0b'
    },
    'fontes': {
        'display': 'Poppins',
        'body': 'Inter',
        'mono': 'JetBrains Mono'
    },
    'espacos': 'compact',  # compact, normal, generous
    'componentes_necessarios': ['cards', 'buttons', 'forms', 'navigation']
}

tema_personalizado = gerar_tema_personalizado(specs)
```

### 12. Sistema de Design Components

```python
# Gerar sistema de componentes completo
sistema_design = tailwind.gerar_sistema_componentes(
    tema='moderno',
    framework='react',
    typescript=True
)

print("=== SISTEMA DE DESIGN GERADO ===")
for componente, codigo in sistema_design.items():
    print(f"\n{componente.upper()}:")
    print(codigo[:200] + "...")  # Preview do código
```

## 📊 Métricas e Monitoramento

O Tailwind Server fornece métricas detalhadas sobre o uso e performance:

### Relatório de Uso de Classes

```python
relatorio = tailwind.gerar_relatorio_uso()

print("=== RELATÓRIO DE USO ===")
print(f"Classes únicas utilizadas: {relatorio['classes_unicas']}")
print(f"Classes mais frequentes:")
for classe, freq in relatorio['classes_frequentes']:
    print(f"  {classe}: {freq} usos")

print(f"\nFuncionalidades v4.1 em uso:")
for feature in relatorio['v4_features_em_uso']:
    print(f"  • {feature}")
```

## 🔗 Integração com Outros Servidores

### Workflow Completo com Múltiplos Servidores

```python
def workflow_desenvolvimento_completo():
    """Exemplo de workflow integrado"""

    # 1. Otimizar prompt para desenvolvimento
    from servers.prompt_server import PromptEngineer
    prompt_opt = PromptEngineer().otimizar_prompt(
        "Crie um dashboard moderno com Tailwind CSS v4.1",
        task_type="web_development"
    )

    # 2. Aplicar contexto Tailwind v4.1
    codigo_inicial = tailwind.contextualizar_prompt(prompt_opt['optimized_prompt'])

    # 3. Analisar estrutura MCP se necessário
    from servers.mcp_server import MCPAnalyzer
    if 'componente_reutilizavel' in prompt_opt['task_type']:
        analise_mcp = MCPAnalyzer().analisar_estrutura(codigo_inicial)

    # 4. Aplicar FastMCP se for servidor
    if 'servidor_mcp' in prompt_opt['task_type']:
        from servers.fastmcp_server import FastMCPAssistant
        fastmcp = FastMCPAssistant()
        codigo_final = fastmcp.otimizar_servidor_mcp(codigo_inicial)

    return codigo_final

# Uso do workflow
resultado_final = workflow_desenvolvimento_completo()
```

## 📝 Conclusão

O Tailwind CSS v4.1 Server oferece suporte completo para a mais recente versão do framework, incluindo:

- **Performance**: Builds até 5x mais rápidos
- **Novas Funcionalidades**: Text shadows, masks, variantes avançadas
- **Configuração Simplificada**: CSS-first configuration
- **Migração Assistida**: Ferramentas automáticas de atualização
- **Integração Completa**: Trabalha perfeitamente com outros servidores MCP

Este servidor é essencial para desenvolvedores que querem aproveitar ao máximo as inovações do Tailwind CSS v4.1 mantendo produtividade e qualidade de código.
