"""HTML page assemblers."""
from .config import CARDS_PER_PAGE
from .styles import CSS


def _page_div(cards: list[str]) -> str:
    """Pad a list of card HTML strings to a full page and wrap in .page div."""
    padded = list(cards)
    while len(padded) < CARDS_PER_PAGE:
        padded.append('<div class="card empty"></div>')
    return f'<div class="page">\n{"".join(padded)}\n</div>'


def standalone_page_html(cards: list[str]) -> str:
    """Full HTML document for a single page (used for per-page files)."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8">
<style>\n{CSS}\n</style>
</head>
<body>
{_page_div(cards)}
</body>
</html>"""


def combined_html(page_divs: list[str]) -> str:
    """Full HTML document containing all pages (for browser print-to-PDF)."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8">
<style>\n{CSS}\n</style>
</head>
<body>
{"".join(page_divs)}
</body>
</html>"""
