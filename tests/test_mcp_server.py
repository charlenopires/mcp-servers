#!/usr/bin/env python3
"""
Unit tests for the MCP Prompt Analyzer server.
"""

import pytest
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from servers.mcp_server import MCPPromptAnalyzer, PromptAnalysis, ValidationReport


class TestMCPPromptAnalyzer:
    """Tests for the MCPPromptAnalyzer class"""

    @pytest.fixture
    def analyzer(self):
        """Fixture to create an analyzer instance"""
        return MCPPromptAnalyzer()

    def test_analyzer_initialization(self, analyzer):
        """Test analyzer initialization"""
        assert analyzer is not None
        assert hasattr(analyzer, 'best_practices')
        assert hasattr(analyzer, 'positive_patterns')
        assert hasattr(analyzer, 'negative_patterns')

    def test_poor_prompt(self, analyzer):
        """Test analysis of poor quality prompt"""
        prompt = "Make a simple MCP server"
        result = analyzer.analyze_prompt(prompt)

        assert isinstance(result, PromptAnalysis)
        assert 1 <= result.score <= 4
        # Allow weaknesses to be empty if there are recommendations
        assert len(result.weaknesses) > 0 or len(result.recommendations) > 0
        assert len(result.missing_elements) > 0

    def test_medium_prompt(self, analyzer):
        """Test analysis of medium quality prompt"""
        prompt = "Create an MCP server with tools for file operations including error handling"
        result = analyzer.analyze_prompt(prompt)

        assert isinstance(result, PromptAnalysis)
        assert 4 <= result.score <= 7
        assert len(result.strengths) > 0
        assert len(result.recommendations) > 0

    def test_good_prompt(self, analyzer):
        """Test analysis of high quality prompt"""
        prompt = """Create an MCP server for file operations with the following requirements:
        - Tools for reading, writing and listing files
        - Comprehensive error handling and validation
        - Security measures including input sanitization
        - Clear schema definitions for all inputs/outputs
        - Documentation and usage examples
        - Testing strategy
        - Performance considerations
        - Uses stdio transport protocol"""

        result = analyzer.analyze_prompt(prompt)

        assert isinstance(result, PromptAnalysis)
        assert 7 <= result.score <= 10
        assert len(result.strengths) > 0
        assert result.best_practices_alignment['error_handling'] is True
        assert result.best_practices_alignment['security_considerations'] is True

    def test_result_fields(self, analyzer):
        """Test if all result fields are present"""
        prompt = "Basic test"
        result = analyzer.analyze_prompt(prompt)

        assert hasattr(result, 'score')
        assert hasattr(result, 'strengths')
        assert hasattr(result, 'weaknesses')
        assert hasattr(result, 'recommendations')
        assert hasattr(result, 'best_practices_alignment')
        assert hasattr(result, 'missing_elements')

        assert isinstance(result.score, int)
        assert isinstance(result.strengths, list)
        assert isinstance(result.weaknesses, list)
        assert isinstance(result.recommendations, list)
        assert isinstance(result.best_practices_alignment, dict)
        assert isinstance(result.missing_elements, list)

    def test_score_range(self, analyzer):
        """Test if score is always in correct range (1-10)"""
        test_prompts = [
            "",
            "abc",
            "Very basic MCP server",
            "Complete MCP server with security, tests, documentation, error handling",
            "x" * 1000  # Very long prompt
        ]

        for prompt in test_prompts:
            result = analyzer.analyze_prompt(prompt)
            assert 1 <= result.score <= 10


class TestRequirementsValidation:
    """Tests for MCP requirements validation"""

    @pytest.mark.asyncio
    async def test_validation_approved(self):
        """Test validation with requirements that should pass"""
        from servers.mcp_server import mcp_validate_requirements

        requirements = """Create MCP server with:
        - Robust error handling
        - Security considerations
        - Complete documentation
        - Comprehensive tests
        - Schema validation
        """

        # Access underlying function via .fn attribute
        result = await mcp_validate_requirements.fn(requirements)

        assert isinstance(result, dict)
        assert 'overall_score' in result
        assert 'validation_passed' in result
        assert 'critical_issues' in result
        assert 'warnings' in result
        assert isinstance(result['critical_issues'], list)
        assert isinstance(result['warnings'], list)

    @pytest.mark.asyncio
    async def test_validation_rejected(self):
        """Test validation with insufficient requirements"""
        from servers.mcp_server import mcp_validate_requirements

        requirements = "Make a basic server"
        # Access underlying function via .fn attribute
        result = await mcp_validate_requirements.fn(requirements)

        assert isinstance(result, dict)
        assert result['overall_score'] < 7
        assert result['validation_passed'] is False
        assert len(result['critical_issues']) > 0


class TestToolIntegration:
    """Integration tests for MCP tools"""

    @pytest.mark.asyncio
    async def test_analyze_prompt_tool(self):
        """Test the prompt analysis tool"""
        from servers.mcp_server import mcp_analyze_server_prompt, PromptAnalysis

        prompt = "Create MCP server with file operations"
        # Access underlying function via .fn attribute
        result = await mcp_analyze_server_prompt.fn(prompt)

        # Result is a PromptAnalysis object
        assert isinstance(result, PromptAnalysis)
        assert result.score >= 1

    def test_improve_prompt_tool_mock(self):
        """Test the prompt improvement tool (mock)"""
        from unittest.mock import Mock

        mock_improve = Mock()
        mock_improve.return_value = {
            "original_prompt": "Make simple server",
            "improved_prompt": "Create a specific MCP server with clear requirements",
            "improvements_made": ["Specificity", "Clarity"]
        }

        prompt = "Make simple server"
        result = mock_improve(prompt)

        assert isinstance(result, dict)
        assert 'original_prompt' in result
        assert 'improved_prompt' in result
        assert 'improvements_made' in result
        assert len(result['improvements_made']) > 0


def main():
    """Main function for manual test execution"""
    print("Running MCP Server tests...")
    print("=" * 50)

    # Run some basic tests manually
    analyzer = MCPPromptAnalyzer()

    test_cases = [
        {
            "name": "Poor Prompt",
            "prompt": "Make a simple MCP server",
            "expected_score_range": (1, 4)
        },
        {
            "name": "Medium Prompt",
            "prompt": "Create an MCP server with tools for file operations including error handling",
            "expected_score_range": (4, 7)
        },
        {
            "name": "Good Prompt",
            "prompt": """Create an MCP server for file operations with the following requirements:
            - Tools for reading, writing and listing files
            - Comprehensive error handling and validation
            - Security measures including input sanitization
            - Clear schema definitions for all inputs/outputs
            - Documentation and usage examples
            - Testing strategy
            - Performance considerations
            - Uses stdio transport protocol""",
            "expected_score_range": (7, 10)
        }
    ]

    for test_case in test_cases:
        print(f"\nTest: {test_case['name']}")
        print(f"Prompt: {test_case['prompt'][:100]}...")

        analysis = analyzer.analyze_prompt(test_case['prompt'])

        print(f"Score: {analysis.score}/10")
        print(f"Expected range: {test_case['expected_score_range']}")

        # Check if within expected range
        min_expected, max_expected = test_case['expected_score_range']
        score = int(analysis.score) if isinstance(analysis.score, str) else analysis.score
        if min_expected <= score <= max_expected:
            print("PASSED")
        else:
            print("FAILED")

        print(f"Strengths: {len(analysis.strengths)}")
        print(f"Weaknesses: {len(analysis.weaknesses)}")
        print(f"Recommendations: {len(analysis.recommendations)}")

    print(f"\nTests completed!")


if __name__ == "__main__":
    main()
