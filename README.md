# vdesk: Virtual Agent Office

`vdesk` is an experimental project that visualizes AI agents in a virtual, retro-styled office environment. It bridges the gap between agentic logic and visual UI by using real-time synchronization via MQTT.

![screenshot](/screenshots/screenshot_01.png)

## 🚀 Overview

The project simulates an office floor where AI agents perform tasks, "think" about solutions, and collaborate. As the agents run in the Python backend, their internal states (thinking, acting, idling) are published to an MQTT broker and visualized in a 16-bit web interface.

## 🏗️ Architecture

- **Backend ([vdesk-agents](./vdesk-agents/))**: A Python-based agent runner powered by the [Google Agent Developer Kit (ADK)](https://github.com/google/agent-developer-kit).
- **Frontend ([vdesk-web](./vdesk-web/))**: A modern web interface built with **Astro 5** and styled with **NES.css** for a nostalgic 16-bit look.
- **Communication**: Real-time event synchronization using **MQTT** via the public broker `broker.emqx.io`.

## 🤖 Meet the Staff

The office currently features three specialized agents:

1.  **Manager (`mgr_agent`)**: The orchestrator. Capable of delegating complex tasks to specialized agents.
2.  **Dev (`dev_agent`)**: A software engineer specializing in low-level code (C and Assembly).
3.  **Ops (`ops_agent`)**: A systems specialist equipped with calculation and server monitoring tools.

## 🏁 Getting Started

### 1. Run the Agents

Requires Python 3.13+ and a Google GenAI API Key.

```bash
cd vdesk-agents
uv sync 
# Create a .env file with GOOGLE_API_KEY=your_key
# Run demo agent OR you might change to chatloop
python main.py
```

### 2. Start the Web Interface

Requires Node.js 18+.

```bash
cd vdesk-web
npm install
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

## 🗺️ Roadmap

- [ ] **Persistent Memory**: Implement long-term storage for agent interactions using ADK session services.
- [ ] **Interactive Furniture**: Add functional office objects (Coffee Machine, Server Racks) that agents can interact with.
- [ ] **Enhanced Security**: Move away from public brokers to a secured, private MQTT instance.
- [ ] **Agent Customization**: Allow users to define new agents and their desk locations via a config file.

## 💡 Inspiration

This project was inspired by the excellent [pixel-agents](https://github.com/pablodelucca/pixel-agents) project.

## 📄 License

This project is licensed under the [MIT License](./LICENSE).
