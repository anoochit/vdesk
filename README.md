# vdesk: Virtual Agent Office

`vdesk` is an experimental project that visualizes AI agents in a virtual, retro-styled office environment. It uses a Python-based agent runner and an Astro-powered web interface, synchronized via MQTT.

![screenshot](/screenshots/screenshot_01.png)

## Project Structure

This repository is organized into two main components:

- **[vdesk-agents](./vdesk-agents/)**: The Python backend. Defines and runs AI agents using the Google Agent Developer Kit (ADK).
- **[vdesk-web](./vdesk-web/)**: The Astro frontend. A 16-bit visual representation of the office built with NES.css.

## Architecture

- **Communication**: Agents and the web interface communicate in real-time using MQTT via a public broker (`broker.emqx.io`).
- **Events**: Agents publish their internal states (thinking, acting, idling), which the frontend subscribes to for animating sprites and displaying status bubbles.

## Getting Started

### 1. Run the Agents

Navigate to the `vdesk-agents` directory and follow the instructions in its [README](./vdesk-agents/README.md).

```bash
cd vdesk-agents
# Set up venv and install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# Run the agents
python agent_office.py
```

### 2. Start the Web Interface

Navigate to the `vdesk-web` directory and follow the instructions in its [README](./vdesk-web/README.md).

```bash
cd vdesk-web
npm install
npm run dev
```

The office will be accessible at `http://localhost:4321`.

## License

This project is licensed under the [MIT License](./LICENSE).
