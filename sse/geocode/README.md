# 🌐 aimiox MCP SSE Geocode Server

The **aimiox MCP Geocode SSE Server** provides real-time access to geocoding and reverse geocoding services using Server-Sent Events (SSE). You can use it with your favorite MCP-compatible client — including the [amx-chat UI](https://github.com/aimiox/amx-chat-ui).

---

##  What It Does

- 🔁 Converts **addresses to coordinates**
- 📍 Converts **coordinates to structured addresses**
- 🌐 Streams results via **SSE (Server-Sent Events)** for low-latency integration

---

## Connect to the Public MCP Endpoint

Use this URL in any compatible MCP client (or plain HTTP SSE library):
https://mcp.aimiox.com/v1/geocode/sse?amx_mcp_key=aimiox-public-mcp-key

## Sample Prompt Ideas

📍 **"What are the coordinates for 575 Florida St, San Francisco, CA?"**

📮 **"What address is near 38.7563, -122.4110?"**


