#!/usr/bin/env python3
"""
MCP Servers Configuration Installer
====================================

Installs MCP server configurations for multiple AI tools:
- Claude Desktop
- Claude Code
- Gemini CLI
- Antigravity
- VSCode Insiders

Configuration Paths:
--------------------
- Claude Desktop (macOS): ~/Library/Application Support/Claude/claude_desktop_config.json
- Claude Code: ~/.claude.json
- Gemini CLI: ~/.gemini/settings.json
- Antigravity: ~/.gemini/antigravity/mcp_config.json
- VSCode Insiders: ~/.vscode-insiders/mcp.json (user profile)

Usage:
    python install_mcp_configs.py                    # Interactive mode
    python install_mcp_configs.py --all              # Install to all locations
    python install_mcp_configs.py --claude-desktop   # Install to Claude Desktop only
    python install_mcp_configs.py --list             # List available configurations
"""

import argparse
import json
import os
import platform
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

# Project root directory
PROJECT_ROOT = Path(__file__).parent.resolve()

# Server configurations
SERVERS = {
    "mcp-analysis": {
        "name": "MCP Analysis Server",
        "module": "servers.mcp_server",
        "port": 3000
    },
    "prompt-engineering": {
        "name": "Prompt Engineering Server",
        "module": "servers.prompt_server",
        "port": 3001
    },
    "tailwind-css": {
        "name": "Tailwind CSS Server",
        "module": "servers.tailwind_server",
        "port": 3002
    },
    "fastmcp": {
        "name": "FastMCP Server",
        "module": "servers.fastmcp_server",
        "port": 3003
    },
    "react-components": {
        "name": "React Components Server",
        "module": "servers.react_server",
        "port": 3004
    },
    "typescript-analysis": {
        "name": "TypeScript Analysis Server",
        "module": "servers.typescript_server",
        "port": 3005
    },
    "shadcn-ui": {
        "name": "shadcn/ui Server",
        "module": "servers.shadcn_server",
        "port": 3006
    },
    "rust-idiomatic": {
        "name": "Rust Idiomatic Server",
        "module": "servers.rust_server",
        "port": 3007
    },
    "axum-web-framework": {
        "name": "Axum Web Framework Server",
        "module": "servers.axum_server",
        "port": 3008
    },
    "docker-optimizer": {
        "name": "Docker Optimizer Server",
        "module": "servers.docker_optimizer_server",
        "port": 3009
    },
    "python-optimizer": {
        "name": "Python Optimizer Server",
        "module": "servers.python_optimizer_server",
        "port": 3010
    },
    "erlang-otp": {
        "name": "Erlang OTP Server",
        "module": "servers.erlang_server",
        "port": 3011
    },
    "elixir-development": {
        "name": "Elixir Development Server",
        "module": "servers.elixir_server",
        "port": 3012
    },
    "phoenix-framework": {
        "name": "Phoenix Framework Server",
        "module": "servers.phoenix_server",
        "port": 3013
    },
    "phoenix-channels": {
        "name": "Phoenix Channels Server",
        "module": "servers.phoenix_channels_server",
        "port": 3014
    },
    "phoenix-liveview": {
        "name": "Phoenix LiveView Server",
        "module": "servers.phoenix_liveview_server",
        "port": 3015
    },
    "neo4j-cypher": {
        "name": "Neo4j Cypher Server",
        "module": "servers.neo4j_server",
        "port": 3016
    },
    "qdrant-vector": {
        "name": "Qdrant Vector Server",
        "module": "servers.qdrant_server",
        "port": 3017
    },
    "htmx-axum": {
        "name": "HTMX + Axum Server",
        "module": "servers.htmx_server",
        "port": 3018
    }
}

# Configuration paths for each tool
def get_config_paths() -> Dict[str, Path]:
    """Get configuration file paths for each AI tool."""
    home = Path.home()
    system = platform.system()

    paths = {
        "claude_code": home / ".claude.json",
        "gemini_cli": home / ".gemini" / "settings.json",
        "antigravity": home / ".gemini" / "antigravity" / "mcp_config.json",
    }

    if system == "Darwin":  # macOS
        paths["claude_desktop"] = home / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
        paths["vscode_insiders"] = home / "Library" / "Application Support" / "Code - Insiders" / "User" / "mcp.json"
    elif system == "Windows":
        paths["claude_desktop"] = home / "AppData" / "Roaming" / "Claude" / "claude_desktop_config.json"
        paths["vscode_insiders"] = home / "AppData" / "Roaming" / "Code - Insiders" / "User" / "mcp.json"
    else:  # Linux
        paths["claude_desktop"] = home / ".config" / "Claude" / "claude_desktop_config.json"
        paths["vscode_insiders"] = home / ".config" / "Code - Insiders" / "User" / "mcp.json"

    return paths


def generate_server_config(server_id: str, server_info: Dict[str, Any]) -> Dict[str, Any]:
    """Generate MCP server configuration for a single server."""
    return {
        "command": "uv",
        "args": [
            "run",
            "--directory",
            str(PROJECT_ROOT),
            "python",
            "-m",
            server_info["module"]
        ],
        "env": {
            "MCP_SERVER_PORT": str(server_info["port"]),
            "MCP_SERVER_PROTOCOL": "stdio"
        }
    }


def generate_all_configs() -> Dict[str, Dict[str, Any]]:
    """Generate configurations for all servers."""
    configs = {}
    for server_id, server_info in SERVERS.items():
        configs[server_id] = generate_server_config(server_id, server_info)
    return configs


def backup_file(path: Path) -> Optional[Path]:
    """Create a backup of existing configuration file."""
    if path.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = path.with_suffix(f".backup_{timestamp}.json")
        shutil.copy2(path, backup_path)
        print(f"  Backup created: {backup_path}")
        return backup_path
    return None


def merge_config(existing: Dict[str, Any], new_servers: Dict[str, Dict[str, Any]], key: str = "mcpServers") -> Dict[str, Any]:
    """Merge new server configs into existing configuration."""
    if key not in existing:
        existing[key] = {}

    existing[key].update(new_servers)
    return existing


def install_claude_desktop(configs: Dict[str, Dict[str, Any]], dry_run: bool = False) -> bool:
    """Install configuration to Claude Desktop."""
    path = get_config_paths()["claude_desktop"]
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Installing to Claude Desktop...")
    print(f"  Path: {path}")

    if dry_run:
        print(f"  Would install {len(configs)} servers")
        return True

    try:
        path.parent.mkdir(parents=True, exist_ok=True)

        existing = {}
        if path.exists():
            backup_file(path)
            with open(path, 'r') as f:
                existing = json.load(f)

        merged = merge_config(existing, configs)

        with open(path, 'w') as f:
            json.dump(merged, f, indent=2)

        print(f"  Installed {len(configs)} servers")
        return True
    except Exception as e:
        print(f"  Error: {e}")
        return False


def install_claude_code(configs: Dict[str, Dict[str, Any]], dry_run: bool = False) -> bool:
    """Install configuration to Claude Code."""
    path = get_config_paths()["claude_code"]
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Installing to Claude Code...")
    print(f"  Path: {path}")

    if dry_run:
        print(f"  Would install {len(configs)} servers")
        return True

    try:
        existing = {}
        if path.exists():
            backup_file(path)
            with open(path, 'r') as f:
                existing = json.load(f)

        merged = merge_config(existing, configs)

        with open(path, 'w') as f:
            json.dump(merged, f, indent=2)

        print(f"  Installed {len(configs)} servers")
        return True
    except Exception as e:
        print(f"  Error: {e}")
        return False


def install_gemini_cli(configs: Dict[str, Dict[str, Any]], dry_run: bool = False) -> bool:
    """Install configuration to Gemini CLI."""
    path = get_config_paths()["gemini_cli"]
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Installing to Gemini CLI...")
    print(f"  Path: {path}")

    if dry_run:
        print(f"  Would install {len(configs)} servers")
        return True

    try:
        path.parent.mkdir(parents=True, exist_ok=True)

        existing = {}
        if path.exists():
            backup_file(path)
            with open(path, 'r') as f:
                existing = json.load(f)

        merged = merge_config(existing, configs)

        with open(path, 'w') as f:
            json.dump(merged, f, indent=2)

        print(f"  Installed {len(configs)} servers")
        return True
    except Exception as e:
        print(f"  Error: {e}")
        return False


def install_antigravity(configs: Dict[str, Dict[str, Any]], dry_run: bool = False) -> bool:
    """Install configuration to Antigravity."""
    path = get_config_paths()["antigravity"]
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Installing to Antigravity...")
    print(f"  Path: {path}")

    if dry_run:
        print(f"  Would install {len(configs)} servers")
        return True

    try:
        path.parent.mkdir(parents=True, exist_ok=True)

        existing = {}
        if path.exists():
            backup_file(path)
            with open(path, 'r') as f:
                existing = json.load(f)

        merged = merge_config(existing, configs)

        with open(path, 'w') as f:
            json.dump(merged, f, indent=2)

        print(f"  Installed {len(configs)} servers")
        return True
    except Exception as e:
        print(f"  Error: {e}")
        return False


def install_vscode_insiders(configs: Dict[str, Dict[str, Any]], dry_run: bool = False) -> bool:
    """Install configuration to VSCode Insiders."""
    path = get_config_paths()["vscode_insiders"]
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Installing to VSCode Insiders...")
    print(f"  Path: {path}")

    if dry_run:
        print(f"  Would install {len(configs)} servers")
        return True

    try:
        path.parent.mkdir(parents=True, exist_ok=True)

        existing = {}
        if path.exists():
            backup_file(path)
            with open(path, 'r') as f:
                existing = json.load(f)

        # VSCode uses different structure
        if "servers" not in existing:
            existing["servers"] = {}

        existing["servers"].update(configs)

        with open(path, 'w') as f:
            json.dump(existing, f, indent=2)

        print(f"  Installed {len(configs)} servers")
        return True
    except Exception as e:
        print(f"  Error: {e}")
        return False


def list_servers():
    """List all available MCP servers."""
    print("\nAvailable MCP Servers:")
    print("=" * 80)
    print(f"{'ID':<25} {'Name':<35} {'Port':<6}")
    print("-" * 80)

    for server_id, info in SERVERS.items():
        print(f"{server_id:<25} {info['name']:<35} {info['port']:<6}")

    print("-" * 80)
    print(f"Total: {len(SERVERS)} servers")


def list_paths():
    """List all configuration paths."""
    print("\nConfiguration File Paths:")
    print("=" * 80)

    paths = get_config_paths()
    for tool, path in paths.items():
        exists = "" if path.exists() else " (not found)"
        print(f"  {tool.replace('_', ' ').title()}: {path}{exists}")


def interactive_mode():
    """Run interactive installation mode."""
    print("\n MCP Servers Configuration Installer")
    print("=" * 50)

    configs = generate_all_configs()

    print(f"\nProject directory: {PROJECT_ROOT}")
    print(f"Total servers: {len(SERVERS)}")

    list_paths()

    print("\nSelect installation targets:")
    print("  1. Claude Desktop")
    print("  2. Claude Code")
    print("  3. Gemini CLI")
    print("  4. Antigravity")
    print("  5. VSCode Insiders")
    print("  6. All of the above")
    print("  7. Exit")

    choice = input("\nEnter choice (1-7): ").strip()

    installers = {
        "1": [("Claude Desktop", install_claude_desktop)],
        "2": [("Claude Code", install_claude_code)],
        "3": [("Gemini CLI", install_gemini_cli)],
        "4": [("Antigravity", install_antigravity)],
        "5": [("VSCode Insiders", install_vscode_insiders)],
        "6": [
            ("Claude Desktop", install_claude_desktop),
            ("Claude Code", install_claude_code),
            ("Gemini CLI", install_gemini_cli),
            ("Antigravity", install_antigravity),
            ("VSCode Insiders", install_vscode_insiders),
        ],
    }

    if choice == "7":
        print("Exiting...")
        return

    if choice not in installers:
        print("Invalid choice")
        return

    print("\nInstalling configurations...")

    results = []
    for name, installer in installers[choice]:
        success = installer(configs)
        results.append((name, success))

    print("\n" + "=" * 50)
    print("Installation Summary:")
    for name, success in results:
        status = "" if success else ""
        print(f"  {status} {name}")

    print("\nNote: Restart the applications for changes to take effect.")


def main():
    parser = argparse.ArgumentParser(
        description="Install MCP server configurations to AI tools",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("--all", action="store_true", help="Install to all locations")
    parser.add_argument("--claude-desktop", action="store_true", help="Install to Claude Desktop")
    parser.add_argument("--claude-code", action="store_true", help="Install to Claude Code")
    parser.add_argument("--gemini-cli", action="store_true", help="Install to Gemini CLI")
    parser.add_argument("--antigravity", action="store_true", help="Install to Antigravity")
    parser.add_argument("--vscode-insiders", action="store_true", help="Install to VSCode Insiders")
    parser.add_argument("--list", action="store_true", help="List available servers")
    parser.add_argument("--paths", action="store_true", help="List configuration paths")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without making changes")
    parser.add_argument("--export", type=str, help="Export configuration to a file")

    args = parser.parse_args()

    if args.list:
        list_servers()
        return

    if args.paths:
        list_paths()
        return

    configs = generate_all_configs()

    if args.export:
        export_path = Path(args.export)
        with open(export_path, 'w') as f:
            json.dump({"mcpServers": configs}, f, indent=2)
        print(f"Configuration exported to: {export_path}")
        return

    # Check if any specific target was selected
    specific_targets = [
        args.claude_desktop,
        args.claude_code,
        args.gemini_cli,
        args.antigravity,
        args.vscode_insiders,
    ]

    if not any(specific_targets) and not args.all:
        # No arguments provided, run interactive mode
        interactive_mode()
        return

    # Run selected installers
    results = []

    if args.all or args.claude_desktop:
        results.append(("Claude Desktop", install_claude_desktop(configs, args.dry_run)))

    if args.all or args.claude_code:
        results.append(("Claude Code", install_claude_code(configs, args.dry_run)))

    if args.all or args.gemini_cli:
        results.append(("Gemini CLI", install_gemini_cli(configs, args.dry_run)))

    if args.all or args.antigravity:
        results.append(("Antigravity", install_antigravity(configs, args.dry_run)))

    if args.all or args.vscode_insiders:
        results.append(("VSCode Insiders", install_vscode_insiders(configs, args.dry_run)))

    print("\n" + "=" * 50)
    print("Installation Summary:")
    for name, success in results:
        status = "" if success else ""
        print(f"  {status} {name}")

    if not args.dry_run:
        print("\nNote: Restart the applications for changes to take effect.")


if __name__ == "__main__":
    main()
