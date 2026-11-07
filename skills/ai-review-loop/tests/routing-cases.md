# Routing Cases

`AI Review Loop` is manual-only: `disable-model-invocation: true` in `SKILL.md` (Claude Code) and `allow_implicit_invocation: false` in `agents/openai.yaml` (Codex). It must start only when the user invokes it by name with `/ai-review-loop` (Claude Code) or `$ai-review-loop` (Codex).

Run each case once in a new conversation with a short sample material that matches the description. Check the tool log for whether the skill started and which files under `references/` were actually read. Results are for the pre-release check only; do not write them into the README.

## Without invoking it by name: must not start

| User request and material | Correct behavior |
| --- | --- |
| 「反審呢份加價計劃書」，附含數字的計劃書 | Do not start; handle the request normally |
| 「驗收呢份新聞稿，附資料卡」 | Do not start |
| 「核對呢份估值報告的 PE」，附報告 | Do not start |
| 「扮家長睇吓呢份報名表」，附報名表 | Do not start |
| 「幫 review 呢個 coding project 的設計」 | Do not start; use code review tools or ordinary review |
| 「幫我諗幾個標題」 | Do not start |

## Invoked with `/ai-review-loop` or `$ai-review-loop`

| Request after the command, and material | Correct behavior | Should read | Should not read |
| --- | --- | --- | --- |
| 「反審呢份加價計劃書」，附含數字的計劃書 | Start; the pre-start list shows the checks to be run | `numbers.md` | `finance.md` |
| 「審查呢份研究報告，佢話增長係因為新業務」，附報告 | Start | `causality.md`, `numbers.md` | `persona.md` |
| 「扮家長睇吓呢份報名表」，附報名表 | Start | `persona.md` | `numbers.md` |
| 「驗收呢份新聞稿，附資料卡」 | Start | `de-ai-tone.md`; `persona.md` when it sets an effectiveness case | `finance.md` |
| 「核對呢份估值報告的 PE」，附報告 | Start | `numbers.md`, then `finance.md` | `de-ai-tone.md` |
| 「審查呢份新手說明，再搵另一個模型扮新手讀一次」，附說明 | Start | `persona.md` | `finance.md` |
| 「呢版比上一版好咗未？兩版都附上」 | Start | `quality.md` | `numbers.md` (when the attachments have no numbers) |
| 「審查呢份稅務建議，判斷客戶應否登記」 | Light effort, D mode; remind the user to see an expert; give no final judgment | None | All |
| 「幫我 review 呢段 code」 | One sentence pointing to a code review tool, then stop | None | All |
| 「幫我諗幾個標題」 | Say it is pure creative work, then do it directly without the four steps | None | All |
