# TCDD — Test × CodeReview Driven Development

**Drop this repo into your agent skills (or clone it) and run the loop.**

**Tests gate code changes. Solar Pro 4 review gates DONE.**

![TCDD poster](diagrams/tcdd-poster-v2.png)

## What you get

| Path | Purpose |
|------|---------|
| [`SKILL.md`](./SKILL.md) | Full TCDD agent skill (copy into Cursor / Grok Bot skills) |
| [`skills/freebuff-post-change-review/SKILL.md`](./skills/freebuff-post-change-review/SKILL.md) | Companion Freebuff review skill |
| [`scripts/set_freebuff_solar_pro4.py`](./scripts/set_freebuff_solar_pro4.py) | Force Freebuff → Solar Pro 4 |
| [`scripts/verify_freebuff_solar_pro4.py`](./scripts/verify_freebuff_solar_pro4.py) | Fail if model is not Solar Pro 4 |
| [`scripts/install_skill.sh`](./scripts/install_skill.sh) | Install skills into agent skills folder |
| [`templates/FREEBUFF_CODE_REVIEW.md`](./templates/FREEBUFF_CODE_REVIEW.md) | Review output template |
| [`templates/manicode.settings.example.json`](./templates/manicode.settings.example.json) | Example Freebuff settings |
| [`diagrams/`](./diagrams/) | TCDD poster + Freebuff setup diagram |

## Quick start (anyone)

```bash
git clone https://github.com/hunkim/TCDD.git
cd TCDD

# 1) Install agent skills
bash scripts/install_skill.sh
# or: bash scripts/install_skill.sh /path/to/your/skills/tcdd-test-codereview-driven-development

# 2) Install Freebuff CLI (if needed)
freebuff --version || npm install -g freebuff
export PATH="$HOME/.local/bin:$PATH"
freebuff login   # once

# 3) Force Solar Pro 4 (REQUIRED before every review)
python3 scripts/set_freebuff_solar_pro4.py
python3 scripts/verify_freebuff_solar_pro4.py

# 4) Run TCDD on your project
#    baseline tests → code → tests → freebuff --cwd <your-repo> → apply → retest
```

## Freebuff + Solar Pro 4 (critical)

![Freebuff Solar Pro 4 setup](diagrams/freebuff-solar-pro4-setup.png)

Freebuff CLI **does not** ship `freebuff config set model` in current versions.

The real setting is:

```text
~/.config/manicode/settings.json
  "freebuffModel": "upstage/solar-pro4"
```

Accepted values: `upstage/solar-pro4` or `solar-pro4`.

**Always SET + VERIFY before Freebuff.** If verify fails → stop. Do not review with another model.

```bash
python3 scripts/set_freebuff_solar_pro4.py
python3 scripts/verify_freebuff_solar_pro4.py
```

Then:

```bash
freebuff --cwd <your-repo>
```

Save the review as `FREEBUFF_CODE_REVIEW.md` for **this** batch (template included).

## TCDD loop (short)

1. Baseline tests  
2. Smallest correct code change  
3. Add/update tests  
4. Tests green  
5. Freebuff / **Solar Pro 4** review → `FREEBUFF_CODE_REVIEW.md`  
6. Verify findings against real code  
7. Apply sensible P0/P1/(valid P2)  
8. Re-test; re-review if code changed  

**DONE** = latest tests green **AND** current-batch Solar Pro 4 Freebuff review complete.

Full rules: [`SKILL.md`](./SKILL.md).

## Agent install (manual)

Copy files:

```text
SKILL.md
  → <skills>/tcdd-test-codereview-driven-development/SKILL.md

skills/freebuff-post-change-review/SKILL.md
  → <skills>/freebuff-post-change-review/SKILL.md
```

Keep `scripts/` available (or copy them next to the skill) so SET/VERIFY commands work.

## License

MIT — see [LICENSE](./LICENSE)
