# Example: Trilingual RU → DE → ZH answer with corrections

## User input

```
Ich möchte das neue feature in die develop branch mergen, aber ich bin nicht sicher ob der code bereit ist. kannst du mir helfen?

Я уже запусти́л тесты, но не все прошли́.
```

## Agent output

Коне́чно, помогу́ вам.
  _Natürlich helfe ich Ihnen._
  当然，我会帮您。

Снача́ла нужно посмотре́ть, каки́е те́сты упа́ли.
  _Zuerst muss man schauen, welche Tests fehlgeschlagen sind._
  首先需要查看哪些测试失败了。

Запусти́те `npm test -- --verbose`, что́бы уви́деть подро́бный вы́вод.
  _Führen Sie `npm test -- --verbose` aus, um die ausführliche Ausgabe zu sehen._
  运行 `npm test -- --verbose` 以查看详细输出。

По́сле э́того мы смо́жем реши́ть, го́тов ли код к ме́рджу.
  _Danach können wir entscheiden, ob der Code bereit für den Merge ist._
  之后我们可以决定代码是否准备好合并。

Е́сли упа́ли то́лько unit-те́сты, а integration-те́сты прошли́, то мо́жно сде́лать ме́рдж с фла́гом `--no-ff`.
  _Falls nur Unit-Tests fehlgeschlagen sind, aber die Integration-Tests bestanden haben, kann man den Merge mit dem Flag `--no-ff` durchführen._
  如果只有单元测试失败，但集成测试通过了，可以使用 `--no-ff` 标志进行合并。

---
**Корректура / Korrekturen:**
- **DE** `ich bin nicht sicher ob` → `ich bin nicht sicher, ob` — Komma vor *ob* (Nebensatz).
- **DE** `kannst du mir helfen?` → `Kannst du mir helfen?` — Frage groß beginnen.
- **RU** `Я уже запусти́л тесты` → `Я уже запусти́л те́сты` — стресс на *те́сты* (тесты́ — это genitive singular, но здесь accusative plural: *те́сты*).
- **RU** `не все прошли́` — без оши́бок, вид глаго́ла пра́вильный (соверше́нный вид *пройти́* для за́вершенного де́йствия).

## Pedagogy integration

After this reply, the agent automatically:

1. **Writes a session file:**

```yaml
# pedagogy/_learn/writing-accuracy/sessions/2026-11-04-feature-merge-komma.toon.md
schema: writing-accuracy/session
date: 2026-11-04
primaryLang: de
targetLang: de
mixedWith: [ru]

corrections:
  - original: "ich bin nicht sicher ob"
    rewrite: "ich bin nicht sicher, ob"
    errorType: nebensatz-komma
    frame: "subordinate_clause_comma"
    explanation: "Komma vor 'ob' (Nebensatz)"
    
  - original: "kannst du mir helfen?"
    rewrite: "Kannst du mir helfen?"
    errorType: kapitalisierung
    frame: "sentence_initial_capital"
    explanation: "Frage groß beginnen"

  - original: "запусти́л тесты"
    rewrite: "запусти́л те́сты"
    targetLang: ru
    errorType: ударение
    frame: "stress_mark_noun_plural"
    explanation: "стресс на те́сты (accusative plural), не тесты́"
```

2. **Runs the ingestion script:**

```bash
python pedagogy/_learn/writing-accuracy/ingest_session.py \
    --session pedagogy/_learn/writing-accuracy/sessions/2026-11-04-feature-merge-komma.toon.md
```

3. **Updates knowledge graphs:**

   - `pedagogy/_learn/writing-accuracy/lexicon.graph.md`: adds `sicher` → `subordinate_clause_comma` frame
   - `pedagogy/_learn/polyglot/bridge.graph.md`: adds DE→RU gap `nicht sicher` ↔ `не уве́рен`
   - Potentially creates drill items in `pedagogy/_learn/writing-accuracy/drills.toon.md`

## Privacy note

If the user had written:

```
Ich möchte das feature für Kunde mueller@example.com mergen.
```

The agent would redact:

```
Я хочу́ сме́рджить фи́чу для клие́нта <email>.
  _Ich möchte das Feature für den Kunden <email> mergen._
  我想为客户 <email> 合并功能。

Адре́с эле́ктрoнной по́чты был отредакти́рован.
  _Die E-Mail-Adresse wurde redigiert._
  电子邮件地址已被编辑。
```

## Slash command exception

If the user writes:

```
/english explain the trilingual format
```

The agent answers in English without the Russian-first format:

```
The trilingual format is a standing rule for this project. Every answer is written in Russian, sentence by sentence, followed by German (italic) and Simplified Chinese translations. This helps with Russian pronunciation practice (via stress marks), German B2+ maintenance (via corrections), and sharing answers with a Chinese-speaking partner.

Slash commands like `/english`, `/deutsch`, or `/explain` are exempt from this format.
```

## Notes

- The agent **always** writes in Russian first, unless the user explicitly uses a slash command.
- The correction block covers **both** German and Russian, even if the user only writes in one language.
- If the user writes only in Chinese, the correction block shows `ohne Fehler / без ошибок` for both DE and RU.
- Stress marks are mandatory for all Russian words with 2+ syllables, except `ё` words and quoted user text.
- Code, commands, paths, and identifiers are never translated.
- The Chinese line is natural Simplified Chinese, not a literal translation.
