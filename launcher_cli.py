#!/usr/bin/env python3
"""
MCP Servers Interactive CLI Launcher
===================================

Modern interactive CLI launcher using PyInquirer for multiple server selection.
Similar to Vue CLI experience with checkbox selection and rich formatting.

Features:
- Multi-select servers with checkboxes
- Rich colored output with icons
- Server status validation
- Parallel execution support
- Development/production modes

Usage:
    uv run mcp_servers                (recommended)
    python launcher_cli.py            (alternative)
    uv run python launcher_cli.py     (alternative)
"""

import asyncio
import logging
import os
import signal
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any
import time

try:
    import questionary
    import colorama
    from colorama import Fore, Back, Style
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.layout import Layout
    from rich.text import Text
except ImportError as e:
    print(f"❌ Missing required dependencies: {e}")
    print("💡 Install with: uv sync")
    sys.exit(1)

# Initialize colorama for cross-platform color support
colorama.init()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Rich console for beautiful output
console = Console()

# Server configurations (imported from main.py structure)
SERVERS_CONFIG = {
    "mcp": {
        "name": "MCP Analysis Server",
        "description": "MCP prompt analysis and validation",
        "emoji": "🔍",
        "category": "Analysis",
        "port": 3000,
        "module": "servers.mcp_server",
        "status": "functional"
    },
    "prompt": {
        "name": "Prompt Engineering Server", 
        "description": "Advanced prompt optimization techniques",
        "emoji": "✏️",
        "category": "Analysis",
        "port": 3001,
        "module": "servers.prompt_server",
        "status": "functional"
    },
    "tailwind": {
        "name": "Tailwind CSS Server",
        "description": "Tailwind CSS v4.1 support and migration",
        "emoji": "🎨",
        "category": "Frontend",
        "port": 3002,
        "module": "servers.tailwind_server",
        "status": "functional"
    },
    "fastmcp": {
        "name": "FastMCP Server",
        "description": "Meta-server for MCP development",
        "emoji": "⚡",
        "category": "Analysis", 
        "port": 3003,
        "module": "servers.fastmcp_server",
        "status": "functional"
    },
    "react": {
        "name": "React Components Server",
        "description": "React 19 development support",
        "emoji": "⚛️",
        "category": "Frontend",
        "port": 3004,
        "module": "servers.react_server", 
        "status": "functional"
    },
    "react_optimizer": {
        "name": "React Optimizer Server",
        "description": "React code analysis and AI prompt optimization",
        "emoji": "🚀",
        "category": "Frontend",
        "port": 3006,
        "module": "servers.react_optimizer_server",
        "status": "functional"
    },
    "shadcn": {
        "name": "shadcn/ui Server",
        "description": "Advanced shadcn/ui component development",
        "emoji": "🧩",
        "category": "Frontend",
        "port": 3007,
        "module": "servers.shadcn_server",
        "status": "functional"
    },
    "rust": {
        "name": "Rust Idiomatic Server",
        "description": "Idiomatic Rust development patterns",
        "emoji": "🦀",
        "category": "Backend",
        "port": 3008,
        "module": "servers.rust_server",
        "status": "functional"
    },
    "axum": {
        "name": "Axum Web Framework Server",
        "description": "Axum web development with tokio",
        "emoji": "🌐",
        "category": "Backend",
        "port": 3009,
        "module": "servers.axum_server",
        "status": "functional"
    },
    "docker": {
        "name": "Docker Optimizer Server",
        "description": "Docker containerization with security best practices",
        "emoji": "🐳",
        "category": "DevOps",
        "port": 3010,
        "module": "servers.docker_optimizer_server",
        "status": "functional"
    },
    "typescript": {
        "name": "TypeScript Analysis Server",
        "description": "TypeScript code analysis and optimization",
        "emoji": "🔷",
        "category": "Backend",
        "port": 3005,
        "module": "servers.typescript_server",
        "status": "development"
    }
}

def validate_server_selection(servers):
    """Validator for server selection"""
    if len(servers) == 0:
        return "Please select at least one server"
    return True


class MCPLauncherCLI:
    """Modern MCP Servers CLI Launcher"""
    
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.running_servers: Dict[str, subprocess.Popen] = {}
        self.selected_servers: List[str] = []
        
    def show_banner(self):
        """Show application banner"""
        console.print()
        banner_panel = Panel.fit(
            "[bold blue]🚀 MCP SERVERS LAUNCHER CLI[/bold blue]\n"
            "[dim]Interactive Multi-Server Selection Interface[/dim]\n"
            "[green]10/11 Servers Available[/green] • [yellow]Powered by FastMCP 2.0[/yellow]",
            title="[bold cyan]Welcome[/bold cyan]",
            border_style="blue",
            padding=(1, 2)
        )
        console.print(banner_panel)
        console.print()

    def validate_server_files(self) -> Dict[str, bool]:
        """Validate if server files exist"""
        validation_results = {}
        
        for server_id, config in SERVERS_CONFIG.items():
            module_path = config['module']
            server_file = self.project_root / f"{module_path.replace('.', '/')}.py"
            validation_results[server_id] = server_file.exists()
            
        return validation_results

    def show_server_status(self):
        """Show detailed server status table"""
        console.print("[bold cyan]📊 Server Status Overview[/bold cyan]")
        console.print()
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Server", style="cyan", no_wrap=True)
        table.add_column("Name", style="white") 
        table.add_column("Category", style="yellow")
        table.add_column("Port", style="green")
        table.add_column("Status", style="bold")
        
        validation_results = self.validate_server_files()
        
        for server_id, config in SERVERS_CONFIG.items():
            status_color = "green" if validation_results[server_id] else "red"
            status_text = "✅ Available" if validation_results[server_id] else "❌ Not Found"
            
            if config['status'] == 'development':
                status_color = "yellow"
                status_text = "🚧 Development"
                
            table.add_row(
                f"{config['emoji']} {server_id}",
                config['name'],
                config['category'],
                str(config['port']),
                f"[{status_color}]{status_text}[/{status_color}]"
            )
        
        console.print(table)
        console.print()

    def get_server_choices(self) -> List[questionary.Choice]:
        """Generate server choices for questionary"""
        validation_results = self.validate_server_files()
        choices = []
        
        # Add "Start All Servers" option at the top
        available_servers = [sid for sid, available in validation_results.items() 
                           if available and SERVERS_CONFIG[sid]['status'] == 'functional']
        
        choices.append(questionary.Choice(
            title="🚀 START ALL SERVERS\n    Launch all available functional servers simultaneously",
            value="__ALL_SERVERS__",
            disabled=len(available_servers) == 0
        ))
        
        choices.append(questionary.Separator())
        choices.append(questionary.Separator('── Individual Servers ──'))
        
        # Group by category
        categories = {}
        for server_id, config in SERVERS_CONFIG.items():
            category = config['category']
            if category not in categories:
                categories[category] = []
            categories[category].append((server_id, config))
        
        # Add choices by category
        for category, servers in categories.items():
            if len(choices) > 3:  # Account for the "Start All" option and separators
                choices.append(questionary.Separator())
                
            choices.append(questionary.Separator(f'── {category} Servers ──'))
            
            for server_id, config in servers:
                disabled = False
                suffix = ""
                
                if not validation_results[server_id]:
                    disabled = True
                    suffix = " [NOT FOUND]"
                elif config['status'] == 'development':
                    suffix = " [DEV]"
                
                choice_name = f"{config['emoji']} {config['name']}{suffix}"
                choice_desc = f"{config['description']} (Port: {config['port']})"
                
                choices.append(questionary.Choice(
                    title=f"{choice_name}\n    {choice_desc}",
                    value=server_id,
                    disabled=disabled
                ))
        
        return choices

    async def prompt_server_selection(self) -> List[str]:
        """Prompt user for server selection"""
        console.print("[bold yellow]🎯 Server Selection[/bold yellow]")
        console.print("[dim]Use ↑↓ to navigate, SPACE to select, ENTER to confirm[/dim]")
        console.print()
        
        selected_servers = await questionary.checkbox(
            "Please select the servers you want to run:",
            choices=self.get_server_choices(),
            validate=validate_server_selection,
            qmark="🎯",
            instruction="(Use arrow keys to navigate, SPACE to select, ENTER to confirm)"
        ).ask_async()
        
        # Handle "Start All Servers" option
        if "__ALL_SERVERS__" in selected_servers:
            validation_results = self.validate_server_files()
            all_functional_servers = [
                server_id for server_id, config in SERVERS_CONFIG.items()
                if validation_results[server_id] and config['status'] == 'functional'
            ]
            console.print(f"[green]🚀 Starting all {len(all_functional_servers)} functional servers![/green]")
            return all_functional_servers
        
        return selected_servers or []

    async def prompt_execution_options(self) -> Dict[str, Any]:
        """Prompt for execution options"""
        # Mode selection
        mode = await questionary.select(
            "Select execution mode:",
            choices=[
                questionary.Choice("🚀 Development Mode (verbose logging, auto-reload)", "dev"),
                questionary.Choice("📊 Production Mode (optimized performance)", "prod"),
                questionary.Choice("🔇 Silent Mode (minimal output)", "quiet")
            ],
            qmark="⚙️"
        ).ask_async()
        
        # Parallel execution
        parallel = await questionary.confirm(
            "Run servers in parallel?",
            default=True,
            qmark="🔄"
        ).ask_async()
        
        # Show logs (only if not quiet mode)
        show_logs = True
        if mode != 'quiet':
            show_logs = await questionary.confirm(
                "Show server logs in real-time?",
                default=True,
                qmark="📊"
            ).ask_async()
        
        return {
            'mode': mode,
            'parallel': parallel,
            'show_logs': show_logs
        }

    async def start_server(self, server_id: str, options: Dict[str, Any]) -> bool:
        """Start a single server"""
        if server_id not in SERVERS_CONFIG:
            logger.error(f"Server '{server_id}' not found")
            return False
            
        config = SERVERS_CONFIG[server_id]
        module_path = config['module']
        
        try:
            # Build command with uv
            cmd = ["uv", "run", "python", "-m", module_path]
            
            # Environment variables
            env = os.environ.copy()
            env['MCP_SERVER_PORT'] = str(config['port'])
            env['MCP_SERVER_PROTOCOL'] = 'stdio'
            
            # Handle different modes
            stdout = None
            stderr = None
            if options['mode'] == 'quiet' or not options.get('show_logs', True):
                stdout = subprocess.PIPE
                stderr = subprocess.PIPE
            
            # Start process
            process = subprocess.Popen(
                cmd,
                cwd=str(self.project_root),
                env=env,
                stdout=stdout,
                stderr=stderr
            )
            
            self.running_servers[server_id] = process
            
            # Wait a moment to check if process started successfully
            await asyncio.sleep(1)
            
            if process.poll() is None:
                logger.info(f"✅ {config['name']} started (PID: {process.pid})")
                return True
            else:
                logger.error(f"❌ Failed to start {config['name']}")
                return False
                
        except Exception as e:
            logger.error(f"Error starting {server_id}: {e}")
            return False

    async def start_servers(self, server_ids: List[str], options: Dict[str, Any]):
        """Start multiple servers"""
        console.print()
        console.print("[bold green]🚀 Starting Selected Servers[/bold green]")
        console.print()
        
        successful_starts = []
        failed_starts = []
        
        if options.get('parallel', True):
            # Start servers in parallel
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console
            ) as progress:
                
                tasks = []
                for server_id in server_ids:
                    config = SERVERS_CONFIG[server_id]
                    task = progress.add_task(
                        f"Starting {config['emoji']} {config['name']}...", 
                        total=1
                    )
                    tasks.append((task, server_id))
                
                # Start all servers
                start_tasks = [
                    self.start_server(server_id, options) 
                    for server_id in server_ids
                ]
                
                results = await asyncio.gather(*start_tasks, return_exceptions=True)
                
                # Update progress and collect results
                for i, (task, server_id) in enumerate(tasks):
                    success = results[i] if not isinstance(results[i], Exception) else False
                    progress.update(task, completed=1)
                    
                    if success:
                        successful_starts.append(server_id)
                    else:
                        failed_starts.append(server_id)
        else:
            # Start servers sequentially
            for server_id in server_ids:
                config = SERVERS_CONFIG[server_id]
                console.print(f"Starting {config['emoji']} {config['name']}...")
                
                success = await self.start_server(server_id, options)
                if success:
                    successful_starts.append(server_id)
                else:
                    failed_starts.append(server_id)
        
        # Show summary
        console.print()
        self.show_launch_summary(successful_starts, failed_starts)
        
        if successful_starts:
            await self.monitor_servers(successful_starts, options)

    def show_launch_summary(self, successful: List[str], failed: List[str]):
        """Show launch summary"""
        summary_table = Table(title="📊 Launch Summary", show_header=True, header_style="bold cyan")
        summary_table.add_column("Status", style="bold")
        summary_table.add_column("Count", justify="center")
        summary_table.add_column("Servers")
        
        if successful:
            server_names = [f"{SERVERS_CONFIG[sid]['emoji']} {sid}" for sid in successful]
            summary_table.add_row(
                "[green]✅ Successful[/green]",
                str(len(successful)),
                ", ".join(server_names)
            )
        
        if failed:
            server_names = [f"{SERVERS_CONFIG[sid]['emoji']} {sid}" for sid in failed] 
            summary_table.add_row(
                "[red]❌ Failed[/red]",
                str(len(failed)),
                ", ".join(server_names)
            )
        
        console.print(summary_table)
        console.print()

    async def monitor_servers(self, server_ids: List[str], options: Dict[str, Any]):
        """Monitor running servers"""
        console.print("[bold cyan]🔄 Monitoring Servers[/bold cyan]")
        console.print("[dim]Press Ctrl+C to stop all servers[/dim]")
        console.print()
        
        # Show running servers info
        info_table = Table(show_header=True, header_style="bold green")
        info_table.add_column("Server") 
        info_table.add_column("Port")
        info_table.add_column("PID")
        info_table.add_column("Status")
        
        for server_id in server_ids:
            config = SERVERS_CONFIG[server_id]
            process = self.running_servers.get(server_id)
            if process:
                info_table.add_row(
                    f"{config['emoji']} {config['name']}",
                    str(config['port']),
                    str(process.pid),
                    "[green]Running[/green]"
                )
        
        console.print(info_table)
        console.print()
        
        try:
            while True:
                await asyncio.sleep(2)
                
                # Check if any server died
                dead_servers = []
                for server_id in list(self.running_servers.keys()):
                    process = self.running_servers[server_id]
                    if process.poll() is not None:
                        dead_servers.append(server_id)
                        del self.running_servers[server_id]
                
                if dead_servers:
                    for server_id in dead_servers:
                        config = SERVERS_CONFIG[server_id]
                        console.print(f"[red]⚠️ {config['name']} stopped unexpectedly[/red]")
                
                if not self.running_servers:
                    console.print("[yellow]All servers have stopped[/yellow]")
                    break
                    
        except KeyboardInterrupt:
            console.print("\n[yellow]🛑 Received stop signal[/yellow]")
            await self.stop_all_servers()

    async def stop_all_servers(self):
        """Stop all running servers"""
        if not self.running_servers:
            return
            
        console.print("[yellow]🛑 Stopping all servers...[/yellow]")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            
            for server_id, process in self.running_servers.items():
                config = SERVERS_CONFIG[server_id]
                task = progress.add_task(f"Stopping {config['name']}...", total=1)
                
                try:
                    process.terminate()
                    
                    # Wait for graceful termination
                    try:
                        await asyncio.wait_for(
                            asyncio.to_thread(process.wait), 
                            timeout=5.0
                        )
                    except asyncio.TimeoutError:
                        console.print(f"[yellow]Force killing {config['name']}...[/yellow]")
                        process.kill()
                        await asyncio.to_thread(process.wait)
                        
                    progress.update(task, completed=1)
                    
                except Exception as e:
                    console.print(f"[red]Error stopping {server_id}: {e}[/red]")
        
        self.running_servers.clear()
        console.print("[green]✅ All servers stopped[/green]")

    def show_help(self):
        """Show help information"""
        help_panel = Panel.fit(
            "[bold]Available Commands:[/bold]\n\n"
            "[green]uv run mcp_servers[/green]         - Start interactive launcher (recommended)\n"
            "[green]uv run mcp_servers --help[/green]  - Show this help\n"
            "[green]uv run mcp_servers --status[/green] - Show server status\n\n"
            "[dim]Alternative direct calls:[/dim]\n"
            "[green]python launcher_cli.py[/green]     - Direct Python call\n"
            "[green]uv run python launcher_cli.py[/green] - Direct uv call\n\n"
            "[bold]Features:[/bold]\n"
            "• 🚀 Quick 'Start All Servers' option\n"
            "• Multi-select servers with checkboxes\n" 
            "• Parallel/sequential execution modes\n"
            "• Development/production/quiet modes\n"
            "• Real-time server monitoring\n"
            "• Graceful shutdown handling\n",
            title="[bold cyan]MCP Launcher CLI Help[/bold cyan]",
            border_style="cyan"
        )
        console.print(help_panel)

    async def run(self, args: Optional[List[str]] = None):
        """Main CLI execution"""
        if args and '--help' in args:
            self.show_help()
            return
            
        if args and '--status' in args:
            self.show_banner()
            self.show_server_status()
            return
        
        try:
            self.show_banner()
            
            # Server selection
            selected_servers = await self.prompt_server_selection()
            if not selected_servers:
                console.print("[yellow]No servers selected. Exiting.[/yellow]")
                return
            
            # Execution options
            console.print()
            execution_options = await self.prompt_execution_options()
            
            # Start servers
            await self.start_servers(selected_servers, execution_options)
            
        except KeyboardInterrupt:
            console.print("\n[yellow]Operation cancelled[/yellow]")
        except Exception as e:
            console.print(f"[red]Unexpected error: {e}[/red]")
            logger.exception("Unexpected error occurred")
        finally:
            await self.stop_all_servers()


def setup_signal_handlers(launcher: MCPLauncherCLI):
    """Setup signal handlers for graceful shutdown"""
    def signal_handler(signum, frame):
        console.print(f"\n[yellow]Received signal {signum}[/yellow]")
        asyncio.create_task(launcher.stop_all_servers())
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)


async def async_main():
    """Async main entry point"""
    launcher = MCPLauncherCLI()
    setup_signal_handlers(launcher)
    await launcher.run(sys.argv[1:])


def main():
    """Synchronous entry point for pyproject.toml script"""
    try:
        asyncio.run(async_main())
    except KeyboardInterrupt:
        console.print("\n[yellow]Goodbye! 👋[/yellow]")
    except Exception as e:
        console.print(f"[red]Fatal error: {e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()