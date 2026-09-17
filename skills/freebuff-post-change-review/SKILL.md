---
name: Freebuff post-change review
description: >-
  Use this when finishing any non-trivial code change — force Freebuff
  freebuffModel to upstage/solar-pro4, run a full Freebuff whole-repo review,
  save FREEBUFF_CODE_REVIEW.md, and summarize findings before calling done.
---
# Freebuff post-change review

Companion skill for TCDD review gate.

## Steps

1. Confirm change complete; tests pass (or note known failures).

2. **Force Solar Pro 4** (required):

```bash
python3 scripts/set_freebuff_solar_pro4.py
python3 scripts/verify_freebuff_solar_pro4.py
```

Or from anywhere after clone:

```bash
python3 <<'PY'
import json
from pathlib import Path
p = Path.home() / ".config/manicode/settings.json"
p.parent.mkdir(parents=True, exist_ok=True)
data = json.loads(p.read_text()) if p.exists() else {}
data["freebuffModel"] = "upstage/solar-pro4"
p.write_text(json.dumps(data, indent=2) + "\n")
print(data["freebuffModel"])
PY
```

3. `freebuff login` if needed.

4. `freebuff --cwd <repo>` — whole-repo review (architecture, security, correctness, observability, cost, test gaps; P0–P2 with paths).

5. Save/update `FREEBUFF_CODE_REVIEW.md` (see `templates/FREEBUFF_CODE_REVIEW.md`). Prefer the user's language.

6. Summarize to the user; no secrets in git.

If step 2 verify fails: **do not review** — TCDD incomplete.
