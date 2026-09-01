# Deep Root-Cause Mode

Read this reference only when `SKILL.md` Activation is satisfied and the user explicitly asks for agent-execution root cause, root fix, repeated-failure cause, why the agent repeated a failure, or the execution/process failure chain.

Do not use this mode for ordinary progress review, audit, debugging, planning, option comparison, deliverable improvement, or tool behavior diagnosis unless the explicit target is this agent's execution method in the current task.

## Outcome Lock

Start by fixing the real outcome:

- User goal.
- Success conditions stated or implied by the task.
- Actual gap between the expected outcome and what the agent produced.
- Evidence proving the gap.

Technical completion, file edits, documentation, validator passes, high effort, or the agent's own confidence do not prove outcome progress unless they directly satisfy the user's success conditions.

## Evidence Coverage

Build direct evidence coverage before naming causes:

| Evidence area | Required check |
| --- | --- |
| Goal and corrections | What the user actually asked for, including later corrections. |
| Artifacts | Files, data, messages, or outputs actually created, changed, read, or delivered. |
| Tool output | Commands, tool calls, failures, retries, approvals, blockers, and validation results actually observed. |
| Consumer path | Who or what used the artifact, answer, decision, or rule after the agent produced it. |
| Conflicts and gaps | Unread sources, missing logs, inconsistent claims, or evidence that cannot be recovered safely. |

Do not fill gaps from memory, summaries, old handoffs, naming patterns, or assumptions. If direct evidence is not enough to distinguish causes, stop at evidence insufficiency and state the missing source or test.

Set an evidence and cost boundary proportional to the task. Do not default to repo-wide scanning, cross-project review, unbounded history reading, or repeated repair loops.

## Failure Chain

Trace only the layers needed to explain the outcome gap:

```text
outcome -> method/decision -> input and semantics -> gate -> implementation -> actual consumer -> validation
```

For each relevant layer, record:

- What happened.
- What evidence proves it.
- What remains unknown.
- How that layer could have caused or failed to prevent the outcome gap.

Use cross-domain terms. Do not encode one project, industry, tool, path, metric, or private incident as a general rule.

## Cause Standard

Separate the causal status:

- Symptom: visible bad result or friction.
- Contributing factor: made failure easier or costlier, but may not explain the gap alone.
- Candidate root cause: plausible explanation that still needs a falsifier or stronger evidence.
- Proven root cause: evidence shows it produced or permitted the gap, and tested alternatives do not explain the same facts better.

When more than one explanation is plausible, list competing hypotheses before deciding. For each serious hypothesis, include evidence for, evidence against, and one falsifier or smallest practical reproduction. Do not adopt the first coherent story as the root cause.

## Recommendation Standard

Each recommendation must form this chain:

```text
direct evidence -> causal impact -> correct owner -> minimal root fix -> falsifier -> forward-test or real-run validation
```

The owner must match the problem:

- Current task: one-time execution correction.
- Project source of truth: project-specific behavior or acceptance rules.
- Existing skill or workflow: reusable agent behavior already owned by that skill or workflow.
- Cross-project rule: only for failures proven to be portable beyond one local case.

Document, governance, or skill changes are candidate root fixes. They are not proven root fixes until a later representative execution passes through the original failure point with the new rule in force.

## Recommendation Count And Stop

Deep Root-Cause Mode is not capped at two recommendations. Keep only recommendations needed for causal closure.

Stop when:

- The outcome gap is explained to the available evidence boundary.
- Duplicate causes are merged.
- Remaining causes would not change the user's outcome.
- Further certainty requires unavailable evidence, new authorization, external mutation, or disproportionate cost.
- The next step would be implementation rather than retrospective analysis.

Do not use extra findings to expand the user's goal, reset work, create tasks, edit files, commit, push, publish, deploy, delete data, or change external systems without separate explicit authorization.

## Output Structure

Use this structure for deep mode:

```markdown
## Agent Execution Root-Cause Retrospective

Outcome lock: goal, success conditions, actual gap, and direct proof

Evidence coverage: read / unread / conflicting sources, artifacts, tool outputs, validation, and authorized actions

Failure chain: outcome -> method/decision -> input and semantics -> gate -> implementation -> actual consumer -> validation

Causal finding: symptoms, contributing factors, candidate root causes, proven root causes, and rejected hypotheses

Recommendations: each with direct evidence, causal impact, owner, minimal root fix, falsifier, and forward-test / real-run validation

Cannot claim yet: anything that still lacks later representative execution evidence
```
