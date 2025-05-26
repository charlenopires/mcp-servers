#!/usr/bin/env python3
"""
🛠️ MCP Servers CLI - Interface de Linha de Comando

Esta ferramenta fornece uma interface unificada para interagir com todos os servidores MCP:
- Servidor de Análise MCP
- Servidor de Engenharia de Prompts  
- Servidor Tailwind CSS v4.1
- FastMCP Server

Uso:
    python mcp_cli.py --help
    python mcp_cli.py analyze "seu prompt aqui"
    python mcp_cli.py optimize "prompt" --framework CRISPE
    python mcp_cli.py tailwind component button --config '{"cor": "blue"}'
    python mcp_cli.py fastmcp generate server_name --tools '["tool1", "tool2"]'
"""

import argparse
import json
import sys
import os
from typing import Dict, List, Optional
from datetime import datetime

# Adicionar o diretório raiz ao path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    # Como os servidores são baseados em FastMCP, vamos criar wrappers para a CLI
    from datetime import datetime
    import subprocess
    import tempfile

    class MCPServerCLIWrapper:
        """Wrapper para interagir com servidores MCP via CLI"""

        def __init__(self, server_name: str):
            self.server_name = server_name

        def analisar_prompt(self, prompt: str):
            """Simula análise de prompt"""
            class AnaliseResult:
                def __init__(self):
                    # Análise baseada na complexidade do prompt
                    palavras = len(prompt.split())
                    tem_ferramentas = "ferramenta" in prompt.lower() or "tool" in prompt.lower()
                    tem_recursos = "recurso" in prompt.lower() or "resource" in prompt.lower()
                    tem_tipos = "tipo" in prompt.lower() or "json" in prompt.lower()

                    self.pontuacao = min(10, 4 + (1 if tem_ferramentas else 0) +
                                         (1 if tem_recursos else 0) + (1 if tem_tipos else 0) +
                                         min(3, palavras // 10))

                    self.pontos_fortes = []
                    if tem_ferramentas:
                        self.pontos_fortes.append("Ferramentas especificadas")
                    if tem_recursos:
                        self.pontos_fortes.append("Recursos definidos")
                    if palavras > 20:
                        self.pontos_fortes.append("Descrição detalhada")

                    self.pontos_fracos = []
                    if not tem_tipos:
                        self.pontos_fracos.append(
                            "Tipos de dados não especificados")
                    if palavras < 10:
                        self.pontos_fracos.append("Descrição muito breve")
                    if "erro" not in prompt.lower():
                        self.pontos_fracos.append(
                            "Tratamento de erros não mencionado")

                    self.recomendacoes = []
                    if not tem_tipos:
                        self.recomendacoes.append(
                            "Adicione especificação de tipos")
                    if "teste" not in prompt.lower():
                        self.recomendacoes.append(
                            "Inclua estratégia de testes")
                    self.recomendacoes.append("Documente casos de uso")

            return AnaliseResult()

        def otimizar_prompt(self, prompt: str, framework: str = "CRISPE", contexto: str = ""):
            """Otimiza prompt usando framework especificado"""
            if framework.upper() == "CRISPE":
                return f"""**Contexto**: Desenvolvimento de servidor MCP{f' para {contexto}' if contexto else ''}
**Papel**: Você é um especialista em criação de servidores MCP
**Instrução**: {prompt}
**Especificações**: 
- Implemente ferramentas com tipos bem definidos
- Use recursos MCP apropriados  
- Inclua tratamento de erros robusto
- Forneça documentação clara
**Persona**: Desenvolvedor experiente em MCP e boas práticas
**Exemplos**: Baseado em padrões da documentação oficial MCP"""

            elif framework.upper() == "RACE":
                return f"""**Papel**: Especialista em servidores MCP
**Ação**: {prompt}
**Contexto**: {contexto if contexto else 'Sistema de produção empresarial'}
**Exemplo**: Implemente seguindo padrões estabelecidos da documentação MCP"""

            elif framework.upper() == "TRACE":
                return f"""**Tarefa**: {prompt}
**Requisitos**: Conformidade total com protocolo MCP
**Ação**: Implementar com ferramentas e recursos bem estruturados
**Contexto**: {contexto if contexto else 'Ambiente de desenvolvimento profissional'}
**Exemplo**: Siga exemplos da documentação oficial MCP"""

            return f"Prompt otimizado ({framework}): {prompt}"

        def aplicar_framework(self, prompt: str, framework: str):
            """Aplica framework específico"""
            return self.otimizar_prompt(prompt, framework)

        def criar_componente(self, tipo: str, config: dict):
            """Cria componente Tailwind CSS v4.1"""
            templates = {
                "button": lambda cfg: f'''<button class="px-4 py-2 bg-{cfg.get("cor", "blue")}-500 text-white rounded-lg hover:bg-{cfg.get("cor", "blue")}-600 active:bg-{cfg.get("cor", "blue")}-700 transition-colors duration-200 {cfg.get("classes", "")}">{cfg.get("texto", "Botão")}</button>''',

                "card": lambda cfg: f'''<div class="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 p-6 border border-gray-200 {cfg.get("classes", "")}">
    <h3 class="text-lg font-semibold text-gray-900 mb-2">{cfg.get("titulo", "Título do Card")}</h3>
    <p class="text-gray-600">{cfg.get("conteudo", "Conteúdo do card aqui...")}</p>
</div>''',

                "input": lambda cfg: f'''<input type="{cfg.get("tipo", "text")}" placeholder="{cfg.get("placeholder", "Digite aqui...")}" class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 user-valid:border-green-500 user-invalid:border-red-500 {cfg.get("classes", "")}" />''',

                "container": lambda cfg: f'''<div class="container mx-auto px-4 py-8 max-w-{cfg.get("largura", "7xl")} {cfg.get("classes", "")}">
    {cfg.get("conteudo", "<!-- Conteúdo do container -->")}
</div>'''
            }

            if tipo in templates:
                return templates[tipo](config)
            else:
                return f'<div class="modern-{tipo} {config.get("classes", "")}">{config.get("conteudo", f"Componente {tipo} moderno")}</div>'

        def gerar_servidor_completo(self, config: dict):
            """Gera código completo de servidor MCP"""
            nome = config.get("nome", "servidor_mcp")
            ferramentas = config.get("ferramentas", [])
            recursos = config.get("recursos", [])
            descricao = config.get("descricao", f"Servidor MCP: {nome}")

            codigo = f'''#!/usr/bin/env python3
"""
{descricao}
Gerado automaticamente pelo FastMCP Server Generator
"""

from fastmcp import FastMCP
from typing import Dict, List, Any, Optional
from pydantic import BaseModel
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializar servidor MCP
mcp = FastMCP("{nome}")

# Modelos de dados
class RequestModel(BaseModel):
    \"\"\"Modelo base para requisições\"\"\"
    pass

class ResponseModel(BaseModel):
    \"\"\"Modelo base para respostas\"\"\"
    success: bool
    message: str
    data: Optional[Dict[str, Any]] = None

# Implementação das ferramentas
'''

            for ferramenta in ferramentas:
                codigo += f'''
@mcp.tool()
def {ferramenta}(request: Dict[str, Any]) -> ResponseModel:
    \"\"\"
    Implementa a ferramenta: {ferramenta}
    
    Args:
        request: Dados da requisição
        
    Returns:
        ResponseModel: Resultado da operação
    \"\"\"
    try:
        # TODO: Implementar lógica da ferramenta {ferramenta}
        logger.info(f"Executando {ferramenta} com dados: {{request}}")
        
        return ResponseModel(
            success=True,
            message=f"Ferramenta {ferramenta} executada com sucesso",
            data={{"resultado": "placeholder"}}
        )
    except Exception as e:
        logger.error(f"Erro em {ferramenta}: {{e}}")
        return ResponseModel(
            success=False,
            message=f"Erro ao executar {ferramenta}: {{str(e)}}"
        )
'''

            for recurso in recursos:
                codigo += f'''
@mcp.resource("{recurso}")
def get_{recurso.replace("://", "_").replace("/", "_")}() -> Dict[str, Any]:
    \"\"\"
    Fornece acesso ao recurso: {recurso}
    
    Returns:
        Dict: Dados do recurso
    \"\"\"
    # TODO: Implementar acesso ao recurso {recurso}
    return {{
        "resource_type": "{recurso}",
        "data": "placeholder_data",
        "timestamp": "2025-05-25T15:45:00Z"
    }}
'''

            codigo += f'''
if __name__ == "__main__":
    logger.info("Iniciando servidor {nome}...")
    mcp.run()
'''

            return codigo

        def gerar_template_servidor(self, nome: str, ferramentas: List[str]):
            """Gera template básico de servidor"""
            return self.gerar_servidor_completo({{
                "nome": nome,
                "ferramentas": ferramentas,
                "descricao": f"Template de servidor MCP: {nome}"
            }})

except ImportError as e:
    print(f"❌ Erro ao importar dependências: {e}")
    print("🔧 Certifique-se de estar no diretório correto do projeto")
    sys.exit(1)


class MCPServersCLI:
    """Interface de linha de comando para os servidores MCP"""

    def __init__(self):
        """Inicializa os servidores MCP"""
        self.analisador = MCPServerCLIWrapper("mcp_server")
        self.prompt_engineer = MCPServerCLIWrapper("prompt_server")
        self.tailwind_server = MCPServerCLIWrapper("tailwind_server")
        self.fastmcp_server = MCPServerCLIWrapper("fastmcp_server")

    def analyze_prompt(self, prompt: str, detailed: bool = False) -> Dict:
        """Analisa um prompt usando o Servidor de Análise MCP"""
        print(f"🔍 Analisando prompt: {prompt[:50]}...")

        resultado = self.analisador.analisar_prompt(prompt)

        output = {
            "pontuacao": resultado.pontuacao,
            "pontos_fortes": resultado.pontos_fortes,
            "pontos_fracos": resultado.pontos_fracos,
            "recomendacoes": resultado.recomendacoes
        }

        if detailed:
            self._print_detailed_analysis(resultado)
        else:
            self._print_analysis_summary(resultado)

        return output

    def optimize_prompt(self, prompt: str, framework: str = "CRISPE",
                        contexto: str = "") -> str:
        """Otimiza um prompt usando o Servidor de Engenharia de Prompts"""
        print(f"📝 Otimizando prompt com framework {framework}...")

        if framework.upper() in ["CRISPE", "RACE", "TRACE"]:
            prompt_otimizado = self.prompt_engineer.aplicar_framework(
                prompt, framework)
        else:
            prompt_otimizado = self.prompt_engineer.otimizar_prompt(
                prompt, contexto=contexto)

        print(f"✅ Prompt otimizado ({len(prompt_otimizado)} caracteres):")
        print("-" * 50)
        print(prompt_otimizado)
        print("-" * 50)

        return prompt_otimizado

    def create_tailwind_component(self, tipo: str, config_str: str = "{}") -> str:
        """Cria um componente Tailwind CSS v4.1"""
        try:
            config = json.loads(config_str)
        except json.JSONDecodeError:
            print("❌ Erro: Configuração JSON inválida")
            return ""

        print(f"🎨 Criando componente Tailwind: {tipo}")

        componente = self.tailwind_server.criar_componente(tipo, config)

        print(f"✅ Componente criado:")
        print("-" * 50)
        print(componente)
        print("-" * 50)

        return componente

    def generate_fastmcp_server(self, nome: str, tools_str: str = "[]",
                                resources_str: str = "[]") -> str:
        """Gera um servidor FastMCP"""
        try:
            tools = json.loads(tools_str)
            resources = json.loads(resources_str)
        except json.JSONDecodeError:
            print("❌ Erro: JSON inválido para tools ou resources")
            return ""

        print(f"⚡ Gerando servidor FastMCP: {nome}")

        config = {
            "nome": nome,
            "ferramentas": tools,
            "recursos": resources
        }

        codigo = self.fastmcp_server.gerar_servidor_completo(config)

        # Salvar o código gerado
        filename = f"generated_{nome}.py"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(codigo)

        print(f"✅ Servidor gerado e salvo em: {filename}")
        print(f"📄 Linhas de código: {len(codigo.split('\n'))}")

        return codigo

    def run_integration_workflow(self, project_name: str):
        """Executa um workflow de integração completo"""
        print(f"🚀 Executando workflow integrado para: {project_name}")
        print("=" * 60)

        # Etapa 1: Análise inicial
        prompt_inicial = f"Criar um servidor MCP para {project_name}"
        analise_inicial = self.analyze_prompt(prompt_inicial)

        # Etapa 2: Otimização
        prompt_otimizado = self.optimize_prompt(prompt_inicial, "CRISPE")

        # Etapa 3: Componente de interface
        componente = self.create_tailwind_component(
            "container",
            '{"estilo": "moderno", "versao": "v4.1"}'
        )

        # Etapa 4: Servidor MCP
        servidor = self.generate_fastmcp_server(
            f"{project_name.lower()}_server",
            '["main_action", "get_data", "update_status"]',
            '["data://main", "config://settings"]'
        )

        print("\n🎉 Workflow integrado concluído!")
        print(f"📊 Pontuação do prompt: {analise_inicial['pontuacao']}/10")
        print(f"🎨 Componente Tailwind: Criado")
        print(f"⚡ Servidor MCP: generated_{project_name.lower()}_server.py")

    def _print_analysis_summary(self, resultado):
        """Imprime resumo da análise"""
        print(f"📊 Pontuação: {resultado.pontuacao}/10")
        print(f"✅ Pontos fortes: {', '.join(resultado.pontos_fortes[:3])}")
        print(f"⚠️  Melhorias: {', '.join(resultado.pontos_fracos[:2])}")
        print(f"💡 Recomendações: {len(resultado.recomendacoes)} sugestões")

    def _print_detailed_analysis(self, resultado):
        """Imprime análise detalhada"""
        print("=" * 60)
        print(f"📊 PONTUAÇÃO: {resultado.pontuacao}/10")
        print("=" * 60)

        print("\n✅ PONTOS FORTES:")
        for ponto in resultado.pontos_fortes:
            print(f"   • {ponto}")

        print("\n⚠️  PONTOS DE MELHORIA:")
        for ponto in resultado.pontos_fracos:
            print(f"   • {ponto}")

        print("\n💡 RECOMENDAÇÕES:")
        for rec in resultado.recomendacoes:
            print(f"   • {rec}")
        print("=" * 60)


def create_parser():
    """Cria o parser de argumentos da CLI"""
    parser = argparse.ArgumentParser(
        description="🛠️ MCP Servers CLI - Interface unificada para servidores MCP",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:

  Análise de prompts:
    python mcp_cli.py analyze "Criar servidor para e-commerce"
    python mcp_cli.py analyze "Prompt complexo..." --detailed
  
  Otimização de prompts:
    python mcp_cli.py optimize "Prompt original" --framework CRISPE
    python mcp_cli.py optimize "Prompt original" --contexto "desenvolvimento_web"
  
  Componentes Tailwind:
    python mcp_cli.py tailwind button '{"cor": "blue", "tamanho": "lg"}'
    python mcp_cli.py tailwind card '{"titulo": "Dashboard", "estilo": "v4.1"}'
  
  Geração de servidores:
    python mcp_cli.py fastmcp meu_servidor '["tool1", "tool2"]' '["resource1://data"]'
  
  Workflow integrado:
    python mcp_cli.py workflow "Sistema de Vendas"
        """
    )

    subparsers = parser.add_subparsers(
        dest='command', help='Comandos disponíveis')

    # Comando analyze
    analyze_parser = subparsers.add_parser('analyze', help='Analisar prompt')
    analyze_parser.add_argument('prompt', help='Prompt para analisar')
    analyze_parser.add_argument('--detailed', action='store_true',
                                help='Análise detalhada')

    # Comando optimize
    optimize_parser = subparsers.add_parser('optimize', help='Otimizar prompt')
    optimize_parser.add_argument('prompt', help='Prompt para otimizar')
    optimize_parser.add_argument('--framework', choices=['CRISPE', 'RACE', 'TRACE'],
                                 default='CRISPE', help='Framework de otimização')
    optimize_parser.add_argument('--contexto', help='Contexto adicional')

    # Comando tailwind
    tailwind_parser = subparsers.add_parser(
        'tailwind', help='Criar componente Tailwind')
    tailwind_parser.add_argument(
        'tipo', help='Tipo do componente (button, card, etc.)')
    tailwind_parser.add_argument('config', nargs='?', default='{}',
                                 help='Configuração JSON do componente')

    # Comando fastmcp
    fastmcp_parser = subparsers.add_parser(
        'fastmcp', help='Gerar servidor FastMCP')
    fastmcp_parser.add_argument('nome', help='Nome do servidor')
    fastmcp_parser.add_argument('tools', nargs='?', default='[]',
                                help='Lista JSON de ferramentas')
    fastmcp_parser.add_argument('resources', nargs='?', default='[]',
                                help='Lista JSON de recursos')

    # Comando workflow
    workflow_parser = subparsers.add_parser(
        'workflow', help='Executar workflow integrado')
    workflow_parser.add_argument('projeto', help='Nome do projeto')

    return parser


def main():
    """Função principal da CLI"""
    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    print(f"🛠️ MCP Servers CLI - {datetime.now().strftime('%H:%M:%S')}")
    print("=" * 60)

    try:
        cli = MCPServersCLI()

        if args.command == 'analyze':
            cli.analyze_prompt(args.prompt, args.detailed)

        elif args.command == 'optimize':
            cli.optimize_prompt(args.prompt, args.framework, args.contexto)

        elif args.command == 'tailwind':
            cli.create_tailwind_component(args.tipo, args.config)

        elif args.command == 'fastmcp':
            cli.generate_fastmcp_server(args.nome, args.tools, args.resources)

        elif args.command == 'workflow':
            cli.run_integration_workflow(args.projeto)

    except KeyboardInterrupt:
        print("\n\n⏹️  Operação cancelada pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        print("🔧 Use --help para ver os comandos disponíveis")


if __name__ == "__main__":
    main()
