# 🖥️ Linux System MCP SSE Server

The **aimiox Linux System MCP SSE Server** is a lightweight agent for exposing system telemetry, logs, and network information via SSE. It's designed for Ubuntu 22.04+ and integrates seamlessly with the OpenAI Agents SDK or any compatible MCP client. 
> ⚠️ **Note:** This server does **not support HTTPS** and is intended for use on **trusted local networks** or over a **secure VPN** connection.

## ✨ Features

✅ Zero-config startup on modern Ubuntu systems (22.04+)

📡 Exposes system info (CPU, memory, uptime, processes, etc.)

📁 Reads logs from journalctl or custom sources

🌐 Reports on IP addresses, interfaces, and ports

🤖 Compatible with OpenAI Assistant's MCPServerSse

## 🚀 Quick Start

Simply download **mcp_ubuntu_system** binary and run :
```bash
$ mcp_ubuntu_system
```

### ⚙️ Server Arguments

| Option   | Env Variable     | Default   | Description               |
|----------|------------------|-----------|---------------------------|
| `--ip`   | `MCP_LINUX_IP`   | `0.0.0.0` | IP to bind the server to  |
| `--port` | `MCP_LINUX_PORT` | `8003`    | Port to listen on         |

## 🧪 Test with CLI Client

To test the SSE server locally or remotely using the OpenAI Agents SDK, use the included `linux_mcp_cli.py`.

### 1. Set Your API Key

Create a `.env` file in the project root and add:

```env
OPENAI_API_KEY=your-openai-key-here
```
### 2. Set the MCP Endpoint
Edit the following line in `linux_mcp_cli.py`:

```python
MCP_LINUX_URL = "http://<mcp_ip_address>:<mcp_port>/sse"
```
Replace <mcp_ip_address> and <mcp_port> with your actual server values.

### 3. Run the Client

```bash
pip install openai-agents
python3 linux_mcp_cli.py
```

### 4. Interact with the Agent

The client will connect to the SSE server and allow you to chat with the Linux System Agent.


## 📞 Support

For questions, issues, or contributions, open an issue on [github.com/aimiox/mcp](https://github.com/aimiox/mcp), or [email us](mailto:hello@aimiox.com)

