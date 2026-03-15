export interface Agent {
	agentId: string;
	name: string;
	sprite: string;
}

export const agents: Agent[] = [
	{ "agentId" : "ops_agent", "name" : "Operations", "sprite": "/assets/characters/char_1.png" },
	{ "agentId" : "dev_agent", "name" : "Developer", "sprite": "/assets/characters/char_0.png" },
	{ "agentId" : "mgr_agent", "name" : "Manager", "sprite": "/assets/characters/char_2.png" }
];

export const MQTT_BROKER_URL = "wss://broker.emqx.io:8084/mqtt";