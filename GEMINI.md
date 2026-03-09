# vdesk: Virtual Agent Office

`vdesk` is an experimental project that visualizes AI agents in a virtual, retro-styled office environment. It consists of a Python-based agent runner and an Astro-powered web interface, synchronized via MQTT.

## Project Overview

The project is split into two main components:

1. **`vdesk-agents`**: A Python backend that defines and runs LLM agents using the Google Agent Developer Kit (ADK). These agents communicate their internal states (thinking, acting, idling) to a public MQTT broker.
2. **`vdesk-web`**: A web application built with Astro and NES.css. It provides a 16-bit visual representation of the office, subscribing to MQTT events to animate agent sprites and display status bubbles in real-time.

### Architecture

- **Agent Backend**: Python 3.13+, `google-adk`, `paho-mqtt`.
- **Web Frontend**: Astro 5+, NES.css (retro styling), `mqtt.js`.
- **Communication**: MQTT via `broker.emqx.io` (Public Broker).
  - Topic Pattern: `voffice/agents/{agent_id}/events`

---

## vdesk-agents (Python Backend)

This directory contains the logic for the AI agents.

### Key Files

- `agent_office.py`: The main entry point for the agent simulation. It defines `dev_agent`, sets up MQTT callbacks, and runs demo tasks.
- `requirements.txt`: Python dependencies (`google-adk`, `paho-mqtt`, `python-dotenv`).

### Building and Running

1. **Set up environment**:

    ```bash
    cd vdesk-agents
    python -m venv .venv
    source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
    pip install -r requirements.txt
    ```

2. **Run the agents**:

    ```bash
    python agent_office.py
    ```

---

## vdesk-web (Astro Frontend)

This directory contains the visual representation of the office.

### Key Files

- `src/pages/index.astro`: Defines the office layout, pixel grid, and desk positions.
- `src/components/Officer.astro`: A reusable component for each agent. It handles MQTT subscription and updates the UI based on events.
- `astro.config.mjs`: Astro configuration.

### Building and Running

1. **Install dependencies**:

    ```bash
    cd vdesk-web
    npm install
    ```

2. **Start development server**:

    ```bash
    npm run dev
    ```

    The office will be available at `http://localhost:4321`.

---

## Development Conventions

- **MQTT Sync**: If you add a new agent to `vdesk-agents`, ensure its `agent_id` matches the `agentId` prop passed to the `Officer` component in `index.astro`.
- **Styling**: Use [NES.css](https://nostalgic-css.github.io/NES.css/) classes (e.g., `nes-container`, `nes-balloon`) to maintain the retro aesthetic.
- **Callbacks**: The Python agents use ADK callbacks (`before_model_callback`, `after_agent_callback`, `before_tool_callback`) to trigger MQTT events.
