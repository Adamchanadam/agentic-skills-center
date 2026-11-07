# `agentic-skills-center` 目錄規格

## 目標

`agentic-skills-center` 是公開、可持續維護的 skills 集合。它不是某個本機專案的事故紀錄，也不是個人操作日誌。

每個 skill 必須能獨立理解、獨立安裝、獨立驗收。公共內容不得依賴私人路徑、私人任務名稱、一次性事故用語或特定對話歷史。

## 建議根目錄

```text
agentic-skills-center/
  README.md
  LICENSE
  CONTRIBUTING.md
  SECURITY.md
  CHANGELOG.md
  skills/
    agent-execution-retrospective/
      SKILL.md
      agents/
        openai.yaml
      references/
      scripts/
      assets/
      tests/
        routing-cases.md
        dry-run.md
  docs/
    directory-spec.md
    naming.md
    quality-gate.md
    release-process.md
  tools/
    validate-skills.ps1
    package-skill.ps1
```

## 必要與可選

### 必要

```text
README.md
skills/<skill-id>/SKILL.md
```

`README.md` 面向普通使用者，說明這個 repo 有甚麼、誰適合用、怎樣開始。

`SKILL.md` 是每個 skill 的單一行為真源。觸發條件、邊界、工作方法、停止條件和驗收例子應以它為準。

### 建議

```text
skills/<skill-id>/agents/openai.yaml
skills/<skill-id>/tests/routing-cases.md
docs/directory-spec.md
docs/quality-gate.md
```

`agents/openai.yaml` 放 UI 顯示名稱、簡短說明和自動啟動政策。它不可與 `SKILL.md` 的觸發條件打架。

`tests/routing-cases.md` 放觸發與不觸發例子。重點是驗證「何時不應啟動」，因為誤觸發通常比未觸發更傷。

`docs/quality-gate.md` 放公開前檢查清單。

### 按需要才加入

```text
skills/<skill-id>/references/
skills/<skill-id>/scripts/
skills/<skill-id>/assets/
tools/
```

`references/` 只放大型、條件式才需要讀的資料，例如詳細規則、格式說明或長例子。

`scripts/` 只放可重複執行、能減少錯誤的工具。不要為了看起來完整而放空腳本。

`assets/` 放產出時會用到的模板、圖片或其他素材，不放指令文字。

`tools/` 放跨 skill 的檢查、打包或發布輔助工具。

## Skill 命名

資料夾名稱用小寫英文與 hyphen，例如：

```text
agent-execution-retrospective
```

公開名稱可以用 Title Case：

```text
Agent Execution Retrospective
```

命名優先說清楚使用場景。避免太廣的名字，例如 `review`、`checker`、`assistant-helper`。太廣會增加誤觸發。

## 文字治理

全 repo 的 README、報告、發布說明、issue 範本、quality gate 和 skill 介紹，都要用人能直接判斷的文字。

禁止用空泛 AI 味句式撐篇幅，例如只說提升效率、強化體驗、無縫協作、賦能流程，而沒有說清楚實際做甚麼、何時用、何時不用、停在哪裡。

不得替讀者編造情緒、問題、使用場景或反應。公開文字可以列真實用途、已知誤用邊界和驗收例子；不能為了吸引用戶而編造「路人會怎樣想」。

公開文字優先回答：

- 這是甚麼。
- 有甚麼價值。
- 何時使用。
- 何時不要使用。
- 能做甚麼。
- 怎樣安裝或驗收。

README 每個 skill 用同一結構介紹：小標題附一句價值；「適合這種情況」一句，該 skill 的 `SKILL.md` 或參考檔已按工作情景（例如公司部門）列出用途時，可加一個情景對照表，只列情景及常見對象，不列內部模式或模組名稱；「和直接叫 AI 做有甚麼不同」不多於 4 點，每點都要對回該 skill 的 `SKILL.md`；「不適合」一句。若 4 點仍說不清，先修 skill 的定位，不用長文補救。

README 的 skill 標題可用一個穩定 emoji 協助辨識。emoji 只作標記，不可代替 skill 名稱、用途或邊界。

安裝說明只列已核實平台。每個平台只保留一個最簡單方法，不放備用命令補位。沒有驗證過的位置、工具或相容方式，不得用 `Other tools`、`一般工具`、`其他平台` 之類泛稱補位。

## 每個 skill 的最低標準

每個 `SKILL.md` 至少應包含：

- `name`
- `description`
- Purpose
- Activation
- Non-Goals
- Evidence 或 Source Boundary
- Change Boundary
- Stop Conditions
- Acceptance Archetypes

不需要每個 skill 都用同一套標題，但同等資訊必須存在。

## 觸發條件標準

`description` 要短，但必須能分辨相近任務。

好的觸發條件應回答：

- 使用者說甚麼時應啟動？
- 哪些看似相近的句子不應啟動？
- 關鍵字本身是否足夠？
- 如果誤載入，代理應怎樣退出？

若某個 skill 容易被「檢查」、「回顧」、「整理」、「判斷」、「比較」等普通詞誤觸發，必須明寫排除。

## 公開內容禁忌

不得把以下內容寫成公共規則：

- 私人檔案路徑。
- 本機專案名稱。
- 特定對話、特定日期或一次任務的事故細節。
- 私人工作習慣。
- 只對某個工具或某個帳戶成立的假設。
- 情緒化、抱怨式或只有當事人才明白的用語。

如果某次本機失敗值得保留，應改寫成 meta 層規則。

README 不寫內部測試或驗證狀態，例如「已驗證」「未測試」「待確認」。這些狀態只用來決定 README 寫甚麼、不寫甚麼，不寫給讀者看；驗證紀錄只記在 `CHANGELOG.md`。

例子：

```text
不要寫：遇到某次本機任務的原句就啟動 retrospective。
應改成：使用者描述代理執行浪費、重複嘗試或未達目標時，只有在他明確要求檢討代理執行方法，才啟動 retrospective。
```

## 測試資料

每個 skill 建議有 `tests/routing-cases.md`。

格式：

```markdown
| 使用者要求 | 正確行為 |
| --- | --- |
| 「回顧目前進度」 | 普通狀態分析，不啟動 retrospective |
| 「檢討今次有甚麼做錯」 | 啟動 Agent Execution Retrospective |
```

測試不要只驗應啟動，也要驗不應啟動。對容易誤判的 skill，不啟動例子應多於啟動例子。

## 版本與發布

建議使用每個 skill 各自版本。

```text
agent-execution-retrospective v0.2.1
another-skill v0.1.0
```

Git tag 可用：

```text
agent-execution-retrospective-v0.2.1
```

repo 層的 `CHANGELOG.md` 記錄所有 skill 的公開變更。每個 skill 若變更頻繁，可另有自己的 `CHANGELOG.md`。

發布包應只包含該 skill 需要的檔案，不包含本機測試暫存、私人 notes 或未完成草稿。

## 公開前檢查

公開前至少檢查：

- `SKILL.md` 沒有私人路徑、私人專案名或本機事故黑話。
- `description` 不會吸走普通檢查、普通回顧、普通決策或普通方案比較。
- `Activation` 和 `Non-Goals` 沒有互相矛盾。
- 權限邊界不會暗示可以自動 commit、push、publish、delete、deploy 或更改外部服務。
- 驗收例子包含應啟動、應拒絕啟動、混合意圖和高風險誤用。
- 若有 scripts，已能在乾淨環境中執行基本檢查。

## 現行首個 skill

第一個公開 skill：

```text
skills/agent-execution-retrospective/
```

日後新增 skill 時，放在 `skills/<skill-id>/`，並按上述結構在 README 補上介紹。
