# ───────────────────────────────────────────────────────────────────────────────
# aimiox.com 
# Grafana MCP Demo. Chat with your grafana dashboard data.
# ───────────────────────────────────────────────────────────────────────────────

import os
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner  # pip install openai-agents
from agents.mcp.server import MCPServerSse

# ───────────────────────────────────────────────────────────────────────────────
# 1️⃣ Load environment
# ───────────────────────────────────────────────────────────────────────────────
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("Set OPENAI_API_KEY in your .env")

GRAFANA_MCP_URL = os.getenv("GRAFANA_MCP_URL")
if not GRAFANA_MCP_URL:
    raise RuntimeError("Set GRAFANA_MCP_URL in your .env")

# ───────────────────────────────────────────────────────────────────────────────
# 2️⃣ Main 
# ───────────────────────────────────────────────────────────────────────────────
async def main():
    # Use async context manager to auto-connect / cleanup
    async with MCPServerSse(
        name="grafana_mcp",
        params={"url": GRAFANA_MCP_URL}
    ) as mcp_server:

        # 3️⃣ Create Agent with built-in MCP support
        agent = Agent(
            name="GrafanaMCPAgent",
            instructions=(
                "You are a conversational assistant. "
                "You can chat normally and, when asked, use the "
                "`grafana_mcp` tool to fetch or subscribe to dashboard data."
            ),
            model="gpt-4.1-mini",
            mcp_servers=[mcp_server]
        )

        # 4️⃣ CLI Loop 
        print("→ Starting aimiox Grafana MCP Agent Demo (type 'exit' to quit)\n")
        conversation = []

        while True:
            user_input = input("\n>>> You: ")
            if user_input.lower() in ("exit", "quit"):
                break

            conversation.append({"role": "user", "content": user_input})

            result = await Runner.run(
                agent,
                conversation
            )

            print("\nAssistant:")
            print(result.final_output)
            conversation.append({"role": "assistant", "content": result.final_output})

        print("\n> Goodbye!")

if __name__ == "__main__":
    asyncio.run(main())