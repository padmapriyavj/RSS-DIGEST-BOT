## RSS Digest BotAdd commentMore actions

A Python-based RSS Digest Bot powered by the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) that fetches items from your favorite tech blogs and news sites, and returns AI-generated summaries via Claude.

## Features

- Pulls the latest posts from:
  - [TechCrunch](https://techcrunch.com/feed/)
  - [Hacker News frontpage](https://hnrss.org/frontpage)
- On-demand summaries driven by Claude (or any other LLM client)
- Easy to run under:
  - **STDIO** (for direct stdin/stdout JSON-RPC)
  - **HTTP** (via `mcp dev` + Inspector / Claude Desktop HTTP mode)
  - **Uvicorn** (expose as ASGI app)
- Minimal dependencies: `feedparser`, `mcp[cli]`, `uvicorn`

## Installation

1. **Clone** this repo:
   
   git clone https://github.com/padmapriyavj/rss-digest-bot.git
   cd rss-digest-bot


2. **Create & activate** a virtual environment:

   python3 -m venv .venv
   source .venv/bin/activate

3. **Install** dependencies:

   pip install mcp[cli] feedparser uvicorn

4. **Running the app**

   uv run main.py

5. Restart Claude Desktop to view the tool added to it

## Configuration for Claude Desktop

Add or edit `claude_desktop_config.json` in:

~/Library/Application Support/Claude/claude_desktop_config.json

to include:

jsonc
{
  "mcpServers": {
    "rss-digest-bot": {
      "command": "/full/path/to/your/project/.venv/bin/mcp",
      "args": ["run", "main.py"],
      "transport": "stdio"
    }
  }
}

1. Quit & relaunch Claude Desktop.
2. Under **Developer → rss-digest-bot**, ensure it’s **Enabled**.
3. In chat, click ⚙️ (Search & tools) → confirm **rss-digest-bot** appears → **On**.
