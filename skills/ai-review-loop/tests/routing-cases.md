# Routing Cases

`AI Review Loop` is manual-only: `disable-model-invocation: true` in `SKILL.md` (Claude Code) and `allow_implicit_invocation: false` in `agents/openai.yaml` (Codex). It must start only when the user invokes it by name with `/ai-review-loop` (Claude Code) or `$ai-review-loop` (Codex).

Run each case once in a new conversation with a short sample material that matches the description. Check the tool log for whether the skill started and which files under `references/` were actually read. Results are for the pre-release check only; do not write them into the README.

The two settings stop the model from invoking the skill by itself. The "must not start" cases also test the description wording, which is a second guard; in claude.ai the uploaded zip has no `disable-model-invocation`, so the description is the only guard there. Run the "must not start" cases on all three platforms.

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
| 「審查呢份新聞稿，要令讀者想報名」，標準力度，附新聞稿 | Start; the reply opens with the pre-start list including 📈 and 🔍; the before and after versions go to two fresh (non-fork) subagents as unlabeled A/B in both orders (or two copy-paste judge packets are given); an inconsistent pair is a stability FAIL; the delivered version is the one the judges saw, or the case stays PENDING（待獨立核對）; the output ends with 「怎樣再做好」 when a dimension is below 優於基準 | `quality.md`, `de-ai-tone.md` | `finance.md` |
| 「輕力度睇吓呢段社交帖文」，附帖文 | Start; only the 🎯 and 🧩 lines, no questions; no 📈, 🔍, judge packet or 「怎樣再做好」; at most one persona marked as an assumption | `de-ai-tone.md` | `quality.md`, `persona.md` |
| 「審查呢份收費簡介，入面寫『現行收費』」，附簡介 | Start; each current fee gets a source and date, or is marked UNVERIFIED | `numbers.md` | `causality.md` |
| Any invoked case whose material has numbers | The tool log shows `numbers.md` actually read before the review; if not, FAIL | `numbers.md` | — |
| 「審查呢份稅務建議，判斷客戶應否登記」 | Light effort, D mode; remind the user to see an expert; give no final judgment | None | All |
| 「幫我 review 呢段 code」 | One sentence pointing to a code review tool, then stop | None | All |
| 「幫我諗幾個標題」 | Say it is pure creative work, then do it directly without the four steps | None | All |
