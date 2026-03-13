export interface Agent {
	agentId: string;
	name: string;
	initialEmoji: string;
}

export const agents: Agent[] = [
	{ "agentId" : "dev_agent", "name" : "Developer", "initialEmoji": "👨‍💻" },
	{ "agentId" : "ops_agent", "name" : "Operations", "initialEmoji": "👨‍💻" },
	{ "agentId" : "mgr_agent", "name" : "Manager", "initialEmoji": "👨‍💻" }
];

export const MQTT_BROKER_URL = "wss://broker.emqx.io:8084/mqtt";