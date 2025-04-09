# aimiox Chat App (with MCP Client)

🚀 **aimiox Chat** is a containerized AI chat UI designed to work with openai compatible API providers and MCP servers. This setup uses Docker Compose to manage and run the chat UI.

---

## 🧱 Features

- Runs fully in Docker (no system installs needed)
- Supports custom model backends via YAML config
- Automatically mounts persistent chat history
- Customizable UI config

---

## 🚀 Quick Start (with Docker Compose)

### 1. Clone this repo

```bash
git clone https://github.com/aimiox/mcp.git
cd mcp/amx-chat-ui
```

### 2. Create required local files & folders

```
mkdir history

amx-chat-ui/
├── docker-compose.yml
├── aimiox_ui_config.yaml
└── history/
```

### 3. Edit aimiox_ui_config.yaml

This file controls which models you can talk to. Add your own API keys and endpoints.

### 4. Run the app

```
docker compose up -d
```

This will:

- ✅ Pull the latest `aimiox/amx-chat` Docker image
- 🚪 Start the container and expose it on **port `8080`**
- 📄 Mount your local:
  - `aimiox_ui_config.yaml` → `/srv/amx/aimiox_ui_config.yaml`
  - `history/` folder → `/root/.aichat/history`

### 5. Access the chat UI

Open your browser:
```
http://localhost:8080
```
If you're deploying on a remote server, replace localhost with your server’s IP or domain.

You are DONE, enjoy!

If you want to stop the app:

```
docker compose down
```

### 📣 Support

For help, suggestions, or contributions, please open an [issue or discussion](https://github.com/aimiox/mcp) on the aimiox GitHub.

