#!/usr/bin/env python3
"""
Servidor MCP para análise de prompts de criação de servidores MCP.
Este servidor fornece ferramentas para avaliar e dar feedback sobre prompts
para criação de servidores MCP baseados nas melhores práticas da documentação MCP.
"""

import logging
from typing import List, Dict, Any, Optional, TypedDict
from fastmcp import FastMCP
from pydantic import BaseModel, Field
import re
import json

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializar servidor FastMCP
mcp = FastMCP("Analisador de Prompts MCP")


class AnalisePrompt(BaseModel):
    """Modelo para resultados de análise de prompt"""
    pontuacao: int = Field(description="Pontuação geral de qualidade de 1-10")
    pontos_fortes: List[str] = Field(
        description="Pontos fortes identificados no prompt")
    pontos_fracos: List[str] = Field(description="Áreas para melhoria")
    recomendacoes: List[str] = Field(
        description="Recomendações específicas para melhoria")
    alinhamento_melhores_praticas: Dict[str, bool] = Field(
        description="Alinhamento com melhores práticas MCP")
    elementos_ausentes: List[str] = Field(
        description="Elementos importantes ausentes do prompt")


class RelatorioValidacao(TypedDict):
    """Estrutura tipada para relatório de validação"""
    pontuacao_geral: int
    validacao_aprovada: bool
    cobertura_requisitos: Dict[str, bool]
    requisitos_ausentes: List[str]
    recomendacoes: List[str]
    problemas_criticos: List[str]
    avisos: List[str]


class AnalisadorPromptMCP:
    """Analisador principal para prompts de criação de servidor MCP"""

    def __init__(self):
        # Principais melhores práticas da documentação MCP
        self.melhores_praticas = {
            "proposito_claro": "Servidor deve ter um propósito bem definido e específico",
            "design_ferramenta_adequado": "Ferramentas devem ser focadas, bem documentadas e seguir convenções de nomenclatura",
            "tratamento_erros": "Tratamento abrangente de erros e validação",
            "consideracoes_seguranca": "Validação de entrada, sanitização e medidas de segurança",
            "gerenciamento_recursos": "Tratamento adequado de recursos e limpeza",
            "documentacao": "Documentação clara e exemplos",
            "validacao_schema": "Definições adequadas de schema e validação",
            "protocolo_transporte": "Seleção apropriada de protocolo de transporte",
            "estrategia_testes": "Considerações de teste e depuração",
            "performance": "Considerações de performance e escalabilidade"
        }

        # Padrões comuns para procurar em bons prompts
        self.padroes_positivos = [
            r"ferramenta(?:s)?\s+(?:que|para|de)",
            r"implement(?:a|ar|ando)?\s+(?:um|uma|o|a)",
            r"tratamento\s+(?:de\s+)?erro(?:s)?",
            r"validação",
            r"segurança",
            r"schema",
            r"documentação",
            r"teste(?:s)?",
            r"debug",
            r"exemplo(?:s)?",
            r"melhor(?:es)?\s+prática(?:s)?",
            r"performance",
            r"escalabilidade"
        ]

        # Sinais de alerta que indicam qualidade pobre do prompt
        self.padroes_negativos = [
            r"faça?\s+(?:um|uma|o|a)\s+(?:simples|básico|rápido)",
            r"apenas\s+(?:crie|faça|construa)",
            r"qualquer\s+coisa",
            r"tanto\s+faz",
            r"genérico",
            r"simples\s+(?:servidor|ferramenta)"
        ]

    def analisar_prompt(self, prompt: str) -> AnalisePrompt:
        """Analisar um prompt de criação de servidor MCP"""

        prompt_minusculo = prompt.lower()

        # Calcular pontuação base
        pontuacao = 5  # Começar com pontuação neutra
        pontos_fortes = []
        pontos_fracos = []
        recomendacoes = []
        elementos_ausentes = []

        # Verificar padrões positivos
        correspondencias_positivas = 0
        for padrao in self.padroes_positivos:
            if re.search(padrao, prompt_minusculo):
                correspondencias_positivas += 1

        # Verificar padrões negativos
        correspondencias_negativas = 0
        for padrao in self.padroes_negativos:
            if re.search(padrao, prompt_minusculo):
                correspondencias_negativas += 1

        # Ajustar pontuação baseada nos padrões
        # Limitar contribuição positiva
        pontuacao += min(correspondencias_positivas * 0.5, 3)
        pontuacao -= correspondencias_negativas * 1.5

        # Analisar contra melhores práticas
        # Analisar contra melhores práticas
        alinhamento_melhores_praticas: Dict[str, bool] = {}
        self._analisar_melhores_praticas(prompt_minusculo, alinhamento_melhores_praticas,
                                         pontos_fortes, pontos_fracos, elementos_ausentes)
        # Gerar recomendações
        recomendacoes = self._gerar_recomendacoes(
            prompt_minusculo, elementos_ausentes)

        # Ajuste final da pontuação baseado no alinhamento com melhores práticas
        pontuacao_alinhamento = sum(
            alinhamento_melhores_praticas.values()) / len(alinhamento_melhores_praticas)
        pontuacao = int((pontuacao + pontuacao_alinhamento * 10) / 2)
        pontuacao = max(1, min(10, pontuacao))  # Limitar entre 1-10

        return AnalisePrompt(
            pontuacao=pontuacao,
            pontos_fortes=pontos_fortes,
            pontos_fracos=pontos_fracos,
            recomendacoes=recomendacoes,
            alinhamento_melhores_praticas=alinhamento_melhores_praticas,
            elementos_ausentes=elementos_ausentes
        )

    def _analisar_melhores_praticas(self, prompt: str, alinhamento: Dict[str, bool],
                                    pontos_fortes: List[str], pontos_fracos: List[str],
                                    elementos_ausentes: List[str]):
        """Analisar prompt contra melhores práticas MCP"""

        # Propósito claro
        if any(palavra in prompt for palavra in ['propósito', 'objetivo', 'meta', 'específico', 'focado']):
            alinhamento['proposito_claro'] = True
            pontos_fortes.append(
                "Mostra compreensão clara do propósito do servidor")
        else:
            alinhamento['proposito_claro'] = False
            elementos_ausentes.append(
                "Declaração clara do propósito e objetivos do servidor")

        # Design de ferramenta
        if any(palavra in prompt for palavra in ['ferramenta', 'função', 'capacidade', 'funcionalidade']):
            alinhamento['design_ferramenta_adequado'] = True
            pontos_fortes.append("Menciona ferramentas ou funcionalidades")
        else:
            alinhamento['design_ferramenta_adequado'] = False
            elementos_ausentes.append(
                "Definições específicas de ferramentas e capacidades")

        # Tratamento de erros
        if any(palavra in prompt for palavra in ['erro', 'exceção', 'validação', 'tratar']):
            alinhamento['tratamento_erros'] = True
            pontos_fortes.append("Considera tratamento de erros")
        else:
            alinhamento['tratamento_erros'] = False
            elementos_ausentes.append(
                "Estratégia de tratamento de erros e validação")

        # Segurança
        if any(palavra in prompt for palavra in ['segurança', 'seguro', 'sanitizar', 'validar']):
            alinhamento['consideracoes_seguranca'] = True
            pontos_fortes.append("Inclui considerações de segurança")
        else:
            alinhamento['consideracoes_seguranca'] = False
            elementos_ausentes.append(
                "Considerações de segurança e validação de entrada")

        # Documentação
        if any(palavra in prompt for palavra in ['documentar', 'exemplo', 'readme', 'guia']):
            alinhamento['documentacao'] = True
            pontos_fortes.append("Valoriza documentação")
        else:
            alinhamento['documentacao'] = False
            elementos_ausentes.append("Documentação e exemplos de uso")

        # Validação de schema
        if any(palavra in prompt for palavra in ['schema', 'tipo', 'modelo', 'estrutura']):
            alinhamento['validacao_schema'] = True
            pontos_fortes.append("Considera schemas de dados")
        else:
            alinhamento['validacao_schema'] = False
            elementos_ausentes.append(
                "Definições de schema e validação de dados")

        # Testes
        if any(palavra in prompt for palavra in ['teste', 'debug', 'verificar']):
            alinhamento['estrategia_testes'] = True
            pontos_fortes.append("Inclui considerações de teste")
        else:
            alinhamento['estrategia_testes'] = False
            elementos_ausentes.append("Estratégia de teste e depuração")

        # Performance
        if any(palavra in prompt for palavra in ['performance', 'escalável', 'eficiente', 'otimizar']):
            alinhamento['performance'] = True
            pontos_fortes.append("Considera aspectos de performance")
        else:
            alinhamento['performance'] = False
            elementos_ausentes.append(
                "Considerações de performance e escalabilidade")

        # Protocolo de transporte
        if any(palavra in prompt for palavra in ['stdio', 'http', 'sse', 'transporte', 'protocolo']):
            alinhamento['protocolo_transporte'] = True
            pontos_fortes.append("Especifica protocolo de transporte")
        else:
            alinhamento['protocolo_transporte'] = False
            elementos_ausentes.append(
                "Especificação de protocolo de transporte")

        # Gerenciamento de recursos
        if any(palavra in prompt for palavra in ['recurso', 'limpeza', 'gerenciar', 'ciclo de vida']):
            alinhamento['gerenciamento_recursos'] = True
            pontos_fortes.append("Considera gerenciamento de recursos")
        else:
            alinhamento['gerenciamento_recursos'] = False
            elementos_ausentes.append("Gerenciamento e limpeza de recursos")

    def _gerar_recomendacoes(self, prompt: str, elementos_ausentes: List[str]) -> List[str]:
        """Gerar recomendações específicas para melhorar o prompt"""
        recomendacoes = []

        if not any(palavra in prompt for palavra in ['ferramenta', 'função']):
            recomendacoes.append(
                "Definir ferramentas específicas e suas funcionalidades claramente")

        if not any(palavra in prompt for palavra in ['erro', 'validação']):
            recomendacoes.append(
                "Incluir requisitos de tratamento de erros e validação de entrada")

        if not any(palavra in prompt for palavra in ['segurança', 'sanitizar']):
            recomendacoes.append(
                "Especificar considerações de segurança e sanitização de entrada")

        if not any(palavra in prompt for palavra in ['schema', 'tipo']):
            recomendacoes.append(
                "Definir schemas de dados e definições de tipos")

        if not any(palavra in prompt for palavra in ['teste', 'debug']):
            recomendacoes.append("Incluir requisitos de teste e depuração")

        if not any(palavra in prompt for palavra in ['documentar', 'exemplo']):
            recomendacoes.append("Solicitar documentação e exemplos de uso")

        if not any(palavra in prompt for palavra in ['performance', 'escalável']):
            recomendacoes.append(
                "Considerar requisitos de performance e escalabilidade")

        if len(prompt.split()) < 20:
            recomendacoes.append(
                "Fornecer requisitos mais detalhados e contexto")

        if not any(palavra in prompt for palavra in ['protocolo', 'transporte']):
            recomendacoes.append(
                "Especificar o protocolo de transporte desejado (stdio, HTTP+SSE)")

        return recomendacoes


# Inicializar o analisador
analisador = AnalisadorPromptMCP()


@mcp.tool()
def analisar_prompt_mcp(prompt: str) -> AnalisePrompt:
    """
    Analisar um prompt de criação de servidor MCP para qualidade e alinhamento com melhores práticas.

    Args:
        prompt: O texto do prompt para analisar para criação de servidor MCP

    Returns:
        AnalisePrompt: Análise detalhada com pontuação, pontos fortes, pontos fracos e recomendações
    """
    try:
        logger.info(f"Analisando prompt: {prompt[:100]}...")
        analise = analisador.analisar_prompt(prompt)
        logger.info(f"Análise completa. Pontuação: {analise.pontuacao}/10")
        return analise
    except Exception as e:
        logger.error(f"Erro ao analisar prompt: {e}")
        raise


@mcp.tool()
def obter_melhores_praticas_mcp() -> Dict[str, str]:
    """
    Obter um resumo das melhores práticas de desenvolvimento de servidor MCP.

    Returns:
        Dict[str, str]: Principais melhores práticas para desenvolvimento de servidor MCP
    """
    return {
        "proposito_claro": "Definir um propósito específico e focado para seu servidor MCP",
        "design_ferramenta": "Projetar ferramentas que sejam focadas, bem documentadas e sigam convenções de nomenclatura",
        "tratamento_erros": "Implementar tratamento abrangente de erros e validação de entrada",
        "seguranca": "Incluir sanitização de entrada e medidas de segurança",
        "schemas": "Definir schemas claros para todas as entradas e saídas",
        "documentacao": "Fornecer documentação clara e exemplos de uso",
        "testes": "Incluir estratégias de teste e depuração",
        "performance": "Considerar requisitos de performance e escalabilidade",
        "transporte": "Escolher protocolo de transporte apropriado (stdio para local, HTTP+SSE para remoto)",
        "recursos": "Implementar gerenciamento adequado de recursos e limpeza"
    }


@mcp.tool()
def sugerir_melhorias_prompt(prompt_original: str) -> Dict[str, Any]:
    """
    Sugerir melhorias específicas para um prompt de criação de servidor MCP.

    Args:
        prompt_original: O prompt original para melhorar

    Returns:
        Dict contendo prompt melhorado e explicação das mudanças
    """
    try:
        analise = analisador.analisar_prompt(prompt_original)

        # Gerar prompt melhorado
        secoes_melhoradas = []

        # Adicionar propósito se ausente
        if not analise.alinhamento_melhores_praticas.get('proposito_claro', False):
            secoes_melhoradas.append(
                "Propósito: Criar um servidor MCP com um objetivo específico e bem definido."
            )

        # Adicionar especificações de ferramenta se ausente
        if not analise.alinhamento_melhores_praticas.get('design_ferramenta_adequado', False):
            secoes_melhoradas.append(
                "Ferramentas: Definir ferramentas específicas com nomes claros, descrições e parâmetros."
            )

        # Adicionar requisitos técnicos
        adicoes_tecnicas = []
        if not analise.alinhamento_melhores_praticas.get('tratamento_erros', False):
            adicoes_tecnicas.append("tratamento abrangente de erros")
        if not analise.alinhamento_melhores_praticas.get('consideracoes_seguranca', False):
            adicoes_tecnicas.append(
                "validação de entrada e medidas de segurança")
        if not analise.alinhamento_melhores_praticas.get('validacao_schema', False):
            adicoes_tecnicas.append("definições adequadas de schema")

        if adicoes_tecnicas:
            secoes_melhoradas.append(
                f"Requisitos Técnicos: Incluir {', '.join(adicoes_tecnicas)}."
            )

        # Adicionar documentação e testes
        if not analise.alinhamento_melhores_praticas.get('documentacao', False):
            secoes_melhoradas.append(
                "Documentação: Fornecer documentação clara e exemplos de uso."
            )

        if not analise.alinhamento_melhores_praticas.get('estrategia_testes', False):
            secoes_melhoradas.append(
                "Testes: Incluir estratégia de teste e considerações de depuração."
            )

        prompt_melhorado = prompt_original
        if secoes_melhoradas:
            prompt_melhorado += "\n\nRequisitos Adicionais:\n" + \
                "\n".join(secoes_melhoradas)

        return {
            "prompt_original": prompt_original,
            "prompt_melhorado": prompt_melhorado,
            "melhorias_feitas": secoes_melhoradas,
            "melhoria_pontuacao": f"Melhoria esperada de {analise.pontuacao}/10 para {min(10, analise.pontuacao + len(secoes_melhoradas))}/10"
        }

    except Exception as e:
        logger.error(f"Erro ao melhorar prompt: {e}")
        raise


@mcp.tool()
def validar_requisitos_mcp(requisitos: str) -> RelatorioValidacao:
    """
    Validar requisitos de servidor MCP contra lista de verificação de melhores práticas.

    Args:
        requisitos: A especificação de requisitos para validar

    Returns:
        RelatorioValidacao contendo resultados de validação e requisitos ausentes
    """
    try:
        analise = analisador.analisar_prompt(requisitos)

        # Criar relatório detalhado de validação
        relatorio_validacao: RelatorioValidacao = {
            "pontuacao_geral": analise.pontuacao,
            "validacao_aprovada": analise.pontuacao >= 7,
            "cobertura_requisitos": analise.alinhamento_melhores_praticas,
            "requisitos_ausentes": analise.elementos_ausentes,
            "recomendacoes": analise.recomendacoes,
            "problemas_criticos": [],
            "avisos": []
        }

        # Identificar problemas críticos
        if not analise.alinhamento_melhores_praticas.get('consideracoes_seguranca', False):
            relatorio_validacao["problemas_criticos"].append(
                "Considerações de segurança ausentes")

        if not analise.alinhamento_melhores_praticas.get('tratamento_erros', False):
            relatorio_validacao["problemas_criticos"].append(
                "Estratégia de tratamento de erros ausente")

        # Identificar avisos
        if not analise.alinhamento_melhores_praticas.get('documentacao', False):
            relatorio_validacao["avisos"].append(
                "Requisitos de documentação não especificados")

        if not analise.alinhamento_melhores_praticas.get('estrategia_testes', False):
            relatorio_validacao["avisos"].append(
                "Estratégia de teste não definida")

        return relatorio_validacao

    except Exception as e:
        logger.error(f"Erro ao validar requisitos: {e}")
        raise


if __name__ == "__main__":
    # Executar o servidor MCP
    mcp.run()
