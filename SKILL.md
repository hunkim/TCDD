---
name: TCDD Test CodeReview Driven Development
description: >-
  MANDATORY for every non-trivial code change: always run full TCDD — tests →
  code → tests → Freebuff solar-pro4 review → apply sensible findings. Never
  skip Freebuff after a change batch.
---
# TCDD — Test × CodeReview Driven Development

**MANDATORY for EVERY non-trivial code change.** Never skip Freebuff review after a fix/feature batch. Nickname: **TCDD**.

Standing rule: always TCDD — tests gate edits; Freebuff `solar-pro4` gates done.

## Loop (never skip)

1. **Baseline tests** — full relevant suite; record counts.
2. **Code change** — smallest correct fix/feature.
3. **Tests for new code** — add/update coverage + regression tests for bugs fixed.
4. **Re-run tests** until green.
5. **freebuff review (`solar-pro4`)** — whole repo or every touched module; save `FREEBUFF_CODE_REVIEW.md`.
6. **Apply only sensible findings** — P0/P1 + valid P2; defer only when user says so.
7. **Re-test** after review-driven fixes; loop 5–7.
8. **Done** only when tests green AND Freebuff review ran this batch.

## freebuff install (if missing)

```bash
npm install -g freebuff
export PATH="$HOME/.local/bin:$PATH"
freebuff --version
freebuff login
# model: solar-pro4 / upstage/solar-pro4 in settings or session picker
freebuff --cwd <repo>
```

## Review prompt (adapt)

Architecture, security, correctness, observability, cost, test gaps; P0–P2 with paths; write `FREEBUFF_CODE_REVIEW.md`. Prefer the user's language for the summary.

## Rules

- After hotfixes (CSS, server restart, etc.) still run Freebuff before calling done.
- Verify Freebuff claims against real code.
- No secrets in git; no push unless asked.
- Visual: see `diagrams/tcdd-poster-v2.png` in this repo.
