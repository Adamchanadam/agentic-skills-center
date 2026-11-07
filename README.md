# Agentic Skills Center

這裡放可安裝的 agent skills。每個 skill 處理一種工作方式，並寫清楚何時應用、何時停手。

## Skill 清單

### 🔁 Agent Execution Retrospective

把一次 AI 執行留下的證據，轉成下一次可採用的改進建議；任務成功、暫停或失敗後都可以用，但它不是自動學習系統，採納與否由使用者決定。

當你明確要求檢討本次 AI 執行、找出做錯或下次可改善的地方時使用；目前進度、方案比較、重做或續行判斷、工具行為診斷不適用。

一般模式最多兩項改善建議；若你明確要求 AI 執行的根因、根修或重犯原因，會進入較深檢查，但仍只處理本次執行證據，不會自動改檔、開任務或發布。

### 🧭 Content-Led Interactive Web

由讀者的實際任務、內容主張與品牌感受出發，設計不落入通用模板的高互動網站。它要求先建立設計論點和可驗證的閱讀路徑，再按需要加入有內容角色的視覺物料，而不是把動效或圖片當作「有創意」的代稱。

適合全新網站、重大 redesign、互動 editorial page、作品集或產品體驗；不適合小型 bug fix、孤立元件，或只要求忠實複製既有版面的工作。它不是固定的「品味模板」：每次都按任務的讀者、主題、目的、明示風格與品牌限制重新推導方向；套件的示例只作驗證資料，並不會被 Skill 載入或當成預設風格。

### 🔎 AI Review Loop

先定好判斷標準和測試案例，再按證據找盲點、修根因，用同一批案例重跑確認是否真的改善，最後留下另一個 AI 可照樣重跑的交接包（REPLAY_PACKET）。材料有數字會獨立重算，有因果主張會逐節核對證據，政策、價格、市場數據等會過時的資料一律查證並附日期。

適合審查策略、研究、表單、文案、財務分析及 AI 生成內容；程式碼審查、軟件測試、測試 skill 本身，以及法律、醫療、稅務的最終判斷不適用，未經授權只交建議稿、不改原檔。

## 安裝

最直接的方法：下載這個 repo，只複製你要用的 skill。

在 GitHub 頁面按 `Code` -> `Download ZIP`，解壓後進入 `agentic-skills-center` 資料夾。

### Codex on Windows

把 `skills\agent-execution-retrospective` 複製到：

```text
%USERPROFILE%\.codex\skills\
```

然後開一個新對話。可直接寫 `$agent-execution-retrospective` 指名使用；未指名時，是否啟動由 skill 的觸發條件決定。

如要安裝內容主導互動網站 Skill，改為複製：

```text
skills\content-led-interactive-web
```

到同一個 `%USERPROFILE%\.codex\skills\` 位置。可直接寫 `$content-led-interactive-web`，也可在明確要求設計或重大重做網站時讓它自動適用。

### macOS or Linux

把 `skills/agent-execution-retrospective` 複製到：

```text
~/.codex/skills/
```

然後開一個新對話。

如要安裝內容主導互動網站 Skill，複製 `skills/content-led-interactive-web` 到同一個 `~/.codex/skills/` 位置。

### Claude Code on Windows

AI Review Loop 目前只在這個平台驗證過。把 `skills\ai-review-loop` 複製到：

```text
%USERPROFILE%\.claude\skills\
```

然後開一個新對話。可直接寫 `/ai-review-loop` 指名使用；未指名時，是否啟動由 skill 的觸發條件決定。

## 回報問題

回報時請給四件事：

- 你原本叫代理做甚麼。
- 哪個 skill 錯誤啟動，或應啟動但沒有啟動。
- 你期望它怎樣做。
- 這是否會在同類任務重複發生。

一次性的錯誤不一定要改 skill。會穩定影響判斷的問題，才應寫進規則。
