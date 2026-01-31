#!/usr/bin/env python3
"""
Tests for Neo4j Cypher Server - MCP server for graph database development.

Tests cover Cypher queries, graph modeling, and optimization patterns.
"""

import pytest
from unittest.mock import AsyncMock

try:
    from servers.neo4j_server import (
        analyze_cypher_query,
        generate_cypher_query,
        optimize_cypher,
        get_cypher_patterns,
        generate_graph_model,
        Neo4jKnowledgeBase
    )
    NEO4J_SERVER_AVAILABLE = True
except ImportError as e:
    print(f"Neo4j Server not available: {e}")
    NEO4J_SERVER_AVAILABLE = False


class TestNeo4jKnowledgeBase:
    """Tests for Neo4j knowledge base"""

    @pytest.mark.skipif(not NEO4J_SERVER_AVAILABLE, reason="Neo4j Server not available")
    def test_match_patterns_exist(self):
        """Test that MATCH patterns are defined"""
        kb = Neo4jKnowledgeBase()
        assert hasattr(kb, 'MATCH_PATTERNS')

    @pytest.mark.skipif(not NEO4J_SERVER_AVAILABLE, reason="Neo4j Server not available")
    def test_create_patterns_exist(self):
        """Test that CREATE patterns are defined"""
        kb = Neo4jKnowledgeBase()
        assert hasattr(kb, 'CREATE_PATTERNS')

    @pytest.mark.skipif(not NEO4J_SERVER_AVAILABLE, reason="Neo4j Server not available")
    def test_path_patterns_exist(self):
        """Test that path patterns are defined"""
        kb = Neo4jKnowledgeBase()
        assert hasattr(kb, 'PATH_PATTERNS')


class TestNeo4jAnalysisFunctions:
    """Tests for Neo4j Server analysis functions"""

    @pytest.mark.skipif(not NEO4J_SERVER_AVAILABLE, reason="Neo4j Server not available")
    @pytest.mark.asyncio
    async def test_analyze_cypher_query_basic(self):
        """Test basic Cypher query analysis"""
        cypher_query = """
        MATCH (u:User)-[:FOLLOWS]->(f:User)
        WHERE u.name = $name
        RETURN f.name, f.email
        """

        result = await analyze_cypher_query(cypher_query)

        assert isinstance(result, dict)
        assert "score" in result
        assert 0 <= result["score"] <= 100
        assert "suggestions" in result

    @pytest.mark.skipif(not NEO4J_SERVER_AVAILABLE, reason="Neo4j Server not available")
    @pytest.mark.asyncio
    async def test_analyze_cypher_query_with_index(self):
        """Test Cypher query analysis with index usage"""
        cypher_query = """
        MATCH (u:User)
        WHERE u.id = $userId
        RETURN u
        """

        result = await analyze_cypher_query(cypher_query)
        assert result["score"] >= 40  # Simple parameterized query

    @pytest.mark.skipif(not NEO4J_SERVER_AVAILABLE, reason="Neo4j Server not available")
    @pytest.mark.asyncio
    async def test_generate_cypher_query(self):
        """Test Cypher query generation"""
        result = await generate_cypher_query(
            operation="find",
            node_type="User",
            conditions=["name", "email"]
        )

        assert isinstance(result, dict)
        assert "query" in result
        assert "MATCH" in result["query"]

    @pytest.mark.skipif(not NEO4J_SERVER_AVAILABLE, reason="Neo4j Server not available")
    @pytest.mark.asyncio
    async def test_optimize_cypher(self):
        """Test Cypher query optimization"""
        original_query = """
        MATCH (n:User)
        WHERE n.name = 'John'
        RETURN n
        """

        result = await optimize_cypher(original_query)

        assert isinstance(result, dict)
        assert "optimized_query" in result
        assert "improvements" in result

    @pytest.mark.skipif(not NEO4J_SERVER_AVAILABLE, reason="Neo4j Server not available")
    @pytest.mark.asyncio
    async def test_generate_graph_model(self):
        """Test graph model generation"""
        result = await generate_graph_model(
            domain="social_network",
            entities=["User", "Post", "Comment"]
        )

        assert isinstance(result, dict)
        assert "nodes" in result
        assert "relationships" in result

    @pytest.mark.skipif(not NEO4J_SERVER_AVAILABLE, reason="Neo4j Server not available")
    @pytest.mark.asyncio
    async def test_get_cypher_patterns_all(self):
        """Test getting all Cypher patterns"""
        result = await get_cypher_patterns()

        assert isinstance(result, dict)
        assert "categories" in result
        assert "match" in result["categories"]
        assert "create" in result["categories"]

    @pytest.mark.skipif(not NEO4J_SERVER_AVAILABLE, reason="Neo4j Server not available")
    @pytest.mark.asyncio
    async def test_get_cypher_patterns_by_category(self):
        """Test getting patterns by category"""
        result = await get_cypher_patterns(category="match")

        assert isinstance(result, dict)
        assert "category" in result
        assert "patterns" in result


@pytest.fixture
def mock_context():
    """Fixture for mocking Context"""
    context = AsyncMock()
    return context


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
