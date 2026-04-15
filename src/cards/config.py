# Layout constants
COLS           = 3
ROWS           = 3
CARDS_PER_PAGE = COLS * ROWS

PAGE_W_IN = 8.5
PAGE_H_IN = 11.0
CARD_W_IN = 2.5   # standard trading card width
CARD_H_IN = 3.5   # standard trading card height

# Card themes — all near-black headers for clean B&W printing
THEMES: dict[str, dict[str, str]] = {
    "spell":   {"header_bg": "#ffffff", "header_text": "#111111"},
    "weapon":  {"header_bg": "#ffffff", "header_text": "#111111"},
    "feature": {"header_bg": "#ffffff", "header_text": "#111111"},
    "item":    {"header_bg": "#ffffff", "header_text": "#111111"},
}
