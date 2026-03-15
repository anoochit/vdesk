export interface Agent {
	agentId: string;
	name: string;
	sprite: string;
}

export const agents: Agent[] = [
	{ "agentId" : "ops_agent", "name" : "Operations", "sprite": "/assets/characters/char_1.png" },
	{ "agentId" : "dev_agent", "name" : "Developer", "sprite": "/assets/characters/char_0.png" },
	{ "agentId" : "mgr_agent", "name" : "Manager", "sprite": "/assets/characters/char_2.png" },
	{ "agentId" : "qa_agent", "name" : "QA Engineer", "sprite": "/assets/characters/char_3.png" },
	{ "agentId" : "designer_agent", "name" : "Designer", "sprite": "/assets/characters/char_4.png" },
	{ "agentId" : "research_agent", "name" : "Researcher", "sprite": "/assets/characters/char_5.png" },
	{ "agentId" : "hr_agent", "name" : "HR", "sprite": "/assets/characters/char_0.png" },
	{ "agentId" : "marketing_agent", "name" : "Marketing", "sprite": "/assets/characters/char_1.png" },
	{ "agentId" : "sales_agent", "name" : "Sales", "sprite": "/assets/characters/char_2.png" },
	{ "agentId" : "support_agent", "name" : "Support", "sprite": "/assets/characters/char_3.png" },
	{ "agentId" : "finance_agent", "name" : "Finance", "sprite": "/assets/characters/char_4.png" },
	{ "agentId" : "legal_agent", "name" : "Legal", "sprite": "/assets/characters/char_5.png" },
	{ "agentId" : "it_agent", "name" : "IT Support", "sprite": "/assets/characters/char_0.png" },
	{ "agentId" : "product_agent", "name" : "Product", "sprite": "/assets/characters/char_1.png" },
	{ "agentId" : "security_agent", "name" : "Security", "sprite": "/assets/characters/char_2.png" },
	{ "agentId" : "data_agent", "name" : "Data Science", "sprite": "/assets/characters/char_3.png" },
	{ "agentId" : "content_agent", "name" : "Content", "sprite": "/assets/characters/char_4.png" }
];

export const MQTT_BROKER_URL = "wss://broker.emqx.io:8084/mqtt";