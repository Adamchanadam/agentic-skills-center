# Changelog

## AI Review Loop v1.7.1 - 2026-11-07

- 與方法原文全文對齊後的補正：用戶已給齊設定或要求一次過完成時，列出模擬角色並註明可改，然後直接模擬，不再停下等確認（`persona.md` 與 SKILL.md 原本互相矛盾）。
- 開始前列出的設定統一為目的卡、模式、力度、授權、角色及測試案例。
- 完整力度及主觀成效案例都要獨立審核，不只限於重大爭議。
- `scenarios.md` 的範例補上「不多不少」案例及成效案例；`de-ai-tone.md` 的角色數目及確認依 `persona.md`。
- 已驗收：skill validator（`quick_validate.py`）通過；另一模型（Fable）獨立通讀方法原文、SKILL.md 及全部參考檔，確認 v1.7 新增規則兩邊一致。另在新會話用 v1.7 重跑同一 README 審查：首輪已推斷讀者要做的決定並向用戶提問，列出來源已讀／未讀及覆蓋清單，主觀成效案例交由獨立子代理模擬，找出多項先前遺漏的問題。

限制：重跑只有一次，用的是同一家族模型（Claude）；未有真實讀者測試。

## AI Review Loop v1.7 - 2026-11-07

- 定基準第一項改為「目的卡」：成品給誰用、用完後要做或決定甚麼、怎樣才算成功（不只是沒有錯）、有沒有基準。AI 先從任務、材料及用戶自己的來源文件推斷；只有填不出或有會改變案例的取捨時才問，每輪最多三條並附預設答案，其餘寫明假設後開始。
- 案例分「正確性」及「成效」兩類；目的卡每項成功標準至少一個必要案例。
- 由來源衍生的成品（摘要、README、新聞稿、簡報、翻譯、AI 產物）：先完整讀過全部來源，列出覆蓋清單並記已讀／未讀；必設「不多不少」案例，既不誇大，也不遺漏來源要點。
- 主觀的成效案例（說服力、可讀性）先定基準，再由獨立會話或真人核對；只有自檢最高 PENDING。
- 模擬角色按讀者的任務、決定及職責選，只看成品；用戶糾正方向時，重看目的卡是否寫錯。
- 已驗收：skill validator（`quick_validate.py`）通過；方案由另一模型（Fable）根據一次 README 審查的失敗經過設計。

限制：未在新會話用新規則重跑同一審查任務驗證成效。

## AI Review Loop v1.6 - 2026-11-07

- 移除 REPLAY_PACKET 交接包、REPLAY_READY 及「交接包必須自足」的規則：方法所指的「可重跑」是審查 loop 內的同案重跑，不是把工作轉交另一個 AI。
- 改為報告正文必寫的「比較紀錄」（力度為標準或完整時）：設定（含原始材料版本及重跑類型）、案例（含輸入）與通過條件、原始結果、準則變更、本輪修改、重跑結果（含環境差異）、剩餘問題。
- 主要問題每項寫位置、影響、根因及標籤；時效事實一律附來源和日期；用了 U 模式時附事實卡。
- 「不假設有前文記憶」改為「不假設有上一個對話的記憶」，避免與同一對話內多輪修改矛盾；在新對話續做時先輸出完整比較紀錄。
- 已驗收：skill validator（`quick_validate.py`）通過；修改後由另一模型（Fable）獨立反審 skill 及方法原文，按其發現補回重跑必需的欄位。

限制：新版比較紀錄未經真實審查任務實測。

## AI Review Loop v1.5 - 2026-11-07

- 力度「標準」改交精簡交接包：原始材料可用穩定位置加版本或 hash，或已附上的檔案，代替全文；「完整」仍交完整交接包。
- 正文必須列出主要問題（每項一句，附標籤），用戶不讀交接包也知道改了甚麼、為何改；交接包能寫檔時寫成獨立檔案，正文只給路徑及 REPLAY_READY 狀態。
- 同一對話連續多輪時，中間輪只重寫有變更的欄，最後一輪或用戶要求轉交時才輸出完整一份。
- 修正規則矛盾：附版本或 hash 的公開位置、已附上的檔案，算已列出材料，不再令 REPLAY_READY 變 NO。
- 已驗收：skill validator（`quick_validate.py`）通過；Claude Code on Windows 安裝後逐檔 hash 一致。

限制：精簡交接包未經真實重跑驗證；若日後重跑因讀不到材料而失敗，「標準」力度應回復全文。

## AI Review Loop v1.4 - 2026-11-07

- 首次收錄 `skills/ai-review-loop/`，並附同內容的 `skills/ai-review-loop.zip`。
- 四步審查：定基準、找盲點、修根因、同案重跑；三種模式：D（專業反審）、U（用戶模擬）、P（產物驗收）；每輪可輸出能重跑的 REPLAY_PACKET。
- 模組按需要才讀：`scenarios.md`、`persona.md`、`numbers.md`、`finance.md`、`de-ai-tone.md`、`causality.md`。
- 包含全局「時效資料」規則：政策、價格、利率、市場數據等一律查證並附日期，查不到標 UNVERIFIED。
- 版本號寫在 `SKILL.md` frontmatter 的 `metadata.version`。
- 已驗收：skill validator（`quick_validate.py`）通過；Claude Code on Windows 安裝後逐檔 hash 一致，`/ai-review-loop` 可載入。

限制：未做觸發／不觸發的 routing 測試或 dry-run；未附 `tests/routing-cases.md` 及 `agents/openai.yaml`；Codex 安裝未驗證。

## Agent Execution Retrospective v0.3.0 - 2026-09-01

- 收窄 discovery description 和 activation：普通進度回顧、方案比較、重做或續行判斷、工具行為診斷、跨任務紀錄檢查，不應啟動此 skill。
- 新增深度根因模式：只有明確要求 agent execution 的根因、根修、重犯原因或失敗鏈時才使用。
- 深度模式改用成果差距、直接證據、競爭假說、正確 owner、可推翻條件和 forward-test；不受一般模式「最多兩項改善」上限限制。
- 新增 `references/deep-root-cause-mode.md`，只在深度模式需要時讀取。
- 更新 `tests/routing-cases.md`，加入 runtime 診斷、validator pass 但父成果未改善、反例推翻首個根因、證據不足、單一專案失敗升級為通用規則等測試。
- 已驗收：skill validator 通過；多情景 dry-run 通過；一次代表性新對話通過，工具／流程狀態重複檢查沒有被錯誤轉成 execution retrospective。

限制：這次可證明代表性誤觸發位已通過；長期根修效果仍要靠後續真實任務累積證據。
