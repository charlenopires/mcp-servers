#!/usr/bin/env python3
"""
Erlang OTP MCP Server
=====================

Advanced MCP server for Erlang/OTP development, featuring:
- OTP behavior patterns (GenServer, Supervisor, gen_statem)
- Fault tolerance and "Let it crash" philosophy
- Supervision tree design patterns
- Hot code upgrade patterns
- Distributed Erlang patterns
- ETS and DETS patterns

Based on: Erlang/OTP documentation, OTP Design Principles
"""

import asyncio
import json
import re
import logging
from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from enum import Enum
from fastmcp import FastMCP, Context
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP(
    name="Erlang OTP Server",
    instructions="""Advanced MCP server for Erlang/OTP development.

This server provides Erlang development expertise:
- OTP behavior patterns (GenServer, Supervisor, gen_statem)
- Fault tolerance and supervision tree design
- Process communication patterns
- Distributed Erlang patterns
- Hot code upgrade support
- ETS/DETS storage patterns

Use these tools to build fault-tolerant, concurrent Erlang applications.""",
    version="3.0.0"
)

# ================================
# ERLANG OTP KNOWLEDGE BASE
# ================================

class OTPBehavior(Enum):
    """OTP behavior types"""
    GEN_SERVER = "gen_server"
    GEN_STATEM = "gen_statem"
    SUPERVISOR = "supervisor"
    GEN_EVENT = "gen_event"
    APPLICATION = "application"

class SupervisorStrategy(Enum):
    """Supervisor restart strategies"""
    ONE_FOR_ONE = "one_for_one"
    ONE_FOR_ALL = "one_for_all"
    REST_FOR_ONE = "rest_for_one"
    SIMPLE_ONE_FOR_ONE = "simple_one_for_one"

@dataclass
class ErlangAnalysisResult:
    """Result of Erlang code analysis"""
    code: str
    score: int
    category_scores: Dict[str, int]
    patterns_found: List[str]
    anti_patterns: List[str]
    suggestions: List[str]
    otp_compliance: Dict[str, bool]

class ErlangKnowledgeBase:
    """Erlang/OTP knowledge base"""

    VERSION = "27.0"
    OTP_VERSION = "27"

    # GenServer Patterns
    GENSERVER_PATTERNS = {
        "init": {
            "description": "Initialize GenServer state",
            "signature": "init(Args) -> {ok, State} | {stop, Reason}",
            "example": '''init(Args) ->
    %% Initialize state
    InitialState = #{
        counter => 0,
        data => Args
    },
    {ok, InitialState}.''',
            "best_practice": "Keep init/1 fast, defer heavy initialization to handle_continue"
        },
        "handle_call": {
            "description": "Handle synchronous calls",
            "signature": "handle_call(Request, From, State) -> {reply, Reply, NewState}",
            "example": '''handle_call({get, Key}, _From, State) ->
    Value = maps:get(Key, State, undefined),
    {reply, {ok, Value}, State};

handle_call({put, Key, Value}, _From, State) ->
    NewState = maps:put(Key, Value, State),
    {reply, ok, NewState};

handle_call(_Request, _From, State) ->
    {reply, {error, unknown_request}, State}.''',
            "best_practice": "Use pattern matching for different request types"
        },
        "handle_cast": {
            "description": "Handle asynchronous casts",
            "signature": "handle_cast(Request, State) -> {noreply, NewState}",
            "example": '''handle_cast({increment, Amount}, #{counter := Counter} = State) ->
    NewState = State#{counter := Counter + Amount},
    {noreply, NewState};

handle_cast(reset, State) ->
    {noreply, State#{counter := 0}};

handle_cast(_Request, State) ->
    {noreply, State}.''',
            "best_practice": "Use cast for fire-and-forget operations"
        },
        "handle_info": {
            "description": "Handle other messages",
            "signature": "handle_info(Info, State) -> {noreply, NewState}",
            "example": '''handle_info(timeout, State) ->
    %% Handle timeout
    perform_periodic_task(),
    {noreply, State, 5000};  %% Set next timeout

handle_info({'DOWN', Ref, process, Pid, Reason}, State) ->
    %% Handle monitored process down
    NewState = handle_process_down(Pid, Reason, State),
    {noreply, NewState};

handle_info(_Info, State) ->
    {noreply, State}.''',
            "best_practice": "Handle monitor/link messages here"
        },
        "terminate": {
            "description": "Cleanup when stopping",
            "signature": "terminate(Reason, State) -> ok",
            "example": '''terminate(_Reason, #{connection := Conn}) ->
    %% Cleanup resources
    close_connection(Conn),
    ok;
terminate(_Reason, _State) ->
    ok.''',
            "best_practice": "Release resources, but don't rely on terminate always being called"
        },
        "code_change": {
            "description": "Hot code upgrade support",
            "signature": "code_change(OldVsn, State, Extra) -> {ok, NewState}",
            "example": '''code_change(_OldVsn, State, _Extra) ->
    %% Migrate state to new format if needed
    NewState = migrate_state(State),
    {ok, NewState}.''',
            "best_practice": "Plan for state migration during upgrades"
        }
    }

    # Supervisor Patterns
    SUPERVISOR_PATTERNS = {
        "one_for_one": {
            "description": "Only restart the failed child",
            "strategy": "one_for_one",
            "example": '''init([]) ->
    SupFlags = #{
        strategy => one_for_one,
        intensity => 5,      %% Max 5 restarts
        period => 60         %% in 60 seconds
    },
    ChildSpecs = [
        #{
            id => worker1,
            start => {worker1, start_link, []},
            restart => permanent,
            shutdown => 5000,
            type => worker,
            modules => [worker1]
        },
        #{
            id => worker2,
            start => {worker2, start_link, []},
            restart => permanent,
            shutdown => 5000,
            type => worker,
            modules => [worker2]
        }
    ],
    {ok, {SupFlags, ChildSpecs}}.''',
            "use_case": "Independent workers where failure of one doesn't affect others"
        },
        "one_for_all": {
            "description": "Restart all children if one fails",
            "strategy": "one_for_all",
            "example": '''init([]) ->
    SupFlags = #{
        strategy => one_for_all,
        intensity => 3,
        period => 60
    },
    ChildSpecs = [
        child_spec(connection_manager),
        child_spec(session_handler),
        child_spec(message_router)
    ],
    {ok, {SupFlags, ChildSpecs}}.''',
            "use_case": "Tightly coupled children that depend on each other"
        },
        "rest_for_one": {
            "description": "Restart failed child and all children started after it",
            "strategy": "rest_for_one",
            "example": '''init([]) ->
    SupFlags = #{
        strategy => rest_for_one,
        intensity => 3,
        period => 60
    },
    %% Order matters: later children depend on earlier ones
    ChildSpecs = [
        child_spec(database_pool),     %% Started first
        child_spec(cache_server),      %% Depends on database
        child_spec(api_handler)        %% Depends on both
    ],
    {ok, {SupFlags, ChildSpecs}}.''',
            "use_case": "Sequential dependencies where later children depend on earlier ones"
        },
        "simple_one_for_one": {
            "description": "Template for dynamically started children",
            "strategy": "simple_one_for_one",
            "example": '''init([]) ->
    SupFlags = #{
        strategy => simple_one_for_one,
        intensity => 10,
        period => 60
    },
    ChildSpecs = [
        #{
            id => session,
            start => {session_worker, start_link, []},
            restart => temporary,
            shutdown => 5000,
            type => worker,
            modules => [session_worker]
        }
    ],
    {ok, {SupFlags, ChildSpecs}}.

%% Start child dynamically
start_session(SessionId) ->
    supervisor:start_child(?MODULE, [SessionId]).''',
            "use_case": "Pool of identical workers started dynamically"
        }
    }

    # Fault Tolerance Patterns
    FAULT_TOLERANCE_PATTERNS = {
        "let_it_crash": {
            "description": "Allow processes to crash and be restarted by supervisor",
            "principle": "Don't program defensively - let the supervisor handle recovery",
            "example": '''%% DON'T do this (defensive programming):
handle_call({divide, A, B}, _From, State) ->
    try
        Result = A / B,
        {reply, {ok, Result}, State}
    catch
        error:badarith ->
            {reply, {error, division_by_zero}, State}
    end.

%% DO this (let it crash):
handle_call({divide, A, B}, _From, State) ->
    Result = A / B,  %% Crashes on division by zero
    {reply, {ok, Result}, State}.

%% The supervisor will restart the worker'''
        },
        "error_kernel": {
            "description": "Separate error-prone code from critical state",
            "example": '''%% Critical state manager (rarely crashes)
-module(state_manager).
handle_call({process, Data}, _From, State) ->
    %% Spawn worker to do risky processing
    Worker = spawn_link(fun() -> process_data(Data) end),
    {reply, {processing, Worker}, State}.

%% The state_manager survives even if processing crashes'''
        },
        "supervision_tree": {
            "description": "Hierarchical supervision for complex systems",
            "example": '''%%       application_sup
%%       /      |      \\
%%   db_sup  cache_sup  api_sup
%%     |        |         |
%%  workers  workers   workers

%% Each supervisor handles failures in its subtree'''
        }
    }

    # Process Patterns
    PROCESS_PATTERNS = {
        "spawn_link": {
            "description": "Spawn linked process (crash together)",
            "example": '''start_worker() ->
    spawn_link(fun() -> worker_loop() end).

%% If worker crashes, caller also terminates'''
        },
        "spawn_monitor": {
            "description": "Spawn with monitor (get notified on crash)",
            "example": '''{Pid, Ref} = spawn_monitor(fun() -> risky_operation() end),
receive
    {'DOWN', Ref, process, Pid, Reason} ->
        handle_worker_died(Reason)
after 5000 ->
    timeout
end.'''
        },
        "message_passing": {
            "description": "Asynchronous message passing between processes",
            "example": '''%% Sender
Pid ! {self(), request, Data},
receive
    {Pid, response, Result} -> Result
after 5000 ->
    {error, timeout}
end.

%% Receiver
receive
    {From, request, Data} ->
        Result = process(Data),
        From ! {self(), response, Result}
end.'''
        },
        "selective_receive": {
            "description": "Pattern matching in receive",
            "example": '''receive
    {priority, Msg} ->
        handle_priority(Msg);
    {normal, Msg} ->
        handle_normal(Msg);
    stop ->
        ok
after 10000 ->
    handle_timeout()
end.'''
        }
    }

    # ETS Patterns
    ETS_PATTERNS = {
        "public_table": {
            "description": "ETS table accessible by all processes",
            "example": '''init(_) ->
    Table = ets:new(my_cache, [
        named_table,
        public,
        {read_concurrency, true}
    ]),
    {ok, #{table => Table}}.

%% Access from any process
lookup(Key) ->
    case ets:lookup(my_cache, Key) of
        [{Key, Value}] -> {ok, Value};
        [] -> not_found
    end.'''
        },
        "protected_table": {
            "description": "ETS table owned by single process",
            "example": '''init(_) ->
    Table = ets:new(my_state, [
        set,
        protected,      %% Only owner can write
        {keypos, 1}
    ]),
    {ok, #{table => Table}}.'''
        }
    }


class ErlangAnalyzer:
    """Erlang code analyzer"""

    def __init__(self):
        self.knowledge_base = ErlangKnowledgeBase()

    async def analyze_erlang(self, code: str) -> ErlangAnalysisResult:
        """Analyze Erlang code for OTP compliance and patterns"""

        score = 50
        category_scores = {}
        patterns_found = []
        anti_patterns = []
        suggestions = []
        otp_compliance = {}

        # Analyze OTP behavior usage
        otp_score = await self._analyze_otp_behaviors(code)
        category_scores["otp_behaviors"] = otp_score
        score += (otp_score - 50) * 0.25

        # Analyze supervision patterns
        sup_score = await self._analyze_supervision(code)
        category_scores["supervision"] = sup_score
        score += (sup_score - 50) * 0.2

        # Analyze error handling
        error_score = await self._analyze_error_handling(code)
        category_scores["error_handling"] = error_score
        score += (error_score - 50) * 0.2

        # Analyze process patterns
        process_score = await self._analyze_processes(code)
        category_scores["processes"] = process_score
        score += (process_score - 50) * 0.15

        # Analyze documentation
        doc_score = await self._analyze_documentation(code)
        category_scores["documentation"] = doc_score
        score += (doc_score - 50) * 0.1

        # Analyze naming conventions
        naming_score = await self._analyze_naming(code)
        category_scores["naming"] = naming_score
        score += (naming_score - 50) * 0.1

        # Generate suggestions
        suggestions = await self._generate_suggestions(category_scores, code)

        # Check OTP compliance
        otp_compliance = await self._check_otp_compliance(code)

        final_score = max(0, min(100, int(score)))

        return ErlangAnalysisResult(
            code=code,
            score=final_score,
            category_scores=category_scores,
            patterns_found=patterns_found,
            anti_patterns=anti_patterns,
            suggestions=suggestions,
            otp_compliance=otp_compliance
        )

    async def _analyze_otp_behaviors(self, code: str) -> int:
        """Analyze OTP behavior usage"""
        score = 50

        # Check for behavior declaration
        if '-behaviour(gen_server)' in code or '-behavior(gen_server)' in code:
            score += 20
        if '-behaviour(supervisor)' in code:
            score += 20

        # Check for required callbacks
        if 'init(' in code:
            score += 5
        if 'handle_call(' in code:
            score += 5
        if 'handle_cast(' in code:
            score += 5

        return min(100, max(0, score))

    async def _analyze_supervision(self, code: str) -> int:
        """Analyze supervision patterns"""
        score = 50

        # Check for supervisor patterns
        if 'supervisor:start_link' in code:
            score += 15
        if 'strategy =>' in code:
            score += 10
        if 'intensity =>' in code and 'period =>' in code:
            score += 10

        # Check for child specs
        if 'restart =>' in code and 'shutdown =>' in code:
            score += 10

        return min(100, max(0, score))

    async def _analyze_error_handling(self, code: str) -> int:
        """Analyze error handling patterns"""
        score = 50

        # "Let it crash" approach (less defensive try/catch)
        try_catch_count = code.count('try') + code.count('catch')
        if try_catch_count < 3:
            score += 15  # Good: not overly defensive

        # Check for proper error returns
        if '{error,' in code:
            score += 10
        if '{ok,' in code:
            score += 10

        return min(100, max(0, score))

    async def _analyze_processes(self, code: str) -> int:
        """Analyze process patterns"""
        score = 50

        # Check for proper process management
        if 'spawn_link' in code or 'spawn_monitor' in code:
            score += 15
        if 'monitor(' in code or 'link(' in code:
            score += 10

        # Check for message handling
        if 'receive' in code:
            score += 10
        if 'after' in code:  # Timeout handling
            score += 5

        return min(100, max(0, score))

    async def _analyze_documentation(self, code: str) -> int:
        """Analyze documentation"""
        score = 50

        # Check for module documentation
        if '%%' in code:
            score += 10
        if '@doc' in code or '-doc(' in code:
            score += 15
        if '-spec' in code:
            score += 15
        if '-type' in code:
            score += 10

        return min(100, max(0, score))

    async def _analyze_naming(self, code: str) -> int:
        """Analyze naming conventions"""
        score = 50

        # Check for snake_case functions (Erlang convention)
        if re.search(r'[a-z]+_[a-z]+\(', code):
            score += 15

        # Check for module attribute
        if '-module(' in code:
            score += 10

        # Check for exports
        if '-export(' in code:
            score += 10

        return min(100, max(0, score))

    async def _generate_suggestions(self, scores: Dict[str, int], code: str) -> List[str]:
        """Generate improvement suggestions"""
        suggestions = []

        if scores.get("otp_behaviors", 50) < 70:
            suggestions.append("Consider using OTP behaviors (gen_server, supervisor)")

        if scores.get("supervision", 50) < 70:
            suggestions.append("Add supervision tree for fault tolerance")

        if scores.get("error_handling", 50) < 60:
            suggestions.append("Follow 'let it crash' philosophy - avoid excessive try/catch")

        if scores.get("documentation", 50) < 70:
            suggestions.append("Add -spec types and @doc documentation")

        if '-export([' not in code:
            suggestions.append("Add explicit exports with -export([...])")

        return suggestions

    async def _check_otp_compliance(self, code: str) -> Dict[str, bool]:
        """Check OTP compliance"""
        return {
            "has_module": "-module(" in code,
            "has_exports": "-export(" in code,
            "has_behavior": "-behaviour(" in code or "-behavior(" in code,
            "has_specs": "-spec" in code,
            "has_init": "init(" in code,
            "has_callbacks": "handle_call(" in code or "handle_cast(" in code
        }


class ErlangGenerator:
    """Erlang code generator"""

    def __init__(self):
        self.knowledge_base = ErlangKnowledgeBase()

    async def generate_genserver(
        self,
        name: str,
        state_type: str = "map",
        callbacks: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Generate GenServer module"""

        if callbacks is None:
            callbacks = ["init", "handle_call", "handle_cast", "handle_info", "terminate"]

        module_name = name.lower().replace(" ", "_")

        code = f'''%%%-------------------------------------------------------------------
%%% @doc
%%% {name} - GenServer implementation
%%% @end
%%%-------------------------------------------------------------------
-module({module_name}).
-behaviour(gen_server).

%% API
-export([start_link/0, start_link/1]).
-export([get_state/0, stop/0]).

%% gen_server callbacks
-export([init/1, handle_call/3, handle_cast/2, handle_info/2,
         terminate/2, code_change/3]).

-define(SERVER, ?MODULE).

-record(state, {{
    data :: map(),
    started_at :: erlang:timestamp()
}}).

%%%===================================================================
%%% API
%%%===================================================================

-spec start_link() -> {{ok, pid()}} | ignore | {{error, term()}}.
start_link() ->
    start_link(#{{}}).

-spec start_link(map()) -> {{ok, pid()}} | ignore | {{error, term()}}.
start_link(Args) ->
    gen_server:start_link({{local, ?SERVER}}, ?MODULE, Args, []).

-spec get_state() -> {{ok, #state{{}}}}.
get_state() ->
    gen_server:call(?SERVER, get_state).

-spec stop() -> ok.
stop() ->
    gen_server:stop(?SERVER).

%%%===================================================================
%%% gen_server callbacks
%%%===================================================================

init(Args) ->
    State = #state{{
        data = Args,
        started_at = erlang:timestamp()
    }},
    {{ok, State}}.

handle_call(get_state, _From, State) ->
    {{reply, {{ok, State}}, State}};
handle_call(_Request, _From, State) ->
    {{reply, {{error, unknown_request}}, State}}.

handle_cast(_Msg, State) ->
    {{noreply, State}}.

handle_info(_Info, State) ->
    {{noreply, State}}.

terminate(_Reason, _State) ->
    ok.

code_change(_OldVsn, State, _Extra) ->
    {{ok, State}}.

%%%===================================================================
%%% Internal functions
%%%===================================================================
'''

        return {
            "module": module_name,
            "code": code,
            "behavior": "gen_server",
            "callbacks": callbacks,
            "usage": f'''%% Start the server
{{{module_name}:start_link()}}.

%% Call the server
{{{module_name}:get_state()}}.

%% Stop the server
{{{module_name}:stop()}}.'''
        }

    async def generate_supervisor(
        self,
        name: str,
        strategy: str = "one_for_one",
        children: Optional[List[Dict[str, str]]] = None
    ) -> Dict[str, Any]:
        """Generate Supervisor module"""

        if children is None:
            children = [{"id": "worker", "module": "worker"}]

        module_name = f"{name.lower().replace(' ', '_')}_sup"

        child_specs = "\n".join([
            f'''        #{{
            id => {child['id']},
            start => {{{child['module']}, start_link, []}},
            restart => permanent,
            shutdown => 5000,
            type => worker,
            modules => [{child['module']}]
        }}''' for child in children
        ])

        code = f'''%%%-------------------------------------------------------------------
%%% @doc
%%% {name} Supervisor
%%% @end
%%%-------------------------------------------------------------------
-module({module_name}).
-behaviour(supervisor).

%% API
-export([start_link/0]).

%% Supervisor callbacks
-export([init/1]).

-define(SERVER, ?MODULE).

%%%===================================================================
%%% API functions
%%%===================================================================

-spec start_link() -> {{ok, pid()}} | ignore | {{error, term()}}.
start_link() ->
    supervisor:start_link({{local, ?SERVER}}, ?MODULE, []).

%%%===================================================================
%%% Supervisor callbacks
%%%===================================================================

init([]) ->
    SupFlags = #{{
        strategy => {strategy},
        intensity => 5,
        period => 60
    }},
    ChildSpecs = [
{child_specs}
    ],
    {{ok, {{SupFlags, ChildSpecs}}}}.

%%%===================================================================
%%% Internal functions
%%%===================================================================
'''

        return {
            "module": module_name,
            "code": code,
            "strategy": strategy,
            "children": children,
            "usage": f'''%% Start the supervisor
{{{module_name}:start_link()}}.

%% The supervisor will automatically start its children'''
        }


# ================================
# MCP TOOLS
# ================================

@mcp.tool(tags=["analysis", "erlang", "scoring"])
async def analyze_erlang_code(code: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Analyzes Erlang code for OTP compliance and patterns.

    Args:
        code: Erlang code to analyze

    Returns:
        Complete analysis with score and recommendations
    """
    try:
        analyzer = ErlangAnalyzer()
        analysis = await analyzer.analyze_erlang(code)

        logger.info(f"Analyzed Erlang code - score: {analysis.score}")

        return {
            "score": analysis.score,
            "grade": (
                "Excellent" if analysis.score >= 90 else
                "Good" if analysis.score >= 75 else
                "Needs Improvement" if analysis.score >= 60 else
                "Poor"
            ),
            "category_scores": analysis.category_scores,
            "patterns_found": analysis.patterns_found,
            "anti_patterns": analysis.anti_patterns,
            "suggestions": analysis.suggestions,
            "otp_compliance": analysis.otp_compliance
        }

    except Exception as e:
        logger.error(f"Error analyzing Erlang code: {str(e)}")
        raise


@mcp.tool(tags=["generation", "otp", "templates"])
async def generate_otp_project(
    name: str,
    type: str = "application",
    behaviors: Optional[List[str]] = None,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Generates OTP project structure.

    Args:
        name: Project name
        type: Project type (application, library)
        behaviors: OTP behaviors to include

    Returns:
        Project structure with files
    """
    try:
        if behaviors is None:
            behaviors = ["gen_server", "supervisor"]

        generator = ErlangGenerator()
        files = {}

        app_name = name.lower().replace(" ", "_")

        # Generate app file
        files[f"src/{app_name}.app.src"] = f'''{{application, {app_name}, [
    {{description, "{name} Application"}},
    {{vsn, "0.1.0"}},
    {{registered, []}},
    {{mod, {{{app_name}_app, []}}}},
    {{applications, [kernel, stdlib]}},
    {{env, []}},
    {{modules, []}}
]}}.'''

        # Generate app module
        files[f"src/{app_name}_app.erl"] = f'''%%%-------------------------------------------------------------------
%%% @doc
%%% {name} Application
%%% @end
%%%-------------------------------------------------------------------
-module({app_name}_app).
-behaviour(application).

-export([start/2, stop/1]).

start(_StartType, _StartArgs) ->
    {app_name}_sup:start_link().

stop(_State) ->
    ok.'''

        # Generate supervisor
        sup_result = await generator.generate_supervisor(app_name)
        files[f"src/{app_name}_sup.erl"] = sup_result["code"]

        # Generate worker if gen_server requested
        if "gen_server" in behaviors:
            worker_result = await generator.generate_genserver(f"{app_name}_worker")
            files[f"src/{app_name}_worker.erl"] = worker_result["code"]

        # Generate rebar.config
        files["rebar.config"] = f'''{{erl_opts, [debug_info]}}.
{{deps, []}}.

{{shell, [
    {{apps, [{app_name}]}}
]}}.'''

        return {
            "project_name": app_name,
            "files": files,
            "structure": [
                f"src/{app_name}.app.src",
                f"src/{app_name}_app.erl",
                f"src/{app_name}_sup.erl",
                f"src/{app_name}_worker.erl" if "gen_server" in behaviors else None,
                "rebar.config"
            ],
            "commands": {
                "compile": "rebar3 compile",
                "shell": "rebar3 shell",
                "test": "rebar3 eunit"
            }
        }

    except Exception as e:
        logger.error(f"Error generating OTP project: {str(e)}")
        raise


@mcp.tool(tags=["generation", "genserver", "erlang"])
async def generate_genserver(
    name: str,
    state_type: str = "map",
    callbacks: Optional[List[str]] = None,
    ctx: Optional[Context] = None
) -> Dict[str, Any]:
    """
    Generates GenServer module boilerplate.

    Args:
        name: Module name
        state_type: State data type (map, record)
        callbacks: Callbacks to include

    Returns:
        Generated GenServer code
    """
    try:
        generator = ErlangGenerator()
        result = await generator.generate_genserver(name, state_type, callbacks)

        logger.info(f"Generated GenServer: {name}")

        return result

    except Exception as e:
        logger.error(f"Error generating GenServer: {str(e)}")
        raise


@mcp.tool(tags=["patterns", "reference", "otp"])
async def get_otp_patterns(category: str = "all", ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Returns OTP patterns by category.

    Args:
        category: Pattern category (genserver, supervisor, fault_tolerance, processes, ets, all)

    Returns:
        OTP patterns with examples
    """
    try:
        kb = ErlangKnowledgeBase()

        categories = {
            "genserver": kb.GENSERVER_PATTERNS,
            "supervisor": kb.SUPERVISOR_PATTERNS,
            "fault_tolerance": kb.FAULT_TOLERANCE_PATTERNS,
            "processes": kb.PROCESS_PATTERNS,
            "ets": kb.ETS_PATTERNS,
        }

        if category == "all":
            return {
                "otp_version": kb.OTP_VERSION,
                "erlang_version": kb.VERSION,
                "categories": categories,
                "behaviors": [b.value for b in OTPBehavior],
                "supervisor_strategies": [s.value for s in SupervisorStrategy]
            }

        if category not in categories:
            return {"error": f"Category '{category}' not found. Available: {list(categories.keys())}"}

        return {
            "category": category,
            "patterns": categories[category]
        }

    except Exception as e:
        logger.error(f"Error getting OTP patterns: {str(e)}")
        raise


@mcp.tool(tags=["prompt", "analysis", "erlang"])
async def analyze_erlang_prompt(prompt: str, ctx: Optional[Context] = None) -> Dict[str, Any]:
    """
    Analyzes a prompt for Erlang development.

    Args:
        prompt: User prompt to analyze

    Returns:
        Analysis with suggestions
    """
    try:
        score = 50
        suggestions = []
        missing = []

        # Check for OTP behavior mention
        if any(b in prompt.lower() for b in ["genserver", "gen_server", "supervisor", "gen_statem"]):
            score += 15
        else:
            suggestions.append("Consider specifying OTP behavior (gen_server, supervisor)")

        # Check for supervision strategy
        if any(s in prompt.lower() for s in ["one_for_one", "one_for_all", "supervision"]):
            score += 10

        # Check for state management
        if any(word in prompt.lower() for word in ["state", "record", "map", "ets"]):
            score += 10
        else:
            suggestions.append("Specify state management approach")

        # Check for error handling
        if any(word in prompt.lower() for word in ["error", "crash", "fault", "tolerance"]):
            score += 10

        # Check for process communication
        if any(word in prompt.lower() for word in ["message", "call", "cast", "process"]):
            score += 10

        return {
            "score": min(100, score),
            "quality": (
                "Excellent" if score >= 90 else
                "Good" if score >= 70 else
                "Needs Details" if score >= 50 else
                "Incomplete"
            ),
            "suggestions": suggestions,
            "missing_elements": missing
        }

    except Exception as e:
        logger.error(f"Error analyzing Erlang prompt: {str(e)}")
        raise


# ================================
# MCP PROMPTS
# ================================

@mcp.prompt()
async def design_otp_application(
    name: str,
    features: List[str] = []
) -> List[Dict[str, str]]:
    """Generate prompt to design OTP application."""
    return [
        {
            "role": "system",
            "content": """You are an Erlang/OTP expert.

Key OTP principles:
1. Use behaviors (gen_server, supervisor, gen_statem)
2. "Let it crash" - don't program defensively
3. Design proper supervision trees
4. Use ETS for shared state
5. Plan for hot code upgrades"""
        },
        {
            "role": "user",
            "content": f"""Design an OTP application: {name}

Features: {', '.join(features) if features else 'Standard OTP structure'}

Please provide:
1. Application structure
2. Supervision tree design
3. GenServer implementations
4. Error handling strategy
5. State management approach"""
        }
    ]


# ================================
# MCP RESOURCES
# ================================

@mcp.resource(uri="guide://erlang-otp-development")
async def get_erlang_guide() -> str:
    """Complete Erlang/OTP development guide"""
    return json.dumps({
        "title": "Erlang/OTP Development Guide 2025",
        "versions": {
            "erlang": ErlangKnowledgeBase.VERSION,
            "otp": ErlangKnowledgeBase.OTP_VERSION
        },
        "sections": {
            "behaviors": "OTP behavior patterns",
            "supervision": "Supervision tree design",
            "fault_tolerance": "Let it crash philosophy",
            "processes": "Process communication patterns",
            "ets": "ETS and DETS storage"
        }
    }, indent=2)


# ================================
# SERVER INITIALIZATION
# ================================

if __name__ == "__main__":
    logger.info("Erlang OTP MCP Server starting...")
    logger.info(f"OTP Version: {ErlangKnowledgeBase.OTP_VERSION}")
    logger.info("Features: Code Analysis | OTP Generation | Pattern Library")

    mcp.run()
