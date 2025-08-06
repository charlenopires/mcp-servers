#!/usr/bin/env python3
"""
Demo script to showcase the new interactive CLI
This script shows the capabilities without actually starting servers
"""

import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from launcher_cli import MCPLauncherCLI

async def demo():
    """Run a demo of the CLI features"""
    cli = MCPLauncherCLI()
    
    print("🎬 MCP Servers Interactive CLI Demo")
    print("=" * 50)
    print()
    
    # Show banner
    cli.show_banner()
    
    # Show server status
    cli.show_server_status()
    
    # Show help
    cli.show_help()
    
    print("📝 To use the interactive interface, run:")
    print("   python launcher_cli.py")
    print()
    print("🎯 Features demonstrated:")
    print("   ✅ Rich formatted output with colors")
    print("   ✅ Server status validation")
    print("   ✅ Categorized server listing")
    print("   ✅ Interactive multi-select (when run interactively)")
    print("   ✅ Real-time monitoring capabilities")

if __name__ == "__main__":
    import asyncio
    asyncio.run(demo())