# tools/rss_tools.py
from typing import List
from server import mcp
from utils.rss_reader import fetch_and_parse

DEFAULT_FEEDS = [
    "https://techcrunch.com/feed/",
    "https://hnrss.org/frontpage"
]

@mcp.tool()
def get_digest(limit: int) -> List[str]:
    """
    Fetch up to `limit` items from your default RSS feeds.
    Returns a list of strings "title: link".
    """
    entries = fetch_and_parse(DEFAULT_FEEDS, limit)
    # Return raw entries; the LLM client will then summarize them.
    return [f"{e.title}: {e.link}" for e in entries]
