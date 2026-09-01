---
name: agent-execution-retrospective
description: Use only when the user explicitly asks to review this agent's own completed, paused, or failed execution for execution-method improvements, lessons, or agent-execution root cause. Do not activate for ordinary review, diagnostics, audits, progress checks, cross-context record reviews, tool or workflow behavior checks, option comparisons, next-step decisions, redo-vs-continue decisions, or deliverable improvement unless the user clearly asks for a retrospective of this agent execution.
---

# Agent Execution Retrospective

Version: v0.3.0

## Purpose

Provide a portable, cross-project retrospective for an AI agent's own execution after a bounded task has completed, paused, or failed.

Support agent self-improvement by turning current-run evidence into adoption-ready execution recommendations. This Skill does not learn persistently or change rules by itself; improvements take effect only when the user adopts them into the correct owner.

This Skill is not a task executor, debugging workflow, audit workflow, project planning workflow, incident postmortem, or team retrospective. In general mode, it identifies up to two evidence-backed improvements to how the agent executed the current task. In deep root-cause mode, it traces the execution failure chain only when the user explicitly asks for agent-execution root cause, root fix, repeated-failure cause, or process failure chain.

## Activation

Activate only when all conditions are true:

1. The target is the current agent execution in the current task or conversation.
2. The execution is completed, paused, failed, or the user explicitly asks to review a bounded segment of the current execution.
3. The user explicitly asks for an execution retrospective, AI self-reflection, lessons learned, a review of what the agent did wrong, improvement to the agent's execution method, or root cause of this agent execution.

Do not activate from keywords alone. Words such as review, retrospective, reflect, check, inspect, audit, debug, error, failure, progress, status, improve, root cause, root fix, or fix are not sufficient unless they clearly target this current agent execution as a retrospective.

If this Skill is loaded but the request does not satisfy the activation conditions, ignore this Skill's retrospective workflow and answer the user's primary request normally. Do not force the retrospective output format onto a non-retrospective task.

Acceptable activation examples:

- "Run a retrospective on this agent execution and identify what should improve."
- "Self-reflect on this task and extract lessons for the next run."
- "檢討這次 AI 執行有甚麼做錯。"
- "回顧本次 AI 執行，提出最多兩項可驗收改善。"
- "找出這次 AI 執行重犯問題的根因，並提出可驗收根修。"

## Non-Goals

The following requests are not agent execution retrospectives unless they also include an explicit request to review the current agent execution:

- Progress, status, or current-state review.
- Option comparison, next-step selection, or redo-vs-continue decisions.
- Reading or comparing other conversations, task records, logs, transcripts, or external reports.
- Diagnosing whether a tool, workflow, integration, system component, or generated output behaved correctly.
- Root-cause analysis of a product, project, external system, tool behavior, data issue, or deliverable quality issue.
- Fixing current output, improving a deliverable, or continuing unfinished work.
- Team retrospectives, incident postmortems, governance reviews, or long-term process design.

Handle these as their own primary task using the sources, depth, and output shape that task requires.

## Mixed-Intent Authority Boundary

Use the mixed-intent flow only when the same user request includes both:

1. A primary task such as a decision, diagnosis, plan, comparison, or implementation; and
2. A separate retrospective request that satisfies Activation.

If the retrospective request does not satisfy Activation, handle the whole request as the primary task only.

### Round 1: Primary Task Analysis

Complete the primary task first. Use the sources, present state, options, costs, risks, reversibility, and success conditions needed for that task, then form a provisional decision or result.

This Skill's two-improvement limit, retrospective evidence boundary, output contract, and stop conditions must not restrict Round 1 source coverage, option count, analysis depth, or decision structure.

### Round 2: Retrospective Challenge

Run this only after Round 1 has produced a provisional decision or result.

Round 2 may only:

- Identify counterexamples visible in the current task evidence that would overturn the provisional decision or result.
- Point out unresolved execution root causes that the provisional decision still preserves.
- Propose execution improvements that do not replace the primary outcome.
- Use the two-improvement cap in General Retrospective Mode only. When the retrospective portion explicitly qualifies for Deep Root-Cause Mode, use that mode's recommendation count and stop conditions.

Round 2 must not:

- Change the user's goal by itself.
- Replace the primary decision with process advice.
- Add blockers unrelated to the user's outcome.
- Expand redo, verification, documentation, or governance scope automatically.
- Compress Round 1 because the retrospective is limited to two improvements.

Run Retrospective Challenge at most once per mixed-intent request by default. If a concrete counterexample overturns Round 1, reopen only the affected fact, assumption, or success condition, then form the final decision directly. Do not recursively rerun the full retrospective unless the user explicitly asks.

For mixed-intent answers, use this order:

1. Primary decision or result.
2. Supporting facts.
3. Option comparison, when relevant.
4. Recommendation and stop conditions.
5. Retrospective challenge result.
6. Execution improvements: up to two in General Retrospective Mode, or the causally necessary recommendations in Deep Root-Cause Mode.

Do not begin with the retrospective output and derive the primary decision from it.

## Mode Routing

Default to General Retrospective Mode.

Use Deep Root-Cause Mode only when Activation is satisfied and the user explicitly asks for agent-execution root cause, root fix, repeated-failure cause, why the agent repeated a failure, or the execution/process failure chain.

When Deep Root-Cause Mode applies, read [references/deep-root-cause-mode.md](references/deep-root-cause-mode.md) before analyzing. Its deeper evidence and causal method replaces the general two-improvement cap for that mode only.

Do not use Deep Root-Cause Mode for:

- Simple "what can improve next time" requests after a successful or ordinary run.
- Root-cause analysis of the user's product, data, system, workflow, tool behavior, or deliverable unless the explicit target is this agent's execution method.
- Progress review, ordinary audits, debugging, option comparison, planning, or redo-vs-continue decisions.
- Attempts to use one local failure as automatic permission for broader reset, governance, publication, or external mutation.

## Evidence Boundary

For the retrospective portion, use only evidence available from the current task or conversation and the work actually performed in that context:

- The user's stated goal, success conditions, and explicit corrections.
- Files, data, messages, or artifacts actually read or modified during this task.
- Tool outputs, failures, blockers, retries, and workarounds observed during this task.
- Validation results, counterexamples, and uncovered scope from this task.
- Repeated issues or instruction conflicts directly visible in this task.

Do not:

- Fill gaps from memory of other tasks, old conversations, or external records.
- Scan unrelated projects or sources only to make the retrospective more complete.
- Treat summaries, hearsay, old handoffs, or guesses as evidence.
- Infer the user's feelings, motivations, or unstated requirements.
- Promote a one-off preference into a general rule.

If evidence is insufficient, say "insufficient evidence" and do not invent improvements.

## General Retrospective Method

Review in this order:

1. Restate the task outcome and success conditions.
2. Compare them with the actual work, failures, corrections, and validation evidence.
3. Identify process, source-of-truth, scope, tool-use, decision, or validation issues.
4. Keep only improvements with a clear evidence -> impact -> change -> acceptance chain.
5. Return at most two improvements. If none are concrete and useful, say there are no new recommendations.

Prioritize issues that can cause repeated rework, source drift, wrong public claims, permission or data risk, user confusion, or validation blind spots. Do not list style preferences, isolated minor slips, or generic "could be better" advice.

## Recommendation Gate

Before presenting any recommendation for adoption, verify that:

- The necessary evidence has been read, and known conflicts are stated or resolved.
- The evidence, impact, proposed change, and acceptance test form a complete chain.
- The recommendation's owner matches the issue. Do not turn a project-specific issue into a global rule, and do not use a local technical change to solve an outcome-level problem.

If the gate fails, explain the evidence gap or blocker without listing recommendations or adoption options.

## Output Contract

For a pure General Retrospective Mode response, use this compact structure. Field names may be translated to match the conversation language, but the decision meaning must stay the same.

```markdown
## Agent Execution Retrospective

Overall finding: no concrete improvement / 1 improvement / 2 improvements

Evidence scope: actual current-task evidence used

### Recommendation 1: short title

- Evidence observed: verifiable fact
- Impact: effect on the outcome, user, data, or process
- Risk: risk if not addressed; write "low" if low
- Practical value: why this is worth changing
- Proposed change: which rule, workflow, or validation point should change
- Expected result / acceptance: how next time can prove the improvement worked
- Decision: recommend adoption / do not recommend adoption
```

List a second recommendation only when one truly exists. Do not add filler recommendations.

For Deep Root-Cause Mode, use the output structure in [references/deep-root-cause-mode.md](references/deep-root-cause-mode.md).

For mixed-intent tasks, follow the order in Mixed-Intent Authority Boundary instead of starting with this template.

## Change Boundary

By default, this Skill analyzes and proposes recommendations only. It does not automatically:

- Modify files, rules, project records, memories, or external systems.
- Create tasks, tickets, schedules, commits, releases, deployments, or publications.
- Write recommendations into long-term instructions or handoff records.
- Treat "self-improvement" as authorization for side effects.

If the user chooses to adopt a recommendation, first identify the correct owner:

- Current project behavior: update that project's source of truth.
- Existing skill or workflow behavior: update that skill or workflow's single rule location.
- Cross-project behavior: update this Skill or another explicit cross-project owner.
- One-time behavior: keep it in the current task without creating a long-term rule.

One rule should have one owner. Other documents should only reference it briefly.

## Stop Conditions

Stop without recommendations when:

- The current task has no verifiable execution evidence.
- The issue is only a style preference with no outcome or risk impact.
- The recommendation would require evidence or permissions the user has not provided.
- The recommendation would change the user's success conditions without their decision.
- General Retrospective Mode already has two concrete recommendations.

Do not claim that an improvement has worked, or that nothing regressed, without direct validation from a later run.

## Acceptance Archetypes

Use these archetypes to validate routing and authority:

| User request type | Correct behavior |
| --- | --- |
| "Review current progress." | Status analysis; do not activate this Skill. |
| "Should we redo or continue?" | Decision comparison; do not activate this Skill. |
| "Check whether a workflow's observed behavior deviates from expectation and read the related records." | Diagnostics and record review; do not activate this Skill. |
| "Review this AI execution and identify what went wrong." | Pure agent execution retrospective. |
| "Find the root cause of this AI execution failure and why it repeated." | Deep root-cause mode; current execution evidence only. |
| "First decide whether to redo or continue, then retrospectively challenge whether this AI execution repeats known issues." | Primary decision first, retrospective challenge second. |
| "Based on one failure, delete or reset the project output." | Verify impact radius first; a lesson does not authorize deletion or reset. |


