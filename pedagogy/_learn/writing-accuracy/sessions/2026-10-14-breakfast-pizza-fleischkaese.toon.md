schema: writing-accuracy/session
version: 1.0

# Session: Frühstück mit Pizza-Fleischkäse (2026-10-14 Morgen)

## Context
Der Benutzer dokumentiert sein Frühstück: Pizza-Fleischkäse (mit Paprika), Hähnchen, ein halbes Brötchen und Latte Macchiato.

## Original Text
"Heute Morgen habe ich ein halbes Pizza Fleisch Käse, ein halbes Brötchen gegessen und eine kleine Flasche Latte macchiato getrunken."

## Corrected Text
"Heute Morgen habe ich eine halbe Scheibe Pizza-Fleischkäse, ein halbes Brötchen und eine kleine Flasche Latte Macchiato gegessen/getrunken."

## Analysis

### Primary Error Focus
**NOUN_GENDER** + **COMPOUND_NOUN** + **CAPITALIZATION**

### Detailed Breakdown

#### Error 1: Noun Gender and Article Agreement
- **Type:** NOUN_GENDER
- **Original:** "ein halbes Pizza Fleisch Käse"
- **Corrected:** "eine halbe Scheibe Pizza-Fleischkäse"
- **Explanation:** Mehrere Probleme:
  1. "ein halbes" (neutral) passt nicht zu "Scheibe" (feminin)
  2. "die Scheibe" → "eine halbe Scheibe" (feminin)
  3. Oder: "ein halbes Stück" (neutral) wäre auch korrekt

**Gender Agreement:**
- die Scheibe → eine halbe Scheibe (feminin)
- das Stück → ein halbes Stück (neutral)
- der Teil → ein halber Teil (maskulin)

**Rule:** Adjektiv "halb-" muss sich an Genus anpassen:
- halbe (feminin): "eine halbe Scheibe"
- halbes (neutral): "ein halbes Stück"
- halber (maskulin): "ein halber Apfel"

#### Error 2: Compound Noun Formation
- **Type:** COMPOUND_NOUN
- **Original:** "Pizza Fleisch Käse"
- **Corrected:** "Pizza-Fleischkäse"
- **Explanation:** Deutsche Komposita werden entweder zusammengeschrieben oder mit Bindestrichen verbunden. Bei mehreren Wörtern sind Bindestriche üblich.

**Correct Forms:**
- Fleischkäse (einfaches Kompositum)
- **Pizza-Fleischkäse** (mit Bindestrich bei drei+ Teilen)
- Paprika-Fleischkäse
- Leberkäse

**Why hyphens:**
- Macht lange Komposita lesbarer
- Bei Produktnamen/Sorten üblich
- "Pizza-Fleischkäse" = Fleischkäse mit Pizza-Geschmack/Zutaten

#### Error 3: Capitalization of Foreign Terms
- **Type:** CAPITALIZATION
- **Original:** "Latte macchiato"
- **Corrected:** "Latte Macchiato"
- **Explanation:** Im Deutschen werden alle Substantive großgeschrieben, auch fremdsprachige. Bei mehrteiligen Namen: beide Teile groß.

**Examples:**
- Latte Macchiato (not: Latte macchiato)
- Cappuccino (single word, capitalize first letter)
- Café au Lait
- Croissant

**Exceptions:**
- If written in italics as foreign phrase: *latte macchiato* (kann klein sein)
- But in German text as noun: Latte Macchiato

#### Error 4: Verb Repetition
- **Type:** SENTENCE_STRUCTURE (minor optimization)
- **Original:** "gegessen und ... getrunken"
- **Better:** "gegessen/getrunken" or "zu mir genommen"
- **Explanation:** Optional: Man kann beide Verben verwenden, oder kombinieren:
  - "Ich habe ... gegessen und ... getrunken." ✓ (korrekt, etwas lang)
  - "Ich habe ... gegessen/getrunken." ✓ (kürzer)
  - "Ich habe ... zu mir genommen." ✓ (formaler)

### Grammar Frame Focus
**GrammarFrame: ADJECTIVE_ENDING_GENDER_AGREEMENT**

Adjektiv-Endungen nach unbestimmtem Artikel:

| Genus | Nominativ | Akkusativ |
|-------|-----------|-----------|
| Maskulin | ein **halber** Apfel | einen **halben** Apfel |
| Feminin | eine **halbe** Scheibe | eine **halbe** Scheibe |
| Neutral | ein **halbes** Brötchen | ein **halbes** Brötchen |

**Pattern:** Im Akkusativ feminin/neutral ändert sich die Endung nicht!

### Vocabulary Additions
- **der Fleischkäse** (auch: der Leberkäse) = meat loaf (Bavarian specialty)
- **die Scheibe** (Plural: die Scheiben) = slice
- **der Pizza-Fleischkäse** = pizza-flavored meat loaf (with paprika/vegetables)
- **der Paprika-Fleischkäse** = bell pepper meat loaf
- **der Latte Macchiato** = latte macchiato (espresso with steamed milk)

### Additional Notes
- Context: Typical German/Bavarian breakfast
- Fleischkäse (Leberkäse) is a specialty from Bavaria/Austria
- Pizza-Fleischkäse = variant with paprika pieces (visible in image)
- User also ate chicken (not mentioned in original text, but visible)

## Session Metadata
- Date: 2026-10-14
- Time: Morgen (~08:15 Uhr)
- Task: Ernährungsdokumentation (nutrition logging)
- Context: Hearty German breakfast after body composition measurement
- Input Mode: Text with image attachment
