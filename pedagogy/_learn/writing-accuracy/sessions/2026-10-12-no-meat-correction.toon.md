schema: writing-accuracy/session
version: 1.0

# Session: Fleisch-Korrektur - Vegetarisches Abendessen (2026-10-12 Abend)

## Context
Der Benutzer korrigiert die Annahme des Assistenten, dass Fleisch im Abendessen war. Er klärt auf, dass es eine vegetarische Bowl ohne Fleisch war.

## Original Text
"Es gibt keine Fleisch darin."

## Corrected Text
"Es gibt kein Fleisch darin."

## Analysis

### Primary Error Focus
**NOUN_ARTICLE_GENDER_AGREEMENT** (NEGATION_ARTICLE_GENDER)

### Detailed Breakdown

#### Error: Negation Article Gender Mismatch
- **Type:** NOUN_ARTICLE_GENDER_AGREEMENT
- **Original:** "keine Fleisch"
- **Corrected:** "kein Fleisch"
- **Explanation:** Das Wort "Fleisch" ist **neutral** ("das Fleisch"), nicht feminin. Die Verneinung muss sich dem Genus anpassen.

**Gender-based negation articles:**

| Genus | Artikel | Negation | Beispiel |
|-------|---------|----------|----------|
| Maskulin | der | kein | der Fisch → **kein** Fisch |
| Feminin | die | keine | die Wurst → **keine** Wurst |
| Neutral | das | kein | **das Fleisch** → **kein Fleisch** ✓ |
| Plural | die | keine | die Eier → **keine** Eier |

**Pattern Rule:**
- Maskulin/Neutral → "kein" (ohne -e)
- Feminin/Plural → "keine" (mit -e)

**Common mistakes with "das Fleisch":**
- ✗ "keine Fleisch" (feminin behandelt)
- ✓ "kein Fleisch" (neutral korrekt)

#### Why this error happens:
1. "Fleisch" endet auf Konsonant → klingt maskulin/neutral (nicht wie typische Feminine auf -e, -heit, -keit)
2. Aber: "das Fleisch" ist neutral
3. User verwechselt mit femininen Lebensmitteln: "keine Wurst", "keine Butter", "keine Milch"

### Grammar Frame Focus
**GrammarFrame: NEGATION_ARTICLE_GENDER**

Verneinungsartikel "kein/keine" richtet sich nach dem **Genus** des Nomens:

**Neutral Nouns (das → kein):**
- das Fleisch → kein Fleisch
- das Brot → kein Brot
- das Gemüse → kein Gemüse
- das Ei → kein Ei

**Masculine Nouns (der → kein):**
- der Käse → kein Käse
- der Fisch → kein Fisch
- der Reis → kein Reis

**Feminine Nouns (die → keine):**
- die Wurst → keine Wurst
- die Pizza → keine Pizza
- die Milch → keine Milch

**Plural (die → keine):**
- die Äpfel → keine Äpfel
- die Eier → keine Eier

### Vocabulary Notes
- **das Fleisch** (neutral, nur Singular) = meat
- **vegetarisch** (Adjektiv) = vegetarian (food)
- **der Vegetarier / die Vegetarierin** = vegetarian (person)
- **vegan** (Adjektiv) = vegan

### Additional Context
- Sentence context: "Es gibt kein Fleisch darin" = There is no meat in it
- "darin" = darin = in it (in the bowl/dish)
- "Es gibt..." = There is/are... (fixed expression)

## Session Metadata
- Date: 2026-10-12
- Time: Abend (~18:06 Uhr)
- Task: Korrektur/Klarstellung der Mahlzeitbeschreibung
- Context: User korrigiert falsche Annahme (Hühnerfleisch → tatsächlich vegetarisch)
- Input Mode: Text oder Speech-to-text
