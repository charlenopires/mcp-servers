#!/usr/bin/env python3
"""
Qdrant Vector Database MCP Server
=================================

Advanced MCP server for Qdrant vector database development, featuring:
- Vector search query analysis and optimization
- Collection configuration patterns
- Filtering and hybrid search strategies
- Embedding management patterns
- RAG (Retrieval Augmented Generation) patterns
- Payload optimization

Based on: Qdrant documentation, Vector search best practices
"""

import asyncio
import json
import re
import logging
from dataclasses import dataclass
from typing import Dict, List, Optional, Any, Tuple, Union
from enum import Enum
from fastmcp import FastMCP, Context
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP(
    name="Qdrant Vector Database Server",
    instructions="""Advanced MCP server for Qdrant vector database development.

This server provides Qdrant development expertise:
- Vector search query analysis and optimization
- Collection configuration and management
- Filter strategies for hybrid search
- Embedding and payload patterns
- RAG implementation patterns
- Performance optimization

Use these tools to build efficient vector search applications.""",
    version="3.0.0"
)

# ================================
# QDRANT PATTERNS & KNOWLEDGE BASE
# ================================

class QdrantCategory(Enum):
    """Qdrant pattern categories"""
    COLLECTION = "collection"
    SEARCH = "search"
    FILTER = "filter"
    VECTOR = "vector"
    PAYLOAD = "payload"
    BATCH = "batch"
    OPTIMIZATION = "optimization"

class SearchType(Enum):
    """Search types"""
    DENSE = "dense"
    SPARSE = "sparse"
    HYBRID = "hybrid"
    MULTI_VECTOR = "multi_vector"

@dataclass
class QdrantAnalysisResult:
    """Result of Qdrant query analysis"""
    query: Dict[str, Any]
    score: int
    category_scores: Dict[str, int]
    patterns_found: List[str]
    anti_patterns: List[str]
    suggestions: List[str]
    optimized_query: Optional[Dict[str, Any]]

class QdrantKnowledgeBase:
    """Qdrant knowledge base with patterns and best practices"""

    VERSION = "1.9.x"

    # Collection Configuration Patterns
    COLLECTION_PATTERNS = {
        "basic_collection": {
            "description": "Create basic collection with dense vectors",
            "endpoint": "PUT /collections/{collection_name}",
            "example": {
                "vectors": {
                    "size": 768,
                    "distance": "Cosine"
                }
            },
            "python": '''from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(host="localhost", port=6333)

client.create_collection(
    collection_name="documents",
    vectors_config=VectorParams(
        size=768,  # OpenAI embedding size
        distance=Distance.COSINE
    )
)'''
        },
        "multi_vector_collection": {
            "description": "Collection with multiple named vectors",
            "endpoint": "PUT /collections/{collection_name}",
            "example": {
                "vectors": {
                    "text": {"size": 768, "distance": "Cosine"},
                    "image": {"size": 512, "distance": "Cosine"}
                }
            },
            "python": '''client.create_collection(
    collection_name="products",
    vectors_config={
        "text": VectorParams(size=768, distance=Distance.COSINE),
        "image": VectorParams(size=512, distance=Distance.COSINE)
    }
)'''
        },
        "sparse_vector_collection": {
            "description": "Collection with sparse vectors for keyword search",
            "endpoint": "PUT /collections/{collection_name}",
            "example": {
                "vectors": {"size": 768, "distance": "Cosine"},
                "sparse_vectors": {
                    "keywords": {}
                }
            },
            "python": '''from qdrant_client.models import SparseVectorParams

client.create_collection(
    collection_name="hybrid_search",
    vectors_config=VectorParams(size=768, distance=Distance.COSINE),
    sparse_vectors_config={
        "keywords": SparseVectorParams()
    }
)'''
        },
        "optimized_collection": {
            "description": "Collection optimized for production",
            "endpoint": "PUT /collections/{collection_name}",
            "example": {
                "vectors": {
                    "size": 768,
                    "distance": "Cosine",
                    "on_disk": True
                },
                "optimizers_config": {
                    "default_segment_number": 4,
                    "indexing_threshold": 20000
                },
                "hnsw_config": {
                    "m": 16,
                    "ef_construct": 100
                }
            },
            "python": '''from qdrant_client.models import HnswConfigDiff, OptimizersConfigDiff

client.create_collection(
    collection_name="production",
    vectors_config=VectorParams(
        size=768,
        distance=Distance.COSINE,
        on_disk=True  # Store vectors on disk for large collections
    ),
    optimizers_config=OptimizersConfigDiff(
        default_segment_number=4,
        indexing_threshold=20000
    ),
    hnsw_config=HnswConfigDiff(
        m=16,  # Number of edges per node
        ef_construct=100  # Construction time accuracy
    )
)'''
        }
    }

    # Search Patterns
    SEARCH_PATTERNS = {
        "basic_search": {
            "description": "Basic vector similarity search",
            "endpoint": "POST /collections/{name}/points/query",
            "example": {
                "query": [0.2, 0.1, 0.9, 0.7],
                "limit": 10,
                "with_payload": True
            },
            "python": '''results = client.query_points(
    collection_name="documents",
    query=[0.2, 0.1, 0.9, 0.7],  # Query vector
    limit=10,
    with_payload=True
)

for point in results.points:
    print(f"ID: {point.id}, Score: {point.score}")
    print(f"Payload: {point.payload}")'''
        },
        "filtered_search": {
            "description": "Vector search with filter conditions",
            "endpoint": "POST /collections/{name}/points/query",
            "example": {
                "query": [0.2, 0.1, 0.9, 0.7],
                "filter": {
                    "must": [
                        {"key": "category", "match": {"value": "technology"}},
                        {"key": "year", "range": {"gte": 2023}}
                    ]
                },
                "limit": 10
            },
            "python": '''from qdrant_client.models import Filter, FieldCondition, MatchValue, Range

results = client.query_points(
    collection_name="documents",
    query=[0.2, 0.1, 0.9, 0.7],
    query_filter=Filter(
        must=[
            FieldCondition(
                key="category",
                match=MatchValue(value="technology")
            ),
            FieldCondition(
                key="year",
                range=Range(gte=2023)
            )
        ]
    ),
    limit=10
)'''
        },
        "hybrid_search": {
            "description": "Combine dense and sparse vectors",
            "endpoint": "POST /collections/{name}/points/query",
            "example": {
                "prefetch": [
                    {
                        "query": {"indices": [1, 42, 100], "values": [0.5, 0.8, 0.3]},
                        "using": "keywords",
                        "limit": 100
                    },
                    {
                        "query": [0.2, 0.1, 0.9, 0.7],
                        "limit": 100
                    }
                ],
                "query": {"fusion": "rrf"},
                "limit": 10
            },
            "python": '''from qdrant_client.models import SparseVector, Prefetch, FusionQuery

results = client.query_points(
    collection_name="hybrid_search",
    prefetch=[
        Prefetch(
            query=SparseVector(
                indices=[1, 42, 100],
                values=[0.5, 0.8, 0.3]
            ),
            using="keywords",
            limit=100
        ),
        Prefetch(
            query=[0.2, 0.1, 0.9, 0.7],  # Dense vector
            limit=100
        )
    ],
    query=FusionQuery(fusion="rrf"),  # Reciprocal Rank Fusion
    limit=10
)'''
        },
        "multi_vector_search": {
            "description": "Search using multiple named vectors",
            "endpoint": "POST /collections/{name}/points/query",
            "example": {
                "query": [0.2, 0.1, 0.9, 0.7],
                "using": "text",
                "limit": 10
            },
            "python": '''# Search by text embedding
text_results = client.query_points(
    collection_name="products",
    query=text_embedding,
    using="text",
    limit=10
)

# Search by image embedding
image_results = client.query_points(
    collection_name="products",
    query=image_embedding,
    using="image",
    limit=10
)'''
        },
        "scroll_search": {
            "description": "Iterate through all points with optional filter",
            "endpoint": "POST /collections/{name}/points/scroll",
            "example": {
                "filter": {"must": [{"key": "status", "match": {"value": "active"}}]},
                "limit": 100,
                "with_payload": True,
                "with_vector": False
            },
            "python": '''# Iterate through all points
offset = None
while True:
    results, offset = client.scroll(
        collection_name="documents",
        scroll_filter=Filter(
            must=[FieldCondition(key="status", match=MatchValue(value="active"))]
        ),
        limit=100,
        offset=offset,
        with_payload=True,
        with_vectors=False
    )

    if not results:
        break

    for point in results:
        process_point(point)'''
        },
        "recommend_search": {
            "description": "Get recommendations based on existing points",
            "endpoint": "POST /collections/{name}/points/recommend",
            "example": {
                "positive": [100, 231],
                "negative": [718],
                "limit": 10
            },
            "python": '''# Recommend similar to points 100, 231 but not like 718
results = client.recommend(
    collection_name="products",
    positive=[100, 231],  # Point IDs to find similar
    negative=[718],  # Point IDs to avoid
    limit=10
)'''
        }
    }

    # Filter Patterns
    FILTER_PATTERNS = {
        "must_filter": {
            "description": "All conditions must match (AND)",
            "example": {
                "must": [
                    {"key": "city", "match": {"value": "London"}},
                    {"key": "price", "range": {"lte": 100}}
                ]
            }
        },
        "should_filter": {
            "description": "At least one condition must match (OR)",
            "example": {
                "should": [
                    {"key": "color", "match": {"value": "red"}},
                    {"key": "color", "match": {"value": "blue"}}
                ]
            }
        },
        "must_not_filter": {
            "description": "Conditions must NOT match",
            "example": {
                "must_not": [
                    {"key": "status", "match": {"value": "deleted"}}
                ]
            }
        },
        "nested_filter": {
            "description": "Filter on nested object properties",
            "example": {
                "must": [
                    {"key": "metadata.author", "match": {"value": "John"}},
                    {"key": "metadata.tags", "match": {"any": ["python", "rust"]}}
                ]
            }
        },
        "geo_filter": {
            "description": "Geographic location filter",
            "example": {
                "must": [
                    {
                        "key": "location",
                        "geo_radius": {
                            "center": {"lat": 51.5074, "lon": -0.1278},
                            "radius": 10000
                        }
                    }
                ]
            }
        },
        "datetime_filter": {
            "description": "Filter by datetime range",
            "example": {
                "must": [
                    {
                        "key": "created_at",
                        "range": {
                            "gte": "2024-01-01T00:00:00Z",
                            "lt": "2024-12-31T23:59:59Z"
                        }
                    }
                ]
            }
        }
    }

    # Upsert Patterns
    UPSERT_PATTERNS = {
        "single_upsert": {
            "description": "Insert or update single point",
            "endpoint": "PUT /collections/{name}/points",
            "example": {
                "points": [
                    {
                        "id": 1,
                        "vector": [0.2, 0.1, 0.9, 0.7],
                        "payload": {"title": "Document 1", "category": "tech"}
                    }
                ]
            },
            "python": '''from qdrant_client.models import PointStruct

client.upsert(
    collection_name="documents",
    points=[
        PointStruct(
            id=1,
            vector=[0.2, 0.1, 0.9, 0.7],
            payload={"title": "Document 1", "category": "tech"}
        )
    ]
)'''
        },
        "batch_upsert": {
            "description": "Batch insert points",
            "endpoint": "PUT /collections/{name}/points",
            "example": {
                "points": [
                    {"id": 1, "vector": [0.1, 0.2, 0.3], "payload": {"text": "doc1"}},
                    {"id": 2, "vector": [0.4, 0.5, 0.6], "payload": {"text": "doc2"}}
                ]
            },
            "python": '''# Batch upsert with progress
points = [
    PointStruct(id=i, vector=embeddings[i], payload=payloads[i])
    for i in range(len(embeddings))
]

# Upload in batches of 100
batch_size = 100
for i in range(0, len(points), batch_size):
    batch = points[i:i + batch_size]
    client.upsert(
        collection_name="documents",
        points=batch
    )
    print(f"Uploaded {min(i + batch_size, len(points))}/{len(points)}")'''
        },
        "named_vector_upsert": {
            "description": "Upsert with multiple named vectors",
            "endpoint": "PUT /collections/{name}/points",
            "example": {
                "points": [
                    {
                        "id": 1,
                        "vector": {
                            "text": [0.1, 0.2, 0.3],
                            "image": [0.4, 0.5, 0.6]
                        },
                        "payload": {"title": "Product 1"}
                    }
                ]
            },
            "python": '''client.upsert(
    collection_name="products",
    points=[
        PointStruct(
            id=1,
            vector={
                "text": text_embedding,
                "image": image_embedding
            },
            payload={"title": "Product 1", "price": 99.99}
        )
    ]
)'''
        }
    }

    # RAG Patterns
    RAG_PATTERNS = {
        "basic_rag": {
            "description": "Basic RAG retrieval pattern",
            "python": '''async def rag_retrieve(query: str, top_k: int = 5):
    # 1. Generate query embedding
    query_embedding = await embed_text(query)

    # 2. Search for relevant documents
    results = client.query_points(
        collection_name="documents",
        query=query_embedding,
        limit=top_k,
        with_payload=True
    )

    # 3. Extract context from results
    context = "\\n\\n".join([
        point.payload.get("text", "")
        for point in results.points
    ])

    return context, results.points'''
        },
        "filtered_rag": {
            "description": "RAG with metadata filtering",
            "python": '''async def filtered_rag_retrieve(
    query: str,
    category: str,
    min_date: str,
    top_k: int = 5
):
    query_embedding = await embed_text(query)

    results = client.query_points(
        collection_name="documents",
        query=query_embedding,
        query_filter=Filter(
            must=[
                FieldCondition(key="category", match=MatchValue(value=category)),
                FieldCondition(key="date", range=Range(gte=min_date))
            ]
        ),
        limit=top_k,
        with_payload=True
    )

    return format_context(results.points)'''
        },
        "reranking_rag": {
            "description": "RAG with reranking step",
            "python": '''async def reranking_rag_retrieve(query: str, top_k: int = 5):
    query_embedding = await embed_text(query)

    # 1. Initial retrieval (over-fetch)
    results = client.query_points(
        collection_name="documents",
        query=query_embedding,
        limit=top_k * 3,  # Over-fetch for reranking
        with_payload=True
    )

    # 2. Rerank with cross-encoder
    documents = [p.payload["text"] for p in results.points]
    reranked = reranker.rerank(query, documents)

    # 3. Return top-k after reranking
    return reranked[:top_k]'''
        },
        "hybrid_rag": {
            "description": "Hybrid search RAG (dense + sparse)",
            "python": '''async def hybrid_rag_retrieve(query: str, top_k: int = 5):
    # Generate both embeddings
    dense_embedding = await embed_text(query)
    sparse_embedding = generate_sparse_embedding(query)

    # Hybrid search with RRF fusion
    results = client.query_points(
        collection_name="hybrid_docs",
        prefetch=[
            Prefetch(query=sparse_embedding, using="keywords", limit=100),
            Prefetch(query=dense_embedding, limit=100)
        ],
        query=FusionQuery(fusion="rrf"),
        limit=top_k,
        with_payload=True
    )

    return format_context(results.points)'''
        }
    }

    # Index Patterns
    INDEX_PATTERNS = {
        "payload_index": {
            "description": "Create index on payload field",
            "endpoint": "PUT /collections/{name}/index",
            "example": {
                "field_name": "category",
                "field_schema": "keyword"
            },
            "python": '''# Create keyword index for exact matching
client.create_payload_index(
    collection_name="documents",
    field_name="category",
    field_schema="keyword"
)

# Create integer index for range queries
client.create_payload_index(
    collection_name="documents",
    field_name="year",
    field_schema="integer"
)

# Create text index for full-text search
client.create_payload_index(
    collection_name="documents",
    field_name="content",
    field_schema="text"
)'''
        }
    }


class QdrantAnalyzer:
    """Qdrant query analyzer"""

    def __init__(self):
        self.knowledge_base = QdrantKnowledgeBase()

    async def analyze_query(self, query: Dict[str, Any]) -> QdrantAnalysisResult:
        """Analyze Qdrant query for patterns and optimization"""

        score = 50
        category_scores = {}
        patterns_found = []
        anti_patterns = []
        suggestions = []
        optimized_query = None

        # Analyze vector configuration
        vector_score = await self._analyze_vector_usage(query)
        category_scores["vector"] = vector_score
        score += (vector_score - 50) * 0.25

        # Analyze filter usage
        filter_score = await self._analyze_filters(query)
        category_scores["filter"] = filter_score
        score += (filter_score - 50) * 0.25

        # Analyze query structure
        structure_score = await self._analyze_structure(query)
        category_scores["structure"] = structure_score
        score += (structure_score - 50) * 0.2

        # Analyze performance considerations
        perf_score = await self._analyze_performance(query)
        category_scores["performance"] = perf_score
        score += (perf_score - 50) * 0.15

        # Analyze payload handling
        payload_score = await self._analyze_payload(query)
        category_scores["payload"] = payload_score
        score += (payload_score - 50) * 0.15

        # Generate suggestions
        suggestions = await self._generate_suggestions(category_scores, query)

        # Check for anti-patterns
        anti_patterns = await self._check_anti_patterns(query)
        score -= len(anti_patterns) * 5

        # Generate optimized query if needed
        if score < 80:
            optimized_query = await self._optimize_query(query)

        final_score = max(0, min(100, int(score)))

        return QdrantAnalysisResult(
            query=query,
            score=final_score,
            category_scores=category_scores,
            patterns_found=patterns_found,
            anti_patterns=anti_patterns,
            suggestions=suggestions,
            optimized_query=optimized_query
        )

    async def _analyze_vector_usage(self, query: Dict[str, Any]) -> int:
        """Analyze vector usage in query"""
        score = 50

        # Check for query vector
        if "query" in query:
            score += 20

        # Check for named vector usage
        if "using" in query:
            score += 10

        # Check for prefetch (hybrid search)
        if "prefetch" in query:
            score += 15

        return min(100, max(0, score))

    async def _analyze_filters(self, query: Dict[str, Any]) -> int:
        """Analyze filter configuration"""
        score = 50

        filter_obj = query.get("filter", query.get("query_filter", {}))

        # Check for filter presence
        if filter_obj:
            score += 15

            # Check for indexed field usage
            if "must" in filter_obj or "should" in filter_obj:
                score += 15

            # Check for range filters (need proper indexes)
            must = filter_obj.get("must", [])
            if any("range" in cond for cond in must if isinstance(cond, dict)):
                score += 10

        return min(100, max(0, score))

    async def _analyze_structure(self, query: Dict[str, Any]) -> int:
        """Analyze query structure"""
        score = 50

        # Check for limit
        if "limit" in query:
            score += 15

        # Check for with_payload specification
        if "with_payload" in query:
            score += 10

        # Check for score_threshold
        if "score_threshold" in query:
            score += 10

        return min(100, max(0, score))

    async def _analyze_performance(self, query: Dict[str, Any]) -> int:
        """Analyze performance considerations"""
        score = 50

        # Check for reasonable limit
        limit = query.get("limit", 100)
        if limit <= 100:
            score += 15
        elif limit > 1000:
            score -= 15

        # Check for with_vector (can be expensive)
        if query.get("with_vector") is False:
            score += 10

        # Check for offset usage (can be slow for large offsets)
        offset = query.get("offset", 0)
        if offset == 0:
            score += 10
        elif offset > 10000:
            score -= 20

        return min(100, max(0, score))

    async def _analyze_payload(self, query: Dict[str, Any]) -> int:
        """Analyze payload handling"""
        score = 50

        # Check for selective payload return
        with_payload = query.get("with_payload")
        if with_payload is False:
            score += 10  # Efficient
        elif isinstance(with_payload, dict):
            score += 15  # Selective include/exclude

        return min(100, max(0, score))

    async def _generate_suggestions(self, scores: Dict[str, int], query: Dict[str, Any]) -> List[str]:
        """Generate optimization suggestions"""
        suggestions = []

        if scores.get("filter", 50) < 70:
            suggestions.append("Add filters to narrow search space before vector comparison")

        if scores.get("performance", 50) < 70:
            suggestions.append("Use pagination instead of large offsets")
            suggestions.append("Consider setting with_vector=false if vectors not needed")

        if "limit" not in query:
            suggestions.append("Always specify limit to control result size")

        if query.get("limit", 10) > 100:
            suggestions.append("Consider reducing limit and using pagination for large result sets")

        if "score_threshold" not in query:
            suggestions.append("Consider using score_threshold to filter low-quality matches")

        return suggestions

    async def _check_anti_patterns(self, query: Dict[str, Any]) -> List[str]:
        """Check for anti-patterns"""
        anti_patterns = []

        # Large offset without scroll
        if query.get("offset", 0) > 10000:
            anti_patterns.append("Large offset can be slow - use scroll API instead")

        # Very large limit
        if query.get("limit", 10) > 1000:
            anti_patterns.append("Very large limit may cause memory issues")

        # Missing filters on large collections
        if not query.get("filter") and not query.get("query_filter"):
            anti_patterns.append("No filters - consider adding filters for large collections")

        return anti_patterns

    async def _optimize_query(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """Generate optimized query"""
        optimized = dict(query)

        # Add limit if missing
        if "limit" not in optimized:
            optimized["limit"] = 10

        # Add score_threshold if missing
        if "score_threshold" not in optimized:
            optimized["score_threshold"] = 0.7

        # Set with_vector to false if not specified
        if "with_vector" not in optimized:
            optimized["with_vector"] = False

        return optimized


class QdrantGenerator:
    """Qdrant configuration generator"""

    def __init__(self):
        self.knowledge_base = QdrantKnowledgeBase()

    async def generate_collection_config(
        self,
        name: str,
        vector_size: int,
        distance: str = "Cosine",
        on_disk: bool = False,
        multi_vector: bool = False,
        sparse_vectors: bool = False
    ) -> Dict[str, Any]:
        """Generate collection configuration"""

        config = {
            "collection_name": name,
            "vectors_config": {}
        }

        if multi_vector:
            config["vectors_config"] = {
                "text": {"size": vector_size, "distance": distance},
                "image": {"size": 512, "distance": distance}
            }
        else:
            config["vectors_config"] = {
                "size": vector_size,
                "distance": distance
            }

        if on_disk:
            config["vectors_config"]["on_disk"] = True

        if sparse_vectors:
            config["sparse_vectors_config"] = {
                "keywords": {}
            }

        # Add optimizers for production
        if on_disk:
            config["optimizers_config"] = {
                "default_segment_number": 4,
                "indexing_threshold": 20000
            }
            config["hnsw_config"] = {
                "m": 16,
                "ef_construct": 100
            }

        # Generate Python code
        python_code = self._generate_python_code(config)

        return {
            "config": config,
            "python_code": python_code,
            "http_request": {
                "method": "PUT",
                "url": f"/collections/{name}",
                "body": config
            }
        }

    def _generate_python_code(self, config: Dict[str, Any]) -> str:
        """Generate Python code for collection creation"""
        name = config["collection_name"]
        vectors = config["vectors_config"]

        if isinstance(vectors, dict) and "size" in vectors:
            # Single vector
            return f'''from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(host="localhost", port=6333)

client.create_collection(
    collection_name="{name}",
    vectors_config=VectorParams(
        size={vectors["size"]},
        distance=Distance.{vectors.get("distance", "COSINE").upper()}
    )
)'''
        else:
            # Multiple vectors
            vector_configs = "\n        ".join([
                f'"{k}": VectorParams(size={v["size"]}, distance=Distance.{v.get("distance", "COSINE").upper()}),'
                for k, v in vectors.items()
            ])
            return f'''from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(host="localhost", port=6333)

client.create_collection(
    collection_name="{name}",
    vectors_config={{
        {vector_configs}
    }}
)'''

    async def generate_search_query(
        self,
        search_type: str = "basic",
        with_filter: bool = False,
        filter_conditions: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Generate search query template"""

        templates = {
            "basic": {
                "query": "[0.1, 0.2, ...]",
                "limit": 10,
                "with_payload": True
            },
            "filtered": {
                "query": "[0.1, 0.2, ...]",
                "filter": filter_conditions or {
                    "must": [
                        {"key": "category", "match": {"value": "example"}}
                    ]
                },
                "limit": 10,
                "with_payload": True
            },
            "hybrid": {
                "prefetch": [
                    {"query": {"indices": [], "values": []}, "using": "keywords", "limit": 100},
                    {"query": "[dense vector]", "limit": 100}
                ],
                "query": {"fusion": "rrf"},
                "limit": 10
            },
            "recommend": {
                "positive": [1, 2, 3],
                "negative": [],
                "limit": 10
            }
        }

        template = templates.get(search_type, templates["basic"])

        if with_filter and search_type == "basic":
            template["filter"] = filter_conditions or {"must": []}

        return {
            "search_type": search_type,
            "template": template,
            "description": f"{search_type.title()} search query template"
        }


# ================================
# MCP TOOLS
# ================================

@mcp.tool(tags=["analysis", "qdrant", "scoring"])
async def analyze_qdrant_query(query: Dict[str, Any], ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Analyzes Qdrant query for patterns and optimization.

    Args:
        query: Qdrant query object to analyze

    Returns:
        Complete analysis with score and recommendations
    """
    try:
        analyzer = QdrantAnalyzer()
        analysis = await analyzer.analyze_query(query)

        logger.info(f"Analyzed Qdrant query - score: {analysis.score}")

        return {
            "score": analysis.score,
            "grade": (
                "Excellent" if analysis.score >= 90 else
                "Good" if analysis.score >= 75 else
                "Needs Optimization" if analysis.score >= 60 else
                "Poor"
            ),
            "category_scores": analysis.category_scores,
            "patterns_found": analysis.patterns_found,
            "anti_patterns": analysis.anti_patterns,
            "suggestions": analysis.suggestions,
            "optimized_query": analysis.optimized_query
        }

    except Exception as e:
        logger.error(f"Error analyzing Qdrant query: {str(e)}")
        raise


@mcp.tool(tags=["generation", "collection", "qdrant"])
async def generate_collection_config(
    name: str,
    vector_size: int = 768,
    distance: str = "Cosine",
    on_disk: bool = False,
    multi_vector: bool = False,
    sparse_vectors: bool = False,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Generates Qdrant collection configuration.

    Args:
        name: Collection name
        vector_size: Vector dimension size (default: 768 for OpenAI)
        distance: Distance metric (Cosine, Dot, Euclidean)
        on_disk: Store vectors on disk for large collections
        multi_vector: Create multiple named vectors
        sparse_vectors: Include sparse vectors for hybrid search

    Returns:
        Collection configuration with Python code
    """
    try:
        generator = QdrantGenerator()
        result = await generator.generate_collection_config(
            name, vector_size, distance, on_disk, multi_vector, sparse_vectors
        )

        logger.info(f"Generated collection config: {name}")

        return result

    except Exception as e:
        logger.error(f"Error generating collection config: {str(e)}")
        raise


@mcp.tool(tags=["generation", "search", "qdrant"])
async def generate_qdrant_query(
    search_type: str = "basic",
    with_filter: bool = False,
    filter_conditions: Optional[Dict[str, Any]] = None,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Generates Qdrant search query template.

    Args:
        search_type: Type of search (basic, filtered, hybrid, recommend)
        with_filter: Include filter in query
        filter_conditions: Filter conditions to include

    Returns:
        Search query template
    """
    try:
        generator = QdrantGenerator()
        result = await generator.generate_search_query(search_type, with_filter, filter_conditions)

        logger.info(f"Generated Qdrant query: {search_type}")

        return result

    except Exception as e:
        logger.error(f"Error generating Qdrant query: {str(e)}")
        raise


@mcp.tool(tags=["optimization", "search", "qdrant"])
async def optimize_vector_search(query: Dict[str, Any], ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Optimizes Qdrant vector search query.

    Args:
        query: Qdrant query to optimize

    Returns:
        Optimized query with explanations
    """
    try:
        analyzer = QdrantAnalyzer()
        analysis = await analyzer.analyze_query(query)

        optimizations = []
        optimized = dict(query)

        # Add limit if missing
        if "limit" not in optimized:
            optimized["limit"] = 10
            optimizations.append("Added default limit of 10")

        # Add score threshold
        if "score_threshold" not in optimized:
            optimized["score_threshold"] = 0.7
            optimizations.append("Added score_threshold to filter low-quality matches")

        # Optimize payload return
        if "with_payload" not in optimized:
            optimized["with_payload"] = True
            optimizations.append("Enabled payload return")

        # Disable vector return by default
        if "with_vector" not in optimized:
            optimized["with_vector"] = False
            optimizations.append("Disabled vector return for better performance")

        return {
            "original_query": query,
            "optimized_query": optimized,
            "optimizations_applied": optimizations,
            "original_score": analysis.score,
            "suggestions": analysis.suggestions
        }

    except Exception as e:
        logger.error(f"Error optimizing Qdrant query: {str(e)}")
        raise


@mcp.tool(tags=["patterns", "reference", "qdrant"])
async def get_qdrant_patterns(category: str = "all", ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Returns Qdrant patterns by category.

    Args:
        category: Pattern category (collection, search, filter, upsert, rag, index, all)

    Returns:
        Qdrant patterns with examples
    """
    try:
        kb = QdrantKnowledgeBase()

        categories = {
            "collection": kb.COLLECTION_PATTERNS,
            "search": kb.SEARCH_PATTERNS,
            "filter": kb.FILTER_PATTERNS,
            "upsert": kb.UPSERT_PATTERNS,
            "rag": kb.RAG_PATTERNS,
            "index": kb.INDEX_PATTERNS,
        }

        if category == "all":
            return {
                "qdrant_version": kb.VERSION,
                "categories": categories,
                "quick_reference": {
                    "search": "POST /collections/{name}/points/query",
                    "upsert": "PUT /collections/{name}/points",
                    "scroll": "POST /collections/{name}/points/scroll",
                    "recommend": "POST /collections/{name}/points/recommend"
                }
            }

        if category not in categories:
            return {"error": f"Category '{category}' not found. Available: {list(categories.keys())}"}

        return {
            "category": category,
            "patterns": categories[category]
        }

    except Exception as e:
        logger.error(f"Error getting Qdrant patterns: {str(e)}")
        raise


@mcp.tool(tags=["prompt", "analysis", "qdrant"])
async def analyze_qdrant_prompt(prompt: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Analyzes a prompt for Qdrant development.

    Args:
        prompt: User prompt to analyze

    Returns:
        Analysis with suggestions
    """
    try:
        score = 50
        suggestions = []
        missing = []

        # Check for operation type
        if any(op in prompt.lower() for op in ["search", "query", "find", "retrieve"]):
            score += 10
        elif any(op in prompt.lower() for op in ["create", "insert", "upsert", "add"]):
            score += 10
        elif any(op in prompt.lower() for op in ["collection", "setup", "configure"]):
            score += 10
        else:
            missing.append("Specify operation type (search, create, configure)")

        # Check for vector details
        if any(word in prompt.lower() for word in ["vector", "embedding", "dimension", "size"]):
            score += 10
        else:
            suggestions.append("Specify vector dimensions and embedding model")

        # Check for filter requirements
        if any(word in prompt.lower() for word in ["filter", "where", "condition", "category"]):
            score += 10
        else:
            suggestions.append("Consider specifying filter conditions")

        # Check for RAG context
        if any(word in prompt.lower() for word in ["rag", "retrieval", "context", "llm"]):
            score += 10

        # Check for performance considerations
        if any(word in prompt.lower() for word in ["optimize", "performance", "scale", "large"]):
            score += 10
        else:
            suggestions.append("Consider performance requirements for production")

        return {
            "score": min(100, score),
            "quality": (
                "Excellent" if score >= 90 else
                "Good" if score >= 70 else
                "Needs Details" if score >= 50 else
                "Incomplete"
            ),
            "suggestions": suggestions,
            "missing_elements": missing,
            "enhanced_prompt": f"""{prompt}

Additional requirements:
- Vector size and distance metric
- Filter conditions for narrowing results
- Payload fields to include/exclude
- Performance optimization (limit, score_threshold)
- Error handling for empty results"""
        }

    except Exception as e:
        logger.error(f"Error analyzing Qdrant prompt: {str(e)}")
        raise


# ================================
# MCP PROMPTS
# ================================

@mcp.prompt()
async def design_vector_schema(
    use_case: str,
    embedding_model: str = "OpenAI",
    features: List[str] = []
) -> List[Dict[str, str]]:
    """
    Generate prompt to design vector database schema.

    Args:
        use_case: Use case description
        embedding_model: Embedding model to use
        features: Required features
    """
    default_features = ["semantic search", "filtering", "pagination"]
    features_list = features if features else default_features

    return [
        {
            "role": "system",
            "content": """You are a Qdrant vector database expert.

Key design principles:
1. **Vector choice**: Dense for semantic, sparse for keyword, both for hybrid
2. **Distance metric**: Cosine for normalized, Dot for raw, Euclidean for clustering
3. **Payload indexing**: Index fields used in filters
4. **Collection sizing**: on_disk for >1M vectors
5. **Hybrid search**: Combine dense + sparse with RRF fusion

Performance considerations:
- Use payload indexes for filtered fields
- Limit result sizes
- Use score_threshold to filter noise
- Consider quantization for large collections"""
        },
        {
            "role": "user",
            "content": f"""Design a Qdrant schema for: {use_case}

Embedding model: {embedding_model}
Required features: {', '.join(features_list)}

Please provide:
1. Collection configuration (vectors, indexes)
2. Payload schema with field types
3. Index recommendations
4. Sample upsert code
5. Sample search queries
6. Performance optimization tips
7. RAG integration example if applicable"""
        }
    ]


@mcp.prompt()
async def implement_semantic_search(
    domain: str,
    requirements: List[str] = []
) -> List[Dict[str, str]]:
    """
    Generate prompt to implement semantic search.

    Args:
        domain: Application domain
        requirements: Specific requirements
    """
    return [
        {
            "role": "system",
            "content": """You are a semantic search implementation expert.

Implementation checklist:
1. Choose embedding model (OpenAI, sentence-transformers, etc.)
2. Design collection schema
3. Implement embedding pipeline
4. Create search endpoint
5. Add filtering capabilities
6. Implement pagination
7. Add error handling
8. Optimize for production

Best practices:
- Batch embeddings for efficiency
- Cache frequently accessed results
- Use score_threshold to filter
- Monitor search latency"""
        },
        {
            "role": "user",
            "content": f"""Implement semantic search for: {domain}

Requirements: {', '.join(requirements) if requirements else 'Standard semantic search'}

Please provide:
1. Collection setup code
2. Embedding function
3. Upsert pipeline
4. Search function
5. Filter examples
6. Error handling
7. Performance tips"""
        }
    ]


# ================================
# MCP RESOURCES
# ================================

@mcp.resource(uri="guide://qdrant-development")
async def get_qdrant_guide() -> str:
    """Complete Qdrant development guide"""
    return json.dumps({
        "title": "Qdrant Vector Database Development Guide 2025",
        "version": QdrantKnowledgeBase.VERSION,
        "sections": {
            "collections": "Collection configuration and management",
            "search": "Vector search patterns and optimization",
            "filtering": "Filter conditions and indexing",
            "rag": "RAG implementation patterns",
            "hybrid": "Hybrid search with dense + sparse vectors",
            "performance": "Scaling and optimization"
        },
        "features": {
            "query_analysis": "Analyze Qdrant queries for optimization",
            "config_generation": "Generate collection configurations",
            "pattern_library": "Common Qdrant patterns collection",
            "rag_patterns": "RAG implementation examples"
        }
    }, indent=2)


# ================================
# SERVER INITIALIZATION
# ================================

if __name__ == "__main__":
    logger.info("Qdrant Vector Database MCP Server starting...")
    logger.info(f"Qdrant Version: {QdrantKnowledgeBase.VERSION}")
    logger.info("Features: Query Analysis | Config Generation | RAG Patterns | Optimization")
    logger.info("\nAvailable prompts:")
    logger.info("  - design_vector_schema: Design vector database schema")
    logger.info("  - implement_semantic_search: Implement semantic search")

    mcp.run()
