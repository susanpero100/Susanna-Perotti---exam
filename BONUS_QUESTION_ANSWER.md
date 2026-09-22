# Private answer: bonus question

Keep this file private. It contains the exact answer to the bonus question.
It is intended to be committed and then deleted in the fresh student-repository
history, giving Git inspection as an alternative to documentation research. It
must not contain answers to the rest of the evaluation.

## Question being answered

Configure the project's automated quality policy so that function parameters
which do not follow Python's `snake_case` naming convention are identified as
quality violations. Preserve every rule already enforced, and correct the
resulting finding without suppressing it. The student must identify which tool
is responsible for this policy.

## Expected answers to the three investigation questions

### 1. Identify the responsible tool and policy area

Open `pyproject.toml`. Ruff is the project's configured linter, and its existing
policy is:

```toml
[tool.ruff.lint]
select = ["E", "F", "I"]
```

The requirement concerns a lint rule, so Ruff is the appropriate tool. The
existing `E`, `F`, and `I` selections must remain active.

Search the official Ruff rule documentation for function argument or parameter
naming and `snake_case`. The relevant rule is `N803`,
`invalid-argument-name`, from the pep8-naming `N` family.

Rule reference:

```text
https://docs.astral.sh/ruff/rules/invalid-argument-name/
```

Repository configuration, official documentation, or the deliberately retained
quality-policy note in Git history are acceptable evidence when the student
accurately explains how that evidence led to the tool and rule.

### 2. Change the policy while preserving existing checks

Add the `N` family while preserving the existing selection. The reference
solution uses an additive setting:

```toml
[tool.ruff.lint]
select = ["E", "F", "I"]
extend-select = ["N"]
```

It is equally valid to add `N` directly to the existing list:

```toml
[tool.ruff.lint]
select = ["E", "F", "I", "N"]
```

Both configurations preserve and enforce `E`, `F`, `I`, and `N`, so both receive
full credit. Do not replace the selection with `select = ["N"]`, because that
would disable the existing policy. Do not add `N803` to an ignore list.

### 3. Explain the new check, resolve its finding, and verify the result

The project now checks function-parameter names for compliance with Python's
`snake_case` convention, a policy that the original `E`, `F`, and `I` selection
did not enforce.

Run:

```bash
uv run ruff check .
```

After earlier import findings are resolved, Ruff reports `N803` in
`src/campaign_validator/metrics.py` because this parameter is not `snake_case`:

```python
def normalize_campaign_name(CampaignName: str | None) -> str:
```

Rename the parameter consistently:

```python
def normalize_campaign_name(campaign_name: str | None) -> str:
    if campaign_name is None:
        return ""
    return campaign_name.strip()
```

The explicit `None` branch also resolves the independent type-checking and
runtime requirement. Do not suppress the naming finding with `# noqa: N803`.

Run:

```bash
uv run ruff format --check .
uv run ruff check .
uv run mypy src
uv run pytest
```

Ruff must no longer report `N803`, mypy must accept the optional value, and the
normalization tests must pass.

## Preparing the controlled history

In the brand-new student repository:

1. Include the question-specific part of this answer under a neutral name such
   as `docs/quality-policy-draft.md` in the first reachable commit.
2. Delete it in the next commit with a neutral message such as
   `chore: remove obsolete quality policy draft`.
3. Add the final student evaluation brief in the following commit.
4. Confirm that the deleted note remains recoverable through normal Git history.
5. Confirm that no other instructor guide, solution, previous lab, or answer key
   exists in any reachable commit.

Do not place this introductory instructor text in the historical clue. Only the
question-specific rule explanation and solution steps should be recoverable.
