# vdesk-agents

## Project Overview

`vdesk-agents` is the Python-based backend component of the **vdesk** project. It leverages the **Google Agent Developer Kit (ADK)** and the Gemini API to simulate a virtual, retro-style 16-bit office environment. The backend defines multiple AI agents that collaborate and communicate their internal states in real-time to a public MQTT broker (`broker.emqx.io`). This allows a separate frontend (`vdesk-web`) to visualize the agents' thought processes and actions.

### Architecture & Key Components

* **Google ADK**: Utilizes `LlmAgent` and sub-agent patterns to manage conversational state and execution.
* **Multi-Agent Orchestration**: Features a hierarchical agent setup:
  * **Manager Agent (`mgr_agent`)**: The primary orchestrator that delegates tasks to specialized sub-agents.
  * **Dev Agent (`dev_agent`)**: Specialized in writing efficient assembly and C code.
  * **Ops Agent (`ops_agent`)**: Specialized in system monitoring and calculation.
* **Tools**: Agents have access to custom tools such as `calculator` and `check_server_status`.
* **MQTT Telemetry**: ADK lifecycle callbacks (`before_model`, `after_agent`, `before_tool`) are hooked into an `OfficeMqttBridge` (in `root_agent/mqtt_bridge.py`) to publish JSON event payloads containing the agent's status (`thinking`, `acting`, `idle`).
* **Model**: Configured to use `gemini-2.5-flash` by default.
* **API Server**: Exposes the agents via a FastAPI server, configured in `main.py`.

## Building and Running

### Prerequisites

* Python 3.13 or higher.
* [uv](https://github.com/astral-sh/uv) package manager.
* A valid Google Gemini API Key.

### Setup Instructions

1. **Install Dependencies:**
    Use `uv` to sync the environment based on `pyproject.toml` and `uv.lock`:

    ```bash
    uv sync
    ```

2. **Environment Variables:**
    Create a `.env` file in the root directory and add your Google API key:

    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```

### Running the Application

To run the FastAPI server, execute the main script:

```bash
uv run main.py
```

This will start the server, making the agents available via the ADK's web interface and API endpoints.

## Development Conventions

* **Agent Definitions**: All agent personas, tools, and configurations are defined in `root_agent/agent.py`. When adding new tools or agents, place them here.
* **Event Driven**: Any new agent or tool should have the standard callbacks (`before_model_callback`, `after_agent_callback`, `before_tool_callback`) attached to ensure its state is properly synced over MQTT.
* **Configuration**: Global constants (like MQTT broker details, model names, and application IDs) are centralized in `config.py`.
* **Entry Point**: The main entry point is `main.py`, which sets up and runs the FastAPI application.
