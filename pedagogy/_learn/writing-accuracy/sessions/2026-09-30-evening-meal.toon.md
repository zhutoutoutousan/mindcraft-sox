schema: writing-accuracy/session
date: 2026-09-30
primaryLang: de
context: evening-meal-documentation

## Raw

Heute Abend habe ich solche Lebensmittel mit Owen zusammen gegessen

## Minimal rewrite

Heute Abend habe ich diese Gerichte mit Owen gegessen.

## Errors

### E1: Demonstrativpronomen [DEMONSTRATIVE]
- Raw: `solche Lebensmittel`
- Fix: `diese Gerichte` oder `dieses Essen`
- Frame: `solch-` = "derart/so beschaffen" (such/of that kind); `dies-` = "hier gezeigte" (this/these)
- Note: "solche" klingt distanziert oder kategorisierend; bei Bezug auf gezeigte Bilder besser "diese"

### E2: Redundanz [REDUNDANCY]
- Raw: `mit Owen zusammen gegessen`
- Fix: `mit Owen gegessen` ODER `zusammen mit Owen gegessen`
- Frame: `mit jemandem essen` impliziert bereits "zusammen"
- Note: "mit" + "zusammen" ist pleonastisch; eines von beiden reicht

### E3: Wortschatz [LEXICAL_CHOICE]
- Raw: `Lebensmittel`
- Fix: `Gerichte` oder `Essen`
- Context: "Lebensmittel" = groceries/food items (roh); "Gerichte" = dishes/meals (zubereitet)
- Note: Bei fertigem Essen in Restaurant/zu Hause besser "Gerichte" oder "Essen"

## GrammarFrame focus

**Demonstrativpronomen (Demonstrative Pronouns)**

| Pronomen | Bedeutung | Verwendung | Beispiel |
|----------|-----------|------------|----------|
| dieser, diese, dieses | this/these | Direkter Bezug auf Anwesende/Gezeigte | Diese Gerichte habe ich gegessen |
| jener, jene, jenes | that/those | Entfernterer Bezug (selten, gehoben) | Jenes Restaurant war teuer |
| solcher, solche, solches | such | Art/Kategorie, oft bewertet | Solche Restaurants mag ich nicht |
| derselbe, dieselbe, dasselbe | the same | Identität | Wir aßen dasselbe Gericht |
| derjenige, diejenige, dasjenige | that one (specific) | Identifikation vor Relativsatz | Diejenigen, die hier waren |

### Merksatz
**"Dies-" zeigt, "solch-" kategorisiert, "derselbe" identifiziert**

## Context
User documented evening meal shared with Owen. Images showed prepared Asian dishes (Pad Thai, wonton soup, bubble tea). "solche Lebensmittel" was too abstract/categorical for this context.
