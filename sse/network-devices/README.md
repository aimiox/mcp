# 🖥️ AMXNet - Network Devices MCP Server

[![Docker Image](https://img.shields.io/badge/docker-aimiox%2Famxnet--mcp-blue)](https://hub.docker.com/r/aimiox/amxnet-mcp)

The **aimiox AMXNet Network Devices MCP Server** enables seamless interaction with network devices through the OpenAI Agents SDK or any SSE-compatible MCP client. It provides a powerful interface for managing, monitoring, and controlling connected devices like servers, routers, switches, and more.

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
  - [Docker](#using-docker-recommended)
  - [Manual Installation](#manual-installation)
- [Configuration](#-configuration)
- [Device Client](#-device-client)
- [Testing with CLI](#-test-with-cli-client)
- [Premium Features](#-premium-features)
- [Example Usage](#-example-usage)
- [Support](#-support)

## ✨ Features

📡 **Device Management**: Register, monitor, and control remote devices

🔍 **File Operations**: List, read, write, and search files on connected devices

📊 **System Monitoring**: View system information, processes, and resource usage

🔄 **Command Execution**: Run shell commands on remote devices (with proper permissions in premium version)

🌐 **Cross-Platform Support**: Works on Linux, OpenWRT, and OpenBSD* devices

🔒 **Secure Communication**: Device connections with TLS encryption

🤖 **Compatible with OpenAI Agent SDK**: Easy integration with AI agents

## 🏗️ Architecture

AMXNet consists of two main components:

1. **AMXNet MCP Server**: Central server that handles communication between:
   - Device clients (via WebSockets on port 8765)
   - MCP host/AI agents (via SSE on port 8002)

2. **AMXNet Device Client**: Lightweight C client that runs on network devices
   - Available for multiple architectures (x86_64, ARM, MIPS)
   - No library dependencies for maximum portability
   - Minimal resource footprint

## 🚀 Installation

### Using Docker (Recommended)

The easiest way to run AMXNet is using our Docker image:

```bash
# Pull the latest image
docker pull aimiox/amxnet-mcp:latest

# Run the server
sudo ./run_amxnet_mcp.sh
```

Or manually with Docker:

```bash
sudo docker run -d --rm \
  -p 8765:8765 \
  -p 8002:8002 \
  -e AMXNET_DEVICE_PORT=8765 \
  -e AMXNET_SSE_PORT=8002 \
  --name amxnet-mcp \
  aimiox/amxnet-mcp:latest
```

## ⚙️ Configuration

AMXNet can be configured using environment variables:

| Env Variable         | Default | Description                   |
|---------------------|---------|-------------------------------|  
| `AMXNET_DEVICE_PORT` | `8765`  | WebSocket port for devices    |
| `AMXNET_SSE_PORT`    | `8002`  | SSE port for MCP host/AI      |

## 📱 Device Client

The AMXNet Device Client is a lightweight application that runs on your network devices and connects to the AMXNet MCP Server.

### Supported Architectures

We provide pre-built binaries for multiple architectures:

- **x86_64 (64-bit)**: For standard Linux servers and desktops
- **ARM (32-bit)**: For OpenWRT routers, Raspberry Pi, and other ARM devices
- **MIPS**: For older OpenWRT routers and embedded devices

### Installation on Devices

1. Download the appropriate binary for your device architecture
2. Make it executable: ```chmod +x amxnet_device_client_<ARCH>```
3. Run it with the server address: ```./amxnet_device_client_<ARCH> --name <device_name> --server <server_ip> --port <server_port>```

## 💎 Premium Features

The free version supports **2 devices**. The **paid version** adds support for:

- **100+ devices**: Connect and manage 100+ devices
- **Command execution**: Modify files and execute commands on devices
- **Custom integrations**: Integration with your existing systems
- **Priority support**: Direct access to our engineering team

## 🧪 Test with CLI Client

To test the SNMP MCP server using the OpenAI Agents SDK, use the included `cli.py`.

### 1. Set Your API Key

Create a `.env` file in the project root and add:

```env
OPENAI_API_KEY=your-openai-key-here
```
### 2. Set the MCP Endpoint
Edit the following line in `amxnet_cli.py`:

```python
MCP_AMXNET_URL = "http://<mcp_ip_address>:<mcp_port>/sse"
```
Replace <mcp_ip_address> and <mcp_port> with your actual server values.

### 3. Run the Client

```bash
pip install openai-agents
python3 amxnet_cli.py
```

### 4. Interact with the Agent

The client will connect to the SSE server and allow you to chat with AMXNet Network Devices MCP.

#### 🤖 Example Response (via GPT-4.1-mini)

**User Prompt:**
> 💻 You: how can you help me with my network devices?

**AI Response:**
> 🤖 Assistant:
> I can assist you with various tasks related to your network devices, such as:

> 1. Listing all your network devices and their status.
> 2. Retrieving detailed information about a specific device.
> 3. Checking device system information, load, and network data.
> 4. Listing files and reading contents on a device.
> 5. Searching, copying, comparing, and creating files on devices.
> 6. Monitoring running processes on a device.
> 7. Executing shell commands on devices (if you have the necessary permissions).
> 8. Refreshing your device list to get the most current status.

> Let me know what specific assistance you need with your network devices!

## 📞 Support

For questions, issues, or contributions, open an issue on [github.com/aimiox/mcp](https://github.com/aimiox/mcp), or [email us](mailto:hello@aimiox.com)
