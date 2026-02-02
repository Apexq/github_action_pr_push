from __future__ import annotations

import argparse
from collections.abc import Sequence

from .core import slugify, word_count


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="gh-actions-demo")
    sub = parser.add_subparsers(dest="command", required=True)

    p_slug = sub.add_parser("slugify", help="Convert input text to a slug")
    p_slug.add_argument("text")

    p_wc = sub.add_parser("wc", help="Count words in input text")
    p_wc.add_argument("text")

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "slugify":
        print(slugify(args.text))
        return 0

    if args.command == "wc":
        print(word_count(args.text))
        return 0

    parser.error("Unknown command")
    return 2
