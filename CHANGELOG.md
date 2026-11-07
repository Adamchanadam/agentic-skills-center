# Changelog

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
