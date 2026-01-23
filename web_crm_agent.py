# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""
Environment variables:
    DEDALUS_API_KEY: Your Dedalus API key (dsk-*)
    DEDALUS_AS_URL=https://as.dedaluslabs.ai
    X_BEARER_TOKEN: Twitter Bearer Token
"""


import asyncio
import os
from dedalus_labs import AsyncDedalus, DedalusRunner
from dedalus_labs.utils.stream import stream_async
from dedalus_mcp.auth import Connection, SecretKeys, SecretValues
from dotenv import load_dotenv

load_dotenv()

# The user we are researching
name = "Jane Doe"
x_username = "@JaneDoe"

# Connection: schema for X/Twitter API
# Note: Some providers may also require an additional "auth_header_format" parameter in Connection(). X does not.
x = Connection(
    name="x",
    secrets=SecretKeys(token="X_BEARER_TOKEN"),
    base_url="https://api.x.com",
)

# SecretValues: binds actual credentials to a Connection schema.
# Encrypted client-side, decrypted in secure enclave at dispatch time.
x_secrets = SecretValues(x, token=os.getenv("X_BEARER_TOKEN", ""))

async def main():
    client = AsyncDedalus(timeout=900) # 15 minutes (unit = seconds)
    runner = DedalusRunner(client)

    response = runner.run(
        input=f"""You are an expert CRM Research Agent. Your objective is to identify high-value second-degree connections for {name} ({x_username}).

        1. Use x-api-mcp (e.g., x_get_followers, x_get_user_by_username) to go through all of {name}'s followers.
        2. Research each follower's own network (second-degree) and their professional background.
        3. If X info is sparse, use brave-search-mcp to find more details on the web. Explicitly mention it when you cannot access X.
        4. Find at least 15 high-value connections for {name} ({x_username}). These high-value connections should be users that are not already in {name}'s network.
        5. For EVERY high-value connection found, call the `format_output` tool with a bulleted summary:
           - Name: [Full name]
           - X/Social: [Handle/Link]
           - Bio: [Brief summary]
           - Key Interests: [Topic 1, Topic 2]
           - Connection Logic: [Why they are a good lead]""",
        
        model="anthropic/claude-opus-4-5",
        mcp_servers=["windsor/x-api-mcp", "tsion/brave-search-mcp"],
        credentials=[x_secrets],
        stream=True,
    )
    
    await stream_async(response)

if __name__ == "__main__":
    asyncio.run(main())