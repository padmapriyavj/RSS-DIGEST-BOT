# main.py

from server import mcp
import sys
import tools.rss_tools

print(" Starting RSS Digest Bot…", file=sys.stderr)

if __name__ == "__main__":
    # STDIO transport for direct stdin/stdout JSON-RPC
    mcp.run()

