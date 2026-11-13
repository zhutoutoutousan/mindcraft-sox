# mindcraft-sox

给朋友用的空框架。机制来自 mindcraft，里面没有那一边的日程、练习记录、简历和队列日记。

仓库是公开的。身份、邮箱、求职聊天、模型权重继续放在本机 ignore 里，不要推进来。

## 先读

1. `ROOT.md` 是这套文件语言。
2. `CPU.md` 是你要跑的队列。现在是空的。
3. `pedagogy/pedagogy-cpu.fu.md` 是学习环。`pedagogy/universe.graph.md` 只有四颗种子顶点。
4. `self/goals.toon.md` 换成你自己的目标。不要写年龄和生日。

## 本机才有的目录

- `.private/` 生活细节。已在 `.gitignore`。
- `tmp/` 生成的视频和 PDF。只保留 `tmp/ttl.toon.md`。
- `checkpoints/` 模型权重。已忽略。

技能在 `.cursor/skills/`，Qoder 的副本在 `.qoder/skills/`。cron 在 `cron/`。求职聊天和简历对照没有放进来。

## 语言纠错（sprachkorrektur）

俄语和德语的写作纠错已经装上，两个工具都注册了 hook：

- `.cursor/hooks.json`（Cursor）：`sessionStart` + `beforeSubmitPrompt`
- `.qoder/settings.json`（Qoder）：`SessionStart` + `UserPromptSubmit`
- 规则：`.cursor/rules/de-ru-tutor.mdc` · `.qoder/rules/de-ru-tutor.md`（每轮 RU→DE→ZH + 纠错块）
- 技能：`.cursor/skills/de-ru-tutor/` · `.qoder/skills/de-ru-tutor/`
- 检测：`es`/`de`/`ru` 一个标记词即算写作样本，其他学习语言要两个
- 存储：`pedagogy/_learn/writing-accuracy/` + `pedagogy/_learn/polyglot/`

`pedagogy/_learn/writing-accuracy/state.toon.md` 现在还是 `status: empty`。填好 `todayFocus` 并改成 `status: active` 之后，hook 才会注入焦点并把缺口写进 `bridge.graph.md`。
