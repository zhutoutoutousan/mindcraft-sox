# Integration with pedagogy/_learn/ system for Russian

The `de-ru-tutor` workspace rule automatically integrates with the existing `pedagogy/_learn/` language learning system. This document explains how Russian corrections flow into the knowledge graphs.

## Architecture

```
User input (DE + RU mixed)
    ↓
Agent correction block (DE + RU)
    ↓
Session file (pedagogy/_learn/writing-accuracy/sessions/<date>-<slug>.toon.md)
    ↓
Ingestion script (ingest_session.py)
    ↓
Knowledge graphs updated:
  - pedagogy/_learn/writing-accuracy/lexicon.graph.md (German lemmas)
  - pedagogy/_learn/polyglot/bridge.graph.md (cross-language gaps)
  - pedagogy/_learn/polyglot/frames/ru.toon.md (Russian grammar frames)
```

## Supported languages

The system already supports Russian (`ru`) alongside German (`de`). Both languages share the same infrastructure:

- **German lexicon:** `pedagogy/_learn/writing-accuracy/lexicon.graph.md`
- **Russian frames:** `pedagogy/_learn/polyglot/frames/ru.toon.md`
- **Cross-language bridge:** `pedagogy/_learn/polyglot/bridge.graph.md`
- **16-language horizon:** `pedagogy/_learn/polyglot/horizon.toon.md`

## Session file format

After giving corrections, the agent writes a session file under:

```
pedagogy/_learn/writing-accuracy/sessions/<YYYY-MM-DD>-<slug>.toon.md
```

### Example: Mixed DE + RU session

```yaml
schema: writing-accuracy/session
date: 2026-11-04
id: 2026-11-04-merge-branch-case
primaryLang: de
targetLang: de
mixedWith: [ru]

corrections:
  - lang: de
    original: "ich bin nicht sicher ob"
    rewrite: "ich bin nicht sicher, ob"
    errorType: nebensatz-komma
    frame: "subordinate_clause_comma"
    explanation: "Komma vor 'ob' (Nebensatz)"
    
  - lang: de
    original: "kannst du mir helfen?"
    rewrite: "Kannst du mir helfen?"
    errorType: kapitalisierung
    frame: "sentence_initial_capital"
    explanation: "Frage groß beginnen"

  - lang: ru
    original: "запусти́л тесты"
    rewrite: "запусти́л те́сты"
    errorType: ударение
    frame: "stress_mark_noun_plural"
    explanation: "стресс на те́сты (accusative plural), не тесты́ (genitive singular)"
    
  - lang: ru
    original: "я имею другое мнение"
    rewrite: "у меня другое мнение"
    errorType: управление
    frame: "u_menja_N_nom"
    explanation: "по-русски: у меня + N (Nom), не 'я имею'"
```

## Ingestion workflow

1. **Agent detects corrections** in the user's input (both DE and RU)
2. **Agent writes session file** with structured corrections
3. **Agent runs ingestion:**
   ```bash
   python pedagogy/_learn/writing-accuracy/ingest_session.py \
       --session pedagogy/_learn/writing-accuracy/sessions/2026-11-04-merge-branch-case.toon.md
   ```
4. **Ingestion script updates graphs:**
   - Adds lemmas and forms to lexicon.graph.md (German)
   - Adds concept/gap vertices to bridge.graph.md (cross-language)
   - Links corrections to grammar frames (de.toon.md, ru.toon.md)
   - Potentially generates drill items in drills.toon.md

## Russian-specific error types

The system tracks these Russian error patterns:

| errorType | Description | Example |
|-----------|-------------|---------|
| `падеж` | Case error | `в театр` (Acc) not `в театре` (Prep) for direction |
| `вид` | Aspect error | `прочитал` (perf) not `читал` (imperf) for completed action |
| `управление` | Verbal government | `скучать по` + Dat, not `о` + Prep |
| `согласование` | Agreement (gender/number/case) | `этот книга` → `эта книга` (fem) |
| `порядок слов` | Word order | New information last |
| `ударение` | Stress mark error | `те́сты` (Nom/Acc pl) not `тесты́` (Gen sg) |
| `род` | Gender (loanwords) | `проект` is masculine, `система` is feminine |

## German-specific error types

The system tracks these German error patterns (unchanged from existing system):

| errorType | Description | Example |
|-----------|-------------|---------|
| `case_gender_article` | Article/gender/case | `mit der Mann` → `mit dem Mann` (Dat masc) |
| `prepositions` | Case after preposition | `durch dem Raum` → `durch den Raum` (Akk) |
| `word_order_particles` | V2 / verb-final | `Ich weiß nicht, ob es klappt` not `ob klappt es` |
| `morphology_endings` | Adjective endings | `ein groß Mann` → `ein großer Mann` |
| `lexis_collocation` | Collocation | `eine Entscheidung nehmen` → `eine Entscheidung treffen` |
| `orthography` | Spelling | `daß` → `dass` (current orthography) |
| `register_imperative` | Register | `Sag mal` vs `Sagen Sie bitte` |
| `sentence_chunking` | Comma rules | `Ich glaube, dass` not `Ich glaube dass` |

## Grammar frames

### Russian frames (pedagogy/_learn/polyglot/frames/ru.toon.md)

Already defined:
- `ja_schitaju_chto` — state an opinion: `Я считаю, что + clause`
- `mne_kazhetsja_chto` — state an impression: `Мне кажется, что + clause`
- `u_menja_N_nom` — have-an-opinion: `У меня + N (Nom)`
- `ja_poka_ne_ochen_ADV_V` — limited understanding: `Я пока не очень хорошо + V`
- `ne_mogli_by_vy_inf` — polite request: `Не могли бы вы + Inf, пожалуйста?`
- `ja_pytajus_inf` — attempt to speak: `Я пытаюсь + Inf`

**To add more frames:** append to `ru.toon.md` following the existing pattern. Each frame has:
- `id`: snake_case identifier
- `gloss`: English description
- `pattern`: Russian template with slots
- `slots`: list of slot names
- `fillers`: attested lemmas that fill the slots
- `anti`: common error pattern to avoid
- `concept`: semantic category

### German frames (pedagogy/_learn/polyglot/frames/de.toon.md)

Existing frames remain unchanged. The system handles both languages separately and links them via `bridge.graph.md`.

## Cross-language bridge

The `bridge.graph.md` records conceptual gaps between languages:

```cypher
# auto-gap 2026-11-04T10:30:00Z surface="я имею мнение"
V Concept_gap_have_opinion kind=concept gloss=unknown-expression-in-de status=open
V Gap_ru_ja_imeju_mnenie kind=gap lang=ru surface="я имею мнение" target=de status=open
V Lemma_ru_ja_imeju_mnenie kind=lemma lang=ru surface="я имею мнение"
E Concept_gap_have_opinion EXPRESSES Lemma_ru_ja_imeju_mnenie SOURCE=session
E Lemma_ru_ja_imeju_mnenie GAP_IN de SOURCE=session
E Concept_gap_have_opinion GAP_IN de SOURCE=session

# Resolved form (after correction)
V Form_ru_u_menja_mnenie kind=form lang=ru surface="у меня мнение" frame=u_menja_N_nom
E Concept_gap_have_opinion RESOLVED_BY Form_ru_u_menja_mnenie
```

## Drill generation

After several sessions, the system may generate drill items in `drills.toon.md`:

```yaml
item:
  point: "Russian: У меня + N (Nom) for possession/opinion"
  stem: "___ другое мнение о этом проекте."
  blank: "У меня"
  distractors: ["Я имею", "Мне есть", "Я владею"]
  lang: ru
  frame: u_menja_N_nom
  source: pedagogy/_learn/writing-accuracy/sessions/2026-11-04-merge-branch-case.toon.md
```

Render drills with:

```bash
python pedagogy/_learn/writing-accuracy/render_drills.py --serve
```

This creates an HTML drill interface with localStorage progress tracking.

## Privacy safeguards

The ingestion script **never logs**:
- Real names, addresses, e-mails, phone numbers
- IP addresses, tokens, passwords
- Card numbers, health data, IDs

If such data appears in a session file (accidentally), **immediately**:
1. Delete the session file: `rm pedagogy/_learn/writing-accuracy/sessions/<file>.toon.md`
2. Check if already ingested: `grep "<leaked-data>" pedagogy/_learn/writing-accuracy/lexicon.graph.md pedagogy/_learn/polyglot/bridge.graph.md`
3. Remove any matching vertices/edges manually
4. Never commit PII to git

## Testing the integration

### 1. Write a test session file

```bash
cat > pedagogy/_learn/writing-accuracy/sessions/2026-11-04-test-ru.toon.md <<'EOF'
schema: writing-accuracy/session
date: 2026-11-04
id: test-ru-integration
primaryLang: ru
targetLang: ru
mixedWith: []

corrections:
  - lang: ru
    original: "я имею вопрос"
    rewrite: "у меня вопрос"
    errorType: управление
    frame: "u_menja_N_nom"
    explanation: "по-русски: у меня + N (Nom), не 'я имею'"
EOF
```

### 2. Run ingestion

```bash
python pedagogy/_learn/writing-accuracy/ingest_session.py \
    --session pedagogy/_learn/writing-accuracy/sessions/2026-11-04-test-ru.toon.md
```

### 3. Verify graph updates

```bash
# Check bridge.graph.md for new Russian vertices
grep "lang=ru" pedagogy/_learn/polyglot/bridge.graph.md | tail -20

# Check session was recorded
grep "Session_test_ru_integration" pedagogy/_learn/writing-accuracy/lexicon.graph.md
```

### 4. Clean up test

```bash
# Do not commit test sessions
git restore pedagogy/_learn/writing-accuracy/sessions/2026-11-04-test-ru.toon.md
# Or delete it
rm pedagogy/_learn/writing-accuracy/sessions/2026-11-04-test-ru.toon.md
```

## Agent automation

The workspace rule `.cursor/rules/de-ru-tutor.mdc` instructs agents to:

1. **Complete the job first.** Language corrections are secondary.
2. **Read `last-signal.toon.md`** to check if gaps are already recorded.
3. **Write session file** after giving corrections (both DE and RU).
4. **Run ingestion script** automatically (do not wait to be asked).
5. **Never edit product code** for language logging.

The agent follows this loop on every turn where corrections are given.

## References

- Method contract: `pedagogy/_learn/writing-accuracy/method.toon.md`
- State and focus: `pedagogy/_learn/writing-accuracy/state.toon.md`
- Pairing (Frame × lexicon): `pedagogy/_learn/polyglot/pairing.toon.md`
- 16-language horizon: `pedagogy/_learn/polyglot/horizon.toon.md`
- German frames: `pedagogy/_learn/polyglot/frames/de.toon.md`
- Russian frames: `pedagogy/_learn/polyglot/frames/ru.toon.md`
- Lexicon graph: `pedagogy/_learn/writing-accuracy/lexicon.graph.md`
- Bridge graph: `pedagogy/_learn/polyglot/bridge.graph.md`
- Ingestion script: `.cursor/hooks/polyglot_ingest.py`
- Full specification: `.cursor/skills/de-ru-tutor/SKILL.md`

## Notes

- Russian is already listed in `horizon.toon.md` as `limited_working` proficiency.
- The system supports all 16 languages in the horizon; German and Russian are just the most active.
- Stress marks (U+0301) are stored verbatim in session files and graphs.
- The ingestion script is language-agnostic: it uses the `lang` field to route corrections to the appropriate frame file.
- Cross-language gaps (e.g., "How do I express X in RU when I only know the DE form?") land in `bridge.graph.md`.
