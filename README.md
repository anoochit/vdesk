# vdesk: Virtual Agent Office

`vdesk` is an experimental project that visualizes AI agents in a virtual, retro-styled office environment. It bridges the gap between agentic logic and visual UI by using real-time synchronization via MQTT.

![screenshot](/screenshots/screenshot_01.png)

## 🚀 Overview

The project simulates an office floor where AI agents perform tasks, "think" about solutions, and collaborate. As the agents run in the Python backend, their internal states (thinking, acting, idling) are published to an MQTT broker and visualized in a 16-bit web interface with a tiled map system and autonomous sprite-based agents.

### Key Features
- **Tiled Map System**: Renders a complex office layout (floors, walls, furniture) from a JSON configuration in the frontend.
- **Sprite-Based Agents**: Agents use animated sprite sheets and autonomously walk to their assigned desks when active, or wander the office floor when idle.
- **Multi-Agent Orchestration**: Demonstrates agent delegation using the ADK `sub_agents` pattern in the backend.
- **Real-time State Sync**: Uses ADK callbacks to publish agent states to MQTT, which the frontend uses to display status bubbles.
- **Tool Integration**: Agents are equipped with tools like a `calculator` and `check_server_status` monitor.

## 🏗️ Architecture

- **Backend ([vdesk-agents](./vdesk-agents/))**: A Python-based agent runner powered by the [Google Agent Developer Kit (ADK)](https://github.com/google/agent-developer-kit).
- **Frontend ([vdesk-web](./vdesk-web/))**: A modern web interface built with **Astro 5** and styled with **NES.css** for a nostalgic 16-bit look.
- **Communication**: Real-time event synchronization using **MQTT** via the public broker `broker.emqx.io`.

## 🤖 Meet the Staff

The office currently features three specialized agents:

1.  **Manager (`mgr_agent`)**: The orchestrator. Capable of delegating complex tasks to specialized agents.
2.  **Dev (`dev_agent`)**: A software engineer specializing in efficient assembly and C code.
3.  **Ops (`ops_agent`)**: A systems specialist equipped with calculation and server monitoring tools.

## 🏁 Getting Started

### 1. Run the Agents (Backend)

Requires Python 3.13+ and a Google GenAI API Key.

```bash
cd vdesk-agents
uv sync 
# Create a .env file with GOOGLE_API_KEY=your_key
# Run demo agent OR you might change to chatloop
python main.py
```

### 2. Start the Web Interface (Frontend)

Requires Node.js 18+.

```bash
cd vdesk-web
npm install
# Sync agent configuration from the Python backend
node sync-agents.cjs 
npm run dev
```

The office will be accessible at `http://localhost:4321`.

## 📡 MQTT Sync

The bridge between logic and visuals is the MQTT topic:
`voffice/agents/{agent_id}/events`

**Example Payload:**
```json
{
  "agent_id": "mgr_agent",
  "status": "thinking",
  "message": "Analyzing the request...",
  "timestamp": 1741512345.678
}
```

### Status Types

* `thinking`: The agent has sent a request to the LLM.
* `acting`: The agent is executing a tool.
* `idle`: The agent has completed its turn.

## 🗺️ Roadmap

- [ ] **Persistent Memory**: Implement long-term storage for agent interactions using ADK session services.
- [ ] **Interactive Furniture**: Add functional office objects (Coffee Machine, Server Racks) that agents can interact with.
- [ ] **Enhanced Security**: Move away from public brokers to a secured, private MQTT instance.
- [ ] **Agent Customization**: Allow users to define new agents and their desk locations via a config file.

## 💡 Inspiration

This project was inspired by the excellent [pixel-agents](https://github.com/pablodelucca/pixel-agents) project.

## 📄 License

This project is licensed under the [MIT License](./LICENSE).