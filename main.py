#!/usr/bin/env python3
"""
MCP Servers - Main Launcher
===========================

Launcher for specialized MCP servers:
- MCP Server: MCP prompt analysis
- Prompt Server: Prompt engineering
- Tailwind Server: Tailwind CSS v4.1 support
- FastMCP Server: High-performance server
- React Server: React components
- TypeScript Server: TypeScript analysis

Usage:
    python main.py [server] [options]
    
    Available servers:
    - mcp: MCP prompt analysis server
    - prompt: Prompt engineering server  
    - tailwind: Tailwind CSS server
    - fastmcp: FastMCP server
    - react: React server
    - typescript: TypeScript server
    - react_optimizer: React Optimizer server (analysis + optimization)
    - shadcn: Advanced shadcn/ui server
    - rust: Advanced Rust server
    - axum: Axum web framework server
    - all: Run all servers (development mode)
    
Examples:
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

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Server configurations
SERVERS_CONFIG = {
    "mcp": {
        "name": "MCP Analysis Server",
        "description": "Server for MCP prompt analysis",
        "module": "servers.mcp_server",
        "port": 3000,
        "protocol": "stdio"
    },
    "prompt": {
        "name": "Prompt Engineering Server",
        "description": "Server for prompt engineering",
        "module": "servers.prompt_server",
        "port": 3001,
        "protocol": "stdio"
    },
    "tailwind": {
        "name": "Tailwind CSS Server",
        "description": "Server for Tailwind CSS v4.1",
        "module": "servers.tailwind_server",
        "port": 3002,
        "protocol": "stdio"
    },
    "fastmcp": {
        "name": "FastMCP Server",
        "description": "High-performance FastMCP server",
        "module": "servers.fastmcp_server",
        "port": 3003,
        "protocol": "stdio"
    },
    "react": {
        "name": "React Components Server",
        "description": "Server for React components",
        "module": "servers.react_server",
        "port": 3004,
        "protocol": "stdio"
    },
    "typescript": {
        "name": "TypeScript Analysis Server",
        "description": "Server for TypeScript analysis",
        "module": "servers.typescript_server",
        "port": 3005,
        "protocol": "stdio"
    },
    "react_optimizer": {
        "name": "React Optimizer Server",
        "description": "Server for React code analysis and optimization + prompts",
        "module": "servers.react_optimizer_server",
        "port": 3006,
        "protocol": "stdio"
    },
    "shadcn": {
        "name": "shadcn/ui Advanced Server",
        "description": "Advanced server for shadcn/ui components with intelligent analysis",
        "module": "servers.shadcn_server",
        "port": 3007,
        "protocol": "stdio"
    },
    "rust": {
        "name": "Rust Idiomatic Server",
        "description": "MCP server for idiomatic Rust development following mre/idiomatic-rust",
        "module": "servers.rust_server",
        "port": 3008,
        "protocol": "stdio"
    },
    "axum": {
        "name": "Axum Web Framework Server",
        "description": "MCP server for development with Axum web framework (tokio-rs + magic patterns)",
        "module": "servers.axum_server",
        "port": 3009,
        "protocol": "stdio"
    }
}


class ServerManager:
    """MCP server manager"""

    def __init__(self):
        self.running_servers: Dict[str, subprocess.Popen] = {}
        self.project_root = Path(__file__).parent

    def list_servers(self) -> None:
        """List all available servers"""
        print("\n🚀 Available MCP Servers:")
        print("=" * 50)

        for server_id, config in SERVERS_CONFIG.items():
            module_path = str(config.get('module', ''))
            server_file = self.project_root / \
                f"{module_path.replace('.', '/')}.py"
            status = "✅ Available" if server_file.exists() else "❌ Not found"
            print(f"  {server_id:12} - {config['name']}")
            print(f"  {'':12}   {config['description']}")
            print(f"  {'':12}   Port: {config['port']} | Status: {status}")
            print()

    def validate_server(self, server_id: str) -> bool:
        """Validate if a server exists and can be executed"""
        if server_id not in SERVERS_CONFIG:
            logger.error(f"Server '{server_id}' not found")
            return False

        config = SERVERS_CONFIG[server_id]
        module_path = str(config.get('module', ''))
        server_file = self.project_root / \
            f"{module_path.replace('.', '/')}.py"

        if not server_file.exists():
            logger.error(f"Server file not found: {server_file}")
            return False

        return True
        return True

    async def start_server(self, server_id: str, args: argparse.Namespace) -> bool:
        """Start a specific server"""
        if not self.validate_server(server_id):
            return False

        config = SERVERS_CONFIG[server_id]
        module_path = config['module']

        try:
            logger.info(f"Starting {config['name']}...")

            # Command to execute the server
            cmd = [
                "uv", "run", "python", "-m", str(module_path)
            ]

            # Add specific arguments if provided
            if hasattr(args, 'port') and args.port:
                config['port'] = args.port

            # Define environment variables
            env = os.environ.copy()
            env['MCP_SERVER_PORT'] = str(config['port'])
            env['MCP_SERVER_PROTOCOL'] = str(config['protocol'])

            # Execute the server
            process = subprocess.Popen(
                cmd,
                cwd=str(self.project_root),
                env=env,
                stdout=subprocess.PIPE if args.quiet else None,
                stderr=subprocess.PIPE if args.quiet else None
            )

            self.running_servers[server_id] = process

            # Wait a bit to check if the process started correctly
            await asyncio.sleep(1)

            if process.poll() is None:
                logger.info(
                    f"✅ {config['name']} started successfully (PID: {process.pid})")
                if not args.quiet:
                    print(f"📡 Server running on port {config['port']}")
                return True
            else:
                logger.error(f"❌ Failed to start {config['name']}")
                return False

        except Exception as e:
            logger.error(f"Error starting server {server_id}: {e}")
            return False

    async def start_all_servers(self, args: argparse.Namespace) -> None:
        """Start all servers in development mode"""
        logger.info(
            "🚀 Starting all servers in development mode...")

        successful_starts = []
        failed_starts = []

        for server_id in SERVERS_CONFIG.keys():
            if await self.start_server(server_id, args):
                successful_starts.append(server_id)
            else:
                failed_starts.append(server_id)

        print(f"\n📊 Launch Summary:")
        print(
            f"  ✅ Successes: {len(successful_starts)} - {', '.join(successful_starts)}")
        if failed_starts:
            print(
                f"  ❌ Failures: {len(failed_starts)} - {', '.join(failed_starts)}")

        if successful_starts:
            print(f"\n🔄 Servers running. Press Ctrl+C to stop all.")
            try:
                # Keep servers running
                while True:
                    await asyncio.sleep(1)
                    # Check if any process died
                    for server_id in list(self.running_servers.keys()):
                        process = self.running_servers[server_id]
                        if process.poll() is not None:
                            logger.warning(
                                f"Server {server_id} stopped unexpectedly")
                            del self.running_servers[server_id]
            except KeyboardInterrupt:
                logger.info(
                    "Received interruption signal, stopping servers...")

    def stop_all_servers(self) -> None:
        """Stop all running servers"""
        if not self.running_servers:
            logger.info("No servers running")
            return

        logger.info("Stopping all servers...")

        for server_id, process in self.running_servers.items():
            try:
                logger.info(f"Stopping {SERVERS_CONFIG[server_id]['name']}...")
                process.terminate()

                # Wait for graceful termination
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    logger.warning(f"Forcing stop of {server_id}...")
                    process.kill()
                    process.wait()

                logger.info(f"✅ {server_id} stopped")
            except Exception as e:
                logger.error(f"Error stopping {server_id}: {e}")

        self.running_servers.clear()
        logger.info("All servers have been stopped")


def setup_signal_handlers(manager: ServerManager) -> None:
    """Configure signal handlers for graceful shutdown"""
    def signal_handler(signum, frame):
        logger.info(f"Received signal {signum}, stopping servers...")
        manager.stop_all_servers()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser"""
    parser = argparse.ArgumentParser(
        description="Launcher for specialized MCP servers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Usage examples:
  python main.py list                    # List available servers
  python main.py mcp                     # Start MCP server
  python main.py prompt --port 3001     # Start Prompt server on port 3001
  python main.py all --dev              # Start all servers
  python main.py tailwind --quiet       # Start Tailwind in quiet mode
        """
    )

    parser.add_argument(
        "server",
        nargs="?",
        choices=list(SERVERS_CONFIG.keys()) + ["all", "list"],
        default="list",
        help="Server to run or 'all' for all servers"
    )

    parser.add_argument(
        "--port", "-p",
        type=int,
        help="Custom port for the server"
    )

    parser.add_argument(
        "--dev",
        action="store_true",
        help="Development mode (more logs)"
    )

    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Quiet mode (fewer logs)"
    )

    parser.add_argument(
        "--version", "-v",
        action="version",
        version="MCP Servers v0.1.0"
    )

    return parser


async def main() -> None:
    """Main function"""
    parser = create_parser()
    args = parser.parse_args()

    # Configure logging level based on arguments
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
            # Start specific server
            success = await manager.start_server(args.server, args)
            if success and not args.quiet:
                print(
                    f"\n🔄 Server {args.server} running. Press Ctrl+C to stop.")
                try:
                    while True:
                        await asyncio.sleep(1)
                        # Check if the process is still running
                        process = manager.running_servers.get(args.server)
                        if process and process.poll() is not None:
                            logger.error(
                                f"Server {args.server} stopped unexpectedly")
                            break
                except KeyboardInterrupt:
                    logger.info("Stopping server...")
            elif not success:
                sys.exit(1)

    except KeyboardInterrupt:
        logger.info("Operation cancelled by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)
    finally:
        manager.stop_all_servers()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Program interrupted")
        sys.exit(0)
