# Agentic Skills Center

這裡放可安裝的 skills。每個資料夾處理一件事，並寫清楚何時不應使用。

目前先放第一個 skill；之後新增的 skill 會放在同一個清單。

## Skill 清單

### Agent Execution Retrospective

路徑：`skills/agent-execution-retrospective/`

價值：檢討 AI 代理正常完成、卡住或失敗的一次執行，找出做錯或下次可做得更順的地方；它只看執行方法，不接管普通進度回顧或專案方向決策。

何時用：當你明確要求檢討 AI 表現、找出本次可改善位、減少下次來回或避免同類錯誤時才用；即使任務成功，也可以用來優化下次執行方法。

功能：只看本次可見證據，最多提出兩項執行改善；若你只是問目前進度、比較方案、決定重做或續行，這個 skill 不應啟動。

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

## 目錄

```text
skills/
  agent-execution-retrospective/
    SKILL.md
    agents/openai.yaml
    tests/routing-cases.md
docs/
  directory-spec.md
  quality-gate.md
tools/
```

`SKILL.md` 是每個 skill 的行為真源。`tests/routing-cases.md` 記錄應啟動和不應啟動的例子，尤其是不應啟動的邊界。

## 回報問題

回報時請給四件事：

- 你原本叫代理做甚麼。
- 哪個 skill 錯誤啟動，或應啟動但沒有啟動。
- 你期望它怎樣做。
- 這是否會在同類任務重複發生。

一次性的錯誤不一定要改 skill。會穩定影響判斷的問題，才應寫進規則。
