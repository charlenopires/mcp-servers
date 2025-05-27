#!/usr/bin/env python3
"""
MCP Servers - Launcher Principal
=====================================

Launcher para os servidores MCP especializados:
- MCP Server: Análise de prompts MCP
- Prompt Server: Engenharia de prompts
- Tailwind Server: Suporte ao Tailwind CSS v4.1
- FastMCP Server: Servidor de alta performance
- React Server: Componentes React
- TypeScript Server: Análise TypeScript

Uso:
    python main.py [servidor] [opções]
    
    Servidores disponíveis:
    - mcp: Servidor de análise de prompts MCP
    - prompt: Servidor de engenharia de prompts  
    - tailwind: Servidor Tailwind CSS
    - fastmcp: Servidor FastMCP
    - react: Servidor React
    - typescript: Servidor TypeScript
    - react_optimizer: Servidor React Optimizer (análise + otimização)
    - all: Executar todos os servidores (modo desenvolvimento)
    
Exemplos:
    python main.py mcp
    python main.py prompt --port 3001
    python main.py all --dev
"""

import argparse
import asyncio
import logging
import signal
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any
import subprocess
import time
import json
import os

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configurações dos servidores
SERVERS_CONFIG = {
    "mcp": {
        "name": "MCP Analysis Server",
        "description": "Servidor para análise de prompts MCP",
        "module": "servers.mcp_server",
        "port": 3000,
        "protocol": "stdio"
    },
    "prompt": {
        "name": "Prompt Engineering Server",
        "description": "Servidor para engenharia de prompts",
        "module": "servers.prompt_server",
        "port": 3001,
        "protocol": "stdio"
    },
    "tailwind": {
        "name": "Tailwind CSS Server",
        "description": "Servidor para Tailwind CSS v4.1",
        "module": "servers.tailwind_server",
        "port": 3002,
        "protocol": "stdio"
    },
    "fastmcp": {
        "name": "FastMCP Server",
        "description": "Servidor FastMCP de alta performance",
        "module": "servers.fastmcp_server",
        "port": 3003,
        "protocol": "stdio"
    },
    "react": {
        "name": "React Components Server",
        "description": "Servidor para componentes React",
        "module": "servers.react_server",
        "port": 3004,
        "protocol": "stdio"
    },
    "typescript": {
        "name": "TypeScript Analysis Server",
        "description": "Servidor para análise TypeScript",
        "module": "servers.typescript_server",
        "port": 3005,
        "protocol": "stdio"
    },
    "react_optimizer": {
        "name": "React Optimizer Server",
        "description": "Servidor para análise e otimização de código React + prompts",
        "module": "servers.react_optimizer_server",
        "port": 3006,
        "protocol": "stdio"
    }
}


class ServerManager:
    """Gerenciador de servidores MCP"""

    def __init__(self):
        self.running_servers: Dict[str, subprocess.Popen] = {}
        self.project_root = Path(__file__).parent

    def list_servers(self) -> None:
        """Lista todos os servidores disponíveis"""
        print("\n🚀 Servidores MCP Disponíveis:")
        print("=" * 50)

        for server_id, config in SERVERS_CONFIG.items():
            module_path = str(config.get('module', ''))
            server_file = self.project_root / \
                f"{module_path.replace('.', '/')}.py"
            status = "✅ Disponível" if server_file.exists() else "❌ Não encontrado"
            print(f"  {server_id:12} - {config['name']}")
            print(f"  {'':12}   {config['description']}")
            print(f"  {'':12}   Porta: {config['port']} | Status: {status}")
            print()

    def validate_server(self, server_id: str) -> bool:
        """Valida se um servidor existe e pode ser executado"""
        if server_id not in SERVERS_CONFIG:
            logger.error(f"Servidor '{server_id}' não encontrado")
            return False

        config = SERVERS_CONFIG[server_id]
        module_path = str(config.get('module', ''))
        server_file = self.project_root / \
            f"{module_path.replace('.', '/')}.py"

        if not server_file.exists():
            logger.error(f"Arquivo do servidor não encontrado: {server_file}")
            return False

        return True
        return True

    async def start_server(self, server_id: str, args: argparse.Namespace) -> bool:
        """Inicia um servidor específico"""
        if not self.validate_server(server_id):
            return False

        config = SERVERS_CONFIG[server_id]
        module_path = config['module']

        try:
            logger.info(f"Iniciando {config['name']}...")

            # Comando para executar o servidor
            cmd = [
                str(sys.executable), "-m", str(module_path)
            ]

            # Adicionar argumentos específicos se fornecidos
            if hasattr(args, 'port') and args.port:
                config['port'] = args.port

            # Definir variáveis de ambiente
            env = os.environ.copy()
            env['MCP_SERVER_PORT'] = str(config['port'])
            env['MCP_SERVER_PROTOCOL'] = str(config['protocol'])

            # Executar o servidor
            process = subprocess.Popen(
                cmd,
                cwd=str(self.project_root),
                env=env,
                stdout=subprocess.PIPE if args.quiet else None,
                stderr=subprocess.PIPE if args.quiet else None
            )

            self.running_servers[server_id] = process

            # Aguardar um pouco para verificar se o processo iniciou corretamente
            await asyncio.sleep(1)

            if process.poll() is None:
                logger.info(
                    f"✅ {config['name']} iniciado com sucesso (PID: {process.pid})")
                if not args.quiet:
                    print(f"📡 Servidor rodando na porta {config['port']}")
                return True
            else:
                logger.error(f"❌ Falha ao iniciar {config['name']}")
                return False

        except Exception as e:
            logger.error(f"Erro ao iniciar servidor {server_id}: {e}")
            return False

    async def start_all_servers(self, args: argparse.Namespace) -> None:
        """Inicia todos os servidores em modo desenvolvimento"""
        logger.info(
            "🚀 Iniciando todos os servidores em modo desenvolvimento...")

        successful_starts = []
        failed_starts = []

        for server_id in SERVERS_CONFIG.keys():
            if await self.start_server(server_id, args):
                successful_starts.append(server_id)
            else:
                failed_starts.append(server_id)

        print(f"\n📊 Resumo do Lançamento:")
        print(
            f"  ✅ Sucessos: {len(successful_starts)} - {', '.join(successful_starts)}")
        if failed_starts:
            print(
                f"  ❌ Falhas: {len(failed_starts)} - {', '.join(failed_starts)}")

        if successful_starts:
            print(f"\n🔄 Servidores em execução. Pressione Ctrl+C para parar todos.")
            try:
                # Manter os servidores rodando
                while True:
                    await asyncio.sleep(1)
                    # Verificar se algum processo morreu
                    for server_id in list(self.running_servers.keys()):
                        process = self.running_servers[server_id]
                        if process.poll() is not None:
                            logger.warning(
                                f"Servidor {server_id} parou inesperadamente")
                            del self.running_servers[server_id]
            except KeyboardInterrupt:
                logger.info(
                    "Recebido sinal de interrupção, parando servidores...")

    def stop_all_servers(self) -> None:
        """Para todos os servidores em execução"""
        if not self.running_servers:
            logger.info("Nenhum servidor em execução")
            return

        logger.info("Parando todos os servidores...")

        for server_id, process in self.running_servers.items():
            try:
                logger.info(f"Parando {SERVERS_CONFIG[server_id]['name']}...")
                process.terminate()

                # Aguardar término gracioso
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    logger.warning(f"Forçando parada de {server_id}...")
                    process.kill()
                    process.wait()

                logger.info(f"✅ {server_id} parado")
            except Exception as e:
                logger.error(f"Erro ao parar {server_id}: {e}")

        self.running_servers.clear()
        logger.info("Todos os servidores foram parados")


def setup_signal_handlers(manager: ServerManager) -> None:
    """Configura handlers de sinal para parada graciosoa"""
    def signal_handler(signum, frame):
        logger.info(f"Recebido sinal {signum}, parando servidores...")
        manager.stop_all_servers()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)


def create_parser() -> argparse.ArgumentParser:
    """Cria o parser de argumentos"""
    parser = argparse.ArgumentParser(
        description="Launcher para servidores MCP especializados",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python main.py list                    # Lista servidores disponíveis
  python main.py mcp                     # Inicia servidor MCP
  python main.py prompt --port 3001     # Inicia servidor Prompt na porta 3001
  python main.py all --dev              # Inicia todos os servidores
  python main.py tailwind --quiet       # Inicia Tailwind em modo silencioso
        """
    )

    parser.add_argument(
        "server",
        nargs="?",
        choices=list(SERVERS_CONFIG.keys()) + ["all", "list"],
        default="list",
        help="Servidor para executar ou 'all' para todos"
    )

    parser.add_argument(
        "--port", "-p",
        type=int,
        help="Porta personalizada para o servidor"
    )

    parser.add_argument(
        "--dev",
        action="store_true",
        help="Modo desenvolvimento (mais logs)"
    )

    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Modo silencioso (menos logs)"
    )

    parser.add_argument(
        "--version", "-v",
        action="version",
        version="MCP Servers v0.1.0"
    )

    return parser


async def main() -> None:
    """Função principal"""
    parser = create_parser()
    args = parser.parse_args()

    # Configurar nível de logging baseado nos argumentos
    if args.dev:
        logging.getLogger().setLevel(logging.DEBUG)
    elif args.quiet:
        logging.getLogger().setLevel(logging.WARNING)

    manager = ServerManager()
    setup_signal_handlers(manager)

    try:
        if args.server == "list":
            manager.list_servers()

        elif args.server == "all":
            await manager.start_all_servers(args)

        else:
            # Iniciar servidor específico
            success = await manager.start_server(args.server, args)
            if success and not args.quiet:
                print(
                    f"\n🔄 Servidor {args.server} em execução. Pressione Ctrl+C para parar.")
                try:
                    while True:
                        await asyncio.sleep(1)
                        # Verificar se o processo ainda está rodando
                        process = manager.running_servers.get(args.server)
                        if process and process.poll() is not None:
                            logger.error(
                                f"Servidor {args.server} parou inesperadamente")
                            break
                except KeyboardInterrupt:
                    logger.info("Parando servidor...")
            elif not success:
                sys.exit(1)

    except KeyboardInterrupt:
        logger.info("Operação cancelada pelo usuário")
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        sys.exit(1)
    finally:
        manager.stop_all_servers()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Programa interrompido")
        sys.exit(0)
