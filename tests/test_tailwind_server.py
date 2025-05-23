#!/usr/bin/env python3
"""
Script de teste para o Servidor MCP Tailwind CSS v4.1.
"""

import json
import sys
import os
# Adicionar o diretório pai ao path para importar os servidores
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def testar_servidor_tailwind():
    """Testar a funcionalidade do Servidor Tailwind CSS v4.1"""
    print("Testando Servidor MCP Tailwind CSS v4.1...\n")

    # Importar as funções e dados do servidor Tailwind
    try:
        from servers.tailwind_server import TAILWIND_V4_CONTEXT
        print("✅ Importação do contexto Tailwind v4.1 realizada com sucesso")
    except ImportError as e:
        print(f"❌ ERRO na importação: {e}")
        return

    # Casos de teste para diferentes funcionalidades
    casos_teste = [
        {
            "nome": "Verificação de Versão e Data",
            "teste": lambda: TAILWIND_V4_CONTEXT["version"] == "4.1.7" and
            TAILWIND_V4_CONTEXT["release_date"] == "2025-05-15"
        },
        {
            "nome": "Verificação de Novas Utilidades text-shadow",
            "teste": lambda: "text-shadow-xs" in TAILWIND_V4_CONTEXT["major_changes"]["new_utilities"]["text-shadow"]
        },
        {
            "nome": "Verificação de Novos Variants",
            "teste": lambda: "user-valid" in TAILWIND_V4_CONTEXT["major_changes"]["new_variants"]
        },
        {
            "nome": "Verificação de Performance",
            "teste": lambda: "full_build" in TAILWIND_V4_CONTEXT["major_changes"]["performance"]
        },
        {
            "nome": "Verificação de Configuração CSS",
            "teste": lambda: TAILWIND_V4_CONTEXT["major_changes"]["configuration"]["import"] == '@import "tailwindcss";'
        }
    ]

    print("🧪 Executando testes de contexto Tailwind CSS...")
    print("=" * 60)

    sucessos = 0
    for i, caso in enumerate(casos_teste, 1):
        print(f"\n{i}. Teste: {caso['nome']}")

        try:
            if caso['teste']():
                print("✅ PASSOU - Verificação bem-sucedida")
                sucessos += 1
            else:
                print("❌ FALHOU - Verificação não passou")
        except Exception as e:
            print(f"❌ ERRO no teste: {e}")

        print("-" * 40)

    # Verificar estrutura completa do contexto
    print(f"\n📊 Verificando estrutura completa do contexto...")
    print("-" * 50)

    secoes_esperadas = [
        "version", "release_date", "major_changes"
    ]

    subsecoes_esperadas = [
        "configuration", "new_utilities", "new_variants",
        "directives", "performance"
    ]

    # Verificar seções principais
    for secao in secoes_esperadas:
        if secao in TAILWIND_V4_CONTEXT:
            print(f"✅ Seção '{secao}' presente")
        else:
            print(f"❌ Seção '{secao}' ausente")

    # Verificar subseções em major_changes
    major_changes = TAILWIND_V4_CONTEXT.get("major_changes", {})
    for subsecao in subsecoes_esperadas:
        if subsecao in major_changes:
            print(f"✅ Subseção '{subsecao}' presente")
        else:
            print(f"❌ Subseção '{subsecao}' ausente")

    # Testar funcionalidades específicas do Tailwind v4.1
    print(f"\n🎨 Testando funcionalidades específicas do Tailwind v4.1...")
    print("-" * 55)

    # Verificar novas utilidades
    new_utilities = major_changes.get("new_utilities", {})

    if "text-shadow" in new_utilities:
        text_shadows = new_utilities["text-shadow"]
        print(f"📝 Utilidades text-shadow disponíveis: {len(text_shadows)}")
        for shadow in text_shadows:
            print(f"   • {shadow}")
        print("✅ Novas utilidades text-shadow verificadas")
    else:
        print("❌ Utilidades text-shadow não encontradas")

    # Verificar novos variants
    new_variants = major_changes.get("new_variants", {})
    print(f"\n🔄 Novos variants disponíveis: {len(new_variants)}")
    for variant, descricao in new_variants.items():
        print(f"   • {variant}: {descricao}")

    # Verificar directives
    directives = major_changes.get("directives", {})
    print(f"\n📋 Diretivas disponíveis: {len(directives)}")
    for diretiva, descricao in directives.items():
        print(f"   • {diretiva}: {descricao}")

    # Verificar melhorias de performance
    performance = major_changes.get("performance", {})
    print(f"\n⚡ Melhorias de performance:")
    for metrica, valor in performance.items():
        print(f"   • {metrica.replace('_', ' ').title()}: {valor}")

    # Teste de simulação de consulta
    print(f"\n🔍 Simulando consultas de exemplo...")
    print("-" * 40)

    consultas_exemplo = [
        "Como usar text-shadow no Tailwind v4.1?",
        "Quais são os novos variants disponíveis?",
        "Como configurar tema no CSS ao invés de JS?",
        "Qual a melhoria de performance no v4.1?"
    ]

    for consulta in consultas_exemplo:
        print(f"📝 Consulta: '{consulta}'")

        # Simular busca no contexto
        if "text-shadow" in consulta.lower():
            if "text-shadow" in new_utilities:
                print("✅ Informação encontrada: utilidades text-shadow disponíveis")
            else:
                print("❌ Informação não encontrada")

        elif "variant" in consulta.lower():
            if new_variants:
                print(
                    f"✅ Informação encontrada: {len(new_variants)} novos variants")
            else:
                print("❌ Informação não encontrada")

        elif "configurar" in consulta.lower() and "css" in consulta.lower():
            config = major_changes.get("configuration", {})
            if config:
                print("✅ Informação encontrada: configuração via CSS disponível")
            else:
                print("❌ Informação não encontrada")

        elif "performance" in consulta.lower():
            if performance:
                print("✅ Informação encontrada: dados de performance disponíveis")
            else:
                print("❌ Informação não encontrada")
        else:
            print("ℹ️ Consulta não corresponde aos padrões testados")

        print()

    # Resumo dos testes
    print(f"\n📈 Resumo dos Testes:")
    print("=" * 30)
    print(f"Testes principais: {sucessos}/{len(casos_teste)} passaram")
    print(
        f"Contexto Tailwind v4.1: {'✅ Válido' if sucessos >= len(casos_teste)//2 else '❌ Inválido'}")
    print(
        f"Estrutura de dados: {'✅ Completa' if all(s in TAILWIND_V4_CONTEXT for s in secoes_esperadas) else '❌ Incompleta'}")

    print(f"\n🎉 Testes do Servidor Tailwind CSS v4.1 concluídos!")

    return sucessos == len(casos_teste)


if __name__ == "__main__":
    testar_servidor_tailwind()
