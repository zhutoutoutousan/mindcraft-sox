schema: writing-accuracy/session
date: 2026-10-10
primaryLang: de
context: breakfast-meal-documentation

## Raw

Das sind meine heutigen Frühstück

## Minimal rewrite

Das ist mein heutiges Frühstück

## Errors

### E1: Subjekt-Verb-Kongruenz Numerus [AGREEMENT_VERB_SUBJECT_NUMBER]
- Raw: `Das sind ... Frühstück`
- Fix: `Das ist ... Frühstück`
- Frame: "das Frühstück" ist **Singular** (eine Mahlzeit) → Verb **ist** (nicht **sind**)
- Note: Auch wenn mehrere Komponenten auf dem Teller sind (Brötchen + Cappuccino), ist "Frühstück" als Mahlzeit singular

**Singular vs. Plural Verb:**
| Subjekt | Verb | Beispiel |
|---------|------|----------|
| Singular | ist | Das **ist** mein Frühstück |
| Plural | sind | Das **sind** meine Brötchen |

### E2: Possessivpronomen + Adjektiv Numerus [POSSESSIVE_ADJECTIVE_NUMBER]
- Raw: `meine heutigen Frühstück`
- Fix: `mein heutiges Frühstück`
- Frame: "das Frühstück" ist **Singular neutrum** → **mein heutig**es** (nicht **meine heutigen**)
- Note: "meine heutigen" wäre Plural (meine heutigen Pläne, meine heutigen Mahlzeiten)

**Possessiv + Adjektiv Deklination (Nominativ):**
| Numerus | Neutrum | Beispiel |
|---------|---------|----------|
| Singular | mein heutig**es** Frühstück | das Frühstück |
| Plural | meine heutig**en** Mahlzeiten | die Mahlzeiten |

### E3: Zusammenhängendes Konzept [CONCEPTUAL_SINGULAR]
- Context: Auch bei mehreren Komponenten (Brötchen, Cappuccino) ist "Frühstück" **eine Mahlzeit** → Singular
- Vergleich: "Das ist mein Frühstück" (die ganze Mahlzeit) vs. "Das sind meine Frühstückssachen" (die einzelnen Dinge)
- Note: In der Alltagssprache behandelt man "Frühstück/Mittagessen/Abendessen" als Singular-Konzept

## GrammarFrame focus

**Singular Mahlzeiten-Konzept trotz mehrerer Komponenten**

"Frühstück", "Mittagessen", "Abendessen" sind **Singular-Nomen**, auch wenn die Mahlzeit aus mehreren Teilen besteht.

**Richtig (Singular):**
| Mahlzeit | Satz |
|----------|------|
| das Frühstück | Das **ist** mein Frühstück (Brötchen + Kaffee) |
| das Mittagessen | Das **ist** mein Mittagessen (Suppe + Brot) |
| das Abendessen | Das **ist** mein Abendessen (Bowl + Drink) |

**Falsch (Plural):**
| Fehler | Warum falsch |
|--------|--------------|
| ❌ Das **sind** mein Frühstück | "sind" ist Plural, aber "Frühstück" ist Singular |
| ❌ Das sind **meine** Frühstück | "meine" ist Plural, aber "Frühstück" ist Singular |

**Wenn du Plural willst, ändere das Nomen:**
| Plural-Alternative | Beispiel |
|--------------------|----------|
| die Sachen | Das **sind** meine Frühstückssachen |
| die Teile | Das **sind** die Teile meines Frühstücks |
| die Gerichte | Das **sind** meine heutigen Gerichte |

### Merksatz
**"Frühstück/Mittagessen/Abendessen" = Singular-Konzept → "Das ist mein..."**

## Context
User documented Saturday breakfast with Leberkäse sandwich and large cappuccino. Made compound error: used plural verb "sind" and plural adjective "meine heutigen" with singular noun "Frühstück". This continues the pattern of adjective gender/number agreement errors from previous sessions.

## Related Errors (Pattern Recognition)
This builds on recent similar errors:
1. **2026-10-09 dinner:** "Mein heutiger Abendessen" → "Mein heutiges Abendessen" (gender)
2. **2026-10-09 breakfast (older):** "Es ist das Frühstück für mich" → "Das ist mein Frühstück" (style)
3. **2026-10-10 breakfast:** "Das sind meine heutigen Frühstück" → "Das ist mein heutiges Frühstück" (number + gender)

Pattern: Adjective agreement (gender, number) with meal nouns needs reinforcement.
