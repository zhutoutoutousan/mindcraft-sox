schema: writing-accuracy/session
date: 2026-10-11
primaryLang: de
context: dinner-dumplings-documentation

## Raw

Wir haben dumplings Abend gegessen. Ich habe ungefähr 5 Stück gegessen.

## Minimal rewrite

Wir haben am Abend Dumplings gegessen. Ich habe ungefähr 5 Stück gegessen.

## Errors

### E1: Zeitangabe ohne Präposition [TIME_EXPRESSION_PREPOSITION]
- Raw: `dumplings Abend gegessen`
- Fix: `**am** Abend Dumplings gegessen`
- Frame: Zeitangaben mit Tageszeiten brauchen die Präposition "**am**" (an dem)
- Note: "Abend" als Zeitpunkt braucht "am"; "zum Abendessen" wäre auch korrekt

**Zeitangaben mit "am":**
| Tageszeit | Präposition | Beispiel |
|-----------|-------------|----------|
| Morgen | **am** Morgen | Ich esse **am** Morgen |
| Vormittag | **am** Vormittag | Wir treffen uns **am** Vormittag |
| Mittag | **am** Mittag | Er isst **am** Mittag |
| Nachmittag | **am** Nachmittag | Sie kommt **am** Nachmittag |
| Abend | **am** Abend | Wir essen **am** Abend |

**Alternative: "zum + Mahlzeit":**
| Mahlzeit | Präposition | Beispiel |
|----------|-------------|----------|
| Frühstück | **zum** Frühstück | Ich esse Brot **zum** Frühstück |
| Mittagessen | **zum** Mittagessen | Wir haben Suppe **zum** Mittagessen |
| Abendessen | **zum** Abendessen | Sie isst Dumplings **zum** Abendessen |

### E2: Großschreibung Fremdwort-Nomen [CAPITALIZATION_LOAN_WORD]
- Raw: `dumplings`
- Fix: `Dumplings`
- Frame: Auch Fremdwörter (Anglizismen, etc.) werden als Nomen großgeschrieben
- Note: Im Deutschen werden **alle** Nomen großgeschrieben, egal aus welcher Sprache sie kommen

**Fremdwörter als Nomen - Großschreibung:**
| Falsch | Richtig | Herkunft |
|--------|---------|----------|
| ❌ dumplings | ✅ Dumplings | Englisch |
| ❌ pizza | ✅ Pizza | Italienisch |
| ❌ sushi | ✅ Sushi | Japanisch |
| ❌ croissant | ✅ Croissant | Französisch |
| ❌ cappuccino | ✅ Cappuccino | Italienisch |

## GrammarFrame focus

**Zeitangaben mit Präpositionen: "am" vs. "zum"**

Im Deutschen brauchen Zeitangaben **immer eine Präposition**, wenn sie als Adverbiale verwendet werden.

**"am" (an dem) = Zeitpunkt (Tageszeit):**
- am Morgen = in the morning
- am Abend = in the evening
- am Wochenende = on the weekend
- am Montag = on Monday

**"zum" (zu dem) = Anlass/Mahlzeit:**
- zum Frühstück = for breakfast
- zum Mittagessen = for lunch
- zum Abendessen = for dinner
- zum Geburtstag = for birthday

**Häufiger Fehler:**
| Falsch | Richtig | Warum |
|--------|---------|-------|
| ❌ Wir essen Abend | ✅ Wir essen **am** Abend | Zeitpunkt braucht "am" |
| ❌ Ich frühstücke Morgen | ✅ Ich frühstücke **am** Morgen | oder "morgen früh" (tomorrow) |
| ❌ Sie isst Mittagessen | ✅ Sie isst **zum** Mittagessen | Mahlzeit braucht "zum" |

**Ohne Präposition nur bei:**
- Wochentagen mit Artikel: "**den** Abend verbringen"
- Als direktes Objekt: "einen schönen Abend haben"

### Merksatz
**Zeitpunkt (Tageszeit) = "am"; Mahlzeit/Anlass = "zum"**

## Context
User documented dinner with Owen after visiting the Chinese Garden in Berlin. They ate Chinese dumplings (jiaozi) - the user had 5 pieces. Photo shows beautiful presentation with soy sauce dip on a blue and white Chinese-style plate. Two errors: missing preposition "am" with time expression and lowercase "dumplings" instead of capitalized noun. The second sentence was perfect.

## Progress Note
The second sentence "Ich habe ungefähr 5 Stück gegessen" was completely correct! This shows the user is getting more consistent with basic sentence structures. The errors were specific to time expressions and foreign word capitalization - both understandable mistakes for learners.

## Cultural Note
After a long day visiting the Chinese Garden, eating Chinese dumplings is thematically fitting! The presentation in the photo (blue and white porcelain, soy sauce dip) looks authentic and restaurant-quality, possibly from a restaurant near the Gärten der Welt.
