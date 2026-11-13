# Quick Start: Trilingual DE-RU-ZH Tutor

## What was installed

Three core files + four documentation files:

### Core files (always active)

1. **`.cursor/rules/de-ru-tutor.mdc`** — Workspace rule that applies to every agent
2. **`.cursor/skills/de-ru-tutor/SKILL.md`** — Detailed specification
3. **`AGENTS.md`** — Agent development guide (new file, root of repo)

### Documentation

4. **`.cursor/skills/de-ru-tutor/README.md`** — Overview and quick reference
5. **`.cursor/skills/de-ru-tutor/EXAMPLE.md`** — Real-world example with corrections
6. **`.cursor/skills/de-ru-tutor/INTEGRATION.md`** — Pedagogy system integration guide
7. **`.cursor/skills/de-ru-tutor/QUICKSTART.md`** — This file

## How it works

From now on, **every Cursor agent** in this repository will automatically:

```
Отвеча́ть на ру́сском языке́, предложе́ние за предложе́нием.
  _Auf Russisch antworten, Satz für Satz._
  用俄语回答，一句接一句。

По́сле ка́ждого ру́сского предложе́ния идёт неме́цкий перево́д (курси́в) и китай́ский перево́д (обы́чный текст).
  _Nach jedem russischen Satz folgen die deutsche Übersetzung (kursiv) und die chinesische Übersetzung (normaler Text)._
  每个俄语句子后面是德语翻译（斜体）和中文翻译（正常文本）。

Все ру́сские слова́ с двумя́ и бо́лее слога́ми получа́ют ударе́ние (U+0301).
  _Alle russischen Wörter mit zwei oder mehr Silben erhalten eine Betonung (U+0301)._
  所有有两个或更多音节的俄语单词都有重音符号（U+0301）。

В конце́ ка́жд

ого отве́та — коррекцио́нный блок для неме́цкого И ру́сского.
  _Am Ende jeder Antwort steht ein Korrekturblock für Deutsch UND Russisch._
  每个回答的末尾都有德语和俄语的纠正块。
```

## Tested integration

The system was tested with a sample session file and successfully:

✅ Created `Session_test_ru_integration` vertex in `lexicon.graph.md`  
✅ Recorded raw and corrected sentences  
✅ Linked corrections to grammar frames (`u_menja_N_nom`)  
✅ Supported mixed DE + RU corrections in one session  

## Usage

### Normal workflow (no change needed)

Just chat with Cursor agents as usual. They will answer in the trilingual format automatically.

### Temporary disable

Start your message with a slash command:

```
/english explain how this works
/deutsch erkläre mir das System
```

The agent will answer in that language without the trilingual format.

### Testing the integration manually

```bash
# 1. Create a test session file
cat > pedagogy/_learn/writing-accuracy/sessions/2026-11-04-my-test.toon.md <<'EOF'
schema: writing-accuracy/session
date: 2026-11-04
id: my-test
primaryLang: ru
targetLang: ru

corrections:
  - lang: ru
    original: "я имею вопрос"
    rewrite: "у меня вопрос"
    errorType: управление
    frame: "u_menja_N_nom"
    explanation: "по-русски: у меня + N (Nom)"
EOF

# 2. Run ingestion
python pedagogy/_learn/writing-accuracy/ingest_session.py \
    --session pedagogy/_learn/writing-accuracy/sessions/2026-11-04-my-test.toon.md

# 3. Check the result
tail -20 pedagogy/_learn/writing-accuracy/lexicon.graph.md

# 4. Clean up (do not commit test sessions)
rm pedagogy/_learn/writing-accuracy/sessions/2026-11-04-my-test.toon.md
```

## Key features

| Feature | Description |
|---------|-------------|
| **Russian stress marks** | Every word with 2+ syllables gets U+0301 after the stressed vowel |
| **German corrections** | Verb position, case, gender, articles, separable prefixes |
| **Russian corrections** | Падежи, вид, управление, согласование, порядок слов |
| **Chinese translations** | Natural Simplified Chinese for sharing with your partner |
| **Auto-internalization** | Corrections flow into `pedagogy/_learn/` knowledge graphs |
| **Privacy** | PII is redacted to placeholders (`<name>`, `<email>`, `<token>`) |
| **Code never translated** | Commands, paths, identifiers stay unchanged |

## Supported error types

### German

- `case_gender_article` — `mit der Mann` → `mit dem Mann`
- `prepositions` — `durch dem Raum` → `durch den Raum`
- `word_order_particles` — V2, verb-final in Nebensätze
- `morphology_endings` — `ein groß Mann` → `ein großer Mann`
- `lexis_collocation` — `eine Entscheidung nehmen` → `treffen`
- `orthography` — `daß` → `dass`
- `register_imperative` — `Sag mal` vs `Sagen Sie bitte`
- `sentence_chunking` — Comma rules

### Russian

- `падеж` — Case after prepositions/verbs
- `вид` — Aspect (совершенный vs несовершенный)
- `управление` — Verbal government (`скучать по` + Dat)
- `согласование` — Gender/number/case agreement
- `порядок слов` — Word order (new information last)
- `ударение` — Stress mark placement
- `род` — Gender of loanwords (`проект` is masculine)

## Files created

```
/agent/repos/mindcraft-zttts/
├── .cursor/
│   ├── rules/
│   │   └── de-ru-tutor.mdc              ← Workspace rule (always active)
│   └── skills/
│       └── de-ru-tutor/
│           ├── SKILL.md                  ← Full specification
│           ├── README.md                 ← Overview
│           ├── EXAMPLE.md                ← Demo output
│           ├── INTEGRATION.md            ← Pedagogy integration
│           └── QUICKSTART.md             ← This file
└── AGENTS.md                             ← Agent development guide (new)
```

## Next steps

1. **Start chatting** — The format is already active.
2. **Read EXAMPLE.md** — See how corrections look in practice.
3. **Read INTEGRATION.md** — Understand how sessions flow into knowledge graphs.
4. **Commit your sessions** — Real sessions (not test files) should be committed so the knowledge graph grows.

## References

- Workspace rule: `.cursor/rules/de-ru-tutor.mdc`
- Full spec: `.cursor/skills/de-ru-tutor/SKILL.md`
- Example: `.cursor/skills/de-ru-tutor/EXAMPLE.md`
- Integration: `.cursor/skills/de-ru-tutor/INTEGRATION.md`
- Agent guide: `AGENTS.md`
- Method contract: `pedagogy/_learn/writing-accuracy/method.toon.md`
- 16-language horizon: `pedagogy/_learn/polyglot/horizon.toon.md`
- Russian frames: `pedagogy/_learn/polyglot/frames/ru.toon.md`
- German frames: `pedagogy/_learn/polyglot/frames/de.toon.md`

## Troubleshooting

**Q: The agent is not using the trilingual format.**  
A: Check that `.cursor/rules/de-ru-tutor.mdc` exists and has `alwaysApply: true`. Reload the Cursor window if needed.

**Q: I don't want the format in this session.**  
A: Start your message with `/english` or another slash command.

**Q: Stress marks look wrong.**  
A: Check that your font supports combining diacritics (U+0301). Most modern fonts do.

**Q: Can I add more Russian grammar frames?**  
A: Yes! Edit `pedagogy/_learn/polyglot/frames/ru.toon.md` and add frames following the existing pattern.

**Q: Where do correction sessions go?**  
A: `pedagogy/_learn/writing-accuracy/sessions/<YYYY-MM-DD>-<slug>.toon.md`. Real sessions should be committed.

**Q: Can I use this for other languages?**  
A: Yes. The system supports all 16 languages in `pedagogy/_learn/polyglot/horizon.toon.md`. Add frames under `pedagogy/_learn/polyglot/frames/<lang>.toon.md`.

---

**Created:** 2026-11-04 (UTC+3)  
**Status:** ✅ Installed and tested  
**Commits:** `2814834`, `38f264a`
