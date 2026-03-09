# vdesk: Virtual Agent Office - Project Context

`vdesk` is an experimental simulation that visualizes AI agents in a virtual, retro-styled office environment. It bridges the gap between agentic logic and visual UI by using real-time synchronization via MQTT.

## Project Overview

The project consists of two primary components:
1.  **`vdesk-agents`**: A Python backend using the [Google Agent Developer Kit (ADK)](https://github.com/google/agent-developer-kit). It defines specialized agents (Manager, Dev, Ops) that perform tasks and report their internal states (thinking, acting, idling).
2.  **`vdesk-web`**: An Astro-powered frontend styled with [NES.css](https://nostalgic-css.github.io/NES.css/). It provides a 16-bit visual representation of the office floor, where agent sprites react to MQTT events.

### Architecture
- **Language**: Python 3.13+ (Backend), TypeScript/Astro (Frontend).
- **Orchestration**: Google ADK for agent logic and delegation.
- **Communication**: MQTT via `broker.emqx.io` (Public Broker).
    - **Topic**: `voffice/agents/{agent_id}/events`
- **Frontend UI**: Astro 5+, NES.css, MQTT.js.

---

## Component Details

### 1. vdesk-agents (Python Backend)
The backend defines the following agents:
- **Manager (`mgr_agent`)**: The orchestrator. Delegating tasks to Dev and Ops.
- **Dev (`dev_agent`)**: Specializes in coding (C/Assembly).
- **Ops (`ops_agent`)**: Handles calculations and server status checks.

**Key Tools:**
- `calculator`: Basic math evaluation.
- `check_server_status`: Returns mock mainframe metrics.

**Building and Running:**
- **Prerequisites**: Python 3.13, `uv` (recommended).
- **Install Dependencies**: `uv sync` or `pip install -r requirements.txt`.
- **Run Agents**: `python agent_office.py`.
- **Configuration**: Requires `GOOGLE_API_KEY` in a `.env` file.

### 2. vdesk-web (Astro Frontend)
The frontend maps `agent_id` from MQTT events to UI components.

**Building and Running:**
- **Install Dependencies**: `npm install`.
- **Start Dev Server**: `npm run dev`.
- **Build**: `npm run build`.

---

## Development Conventions

### MQTT Sync
To add a new agent, ensure consistency across both layers:
1.  **Backend**: Define the agent in `agent_office.py` with a unique name (e.g., `sales_agent`).
2.  **Frontend**: Add the agent to the `agents` array in `src/pages/index.astro` with a matching `agentId`.

### Coding Style
- **Python**: Use ADK callbacks (`before_model`, `after_agent`, `before_tool`) to trigger MQTT events.
- **Astro**: Use the `Officer.astro` component for agent visualization. It handles MQTT connections via WebSocket (`wss://broker.emqx.io:8084/mqtt`).
- **Styling**: Adhere to the NES.css retro aesthetic for all UI elements.

### Topic Pattern
`voffice/agents/{agent_id}/events`
**Payload Example:**
```json
{
  "agent_id": "mgr_agent",
  "status": "thinking",
  "message": "Wait... I'm thinking...",
  "timestamp": 1741512345.678
}
```

---

## TODO / Roadmap
- [ ] Implement persistent storage for agent memory using ADK session services.
- [ ] Add more "Office Furniture" components (e.g., Coffee Machine, Server Rack) that agents can interact with.
- [ ] Enhance MQTT security (currently using a public broker).
