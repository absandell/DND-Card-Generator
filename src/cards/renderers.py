"""Card HTML renderers — one per card type."""
import html as html_module
from .config import THEMES


# ─────────────────────────────────────────────────────────────────────────────
# Shared helpers
# ─────────────────────────────────────────────────────────────────────────────

def esc(val: object) -> str:
    return html_module.escape(str(val)) if val else ""


def get(row: dict, *keys: str) -> str:
    """Return the first non-empty value matching any key (case-insensitive)."""
    lower_row = {k.lower(): v for k, v in row.items()}
    for k in keys:
        v = lower_row.get(k.lower(), "")
        if v and str(v).strip():
            return str(v).strip()
    return ""


def stat_cell_html(label: str, value: str, sub: str = "") -> str:
    val_html = f'<span class="stat-value">{esc(value)}</span>' if value \
               else '<span class="stat-value muted">&#x2014;</span>'
    sub_html = f'<span class="stat-sub">{esc(sub)}</span>' if sub else ""
    return (
        f'<div class="stat-cell">'
        f'<span class="stat-label">{esc(label)}</span>'
        f'{val_html}{sub_html}'
        f'</div>'
    )


def section_html(label: str, text: str) -> str:
    if not text:
        return ""
    return (
        f'<p class="section-line">'
        f'<span class="section-label">{esc(label)}</span> '
        f'<span class="section-text">{esc(text)}</span>'
        f'</p>'
    )


def pad_stats(cells: list, count: int = 6) -> list:
    """Pad stat list to a multiple of 3 so the grid always ends on a full row."""
    padded = list(cells)
    while len(padded) < count:
        padded.append('<div class="stat-cell"></div>')
    return padded


# ─────────────────────────────────────────────────────────────────────────────
# Card renderers
# ─────────────────────────────────────────────────────────────────────────────

def render_spell_card(row: dict) -> str:
    name         = get(row, "Name", "Spell Name")
    card_type    = get(row, "Type", "Level")
    school       = get(row, "Magic Type", "School")
    casting_time = get(row, "Casting Time")
    range_val    = get(row, "Range")
    target       = get(row, "Target")
    components   = get(row, "Components")
    duration     = get(row, "Duration")
    description  = get(row, "Description", "Effect")
    saving_throw = get(row, "Saving Throw", "Save")
    higher       = get(row, "Higher Levels", "Higher Spell Slots", "At Higher Levels")
    notes        = get(row, "Notes")

    subtitle = ", ".join(filter(None, [school, card_type, components]))
    badge    = card_type or school

    stats = pad_stats([
        stat_cell_html("Casting Time", casting_time),
        stat_cell_html("Range",        range_val),
        stat_cell_html("Duration",     duration),
        stat_cell_html("Target",       target),
        stat_cell_html("Components",   components),
        stat_cell_html("Save",         saving_throw),
    ])

    body = f'<p class="description">{esc(description)}</p>'
    body += section_html("Higher Levels:", higher)
    body += section_html("Notes:", notes)

    return _assemble_card("spell", name, subtitle, badge, stats, body, footer=True, prepared=True)


def render_weapon_card(row: dict) -> str:
    name        = get(row, "Name", "Weapon Name")
    wtype       = get(row, "Type", "Weapon Type", "Category")
    damage      = get(row, "Damage")
    damage_type = get(row, "Damage Type")
    range_val   = get(row, "Range", "Range/Reach", "Reach")
    properties  = get(row, "Properties")
    weight      = get(row, "Weight")
    cost        = get(row, "Cost", "Value", "Price")
    description = get(row, "Description", "Notes", "Effect")
    notes       = get(row, "Notes") if get(row, "Description") else ""

    subtitle = wtype
    badge    = wtype

    stats = pad_stats([
        stat_cell_html("Damage",      damage, damage_type),
        stat_cell_html("Range/Reach", range_val),
        stat_cell_html("Properties",  properties),
        stat_cell_html("Weight",      weight),
        stat_cell_html("Cost",        cost),
    ])

    body  = f'<p class="description">{esc(description)}</p>' if description else ""
    body += section_html("Notes:", notes)

    return _assemble_card("weapon", name, subtitle, badge, stats, body, footer=False, proficiency=True)


def render_feature_card(row: dict) -> str:
    name        = get(row, "Name", "Feature Name", "Trait Name", "Ability")
    source      = get(row, "Source", "Class", "Origin", "Type")
    level       = get(row, "Level")
    uses        = get(row, "Uses", "Uses Per Rest", "Uses/Rest")
    recharge    = get(row, "Recharge", "Rest", "Refresh", "Recovery")
    description = get(row, "Description", "Effect", "Text")
    notes       = get(row, "Notes")

    subtitle_parts = [p for p in [source, f"Level {level}" if level else ""] if p]
    subtitle = ", ".join(subtitle_parts)
    badge    = source or level

    stats = pad_stats([
        stat_cell_html("Source",   source),
        stat_cell_html("Level",    level),
        stat_cell_html("Uses",     uses),
        stat_cell_html("Recharge", recharge),
    ])

    body  = f'<p class="description">{esc(description)}</p>' if description else ""
    body += section_html("Notes:", notes)

    return _assemble_card("feature", name, subtitle, badge, stats, body, footer=False)


def render_item_card(row: dict) -> str:
    name        = get(row, "Name", "Item Name")
    itype       = get(row, "Type", "Item Type", "Category")
    rarity      = get(row, "Rarity")
    attunement  = get(row, "Attunement", "Requires Attunement", "Attune")
    weight      = get(row, "Weight")
    cost        = get(row, "Cost", "Value", "Price")
    count       = get(row, "Count", "Quantity", "Qty")
    description = get(row, "Description", "Effect", "Text")
    notes       = get(row, "Notes")

    subtitle = ", ".join(filter(None, [itype, rarity]))
    badge    = rarity or itype

    stats = pad_stats([
        stat_cell_html("Type",       itype),
        stat_cell_html("Rarity",     rarity),
        stat_cell_html("Count",      count),
        stat_cell_html("Attunement", attunement),
        stat_cell_html("Weight",     weight),
        stat_cell_html("Cost",       cost),
    ])

    body  = f'<p class="description">{esc(description)}</p>' if description else ""
    body += section_html("Notes:", notes)

    return _assemble_card("item", name, subtitle, badge, stats, body, footer=False, proficiency=True)


# ─────────────────────────────────────────────────────────────────────────────
# Card assembler
# ─────────────────────────────────────────────────────────────────────────────

def _assemble_card(
    card_type: str,
    name: str,
    subtitle: str,
    badge: str,
    stats: list,
    body_html: str,
    footer: bool,
    prepared: bool = False,
    proficiency: bool = False,
) -> str:
    t = THEMES[card_type]

    badge_html = (
        f'<span class="card-badge">{esc(badge)}</span>'
        if badge else ""
    )

    prepared_html = """
        <div class="header-indicator">
          <span class="indicator-label">Prepared</span>
          <div class="indicator-bubble"></div>
        </div>""" if prepared else ""

    proficiency_html = """
        <div class="header-indicator">
          <span class="indicator-label">Proficiency</span>
          <div class="indicator-bubble"></div>
        </div>""" if proficiency else ""

    stats_html = f'<div class="stat-grid">{"".join(stats)}</div>' if stats else ""

    footer_html = ""
    if footer:
        footer_html = """
      <div class="card-footer">
        <div class="free-uses-row">
          <span class="free-uses-label"><strong>Free uses</strong> <em>(if any)</em></span>
          <div class="circles">
            <div class="circle"></div><div class="circle"></div>
            <div class="circle"></div><div class="circle"></div>
            <div class="circle"></div>
          </div>
        </div>
        <div class="details-line">
          <span>Details:</span><div class="details-rule"></div>
        </div>
      </div>"""

    return f"""
    <div class="card" data-type="{card_type}" style="--hbg:{t['header_bg']};--htxt:{t['header_text']}">
      <div class="card-header">
        <div class="card-header-inner">
          <div class="card-name">{esc(name)}</div>
          <div class="card-subtitle">{esc(subtitle)}</div>
        </div>
        <div class="card-header-right">
          {badge_html}
          {prepared_html}
          {proficiency_html}
        </div>
      </div>
      {stats_html}
      <div class="card-body">{body_html}</div>
      {footer_html}
    </div>"""
