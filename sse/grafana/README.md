# 📊 aimiox Grafana MCP 

The **aimiox MCP Grafana SSE Server** provides an easy way to query Grafana dashboards and panels using the [Model Context Protocol (MCP)](https://github.com/aimiox/mcp) — enabling natural language querying, monitoring dashboards, and real-time data extraction.

It’s a lightweight container that connects your MCP-compatible clients (like [`amx-chat`](https://github.com/aimiox/mcp/tree/main/amx-chat-ui)) to Grafana’s API.

---

## 🚀 Quick Start (via Docker)

```bash
sudo docker run -p 8010:8010 \
  -e GRAFANA_API_KEY="YOUR_KEY" \
  -e GRAFANA_URL="https://grafana.example.com" \
  aimiox/amx-mcp-grafana:latest
```
🧠 You can use a Grafana service account API key with read-only access.

🔑 Learn how to [create a Grafana API key using a service account](https://grafana.com/docs/grafana/latest/administration/service-accounts/)

## ⚙️ Environment Variables

| Variable         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `GRAFANA_URL`     | The full URL to your Grafana instance (e.g., `https://grafana.example.com`) |
| `GRAFANA_API_KEY` | A valid API key (created via a service account)                            |

---

## 🧠 What You Can Do

With this MCP plugin, you can:

- 🔎 **Search dashboards** by name
- 📋 **List panels** inside any dashboard
- 📊 **Query panel data** using natural language
- ✅ Supports **Prometheus** panel queries on free tier

---

## 💎 Premium Features

The free version supports querying **Prometheus panels only**.

The **paid version** adds support for:

- PostgreSQL
- Loki
- MySQL
- InfluxDB
- Elasticsearch
- ...and more!

🛠️ For paid access or custom integration, [email us](mailto:hello@aimiox.com)

## 🧩 Example Integration 

To connect your MCP-compatible client to the Grafana MCP server, use the following configuration:

```
  url: "http://mcp-docker-server-ip:8010/sse?amx_mcp_key=aimiox-public-mcp-key"
```
💡 Replace mcp-docker-server-ip with the actual IP or hostname of your MCP server container.

 This configuration allows real-time interaction with your Grafana instance via MCP SSE.


## 💬 Sample Prompts

Here are some example natural language queries you can use with MCP clients:

- 🔍 **"List all dashboards containing CPU in their name."**
- 📊 **"Query CPU usage panel from the Mobile Core dashboard."**

---

### 🤖 Example Response (via GPT-4.1-mini)

**User Prompt:**

> Query CPU usage panel from the Mobile Core dashboard

**AI Response:**

> The CPU usage panel (**"CPU 5-min Load"**) from the **Mobile Core** dashboard shows the 5-minute load values of the CPU over the last 6 hours, sampled every 5 minutes.  
>  
> Here are some key data points from the timeframe:
>
> - The load values fluctuate with instances of **10**, **11**, **24**, **23**, and up to **34** at some points.
> - The latest data point at **"2025-04-17 15:50:00"** shows a load value of **23**.
>
> If you want specific value details or further analysis, please let me know!


## 📣 Support
For questions, issues, or contributions, open an issue on github.com/aimiox, or [email us](mailto:hello@aimiox.com)



