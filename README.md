# TCDD — Test × CodeReview Driven Development

**TCDD** is a mandatory loop for every non-trivial code change:

**tests → code → tests → Freebuff (`solar-pro4`) review → apply sensible findings → retest**

Tests gate edits. Freebuff gates “done.” Never skip the review step after a change batch.

![TCDD poster](diagrams/tcdd-poster-v2.png)

## Agent skill

Copy [`SKILL.md`](./SKILL.md) into your agent skills folder (for example Cursor / Grok Bot workflows), or point your agent at this repo.

Frontmatter:

- **name:** `TCDD Test CodeReview Driven Development`
- **description:** MANDATORY full TCDD loop with Freebuff `solar-pro4`

## Loop (short)

1. Baseline tests  
2. Code change  
3. Add/update tests  
4. Re-run until green  
5. Freebuff whole-repo review → `FREEBUFF_CODE_REVIEW.md`  
6. Apply sensible P0/P1 (and valid P2)  
7. Re-test; repeat 5–7 as needed  
8. Done only when tests are green **and** Freebuff ran this batch  

## Freebuff

```bash
npm install -g freebuff
freebuff login
freebuff --cwd <repo>
# pick Solar Pro 4 / upstage/solar-pro4
```

## License

MIT
