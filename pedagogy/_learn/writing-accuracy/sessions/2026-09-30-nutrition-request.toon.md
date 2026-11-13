schema: writing-accuracy/session
date: 2026-09-30
primaryLang: de
context: nutrition-meal-documentation

## Raw

From der Frühstück von mir heute. Morgen. Bitte Dokumentieren Sie für mich. Und äh Analyse. Jeden Tag für mich meine Kalorien zu verbrennen.

## Minimal rewrite

Mein Frühstück von heute Vormittag. Bitte dokumentieren Sie es für mich und analysieren Sie meinen täglichen Kalorienverbrauch.

## Errors

### E1: Präposition + Kasus [PREP_CASE]
- Raw: `From der Frühstück`
- Fix: `Mein Frühstück` oder `Von meinem Frühstück`
- Frame: Präposition `von` + Dativ: `von meinem Frühstück (n, Dat.Sg.)`
- Note: "From" ist Englisch; nach `von` steht Dativ, nicht Nominativ

### E2: Wortart [PART_OF_SPEECH]
- Raw: `Analyse`
- Fix: `analysieren`
- Frame: Verb benötigt, nicht Nomen: `Bitte analysieren Sie`
- Note: Nach "und" parallel zu "dokumentieren Sie" braucht man Verb-Infinitiv oder konjugierte Form

### E3: Infinitivkonstruktion [INF_CONSTRUCTION]
- Raw: `Jeden Tag für mich meine Kalorien zu verbrennen`
- Fix: `meinen täglichen Kalorienverbrauch zu analysieren`
- Frame: `zu + Infinitiv`: Akkusativobjekt vor `zu` - `[Akk] zu [Verb]`
- Note: "Kalorien verbrennen" = physiologisch; gemeint war "Kalorienverbrauch analysieren/berechnen"

## GrammarFrame focus

**Präpositionen + Kasus (Prepositions + Case)**

| Präposition | Kasus | Beispiel |
|-------------|-------|----------|
| von | Dativ | von meinem Frühstück, von der Arbeit, von dem Trainer |
| mit | Dativ | mit meinem Freund, mit der Gabel |
| aus | Dativ | aus meinem Zimmer, aus der Stadt |
| zu | Dativ | zu meinem Arzt, zum Training, zur Arbeit |
| nach | Dativ | nach dem Essen, nach der Arbeit |
| bei | Dativ | bei meinem Bruder, beim Sport |
| seit | Dativ | seit einem Jahr, seit dem Training |

### Merksatz
**Von, mit, nach, aus, zu, bei, seit — verlangen stets den Fall Nummer drei** (Dativ)

## Context
User requested meal documentation and calorie-burn analysis. Wanted morning/breakfast meal logged with images provided.
