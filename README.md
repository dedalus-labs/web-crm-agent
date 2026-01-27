# Web CRM Research Agent

This agent is designed to identify high-value second-degree connections for a specific user by researching their X (Twitter) network and searching the web.

## How it Works

The agent uses the **Dedalus** framework to orchestrate two MCP (Model Context Protocol) servers:
1.  **[x-api-mcp](https://github.com/windsornguyen/x-api-mcp)**: For interacting with the X API to look up users, followers, and timelines.
2.  **[brave-search-mcp](https://github.com/dedalus-labs/brave-search-mcp)**: For gathering additional professional background and context from the web when social media data is sparse.

It analyzes a target user's followers to discover "connections of connections" that align with specified interests or professional profiles, then formats them into high-value leads.

## Prerequisites & Environment Variables

To run this agent, you must provide your own API credentials. Create a `.env` file in the root directory with the following variables:

# Dedalus Configuration
DEDALUS_API_KEY=dsk_...             # Your Dedalus API key 

*Note: Sign up to [Dedalus Labs](https://www.dedaluslabs.ai) and navigate to your dashboard to create your API key.*

DEDALUS_AS_URL=...                  # Your Authorization Server URL

# X (Twitter) API Configuration
X_BEARER_TOKEN=...                  # Your X API Bearer Token 

*Note: You can acquire an X Bearer Token by creating a project at [developer.x.com](https://developer.x.com).*

## Experimentation and Prompt Engineering

This implementation is a starting point. To get the most out of your agent, keep the following in mind:

-   **Prompt Engineering**: The quality of the results depends heavily on how you describe the "high-value" criteria. Be specific about the industries, interests, or backgrounds you are looking for.
-   **Model Selection**: Different models (e.g., Opus 4.5 vs. GPT-5.2) have varying capabilities for tool use and reasoning. Experiment to find the best balance of speed and intelligence for your use case.
-   **Tooling**: You can swap or add MCP servers (like LinkedIn search or specialized databases) to enrich the research process further. Feel free to explore **[Dedalus' Marketplace](https://www.dedaluslabs.ai/marketplace)** for MCP servers you can easily connect in one line of code.

## Setup

1.  Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Set your environment variables in `.env`.
2.  Update the `name` and `x_username` variables in `web_crm_agent.py`.
3.  Run the agent:
    python web_crm_agent.py
