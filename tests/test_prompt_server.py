#!/usr/bin/env python3
"""
Script de teste para o Servidor MCP de Engenharia de Prompts.
"""

from servers.prompt_server import PromptEngineer, TaskType, PromptOptimizationRequest
import sys
import os
# Adicionar o diretório pai ao path para importar os servidores
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def testar_servidor_prompts():
    """Testar a funcionalidade do Servidor de Engenharia de Prompts"""
    print("Testando Servidor MCP de Engenharia de Prompts...\n")

    # Inicializar o engenheiro de prompts
    engenheiro = PromptEngineer()

    # Casos de teste
    casos_teste = [
        {
            "nome": "Prompt de Geração de Código",
            "prompt": "Escreva uma função",
            "tipo_tarefa": "code_generation",
            "audiencia": "desenvolvedores",
            "tom": "tecnico"
        },
        {
            "nome": "Prompt de Análise de Texto",
            "prompt": "Analise este texto",
            "tipo_tarefa": "analysis",
            "audiencia": "analistas",
            "tom": "formal"
        },
        {
            "nome": "Prompt Criativo",
            "prompt": "Conte uma história",
            "tipo_tarefa": "creative",
            "audiencia": "geral",
            "tom": "casual"
        },
        {
            "nome": "Prompt de Resolução de Problemas",
            "prompt": "Como resolver este problema?",
            "tipo_tarefa": "problem_solving",
            "audiencia": "estudantes",
            "tom": "educativo"
        }
    ]

    print("🧪 Executando testes de otimização de prompts...")
    print("=" * 60)

    for i, caso in enumerate(casos_teste, 1):
        print(f"\n{i}. Teste: {caso['nome']}")
        print(f"Prompt original: '{caso['prompt']}'")
        print(f"Tipo de tarefa: {caso['tipo_tarefa']}")
        print("-" * 40)

        try:
            # Criar requisição de otimização
            requisicao = PromptOptimizationRequest(
                prompt=caso['prompt'],
                task_type=caso['tipo_tarefa'],
                target_audience=caso['audiencia'],
                tone=caso['tom']
            )

            # Otimizar o prompt
            resultado = engenheiro.optimize_prompt(requisicao)

            print("✅ Otimização realizada com sucesso!")
            print(
                f"📝 Prompt otimizado: '{resultado.optimized_prompt[:100]}{'...' if len(resultado.optimized_prompt) > 100 else ''}'")
            print(
                f"🔧 Técnicas aplicadas: {', '.join(resultado.techniques_applied)}")
            print(f"🎯 Tipo identificado: {resultado.task_type}")
            print(f"💡 Sugestões: {len(resultado.suggestions)} disponíveis")

            # Verificar se o prompt foi realmente melhorado
            if len(resultado.optimized_prompt) > len(caso['prompt']):
                print("✅ PASSOU - Prompt foi expandido e melhorado")
            else:
                print("⚠️ AVISO - Prompt não foi significativamente expandido")

        except Exception as e:
            print(f"❌ ERRO no teste: {e}")

        print("-" * 40)

    # Testar identificação de tipo de tarefa
    print(f"\n🔍 Testando identificação de tipos de tarefa...")
    print("-" * 40)

    prompts_teste_tipo = [
        ("Escreva um código Python para calcular fibonacci", TaskType.CODE_GENERATION),
        ("Resuma este artigo científico", TaskType.SUMMARIZATION),
        ("Traduza este texto para inglês", TaskType.TRANSLATION),
        ("Analise os dados de vendas", TaskType.ANALYSIS),
        ("Responda: qual é a capital do Brasil?", TaskType.QUESTION_ANSWERING)
    ]

    for prompt_teste, tipo_esperado in prompts_teste_tipo:
        tipo_identificado = engenheiro.identify_task_type(prompt_teste)
        print(f"Prompt: '{prompt_teste[:50]}...'")
        print(
            f"Esperado: {tipo_esperado.value}, Identificado: {tipo_identificado.value}")

        if tipo_identificado == tipo_esperado:
            print("✅ PASSOU - Tipo identificado corretamente")
        else:
            print("⚠️ DIVERGÊNCIA - Tipo identificado diferente do esperado")
        print()

    # Testar frameworks de prompt
    print(f"\n📋 Testando frameworks de prompt...")
    print("-" * 40)

    frameworks_disponiveis = engenheiro.frameworks
    print(f"Frameworks disponíveis: {len(frameworks_disponiveis)}")

    for nome_framework, componentes in frameworks_disponiveis.items():
        print(f"• {nome_framework}: {', '.join(componentes)}")

    # Testar aplicação de framework RACE
    prompt_simples = "Escreva um email"
    try:
        prompt_com_race = engenheiro.apply_framework(prompt_simples, "RACE")
        print(f"\n🎯 Exemplo de aplicação do framework RACE:")
        print(f"Original: '{prompt_simples}'")
        print(f"Com RACE: '{prompt_com_race}'")

        if "Role:" in prompt_com_race and "Action:" in prompt_com_race:
            print("✅ PASSOU - Framework RACE aplicado corretamente")
        else:
            print("❌ FALHOU - Framework RACE não aplicado adequadamente")

    except Exception as e:
        print(f"❌ ERRO ao aplicar framework: {e}")

    print(f"\n🎉 Testes do Servidor de Engenharia de Prompts concluídos!")


if __name__ == "__main__":
    testar_servidor_prompts()
