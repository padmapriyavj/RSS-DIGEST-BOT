import feedparser
from typing import List
from feedparser import FeedParserDict

def fetch_and_parse(feeds: List[str], limit: int) -> List[FeedParserDict]:

    """
    Fetch each RSS URL in `feeds`, parse it, and return up to `limit`
    entries in total (across all feeds), in feed order.
    """

    items: List[FeedParserDict] = []
    for url in feeds:
        if len(items) >= limit:
            break
        parsed = feedparser.parse(url)
        if parsed.bozo:
            print(f"Warning: failed to parse {url}: {parsed.bozo_exception}")
            continue

        remaining = limit - len(items)
        items.extend(parsed.entries[:remaining])

    return items