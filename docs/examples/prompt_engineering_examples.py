"""
Exemplos de Engenharia de Prompts

Este arquivo demonstra como utilizar as ferramentas do Servidor de Engenharia de Prompts
para otimizar, analisar e aplicar estratégias avançadas a prompts para diferentes tarefas.
"""

from servers.prompt_server import PromptEngineer

# Inicialização do engenheiro de prompts
engenheiro = PromptEngineer()

# Exemplo 1: Otimização de um prompt para geração de código
print("EXEMPLO 1: OTIMIZAÇÃO DE PROMPT PARA CÓDIGO")
print("-" * 60)

prompt_original = "Escreva uma função para ordenar uma lista"

resultado = engenheiro.otimizar_prompt(
    prompt=prompt_original,
    tipo_tarefa="code_generation",
    modelo_alvo="gpt-4",
    nivel_detalhe="detalhado"
)

print(f"Prompt original:\n{prompt_original}\n")
print(f"Prompt otimizado:\n{resultado['prompt_otimizado']}\n")

print("Técnicas aplicadas:")
for tecnica in resultado['tecnicas_aplicadas']:
    print(f"- {tecnica}")

print("\nMétricas estimadas:")
for metrica, valor in resultado['metricas'].items():
    print(f"- {metrica}: {valor}")

# Exemplo 2: Análise da estrutura de um prompt
print("\n\nEXEMPLO 2: ANÁLISE DE ESTRUTURA DE PROMPT")
print("-" * 60)

prompt_analise = """
Você é um assistente especializado em biologia marinha.

Explique como ocorre o fenômeno da bioluminescência em organismos marinhos de águas profundas.
Inclua exemplos de organismos específicos e suas adaptações evolutivas.

Formate a resposta com seções claras e inclua referências científicas relevantes.
"""

analise = engenheiro.analisar_estrutura_prompt(prompt_analise)

print(f"Prompt analisado:\n{prompt_analise}\n")

print("Componentes identificados:")
for componente, conteudo in analise['componentes'].items():
    print(f"- {componente}: {conteudo}")

print(f"\nComplexidade: {analise['complexidade']}/10")
print(f"Clareza: {analise['clareza']}/10")

print("\nÁreas ambíguas:")
for area in analise['ambiguidade']:
    print(f"- {area}")

print("\nRecomendações:")
for rec in analise['recomendacoes']:
    print(f"- {rec}")

# Exemplo 3: Aplicação de estratégia de Chain-of-Thought
print("\n\nEXEMPLO 3: APLICAÇÃO DE CHAIN-OF-THOUGHT")
print("-" * 60)

prompt_base = """
Em uma festa, há 8 pessoas e cada pessoa aperta a mão de todas as outras exatamente uma vez.
Quantos apertos de mão acontecem no total?
"""

resultado_cot = engenheiro.aplicar_estrategia_prompt(
    prompt=prompt_base,
    estrategia="chain_of_thought"
)

print(f"Prompt original:\n{prompt_base}\n")
print(f"Prompt com Chain-of-Thought:\n{resultado_cot['prompt_resultante']}\n")

print("Estrutura do novo prompt:")
for elemento, descricao in resultado_cot['estrutura'].items():
    print(f"- {elemento}: {descricao}")

print(f"\nNotas de uso:\n{resultado_cot['notas_uso']}")

# Exemplo 4: Aplicação de estratégia de Few-Shot Learning
print("\n\nEXEMPLO 4: APLICAÇÃO DE FEW-SHOT LEARNING")
print("-" * 60)

prompt_classificacao = "Determine se o seguinte comentário expressa uma opinião positiva, negativa ou neutra: 'O atendimento foi rápido, mas o produto não funcionou como esperado.'"

resultado_fewshot = engenheiro.aplicar_estrategia_prompt(
    prompt=prompt_classificacao,
    estrategia="few_shot",
    parametros={
        "num_exemplos": 3,
        "formato_saida": "Sentimento: [CLASSIFICAÇÃO]"
    }
)

print(f"Prompt original:\n{prompt_classificacao}\n")
print(
    f"Prompt com Few-Shot Learning:\n{resultado_fewshot['prompt_resultante']}\n")

# Exemplo 5: Geração de template para um cenário específico
print("\n\nEXEMPLO 5: GERAÇÃO DE TEMPLATE DE PROMPT")
print("-" * 60)

template = engenheiro.gerar_prompt_template(
    cenario="Análise de código para revisão de segurança",
    tipo_tarefa="code_generation",
    nivel_complexidade="avançado",
    incluir_exemplos=True
)

print(f"Template gerado para análise de segurança de código:\n")
print("-" * 60)
print(template['template'])
print("-" * 60)

print("\nVariáveis a serem preenchidas:")
for var in template['variaveis']:
    print(f"- {var}")

print("\nExemplo de uso:")
exemplo = template['exemplos_uso'][0]
print(f"- Descrição: {exemplo['descricao']}")
print(f"- Template preenchido: {exemplo['prompt']}")

# Exemplo 6: Comparação de estratégias para um mesmo prompt
print("\n\nEXEMPLO 6: COMPARAÇÃO DE ESTRATÉGIAS")
print("-" * 60)

prompt_problema = "Como podemos reduzir o desperdício de alimentos em restaurantes?"

estrategias = ["role_prompting", "tree_of_thoughts", "self_consistency"]
resultados = {}

for estrategia in estrategias:
    resultado = engenheiro.aplicar_estrategia_prompt(
        prompt=prompt_problema,
        estrategia=estrategia
    )
    resultados[estrategia] = resultado

print(f"Prompt original: {prompt_problema}\n")

for estrategia, resultado in resultados.items():
    print(f"Estratégia: {estrategia}")
    print(f"- Comprimento: {len(resultado['prompt_resultante'])} caracteres")
    print(f"- Estrutura: {', '.join(resultado['estrutura'].keys())}")
    print(f"- Amostra: {resultado['prompt_resultante'][:100]}...\n")

# Exemplo 7: Pipeline completo para um caso real
print("\n\nEXEMPLO 7: PIPELINE COMPLETO DE ENGENHARIA DE PROMPTS")
print("-" * 60)

caso_real = """
Escreva um email para clientes anunciando uma manutenção programada no sistema.
"""

# Passo 1: Analisar a estrutura
analise = engenheiro.analisar_estrutura_prompt(caso_real)
print(
    f"Análise inicial - Clareza: {analise['clareza']}/10, Complexidade: {analise['complexidade']}/10")

# Passo 2: Identificar estratégia mais adequada
if analise['clareza'] < 7:
    estrategia_recomendada = "role_prompting"  # Para adicionar contexto
elif "tarefa" not in analise['componentes']:
    estrategia_recomendada = "few_shot"  # Para mostrar exemplos do formato desejado
else:
    estrategia_recomendada = "refinement"  # Para refinar iterativamente

print(f"Estratégia recomendada: {estrategia_recomendada}")

# Passo 3: Aplicar a estratégia
prompt_intermediario = engenheiro.aplicar_estrategia_prompt(
    prompt=caso_real,
    estrategia=estrategia_recomendada
)

# Passo 4: Otimização final
prompt_final = engenheiro.otimizar_prompt(
    prompt=prompt_intermediario['prompt_resultante'],
    tipo_tarefa="text_generation",
    nivel_detalhe="detalhado"
)

print("\nPipeline completo:")
print(f"1. Prompt original ({len(caso_real)} caracteres)")
print(
    f"2. Após {estrategia_recomendada} ({len(prompt_intermediario['prompt_resultante'])} caracteres)")
print(
    f"3. Após otimização final ({len(prompt_final['prompt_otimizado'])} caracteres)")

print("\nPrompt final otimizado:")
print("-" * 60)
print(prompt_final['prompt_otimizado'])
print("-" * 60)

# Demonstração interativa (simulada)
if __name__ == "__main__":
    print("\n\nDEMONSTRAÇÃO INTERATIVA")
    print("=" * 70)

    print(
        "Por favor, digite um prompt para otimizar: [Simulado] Traduza este texto para espanhol")
    tipo = "text_generation"  # Simulando entrada do usuário

    prompt_usuario = "Traduza este texto para espanhol"

    # Análise e recomendação
    analise = engenheiro.analisar_estrutura_prompt(prompt_usuario)

    print("\nAnálise do seu prompt:")
    print(f"- Clareza: {analise['clareza']}/10")
    print(f"- Complexidade: {analise['complexidade']}/10")
    print(f"- Principais recomendações: {analise['recomendacoes'][0]}")

    # Otimização
    otimizado = engenheiro.otimizar_prompt(
        prompt=prompt_usuario,
        tipo_tarefa=tipo
    )

    print("\nSeu prompt otimizado:")
    print("-" * 60)
    print(otimizado['prompt_otimizado'])
    print("-" * 60)

    print("\nTécnicas aplicadas:")
    for tecnica in otimizado['tecnicas_aplicadas']:
        print(f"- {tecnica}")

    print("\nSimulação concluída!")
