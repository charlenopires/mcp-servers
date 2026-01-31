#!/usr/bin/env python3
"""
Tests for Erlang OTP Server - MCP server for Erlang/OTP patterns.

Tests cover GenServer, Supervisor, fault tolerance patterns, and code analysis.
"""

import pytest
from unittest.mock import AsyncMock

try:
    from servers.erlang_server import (
        analyze_erlang_code,
        generate_otp_project,
        generate_genserver,
        get_otp_patterns,
        ErlangKnowledgeBase
    )
    ERLANG_SERVER_AVAILABLE = True
except ImportError as e:
    print(f"Erlang Server not available: {e}")
    ERLANG_SERVER_AVAILABLE = False


class TestErlangKnowledgeBase:
    """Tests for Erlang knowledge base"""

    @pytest.mark.skipif(not ERLANG_SERVER_AVAILABLE, reason="Erlang Server not available")
    def test_genserver_patterns_exist(self):
        """Test that GenServer patterns are defined"""
        kb = ErlangKnowledgeBase()
        assert hasattr(kb, 'GENSERVER_PATTERNS')
        assert "basic" in kb.GENSERVER_PATTERNS
        assert "with_state" in kb.GENSERVER_PATTERNS

    @pytest.mark.skipif(not ERLANG_SERVER_AVAILABLE, reason="Erlang Server not available")
    def test_supervisor_patterns_exist(self):
        """Test that Supervisor patterns are defined"""
        kb = ErlangKnowledgeBase()
        assert hasattr(kb, 'SUPERVISOR_PATTERNS')
        assert "one_for_one" in kb.SUPERVISOR_PATTERNS

    @pytest.mark.skipif(not ERLANG_SERVER_AVAILABLE, reason="Erlang Server not available")
    def test_fault_tolerance_patterns_exist(self):
        """Test that fault tolerance patterns are defined"""
        kb = ErlangKnowledgeBase()
        assert hasattr(kb, 'FAULT_TOLERANCE_PATTERNS')


class TestErlangAnalysisFunctions:
    """Tests for Erlang Server analysis functions"""

    @pytest.mark.skipif(not ERLANG_SERVER_AVAILABLE, reason="Erlang Server not available")
    @pytest.mark.asyncio
    async def test_analyze_erlang_code_basic(self):
        """Test basic Erlang code analysis"""
        erlang_code = """
        -module(my_server).
        -behaviour(gen_server).
        -export([start_link/0, init/1, handle_call/3, handle_cast/2]).

        start_link() ->
            gen_server:start_link({local, ?MODULE}, ?MODULE, [], []).

        init([]) ->
            {ok, #{}}.

        handle_call(_Request, _From, State) ->
            {reply, ok, State}.

        handle_cast(_Msg, State) ->
            {noreply, State}.
        """

        result = await analyze_erlang_code(erlang_code)

        assert isinstance(result, dict)
        assert "score" in result
        assert 0 <= result["score"] <= 100
        assert "suggestions" in result

    @pytest.mark.skipif(not ERLANG_SERVER_AVAILABLE, reason="Erlang Server not available")
    @pytest.mark.asyncio
    async def test_analyze_erlang_code_with_supervisor(self):
        """Test Erlang code analysis with supervisor"""
        erlang_code = """
        -module(my_sup).
        -behaviour(supervisor).
        -export([start_link/0, init/1]).

        start_link() ->
            supervisor:start_link({local, ?MODULE}, ?MODULE, []).

        init([]) ->
            SupFlags = #{strategy => one_for_one},
            ChildSpecs = [
                #{id => worker, start => {worker, start_link, []}}
            ],
            {ok, {SupFlags, ChildSpecs}}.
        """

        result = await analyze_erlang_code(erlang_code)
        assert result["score"] >= 50

    @pytest.mark.skipif(not ERLANG_SERVER_AVAILABLE, reason="Erlang Server not available")
    @pytest.mark.asyncio
    async def test_generate_otp_project(self):
        """Test OTP project generation"""
        result = await generate_otp_project(
            name="TestApp",
            type="application"
        )

        assert isinstance(result, dict)
        assert "project_name" in result
        assert "files" in result

    @pytest.mark.skipif(not ERLANG_SERVER_AVAILABLE, reason="Erlang Server not available")
    @pytest.mark.asyncio
    async def test_generate_genserver(self):
        """Test GenServer module generation"""
        result = await generate_genserver(name="MyWorker")

        assert isinstance(result, dict)
        assert "module" in result
        assert "code" in result
        assert "-behaviour(gen_server)" in result["code"]

    @pytest.mark.skipif(not ERLANG_SERVER_AVAILABLE, reason="Erlang Server not available")
    @pytest.mark.asyncio
    async def test_get_otp_patterns_all(self):
        """Test getting all OTP patterns"""
        result = await get_otp_patterns()

        assert isinstance(result, dict)
        assert "categories" in result
        assert "genserver" in result["categories"]
        assert "supervisor" in result["categories"]

    @pytest.mark.skipif(not ERLANG_SERVER_AVAILABLE, reason="Erlang Server not available")
    @pytest.mark.asyncio
    async def test_get_otp_patterns_by_category(self):
        """Test getting patterns by category"""
        result = await get_otp_patterns(category="genserver")

        assert isinstance(result, dict)
        assert "category" in result
        assert "patterns" in result


@pytest.fixture
def mock_context():
    """Fixture for mocking Context"""
    context = AsyncMock()
    context.info = AsyncMock()
    context.warning = AsyncMock()
    context.error = AsyncMock()
    return context


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
