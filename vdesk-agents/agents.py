from google.adk.agents import LlmAgent
from mqtt_bridge import before_model_cb, after_agent_cb, before_tool_cb
from config import MODEL_NAME

# Agent Tools
def calculator(expression: str) -> dict:
    """
    Evaluates a basic mathematical expression.
    Args:
        expression: A string containing a mathematical expression (e.g., "256 * 2").
    Returns:
        A dictionary with the result or an error message.
    """
    try:
        if not all(c in "0123456789+-*/(). " for c in expression):
            return {"status": "error", "message": "Invalid characters in expression."}
        result = eval(expression, {"__builtins__": None}, {})
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def check_server_status() -> dict:
    """
    Checks the status of the virtual office mainframe.
    Returns:
        A dictionary with the server status details.
    """
    return {
        "status": "ONLINE",
        "cpu_load": "12%",
        "memory": "640KB/640KB FREE",
        "uptime": "128:42:15",
        "temp": "42C"
    }

# Agent Definitions
ops_agent = LlmAgent(
    name="ops_agent",
    model=MODEL_NAME,
    instruction="You are a Ops Specialist. Use 'calculator' for math and 'check_server_status' to monitor the mainframe. Keep responses short and retro.",
    tools=[calculator, check_server_status],
    before_model_callback=before_model_cb,
    after_agent_callback=after_agent_cb,
    before_tool_callback=before_tool_cb
)

dev_agent = LlmAgent(
    name="dev_agent",
    model=MODEL_NAME,
    instruction="You are a Software Developer. You write efficient assembly and C code. Keep responses short and retro.",
    before_model_callback=before_model_cb,
    after_agent_callback=after_agent_cb,
    before_tool_callback=before_tool_cb
)

mgr_agent = LlmAgent(
    name="mgr_agent",
    model=MODEL_NAME,
    instruction="You are the Office Manager. Delegate tasks to 'dev_agent' for coding and 'ops_agent' for math or server status. Keep responses short and retro.",
    sub_agents=[dev_agent, ops_agent],
    before_model_callback=before_model_cb,
    after_agent_callback=after_agent_cb,
    before_tool_callback=before_tool_cb
)
