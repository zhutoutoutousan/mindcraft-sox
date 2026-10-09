schema: writing-accuracy/session
date: 2026-10-09
primaryLang: de
context: health-data-documentation

## Raw

Das ist die Daten für mich heute Morgen bevor Frühstück

## Minimal rewrite

Das sind die Daten von heute Morgen vor dem Frühstück.

## Errors

### E1: Verb-Subjekt-Kongruenz [AGREEMENT_VERB_SUBJECT]
- Raw: `Das ist die Daten`
- Fix: `Das sind die Daten`
- Frame: Plural-Subjekt "die Daten" erfordert Plural-Verb "sind" (nicht Singular "ist")
- Note: "Daten" ist immer Plural (Datum → Daten)

### E2: Präposition mit Dativ [PREPOSITION_CASE]
- Raw: `von ... bevor Frühstück`
- Fix: `von ... vor dem Frühstück`
- Frame: Temporale Präposition "vor" + Dativ-Artikel "dem" (nicht ohne Artikel)
- Note: "bevor" ist Konjunktion (vor Nebensatz mit Verb); "vor" ist Präposition (vor Nomen)

### E3: Possessivpronomen vs. Präposition (optional) [REDUNDANCY]
- Raw: `die Daten für mich`
- Alternative: `meine Daten` (stilistisch natürlicher, aber nicht falsch)
- Note: "für mich" ist hier akzeptabel im Kontext "diese Daten gehören mir"; nicht so redundant wie "mein Frühstück für mich"

## GrammarFrame focus

**Temporale Präpositionen vs. Konjunktionen**

| Präposition + Nomen | Konjunktion + Nebensatz | Bedeutung |
|---------------------|-------------------------|-----------|
| vor dem Frühstück | bevor ich frühstücke | temporal: früher als |
| vor der Arbeit | bevor ich arbeite | Zeitpunkt davor |
| vor dem Schlafen | bevor ich schlafe | vorher |

**vor + Dativ:**
- vor **dem** Frühstück
- vor **der** Schule
- vor **den** Ferien

**bevor + Verb (Konjunktion):**
- bevor ich **frühstücke**
- bevor du **gehst**
- bevor wir **anfangen**

### Merksatz
**"vor" + Artikel + Nomen; "bevor" + Subjekt + Verb**

## Context
User documented morning health metrics (weight 66.05 kg, BMI 23.4, body fat 32.9%) taken before breakfast on October 9, 2026. Subject-verb agreement error with plural noun "Daten" and missing article with temporal preposition.
