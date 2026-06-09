"""Design tokens and platform size presets for visual renderers."""

BASE_TOKENS = {
    "BG": "#ffffff",
    "TEXT": "#1e293b",
    "TEXT_2": "#475569",
    "MUTED": "#94a3b8",
    "GRID": "#e5e7eb",
    "LIGHT_BG": "#f8fafc",
}

THEMES = {
    "default": {
        "ACCENT": "#1f6feb",
        "ACCENT_2": "#0d9488",
        "ACCENT_3": "#7c3aed",
        "WARN": "#dc2626",
        "SUCCESS": "#16a34a",
        "BLUE_BG": "#dbeafe",
        "TEAL_BG": "#ccfbf1",
        "PURPLE_BG": "#ede9fe",
        "RED_BG": "#fee2e2",
    },
    "ocean": {
        "ACCENT": "#0ea5e9",
        "ACCENT_2": "#06b6d4",
        "ACCENT_3": "#155e75",
        "WARN": "#f97316",
        "SUCCESS": "#14b8a6",
        "BLUE_BG": "#e0f2fe",
        "TEAL_BG": "#ccfbf1",
        "PURPLE_BG": "#cffafe",
        "RED_BG": "#ffedd5",
    },
    "sunset": {
        "ACCENT": "#f97316",
        "ACCENT_2": "#ef4444",
        "ACCENT_3": "#b91c1c",
        "WARN": "#dc2626",
        "SUCCESS": "#eab308",
        "BLUE_BG": "#fff7ed",
        "TEAL_BG": "#fef3c7",
        "PURPLE_BG": "#fee2e2",
        "RED_BG": "#fef2f2",
    },
    "forest": {
        "ACCENT": "#16a34a",
        "ACCENT_2": "#65a30d",
        "ACCENT_3": "#a16207",
        "WARN": "#ca8a04",
        "SUCCESS": "#15803d",
        "BLUE_BG": "#f0fdf4",
        "TEAL_BG": "#ecfccb",
        "PURPLE_BG": "#fefce8",
        "RED_BG": "#fef9c3",
    },
    "midnight": {
        "ACCENT": "#7c3aed",
        "ACCENT_2": "#6366f1",
        "ACCENT_3": "#8b5cf6",
        "WARN": "#ec4899",
        "SUCCESS": "#a78bfa",
        "BLUE_BG": "#ede9fe",
        "TEAL_BG": "#e0e7ff",
        "PURPLE_BG": "#fae8ff",
        "RED_BG": "#fce7f3",
    },
}

FONT = "Helvetica Neue"
DPI = 320

PLATFORM_SIZES = {
    "blog_infographic": (3200, 2080),
    "blog_wide": (3200, 1800),
    "linkedin_card": (1080, 1350),
    "linkedin_square": (1080, 1080),
    "linkedin_exhibit": (1200, 627),
    "medium_hero": (1400, 800),
    "medium_inline": (1200, 800),
    "substack_hero": (1200, 630),
}


def get_tokens(theme_name: str = "default") -> dict[str, str]:
    """Return base tokens merged with a named theme."""
    if theme_name not in THEMES:
        raise ValueError(f"Unknown theme: {theme_name}")
    return {**BASE_TOKENS, **THEMES[theme_name]}


def theme_for_index(index: int) -> dict[str, str]:
    """Return a round-robin theme for a visual index."""
    names = list(THEMES.keys())
    return get_tokens(names[index % len(names)])

