"""
Exemplo de uso do Analisador de Prompts MCP

Este arquivo demonstra como utilizar o Analisador de Prompts MCP para
avaliar e melhorar seus prompts para criação de servidores MCP.
"""

from servers.mcp_server import AnalisadorPromptMCP

# Inicialização do analisador
analisador = AnalisadorPromptMCP()

# Exemplo 1: Análise de um prompt básico
print("EXEMPLO 1: ANÁLISE DE PROMPT BÁSICO")
print("-" * 50)

prompt_basico = "Faça um servidor MCP para processamento de arquivos"

resultado = analisador.analisar_prompt(prompt_basico)

print(f"Pontuação: {resultado['pontuacao']}/10")
print("\nPontos fortes:")
for ponto in resultado['pontos_fortes']:
    print(f"- {ponto}")

print("\nPontos fracos:")
for ponto in resultado['pontos_fracos']:
    print(f"- {ponto}")

print("\nSugestões:")
for sugestao in resultado['sugestoes']:
    print(f"- {sugestao}")

print("\nCritérios avaliados:")
for criterio, pontuacao in resultado['criterios_avaliados'].items():
    print(f"- {criterio}: {pontuacao}/10")

# Exemplo 2: Obtenção de melhores práticas
print("\n\nEXEMPLO 2: OBTENÇÃO DE MELHORES PRÁTICAS")
print("-" * 50)

melhores_praticas = analisador.obter_melhores_praticas_mcp(
    categoria="design_ferramentas")

print("Melhores práticas para design de ferramentas:")
for i, pratica in enumerate(melhores_praticas['praticas'], 1):
    print(f"\n{i}. {pratica['titulo']}")
    print(f"   {pratica['descricao']}")

print("\nExemplos:")
for titulo, exemplo in melhores_praticas['exemplos'].items():
    print(f"\n- {titulo}:")
    print(f"  Bom exemplo: {exemplo['bom']}")
    print(f"  Mau exemplo: {exemplo['ruim']}")

# Exemplo 3: Melhoria de um prompt existente
print("\n\nEXEMPLO 3: MELHORIA DE PROMPT")
print("-" * 50)

prompt_original = """
Crie um servidor MCP para processamento de imagens.
"""

melhorias = analisador.sugerir_melhorias_prompt(
    prompt=prompt_original,
    foco=["clareza", "tratamento_erros", "documentacao"]
)

print(f"Prompt original:\n{prompt_original}\n")
print(f"Prompt melhorado:\n{melhorias['prompt_melhorado']}\n")

print("Alterações realizadas:")
for alteracao in melhorias['alteracoes']:
    print(f"- {alteracao}")

print("\nExplicações:")
for tipo, explicacao in melhorias['explicacoes'].items():
    print(f"\n- {tipo}:")
    print(f"  {explicacao}")

# Exemplo 4: Validação de requisitos MCP
print("\n\nEXEMPLO 4: VALIDAÇÃO DE REQUISITOS")
print("-" * 50)

prompt_avancado = """
Desenvolva um servidor MCP para processamento de documentos com estas ferramentas:
1. extrair_texto(documento: bytes, formato: str) -> dict
2. analisar_estrutura(documento: bytes) -> dict
3. converter_formato(documento: bytes, formato_origem: str, formato_destino: str) -> bytes

Cada ferramenta deve validar suas entradas e retornar mensagens de erro descritivas.
Documente claramente os formatos suportados e os campos retornados em cada resposta.
Implemente tratamento de segurança para evitar injeção de código e processamento de arquivos maliciosos.
"""

validacao = analisador.validar_requisitos_mcp(
    prompt=prompt_avancado,
    nivel_rigor="intermediário"
)

print(f"Conformidade: {validacao['conformidade']}%")

print("\nRequisitos atendidos:")
for req in validacao['requisitos_atendidos']:
    print(f"✅ {req}")

print("\nRequisitos faltantes:")
for req in validacao['requisitos_faltantes']:
    print(f"❌ {req}")

# Exemplo 5: Fluxo completo de análise e melhoria
print("\n\nEXEMPLO 5: FLUXO COMPLETO")
print("-" * 50)

# Prompt inicial com problemas
prompt_inicial = "Fazer um servidor MCP de IA"

# Passo 1: Analisar o prompt
analise = analisador.analisar_prompt(prompt_inicial)
print(f"Análise inicial: {analise['pontuacao']}/10")

# Passo 2: Identificar pontos fracos principais
pontos_fracos_principais = analise['pontos_fracos'][:3]
print("\nPrincipais pontos fracos:")
for ponto in pontos_fracos_principais:
    print(f"- {ponto}")

# Passo 3: Obter melhores práticas relevantes
mp_design = analisador.obter_melhores_praticas_mcp(
    categoria="design_ferramentas")
print(f"\nObtidas {len(mp_design['praticas'])} melhores práticas para design")

# Passo 4: Melhorar o prompt com base nos pontos fracos
melhoria = analisador.sugerir_melhorias_prompt(
    prompt=prompt_inicial,
    foco=[p.split(":")[0].lower() for p in pontos_fracos_principais]
)

# Passo 5: Validar o prompt melhorado
validacao_final = analisador.validar_requisitos_mcp(
    prompt=melhoria['prompt_melhorado'],
    nivel_rigor="básico"
)

print(
    f"\nPrompt melhorado (conformidade: {validacao_final['conformidade']}%):")
print("-" * 50)
print(melhoria['prompt_melhorado'])
print("-" * 50)

print("\nFluxo completo concluído!")

# Exemplo de uso em um caso real
if __name__ == "__main__":
    print("\n\nEXEMPLO DE CASO REAL")
    print("=" * 70)

    caso_real = """
    Crie um servidor MCP para análise de sentimento em textos de redes sociais.
    """

    # Análise inicial
    analise = analisador.analisar_prompt(caso_real)

    if analise['pontuacao'] < 7.0:
        print(
            f"Prompt precisa de melhorias (pontuação: {analise['pontuacao']}/10)")

        # Melhorar o prompt
        melhoria = analisador.sugerir_melhorias_prompt(
            prompt=caso_real,
            foco=["clareza", "design_ferramentas",
                  "tratamento_erros", "documentacao"]
        )

        print("\nPrompt melhorado:")
        print(melhoria['prompt_melhorado'])

        # Verificar novamente
        analise_final = analisador.analisar_prompt(
            melhoria['prompt_melhorado'])
        print(f"\nNova pontuação: {analise_final['pontuacao']}/10")
    else:
        print(f"Prompt já está bom! (pontuação: {analise['pontuacao']}/10)")
