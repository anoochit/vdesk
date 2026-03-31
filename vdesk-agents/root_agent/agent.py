from config import MODEL_NAME
from mcp import StdioServerParameters
from google.adk.agents import Agent, Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from root_agent.mqtt_bridge import after_agent_cb, before_tool_cb, before_model_cb
from root_agent.tools import todo, calculator, current_datetime, check_server_status

# Agent Definitions
ops_agent = Agent(
    name="operation_agent",
    model=MODEL_NAME,
    instruction="You are a Ops Specialist. Use 'calculator' for math, 'check_server_status' to monitor the mainframe.Keep responses short and retro.",
    tools=[calculator, check_server_status],
    before_model_callback=before_model_cb,
    after_agent_callback=after_agent_cb,
    before_tool_callback=before_tool_cb
)

dev_agent = Agent(
    name="developer_agent",
    model=MODEL_NAME,
    instruction="You are a Software Developer. You write efficient assembly and C, C++ code. **DONOT** run your code.Keep responses short and retro.",
    before_model_callback=before_model_cb,
    after_agent_callback=after_agent_cb,
    before_tool_callback=before_tool_cb
)

research_agent = Agent(
    name="research_agent",
    model=MODEL_NAME,
    instruction="You are a researcher. You find information on the web using `google_search` tool and summarize it.Keep responses short and retro.",
    tools=[ 
      McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="uvx",
                    args=[
                        "duckduckgo-mcp-server",
                    ]
                ),
            ),
        )
    ],
    before_model_callback=before_model_cb,
    after_agent_callback=after_agent_cb,
    before_tool_callback=before_tool_cb
)

mgr_agent = Agent(
    name="manager_agent",
    model=MODEL_NAME,
    instruction="""You are the Office Manager, a meticulous dispatcher. Your primary function is to deconstruct user requests into a checklist using the `todo` tool and then delegate each item to the appropriate specialist: 'dev_agent' for coding, and 'ops_agent' for math, server status, or time inquiries.

CRITICAL WORKFLOW:
1.  **Acknowledge and Plan:** First, analyze the user's request. If it contains multiple distinct tasks, your immediate first step is to use the `todo` tool to create a task list, and 'current_datetime' to get the current time.
2.  **Delegate Sequentially:** Address each item on your to-do list by delegating it to the correct sub-agent. Do not skip any steps.
3.  **Track Progress:** As each task is completed, update its status using the `todo` tool.
4.  **Synthesize and Respond:** Once all delegated tasks are marked as 'completed' in your list, gather the results and present the final, consolidated answer to the user.

Your primary goal is to ensure no task is ever lost. Follow this workflow rigidly.
""",
    tools=[todo, current_datetime],
    sub_agents=[dev_agent, ops_agent, research_agent],
    before_model_callback=before_model_cb,
    after_agent_callback=after_agent_cb,
    before_tool_callback=before_tool_cb
)


root_agent = mgr_agent;