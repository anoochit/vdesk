import json
import time
import asyncio
import paho.mqtt.client as mqtt
from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmResponse, LlmRequest
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext
from google.genai import types
from typing import Optional

# MQTT Configuration
MQTT_BROKER = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_TOPIC_PREFIX = "voffice/agents"

class OfficeMqttBridge:
    def __init__(self):
        self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
        self.client.connect(MQTT_BROKER, MQTT_PORT, 60)
        self.client.loop_start()

    def publish_event(self, agent_id, status, message):
        payload = {
            "agent_id": agent_id,
            "status": status,
            "message": message,
            "timestamp": time.time()
        }
        topic = f"{MQTT_TOPIC_PREFIX}/{agent_id}/events"
        print(f"[MQTT] Publishing to {topic}: {status} - {message[:30]}...")
        self.client.publish(topic, json.dumps(payload))

bridge = OfficeMqttBridge()

# Correct signature (CallbackContext, LlmRequest) -> Optional[LlmResponse]
def before_model_cb(
    callback_context: CallbackContext,
    llm_request: LlmRequest
) -> Optional[LlmResponse]:
    agent_id = callback_context.agent_name.lower().replace(" ", "_")
    bridge.publish_event(agent_id, "thinking", "Wait... I'm thinking...")
    return None  # Allow the model call to proceed

# Correct signature (CallbackContext) -> Optional[types.Content]
def after_agent_cb(
    callback_context: CallbackContext
) -> Optional[types.Content]:
    agent_id = callback_context.agent_name.lower().replace(" ", "_")
    bridge.publish_event(agent_id, "idle", "Agent turn complete.")
    return None  # Return None to keep original response unchanged

# Correct signature (tool, args, tool_context) -> Optional[dict]
def before_tool_cb(
    tool: BaseTool,
    args: dict,
    tool_context: ToolContext
) -> Optional[dict]:
    agent_id = tool_context.agent_name.lower().replace(" ", "_")
    bridge.publish_event(agent_id, "acting", f"Executing tool: {tool.name}")
    return None  # Allow the tool call to proceed

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
# 1. Ops Agent (Service Status & Calculator)
ops_agent = LlmAgent(
    name="ops_agent",
    model="gemini-2.5-flash",
    instruction="You are a 16-bit Ops Specialist. Use 'calculator' for math and 'check_server_status' to monitor the mainframe. Keep responses short and retro.",
    tools=[calculator, check_server_status],
    before_model_callback=before_model_cb,
    after_agent_callback=after_agent_cb,
    before_tool_callback=before_tool_cb
)

# 2. Dev Agent (Coding)
dev_agent = LlmAgent(
    name="dev_agent",
    model="gemini-2.5-flash",
    instruction="You are a 16-bit Software Developer. You write efficient assembly and C code. Keep responses short and retro.",
    before_model_callback=before_model_cb,
    after_agent_callback=after_agent_cb,
    before_tool_callback=before_tool_cb
)

# 3. Manager Agent (Orchestrator)
mgr_agent = LlmAgent(
    name="mgr_agent",
    model="gemini-2.5-flash",
    instruction="You are the 16-bit Office Manager. Delegate tasks to 'dev_agent' for coding and 'ops_agent' for math or server status. Keep responses short and retro.",
    sub_agents=[dev_agent, ops_agent],
    before_model_callback=before_model_cb,
    after_agent_callback=after_agent_cb,
    before_tool_callback=before_tool_cb
)

async def run_demo_task(query):
    session_service = InMemorySessionService()
    # We use mgr_agent as the main entry point
    runner = Runner(
        agent=mgr_agent,
        app_name="RetroOffice",
        session_service=session_service,
    )

    # Create session explicitly before running
    await session_service.create_session(
        app_name="RetroOffice",
        user_id="user_1",
        session_id="session_1"
    )

    print(f"\n--- Running Task: {query} ---")
    async for event in runner.run_async(
        user_id="user_1",
        session_id="session_1",
        new_message=types.Content(role="user", parts=[types.Part(text=query)])
    ):
        if event.is_final_response():
            print(f"Final Response: {event.content.parts[0].text}")

if __name__ == "__main__":
    queries = [
        "What is 1024 / 4?",
        "Check the mainframe status.",
        "Write a simple C function to add two numbers.",
        "Manager, please ask Ops to check the server and then ask Dev to write a script for it."
    ]

    for q in queries:
        asyncio.run(run_demo_task(q))
        time.sleep(2)
