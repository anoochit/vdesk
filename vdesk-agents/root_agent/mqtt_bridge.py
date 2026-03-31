import json
import time
from typing import Optional
from google.genai import types
import paho.mqtt.client as mqtt
from google.adk.tools.base_tool import BaseTool
from google.adk.models import LlmRequest, LlmResponse
from google.adk.tools.tool_context import ToolContext
from config import MQTT_PORT, MQTT_BROKER, MQTT_TOPIC_PREFIX
from google.adk.agents.callback_context import CallbackContext

class OfficeMqttBridge:
    def __init__(self):
        self.client = mqtt.Client(client_id="vdesk_agents")
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
        print(f"[MQTT] Publishing to {topic}: {status} - {message[:30]}")
        self.client.publish(topic, json.dumps(payload))

bridge = OfficeMqttBridge()

def before_model_cb(
    callback_context: CallbackContext,
    llm_request: LlmRequest
) -> Optional[LlmResponse]:
    agent_id = callback_context.agent_name.lower().replace(" ", "_")
    bridge.publish_event(agent_id, "thinking", "thinking...")
    return None

def after_agent_cb(
    callback_context: CallbackContext
) -> Optional[types.Content]:
    agent_id = callback_context.agent_name.lower().replace(" ", "_")
    bridge.publish_event(agent_id, "idle", "complete!")
    return None

def before_tool_cb(
    tool: BaseTool,
    args: dict,
    tool_context: ToolContext
) -> Optional[dict]:
    agent_id = tool_context.agent_name.lower().replace(" ", "_")
    bridge.publish_event(agent_id, "acting", f" {tool.name.replace('_', ' ')}")
    return None