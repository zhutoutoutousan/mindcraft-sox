schema: writing-accuracy/session
version: 1.0

# Session: Mittagessen HIGH PROTEIN Lachs-Bandnudeln (2026-10-15 Mittag)

## Context
Der Benutzer dokumentiert sein Mittagessen: REWE HIGH PROTEIN Fertiggericht mit Bandnudeln, Lachs und Gemüse in Kräuter-Sahne-Sauce, plus zusätzliches gebratenes Gemüse.

## Original Text
"Am Mittag habe ich diese Nudel und halb Portion von Gemüse gegessen."

## Corrected Text
"Zum Mittagessen habe ich diese Nudeln und eine halbe Portion Gemüse gegessen."

**Alternative:**
"Mittags habe ich diese Nudeln und eine halbe Portion Gemüse gegessen."

## Analysis

### Primary Error Focus
**NUMBER** + **ARTICLE_ADJECTIVE** + **PREPOSITION**

### Detailed Breakdown

#### Error 1: Singular vs. Plural
- **Type:** NUMBER
- **Original:** "diese Nudel"
- **Corrected:** "diese Nudeln"
- **Explanation:** Nudeln werden fast immer im Plural verwendet!

**Singular vs. Plural:**
- **die Nudel** (Singular) = one single noodle (sehr selten verwendet)
- **die Nudeln** (Plural) = noodles (normale Verwendung!)

**Common Pattern:**
- "Ich esse Nudeln." (NOT "Ich esse Nudel.")
- "Diese Nudeln schmecken gut." (NOT "Diese Nudel...")
- "eine Portion Nudeln" (NOT "eine Portion Nudel")

**Similar Words (Plural in Normal Use):**
- die Spaghetti (Plural! from Italian, no singular in German)
- die Pommes (Plural! die Pommes frites)
- die Nudeln (Plural!)
- die Kartoffeln (Plural when eating, Singular: "eine Kartoffel" only when counting)

**Rule:** Food items that come in multiples are USUALLY plural in German!

#### Error 2: Article + Adjective
- **Type:** ARTICLE_ADJECTIVE
- **Original:** "halb Portion"
- **Corrected:** "eine halbe Portion"
- **Explanation:** Braucht Artikel "eine" + Adjektivendung "-e"

**Correct Structure:**
- **Article:** eine (feminine, accusative)
- **Adjective:** halbe (ending -e after indefinite article feminine/nominative/accusative)
- **Noun:** Portion (feminine)

**Declension Pattern:**
| Case | Article + Adjective + Noun |
|------|----------------------------|
| Nominativ | eine halbe Portion |
| Akkusativ | eine halbe Portion |
| Dativ | einer halben Portion |
| Genitiv | einer halben Portion |

**Common Fractions:**
- eine halbe Portion = half a portion
- eine ganze Portion = a whole portion
- eine doppelte Portion = a double portion
- eine große Portion = a large portion

**Wrong vs. Right:**
- ❌ "halb Portion" (no article, no adjective ending)
- ✓ **"eine halbe Portion"** (article + adjective -e ending)

#### Error 3: Unnecessary Preposition "von"
- **Type:** PREPOSITION
- **Original:** "halb Portion von Gemüse"
- **Corrected:** "eine halbe Portion Gemüse"
- **Explanation:** Kein "von" nötig! Direkte Genitivverbindung oder Kompositum.

**Correct Pattern:**
- eine Portion Gemüse (NOT "von Gemüse")
- eine Tasse Kaffee (NOT "von Kaffee")
- ein Glas Wasser (NOT "von Wasser")
- ein Stück Kuchen (NOT "von Kuchen")
- eine Scheibe Brot (NOT "von Brot")

**When to use "von":**
- "die Hälfte **von** diesem Gemüse" = the half of THIS vegetable (specific reference)
- "ein Teil **von** der Pizza" = a part of THE pizza (specific item)

**Rule:** 
Quantity expressions (Portion, Glas, Tasse, Stück) + direct noun WITHOUT "von"!

#### Error 4: Time Expression (minor)
- **Type:** TIME_EXPRESSION
- **Original:** "Am Mittag"
- **Better:** "Zum Mittagessen" oder "Mittags"
- **Explanation:** "Am Mittag" ist korrekt, aber "zum Mittagessen" ist für Mahlzeiten üblicher.

**Time Expressions for Meals:**
- **zum Frühstück** = for breakfast (preferred)
- **zum Mittagessen** = for lunch (preferred)
- **zum Abendessen** = for dinner (preferred)

**Alternative Adverbs:**
- **morgens** = in the morning
- **mittags** = at noon, at lunchtime
- **abends** = in the evening

**Less Common but Correct:**
- am Morgen = in the morning
- am Mittag = at noon
- am Abend = in the evening

### Grammar Frame Focus
**GrammarFrame: ARTIKEL_ADJEKTIV_ENDUNG**

Adjektive nach unbestimmtem Artikel (ein, eine, ein) im Nominativ/Akkusativ Femininum enden auf **-e**:

| Gender | Nominativ | Akkusativ |
|--------|-----------|-----------|
| Feminin | eine **halbe** Portion | eine **halbe** Portion |
| Maskulin | ein **halber** Apfel | einen **halben** Apfel |
| Neutral | ein **halbes** Brot | ein **halbes** Brot |

**Pattern:**
- Feminine: ein**e** + adjective**-e** + noun (Nom/Akk)
- Masculine: ein + adjective**-er** + noun (Nom) / ein**en** + adjective**-en** (Akk)
- Neuter: ein + adjective**-es** + noun (Nom/Akk)

### Vocabulary Additions
- **die Nudel** (Plural: die Nudeln) = noodle, noodles (ALWAYS plural in normal use!)
- **die Portion** (Plural: die Portionen) = portion, serving
- **die Bandnudeln** (Plural) = ribbon noodles, fettuccine, tagliatelle
- **der Lachs** (Plural: die Lachse) = salmon
- **die Kräuter-Sahne-Sauce** = herb cream sauce
- **zum Mittagessen** = for lunch, at lunchtime
- **mittags** (Adverb) = at noon, at lunchtime

### Additional Notes
- Context: REWE HIGH PROTEIN ready meal (489 kcal, 28g protein per pack)
- ASC-certified Norwegian salmon (sustainable aquaculture)
- User learning plural forms for food items
- User learning article + adjective declension
- User learning when to omit preposition "von"

## Session Metadata
- Date: 2026-10-15
- Time: Mittag (~12:12 Uhr)
- Task: Ernährungsdokumentation (nutrition logging)
- Context: Lunch with high-protein ready meal + vegetables
- Input Mode: Text with 3 image attachments (package front, back, cooked dish)
