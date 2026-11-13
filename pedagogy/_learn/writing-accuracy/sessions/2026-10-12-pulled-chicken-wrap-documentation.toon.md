schema: writing-accuracy/session
version: 1.0

# Session: Pulled-Chicken-Wrap Dokumentation (2026-10-12 Mittag)

## Context
Der Benutzer dokumentiert sein Mittagessen: ein großer Pulled-Chicken-Wrap mit bunten Paprika, Sauerkraut und Zwiebeln in Alufolie.

## Original Text
"Heute habe ich ein pulled chicken wraps gegessen"

## Corrected Text
"Heute habe ich einen Pulled-Chicken-Wrap gegessen."

## Analysis

### Primary Error Focus
**NOUN_ARTICLE_CASE_AGREEMENT** + **COMPOUND_NOUN_HYPHENATION**

### Detailed Breakdown

#### Error 1: Article-Noun Number and Case Agreement
- **Type:** NOUN_ARTICLE_CASE_AGREEMENT
- **Original:** "ein pulled chicken wraps"
- **Corrected:** "einen Pulled-Chicken-Wrap"
- **Multiple Issues:**
  1. **Case:** "ein" (Nominativ) → "einen" (Akkusativ nach "gegessen")
  2. **Number:** "ein" (Singular) + "wraps" (Plural) → beide müssen Singular sein
  3. **Gender:** "der Wrap" ist maskulin → Akkusativ = "den Wrap"

**Detailed Explanation:**

1. **Akkusativ nach "haben + Partizip":**
   - "Ich habe [WAS?] gegessen" → Akkusativ-Objekt
   - "der Wrap" → Akkusativ = "den Wrap"
   - Mit unbestimmtem Artikel: "einen Wrap"

2. **Singular/Plural Kongruenz:**
   - "ein" / "eine" / "ein" = Singular-Artikel
   - → Nomen muss auch Singular sein
   - "wraps" (Plural) passt NICHT zu "ein"
   - Entweder: "ein Wrap" (Singular) ODER "Wraps" (Plural ohne Artikel)

**Correct Forms:**
- Singular: "einen Wrap" (einen = Akkusativ maskulin)
- Plural: "Wraps" (ohne Artikel) oder "mehrere Wraps"

#### Error 2: English Compound Noun in German
- **Type:** COMPOUND_NOUN_HYPHENATION (ANGLICISM_INTEGRATION)
- **Original:** "pulled chicken wraps"
- **Corrected:** "Pulled-Chicken-Wrap"
- **Explanation:** Englische Mehrwort-Begriffe in deutschen Sätzen werden mit Bindestrichen verbunden und das erste Wort wird großgeschrieben (Nomen-Regel).
  
**Rules for English Compounds in German:**
1. Bindestriche zwischen allen Wörtern: "Pulled-Chicken-Wrap"
2. Erstes Wort groß (Nomen in Deutsch): "Pulled" nicht "pulled"
3. Letztes Wort bestimmt Genus: "der Wrap" → maskulin
4. Deutsche Deklination: "des Wraps", "dem Wrap", "den Wrap"

**More Examples:**
- "Fast Food" → "Fast-Food-Restaurant"
- "New York" → "New-York-Pizza"
- "Hot Dog" → "Hot-Dog-Stand"

### Grammar Frame Focus
**GrammarFrame: AKKUSATIV_NACH_HABEN_GEGESSEN**

Nach "haben + gegessen/getrunken/gekauft/..." steht das Objekt im **Akkusativ**:

| Nominativ (wer/was?) | Akkusativ (wen/was?) | Beispiel |
|---------------------|---------------------|----------|
| der Wrap | den Wrap | Ich habe **den** Wrap gegessen |
| ein Wrap | einen Wrap | Ich habe **einen** Wrap gegessen |
| die Pizza | die Pizza | Ich habe **die** Pizza gegessen |
| das Brötchen | das Brötchen | Ich habe **das** Brötchen gegessen |

**Merksatz:** "Wen oder was habe ich gegessen?" → Akkusativ!

### Vocabulary Additions
- **Pulled Chicken** (das, nur Singular) = gezupftes/gezogenes Hähnchenfleisch (slow-cooked and shredded chicken)
- **der Wrap** (Plural: die Wraps) = filled tortilla roll
- **die Tortilla** (Plural: die Tortillas) = flat wheat/corn bread (Mexican)
- **das Sauerkraut** (nur Singular) = fermented cabbage
- **bunt** (Adjektiv) = colorful, multicolored

### Additional Patterns
- "Ich habe einen Burger gegessen" ✓
- "Ich habe ein Burger gegessen" ✗
- "Ich habe Burger gegessen" ✓ (Plural ohne Artikel)

## Session Metadata
- Date: 2026-10-12
- Time: Mittag (~12:35 Uhr)
- Task: Ernährungsdokumentation (nutrition logging)
- Context: Mittagessen to-go, Pulled-Chicken-Wrap
- Input Mode: Speech-to-text (wahrscheinlich)
