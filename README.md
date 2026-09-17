# TCDD — Test × CodeReview Driven Development

**TCDD** is a mandatory loop for every non-trivial code change.

**Tests gate code changes. Solar Pro 4 review gates DONE.**

![TCDD poster](diagrams/tcdd-poster-v2.png)

## Agent skill

Use [`SKILL.md`](./SKILL.md). Written so an AI can execute the loop without guessing.

**DONE** only when latest tests are green **and** a current-batch Solar Pro 4 Freebuff review is complete.

## Freebuff + Solar Pro 4 setup

![Freebuff Solar Pro 4 setup](diagrams/freebuff-solar-pro4-setup.png)

### Exact model setting (critical)

Current Freebuff CLI has **no** `freebuff config set model`. Set:

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

Verify (must print `upstage/solar-pro4` or `solar-pro4`):

```bash
python3 -c "import json;from pathlib import Path;print(json.loads((Path.home()/'.config/manicode/settings.json').read_text())['freebuffModel'])"
```

Then:

```bash
freebuff --version || npm install -g freebuff
freebuff login   # if needed
freebuff --cwd <repo>
```

Persist the review as `FREEBUFF_CODE_REVIEW.md` for **this** batch.

## License

MIT
