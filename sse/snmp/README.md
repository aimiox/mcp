# 🖥️ SNMP MCP SSE Server

The **aimiox SNMP MCP SSE Server** integrates easily with the OpenAI Agents SDK or any SSE compatible MCP client, providing a seamless interface for SNMP device and MIBs interaction and monitoring.

## ✨ Features

✅ **Device Discovery**: Automatically discover SNMP-enabled devices on the network

📡 **Device Management**: Register, update, and remove SNMP devices

🔍 **SNMP Operations**: Perform SNMP get and walk operations with OID validation

📊 **MIB Support**: Map OIDs to human-readable MIB names and descriptions

🔄 **Flexible Device Lookup**: Identify devices by ID, IP address, or system name

🌐 **OID Validation**: Prevents walking top-level MIBs to avoid excessive data retrieval

🤖 **Compatible with OpenAI Agent SDK's MCPServerSse**: Easy integration with AI agents

## 🚀 Quick Start

### Running the Server

Create a directory for config.yaml and data, e.g amx-snmp. Edit config.yaml and add your devices. Create "data" directory for the database.

In the same directory, you can run the server in a docker container with:

```bash
$ sudo docker run -it \
  -p 8001:8001 \
  -v $(pwd)/config.yaml:/app/config.yaml \
  -v $(pwd)/data:/app/data \
  aimiox/amx-snmp-mcp:latest
```

### ⚙️ Configuration

| Env Variable           | Default     | Description                       |
|------------------------|-------------|-----------------------------------|
| `AMX_SNMP_PORT`        | `8001`      | Port to listen on                 |


## 💎 Premium Features

The free version supports **2 devices**.

The **paid version** adds support for:

- 100+ devices
- OID data history

🛠️ For paid access or custom integration, [email us](mailto:hello@aimiox.com)

## 🧪 Test with CLI Client

To test the SNMP MCP server using the OpenAI Agents SDK, use the included `cli.py`.

### 1. Set Your API Key

Create a `.env` file in the project root and add:

```env
OPENAI_API_KEY=your-openai-key-here
```
### 2. Set the MCP Endpoint
Edit the following line in `snmp_mcp_cli.py`:

```python
MCP_SNMP_URL = "http://<mcp_ip_address>:<mcp_port>/sse"
```
Replace <mcp_ip_address> and <mcp_port> with your actual server values.

### 3. Run the Client

```bash
pip install openai-agents
python3 snmp_mcp_cli.py
```

### 4. Interact with the Agent

The client will connect to the SSE server and allow you to chat with SNMP MCP.

#### 🤖 Example Response (via GPT-4.1-mini)

**User Prompt:**
> 💻 You: How can you help me with SNMP devices?

**AI Response:**
> 🤖 Assistant:
> I can help you with SNMP devices in several ways, including:

> 1. Retrieving information from SNMP-enabled devices, such as system details, interface statistics, CPU and memory usage, disk I/O, and more.
> 2. Performing SNMP walk operations to browse whole OID subtrees or get specific OID values.
> 3. Listing all SNMP devices that you have configured.
> 4. Providing details about available MIB modules and specific objects within those MIBs.
> 5. Fetching historical SNMP data if it's available for monitoring trends over time.

> You can ask me to query specific data points or perform walks on your SNMP devices and I will retrieve the relevant information for you. How would you like to start?


## 📞 Support

For questions, issues, or contributions, open an issue on [github.com/aimiox/mcp](https://github.com/aimiox/mcp), or [email us](mailto:hello@aimiox.com)

