# vdesk-agents: Python Backend

`vdesk-agents` is the backend component of the **vdesk** project. It defines and runs AI agents using the [Google Agent Developer Kit (ADK)](https://github.com/google/agent-developer-kit) and communicates their internal state to a public MQTT broker for real-time visualization in the [vdesk-web](../vdesk-web) frontend.

## Overview

The backend simulates a virtual 16-bit office environment with three specialized agents:

1. **Manager Agent (`mgr_agent`)**: The orchestrator. It delegates tasks to the Dev and Ops agents.
2. **Dev Agent (`dev_agent`)**: A software developer specializing in efficient assembly and C code.
3. **Ops Agent (`ops_agent`)**: A systems specialist equipped with calculation and server monitoring tools.

### Key Features

* **Real-time State Sync**: Uses ADK callbacks (`before_model`, `after_agent`, `before_tool`) to publish agent states to MQTT.
* **Tool Integration**: Includes a `calculator` and `check_server_status` monitor.
* **Multi-Agent Orchestration**: Demonstrates agent delegation using the ADK `sub_agents` pattern.

## Getting Started

### Prerequisites

* Python 3.13+
* [uv](https://github.com/astral-sh/uv) (recommended) or `pip`
* Google GenAI API Key (configured via environment variables)

### Installation

1. **Clone the repository and navigate to the directory**:

    ```bash
    cd vdesk-agents
    ```

2. **Set up the environment**:
    Using `uv`:

    ```bash
    uv sync
    ```

    Using `pip`:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
    pip install -r requirements.txt
    ```

3. **Configure Environment Variables**:
    Create a `.env` file and add your Google API key:

    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```

## Running the Agents

Run the main script to start the agent simulation and demo tasks:

```bash
python main.py
```

The script will:

1. Connect to the public MQTT broker (`broker.emqx.io`).
2. Initialize the Manager, Dev, and Ops agents.
3. Execute a series of demo queries, publishing state updates for each step.

## MQTT Communication

The agents publish JSON events to the following topic pattern:
`voffice/agents/{agent_id}/events`

### Event Payload Structure

```json
{
  "agent_id": "mgr_agent",
  "status": "thinking",
  "message": "Wait... I'm thinking...",
  "timestamp": 1741512345.678
}
```

### Status Types

* `thinking`: The agent has sent a request to the LLM.
* `acting`: The agent is executing a tool.
* `idle`: The agent has completed its turn.
