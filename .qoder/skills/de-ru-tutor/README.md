# DE-RU-Tutor: Trilingual Answer Format for Cursor

This skill provides a **standing trilingual answer format** for all Cursor agents in this repository:

```
Ка́ждый отве́т пи́шется на ру́сском языке́.
  _Jede Antwort wird auf Russisch geschrieben._
  每个回答都用俄语书写。

По́сле ка́ждого предложе́ния идёт неме́цкий перево́д (курси́вом) и китай́ский перево́д (обы́чным те́кстом).
  _Nach jedem Satz folgen die deutsche Übersetzung (kursiv) und die chinesische Übersetzung (normaler Text)._
  每句话后面是德语翻译（斜体）和中文翻译（正常文本）。
```

## Features

1. **Russian-first answers** with mandatory stress marks (U+0301) for pronunciation practice
2. **German translations** for B2+ maintenance
3. **Simplified Chinese translations** for sharing with your partner
4. **Dual-language corrections** (DE + RU) at the end of every reply
5. **Automatic integration** with `pedagogy/_learn/` knowledge graphs

## Files

- **`.qoder/rules/de-ru-tutor.md`** — Workspace rule (always applied)
- **`SKILL.md`** — Detailed specification
- **`EXAMPLE.md`** — Example output with corrections
- **`INTEGRATION.md`** — Integration with pedagogy/_learn/ system
- **`README.md`** — This file

## Quick start

The workspace rule is **always active**. Every agent in this repository will automatically:

1. Write answers in Russian, sentence by sentence
2. Add German (italic) and Chinese (plain) translations after each sentence
3. Place stress marks on Russian words (2+ syllables)
4. End with a correction block for both DE and RU

**To disable temporarily:** start your message with a slash command (`/english`, `/deutsch`, etc.)

## Example

**User:** `kannst du den fehler finden?`

**Agent:**

```
Да, могу́.
  _Ja, das kann ich._
  是的，我可以。

Оши́бка в фу́нкции па́рсинга на строке́ 12.
  _Der Fehler steckt in der Parsing-Funktion in Zeile 12._
  错误在解析函数的第 12 行。

---
**Корректура / Korrekturen:**
- **DE** `kannst du den fehler finden?` → `Kannst du den Fehler finden?` — Frage groß beginnen, *Fehler* ist ein Nomen.
- **RU** без оши́бок — в сообще́нии нет ру́сского те́кста.
```

## Pedagogy integration

When corrections are given, the agent:

1. Writes a session file: `pedagogy/_learn/writing-accuracy/sessions/<date>-<slug>.toon.md`
2. Runs: `python pedagogy/_learn/writing-accuracy/ingest_session.py --session <file>`
3. Updates knowledge graphs:
   - `lexicon.graph.md` (German lemmas)
   - `bridge.graph.md` (cross-language gaps)
   - `frames/ru.toon.md` (Russian grammar frames)

See `INTEGRATION.md` for details.

## Supported languages

- **German (`de`)** — professional working proficiency (prior Goethe B2+)
- **Russian (`ru`)** — limited working proficiency
- **Chinese (`zh`)** — native/bilingual proficiency

All three are part of the 16-language learning horizon in `pedagogy/_learn/polyglot/horizon.toon.md`.

## Privacy

**No PII logging.** The system never requests, repeats, logs, or commits:
- Names, addresses, e-mails, phone numbers
- IP addresses, tokens, passwords
- Card numbers, health data, IDs

If such data appears, it is redacted to placeholders (`<name>`, `<email>`, `<token>`).

## Slash commands

Slash commands (`/english`, `/explain`, `/debug`) and their replies are **exempt** from the trilingual format.

## Stress marks

Every Russian word with 2+ syllables gets a stress mark (combining acute, U+0301):

- `предложе́ние` (sentence)
- `перево́д` (translation)
- `кома́нда` (command)

**Exceptions:**
- One-syllable words: `и`, `он`, `путь`
- Words with `ё`: always stressed, never marked
- Quoted user text: stays verbatim

## Correction rules

The correction block at the end of every reply:

```
---
**Корректура / Korrekturen:**
- **DE** `wrong` → `correct` — reason
- **RU** `неве́рное` → `пра́вильное` — объясне́ние
```

**Rules:**
- Both languages, always (even if only one was used)
- Quote smallest wrong fragment
- Write `ohne Fehler` / `без ошибок` when correct
- Max ~6 lines per language

## References

- **Full specification:** `SKILL.md`
- **Example output:** `EXAMPLE.md`
- **Pedagogy integration:** `INTEGRATION.md`
- **Workspace rule:** `.qoder/rules/de-ru-tutor.md`
- **Method contract:** `pedagogy/_learn/writing-accuracy/method.toon.md`
- **16-language horizon:** `pedagogy/_learn/polyglot/horizon.toon.md`

## Notes

- The trilingual format is optimized for:
  1. **Russian pronunciation practice** (via stress marks)
  2. **German B2+ maintenance** (via corrections)
  3. **Sharing with Chinese-speaking partner** (via translations)
- Code, commands, paths, and identifiers are **never translated**
- Lists and headings follow the same pattern: Russian → German → Chinese
- The format is always active unless a slash command is used

---

**Created:** 2026-11-04  
**License:** Internal use only (mindcraft-zttts repository)  
**Author:** Cursor Agent (user: zhutoutoutousan)
