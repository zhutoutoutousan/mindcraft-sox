schema: writing-accuracy/session
date: 2026-10-11
primaryLang: de
context: clarifying-dumpling-filling-ingredients

## Raw

Die Erfüllungen sind Schwein und 韭菜

## Minimal rewrite

Die Füllungen sind Schweinefleisch und Schnittlauch (韭菜).

## Errors

### E1: Falsches Wort "Erfüllung" statt "Füllung" [VOCABULARY_CONFUSION]
- Raw: `Erfüllungen`
- Fix: `Füllungen`
- Frame: Verwechslung ähnlich klingender Wörter mit unterschiedlicher Bedeutung
- Note: Klassischer Anfängerfehler bei ähnlichen Wortstämmen

**"Füllung" vs. "Erfüllung":**
| Wort | Bedeutung | Beispiel |
|------|-----------|----------|
| die Füllung | filling (in food) | Die Füllung der Dumplings ist Schweinefleisch |
| die Erfüllung | fulfillment, completion | Die Erfüllung eines Wunsches |

**Weitere ähnliche Paare:**
| Oft verwechselt | Bedeutung 1 | Bedeutung 2 |
|-----------------|-------------|-------------|
| fallen vs. fällen | to fall | to cut down (trees) |
| bieten vs. bitten | to offer | to ask/request |
| raten vs. beraten | to guess | to advise |

### E2: "Schweinefleisch" statt nur "Schwein" [WORD_SPECIFICITY]
- Raw: `Schwein`
- Fix: `Schweinefleisch`
- Frame: Beim Essen verwendet man das vollständige Wort "Schweinefleisch" (nicht nur das Tier)
- Note: "Schwein" allein ist umgangssprachlich verständlich, aber "Schweinefleisch" ist korrekter

**Tier vs. Fleisch:**
| Tier | Fleisch | Beispiel |
|------|---------|----------|
| das Schwein | das Schweinefleisch | Ich esse Schweinefleisch |
| das Rind | das Rindfleisch | Die Füllung ist Rindfleisch |
| das Huhn | das Hühnerfleisch / Hähnchen | Wir haben Hühnerfleisch |
| das Lamm | das Lammfleisch | Das Restaurant serviert Lammfleisch |

**Ausnahmen (wo Tier = Fleisch):**
- der Fisch → der Fisch (gleich)
- das Hähnchen → das Hähnchen (gleich)

### E3: Code-Switching mit chinesischen Zeichen [LANGUAGE_MIX]
- Raw: `韭菜` (nur Chinesisch)
- Fix: `Schnittlauch (韭菜)` oder `韭菜 (Schnittlauch)`
- Frame: Beim Mischen von Sprachen: deutsche Übersetzung + chinesisches Original in Klammern
- Note: Für deutsche Leser ist die Übersetzung hilfreich

**Gute Praxis beim Code-Switching:**
| Situation | Besser |
|-----------|--------|
| Chinesisches Essen | Dumplings (饺子) |
| Zutaten | Schnittlauch (韭菜) |
| Orte | Babelsberg Starry Night |
| Fachbegriffe | Erkläre beide |

## GrammarFrame focus

**Verwechslungsgefahr: "Füllung" vs. "Erfüllung"**

Diese Wörter klingen ähnlich, haben aber **völlig unterschiedliche Bedeutungen**.

**die Füllung (filling):**
- Verwendet bei: Essen, Kissen, Zahnmedizin
- Stamm: füllen (to fill)
- Beispiele:
  - Die **Füllung** der Dumplings
  - Die **Füllung** des Kissens (pillow stuffing)
  - Die **Füllung** im Zahn (dental filling)

**die Erfüllung (fulfillment/completion):**
- Verwendet bei: Wünsche, Träume, Pflichten
- Stamm: erfüllen (to fulfill)
- Beispiele:
  - Die **Erfüllung** eines Wunsches
  - Die **Erfüllung** einer Aufgabe
  - Persönliche **Erfüllung** finden

**Eselsbrücke:**
- Füllung → füllen → etwas **füllen** (physisch)
- Erfüllung → erfüllen → etwas **erfüllen** (abstrakt)

### Merksatz
**Füllung = physisch (Essen, Kissen); Erfüllung = abstrakt (Wünsche, Träume)**

## Context
User clarified the filling of the dumplings eaten earlier: pork (猪肉) and Chinese chives (韭菜/jiǔcài). This is a classic and popular Chinese dumpling filling combination (韭菜猪肉饺子). Made an interesting vocabulary error: used "Erfüllung" (fulfillment) instead of "Füllung" (filling) - these sound similar but have completely different meanings. Also used "Schwein" (pig/animal) instead of "Schweinefleisch" (pork/meat). Code-switching with Chinese character 韭菜 without German translation.

## Cultural Note
韭菜猪肉饺子 (jiǔcài zhūròu jiǎozi) is one of the most traditional and beloved dumpling fillings in northern Chinese cuisine. The combination of savory pork with aromatic garlic chives is iconic. The user visited the Chinese Garden and then ate authentic Chinese dumplings - a thematically perfect day!

## Vocabulary Building
This error ("Erfüllung" vs. "Füllung") is actually a great learning opportunity because both words exist and sound similar, but mean completely different things. This type of error shows the learner is trying to construct German words logically (adding "Er-" prefix), which is a sign of active language processing, not just memorization.
