#!/usr/bin/env python3
"""
Neo4j Graph Database MCP Server
===============================

Advanced MCP server for Neo4j graph database development, featuring:
- Cypher query analysis and optimization
- Graph data modeling patterns
- Query generation and refactoring
- Index strategy recommendations
- Path traversal patterns
- APOC procedures guidance

Based on: Neo4j Cypher Manual, APOC documentation, Graph Data Modeling guidelines
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
    name="Neo4j Graph Database Server",
    instructions="""Advanced MCP server for Neo4j graph database development.

This server provides Neo4j development expertise:
- Cypher query analysis and optimization
- Graph data modeling patterns
- Query generation for common patterns
- Index and constraint recommendations
- Path traversal and pattern matching
- APOC procedures guidance

Use these tools to build efficient graph database applications.""",
    version="3.0.0"
)

# ================================
# NEO4J PATTERNS & KNOWLEDGE BASE
# ================================

class CypherCategory(Enum):
    """Cypher pattern categories"""
    MATCH = "match"
    CREATE = "create"
    MERGE = "merge"
    DELETE = "delete"
    SET = "set"
    PATH = "path"
    AGGREGATION = "aggregation"
    INDEX = "index"
    CONSTRAINT = "constraint"
    APOC = "apoc"

class QueryComplexity(Enum):
    """Query complexity levels"""
    SIMPLE = "simple"
    MODERATE = "moderate"
    COMPLEX = "complex"
    ADVANCED = "advanced"

@dataclass
class CypherAnalysisResult:
    """Result of Cypher query analysis"""
    query: str
    score: int
    category_scores: Dict[str, int]
    patterns_found: List[str]
    anti_patterns: List[str]
    suggestions: List[str]
    optimized_query: Optional[str]
    index_recommendations: List[str]

class Neo4jKnowledgeBase:
    """Neo4j knowledge base with Cypher patterns"""

    VERSION = "5.x"
    APOC_VERSION = "5.x"

    # Core Cypher Patterns
    MATCH_PATTERNS = {
        "basic_match": {
            "description": "Basic node pattern matching",
            "syntax": "MATCH (n:Label) RETURN n",
            "example": '''// Find all Person nodes
MATCH (p:Person)
RETURN p.name, p.age
ORDER BY p.name''',
            "best_practice": "Always use labels in MATCH to leverage indexes"
        },
        "relationship_match": {
            "description": "Match nodes connected by relationships",
            "syntax": "MATCH (a)-[r:REL_TYPE]->(b) RETURN a, r, b",
            "example": '''// Find friends of a person
MATCH (p:Person {name: 'Alice'})-[:FRIENDS_WITH]->(friend:Person)
RETURN friend.name AS friendName''',
            "best_practice": "Specify relationship direction when known for better performance"
        },
        "optional_match": {
            "description": "Match pattern that may or may not exist",
            "syntax": "OPTIONAL MATCH (a)-[r]->(b)",
            "example": '''// Find person with optional address
MATCH (p:Person {name: 'Alice'})
OPTIONAL MATCH (p)-[:LIVES_AT]->(a:Address)
RETURN p.name, a.city''',
            "best_practice": "Use OPTIONAL MATCH instead of multiple queries for optional data"
        },
        "variable_length_path": {
            "description": "Match paths of variable length",
            "syntax": "MATCH path = (a)-[*1..5]->(b)",
            "example": '''// Find connection paths up to 5 hops
MATCH path = (start:Person {name: 'Alice'})-[:KNOWS*1..5]->(end:Person {name: 'Bob'})
RETURN path, length(path) AS hops
ORDER BY hops
LIMIT 1''',
            "best_practice": "Always specify upper bound for variable length to prevent runaway queries"
        },
        "shortest_path": {
            "description": "Find shortest path between nodes",
            "syntax": "shortestPath((a)-[*]->(b))",
            "example": '''// Find shortest connection path
MATCH (start:Person {name: 'Alice'}), (end:Person {name: 'Bob'})
MATCH path = shortestPath((start)-[:KNOWS*]-(end))
RETURN path, length(path) AS distance''',
            "best_practice": "Use shortestPath for single path, allShortestPaths for all equal-length paths"
        }
    }

    CREATE_PATTERNS = {
        "create_node": {
            "description": "Create a new node",
            "syntax": "CREATE (n:Label {props})",
            "example": '''// Create a new person
CREATE (p:Person {
    name: 'John Doe',
    email: 'john@example.com',
    createdAt: datetime()
})
RETURN p''',
            "best_practice": "Use MERGE for idempotent operations"
        },
        "create_relationship": {
            "description": "Create relationship between nodes",
            "syntax": "CREATE (a)-[r:REL_TYPE {props}]->(b)",
            "example": '''// Create friendship relationship
MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'})
CREATE (a)-[r:FRIENDS_WITH {since: date('2024-01-01')}]->(b)
RETURN r''',
            "best_practice": "Check for existing relationship before creating to avoid duplicates"
        },
        "create_with_return": {
            "description": "Create and return created elements",
            "syntax": "CREATE ... RETURN ...",
            "example": '''// Create multiple nodes and relationships
CREATE (company:Company {name: 'Acme Inc'})
CREATE (employee:Person {name: 'Jane'})
CREATE (employee)-[:WORKS_FOR {since: date()}]->(company)
RETURN company, employee''',
            "best_practice": "Return created nodes for confirmation and further processing"
        }
    }

    MERGE_PATTERNS = {
        "merge_node": {
            "description": "Create node if not exists, match if exists",
            "syntax": "MERGE (n:Label {key: value})",
            "example": '''// Upsert a person by email
MERGE (p:Person {email: 'john@example.com'})
ON CREATE SET p.name = 'John Doe', p.createdAt = datetime()
ON MATCH SET p.lastSeen = datetime()
RETURN p''',
            "best_practice": "Use unique properties in MERGE pattern to prevent duplicates"
        },
        "merge_relationship": {
            "description": "Create relationship if not exists",
            "syntax": "MERGE (a)-[r:REL_TYPE]->(b)",
            "example": '''// Ensure friendship exists
MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'})
MERGE (a)-[r:FRIENDS_WITH]->(b)
ON CREATE SET r.since = date()
RETURN r''',
            "best_practice": "Always MATCH the nodes first, then MERGE the relationship"
        }
    }

    AGGREGATION_PATTERNS = {
        "count": {
            "description": "Count matching patterns",
            "syntax": "RETURN count(n)",
            "example": '''// Count friends per person
MATCH (p:Person)-[:FRIENDS_WITH]->(friend)
RETURN p.name, count(friend) AS friendCount
ORDER BY friendCount DESC'''
        },
        "collect": {
            "description": "Collect values into a list",
            "syntax": "RETURN collect(n.prop)",
            "example": '''// Collect all friend names
MATCH (p:Person {name: 'Alice'})-[:FRIENDS_WITH]->(friend)
RETURN p.name, collect(friend.name) AS friends'''
        },
        "sum_avg": {
            "description": "Sum and average calculations",
            "syntax": "RETURN sum(n.value), avg(n.value)",
            "example": '''// Calculate order statistics
MATCH (c:Customer)-[:PLACED]->(o:Order)
RETURN c.name,
       count(o) AS orderCount,
       sum(o.total) AS totalSpent,
       avg(o.total) AS avgOrderValue'''
        },
        "reduce": {
            "description": "Reduce list to single value",
            "syntax": "reduce(acc = init, x IN list | expression)",
            "example": '''// Calculate path weight
MATCH path = (a:City)-[:ROAD*]->(b:City)
WITH path, [r IN relationships(path) | r.distance] AS distances
RETURN reduce(total = 0, d IN distances | total + d) AS totalDistance'''
        }
    }

    PATH_PATTERNS = {
        "named_path": {
            "description": "Capture path as variable",
            "syntax": "MATCH path = (a)-[*]->(b)",
            "example": '''// Analyze path structure
MATCH path = (start:Person)-[:KNOWS*1..4]->(end:Person)
RETURN path,
       length(path) AS hops,
       nodes(path) AS people,
       relationships(path) AS connections'''
        },
        "all_shortest_paths": {
            "description": "Find all shortest paths",
            "syntax": "allShortestPaths((a)-[*]->(b))",
            "example": '''// Find all shortest connection routes
MATCH (start:Person {name: 'Alice'}), (end:Person {name: 'Charlie'})
MATCH path = allShortestPaths((start)-[:KNOWS*]-(end))
RETURN path'''
        },
        "quantified_path": {
            "description": "Quantified path patterns (Neo4j 5.x)",
            "syntax": "(a)-->+{1,3}(b)",
            "example": '''// Find paths with exactly 2-4 hops
MATCH (start:Person {name: 'Alice'})
      (()-[:KNOWS]->())+ {2,4}
      (end:Person)
RETURN end.name'''
        }
    }

    INDEX_PATTERNS = {
        "btree_index": {
            "description": "B-tree index for equality and range queries",
            "syntax": "CREATE INDEX FOR (n:Label) ON (n.property)",
            "example": '''// Create index on Person.email
CREATE INDEX person_email FOR (p:Person) ON (p.email)

// Create composite index
CREATE INDEX person_name_age FOR (p:Person) ON (p.name, p.age)''',
            "use_case": "Equality lookups and range queries"
        },
        "fulltext_index": {
            "description": "Full-text search index",
            "syntax": "CREATE FULLTEXT INDEX FOR (n:Label) ON EACH [n.prop]",
            "example": '''// Create fulltext index for search
CREATE FULLTEXT INDEX articleSearch
FOR (a:Article)
ON EACH [a.title, a.content]

// Query using fulltext
CALL db.index.fulltext.queryNodes('articleSearch', 'graph database')
YIELD node, score
RETURN node.title, score
ORDER BY score DESC''',
            "use_case": "Text search across properties"
        },
        "relationship_index": {
            "description": "Index on relationship properties",
            "syntax": "CREATE INDEX FOR ()-[r:REL_TYPE]-() ON (r.property)",
            "example": '''// Index relationship property
CREATE INDEX transaction_date FOR ()-[t:TRANSACTION]-() ON (t.date)'''
        }
    }

    CONSTRAINT_PATTERNS = {
        "unique_constraint": {
            "description": "Enforce unique property values",
            "syntax": "CREATE CONSTRAINT FOR (n:Label) REQUIRE n.prop IS UNIQUE",
            "example": '''// Ensure unique email
CREATE CONSTRAINT person_email_unique
FOR (p:Person)
REQUIRE p.email IS UNIQUE'''
        },
        "exists_constraint": {
            "description": "Enforce property existence",
            "syntax": "CREATE CONSTRAINT FOR (n:Label) REQUIRE n.prop IS NOT NULL",
            "example": '''// Require name property
CREATE CONSTRAINT person_name_exists
FOR (p:Person)
REQUIRE p.name IS NOT NULL'''
        },
        "node_key": {
            "description": "Composite unique key constraint",
            "syntax": "CREATE CONSTRAINT FOR (n:Label) REQUIRE (n.p1, n.p2) IS NODE KEY",
            "example": '''// Composite key for uniqueness
CREATE CONSTRAINT address_key
FOR (a:Address)
REQUIRE (a.street, a.city, a.country) IS NODE KEY'''
        }
    }

    APOC_PATTERNS = {
        "batch_operations": {
            "description": "Process large datasets in batches",
            "example": '''// Batch delete old records
CALL apoc.periodic.iterate(
  "MATCH (n:TempNode) WHERE n.createdAt < datetime() - duration('P30D') RETURN n",
  "DETACH DELETE n",
  {batchSize: 1000, parallel: false}
)'''
        },
        "data_import": {
            "description": "Import data from various sources",
            "example": '''// Import from JSON
CALL apoc.load.json('https://api.example.com/users')
YIELD value
CREATE (u:User {
  id: value.id,
  name: value.name,
  email: value.email
})'''
        },
        "graph_algorithms": {
            "description": "Graph algorithms via APOC",
            "example": '''// PageRank algorithm
CALL apoc.algo.pageRank(['Person'], ['KNOWS'], {iterations: 20})
YIELD node, score
RETURN node.name, score
ORDER BY score DESC
LIMIT 10'''
        },
        "path_expansion": {
            "description": "Advanced path finding",
            "example": '''// Expand paths with filters
MATCH (start:Person {name: 'Alice'})
CALL apoc.path.expandConfig(start, {
  relationshipFilter: "KNOWS>",
  minLevel: 1,
  maxLevel: 3,
  uniqueness: "NODE_GLOBAL"
})
YIELD path
RETURN path'''
        }
    }

    # Anti-patterns to avoid
    ANTI_PATTERNS = {
        "unbounded_variable_length": {
            "pattern": "(a)-[*]->(b)",
            "problem": "Can cause runaway queries and memory issues",
            "solution": "Always specify upper bound: (a)-[*1..5]->(b)"
        },
        "cartesian_product": {
            "pattern": "MATCH (a), (b) ...",
            "problem": "Creates cross product of all nodes",
            "solution": "Connect patterns or use WHERE clause to filter"
        },
        "no_index_usage": {
            "pattern": "MATCH (n) WHERE n.prop = 'value'",
            "problem": "Full scan if no label specified",
            "solution": "Always use labels: MATCH (n:Label) WHERE n.prop = 'value'"
        },
        "property_access_in_relationship": {
            "pattern": "MATCH (a)-[r]->(b) WHERE r.prop = 'value'",
            "problem": "Relationship properties not indexed by default",
            "solution": "Create relationship property index or filter early"
        }
    }


class CypherAnalyzer:
    """Cypher query analyzer"""

    def __init__(self):
        self.knowledge_base = Neo4jKnowledgeBase()

    async def analyze_cypher(self, query: str) -> CypherAnalysisResult:
        """Analyze Cypher query for patterns and optimization opportunities"""

        score = 50
        category_scores = {}
        patterns_found = []
        anti_patterns = []
        suggestions = []
        optimized_query = None
        index_recommendations = []

        # Analyze query structure
        structure_score = await self._analyze_structure(query)
        category_scores["structure"] = structure_score
        score += (structure_score - 50) * 0.2

        # Analyze index usage
        index_score = await self._analyze_index_usage(query)
        category_scores["index_usage"] = index_score
        score += (index_score - 50) * 0.25

        # Analyze pattern matching
        pattern_score = await self._analyze_patterns(query)
        category_scores["pattern_matching"] = pattern_score
        score += (pattern_score - 50) * 0.2

        # Analyze path traversal
        path_score = await self._analyze_paths(query)
        category_scores["path_traversal"] = path_score
        score += (path_score - 50) * 0.15

        # Analyze parameterization
        param_score = await self._analyze_parameterization(query)
        category_scores["parameterization"] = param_score
        score += (param_score - 50) * 0.1

        # Check for anti-patterns
        anti_patterns = await self._check_anti_patterns(query)
        score -= len(anti_patterns) * 5

        # Generate suggestions
        suggestions = await self._generate_suggestions(category_scores, query)

        # Generate index recommendations
        index_recommendations = await self._generate_index_recommendations(query)

        # Generate optimized query if needed
        if score < 80:
            optimized_query = await self._optimize_query(query)

        final_score = max(0, min(100, int(score)))

        return CypherAnalysisResult(
            query=query,
            score=final_score,
            category_scores=category_scores,
            patterns_found=patterns_found,
            anti_patterns=anti_patterns,
            suggestions=suggestions,
            optimized_query=optimized_query,
            index_recommendations=index_recommendations
        )

    async def _analyze_structure(self, query: str) -> int:
        """Analyze query structure"""
        score = 50
        query_upper = query.upper()

        # Check for proper MATCH usage
        if 'MATCH' in query_upper:
            score += 10

        # Check for RETURN clause
        if 'RETURN' in query_upper:
            score += 10

        # Check for WHERE filtering
        if 'WHERE' in query_upper:
            score += 5

        # Check for ORDER BY (could indicate good data management)
        if 'ORDER BY' in query_upper:
            score += 5

        # Check for LIMIT (good practice for large results)
        if 'LIMIT' in query_upper:
            score += 10

        return min(100, max(0, score))

    async def _analyze_index_usage(self, query: str) -> int:
        """Analyze index usage potential"""
        score = 50

        # Check for labels in MATCH (enables index usage)
        if re.search(r'MATCH\s*\([^)]*:[A-Z][a-zA-Z]*', query):
            score += 20

        # Check for property lookup with label
        if re.search(r'\([a-z]+:[A-Z][a-zA-Z]*\s*\{[^}]+\}\)', query):
            score += 15

        # Check for parameterized property values
        if re.search(r'\{[^}]*\$[a-zA-Z]+[^}]*\}', query):
            score += 10

        return min(100, max(0, score))

    async def _analyze_patterns(self, query: str) -> int:
        """Analyze pattern matching quality"""
        score = 50

        # Check for relationship direction
        if '->' in query or '<-' in query:
            score += 15

        # Check for relationship type specification
        if re.search(r'\[:[A-Z_]+\]', query):
            score += 15

        # Check for property patterns
        if re.search(r'\{[^}]+\}', query):
            score += 10

        return min(100, max(0, score))

    async def _analyze_paths(self, query: str) -> int:
        """Analyze path traversal patterns"""
        score = 50

        # Check for bounded variable length
        if re.search(r'\[\*\d+\.\.\d+\]', query):
            score += 20
        elif re.search(r'\[\*\]', query):
            score -= 20  # Unbounded is bad

        # Check for path functions
        if any(func in query for func in ['shortestPath', 'allShortestPaths', 'length(', 'nodes(', 'relationships(']):
            score += 15

        return min(100, max(0, score))

    async def _analyze_parameterization(self, query: str) -> int:
        """Analyze query parameterization"""
        score = 50

        # Check for parameters
        param_count = len(re.findall(r'\$[a-zA-Z_][a-zA-Z0-9_]*', query))
        if param_count > 0:
            score += min(30, param_count * 10)

        # Penalize hardcoded values that should be parameters
        hardcoded = len(re.findall(r"'[^']+'" , query))
        if hardcoded > 2:
            score -= (hardcoded - 2) * 5

        return min(100, max(0, score))

    async def _check_anti_patterns(self, query: str) -> List[str]:
        """Check for anti-patterns"""
        anti_patterns = []

        # Check for unbounded variable length
        if re.search(r'\[\*\](?!\d)', query):
            anti_patterns.append("Unbounded variable length path - specify upper bound")

        # Check for potential cartesian product
        if re.search(r'MATCH\s*\([^)]+\)\s*,\s*\([^)]+\)(?!.*WHERE)', query, re.IGNORECASE):
            anti_patterns.append("Potential cartesian product - connect patterns or add WHERE")

        # Check for missing labels
        if re.search(r'MATCH\s*\([a-z]+\)(?!\s*:)', query):
            anti_patterns.append("MATCH without label - will cause full scan")

        return anti_patterns

    async def _generate_suggestions(self, scores: Dict[str, int], query: str) -> List[str]:
        """Generate optimization suggestions"""
        suggestions = []

        if scores.get("index_usage", 50) < 70:
            suggestions.append("Add labels to MATCH patterns to enable index usage")

        if scores.get("parameterization", 50) < 70:
            suggestions.append("Use parameters ($param) instead of hardcoded values for query caching")

        if scores.get("path_traversal", 50) < 60:
            suggestions.append("Specify upper bound for variable length paths")

        if 'LIMIT' not in query.upper():
            suggestions.append("Consider adding LIMIT for large result sets")

        if 'EXPLAIN' not in query.upper() and 'PROFILE' not in query.upper():
            suggestions.append("Use EXPLAIN or PROFILE to analyze query plan")

        return suggestions

    async def _generate_index_recommendations(self, query: str) -> List[str]:
        """Generate index recommendations"""
        recommendations = []

        # Find labels with property lookups
        matches = re.findall(r'\((\w+):(\w+)\s*\{(\w+):', query)
        for var, label, prop in matches:
            recommendations.append(f"CREATE INDEX FOR (n:{label}) ON (n.{prop})")

        # Find WHERE property conditions
        where_matches = re.findall(r'WHERE\s+\w+\.(\w+)\s*=', query, re.IGNORECASE)
        for prop in where_matches:
            # Try to find the label for this property
            recommendations.append(f"Consider index on property: {prop}")

        return list(set(recommendations))

    async def _optimize_query(self, query: str) -> str:
        """Generate optimized version of query"""
        optimized = query

        # Add LIMIT if missing
        if 'LIMIT' not in query.upper() and 'RETURN' in query.upper():
            optimized = re.sub(r'(RETURN\s+.+)$', r'\1\nLIMIT 100', optimized, flags=re.MULTILINE)

        # Fix unbounded paths
        optimized = re.sub(r'\[\*\](?!\d)', '[*1..10]', optimized)

        return optimized


class CypherGenerator:
    """Cypher query generator"""

    def __init__(self):
        self.knowledge_base = Neo4jKnowledgeBase()

    async def generate_query(
        self,
        operation: str,
        labels: List[str],
        properties: Optional[Dict[str, Any]] = None,
        relationships: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """Generate Cypher query for operation"""

        if properties is None:
            properties = {}
        if relationships is None:
            relationships = []

        generators = {
            "find": self._generate_find,
            "create": self._generate_create,
            "update": self._generate_update,
            "delete": self._generate_delete,
            "merge": self._generate_merge,
            "path": self._generate_path,
        }

        if operation not in generators:
            return {"error": f"Unknown operation: {operation}"}

        return await generators[operation](labels, properties, relationships)

    async def _generate_find(
        self,
        labels: List[str],
        properties: Dict[str, Any],
        relationships: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Generate MATCH query"""
        label = labels[0] if labels else "Node"
        var = label[0].lower()

        # Build property conditions
        conditions = []
        params = {}
        for key, value in properties.items():
            param_name = f"{var}_{key}"
            conditions.append(f"{var}.{key} = ${param_name}")
            params[param_name] = value

        where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""

        query = f"""MATCH ({var}:{label})
{where_clause}
RETURN {var}
ORDER BY {var}.id
LIMIT $limit"""

        params["limit"] = 100

        return {
            "query": query.strip(),
            "parameters": params,
            "operation": "find",
            "description": f"Find {label} nodes matching criteria"
        }

    async def _generate_create(
        self,
        labels: List[str],
        properties: Dict[str, Any],
        relationships: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Generate CREATE query"""
        label = labels[0] if labels else "Node"
        var = label[0].lower()

        # Build property string
        prop_assignments = ", ".join([f"{key}: ${key}" for key in properties.keys()])
        props_str = f"{{{prop_assignments}}}" if properties else ""

        query = f"""CREATE ({var}:{label} {props_str})
RETURN {var}"""

        return {
            "query": query.strip(),
            "parameters": properties,
            "operation": "create",
            "description": f"Create new {label} node"
        }

    async def _generate_update(
        self,
        labels: List[str],
        properties: Dict[str, Any],
        relationships: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Generate SET query for updates"""
        label = labels[0] if labels else "Node"
        var = label[0].lower()

        # Separate lookup and update properties
        lookup_prop = list(properties.keys())[0] if properties else "id"
        update_props = {k: v for k, v in list(properties.items())[1:]}

        set_clause = ", ".join([f"{var}.{key} = ${key}" for key in update_props.keys()])

        query = f"""MATCH ({var}:{label} {{{lookup_prop}: ${lookup_prop}}})
SET {set_clause}, {var}.updatedAt = datetime()
RETURN {var}"""

        return {
            "query": query.strip(),
            "parameters": properties,
            "operation": "update",
            "description": f"Update {label} node properties"
        }

    async def _generate_delete(
        self,
        labels: List[str],
        properties: Dict[str, Any],
        relationships: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Generate DELETE query"""
        label = labels[0] if labels else "Node"
        var = label[0].lower()

        lookup_prop = list(properties.keys())[0] if properties else "id"

        query = f"""MATCH ({var}:{label} {{{lookup_prop}: ${lookup_prop}}})
DETACH DELETE {var}
RETURN count(*) AS deletedCount"""

        return {
            "query": query.strip(),
            "parameters": {lookup_prop: properties.get(lookup_prop)},
            "operation": "delete",
            "description": f"Delete {label} node and its relationships"
        }

    async def _generate_merge(
        self,
        labels: List[str],
        properties: Dict[str, Any],
        relationships: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Generate MERGE query"""
        label = labels[0] if labels else "Node"
        var = label[0].lower()

        # First property is the merge key
        merge_key = list(properties.keys())[0] if properties else "id"
        other_props = {k: v for k, v in list(properties.items())[1:]}

        on_create_set = ", ".join([f"{var}.{key} = ${key}" for key in other_props.keys()])
        on_create_set = f", {on_create_set}" if on_create_set else ""

        query = f"""MERGE ({var}:{label} {{{merge_key}: ${merge_key}}})
ON CREATE SET {var}.createdAt = datetime(){on_create_set}
ON MATCH SET {var}.lastSeen = datetime()
RETURN {var}"""

        return {
            "query": query.strip(),
            "parameters": properties,
            "operation": "merge",
            "description": f"Merge (upsert) {label} node"
        }

    async def _generate_path(
        self,
        labels: List[str],
        properties: Dict[str, Any],
        relationships: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Generate path query"""
        if len(labels) < 2:
            labels = labels + ["Node"] * (2 - len(labels))

        start_label = labels[0]
        end_label = labels[1]
        rel_type = relationships[0].get("type", "CONNECTED_TO") if relationships else "CONNECTED_TO"
        max_depth = properties.get("max_depth", 5)

        query = f"""MATCH (start:{start_label} {{$startKey: $startValue}})
MATCH (end:{end_label} {{$endKey: $endValue}})
MATCH path = shortestPath((start)-[:{rel_type}*1..{max_depth}]-(end))
RETURN path, length(path) AS distance"""

        return {
            "query": query.strip(),
            "parameters": {
                "startKey": "id",
                "startValue": None,
                "endKey": "id",
                "endValue": None
            },
            "operation": "path",
            "description": f"Find shortest path between {start_label} and {end_label}"
        }


# ================================
# MCP TOOLS
# ================================

@mcp.tool(tags=["analysis", "cypher", "scoring"])
async def analyze_cypher_query(query: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Analyzes Cypher query for patterns and optimization opportunities.

    Args:
        query: Cypher query to analyze

    Returns:
        Complete analysis with score and recommendations
    """
    try:
        analyzer = CypherAnalyzer()
        analysis = await analyzer.analyze_cypher(query)

        logger.info(f"Analyzed Cypher query - score: {analysis.score}")

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
            "optimized_query": analysis.optimized_query,
            "index_recommendations": analysis.index_recommendations
        }

    except Exception as e:
        logger.error(f"Error analyzing Cypher query: {str(e)}")
        raise


@mcp.tool(tags=["generation", "cypher", "query"])
async def generate_cypher_query(
    operation: str,
    labels: List[str],
    properties: Optional[Dict[str, Any]] = None,
    relationships: Optional[List[Dict[str, Any]]] = None,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Generates Cypher query for specified operation.

    Args:
        operation: Operation type (find, create, update, delete, merge, path)
        labels: Node labels involved
        properties: Properties for the operation
        relationships: Relationships involved

    Returns:
        Generated Cypher query with parameters
    """
    try:
        generator = CypherGenerator()
        result = await generator.generate_query(operation, labels, properties, relationships)

        logger.info(f"Generated Cypher query for operation: {operation}")

        return result

    except Exception as e:
        logger.error(f"Error generating Cypher query: {str(e)}")
        raise


@mcp.tool(tags=["optimization", "cypher", "performance"])
async def optimize_cypher(query: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Optimizes Cypher query for better performance.

    Args:
        query: Cypher query to optimize

    Returns:
        Optimized query with explanations
    """
    try:
        analyzer = CypherAnalyzer()
        analysis = await analyzer.analyze_cypher(query)

        optimizations = []
        optimized = query

        # Fix unbounded variable length paths
        if re.search(r'\[\*\](?!\d)', optimized):
            optimized = re.sub(r'\[\*\](?!\d)', '[*1..10]', optimized)
            optimizations.append("Added upper bound to variable length path")

        # Add LIMIT if missing
        if 'LIMIT' not in query.upper() and 'RETURN' in query.upper():
            optimized = re.sub(r'(RETURN\s+.+)$', r'\1\nLIMIT 100', optimized, flags=re.MULTILINE)
            optimizations.append("Added LIMIT clause to prevent large result sets")

        # Suggest PROFILE
        if 'PROFILE' not in query.upper():
            optimizations.append("Tip: Prefix query with PROFILE to see execution plan")

        return {
            "original_query": query,
            "optimized_query": optimized,
            "optimizations_applied": optimizations,
            "original_score": analysis.score,
            "index_recommendations": analysis.index_recommendations,
            "additional_suggestions": analysis.suggestions
        }

    except Exception as e:
        logger.error(f"Error optimizing Cypher query: {str(e)}")
        raise


@mcp.tool(tags=["patterns", "reference", "cypher"])
async def get_cypher_patterns(category: str = "all", ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Returns Cypher patterns by category.

    Args:
        category: Pattern category (match, create, merge, delete, path, aggregation, index, constraint, apoc, all)

    Returns:
        Cypher patterns with examples
    """
    try:
        kb = Neo4jKnowledgeBase()

        categories = {
            "match": kb.MATCH_PATTERNS,
            "create": kb.CREATE_PATTERNS,
            "merge": kb.MERGE_PATTERNS,
            "aggregation": kb.AGGREGATION_PATTERNS,
            "path": kb.PATH_PATTERNS,
            "index": kb.INDEX_PATTERNS,
            "constraint": kb.CONSTRAINT_PATTERNS,
            "apoc": kb.APOC_PATTERNS,
            "anti_patterns": kb.ANTI_PATTERNS,
        }

        if category == "all":
            return {
                "neo4j_version": kb.VERSION,
                "apoc_version": kb.APOC_VERSION,
                "categories": categories,
                "quick_reference": {
                    "match": "MATCH (n:Label) WHERE ... RETURN ...",
                    "create": "CREATE (n:Label {props}) RETURN n",
                    "merge": "MERGE (n:Label {key}) ON CREATE SET ... ON MATCH SET ...",
                    "delete": "MATCH (n) DETACH DELETE n",
                    "path": "MATCH path = shortestPath((a)-[*]-(b)) RETURN path"
                }
            }

        if category not in categories:
            return {"error": f"Category '{category}' not found. Available: {list(categories.keys())}"}

        return {
            "category": category,
            "patterns": categories[category]
        }

    except Exception as e:
        logger.error(f"Error getting Cypher patterns: {str(e)}")
        raise


@mcp.tool(tags=["generation", "model", "graph"])
async def generate_graph_model(
    domain: str,
    entities: Optional[List[str]] = None,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Generates graph data model for a domain.

    Args:
        domain: Business domain (e.g., "social_network", "e_commerce", "knowledge_graph")
        entities: Main entities to model

    Returns:
        Complete graph model with nodes, relationships, and constraints
    """
    try:
        templates = {
            "social_network": {
                "nodes": [
                    {"label": "User", "properties": ["id", "name", "email", "createdAt"]},
                    {"label": "Post", "properties": ["id", "content", "createdAt"]},
                    {"label": "Comment", "properties": ["id", "content", "createdAt"]},
                    {"label": "Tag", "properties": ["name"]}
                ],
                "relationships": [
                    {"type": "FOLLOWS", "from": "User", "to": "User", "properties": ["since"]},
                    {"type": "POSTED", "from": "User", "to": "Post", "properties": ["at"]},
                    {"type": "COMMENTED", "from": "User", "to": "Post", "properties": ["at"]},
                    {"type": "TAGGED", "from": "Post", "to": "Tag", "properties": []},
                    {"type": "LIKES", "from": "User", "to": "Post", "properties": ["at"]}
                ],
                "constraints": [
                    "CREATE CONSTRAINT user_email_unique FOR (u:User) REQUIRE u.email IS UNIQUE",
                    "CREATE CONSTRAINT tag_name_unique FOR (t:Tag) REQUIRE t.name IS UNIQUE"
                ],
                "indexes": [
                    "CREATE INDEX user_name FOR (u:User) ON (u.name)",
                    "CREATE INDEX post_created FOR (p:Post) ON (p.createdAt)"
                ]
            },
            "e_commerce": {
                "nodes": [
                    {"label": "Customer", "properties": ["id", "name", "email"]},
                    {"label": "Product", "properties": ["id", "name", "price", "stock"]},
                    {"label": "Order", "properties": ["id", "total", "status", "createdAt"]},
                    {"label": "Category", "properties": ["id", "name"]}
                ],
                "relationships": [
                    {"type": "PLACED", "from": "Customer", "to": "Order", "properties": ["at"]},
                    {"type": "CONTAINS", "from": "Order", "to": "Product", "properties": ["quantity", "price"]},
                    {"type": "BELONGS_TO", "from": "Product", "to": "Category", "properties": []},
                    {"type": "REVIEWED", "from": "Customer", "to": "Product", "properties": ["rating", "comment"]},
                    {"type": "VIEWED", "from": "Customer", "to": "Product", "properties": ["at"]}
                ],
                "constraints": [
                    "CREATE CONSTRAINT customer_email FOR (c:Customer) REQUIRE c.email IS UNIQUE",
                    "CREATE CONSTRAINT product_id FOR (p:Product) REQUIRE p.id IS UNIQUE"
                ],
                "indexes": [
                    "CREATE INDEX product_name FOR (p:Product) ON (p.name)",
                    "CREATE INDEX order_status FOR (o:Order) ON (o.status)"
                ]
            },
            "knowledge_graph": {
                "nodes": [
                    {"label": "Entity", "properties": ["id", "name", "type", "description"]},
                    {"label": "Concept", "properties": ["id", "name", "definition"]},
                    {"label": "Source", "properties": ["id", "url", "title", "publishedAt"]}
                ],
                "relationships": [
                    {"type": "RELATED_TO", "from": "Entity", "to": "Entity", "properties": ["weight", "type"]},
                    {"type": "IS_A", "from": "Entity", "to": "Concept", "properties": []},
                    {"type": "PART_OF", "from": "Entity", "to": "Entity", "properties": []},
                    {"type": "MENTIONED_IN", "from": "Entity", "to": "Source", "properties": ["context"]},
                    {"type": "SUBCONCEPT_OF", "from": "Concept", "to": "Concept", "properties": []}
                ],
                "constraints": [
                    "CREATE CONSTRAINT entity_id FOR (e:Entity) REQUIRE e.id IS UNIQUE",
                    "CREATE CONSTRAINT concept_name FOR (c:Concept) REQUIRE c.name IS UNIQUE"
                ],
                "indexes": [
                    "CREATE FULLTEXT INDEX entity_search FOR (e:Entity) ON EACH [e.name, e.description]",
                    "CREATE INDEX entity_type FOR (e:Entity) ON (e.type)"
                ]
            }
        }

        if domain.lower() in templates:
            model = templates[domain.lower()]
        else:
            # Generate generic model from entities
            if entities is None:
                entities = ["Entity"]

            model = {
                "nodes": [
                    {"label": entity, "properties": ["id", "name", "createdAt", "updatedAt"]}
                    for entity in entities
                ],
                "relationships": [],
                "constraints": [
                    f"CREATE CONSTRAINT {entity.lower()}_id FOR (n:{entity}) REQUIRE n.id IS UNIQUE"
                    for entity in entities
                ],
                "indexes": [
                    f"CREATE INDEX {entity.lower()}_name FOR (n:{entity}) ON (n.name)"
                    for entity in entities
                ]
            }

        return {
            "domain": domain,
            "model": model,
            "sample_queries": {
                "find_all": f"MATCH (n:{model['nodes'][0]['label']}) RETURN n LIMIT 100",
                "find_by_id": f"MATCH (n:{model['nodes'][0]['label']} {{id: $id}}) RETURN n",
                "find_related": f"MATCH (n:{model['nodes'][0]['label']} {{id: $id}})-[r]->(m) RETURN n, r, m"
            }
        }

    except Exception as e:
        logger.error(f"Error generating graph model: {str(e)}")
        raise


@mcp.tool(tags=["prompt", "analysis", "neo4j"])
async def analyze_neo4j_prompt(prompt: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Analyzes a prompt for Neo4j/Cypher development.

    Args:
        prompt: User prompt to analyze

    Returns:
        Analysis with suggestions and improvements
    """
    try:
        score = 50
        suggestions = []
        missing = []

        # Check for operation type
        if any(op in prompt.lower() for op in ["find", "search", "get", "match", "query"]):
            score += 10
        elif any(op in prompt.lower() for op in ["create", "add", "insert"]):
            score += 10
        elif any(op in prompt.lower() for op in ["update", "modify", "change"]):
            score += 10
        elif any(op in prompt.lower() for op in ["delete", "remove"]):
            score += 10
        else:
            missing.append("Specify the operation (find, create, update, delete)")

        # Check for labels/entities
        if any(word in prompt.lower() for word in ["node", "label", "entity", "user", "product", "person"]):
            score += 10
        else:
            missing.append("Specify node labels or entity types")

        # Check for properties
        if any(word in prompt.lower() for word in ["property", "field", "attribute", "name", "id", "email"]):
            score += 10
        else:
            suggestions.append("Consider specifying properties to filter or return")

        # Check for relationships
        if any(word in prompt.lower() for word in ["relationship", "connected", "related", "link", "path"]):
            score += 10
        else:
            suggestions.append("Specify relationships if traversing the graph")

        # Check for performance considerations
        if any(word in prompt.lower() for word in ["index", "optimize", "performance", "limit"]):
            score += 10
        else:
            suggestions.append("Consider performance requirements (indexes, limits)")

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

Please include:
- Cypher query with proper MATCH pattern
- Use labels for index usage
- Include WHERE clause for filtering
- Add LIMIT for result set control
- Consider index recommendations"""
        }

    except Exception as e:
        logger.error(f"Error analyzing Neo4j prompt: {str(e)}")
        raise


# ================================
# MCP PROMPTS
# ================================

@mcp.prompt()
async def design_graph_model(
    domain: str,
    entities: List[str] = [],
    relationships: List[str] = []
) -> List[Dict[str, str]]:
    """
    Generate prompt to design a graph data model.

    Args:
        domain: Business domain description
        entities: Main entities in the domain
        relationships: Key relationships between entities
    """
    return [
        {
            "role": "system",
            "content": """You are a Neo4j graph database modeling expert.

Key principles for graph modeling:
1. **Nodes represent entities**: Things with identity
2. **Relationships connect nodes**: Verbs between nouns
3. **Properties describe**: Attributes on nodes and relationships
4. **Labels categorize**: Enable indexing and queries

Best practices:
- Use nouns for labels (Person, Product, Order)
- Use verbs for relationships (KNOWS, PURCHASED, CONTAINS)
- Keep relationships directional when semantically meaningful
- Index frequently queried properties
- Use constraints for data integrity
- Prefer relationships over join tables"""
        },
        {
            "role": "user",
            "content": f"""Design a graph data model for: {domain}

Entities: {', '.join(entities) if entities else 'Determine from domain'}
Relationships: {', '.join(relationships) if relationships else 'Determine from entities'}

Please provide:
1. Node definitions with labels and properties
2. Relationship definitions with types and properties
3. Unique constraints for data integrity
4. Indexes for common queries
5. Sample CRUD queries
6. Sample analytical queries
7. Visual diagram description"""
        }
    ]


@mcp.prompt()
async def optimize_cypher_query(
    query: str,
    context: str = ""
) -> List[Dict[str, str]]:
    """
    Generate prompt to optimize a Cypher query.

    Args:
        query: Cypher query to optimize
        context: Additional context about data size, patterns, etc.
    """
    return [
        {
            "role": "system",
            "content": """You are a Neo4j Cypher optimization expert.

Optimization strategies:
1. **Index usage**: Ensure MATCH patterns use indexed properties
2. **Label specificity**: Always use labels in MATCH
3. **Path bounds**: Limit variable length paths
4. **Early filtering**: Use WHERE early in query
5. **Result limiting**: Use LIMIT for large results
6. **Query planning**: Use PROFILE to analyze

Common performance issues:
- Cartesian products from unconnected patterns
- Unbounded variable length paths
- Missing indexes on frequently queried properties
- Full label scans without property filters"""
        },
        {
            "role": "user",
            "content": f"""Optimize this Cypher query:

```cypher
{query}
```

{f"Context: {context}" if context else ""}

Please provide:
1. Analysis of current query issues
2. Optimized version of the query
3. Explanation of changes
4. Required indexes
5. Alternative approaches if applicable
6. PROFILE/EXPLAIN interpretation guidance"""
        }
    ]


# ================================
# MCP RESOURCES
# ================================

@mcp.resource(uri="guide://neo4j-development")
async def get_neo4j_guide() -> str:
    """Complete Neo4j development guide"""
    return json.dumps({
        "title": "Neo4j Graph Database Development Guide 2025",
        "versions": {
            "neo4j": "5.x",
            "apoc": "5.x",
            "gds": "2.x"
        },
        "sections": {
            "data_modeling": "Graph data modeling principles and patterns",
            "cypher_basics": "Core Cypher query language",
            "cypher_advanced": "Advanced patterns and optimizations",
            "indexing": "Index strategies for performance",
            "apoc": "APOC procedures and functions",
            "gds": "Graph Data Science algorithms"
        },
        "features": {
            "query_analysis": "Analyze Cypher queries for optimization",
            "query_generation": "Generate Cypher for common operations",
            "model_design": "Design graph data models",
            "pattern_library": "Common Cypher patterns collection"
        }
    }, indent=2)


# ================================
# SERVER INITIALIZATION
# ================================

if __name__ == "__main__":
    logger.info("Neo4j Graph Database MCP Server starting...")
    logger.info(f"Neo4j Version: {Neo4jKnowledgeBase.VERSION}")
    logger.info("Features: Query Analysis | Query Generation | Model Design | Optimization")
    logger.info("\nAvailable prompts:")
    logger.info("  - design_graph_model: Design graph data model")
    logger.info("  - optimize_cypher_query: Optimize Cypher query")

    mcp.run()
