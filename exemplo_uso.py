#!/usr/bin/env python3
"""
Exemplo de uso do Servidor Analisador de Prompts MCP.
Este arquivo demonstra como usar as ferramentas do servidor para analisar prompts.
"""

import asyncio
import json
from servers.mcp_server import AnalisadorPromptMCP


async def exemplo_uso():
    """Demonstrar o uso do Analisador de Prompts MCP"""

    print("🔍 Exemplo de Uso: Servidor Analisador de Prompts MCP\n")
    print("=" * 60)

    # Inicializar o analisador
    analisador = AnalisadorPromptMCP()

    # Exemplos de prompts para demonstração
    exemplos_prompts = [
        {
            "titulo": "❌ Prompt Inadequado",
            "prompt": "Faça um servidor MCP qualquer",
            "expectativa": "Pontuação baixa devido à falta de especificidade"
        },
        {
            "titulo": "⚠️ Prompt Básico",
            "prompt": "Crie um servidor MCP com ferramentas para manipular arquivos",
            "expectativa": "Pontuação média - menciona ferramentas mas falta detalhes"
        },
        {
            "titulo": "✅ Prompt Excelente",
            "prompt": """Crie um servidor MCP para gerenciamento de arquivos com os seguintes requisitos:
            
            Propósito: Servidor especializado em operações seguras de arquivo para desenvolvimento
            
            Ferramentas:
            - ler_arquivo: Ler conteúdo de arquivos com validação de caminho
            - escrever_arquivo: Escrever dados em arquivos com backup automático
            - listar_diretorio: Listar conteúdos de diretório com filtros
            
            Requisitos Técnicos:
            - Tratamento abrangente de erros para operações de E/S
            - Validação rigorosa de entrada para prevenir path traversal
            - Sanitização de nomes de arquivo
            - Schemas Pydantic para todas as entradas e saídas
            
            Segurança:
            - Restrição de acesso a diretórios específicos
            - Validação de permissões de arquivo
            - Log de todas as operações
            
            Implementação:
            - Usar protocolo stdio para integração local
            - Documentação completa com exemplos de uso
            - Testes unitários para cada ferramenta
            - Considerações de performance para arquivos grandes
            - Limpeza adequada de recursos""",
            "expectativa": "Pontuação alta - prompt completo e bem estruturado"
        }
    ]

    # Analisar cada exemplo
    for i, exemplo in enumerate(exemplos_prompts, 1):
        print(f"\n{i}. {exemplo['titulo']}")
        print(f"Expectativa: {exemplo['expectativa']}")
        print("-" * 40)

        # Analisar o prompt
        analise = analisador.analisar_prompt(exemplo['prompt'])

        # Mostrar resultados
        print(f"📊 Pontuação: {analise.pontuacao}/10")

        if analise.pontos_fortes:
            print(f"\n💪 Pontos Fortes ({len(analise.pontos_fortes)}):")
            for ponto in analise.pontos_fortes:
                print(f"   • {ponto}")

        if analise.elementos_ausentes:
            print(
                f"\n❌ Elementos Ausentes ({len(analise.elementos_ausentes)}):")
            # Mostrar primeiros 5
            for elemento in analise.elementos_ausentes[:5]:
                print(f"   • {elemento}")
            if len(analise.elementos_ausentes) > 5:
                print(
                    f"   ... e mais {len(analise.elementos_ausentes) - 5} elementos")

        if analise.recomendacoes:
            print(f"\n💡 Recomendações ({len(analise.recomendacoes)}):")
            # Mostrar primeiras 3
            for recomendacao in analise.recomendacoes[:3]:
                print(f"   • {recomendacao}")
            if len(analise.recomendacoes) > 3:
                print(
                    f"   ... e mais {len(analise.recomendacoes) - 3} recomendações")

        # Mostrar alinhamento com melhores práticas
        print(f"\n📋 Alinhamento com Melhores Práticas:")
        praticas_aderidas = sum(analise.alinhamento_melhores_praticas.values())
        total_praticas = len(analise.alinhamento_melhores_praticas)
        percentual = (praticas_aderidas / total_praticas) * 100
        print(
            f"   {praticas_aderidas}/{total_praticas} práticas seguidas ({percentual:.1f}%)")

        print("\n" + "=" * 60)

    # Demonstrar funcionalidade de melhores práticas
    print(f"\n📚 Melhores Práticas MCP:")
    print("-" * 30)
    melhores_praticas = analisador.melhores_praticas
    for chave, descricao in melhores_praticas.items():
        print(f"• {chave.replace('_', ' ').title()}: {descricao}")

    print(f"\n🎯 Dicas para Prompts de Qualidade:")
    print("-" * 35)
    dicas = [
        "Seja específico sobre o propósito do servidor",
        "Defina claramente cada ferramenta e seus parâmetros",
        "Inclua requisitos de segurança e validação",
        "Especifique schemas de dados e tipos",
        "Mencione estratégia de testes e depuração",
        "Considere documentação e exemplos de uso",
        "Pense em performance e escalabilidade",
        "Escolha o protocolo de transporte adequado"
    ]

    for i, dica in enumerate(dicas, 1):
        print(f"{i}. {dica}")

    print(f"\n✅ Exemplo concluído! Use estas diretrizes para criar prompts de alta qualidade.")

if __name__ == "__main__":
    asyncio.run(exemplo_uso())
