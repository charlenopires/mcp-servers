#!/usr/bin/env python3
"""
Script para executar todos os testes dos servidores MCP.

Este script executa todos os testes presentes no diretório tests/
e fornece um relatório consolidado dos resultados.
"""

import subprocess
import sys
import os
from pathlib import Path


def run_all_tests():
    """Executa todos os testes e exibe os resultados."""

    # Diretório atual do script
    script_dir = Path(__file__).parent
    tests_dir = script_dir / "tests"

    print("🧪 Executando todos os testes dos servidores MCP...")
    print("=" * 60)

    # Lista todos os arquivos de teste
    test_files = list(tests_dir.glob("test_*.py"))

    if not test_files:
        print("❌ Nenhum arquivo de teste encontrado!")
        return False

    print(f"📁 Encontrados {len(test_files)} arquivos de teste:")
    for test_file in test_files:
        print(f"   • {test_file.name}")
    print()

    # Executar pytest
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest",
            str(tests_dir),
            "-v",  # verbose
            "--tb=short",  # traceback curto
            "--color=yes"  # colorir output
        ], capture_output=True, text=True, cwd=script_dir)

        print("📊 Resultado dos testes:")
        print("-" * 40)
        print(result.stdout)

        if result.stderr:
            print("⚠️  Avisos/Erros:")
            print(result.stderr)

        success = result.returncode == 0

        if success:
            print("✅ Todos os testes passaram!")
        else:
            print("❌ Alguns testes falharam!")

        return success

    except FileNotFoundError:
        print("❌ pytest não encontrado! Instale com: pip install pytest")
        return False
    except Exception as e:
        print(f"❌ Erro ao executar testes: {e}")
        return False


def check_dependencies():
    """Verifica se as dependências necessárias estão instaladas."""

    print("🔍 Verificando dependências...")

    # Verificar se pytest está instalado
    try:
        import pytest
        print("✅ pytest encontrado")
    except ImportError:
        print("❌ pytest não encontrado! Instale com: pip install pytest")
        return False

    # Verificar se fastmcp está instalado
    try:
        import fastmcp
        print("✅ fastmcp encontrado")
    except ImportError:
        print("❌ fastmcp não encontrado! Instale com: pip install fastmcp")
        return False

    return True


if __name__ == "__main__":
    print("🚀 Iniciando execução dos testes dos servidores MCP")
    print("=" * 60)

    # Verificar dependências
    if not check_dependencies():
        print("\n❌ Dependências em falta. Execute:")
        print("   pip install -r requirements.txt")
        sys.exit(1)

    print()

    # Executar testes
    success = run_all_tests()

    print("\n" + "=" * 60)
    if success:
        print("🎉 Execução concluída com sucesso!")
        sys.exit(0)
    else:
        print("💥 Execução concluída com falhas!")
        sys.exit(1)
