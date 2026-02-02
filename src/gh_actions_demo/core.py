from __future__ import annotations

import re
import unicodedata

_NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug.

    - Lowercase
    - Replace non-alphanumeric runs with a single '-'
    - Strip leading/trailing '-'
    """

    lowered = text.casefold()
    ascii_text = (
        unicodedata.normalize("NFKD", lowered).encode("ascii", "ignore").decode("ascii")
    )
    normalized = _NON_ALNUM_RE.sub("-", ascii_text)
    return normalized.strip("-")


def word_count(text: str) -> int:
    """Count words separated by whitespace."""

    words = [w for w in text.split() if w]
    return len(words)
