#!/usr/bin/env python3
"""Force Freebuff model to upstage/solar-pro4 (Solar Pro 4).

Freebuff CLI has no `config set model`. The real setting is:
  ~/.config/manicode/settings.json  ->  freebuffModel
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SETTINGS = Path.home() / ".config" / "manicode" / "settings.json"
ALLOWED = ("upstage/solar-pro4", "solar-pro4")
DEFAULT = "upstage/solar-pro4"


def load() -> dict:
    if not SETTINGS.exists():
        return {}
    return json.loads(SETTINGS.read_text(encoding="utf-8"))


def save(data: dict) -> None:
    SETTINGS.parent.mkdir(parents=True, exist_ok=True)
    SETTINGS.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    p = argparse.ArgumentParser(description="Set Freebuff freebuffModel to Solar Pro 4")
    p.add_argument(
        "--model",
        default=DEFAULT,
        choices=list(ALLOWED),
        help="Model id (default: upstage/solar-pro4)",
    )
    p.add_argument("--check", action="store_true", help="Verify only; do not write")
    args = p.parse_args()

    if args.check:
        data = load()
        model = data.get("freebuffModel")
        print(model)
        if model not in ALLOWED:
            print(
                f"ERROR: freebuffModel must be one of {ALLOWED}, got {model!r}",
                file=sys.stderr,
            )
            print(f"settings: {SETTINGS}", file=sys.stderr)
            return 1
        print(f"OK: {SETTINGS}")
        return 0

    data = load()
    data["freebuffModel"] = args.model
    save(data)
    print(f"freebuffModel = {data['freebuffModel']}")
    print(f"wrote {SETTINGS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
