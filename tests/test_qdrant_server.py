#!/usr/bin/env python3
"""
Tests for Qdrant Vector Server - MCP server for vector search and RAG.

Tests cover collection management, search queries, and filter patterns.
"""

import pytest
from unittest.mock import AsyncMock

try:
    from servers.qdrant_server import (
        analyze_qdrant_query,
        generate_collection_config,
        generate_qdrant_query,
        optimize_vector_search,
        get_qdrant_patterns,
        QdrantKnowledgeBase
    )
    QDRANT_SERVER_AVAILABLE = True
except ImportError as e:
    print(f"Qdrant Server not available: {e}")
    QDRANT_SERVER_AVAILABLE = False


class TestQdrantKnowledgeBase:
    """Tests for Qdrant knowledge base"""

    @pytest.mark.skipif(not QDRANT_SERVER_AVAILABLE, reason="Qdrant Server not available")
    def test_collection_patterns_exist(self):
        """Test that collection patterns are defined"""
        kb = QdrantKnowledgeBase()
        assert hasattr(kb, 'COLLECTION_PATTERNS')

    @pytest.mark.skipif(not QDRANT_SERVER_AVAILABLE, reason="Qdrant Server not available")
    def test_search_patterns_exist(self):
        """Test that search patterns are defined"""
        kb = QdrantKnowledgeBase()
        assert hasattr(kb, 'SEARCH_PATTERNS')

    @pytest.mark.skipif(not QDRANT_SERVER_AVAILABLE, reason="Qdrant Server not available")
    def test_filter_patterns_exist(self):
        """Test that filter patterns are defined"""
        kb = QdrantKnowledgeBase()
        assert hasattr(kb, 'FILTER_PATTERNS')

    @pytest.mark.skipif(not QDRANT_SERVER_AVAILABLE, reason="Qdrant Server not available")
    def test_rag_patterns_exist(self):
        """Test that RAG patterns are defined"""
        kb = QdrantKnowledgeBase()
        assert hasattr(kb, 'RAG_PATTERNS')


class TestQdrantAnalysisFunctions:
    """Tests for Qdrant Server analysis functions"""

    @pytest.mark.skipif(not QDRANT_SERVER_AVAILABLE, reason="Qdrant Server not available")
    @pytest.mark.asyncio
    async def test_analyze_qdrant_query_basic(self):
        """Test basic Qdrant query analysis"""
        qdrant_query = """
        client.search(
            collection_name="documents",
            query_vector=embedding,
            limit=10,
            with_payload=True
        )
        """

        result = await analyze_qdrant_query(qdrant_query)

        assert isinstance(result, dict)
        assert "score" in result
        assert 0 <= result["score"] <= 100
        assert "suggestions" in result

    @pytest.mark.skipif(not QDRANT_SERVER_AVAILABLE, reason="Qdrant Server not available")
    @pytest.mark.asyncio
    async def test_analyze_qdrant_query_with_filter(self):
        """Test Qdrant query analysis with filters"""
        qdrant_query = """
        client.search(
            collection_name="documents",
            query_vector=embedding,
            query_filter=Filter(
                must=[
                    FieldCondition(
                        key="category",
                        match=MatchValue(value="tech")
                    )
                ]
            ),
            limit=10
        )
        """

        result = await analyze_qdrant_query(qdrant_query)
        assert result["score"] >= 50  # Filter usage should boost score

    @pytest.mark.skipif(not QDRANT_SERVER_AVAILABLE, reason="Qdrant Server not available")
    @pytest.mark.asyncio
    async def test_generate_collection_config(self):
        """Test collection configuration generation"""
        result = await generate_collection_config(
            name="documents",
            vector_size=1536,
            distance="Cosine"
        )

        assert isinstance(result, dict)
        assert "collection_name" in result
        assert "config" in result

    @pytest.mark.skipif(not QDRANT_SERVER_AVAILABLE, reason="Qdrant Server not available")
    @pytest.mark.asyncio
    async def test_generate_qdrant_query(self):
        """Test Qdrant query generation"""
        result = await generate_qdrant_query(
            operation="search",
            collection="documents"
        )

        assert isinstance(result, dict)
        assert "code" in result

    @pytest.mark.skipif(not QDRANT_SERVER_AVAILABLE, reason="Qdrant Server not available")
    @pytest.mark.asyncio
    async def test_optimize_vector_search(self):
        """Test vector search optimization"""
        original_query = """
        client.search(
            collection_name="docs",
            query_vector=vec,
            limit=100
        )
        """

        result = await optimize_vector_search(original_query)

        assert isinstance(result, dict)
        assert "optimized_code" in result
        assert "improvements" in result

    @pytest.mark.skipif(not QDRANT_SERVER_AVAILABLE, reason="Qdrant Server not available")
    @pytest.mark.asyncio
    async def test_get_qdrant_patterns_all(self):
        """Test getting all Qdrant patterns"""
        result = await get_qdrant_patterns()

        assert isinstance(result, dict)
        assert "categories" in result
        assert "collection" in result["categories"]
        assert "search" in result["categories"]

    @pytest.mark.skipif(not QDRANT_SERVER_AVAILABLE, reason="Qdrant Server not available")
    @pytest.mark.asyncio
    async def test_get_qdrant_patterns_by_category(self):
        """Test getting patterns by category"""
        result = await get_qdrant_patterns(category="filter")

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
