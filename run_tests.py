#!/usr/bin/env python3
"""
Script para executar todos os testes dos servidores MCP.

Este script executa todos os testes presentes no diretório tests/
e fornece um relatório consolidado dos resultados usando uv e pytest.
"""

import subprocess
import sys
import os
from pathlib import Path
import json
import time


def check_dependencies():
    """Verifica se as dependências necessárias estão disponíveis."""

    # Verificar uv
    if subprocess.run(["which", "uv"], capture_output=True).returncode != 0:
        print("❌ Erro: 'uv' não está instalado")
        print("💡 Instale com: curl -LsSf https://astral.sh/uv/install.sh | sh")
        return False

    return True


def run_individual_tests():
    """Executa testes individuais para cada servidor."""

    script_dir = Path(__file__).parent
    tests_dir = script_dir / "tests"

    print("🔍 Executando testes individuais...")
    print("-" * 50)

    test_files = list(tests_dir.glob("test_*.py"))
    results = {}

    for test_file in test_files:
        server_name = test_file.stem.replace("test_", "")
        print(f"\n📝 Testando {server_name}...")

        try:
            result = subprocess.run([
                "uv", "run", "python", "-m", "pytest",
                str(test_file),
                "-v",
                "--tb=short",
                "--json-report",
                "--json-report-file=/tmp/pytest_report.json"
            ], capture_output=True, text=True, cwd=script_dir, timeout=60)

            if result.returncode == 0:
                print(f"   ✅ {server_name}: PASSOU")
                results[server_name] = "PASSOU"
            else:
                print(f"   ❌ {server_name}: FALHOU")
                results[server_name] = "FALHOU"
                if result.stderr:
                    print(f"   Erro: {result.stderr[:200]}...")

        except subprocess.TimeoutExpired:
            print(f"   ⏰ {server_name}: TIMEOUT")
            results[server_name] = "TIMEOUT"
        except Exception as e:
            print(f"   💥 {server_name}: ERRO - {e}")
            results[server_name] = "ERRO"

    return results


def run_all_tests():
    """Executa todos os testes e exibe os resultados."""

    script_dir = Path(__file__).parent
    tests_dir = script_dir / "tests"

    print("🧪 Executando todos os testes dos servidores MCP...")
    print("=" * 60)

    # Verificar dependências
    if not check_dependencies():
        return False

    # Lista todos os arquivos de teste
    test_files = list(tests_dir.glob("test_*.py"))

    if not test_files:
        print("❌ Nenhum arquivo de teste encontrado!")
        return False

    print(f"📁 Encontrados {len(test_files)} arquivos de teste:")
    for test_file in test_files:
        print(f"   • {test_file.name}")
    print()

    # Executar pytest com uv
    try:
        start_time = time.time()

        # Verificar se pytest-cov está disponível
        try:
            cov_check = subprocess.run(
                ["uv", "run", "python", "-c", "import pytest_cov"],
                capture_output=True, text=True, cwd=script_dir
            )
            has_coverage = cov_check.returncode == 0
        except:
            has_coverage = False

        print("🚀 Executando pytest...")

        # Comandos pytest com ou sem cobertura
        if has_coverage:
            cmd_args = [
                "uv", "run", "python", "-m", "pytest",
                str(tests_dir),
                "-v",  # verbose
                "--tb=short",  # traceback curto
                "--color=yes",  # colorir output
                "--durations=10",  # mostrar 10 testes mais lentos
                "--cov=servers",  # cobertura de código
                "--cov-report=term-missing"  # relatório de cobertura
            ]
        else:
            cmd_args = [
                "uv", "run", "python", "-m", "pytest",
                str(tests_dir),
                "-v",  # verbose
                "--tb=short",  # traceback curto
                "--color=yes",  # colorir output
                "--durations=10"  # mostrar 10 testes mais lentos
            ]

        result = subprocess.run(
            cmd_args, capture_output=True, text=True, cwd=script_dir)

        end_time = time.time()
        duration = end_time - start_time

        print("📊 Resultado dos testes:")
        print("-" * 40)
        print(result.stdout)

        if result.stderr:
            print("\n⚠️ Avisos/Erros:")
            print("-" * 40)
            print(result.stderr)

        # Análise do resultado
        if result.returncode == 0:
            print(f"\n✅ Todos os testes passaram! ({duration:.2f}s)")
            return True
        else:
            print(f"\n❌ Alguns testes falharam! ({duration:.2f}s)")
            return False

    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar testes: {e}")
        return False
    except Exception as e:
        print(f"💥 Erro inesperado: {e}")
        return False


def run_specific_test(test_name: str):
    """Executa um teste específico."""

    script_dir = Path(__file__).parent
    tests_dir = script_dir / "tests"

    # Procurar arquivo de teste
    test_file = tests_dir / f"test_{test_name}.py"
    if not test_file.exists():
        test_file = tests_dir / f"{test_name}.py"
        if not test_file.exists():
            print(f"❌ Arquivo de teste não encontrado: {test_name}")
            return False

    print(f"🧪 Executando teste específico: {test_file.name}")
    print("-" * 50)

    try:
        result = subprocess.run([
            "uv", "run", "python", "-m", "pytest",
            str(test_file),
            "-v",
            "--tb=long",  # traceback longo para debug
            "--color=yes"
        ], cwd=script_dir)

        return result.returncode == 0

    except Exception as e:
        print(f"💥 Erro ao executar teste {test_name}: {e}")
        return False


def main():
    """Função principal do script."""

    import argparse

    parser = argparse.ArgumentParser(
        description="Executar testes dos servidores MCP",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python run_tests.py                    # Executa todos os testes
  python run_tests.py --individual      # Executa testes individuais
  python run_tests.py --test mcp_server # Executa teste específico
  python run_tests.py --coverage        # Executa com relatório de cobertura
        """
    )

    parser.add_argument(
        "--individual", "-i",
        action="store_true",
        help="Executar testes individuais para cada servidor"
    )

    parser.add_argument(
        "--test", "-t",
        type=str,
        help="Executar teste específico (nome do arquivo sem 'test_' e '.py')"
    )

    parser.add_argument(
        "--coverage", "-c",
        action="store_true",
        help="Executar com relatório de cobertura detalhado"
    )

    parser.add_argument(
        "--quick", "-q",
        action="store_true",
        help="Executação rápida (sem cobertura)"
    )

    args = parser.parse_args()

    # Banner
    print("🧪 MCP Servers - Test Runner")
    print("=" * 40)

    success = True

    try:
        if args.test:
            # Teste específico
            success = run_specific_test(args.test)
        elif args.individual:
            # Testes individuais
            results = run_individual_tests()

            print(f"\n📈 Resumo dos resultados:")
            print("-" * 30)
            for server, result in results.items():
                status_icon = "✅" if result == "PASSOU" else "❌"
                print(f"  {status_icon} {server}: {result}")

            passed = sum(1 for r in results.values() if r == "PASSOU")
            total = len(results)
            print(f"\n📊 Total: {passed}/{total} passaram")
            success = passed == total

        else:
            # Todos os testes
            success = run_all_tests()

        # Resultado final
        if success:
            print(f"\n🎉 Execução concluída com sucesso!")
            sys.exit(0)
        else:
            print(f"\n💥 Execução concluída com falhas!")
            sys.exit(1)

    except KeyboardInterrupt:
        print(f"\n⏹️ Execução interrompida pelo usuário")
        sys.exit(130)
    except Exception as e:
        print(f"\n💥 Erro inesperado: {e}")
        sys.exit(1)


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
