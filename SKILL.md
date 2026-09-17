---
name: TCDD Test CodeReview Driven Development
description: >-
  MANDATORY for every non-trivial code change. Execute the complete TCDD
  loop: establish a green test baseline → make the smallest correct code
  change → add/update tests → get tests green → run Freebuff with Solar
  Pro 4 → verify and apply sensible review findings → re-test and
  re-review after review-driven code changes. Never declare DONE unless
  the final tests are green AND a current-batch Solar Pro 4 Freebuff
  review has completed.
---

# TCDD — Test × CodeReview Driven Development

TCDD stands for **Test × CodeReview Driven Development**.

For every non-trivial code change, you MUST complete both gates:

```text
TEST GATE          REVIEW GATE
Tests green   AND  Freebuff / Solar Pro 4 complete
        \             /
         \           /
              DONE
```

**Tests gate code changes.
Solar Pro 4 review gates DONE.**

Do not skip either gate.

---

# 1. When TCDD applies

TCDD is MANDATORY for every non-trivial code change, including:

* bug fixes;
* new features;
* refactoring;
* API changes;
* dependency-related code changes;
* configuration changes affecting behavior;
* performance changes;
* security changes;
* meaningful UI/CSS changes;
* hotfixes.

Minor non-code work such as documentation-only edits may skip the full cycle when no executable behavior can change.

When uncertain whether a change is trivial, run TCDD.

---

# 2. The TCDD loop

Execute these steps IN ORDER.

```text
1. BASELINE TESTS
        ↓
2. SMALLEST CORRECT CODE CHANGE
        ↓
3. ADD / UPDATE TESTS
        ↓
4. RUN TESTS
        ↓
   tests green?
    ↙       ↘
   NO       YES
   ↓         ↓
 FIX      5. FREEBUFF
   ↑       SOLAR PRO 4 REVIEW
   └─test       ↓
          6. VERIFY FINDINGS
                 ↓
          7. APPLY SENSIBLE
             FINDINGS
                 ↓
          code changed?
            ↙       ↘
           YES       NO
            ↓         ↓
         RE-TEST     DONE
            ↓
         GREEN?
          ↓
       FREEBUFF AGAIN
          ↓
          LOOP
```

Never jump directly from implementation to DONE.

---

# 3. Step 1 — Establish baseline

Before modifying code, run the full relevant existing test suite.

Record:

* test command(s);
* number of tests passed;
* number of tests failed;
* existing known failures, if any.

The goal is to distinguish pre-existing failures from regressions caused by the change.

Preferred state:

```text
BASELINE = GREEN
```

If baseline tests fail before any code change:

1. determine whether the failures are related to the requested work;
2. do not silently attribute them to the new change;
3. record the failures;
4. fix them only when necessary or relevant to the task;
5. otherwise preserve them as known pre-existing failures.

Do not claim that the final repository is fully green if known failures remain.

---

# 4. Step 2 — Make the smallest correct change

Implement the requested fix or feature using the smallest sensible change.

Prefer:

* minimal surface area;
* existing project conventions;
* existing abstractions when appropriate;
* backward compatibility unless intentionally changed;
* no unrelated cleanup.

Avoid opportunistic refactoring that is not required for the task.

Do not modify unrelated code merely because it could be improved.

---

# 5. Step 3 — Add or update tests

Every behavior change should have appropriate test coverage.

For bug fixes:

```text
BUG
 ↓
REGRESSION TEST reproducing bug
 ↓
FIX
 ↓
TEST proves bug stays fixed
```

For new features, test:

* normal behavior;
* important edge cases;
* failure behavior where relevant.

Prefer tests that would have failed before the code change and pass afterward.

Do not add meaningless tests merely to increase coverage.

---

# 6. Step 4 — Run tests until green

Run the relevant test suite after implementation.

If tests fail:

```text
FAIL
 ↓
inspect failure
 ↓
fix code or test
 ↓
run tests again
```

Repeat until the relevant suite is green.

Do NOT proceed to the final completion state because tests pass.

Passing tests only opens the **review gate**.

---

# 7. Step 5 — Freebuff / Solar Pro 4 review

Freebuff review is MANDATORY after each completed implementation/fix batch.

The required review model is:

```text
solar-pro4
```

or its provider-qualified equivalent:

```text
upstage/solar-pro4
```

Do not silently substitute another model.

---

## 7.1 Ensure Freebuff exists

First run:

```bash
freebuff --version
```

If Freebuff is unavailable, install it:

```bash
npm install -g freebuff
export PATH="$HOME/.local/bin:$PATH"
freebuff --version
```

Do not reinstall a working Freebuff installation.

---

## 7.2 Ensure authentication

Attempt to use Freebuff.

If authentication is required:

```bash
freebuff login
```

Complete the supported authentication flow and retry.

Do not claim that review completed if:

* authentication failed;
* Freebuff failed to start;
* the review was interrupted;
* no usable review result was produced.

---

## 7.3 Select Solar Pro 4

Required model id:

```text
solar-pro4
```

or provider-qualified:

```text
upstage/solar-pro4
```

**How to select (use what this Freebuff install actually supports):**

1. **Preferred — settings file** (current Freebuff CLI has no `config set` subcommand):

```bash
# ~/.config/manicode/settings.json
# set: "freebuffModel": "upstage/solar-pro4"
```

Verify before review:

```bash
python3 -c "import json;print(json.load(open('$HOME/.config/manicode/settings.json'))['freebuffModel'])"
```

2. **Or** interactive/session model picker inside Freebuff UI.
3. **Or** any CLI option Freebuff exposes in your installed version.

Do **not** invent CLI commands that `freebuff --help` does not list.

When Freebuff exposes the active model, verify Solar Pro 4 is selected.

If a setup poster shows `freebuff config set model …` but your CLI rejects it, use the settings-file method above and continue — do not stop solely because a poster command is missing.

If Solar Pro 4 cannot be selected or verified:

**STOP THE REVIEW GATE.**

Do not silently fall back to another model.

Report the blocker if it cannot be resolved.

---

## 7.4 Review scope

Run Freebuff from the repository root:

```bash
freebuff --cwd <repo>
```

Prefer reviewing the whole repository when practical.

For large repositories, at minimum review:

* every touched file/module;
* directly affected callers/callees;
* related tests;
* relevant configuration;
* security-sensitive boundaries affected by the change.

The review MUST consider:

1. correctness;
2. architecture;
3. security;
4. observability;
5. performance;
6. cost/resource usage;
7. test gaps;
8. regressions;
9. error handling;
10. unintended behavior introduced by the change.

---

## 7.5 Review prompt

Use or adapt the following prompt:

```text
Review the current repository and the current change batch as a senior
software engineer.

Focus on issues introduced by or relevant to the current changes.

Check:

- correctness
- architecture
- security
- observability
- performance
- cost/resource usage
- test coverage and missing regression tests
- error handling
- regressions or unintended behavior

Classify actionable findings:

P0 — critical
P1 — important
P2 — worthwhile improvement

For every finding:

1. identify the concrete problem;
2. provide the relevant file/path and code location when possible;
3. explain why it matters;
4. recommend the smallest sensible fix.

Do not invent findings merely to produce feedback.
Do not recommend unrelated refactoring.

Write the final review to:

FREEBUFF_CODE_REVIEW.md

Prefer the user's language for the summary.
```

---

# 8. Step 6 — Persist and validate the review

The current review must be represented by:

```text
FREEBUFF_CODE_REVIEW.md
```

If Freebuff does not automatically create the file, explicitly instruct it to produce the review there or save the final review output there.

IMPORTANT:

An existing `FREEBUFF_CODE_REVIEW.md` does NOT prove that the current batch was reviewed.

Verify that the review corresponds to the current code/change batch.

Never use a stale review to satisfy the review gate.

---

# 9. Step 7 — Verify findings against real code

Freebuff is a reviewer, not an authority.

Do NOT mechanically implement every suggestion.

For each finding:

```text
FREEBUFF FINDING
       ↓
inspect actual code
       ↓
is the finding real?
   ↙          ↘
 NO           YES
 ↓             ↓
reject       is fix sensible?
               ↙       ↘
              NO       YES
              ↓         ↓
            reject     APPLY
```

Verify:

* the referenced code exists;
* the described behavior is accurate;
* the issue is relevant;
* the recommendation fits repository architecture;
* the fix will not introduce unnecessary complexity.

Apply:

* valid P0 findings;
* valid P1 findings;
* valid and sensible P2 findings.

Reject:

* hallucinated findings;
* incorrect assumptions;
* irrelevant suggestions;
* unnecessary rewrites;
* harmful or disproportionate changes.

If useful, record why a finding was rejected.

---

# 10. Step 8 — Re-test review-driven changes

Any code modification made because of Freebuff invalidates the previous final test state.

Therefore:

```text
FREEBUFF
   ↓
FIX CODE
   ↓
RUN TESTS AGAIN
```

Tests must return to green.

If tests fail:

```text
FAIL
 ↓
FIX
 ↓
TEST
 ↓
repeat until GREEN
```

---

# 11. Step 9 — Re-review after review-driven changes

Any meaningful code change made in response to Freebuff must itself pass the review gate.

Therefore:

```text
Solar Pro 4 review
       ↓
valid finding
       ↓
code change
       ↓
tests green
       ↓
Solar Pro 4 review AGAIN
```

Repeat:

```text
REVIEW
  ↓
VERIFY
  ↓
APPLY
  ↓
TEST
  ↓
REVIEW
```

until the latest review produces no additional sensible findings requiring code changes.

Do not create an infinite cleanup loop for optional or irrelevant suggestions.

The stopping condition is:

```text
Tests green
AND
latest Solar Pro 4 review complete
AND
no remaining sensible finding requires code modification
```

---

# 12. Definition of DONE

Before saying:

* done;
* fixed;
* complete;
* ready;
* finished;
* shipped;

verify EVERY applicable condition below.

```text
[ ] Baseline tests were run
[ ] Baseline results were understood/recorded
[ ] Requested change was implemented
[ ] Appropriate tests were added or updated
[ ] Regression tests were added for fixed bugs where appropriate
[ ] Final relevant tests are green
[ ] Freebuff ran for THIS change batch
[ ] Solar Pro 4 was used
[ ] Active model was verified when Freebuff exposes it
[ ] FREEBUFF_CODE_REVIEW.md represents THIS batch
[ ] Freebuff findings were verified against real code
[ ] Valid P0/P1 findings were handled
[ ] Sensible valid P2 findings were handled
[ ] Review-driven code changes were re-tested
[ ] Review-driven code changes were re-reviewed
[ ] Latest tests are green
[ ] Latest Solar Pro 4 review is complete
[ ] No remaining sensible finding requires another code change
[ ] No secrets were added to git
```

Only then:

```text
DONE = TRUE
```

The fundamental invariant is:

```text
DONE
 =
TESTS GREEN
 AND
CURRENT-BATCH SOLAR-PRO-4 REVIEW COMPLETE
```

---

# 13. Failure handling

Tooling failure does NOT waive TCDD.

If Freebuff cannot complete because of:

* installation failure;
* authentication failure;
* Solar Pro 4 unavailable;
* network failure;
* permission failure;
* repository access failure;
* Freebuff internal error;

then:

1. preserve completed code and test work;
2. capture the relevant error;
3. attempt a reasonable fix when safe;
4. retry;
5. if still blocked, report the blocker clearly.

Do NOT:

```text
Freebuff failed
     ↓
"tests pass, so done"
```

Instead:

```text
Freebuff failed
     ↓
TCDD INCOMPLETE
```

Never fabricate a review.

Never claim Solar Pro 4 reviewed code when it did not.

---

# 14. Hotfix rule

Hotfixes do not bypass TCDD.

Examples:

* CSS fix;
* configuration tweak;
* server/runtime fix;
* small production bug;
* emergency patch.

After the immediate fix:

```text
HOTFIX
  ↓
TEST
  ↓
FREEBUFF / SOLAR PRO 4
  ↓
VERIFY / FIX
  ↓
RE-TEST
  ↓
DONE
```

Urgency may change when the review happens, but it does not remove the review gate.

---

# 15. Git and security rules

Never commit secrets.

Check for accidental inclusion of:

* API keys;
* passwords;
* tokens;
* credentials;
* private keys;
* `.env` contents;
* sensitive internal URLs or data.

Do not push code unless the user explicitly asks.

Do not rewrite unrelated git history.

Do not delete or overwrite user work merely to make tests pass.

---

# 16. Final AI report

When TCDD completes, give the user a concise summary containing:

```text
Change:
- what was changed

Tests:
- baseline result
- final result

Solar Pro 4 review:
- review completed
- important findings
- fixes applied
- findings intentionally rejected, if relevant

Status:
- TCDD complete
```

Do not overwhelm the user with internal execution details unless requested.

If TCDD is blocked, report instead:

```text
Change:
- what was completed

Tests:
- current state

TCDD blocker:
- exact blocking step
- relevant error/reason

Status:
- TCDD incomplete
```

---

# Golden rule

At every point where you are tempted to say **DONE**, ask:

```text
Are the latest tests green?

AND

Did Solar Pro 4 review the current batch after the latest meaningful
code changes?
```

If either answer is NO:

```text
NOT DONE.
```
