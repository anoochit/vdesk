# vdesk-web: The Virtual Agent Office

## Project Overview

`vdesk-web` is the visual frontend for the **vdesk** project. It is a 16-bit retro office simulator that visualizes autonomous AI agents in real-time. The application provides a top-down view of a virtual office, featuring a tiled map system and sprite-based agents that react to MQTT events emitted from a companion Python backend (`vdesk-agents`).

### Key Technologies & Architecture
- **Framework:** Astro 5 (Static Site Generator / UI Framework)
- **Styling:** NES.css (for the 16-bit retro aesthetic) and `@fontsource/press-start-2p` (typography)
- **Communication:** MQTT.js (subscribes to agent states via WebSockets)
- **Assets:** Custom pixel art sprites for characters, furniture, floors, and walls located in `public/assets/`.

## Directory & Key Files

- `src/pages/index.astro`: The main entry point that lays out the application, rendering the Map and initializing all Agent/Officer components at specific starting positions.
- `src/components/Map.astro`: Renders the office environment using tiled assets based on `public/assets/default-layout-1.json`.
- `src/components/Officer.astro`: The core agent controller component. It handles sprite animations, pathfinding, and the MQTT subscription logic to display real-time status bubbles (thinking, acting, idling).
- `src/config/agents.ts`: The configuration file containing the list of active agents (IDs, display names, and assigned sprites) and the MQTT broker URL.
- `sync-agents.cjs`: A Node.js utility script used to synchronize agent configurations from the `vdesk-agents` Python backend into the frontend's `agents.ts` config.
- `package.json`: Contains standard npm scripts for Astro (`dev`, `build`, `preview`) and lists project dependencies.

## Building and Running

### Prerequisites
- Node.js (v18+)
- npm

### Commands
- **Install Dependencies:**
  ```bash
  npm install
  ```
- **Start Development Server:**
  ```bash
  npm run dev
  ```
  *The app will be available at `http://localhost:4321`.*
- **Build for Production:**
  ```bash
  npm run build
  ```
- **Preview Production Build:**
  ```bash
  npm run preview
  ```

## Development Conventions & Workflows

- **Agent Synchronization:** If new agents are added or removed in the Python backend (`../vdesk-agents/agents.py`), run `node sync-agents.cjs` to automatically update `src/config/agents.ts` so the frontend knows to render them.
- **MQTT Integration:** The application relies on an MQTT broker (e.g., `wss://broker.emqx.io:8084/mqtt`) to receive real-time updates. Agents listen to topics formatted as `voffice/agents/{agent_id}/events`.
- **Aesthetic Constraints:** All UI additions should respect the 16-bit retro style by utilizing NES.css classes and the "Press Start 2P" font.
- **Component Separation:** Maintain the separation of concerns between static environment rendering (`Map.astro`) and dynamic entity behavior (`Officer.astro` and `utils/pathfinding.ts`).
