import feedparser
from typing import List
from feedparser import FeedParserDict

def fetch_and_parse(feeds: List[str], limit: int) -> List[FeedParserDict]:

    """
    Fetch each RSS URL in `feeds`, parse it, and return up to `limit`
    entries per feed.
    """

    items: List[FeedParserDict] = []
    for url in feeds:
        parsed = feedparser.parse(url)
        if parsed.bozo:
            print(f"Warning: failed to parse {url}: {parsed.bozo_exception}")
            continue

        items.extend(parsed.entries[:limit])

    return items