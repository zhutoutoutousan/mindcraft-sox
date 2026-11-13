schema: writing-accuracy/session
date: 2026-10-11
primaryLang: de
context: weight-update-with-explanation

## Raw

Heute morgen ist mein Körpergewicht 66,70kg. Vielleicht liegt das daran, gestern hatte ich mit Owen in der Nacht bevor schlafen einige Hühnerschenkeln gegessen.

## Minimal rewrite

Heute Morgen beträgt mein Körpergewicht 66,70 kg. Vielleicht liegt das daran, dass ich gestern Abend mit Owen vor dem Schlafen einige Hühnerschenkel gegessen habe.

## Errors

### E1: Nebensatz mit "dass" [SUBORDINATE_CLAUSE_DASS]
- Raw: `liegt das daran, gestern hatte ich`
- Fix: `liegt das daran, **dass** ich gestern`
- Frame: Nach "daran, dass..." muss ein Nebensatz mit konjugiertem Verb am Ende folgen
- Note: "daran" verlangt eine Erklärung mit "dass" + Subjekt + ... + Verb

**Struktur "liegt daran, dass...":**
| Falsch | Richtig |
|--------|---------|
| ❌ liegt das daran, ich hatte | ✅ liegt das daran, **dass** ich ... hatte |
| ❌ liegt das daran, gestern aß ich | ✅ liegt das daran, **dass** ich gestern ... aß |

### E2: Temporale Präposition vs. Konjunktion [TEMPORAL_PREP_CONJ]
- Raw: `in der Nacht **bevor** schlafen`
- Fix: `am Abend **vor dem** Schlafen` oder `**bevor ich schlief**`
- Frame: "bevor" = Konjunktion (braucht Subjekt + Verb); "vor" = Präposition (braucht Nomen/Artikel + Dativ)
- Note: "bevor schlafen" ist ungrammatisch; entweder "bevor ich schlafe" oder "vor dem Schlafen"

**"bevor" (Konjunktion) vs. "vor" (Präposition):**
| Konjunktion + Verb | Präposition + Nomen |
|--------------------|---------------------|
| bevor ich **schlafe** | vor dem **Schlafen** |
| bevor wir **essen** | vor dem **Essen** |
| bevor du **gehst** | vor deinem **Gehen** / vor der Arbeit |

### E3: Plural-Form Akkusativ [NOUN_PLURAL_CASE]
- Raw: `einige Hühnerschenkel**n**`
- Fix: `einige Hühnerschenkel`
- Frame: Plural von "der Schenkel" = "die Schenkel" (keine -n Endung im Akkusativ nach "einige")
- Note: Im Dativ wäre es "mit den Hühnerschenkel**n**", aber Akkusativ hat kein -n

**Plural-Deklination "der Schenkel":**
| Kasus | Plural | Beispiel |
|-------|--------|----------|
| Nominativ | die Schenkel | Die Schenkel sind groß |
| Akkusativ | die Schenkel | Ich esse die Schenkel |
| Dativ | den Schenkel**n** | mit den Schenkel**n** |
| Genitiv | der Schenkel | der Geschmack der Schenkel |

### E4: Großschreibung "Morgen" [CAPITALIZATION_NOUN]
- Raw: `Heute morgen`
- Fix: `Heute **M**orgen`
- Frame: "Morgen" als Nomen (Tageszeit) wird großgeschrieben
- Note: "morgen" (klein) = tomorrow; "Morgen" (groß) = morning

**Zeitangaben Groß-/Kleinschreibung:**
| Klein (Adverb) | Groß (Nomen) |
|----------------|--------------|
| morgen (= tomorrow) | heute **Morgen** (= this morning) |
| gestern | gestern **Abend** |
| heute | heute **Nachmittag** |

### E5: Verb-Perfekt statt Präteritum [VERB_TENSE_SPOKEN]
- Raw: `gestern hatte ich ... gegessen` (Präteritum + Partizip = gemischt)
- Fix: `gestern habe ich ... gegessen` (Perfekt) oder `gestern aß ich` (Präteritum)
- Frame: In gesprochener Sprache: Perfekt bevorzugt; "hatte gegessen" = Plusquamperfekt (für Vorvergangenheit)
- Note: "hatte gegessen" bedeutet "etwas war schon vorher passiert"; hier ist einfaches Perfekt richtig

**Vergangenheits-Zeitformen:**
| Form | Wann | Beispiel |
|------|------|----------|
| Perfekt | Standard Vergangenheit (gesprochen) | Ich **habe** gegessen |
| Präteritum | Literatur / formell | Ich **aß** |
| Plusquamperfekt | Vorvergangenheit (schon davor) | Ich **hatte** gegessen (bevor X passierte) |

### E6: "beträgt" statt "ist" [VERB_CHOICE_WEIGHT]
- Raw: `ist mein Körpergewicht 66,70kg`
- Fix: `**beträgt** mein Körpergewicht 66,70 kg` oder `**wiegt** mein Körper 66,70 kg`
- Frame: Bei Messungen: "beträgt" (= amounts to) oder "liegt bei" oder "wiegen" natürlicher als "ist"
- Note: "ist" nicht falsch, aber "beträgt" ist präziser bei Zahlen/Messungen

## GrammarFrame focus

**Nebensatz nach "daran, dass..."**

"daran" ist ein Verweiswort (Pronominaladverb) und verlangt eine Erklärung mit "dass" + Nebensatz.

**Struktur:**
- Hauptsatz: Das liegt daran, [...]
- Nebensatz: dass + Subjekt + ... + Verb

**Beispiele:**
| Situation | Satz |
|-----------|------|
| Gewichtszunahme | Das liegt daran, **dass** ich gestern viel gegessen **habe** |
| Müdigkeit | Das liegt daran, **dass** ich schlecht geschlafen **habe** |
| Verspätung | Das liegt daran, **dass** der Zug ausgefallen **ist** |

**Häufiger Fehler:**
❌ Das liegt daran, gestern habe ich... (kein "dass")  
✅ Das liegt daran, **dass** ich gestern...

### Merksatz
**"daran" + Komma → immer "dass" + Nebensatz mit Verb am Ende**

## Context
User reported morning weight of 66.70 kg (up from 66.05 kg two days ago) and correctly attributed it to eating chicken thighs with Owen late at night before sleeping. Complex sentence with multiple errors: missing "dass" in subordinate clause, temporal preposition/conjunction confusion, plural form error, capitalization, and mixed verb tenses.

## Progress Note
Despite grammatical errors, the user correctly identified cause-and-effect (late eating → weight gain), showing good logical reasoning in German context.
