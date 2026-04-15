#!/usr/bin/env python3
"""
D&D Card Generator
==================
Reads spell, weapon, feature, and item data from an XLSX workbook and
generates printable cards collated onto letter-size pages.

Supported sheets (matched by name, case-insensitive):
  - Spells              -> Spell cards
  - Weapon(s)           -> Weapon cards
  - Features / Traits   -> Feature/Trait cards
  - Items               -> Item cards

Usage:
    python generate-cards.py [input.xlsx] [--output DIR]

Output:
    <output>/
        spells_page_1.html, ...
        print_all.html          (open in browser -> Ctrl+P -> Save as PDF)

Requirements:
    pip install openpyxl
"""

import argparse
import sys
from pathlib import Path

# Allow running directly from the src/ directory
sys.path.insert(0, str(Path(__file__).parent))

from cards.reader import generate


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate printable D&D cards from an XLSX workbook."
    )
    parser.add_argument(
        "input", nargs="?", default="DND Cards.xlsx",
        help="Path to the input XLSX file (default: 'DND Cards.xlsx')",
    )
    parser.add_argument(
        "--output", "-o", default="output",
        help="Output directory (default: output)",
    )
    args = parser.parse_args()

    generate(
        xlsx_path  = Path(args.input),
        output_dir = Path(args.output),
    )


if __name__ == "__main__":
    main()
