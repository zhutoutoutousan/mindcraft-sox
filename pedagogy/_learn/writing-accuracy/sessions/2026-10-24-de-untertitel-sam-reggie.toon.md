schema: writing-accuracy/session
version: 1.0

# Session: DE-Untertitel Sam / Reggie / Gabe (2026-10-24)

## Context
Benutzer prüft deutsche Untertitelzeilen (Voicemail + Dialog: Reggie, Gabe, Verrat, Nubische Schwester).

## Original Text
"Hier ist Sam. Hinterlasse eine Nachricht.

Reggie, mein Kriegskamerad. Es war Gabe, der uns an die Bullen Schweine verraten hat.

Ich wusste es, meine Nubische Schwester. Ich habe diesen weißen Teufel sowieso nie vertraut."

## Corrected Text
"Hier ist Sam. Hinterlasse eine Nachricht.

Reggie, mein Kriegskamerad. Es war Gabe, der uns an die Bullenschweine verraten hat.

Ich wusste es, meine nubische Schwester. Ich habe diesem weißen Teufel sowieso nie vertraut."

## Analysis

### Primary Error Focus
**CASE** (vertrauen + Dativ) + **ORTHOGRAPHY** (Adjektiv klein, Kompositum)

### Detailed Breakdown

#### Error 1: vertrauen + Dativ
- **Type:** case_gender_article
- **Original:** "diesen weißen Teufel … vertraut"
- **Corrected:** "diesem weißen Teufel … vertraut"
- **Explanation:** *vertrauen* regiert den Dativ, nicht den Akkusativ.

**Pattern:**
- jdm. vertrauen = jemandem (Dativ) vertrauen
- Ich vertraue **ihm**. / Ich habe **ihm** nie vertraut.
- ❌ diesen Teufel vertraut → ✓ **diesem** Teufel vertraut

#### Error 2: Adjektiv-Kleinschreibung
- **Type:** orthography
- **Original:** "meine Nubische Schwester"
- **Corrected:** "meine nubische Schwester"
- **Explanation:** Adjektive (auch Herkunft/Ethnie) werden klein geschrieben; nur das Nomen *Schwester* groß.

#### Error 3: Kompositum statt zwei Wörter
- **Type:** orthography / lexis_collocation
- **Original:** "die Bullen Schweine"
- **Corrected:** "die Bullenschweine"
- **Explanation:** Beleidigendes Kompositum zusammenschreiben (oder mit Bindestrich: Bullen-Schweine). Getrennt wirkt wie zwei Nomen ohne Verbindung.

### GrammarFrame focus
**GrammarFrame: VERTRAUEN_DATIV**

Slot: `vertrauen` + Pronomen/NP im **Dativ**.

| Form | Beispiel |
|------|----------|
| Dativ mask. | diesem weißen Teufel |
| Dativ fem. | dieser Schwester |
| Dativ neutr. | diesem Team |
| Pronomen | ihm / ihr / ihnen |

Wiederverwendung nächste Session: einen Satz mit *vertrauen* + Dativ-Demonstrativ (*diesem/dieser/diesem*).

### Vocabulary
- der Kriegskamerad = war buddy / comrade-in-arms
- verraten an + Akk. = sell out / betray to
- das Bullenschwein (ugs., pej.) = cop (insult)
- der weiße Teufel = white devil (register: film/slang)

## Session Metadata
- Date: 2026-10-24
- Task: Untertitel-Korrektur (DE)
- Input Mode: Text paste
- oneFocus: VERTRAUEN_DATIV
