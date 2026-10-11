schema: writing-accuracy/session
date: 2026-10-11
primaryLang: de
context: snack-documentation-before-garden-trip

## Raw

Ich habe gerade eine Tasse Kaffee und etwas Hühnchenherz gegessen

## Minimal rewrite

Ich habe gerade eine Tasse Kaffee getrunken und etwas Hühnerherz gegessen.

## Errors

### E1: Verb-Wahl "trinken" vs. "essen" [VERB_CHOICE_DRINK_EAT]
- Raw: `Kaffee ... gegessen`
- Fix: `Kaffee getrunken`
- Frame: Flüssigkeiten werden **getrunken**, nicht gegessen
- Note: Häufiger Fehler bei Nicht-Muttersprachlern; im Deutschen strikt getrennt

**"trinken" vs. "essen":**
| Flüssigkeit (trinken) | Feste Nahrung (essen) |
|-----------------------|-----------------------|
| Kaffee **trinken** | Brot **essen** |
| Tee **trinken** | Fleisch **essen** |
| Wasser **trinken** | Obst **essen** |
| Milch **trinken** | Gemüse **essen** |
| Saft **trinken** | - |

**Sonderfall Suppe:**
- Im Deutschen: Suppe **essen** ✓ (obwohl flüssig!)
- "Ich esse eine Suppe" (nicht "trinke")

### E2: Kompositum "Hühnerherz" nicht "Hühnchenherz" [NOUN_COMPOUND]
- Raw: `Hühnchenherz`
- Fix: `Hühnerherz`
- Frame: Organ-Fleisch verwendet "Huhn" als Stamm, nicht "Hühnchen"
- Note: "Hühnchen" = das ganze (junge) Tier beim Essen; Organe = "Hühner-"

**Komposita mit "Huhn" vs. "Hühnchen":**
| Organe/Teile (Hühner-) | Ganzes Tier (Hühnchen) |
|------------------------|------------------------|
| das Hühner**herz** | das Hühnchen (gegrillt) |
| die Hühner**leber** | das Brathühnchen |
| der Hühner**magen** | das gebratene Hühnchen |
| die Hühner**brust** | - |
| der Hühner**schenkel** | - |

**Warum "Hühner-"?**
- Kommt von "das Huhn" (das Tier)
- Genitiv Plural: "der Hühner" → "Hühnerherz" = Herz der Hühner

**Warum "Hühnchen"?**
- Diminutiv von "Huhn" (kleines Huhn, junges Huhn)
- Wird für das ganze gebratene/gekochte Tier verwendet

## GrammarFrame focus

**Verb-Wahl nach Nahrungsart: "trinken" vs. "essen"**

Im Deutschen gibt es eine **strikte Trennung** zwischen Flüssigkeiten und fester Nahrung beim Verb.

**Regel:**
- Flüssigkeiten → **trinken**
- Feste Nahrung → **essen**

**Häufige Fehler:**
| Falsch | Richtig | Warum |
|--------|---------|-------|
| ❌ Kaffee essen | ✅ Kaffee **trinken** | Flüssigkeit |
| ❌ Wasser essen | ✅ Wasser **trinken** | Flüssigkeit |
| ❌ Suppe trinken | ✅ Suppe **essen** | Sonderfall! |
| ❌ Brot trinken | ✅ Brot **essen** | Fest |

**Sonderfall Suppe:**
Obwohl Suppe flüssig ist, sagt man im Deutschen "Suppe **essen**" (nicht "trinken"). Das ist eine Ausnahme!

**Englisch vs. Deutsch:**
- Englisch: "I had coffee" (neutral)
- Deutsch: "Ich habe Kaffee **getrunken**" (spezifisch)

### Merksatz
**Flüssigkeiten trinken, feste Nahrung essen – Suppe ist die Ausnahme!**

## Context
User documented a quick snack before departure to the Chinese Garden: coffee and chicken hearts (prepared at home). Made two errors: used "essen" (eat) instead of "trinken" (drink) for coffee, and used "Hühnchenherz" instead of "Hühnerherz" for the organ meat compound.

## Pattern Note
The verb error (trinken vs. essen) is a common mistake for non-native speakers, especially from languages that use one verb for both (e.g., Chinese 吃/喝 distinction is similar but not identical). The compound noun error shows German noun composition rules still need reinforcement.

## Progress Context
Despite these errors, the sentence structure was good, and the user is documenting meals proactively. The basic sentence construction ("Ich habe ... gegessen/getrunken") was correct, just the specific verbs need attention.
