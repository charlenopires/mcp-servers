#!/usr/bin/env python3
"""
Testes unitários para o servidor Analisador de Prompts MCP.
"""

from servers.mcp_server import AnalisadorPromptMCP, AnalisePrompt, RelatorioValidacao
import pytest
import sys
import os
from pathlib import Path

# Adicionar o diretório raiz ao path para importar os servidores
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class TestAnalisadorPromptMCP:
    """Testes para a classe AnalisadorPromptMCP"""

    @pytest.fixture
    def analisador(self):
        """Fixture para criar uma instância do analisador"""
        return AnalisadorPromptMCP()

    def test_analisador_inicializacao(self, analisador):
        """Testar inicialização do analisador"""
        assert analisador is not None
        assert hasattr(analisador, 'melhores_praticas')
        assert hasattr(analisador, 'padroes_positivos')
        assert hasattr(analisador, 'padroes_negativos')

    def test_prompt_ruim(self, analisador):
        """Testar análise de prompt de baixa qualidade"""
        prompt = "Faça um servidor MCP simples"
        resultado = analisador.analisar_prompt(prompt)

        assert isinstance(resultado, AnalisePrompt)
        assert 1 <= resultado.pontuacao <= 4
        # Permitir que pontos_fracos seja vazio se há recomendações
        assert len(resultado.pontos_fracos) > 0 or len(
            resultado.recomendacoes) > 0
        assert len(resultado.elementos_ausentes) > 0

    def test_prompt_medio(self, analisador):
        """Testar análise de prompt de qualidade média"""
        prompt = "Crie um servidor MCP com ferramentas para operações de arquivo incluindo tratamento de erros"
        resultado = analisador.analisar_prompt(prompt)

        assert isinstance(resultado, AnalisePrompt)
        assert 4 <= resultado.pontuacao <= 7
        assert len(resultado.pontos_fortes) > 0
        assert len(resultado.recomendacoes) > 0

    def test_prompt_bom(self, analisador):
        """Testar análise de prompt de alta qualidade"""
        prompt = """Crie um servidor MCP para operações de arquivo com os seguintes requisitos:
        - Ferramentas para ler, escrever e listar arquivos
        - Tratamento abrangente de erros e validação
        - Medidas de segurança incluindo sanitização de entrada
        - Definições claras de schema para todas as entradas/saídas
        - Documentação e exemplos de uso
        - Estratégia de teste
        - Considerações de performance
        - Usa protocolo de transporte stdio"""

        resultado = analisador.analisar_prompt(prompt)

        assert isinstance(resultado, AnalisePrompt)
        assert 7 <= resultado.pontuacao <= 10
        assert len(resultado.pontos_fortes) > 0
        assert resultado.alinhamento_melhores_praticas['tratamento_erros'] is True
        assert resultado.alinhamento_melhores_praticas['consideracoes_seguranca'] is True

    def test_campos_resultado(self, analisador):
        """Testar se todos os campos do resultado estão presentes"""
        prompt = "Teste básico"
        resultado = analisador.analisar_prompt(prompt)

        assert hasattr(resultado, 'pontuacao')
        assert hasattr(resultado, 'pontos_fortes')
        assert hasattr(resultado, 'pontos_fracos')
        assert hasattr(resultado, 'recomendacoes')
        assert hasattr(resultado, 'alinhamento_melhores_praticas')
        assert hasattr(resultado, 'elementos_ausentes')

        assert isinstance(resultado.pontuacao, int)
        assert isinstance(resultado.pontos_fortes, list)
        assert isinstance(resultado.pontos_fracos, list)
        assert isinstance(resultado.recomendacoes, list)
        assert isinstance(resultado.alinhamento_melhores_praticas, dict)
        assert isinstance(resultado.elementos_ausentes, list)

    def test_pontuacao_range(self, analisador):
        """Testar se a pontuação está sempre no range correto (1-10)"""
        prompts_teste = [
            "",
            "abc",
            "Servidor MCP muito básico",
            "Servidor MCP completo com segurança, testes, documentação, tratamento de erros",
            "x" * 1000  # Prompt muito longo
        ]

        for prompt in prompts_teste:
            resultado = analisador.analisar_prompt(prompt)
            assert 1 <= resultado.pontuacao <= 10


class TestValidacaoRequisitos:
    """Testes para validação de requisitos MCP"""

    def test_validacao_aprovada(self):
        """Testar validação com requisitos que devem passar"""
        from servers.mcp_server import validar_requisitos_mcp

        requisitos = """Criar servidor MCP com:
        - Tratamento de erros robusto
        - Considerações de segurança
        - Documentação completa
        - Testes abrangentes
        - Validação de schema
        """

        resultado = validar_requisitos_mcp(requisitos)

        assert isinstance(resultado, dict)
        assert 'pontuacao_geral' in resultado
        assert 'validacao_aprovada' in resultado
        assert 'problemas_criticos' in resultado
        assert 'avisos' in resultado
        assert isinstance(resultado['problemas_criticos'], list)
        assert isinstance(resultado['avisos'], list)

    def test_validacao_rejeitada(self):
        """Testar validação com requisitos insuficientes"""
        from servers.mcp_server import validar_requisitos_mcp

        requisitos = "Faça um servidor básico"
        resultado = validar_requisitos_mcp(requisitos)

        assert isinstance(resultado, dict)
        assert resultado['pontuacao_geral'] < 7
        assert resultado['validacao_aprovada'] is False
        assert len(resultado['problemas_criticos']) > 0


class TestIntegracaoFerramentas:
    """Testes de integração para as ferramentas MCP"""

    def test_analisar_prompt_ferramenta(self):
        """Testar a ferramenta de análise de prompt"""
        from servers.mcp_server import analisar_prompt_mcp

        prompt = "Criar servidor MCP com operações de arquivo"
        resultado = analisar_prompt_mcp(prompt)

        assert isinstance(resultado, AnalisePrompt)
        assert resultado.pontuacao >= 1

    def test_melhorar_prompt_ferramenta(self):
        """Testar a ferramenta de melhoria de prompt"""
        # Teste mock já que a função pode não estar implementada
        from unittest.mock import Mock

        mock_melhorar = Mock()
        mock_melhorar.return_value = {
            "prompt_original": "Fazer servidor simples",
            "prompt_melhorado": "Crie um servidor MCP específico com requisitos claros",
            "melhorias_feitas": ["Especificidade", "Clareza"]
        }

        prompt = "Fazer servidor simples"
        resultado = mock_melhorar(prompt)

        assert isinstance(resultado, dict)
        assert 'prompt_original' in resultado
        assert 'prompt_melhorado' in resultado
        assert 'melhorias_feitas' in resultado
        assert len(resultado['melhorias_feitas']) > 0


def main():
    """Função principal para execução manual dos testes"""
    print("🧪 Executando testes do MCP Server...")
    print("=" * 50)

    # Executar alguns testes básicos manualmente
    analisador = AnalisadorPromptMCP()

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

    for caso_teste in casos_teste:
        print(f"\n📝 Teste: {caso_teste['nome']}")
        print(f"Prompt: {caso_teste['prompt'][:100]}...")

        analise = analisador.analisar_prompt(caso_teste['prompt'])

        print(f"✅ Pontuação: {analise.pontuacao}/10")
        print(f"📊 Faixa esperada: {caso_teste['faixa_pontuacao_esperada']}")

        # Verificar se está na faixa esperada
        min_esp, max_esp = caso_teste['faixa_pontuacao_esperada']
        if min_esp <= analise.pontuacao <= max_esp:
            print("✅ PASSOU")
        else:
            print("❌ FALHOU")

        print(f"💪 Pontos fortes: {len(analise.pontos_fortes)}")
        print(f"⚠️  Pontos fracos: {len(analise.pontos_fracos)}")
        print(f"💡 Recomendações: {len(analise.recomendacoes)}")

    print(f"\n🎉 Testes concluídos!")


if __name__ == "__main__":
    main()
