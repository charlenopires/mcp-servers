#!/usr/bin/env python3
"""
Script de teste para o servidor Analisador de Prompts MCP.
"""

from servers.mcp_server import AnalisadorPromptMCP
import sys
import os
# Adicionar o diretório pai ao path para importar os servidores
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def testar_analisador():
    """Testar a funcionalidade do AnalisadorPromptMCP"""
    analisador = AnalisadorPromptMCP()

    # Casos de teste
    casos_teste = [
        {
            "nome": "Prompt Ruim",
            "prompt": "Faça um servidor MCP simples",
            "faixa_pontuacao_esperada": (1, 4)
        },
        {
            "nome": "Prompt Médio",
            "prompt": "Crie um servidor MCP com ferramentas para operações de arquivo incluindo tratamento de erros",
            "faixa_pontuacao_esperada": (4, 7)
        },
        {
            "nome": "Prompt Bom",
            "prompt": """Crie um servidor MCP para operações de arquivo com os seguintes requisitos:
            - Ferramentas para ler, escrever e listar arquivos
            - Tratamento abrangente de erros e validação
            - Medidas de segurança incluindo sanitização de entrada
            - Definições claras de schema para todas as entradas/saídas
            - Documentação e exemplos de uso
            - Estratégia de teste
            - Considerações de performance
            - Usa protocolo de transporte stdio""",
            "faixa_pontuacao_esperada": (7, 10)
        }
    ]

    print("Testando Analisador de Prompts MCP...\n")

    for caso_teste in casos_teste:
        print(f"Teste: {caso_teste['nome']}")
        print(f"Prompt: {caso_teste['prompt'][:100]}...")

        analise = analisador.analisar_prompt(caso_teste['prompt'])

        print(f"Pontuação: {analise.pontuacao}/10")
        print(f"Faixa esperada: {caso_teste['faixa_pontuacao_esperada']}")

        # Verificar se a pontuação está na faixa esperada
        pontuacao_min, pontuacao_max = caso_teste['faixa_pontuacao_esperada']
        if pontuacao_min <= analise.pontuacao <= pontuacao_max:
            print("✅ PASSOU - Pontuação na faixa esperada")
        else:
            print("❌ FALHOU - Pontuação fora da faixa esperada")

        print(f"Pontos fortes: {len(analise.pontos_fortes)}")
        for ponto_forte in analise.pontos_fortes[:3]:  # Mostrar os primeiros 3
            print(f"  - {ponto_forte}")

        print(f"Pontos fracos: {len(analise.pontos_fracos)}")
        for ponto_fraco in analise.pontos_fracos[:3]:  # Mostrar os primeiros 3
            print(f"  - {ponto_fraco}")

        print(f"Elementos ausentes: {len(analise.elementos_ausentes)}")
        # Mostrar os primeiros 3
        for ausente in analise.elementos_ausentes[:3]:
            print(f"  - {ausente}")

        print("-" * 50)

    print("Testando recuperação de melhores práticas...")
    melhores_praticas = analisador.melhores_praticas
    print(f"Encontradas {len(melhores_praticas)} melhores práticas")
    for chave, valor in list(melhores_praticas.items())[:3]:
        print(f"  - {chave}: {valor}")

    print("\n✅ Todos os testes concluídos!")


if __name__ == "__main__":
    testar_analisador()
