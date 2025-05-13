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

MCP_SNMP_URL = "http://<mcp_ip_address>:<mcp_port>/sse"

# ───────────────────────────────────────────────────────────────────────────────
# 2️⃣ Main Entrypoint
# ───────────────────────────────────────────────────────────────────────────────
async def main():
    # Use async context manager to auto-connect / cleanup
    async with MCPServerSse(
        name="mcp_snmp",
        params={"url": MCP_SNMP_URL}
    ) as mcp_server:

        # 3️⃣ Create Agent with built-in MCP support
        agent = Agent(
            name="mcp_snmp_agent",
            instructions=(
                "You are a conversational assistant. "
                "You can chat normally and, when asked, use the "
                "`mcp_snmp` tool to access to SNMP MIBs and devices"
            ),
            model="gpt-4.1-mini",
            mcp_servers=[mcp_server]
        )

        # 4️⃣ CLI Loop 
        print("→ Starting SNMP MCP Agent CLI (type 'exit' to quit)\n")
        conversation = []

        while True:
            user_input = input("💻 You: ")
            if user_input.lower() in ("exit", "quit"):
                break

            conversation.append({"role": "user", "content": user_input})

            result = await Runner.run(
                agent,
                conversation
            )

            print("\n🤖 Assistant:")
            print(result.final_output)
            conversation.append({"role": "assistant", "content": result.final_output})

        print("\n> Goodbye!")

if __name__ == "__main__":
    asyncio.run(main())
