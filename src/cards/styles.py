"""Card stylesheet — imported by builder.py."""
from .config import PAGE_W_IN, PAGE_H_IN, CARD_W_IN, CARD_H_IN, COLS, ROWS

CSS = f"""
  @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=Alegreya+Sans:wght@400;500;700&display=swap');

  :root {{
    --font-title: 'Cinzel', 'Palatino Linotype', serif;
    --font-body:  'Crimson Text', Georgia, serif;
    --font-ui:    'Alegreya Sans', 'Trebuchet MS', sans-serif;
    --border:     2px solid #111;
    --radius:     5px;
    --rule:       #999;
    --muted:      #666;
    --hbg:        #1a1a1a;
    --htxt:       #ffffff;
    --card-w:     {CARD_W_IN}in;
    --card-h:     {CARD_H_IN}in;
  }}

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    width: {PAGE_W_IN}in;
    background: #fff;
    font-family: var(--font-body);
  }}

  /* ── Page: centres the 3x3 block on letter paper ── */
  .page {{
    width:   {PAGE_W_IN}in;
    height:  {PAGE_H_IN}in;
    padding-top:    calc(({PAGE_H_IN}in - {ROWS} * var(--card-h) - {ROWS - 1} * 0.1in) / 2);
    padding-bottom: calc(({PAGE_H_IN}in - {ROWS} * var(--card-h) - {ROWS - 1} * 0.1in) / 2);
    padding-left:   calc(({PAGE_W_IN}in - {COLS} * var(--card-w) - {COLS - 1} * 0.1in) / 2);
    padding-right:  calc(({PAGE_W_IN}in - {COLS} * var(--card-w) - {COLS - 1} * 0.1in) / 2);
    display: grid;
    grid-template-columns: repeat({COLS}, var(--card-w));
    grid-template-rows:    repeat({ROWS}, var(--card-h));
    gap: 0.1in;
    break-after: page;
  }}

  /* ── Card shell ── */
  .card {{
    width:  var(--card-w);
    height: var(--card-h);
    border: var(--border);
    border-radius: var(--radius);
    background: #fff;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }}
  .card.empty {{ border: 1px dashed #bbb; background: transparent; }}

  /* ── Header ── */
  .card-header {{
    background: var(--hbg);
    color: var(--htxt);
    padding: 0.07in 0.09in 0.06in;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 5px;
    flex-shrink: 0;
    border-bottom: 2px solid #111;
  }}
  .card-header-inner {{ flex: 1; min-width: 0; }}
  .card-name {{
    font-family: var(--font-title);
    font-size: 11pt;
    font-weight: 700;
    line-height: 1.15;
    color: var(--htxt);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}
  .card-subtitle {{
    font-family: var(--font-body);
    font-style: italic;
    font-size: 7pt;
    color: var(--htxt);
    opacity: 0.82;
    margin-top: 1px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}
  .card-header-right {{
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 4px;
    flex-shrink: 0;
  }}
  /* Outlined badge */
  .card-badge {{
    font-family: var(--font-ui);
    font-size: 6pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #111;
    padding: 2px 5px;
    border-radius: 3px;
    border: 1.5px solid #111;
    white-space: nowrap;
  }}

  /* ── Header indicators (Prepared, Proficiency, etc.) ── */
  .header-indicator {{
    display: flex;
    align-items: center;
    gap: 4px;
  }}
  .indicator-label {{
    font-family: var(--font-ui);
    font-size: 6pt;
    color: var(--htxt);
  }}
  .indicator-bubble {{
    width: 13px;
    height: 13px;
    border-radius: 50%;
    border: 2.5px solid #111;
    flex-shrink: 0;
  }}

  /* ── Stat grid ── */
  .stat-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    border-top:    1px solid var(--rule);
    border-bottom: 1px solid var(--rule);
    flex-shrink: 0;
  }}
  .stat-cell {{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 3px 3px;
    min-height: 0.3in;
    border-bottom: 1px solid var(--rule);
  }}
  .stat-cell:nth-last-child(-n+3) {{ border-bottom: none; }}
  .stat-cell:not(:nth-child(3n+1)) {{ border-left: 1px solid var(--rule); }}
  .stat-label {{ font-family: var(--font-ui); font-size: 6.5pt; font-weight: 700; color: #333; line-height: 1.2; }}
  .stat-value {{ font-family: var(--font-ui); font-size: 7pt;   color: #1a1a1a; line-height: 1.25; }}
  .stat-value.muted {{ color: var(--muted); }}
  .stat-sub   {{ font-family: var(--font-ui); font-size: 6pt;   color: var(--muted); line-height: 1.1; }}

  /* ── Body ── */
  .card-body {{
    flex: 1;
    padding: 0.06in 0.09in 0.04in;
    overflow: hidden;
    font-size: 7.5pt;
    line-height: 1.4;
    font-family: var(--font-body);
    color: #1a1a1a;
  }}
  .description  {{ margin-bottom: 4px; }}
  .section-line {{ margin-bottom: 3px; font-size: 7.5pt; }}
  .section-label {{
    font-family: var(--font-ui);
    font-weight: 700;
    font-size: 7pt;
  }}

  /* ── Footer ── */
  .card-footer {{
    padding: 4px 0.09in 0.06in;
    border-top: 1px solid var(--rule);
    flex-shrink: 0;
  }}
  .free-uses-row {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 3px;
  }}
  .free-uses-label {{
    font-family: var(--font-body);
    font-size: 6.5pt;
    color: #333;
  }}
  .free-uses-label em {{ color: var(--muted); }}
  .circles {{ display: flex; gap: 4px; }}
  .circle  {{ width: 11px; height: 11px; border: 1.5px solid #333; border-radius: 50%; }}
  .details-line {{
    font-family: var(--font-body);
    font-size: 6.5pt;
    color: #444;
    display: flex;
    align-items: baseline;
    gap: 4px;
  }}
  .details-rule {{
    flex: 1;
    border-bottom: 1px solid var(--rule);
    height: 0;
  }}

  @media print {{
    body {{ margin: 0; padding: 0; }}
    .page {{ break-after: page; }}
  }}
"""
