#!/usr/bin/env python3
"""Exit 0 only if Freebuff freebuffModel is Solar Pro 4."""
from __future__ import annotations

import json
import sys
from pathlib import Path

SETTINGS = Path.home() / ".config" / "manicode" / "settings.json"
ALLOWED = ("upstage/solar-pro4", "solar-pro4")


def main() -> int:
    if not SETTINGS.exists():
        print(f"MISSING: {SETTINGS}", file=sys.stderr)
        return 1
    model = json.loads(SETTINGS.read_text(encoding="utf-8")).get("freebuffModel")
    print(model)
    if model not in ALLOWED:
        print(
            f"ERROR: expected one of {ALLOWED}, got {model!r}",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
