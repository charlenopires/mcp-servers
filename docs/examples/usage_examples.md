# 🚀 Exemplos de Uso dos Servidores MCP

Este documento apresenta uma visão geral dos exemplos práticos para cada servidor MCP no projeto MCP Servers v2.0.

## 📖 Índice de Exemplos

### 📚 Documentação Detalhada por Servidor

1. **[Servidor de Análise MCP](./mcp_server_examples.md)** - Análise completa de prompts e estruturas
2. **[Servidor de Engenharia de Prompts](./prompt_server_examples.md)** - Otimização avançada de prompts
3. **[Servidor Tailwind CSS v4.1](./tailwind_server_examples.md)** - Desenvolvimento frontend moderno
4. **[FastMCP Server](./fastmcp_server_examples.md)** - Criação de servidores MCP especializados

### 🔄 Workflows Integrados

5. **[Exemplos de Integração Completa](./integrated_workflows.md)** - Workflows usando múltiplos servidores

### 📋 Visão Geral Rápida

6. [Exemplos Básicos](#exemplos-básicos) - Introdução rápida a cada servidor
7. [Casos de Uso Comuns](#casos-de-uso-comuns) - Cenários práticos do dia a dia
8. [Configuração Claude Desktop](#configuração-claude-desktop) - Setup para uso com IA

---

## 🔍 Servidor de Análise MCP

### Cenário: Análise de Prompt para Servidor de E-commerce

```python
from servers.mcp_server import AnalisadorPromptMCP

# Inicializar o analisador
analisador = AnalisadorPromptMCP()

# Prompt de exemplo para análise
prompt_ecommerce = """
Criar um servidor MCP para gestão de e-commerce que deve:
- Gerenciar produtos (CRUD)
- Processar pedidos
- Calcular fretes
- Integrar com APIs de pagamento
- Gerar relatórios de vendas
Ferramentas necessárias: add_product, process_order, calculate_shipping
Recursos: products://catalog, orders://pending
"""

# Realizar análise
resultado = analisador.analisar_prompt(prompt_ecommerce)

print(f"📊 Pontuação: {resultado.pontuacao}/10")
print(f"✅ Pontos Fortes: {', '.join(resultado.pontos_fortes)}")
print(f"⚠️  Pontos Fracos: {', '.join(resultado.pontos_fracos)}")
print(f"💡 Recomendações: {', '.join(resultado.recomendacoes)}")
```

**Saída Esperada:**

```
📊 Pontuação: 8/10
✅ Pontos Fortes: Objetivo claro, Ferramentas especificadas, Recursos definidos
⚠️  Pontos Fracos: Falta especificação de tipos de dados
💡 Recomendações: Adicione tipos de entrada/saída, Inclua tratamento de erros
```

### Cenário: Validação de Requisitos MCP

```python
# Definir requisitos para validação
requisitos = {
    "ferramentas": ["get_weather", "set_alert"],
    "recursos": ["weather://current", "alerts://active"],
    "tipos_entrada": {"location": "str", "alert_type": "str"},
    "tipos_saida": {"temperature": "float", "condition": "str"},
    "tratamento_erros": True,
    "testes": True
}

# Validar requisitos
validacao = analisador.validar_requisitos_mcp(requisitos)

if validacao.aprovado:
    print("✅ Requisitos aprovados!")
    print(f"📋 Itens verificados: {', '.join(validacao.itens_verificados)}")
else:
    print("❌ Requisitos precisam de melhorias")
    print(f"⚠️  Itens faltantes: {', '.join(validacao.itens_faltantes)}")
```

---

## 📝 Servidor de Engenharia de Prompts

### Cenário: Otimização de Prompt para IA de Atendimento

```python
from servers.prompt_server import ServidorPrompts

servidor = ServidorPrompts()

# Prompt original que precisa de otimização
prompt_original = """
Você é um assistente de atendimento. Responda as perguntas dos clientes.
"""

# Otimizar para atendimento ao cliente
prompt_otimizado = servidor.otimizar_prompt(
    prompt_original,
    objetivo="atendimento_cliente",
    contexto="loja online de eletrônicos"
)

print("🔄 ANTES:")
print(prompt_original)
print("\n✨ DEPOIS:")
print(prompt_otimizado)
```

**Saída Esperada:**

```
🔄 ANTES:
Você é um assistente de atendimento. Responda as perguntas dos clientes.

✨ DEPOIS:
Você é um assistente especializado em atendimento ao cliente para uma loja online de eletrônicos.

CONTEXTO:
- Loja: Eletrônicos online
- Produtos: Smartphones, laptops, tablets, acessórios
- Política: Garantia 12 meses, troca em 30 dias

INSTRUÇÕES:
1. Seja cordial e profissional
2. Forneça informações precisas sobre produtos
3. Ajude com dúvidas sobre pedidos e entregas
4. Escale problemas complexos quando necessário

FORMATO DE RESPOSTA:
- Cumprimento personalizado
- Resposta clara e objetiva
- Oferecimento de ajuda adicional
```

### Cenário: Aplicação de Estratégias de Prompt

```python
# Aplicar estratégia Chain-of-Thought para resolução de problemas
estrategia_cot = servidor.aplicar_estrategia_prompt(
    prompt="Calcule o total de uma compra com desconto",
    estrategia="chain_of_thought",
    parametros={
        "passos": ["identificar valores", "aplicar desconto", "calcular total"],
        "exemplos": True
    }
)

print("🧠 Prompt com Chain-of-Thought:")
print(estrategia_cot)
```

---

## 🎨 Servidor Tailwind CSS

### Cenário: Migração de Projeto para v4.1

```python
from servers.tailwind_server import ServidorTailwind

servidor_tw = ServidorTailwind()

# Código CSS antigo que precisa ser convertido
codigo_antigo = """
<div class="bg-blue-500 text-white p-4 rounded-lg shadow-md">
  <h1 class="text-2xl font-bold mb-2">Título</h1>
  <p class="text-sm opacity-75">Descrição do componente</p>
</div>
"""

# Converter para Tailwind v4.1
codigo_convertido = servidor_tw.converter_codigo_tailwind(
    codigo_antigo,
    versao_origem="3.4",
    versao_destino="4.1"
)

print("🔄 Código Original (v3.4):")
print(codigo_antigo)
print("\n✨ Código Convertido (v4.1):")
print(codigo_convertido)
```

### Cenário: Geração de Componente Otimizado

```python
# Gerar componente de card seguindo boas práticas v4.1
card_component = servidor_tw.gerar_componentes_tailwind(
    tipo="card",
    especificacoes={
        "estilo": "moderno",
        "responsivo": True,
        "dark_mode": True,
        "animacoes": True
    }
)

print("🎯 Componente Card Otimizado:")
print(card_component)
```

**Saída Esperada:**

```html
<!-- Card Component - Tailwind CSS v4.1 -->
<div class="card group">
  <div class="card-header">
    <h3 class="card-title">Título do Card</h3>
  </div>
  <div class="card-body">
    <p class="card-text">
      Conteúdo do card com suporte completo a dark mode e responsividade.
    </p>
  </div>
  <div class="card-footer">
    <button class="btn btn-primary">Ação</button>
  </div>
</div>

<style>
  @layer components {
    .card {
      @apply bg-white dark:bg-gray-800 rounded-xl shadow-sm hover:shadow-lg transition-shadow duration-300;
      @apply border border-gray-200 dark:border-gray-700;
    }

    .card-header {
      @apply p-6 pb-3;
    }

    .card-title {
      @apply text-xl font-semibold text-gray-900 dark:text-white;
    }

    .card-body {
      @apply px-6 pb-3;
    }

    .card-text {
      @apply text-gray-600 dark:text-gray-300 leading-relaxed;
    }

    .card-footer {
      @apply p-6 pt-3 flex justify-end;
    }
  }
</style>
```

---

## ⚡ FastMCP Server

### Cenário: Análise Completa de Prompt

```python
import asyncio
from servers.fastmcp_server import analyze_mcp_prompt

async def exemplo_analise_avancada():
    # Simular contexto FastMCP
    class MockContext:
        async def info(self, message): print(f"ℹ️  {message}")

    ctx = MockContext()

    # Prompt complexo para análise
    prompt_complexo = """
    Criar servidor MCP para análise de sentimentos em redes sociais

    Funcionalidades:
    - Coletar posts do Twitter/X, Instagram, Facebook
    - Analisar sentimento (positivo, negativo, neutro)
    - Gerar relatórios visuais
    - Detectar tendências em tempo real
    - API para integração externa

    Ferramentas necessárias:
    - collect_social_posts(platform, keywords, limit)
    - analyze_sentiment(text) -> SentimentResult
    - generate_report(data, format) -> Report
    - detect_trends(timeframe) -> TrendAnalysis

    Recursos:
    - social://posts/{platform}
    - analytics://sentiment/{id}
    - reports://generated/{date}

    Tipos de dados:
    - Input: strings, arrays, timestamps
    - Output: JSON estruturado, relatórios PDF/HTML

    Tratamento de erros:
    - Rate limiting das APIs
    - Validação de entrada
    - Fallbacks para indisponibilidade

    Testes incluídos:
    - Testes unitários por ferramenta
    - Testes de integração com APIs
    - Testes de performance
    """

    # Realizar análise
    resultado = await analyze_mcp_prompt(prompt_complexo, ctx)

    print(f"\n📊 RESULTADO DA ANÁLISE")
    print(f"🎯 Pontuação: {resultado.score:.1f}/100")
    print(f"✅ Pontos Fortes: {', '.join(resultado.strengths)}")
    print(f"⚠️  Pontos Fracos: {', '.join(resultado.weaknesses)}")
    print(f"💡 Recomendações: {', '.join(resultado.recommendations)}")
    print(f"📋 Frameworks Aplicados: {', '.join(resultado.frameworks)}")

# Executar exemplo
asyncio.run(exemplo_analise_avancada())
```

### Cenário: Geração de Template de Servidor

```python
async def exemplo_geracao_template():
    from servers.fastmcp_server import generate_mcp_server_template

    ctx = MockContext()

    # Gerar template para servidor de produção
    template = await generate_mcp_server_template(
        name="ProductionAPIServer",
        server_type="production_ready",
        ctx=ctx
    )

    print("🏗️  TEMPLATE GERADO:")
    print("=" * 50)
    print(template[:1000] + "...")  # Primeiros 1000 caracteres

asyncio.run(exemplo_geracao_template())
```

---

## 🔗 Exemplos de Integração

### Cenário: Pipeline Completo de Desenvolvimento

```python
async def pipeline_desenvolvimento_mcp():
    """
    Exemplo de pipeline completo usando múltiplos servidores MCP
    """

    # 1. ANÁLISE INICIAL - MCP Server
    from servers.mcp_server import AnalisadorPromptMCP

    analisador = AnalisadorPromptMCP()
    prompt_inicial = "Criar servidor MCP para gestão de inventário"

    analise_inicial = analisador.analisar_prompt(prompt_inicial)
    print(f"1️⃣  Análise Inicial: {analise_inicial.pontuacao}/10")

    # 2. OTIMIZAÇÃO - Prompt Server
    from servers.prompt_server import ServidorPrompts

    servidor_prompts = ServidorPrompts()
    prompt_otimizado = servidor_prompts.otimizar_prompt(
        prompt_inicial,
        objetivo="servidor_mcp",
        contexto="gestão de inventário empresarial"
    )
    print("2️⃣  Prompt Otimizado ✓")

    # 3. ANÁLISE AVANÇADA - FastMCP Server
    from servers.fastmcp_server import analyze_mcp_prompt

    class MockContext:
        async def info(self, msg): pass

    analise_avancada = await analyze_mcp_prompt(prompt_otimizado, MockContext())
    print(f"3️⃣  Análise Avançada: {analise_avancada.score:.1f}/100")

    # 4. GERAÇÃO DE TEMPLATE
    from servers.fastmcp_server import generate_mcp_server_template

    template = await generate_mcp_server_template(
        name="InventoryMCPServer",
        server_type="api_integration",
        ctx=MockContext()
    )
    print("4️⃣  Template Gerado ✓")

    # 5. RESULTADO FINAL
    print("\n🎉 PIPELINE CONCLUÍDO!")
    print(f"📈 Melhoria de qualidade: {analise_inicial.pontuacao} → {analise_avancada.score:.1f}")

    return {
        "prompt_final": prompt_otimizado,
        "analise": analise_avancada,
        "template": template[:500] + "..."
    }

# Executar pipeline
resultado_pipeline = asyncio.run(pipeline_desenvolvimento_mcp())
print("\n📋 Resumo do Pipeline:")
for chave, valor in resultado_pipeline.items():
    print(f"{chave}: {valor}")
```

### Cenário: Integração com Claude/ChatGPT

```python
def integrar_com_claude():
    """
    Exemplo de como integrar os servidores MCP com Claude
    """

    # Configuração para Claude Desktop
    config_claude = {
        "mcpServers": {
            "mcp-analysis": {
                "command": "python",
                "args": ["/path/to/mcp-servers/main.py", "mcp"],
                "env": {
                    "PATH": "/usr/local/bin:/usr/bin:/bin"
                }
            },
            "prompt-engineering": {
                "command": "python",
                "args": ["/path/to/mcp-servers/main.py", "prompt"],
                "env": {
                    "PATH": "/usr/local/bin:/usr/bin:/bin"
                }
            },
            "fastmcp-analysis": {
                "command": "python",
                "args": ["/path/to/mcp-servers/main.py", "fastmcp"],
                "env": {
                    "PATH": "/usr/local/bin:/usr/bin:/bin"
                }
            }
        }
    }

    print("🔧 Configuração para Claude Desktop:")
    import json
    print(json.dumps(config_claude, indent=2))

    # Comandos de exemplo para usar no Claude
    exemplos_claude = [
        "Analise este prompt MCP: 'Criar servidor para processamento de imagens'",
        "Otimize este prompt para um servidor de chat bot",
        "Gere um template de servidor MCP para análise de dados",
        "Valide os requisitos deste servidor MCP"
    ]

    print("\n💬 Exemplos de comandos para Claude:")
    for i, exemplo in enumerate(exemplos_claude, 1):
        print(f"{i}. {exemplo}")

integrar_com_claude()
```

---

## 🎯 Casos de Uso Específicos

### E-commerce

```python
# Análise de prompt para loja online
prompt_ecommerce = """
Criar servidor MCP para e-commerce com:
- Catálogo de produtos
- Carrinho de compras
- Processamento de pagamentos
- Gestão de estoque
- Sistema de avaliações
"""
```

### Análise de Dados

```python
# Template para servidor de data science
prompt_datascience = """
Servidor MCP para análise de dados:
- Importação de datasets (CSV, JSON, Excel)
- Limpeza e transformação de dados
- Análise estatística
- Visualizações interativas
- Modelos de machine learning
"""
```

### Automação

```python
# Servidor para automação de processos
prompt_automacao = """
Servidor MCP para automação:
- Integração com APIs externas
- Workflows configuráveis
- Notificações automáticas
- Monitoramento de sistemas
- Relatórios agendados
"""
```

---

## 🚀 Execução dos Exemplos

Para executar estes exemplos:

```bash
# Executar servidor específico
python main.py mcp
python main.py prompt
python main.py tailwind
python main.py fastmcp

# Executar todos os servidores
python main.py all

# Executar testes
python run_tests.py

# Modo interativo
./run_servers.sh
```

## 📚 Próximos Passos

1. **Personalize** os exemplos para seus casos específicos
2. **Teste** diferentes combinações de servidores
3. **Explore** as funcionalidades avançadas
4. **Integre** com suas ferramentas favoritas
5. **Contribua** com novos exemplos!

---

_Documentação atualizada em: 25 de maio de 2025_
