# vdesk-web: The Virtual Agent Office

`vdesk-web` is the visual frontend for the **vdesk** project, a 16-bit retro office simulator that visualizes AI agents in real-time.

## 🚀 Overview

Built with **Astro 5** and styled with **NES.css**, this application provides a top-down view of a virtual office. It features a tiled map system and autonomous agents that react to **MQTT** events from the Python backend.

### Key Features

- **Tiled Map System**: Renders a complex office layout (floors, walls, furniture) from a JSON configuration.
- **Sprite-Based Agents**: Agents use animated sprite sheets with directions (front, back, side) and mirror support.
- **Autonomous Behavior**: Agents walk to their assigned desks when active and wander the office floor when idle.
- **Real-time Sync**: Uses `MQTT.js` to subscribe to agent states (thinking, acting, idling) and display status bubbles.
- **Retro Aesthetic**: 16-bit pixel art style with the "Press Start 2P" font and NES-style UI components.

## 🛠️ Tech Stack

- **Framework**: [Astro 5](https://astro.build/)
- **Styling**: [NES.css](https://nostalgic-css.github.io/NES.css/)
- **Typography**: Press Start 2P via `@fontsource/press-start-2p`
- **Communication**: [MQTT.js](https://github.com/mqttjs/MQTT.js)
- **Assets**: Custom tiled map and character sprite sheets.

## 🏁 Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (v18+)
- [npm](https://www.npmjs.com/)

### Installation

1. Install dependencies:
    ```bash
    npm install
    ```

2. Start the development server:
    ```bash
    npm run dev
    ```

The office will be available at `http://localhost:4321`.

## 📂 Project Structure

- `src/components/Map.astro`: Renders the office environment using tiled assets and `public/assets/default-layout-1.json`.
- `src/components/Officer.astro`: The agent controller. Handles sprite animations, MQTT logic, and pathfinding (walking).
- `src/config/agents.ts`: Configuration for agent IDs, display names, and sprites.
- `sync-agents.cjs`: A utility script to synchronize agent metadata from the `vdesk-agents` Python backend.
- `public/assets/`: Contains all pixel art assets (characters, furniture, floors, walls).

## ⚙️ Configuration & Sync

### Synchronizing Agents
To keep the frontend in sync with new agents defined in the Python backend, run:
```bash
node sync-agents.cjs
```

### Manual Configuration
You can manually edit `src/config/agents.ts` to change sprites or the MQTT broker:

```typescript
export const agents: Agent[] = [
	{ "agentId" : "ops_agent", "name" : "Operations", "sprite": "/assets/characters/char_1.png" },
	// ...
];

export const MQTT_BROKER_URL = "wss://broker.emqx.io:8084/mqtt";
```

## 🔌 MQTT Integration

The UI listens for events on: `voffice/agents/{agent_id}/events`

**Expected Payload:**
```json
{
  "agent_id": "dev_agent",
  "status": "thinking",
  "message": "Optimizing assembly code...",
  "timestamp": 1741512345
}
```

---
Part of the [vdesk](../README.md) project.
