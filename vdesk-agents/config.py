import os

MODEL_NAME = "gemini-2.5-pro"
MQTT_BROKER = os.environ.get("MQTT_BROKER", "broker.emqx.io")
MQTT_PORT = int(os.environ.get("MQTT_PORT", 1883))
MQTT_TOPIC_PREFIX = "voffice/agents"
APP_NAME = "vdesk-agents"
DEFAULT_USER_ID = "user-1"
DEFAULT_SESSION_ID = "session-1"
