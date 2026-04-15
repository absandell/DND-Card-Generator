# DND-Card-Generator
Automation to generate printable DND cards for spells, weapons, feats, and items given an .xlsx input

## Requirements

- Python 3.x
- [openpyxl](https://pypi.org/project/openpyxl/)

```bash
pip install openpyxl
```

## Spreadsheet Format

The input workbook should contain one or more of the following sheets (matched by name, case-insensitive):

| Sheet name         | Card type      |
|--------------------|----------------|
| `Spells`           | Spell cards    |
| `Weapons`          | Weapon cards   |
| `Features`/`Traits`| Feature cards  |
| `Items`            | Item cards     |

## Usage

Run the script from the project root:

```bash
python src/generate-cards.py
```

By default it reads `DND Cards.xlsx` in the current directory and writes output to the `output/` folder.

**Custom input file or output directory:**

```bash
python src/generate-cards.py path/to/cards.xlsx --output path/to/output
```

## Output

Generated files are written to `output/`:

- `spells_page_1.html`, `weapons_page_1.html`, etc. — per-type paginated cards
- `print_all.html` — all cards combined; open in a browser and use **Ctrl+P → Save as PDF** to print

Cards are sized to standard trading card dimensions (2.5" × 3.5"), arranged 3×3 on letter-size pages.
