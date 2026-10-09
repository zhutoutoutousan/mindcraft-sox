schema: writing-accuracy/session
date: 2026-10-09
primaryLang: de
context: dinner-meal-documentation

## Raw

Mein heutiger Abendessen

## Minimal rewrite

Mein heutiges Abendessen

## Errors

### E1: Adjektivdeklination nach Possessivpronomen - Genus [ADJECTIVE_GENDER]
- Raw: `Mein heutiger Abendessen`
- Fix: `Mein heutiges Abendessen`
- Frame: **das** Abendessen (neutrum!) → Adjektiv **heutiges** (nicht **heutiger**)
- Note: "heutiger" wäre für maskulin Nomen (mein heutiger Tag); "heutige" für feminin (meine heutige Mahlzeit)

**Adjektivdeklination nach Possessivpronomen (Nominativ):**
| Genus | Possessiv + Adjektiv + Nomen | Beispiel |
|-------|------------------------------|----------|
| maskulin | mein heutig**er** Tag | der Tag → -er |
| feminin | meine heutig**e** Mahlzeit | die Mahlzeit → -e |
| neutrum | mein heutig**es** Abendessen | das Abendessen → -es |
| Plural | meine heutig**en** Pläne | die Pläne → -en |

## GrammarFrame focus

**Adjektivdeklination nach Possessivpronomen - Genus-Kongruenz**

Das Adjektiv richtet sich nach dem **Genus des Nomens**, nicht nach dem Possessivpronomen.

**Neutrum Nomen braucht -es:**
| Nomen | Richtig | Falsch |
|-------|---------|--------|
| das Abendessen | mein heutig**es** Abendessen | ❌ mein heutig**er** |
| das Frühstück | mein leckeres Frühstück | ❌ mein leckerer |
| das Mittagessen | mein gestrig**es** Mittagessen | ❌ mein gestrig**er** |
| das Essen | mein lieb**es** Essen | ❌ mein lieb**er** |

**Maskulin Nomen braucht -er:**
| Nomen | Richtig |
|-------|---------|
| der Tag | mein heutig**er** Tag |
| der Morgen | mein gestrig**er** Morgen |
| der Abend | mein schön**er** Abend |

**Feminin Nomen braucht -e:**
| Nomen | Richtig |
|-------|---------|
| die Mahlzeit | meine heutig**e** Mahlzeit |
| die Woche | meine nächst**e** Woche |
| die Suppe | meine lecker**e** Suppe |

### Merksatz
**"das" = neutrum → Adjektiv endet auf -es (mein heutiges Essen)**

## Context
User documented dinner with mixed vegetable bowl, breaded chicken/schnitzel, and YoPRO protein drink. Simple sentence but critical gender agreement error: "das Abendessen" is neuter, requires "heutiges" not "heutiger" (masculine).

## Related Errors
This is part of the same error pattern as:
- "ein neuer Chatsitzung" → "eine neue Chat-Sitzung" (from 2026-10-09-communication-channel-request)
- Both involve adjective gender agreement with the noun
