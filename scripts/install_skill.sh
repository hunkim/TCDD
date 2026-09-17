#!/usr/bin/env bash
# Install TCDD SKILL.md into a Cursor / Grok Bot style skills folder.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:-}"

if [[ -z "$DEST" ]]; then
  if [[ -d "$HOME/.cursor/skills" ]]; then
    DEST="$HOME/.cursor/skills/tcdd-test-codereview-driven-development"
  elif [[ -d "$HOME/agent-data/workflows" ]]; then
    DEST="$HOME/agent-data/workflows/tcdd-test-codereview-driven-development"
  else
    DEST="$HOME/.cursor/skills/tcdd-test-codereview-driven-development"
  fi
fi

mkdir -p "$DEST"
cp "$ROOT/SKILL.md" "$DEST/SKILL.md"
# companion freebuff skill
FB_DEST="$(dirname "$DEST")/freebuff-post-change-review"
mkdir -p "$FB_DEST"
cp "$ROOT/skills/freebuff-post-change-review/SKILL.md" "$FB_DEST/SKILL.md"

echo "Installed:"
echo "  $DEST/SKILL.md"
echo "  $FB_DEST/SKILL.md"
echo
echo "Next: set Freebuff model"
echo "  python3 $ROOT/scripts/set_freebuff_solar_pro4.py"
echo "  python3 $ROOT/scripts/verify_freebuff_solar_pro4.py"
