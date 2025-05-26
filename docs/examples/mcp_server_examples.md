# 🔍 Exemplos Práticos - Servidor de Análise MCP

Exemplos detalhados de como usar o Servidor de Análise MCP para avaliar e melhorar prompts de criação de servidores MCP.

## 🎯 Casos de Uso Principais

### 1. Análise de Qualidade de Prompt

#### Exemplo: Servidor de Blog

```python
from servers.mcp_server import AnalisadorPromptMCP

# Inicializar analisador
analisador = AnalisadorPromptMCP()

# Prompt básico que precisa melhorias
prompt_blog = """
Criar um servidor MCP para blog
"""

# Analisar prompt
resultado = analisador.analisar_prompt(prompt_blog)

print(f"Pontuação: {resultado.pontuacao}/10")
# Saída: Pontuação: 2/10

print("Pontos fracos encontrados:")
for fraco in resultado.pontos_fracos:
    print(f"- {fraco}")
# Saída:
# - Prompt muito vago
# - Não especifica ferramentas
# - Falta definição de recursos
# - Sem exemplos de uso

print("Recomendações:")
for rec in resultado.recomendacoes:
    print(f"- {rec}")
# Saída:
# - Especifique as funcionalidades do blog
# - Liste as ferramentas necessárias
# - Defina os recursos que serão expostos
```

#### Exemplo: Prompt Melhorado

```python
# Versão melhorada do prompt
prompt_blog_melhorado = """
Criar servidor MCP para gestão de blog com as seguintes funcionalidades:

FERRAMENTAS:
- create_post(title, content, tags) -> Post
- edit_post(id, updates) -> Post
- delete_post(id) -> bool
- list_posts(filters) -> List[Post]
- publish_post(id) -> bool
- add_comment(post_id, content) -> Comment

RECURSOS:
- blog://posts/{id} - Acesso a posts individuais
- blog://categories - Lista de categorias
- blog://tags - Tags disponíveis
- blog://comments/{post_id} - Comentários por post

TIPOS DE DADOS:
- Post: {id, title, content, author, created_at, published}
- Comment: {id, post_id, author, content, created_at}

CASOS DE USO:
- Criação e edição de posts
- Gestão de categorias e tags
- Sistema de comentários
- Publicação e rascunhos
"""

# Nova análise
resultado_melhorado = analisador.analisar_prompt(prompt_blog_melhorado)

print(f"Nova pontuação: {resultado_melhorado.pontuacao}/10")
# Saída: Nova pontuação: 9/10

print("Melhorias identificadas:")
for forte in resultado_melhorado.pontos_fortes:
    print(f"+ {forte}")
# Saída:
# + Ferramentas bem definidas
# + Recursos claramente especificados
# + Tipos de dados estruturados
# + Casos de uso práticos
```

### 2. Validação de Requisitos MCP

#### Exemplo: Sistema de E-commerce

```python
# Definir requisitos para validação
requisitos_ecommerce = {
    "ferramentas": [
        "add_product",
        "update_inventory",
        "process_order",
        "calculate_shipping",
        "process_payment"
    ],
    "recursos": [
        "products://catalog",
        "orders://pending",
        "inventory://stock",
        "shipping://rates"
    ],
    "tipos_entrada": {
        "product_id": "str",
        "quantity": "int",
        "price": "float",
        "customer_data": "CustomerInfo"
    },
    "tipos_saida": {
        "order_id": "str",
        "total_amount": "float",
        "shipping_cost": "float",
        "estimated_delivery": "datetime"
    },
    "tratamento_erros": True,
    "testes": True,
    "documentacao": True
}

# Validar requisitos
validacao = analisador.validar_requisitos_mcp(requisitos_ecommerce)

if validacao.aprovado:
    print("✅ Requisitos aprovados para produção!")
    print(f"Pontuação: {validacao.pontuacao}/10")
    print("Itens verificados:")
    for item in validacao.itens_verificados:
        print(f"  ✓ {item}")
else:
    print("❌ Requisitos precisam de melhorias")
    print("Itens faltantes:")
    for item in validacao.itens_faltantes:
        print(f"  ✗ {item}")
```

### 3. Melhoria de Prompts Existentes

#### Exemplo: Sistema de Chat

```python
# Prompt original com problemas
prompt_chat_original = """
Fazer um servidor para chat em tempo real
"""

# Solicitar melhorias
melhorias = analisador.sugerir_melhorias_prompt(
    prompt_chat_original,
    foco="funcionalidades"
)

print("Sugestões de melhoria:")
for melhoria in melhorias.sugestoes:
    print(f"- {melhoria}")

# Aplicar melhorias sugeridas
prompt_chat_melhorado = """
Criar servidor MCP para chat em tempo real com:

FUNCIONALIDADES PRINCIPAIS:
- Sistema de salas/canais
- Mensagens privadas
- Compartilhamento de arquivos
- Notificações push
- Histórico de mensagens

FERRAMENTAS:
- send_message(room_id, content, type) -> Message
- create_room(name, type, members) -> Room
- join_room(room_id, user_id) -> bool
- upload_file(file_data, room_id) -> FileInfo
- get_history(room_id, limit, offset) -> List[Message]

RECURSOS:
- chat://rooms/{id}/messages
- chat://users/{id}/profile
- chat://files/{id}

EVENTOS EM TEMPO REAL:
- message_received
- user_joined
- user_left
- typing_indicator

SEGURANÇA:
- Autenticação de usuários
- Criptografia de mensagens
- Rate limiting
- Moderação de conteúdo
"""

# Verificar melhoria
nova_analise = analisador.analisar_prompt(prompt_chat_melhorado)
print(f"Melhoria: {nova_analise.pontuacao - 2}/10 pontos a mais!")
```

### 4. Análise Comparativa

#### Exemplo: Comparar Múltiplos Prompts

```python
# Prompts de diferentes qualidades
prompts_teste = {
    "basico": "Criar servidor MCP",
    "simples": "Criar servidor MCP para dados",
    "medio": "Criar servidor MCP para análise de dados com ferramentas básicas",
    "avancado": """
    Criar servidor MCP para análise de dados científicos com:

    FERRAMENTAS:
    - import_dataset(source, format) -> Dataset
    - clean_data(dataset_id, rules) -> CleanedDataset
    - analyze_statistics(dataset_id) -> StatReport
    - create_visualization(data, chart_type) -> Chart
    - export_results(analysis_id, format) -> File

    RECURSOS:
    - data://datasets/{id}
    - data://analyses/{id}
    - data://visualizations/{id}

    FORMATOS SUPORTADOS:
    - CSV, JSON, Excel, Parquet
    - Pandas DataFrames
    - NumPy arrays

    ANÁLISES DISPONÍVEIS:
    - Estatística descritiva
    - Correlações
    - Regressões
    - Clustering
    - Séries temporais
    """
}

# Analisar todos os prompts
resultados = {}
for nome, prompt in prompts_teste.items():
    resultado = analisador.analisar_prompt(prompt)
    resultados[nome] = resultado

# Mostrar comparação
print("📊 COMPARAÇÃO DE QUALIDADE")
print("=" * 40)
for nome, resultado in resultados.items():
    print(f"{nome.upper()}: {resultado.pontuacao}/10")
    print(f"  Fortes: {len(resultado.pontos_fortes)}")
    print(f"  Fracos: {len(resultado.pontos_fracos)}")
    print()

# Ranking de qualidade
ranking = sorted(resultados.items(), key=lambda x: x[1].pontuacao, reverse=True)
print("🏆 RANKING:")
for i, (nome, resultado) in enumerate(ranking, 1):
    print(f"{i}. {nome}: {resultado.pontuacao}/10")
```

### 5. Geração de Relatório Detalhado

#### Exemplo: Relatório Completo

```python
def gerar_relatorio_completo(prompt, nome_projeto="MeuProjeto"):
    """
    Gera relatório completo de análise de prompt
    """

    analisador = AnalisadorPromptMCP()

    # Análise principal
    resultado = analisador.analisar_prompt(prompt)

    # Análise de requisitos (se houver)
    try:
        requisitos = extrair_requisitos_do_prompt(prompt)
        validacao = analisador.validar_requisitos_mcp(requisitos)
    except:
        validacao = None

    # Sugestões de melhoria
    melhorias = analisador.sugerir_melhorias_prompt(prompt)

    # Gerar relatório
    relatorio = f"""
    📋 RELATÓRIO DE ANÁLISE MCP - {nome_projeto}
    {'=' * 50}

    📊 PONTUAÇÃO GERAL: {resultado.pontuacao}/10

    ✅ PONTOS FORTES ({len(resultado.pontos_fortes)}):
    {chr(10).join(f'  + {ponto}' for ponto in resultado.pontos_fortes)}

    ⚠️ PONTOS FRACOS ({len(resultado.pontos_fracos)}):
    {chr(10).join(f'  - {ponto}' for ponto in resultado.pontos_fracos)}

    💡 RECOMENDAÇÕES ({len(resultado.recomendacoes)}):
    {chr(10).join(f'  → {rec}' for rec in resultado.recomendacoes)}

    🔧 SUGESTÕES DE MELHORIA:
    {chr(10).join(f'  • {sug}' for sug in melhorias.sugestoes)}
    """

    if validacao:
        relatorio += f"""

    ✅ VALIDAÇÃO DE REQUISITOS:
    Status: {'Aprovado' if validacao.aprovado else 'Precisa melhorias'}
    Pontuação: {validacao.pontuacao}/10
    """

    relatorio += f"""

    📈 CLASSIFICAÇÃO:
    {classificar_prompt(resultado.pontuacao)}

    🎯 PRÓXIMOS PASSOS:
    1. Implementar correções dos pontos fracos
    2. Aplicar recomendações sugeridas
    3. Validar requisitos técnicos
    4. Realizar nova análise

    Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}
    """

    return relatorio

def classificar_prompt(pontuacao):
    """Classifica o prompt baseado na pontuação"""
    if pontuacao >= 9:
        return "🏆 EXCELENTE - Pronto para produção"
    elif pontuacao >= 7:
        return "🥇 BOM - Pequenos ajustes necessários"
    elif pontuacao >= 5:
        return "🥈 MÉDIO - Melhorias importantes necessárias"
    elif pontuacao >= 3:
        return "🥉 BÁSICO - Precisa de reformulação"
    else:
        return "❌ INADEQUADO - Reescrever completamente"

# Exemplo de uso
prompt_exemplo = """
Criar servidor MCP para análise de sentimentos em textos
com processamento de linguagem natural
"""

relatorio = gerar_relatorio_completo(prompt_exemplo, "AnáliseSentimentos")
print(relatorio)
```

## 🛠️ Ferramentas Utilitárias

### Extrator de Requisitos

```python
def extrair_requisitos_do_prompt(prompt):
    """
    Extrai requisitos automaticamente do prompt
    """
    import re

    # Buscar ferramentas mencionadas
    ferramentas = re.findall(r'(\w+)\s*\([^)]*\)', prompt)

    # Buscar recursos
    recursos = re.findall(r'(\w+://[\w/{}]+)', prompt)

    # Buscar tipos de dados
    tipos = re.findall(r'(\w+):\s*(\w+)', prompt)

    return {
        "ferramentas": ferramentas,
        "recursos": recursos,
        "tipos_entrada": dict(tipos),
        "tipos_saida": {},
        "tratamento_erros": "erro" in prompt.lower(),
        "testes": "test" in prompt.lower(),
        "documentacao": "doc" in prompt.lower()
    }
```

### Comparador de Versões

```python
def comparar_versoes_prompt(prompt_v1, prompt_v2):
    """
    Compara duas versões de um prompt
    """
    analisador = AnalisadorPromptMCP()

    resultado_v1 = analisador.analisar_prompt(prompt_v1)
    resultado_v2 = analisador.analisar_prompt(prompt_v2)

    melhoria = resultado_v2.pontuacao - resultado_v1.pontuacao

    print(f"📊 COMPARAÇÃO DE VERSÕES")
    print(f"Versão 1: {resultado_v1.pontuacao}/10")
    print(f"Versão 2: {resultado_v2.pontuacao}/10")
    print(f"Melhoria: {melhoria:+.1f} pontos")

    if melhoria > 0:
        print("✅ Versão 2 é melhor!")
    elif melhoria < 0:
        print("❌ Versão 1 era melhor")
    else:
        print("🔄 Mesma qualidade")

    return {
        "v1": resultado_v1,
        "v2": resultado_v2,
        "melhoria": melhoria
    }
```

## 🚀 Executando os Exemplos

```bash
# Iniciar o servidor
python main.py mcp

# Em outro terminal, testar as funcionalidades
python -c "
from servers.mcp_server import AnalisadorPromptMCP
analisador = AnalisadorPromptMCP()
resultado = analisador.analisar_prompt('Criar servidor MCP para gestão de tarefas')
print(f'Pontuação: {resultado.pontuacao}/10')
"
```

## 📚 Documentação Relacionada

- [Guia de Melhores Práticas MCP](../guides/mcp_best_practices.md)
- [API Completa do Servidor](../api/mcp_server_api.md)
- [Estratégias de Prompts](../guides/prompt_strategies.md)

---

_Exemplos atualizados em: 25 de maio de 2025_
