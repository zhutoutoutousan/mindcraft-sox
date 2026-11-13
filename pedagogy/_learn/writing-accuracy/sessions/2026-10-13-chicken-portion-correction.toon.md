schema: writing-accuracy/session
version: 1.0

# Session: Hähnchen-Portion Korrektur (2026-10-13 Nachmittag)

## Context
Der Benutzer korrigiert die Annahme des Assistenten über die Portionsgröße: Er hat nicht die ganze Hähnchenstelze gegessen, sondern nur ein kleines Stück vom Hähnchenschenkel.

## Original Text
"Aber nicht ein ganzes Hähnchen-Stelze, sondern nur ein kleines Stück Hähnchen schenke gegessen."

## Corrected Text
"Aber ich habe nicht die ganze Hähnchenstelze gegessen, sondern nur ein kleines Stück vom Hähnchenschenkel."

## Analysis

### Primary Error Focus
**NOUN_ARTICLE_GENDER_AGREEMENT** + **SPELLING_ERROR** + **SENTENCE_STRUCTURE**

### Detailed Breakdown

#### Error 1: Article Gender Agreement
- **Type:** NOUN_ARTICLE_GENDER_AGREEMENT
- **Original:** "ein ganzes Hähnchen-Stelze"
- **Corrected:** "eine ganze Hähnchenstelze"
- **Explanation:** "die Stelze" ist **feminin**, nicht neutral/maskulin.

**Gender Rule:**
- die Stelze → eine Stelze (feminin)
- der Schenkel → ein Schenkel (maskulin)
- das Hähnchen → ein Hähnchen (neutral)

**Common Mistake:**
- User verwechselt "das Hähnchen" (neutral) mit "die Stelze" (feminin)
- Bei Komposita bestimmt das **letzte Wort** das Genus:
  - "Hähnchen + Stelze" → "die Hähnchenstelze" (feminin, weil "Stelze")

#### Error 2: Spelling Error (Typo)
- **Type:** SPELLING_ERROR
- **Original:** "Hähnchen schenke"
- **Corrected:** "Hähnchenschenkel"
- **Explanation:** "schenke" ist falsch geschrieben. Das richtige Wort ist "der Schenkel" (thigh/leg).

**Correct Forms:**
- der Schenkel (Singular) = leg/thigh
- die Schenkel (Plural) = legs/thighs
- der Hähnchenschenkel = chicken leg/thigh

**Possible Source:**
- Speech-to-text error
- Or confusion with "schenken" (to give as a gift) → "schenke" (I give)

#### Error 3: Sentence Structure Optimization
- **Type:** SENTENCE_STRUCTURE
- **Original:** "nur ein kleines Stück Hähnchen schenke gegessen"
- **Corrected:** "nur ein kleines Stück vom Hähnchenschenkel gegessen"
- **Explanation:** "vom Hähnchenschenkel" ist klarer als "Hähnchen schenke" und zeigt die Herkunft (Teil vom Ganzen).

**Better Phrasing:**
- "ein Stück **vom** Hähnchenschenkel" (a piece from the chicken leg)
- "ein Stück **Hähnchenfleisch**" (a piece of chicken meat)
- "etwas **vom** Hähnchen" (some from the chicken)

**Complete Sentence Improvement:**
- Original (holprig): "Aber nicht ein ganzes Hähnchen-Stelze, sondern nur ein kleines Stück Hähnchen schenke gegessen."
- Better: "Aber ich habe nicht die ganze Hähnchenstelze gegessen, sondern nur ein kleines Stück vom Hähnchenschenkel."
- Alternative: "Aber nicht die ganze Stelze, sondern nur ein kleines Stück Hähnchen."

### Grammar Frame Focus
**GrammarFrame: COMPOUND_NOUN_GENDER**

Bei zusammengesetzten Nomen (Komposita) bestimmt das **letzte Wort** das Genus:

| Kompositum | Letztes Wort | Genus | Artikel |
|------------|--------------|-------|---------|
| Hähnchen + Stelze | **die** Stelze | feminin | **eine** Hähnchenstelze |
| Hähnchen + Schenkel | **der** Schenkel | maskulin | **ein** Hähnchenschenkel |
| Hähnchen + Brust | **die** Brust | feminin | **eine** Hähnchenbrust |
| Hähnchen + Flügel | **der** Flügel | maskulin | **ein** Hähnchenflügel |

**Merksatz:** Das Genus kommt vom Ende, nicht vom Anfang!

### Vocabulary Additions
- **die Stelze** (Plural: die Stelzen) = leg (especially lower leg/shank, Bavarian/Austrian for Schweinshaxe or Hähnchenstelze)
- **der Schenkel** (Plural: die Schenkel) = thigh/leg (upper part)
- **die Hähnchenstelze** = chicken leg/drumstick (whole lower leg)
- **der Hähnchenschenkel** = chicken thigh/leg
- **das Stück** (Plural: die Stücke) = piece, portion
- **vom** = von + dem = from the (Dativ)

### Additional Notes
- "Stelze" wird hauptsächlich in Bayern/Österreich verwendet
- In Norddeutschland: "Hähnchenschenkel" oder "Hähnchenkeule"
- Portionsgröße: "ein kleines Stück" ≈ 80-100g (vs. ganze Stelze ≈ 400-450g)

## Session Metadata
- Date: 2026-10-13
- Time: Nachmittag (~14:29 Uhr)
- Task: Korrektur/Klarstellung der Portionsgröße
- Context: User korrigiert Überinterpretation (ganze Stelze → nur kleines Stück)
- Input Mode: Text oder Speech-to-text (wahrscheinlich Speech wegen "schenke" Typo)
