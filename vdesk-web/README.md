# vdesk-web: The Virtual Agent Office

`vdesk-web` is the visual frontend for the **vdesk** project, an experimental office simulator that visualizes AI agents in a 16-bit, retro-styled environment.

## 🚀 Overview

Built with **Astro** and styled with **NES.css**, this web application provides a real-time view of agents working at their desks. It synchronizes with the Python agent backend via **MQTT**, allowing the UI to animate sprites and display "thinking" bubbles as agents perform tasks.

### Features
- **Retro Aesthetic**: 16-bit pixel art style using [NES.css](https://nostalgic-css.github.io/NES.css/).
- **Real-time Synchronization**: Subscribes to MQTT events (using `mqtt.js`) to reflect agent states (thinking, acting, idling).
- **Responsive Grid**: A pixel-perfect office layout with dynamic agent components.

## 🛠️ Tech Stack
- **Framework**: [Astro 5+](https://astro.build/)
- **Styling**: [NES.css](https://nostalgic-css.github.io/NES.css/)
- **Communication**: [MQTT.js](https://github.com/mqttjs/MQTT.js) via `broker.emqx.io`

## 🏁 Getting Started

### Prerequisites
- [Node.js](https://nodejs.org/) (v18 or higher recommended)
- [npm](https://www.npmjs.com/)

### Installation

1.  Navigate to the web directory:
    ```bash
    cd vdesk-web
    ```

2.  Install dependencies:
    ```bash
    npm install
    ```

3.  Start the development server:
    ```bash
    npm run dev
    ```

The office will be available at `http://localhost:4321`.

## 📂 Project Structure

- `src/pages/index.astro`: Main office layout, grid definition, and desk placement.
- `src/components/Officer.astro`: Reusable agent component. Handles MQTT subscriptions and state-based animations.
- `public/`: Static assets and icons.

## 🔌 MQTT Integration

The UI listens for events on the following topic pattern:
`voffice/agents/{agent_id}/events`

Ensure that the `agentId` prop passed to the `Officer` component in `index.astro` matches the `agent_id` configured in the Python backend.

---
Part of the [vdesk](https://github.com/your-repo/vdesk) project.
