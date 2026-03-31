export interface Agent {
	agentId: string;
	name: string;
	sprite: string;
}

export const agents: Agent[] = [
	{ "agentId" : "operation_agent", "name" : "Operation", "sprite": "/assets/characters/char_0.png" },
	{ "agentId" : "developer_agent", "name" : "Developer", "sprite": "/assets/characters/char_3.png" },
	{ "agentId" : "research_agent", "name" : "Research", "sprite": "/assets/characters/char_2.png" },
	{ "agentId" : "manager_agent", "name" : "Manager", "sprite": "/assets/characters/char_0.png" }
];

export const MQTT_BROKER_URL = import.meta.env.PUBLIC_MQTT_BROKER_URL || "wss://broker.emqx.io:8084/mqtt";