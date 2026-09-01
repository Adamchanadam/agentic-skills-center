# Agentic Skills Center

這裡放可安裝的 agent skills。每個 skill 處理一種工作方式，並寫清楚何時應用、何時停手。

## Skill 清單

### 🔁 Agent Execution Retrospective

把一次 AI 執行留下的證據，轉成下一次可採用的改進建議；任務成功、暫停或失敗後都可以用，但它不是自動學習系統，採納與否由使用者決定。

當你明確要求檢討本次 AI 執行、找出做錯或下次可改善的地方時使用；目前進度、方案比較、重做或續行判斷、工具行為診斷不適用。

一般模式最多兩項改善建議；若你明確要求 AI 執行的根因、根修或重犯原因，會進入較深檢查，但仍只處理本次執行證據，不會自動改檔、開任務或發布。

## 安裝

最直接的方法：下載這個 repo，只複製你要用的 skill。

在 GitHub 頁面按 `Code` -> `Download ZIP`，解壓後進入 `agentic-skills-center` 資料夾。

### Codex on Windows

把 `skills\agent-execution-retrospective` 複製到：

```text
%USERPROFILE%\.codex\skills\
```

然後開一個新對話。可直接寫 `$agent-execution-retrospective` 指名使用；未指名時，是否啟動由 skill 的觸發條件決定。

### macOS or Linux

把 `skills/agent-execution-retrospective` 複製到：

```text
~/.codex/skills/
```

然後開一個新對話。

## 回報問題

回報時請給四件事：

- 你原本叫代理做甚麼。
- 哪個 skill 錯誤啟動，或應啟動但沒有啟動。
- 你期望它怎樣做。
- 這是否會在同類任務重複發生。

一次性的錯誤不一定要改 skill。會穩定影響判斷的問題，才應寫進規則。
