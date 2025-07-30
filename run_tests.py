#!/usr/bin/env python3
"""
Script to run all tests for MCP servers.

This script runs all tests present in the tests/ directory
and provides a consolidated report of results using uv and pytest.
"""

import subprocess
import sys
import os
from pathlib import Path
import json
import time


def check_dependencies():
    """Check if required dependencies are available."""

    # Check uv
    if subprocess.run(["which", "uv"], capture_output=True).returncode != 0:
        print("❌ Error: 'uv' is not installed")
        print("💡 Install with: curl -LsSf https://astral.sh/uv/install.sh | sh")
        return False

    return True


def run_individual_tests():
    """Run individual tests for each server."""

    script_dir = Path(__file__).parent
    tests_dir = script_dir / "tests"

    print("🔍 Running individual tests...")
    print("-" * 50)

    test_files = list(tests_dir.glob("test_*.py"))
    results = {}

    for test_file in test_files:
        server_name = test_file.stem.replace("test_", "")
        print(f"\n📝 Testing {server_name}...")

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
                print(f"   ✅ {server_name}: PASSED")
                results[server_name] = "PASSED"
            else:
                print(f"   ❌ {server_name}: FAILED")
                results[server_name] = "FAILED"
                if result.stderr:
                    print(f"   Error: {result.stderr[:200]}...")

        except subprocess.TimeoutExpired:
            print(f"   ⏰ {server_name}: TIMEOUT")
            results[server_name] = "TIMEOUT"
        except Exception as e:
            print(f"   💥 {server_name}: ERROR - {e}")
            results[server_name] = "ERROR"

    return results


def run_all_tests():
    """Run all tests and display results."""

    script_dir = Path(__file__).parent
    tests_dir = script_dir / "tests"

    print("🧪 Running all MCP server tests...")
    print("=" * 60)

    # Check dependencies
    if not check_dependencies():
        return False

    # List all test files
    test_files = list(tests_dir.glob("test_*.py"))

    if not test_files:
        print("❌ No test files found!")
        return False

    print(f"📁 Found {len(test_files)} test files:")
    for test_file in test_files:
        print(f"   • {test_file.name}")
    print()

    # Execute pytest with uv
    try:
        start_time = time.time()

        # Check if pytest-cov is available
        try:
            cov_check = subprocess.run(
                ["uv", "run", "python", "-c", "import pytest_cov"],
                capture_output=True, text=True, cwd=script_dir
            )
            has_coverage = cov_check.returncode == 0
        except:
            has_coverage = False

        print("🚀 Running pytest...")

        # Pytest commands with or without coverage
        if has_coverage:
            cmd_args = [
                "uv", "run", "python", "-m", "pytest",
                str(tests_dir),
                "-v",  # verbose
                "--tb=short",  # short traceback
                "--color=yes",  # colorize output
                "--durations=10",  # show 10 slowest tests
                "--cov=servers",  # code coverage
                "--cov-report=term-missing"  # coverage report
            ]
        else:
            cmd_args = [
                "uv", "run", "python", "-m", "pytest",
                str(tests_dir),
                "-v",  # verbose
                "--tb=short",  # short traceback
                "--color=yes",  # colorize output
                "--durations=10"  # show 10 slowest tests
            ]

        result = subprocess.run(
            cmd_args, capture_output=True, text=True, cwd=script_dir)

        end_time = time.time()
        duration = end_time - start_time

        print("📊 Test results:")
        print("-" * 40)
        print(result.stdout)

        if result.stderr:
            print("\n⚠️ Warnings/Errors:")
            print("-" * 40)
            print(result.stderr)

        # Result analysis
        if result.returncode == 0:
            print(f"\n✅ All tests passed! ({duration:.2f}s)")
            return True
        else:
            print(f"\n❌ Some tests failed! ({duration:.2f}s)")
            return False

    except subprocess.CalledProcessError as e:
        print(f"❌ Error running tests: {e}")
        return False
    except Exception as e:
        print(f"💥 Unexpected error: {e}")
        return False


def run_specific_test(test_name: str):
    """Run a specific test."""

    script_dir = Path(__file__).parent
    tests_dir = script_dir / "tests"

    # Search for test file
    test_file = tests_dir / f"test_{test_name}.py"
    if not test_file.exists():
        test_file = tests_dir / f"{test_name}.py"
        if not test_file.exists():
            print(f"❌ Test file not found: {test_name}")
            return False

    print(f"🧪 Running specific test: {test_file.name}")
    print("-" * 50)

    try:
        result = subprocess.run([
            "uv", "run", "python", "-m", "pytest",
            str(test_file),
            "-v",
            "--tb=long",  # long traceback for debugging
            "--color=yes"
        ], cwd=script_dir)

        return result.returncode == 0

    except Exception as e:
        print(f"💥 Error running test {test_name}: {e}")
        return False


def main():
    """Main function of the script."""

    import argparse

    parser = argparse.ArgumentParser(
        description="Run MCP server tests",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_tests.py                    # Run all tests
  python run_tests.py --individual      # Run individual tests
  python run_tests.py --test mcp_server # Run specific test
  python run_tests.py --coverage        # Run with coverage report
        """
    )

    parser.add_argument(
        "--individual", "-i",
        action="store_true",
        help="Run individual tests for each server"
    )

    parser.add_argument(
        "--test", "-t",
        type=str,
        help="Run specific test (filename without 'test_' and '.py')"
    )

    parser.add_argument(
        "--coverage", "-c",
        action="store_true",
        help="Run with detailed coverage report"
    )

    parser.add_argument(
        "--quick", "-q",
        action="store_true",
        help="Quick execution (without coverage)"
    )

    args = parser.parse_args()

    # Banner
    print("🧪 MCP Servers - Test Runner")
    print("=" * 40)

    success = True

    try:
        if args.test:
            # Specific test
            success = run_specific_test(args.test)
        elif args.individual:
            # Individual tests
            results = run_individual_tests()

            print(f"\n📈 Results summary:")
            print("-" * 30)
            for server, result in results.items():
                status_icon = "✅" if result == "PASSED" else "❌"
                print(f"  {status_icon} {server}: {result}")

            passed = sum(1 for r in results.values() if r == "PASSED")
            total = len(results)
            print(f"\n📊 Total: {passed}/{total} passed")
            success = passed == total

        else:
            # All tests
            success = run_all_tests()

        # Final result
        if success:
            print(f"\n🎉 Execution completed successfully!")
            sys.exit(0)
        else:
            print(f"\n💥 Execution completed with failures!")
            sys.exit(1)

    except KeyboardInterrupt:
        print(f"\n⏹️ Execution interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        sys.exit(1)


def check_dependencies():
    """Check if required dependencies are installed."""

    print("🔍 Checking dependencies...")

    # Check if pytest is installed
    try:
        import pytest
        print("✅ pytest found")
    except ImportError:
        print("❌ pytest not found! Install with: pip install pytest")
        return False

    # Check if fastmcp is installed
    try:
        import fastmcp
        print("✅ fastmcp found")
    except ImportError:
        print("❌ fastmcp not found! Install with: pip install fastmcp")
        return False

    return True


if __name__ == "__main__":
    print("🚀 Starting MCP server test execution")
    print("=" * 60)

    # Check dependencies
    if not check_dependencies():
        print("\n❌ Missing dependencies. Run:")
        print("   pip install -r requirements.txt")
        sys.exit(1)

    print()

    # Run tests
    success = run_all_tests()

    print("\n" + "=" * 60)
    if success:
        print("🎉 Execution completed successfully!")
        sys.exit(0)
    else:
        print("💥 Execution completed with failures!")
        sys.exit(1)
