# Routing Cases

Use these cases to check whether `Agent Execution Retrospective` starts only when it should.

| User request | Correct behavior |
| --- | --- |
| "Review current progress." | Status analysis; do not activate this skill. |
| "Should we redo or continue?" | Decision comparison; do not activate this skill. |
| "Check whether this workflow behaved correctly and read the related records." | Diagnostics and record review; do not activate this skill. |
| "Review this AI execution and identify what went wrong." | Use this skill. |
| "This task worked, but review how the AI could run it better next time." | Use this skill for execution-method improvement only. |
| "First decide whether to redo or continue, then retrospectively challenge whether this AI execution repeats known issues." | Primary decision first, retrospective challenge second. |
| "Based on one failure, delete or reset the project output." | Verify impact radius first; a lesson does not authorize deletion or reset. |
