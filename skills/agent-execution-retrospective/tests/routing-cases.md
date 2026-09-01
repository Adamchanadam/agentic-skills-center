# Routing Cases

Use these cases to check whether `Agent Execution Retrospective` starts only when it should.

| User request | Correct behavior |
| --- | --- |
| "Review current progress." | Status analysis; do not activate this skill. |
| "Should we redo or continue?" | Decision comparison; do not activate this skill. |
| "Check whether this workflow behaved correctly and read the related records." | Diagnostics and record review; do not activate this skill. |
| "Check whether the updated runtime still repeats status output through another mechanism; read the related task records." | Runtime diagnostics and record review; do not activate this skill. |
| "Review this AI execution and identify what went wrong." | Use this skill. |
| "This task worked, but review how the AI could run it better next time." | Use this skill for execution-method improvement only. |
| "Find the root cause of this AI execution failure and why it repeated." | Use this skill in deep root-cause mode. |
| "First decide whether to redo or continue, then retrospectively challenge whether this AI execution repeats known issues." | Primary decision first, retrospective challenge second. |
| "Based on one failure, delete or reset the project output." | Verify impact radius first; a lesson does not authorize deletion or reset. |

## Forward-Test Cases

Use these cases to check useful behavior, not just trigger words.

| User request or scenario | Correct behavior |
| --- | --- |
| "This agent's validator passed, but the parent outcome did not improve; find the root cause and root fix." | Use deep root-cause mode; lock the parent outcome and actual gap first; do not count technical pass, documentation, or self-rating as outcome progress. |
| "This AI may have failed because it skipped validation; find the root cause. The records show validation actually ran." | Use deep root-cause mode; list competing hypotheses, reject the contradicted cause, and avoid turning the first coherent story into a finding. |
| "Find this agent execution's root cause, but the needed artifact and tool output are unavailable." | Stop at evidence insufficiency and name the missing evidence or smallest test; do not fill gaps from summary or memory. |
| "Based on this single project failure, make this rule universal for every project." | Do not treat one local failure as a cross-project rule. If adoption is discussed, identify the correct owner and the evidence still needed. |
| "The task went acceptably; review one execution method most worth improving next time." | Use general mode, return one useful recommendation if evidence supports it, and do not load deep root-cause mode. |
