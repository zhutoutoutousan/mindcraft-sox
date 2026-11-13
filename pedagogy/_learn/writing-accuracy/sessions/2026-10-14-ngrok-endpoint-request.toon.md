schema: writing-accuracy/session
version: 1.0

# Session: ngrok-Endpunkt Anfrage (2026-10-14 Morgen)

## Context
Der Benutzer möchte einen ngrok-Endpunkt erstellen, damit er das PDF auf seinem Handy herunterladen kann.

## Original Text
"Naja, könntest du ngrok Endpunkt machen, sodass kann ich es auf meinem Handy herunterladen"

## Corrected Text
"Naja, könntest du einen ngrok-Endpunkt erstellen, sodass ich es auf meinem Handy herunterladen kann?"

## Analysis

### Primary Error Focus
**ARTICLE_MISSING** + **WORD_ORDER** + **COMPOUND_NOUN**

### Detailed Breakdown

#### Error 1: Missing Article
- **Type:** ARTICLE_MISSING
- **Original:** "ngrok Endpunkt machen"
- **Corrected:** "einen ngrok-Endpunkt erstellen"
- **Explanation:** Vor einem Nomen (Endpunkt) braucht man normalerweise einen Artikel. "einen" (Akkusativ maskulin) nach "könntest du ... machen".

**Rule:**
- der Endpunkt (Nominativ) → den Endpunkt (Akkusativ) → einen Endpunkt (unbestimmt)
- "einen Endpunkt erstellen/machen"

#### Error 2: Word Order After "sodass"
- **Type:** WORD_ORDER (SUBORDINATE_CLAUSE)
- **Original:** "sodass kann ich"
- **Corrected:** "sodass ich"
- **Explanation:** Nach der Subjunktion "sodass" steht das **Verb am Ende**, KEINE Inversion!

**Subordinating Conjunctions (Verb am Ende):**
- "weil ich gehe" ✗ → "weil ich **gehe**" ✓
- "damit kann ich" ✗ → "damit ich **kann**" ✓
- "sodass kann ich" ✗ → "sodass ich ... **kann**" ✓

**Complete Sentence Structure:**
- Main clause: "Könntest du einen Endpunkt erstellen"
- Subordinate clause: "sodass ich es ... herunterladen **kann**"
- → "sodass ich es auf meinem Handy herunterladen **kann**"

#### Error 3: Compound Noun Format
- **Type:** COMPOUND_NOUN
- **Original:** "ngrok Endpunkt"
- **Corrected:** "ngrok-Endpunkt"
- **Explanation:** Englische/technische Begriffe + deutsche Nomen werden mit Bindestrich verbunden.

**Examples:**
- API-Endpunkt (not: API Endpunkt)
- HTTP-Server
- PDF-Datei
- ngrok-Tunnel
- **ngrok-Endpunkt**

#### Additional: Verb Choice
- **Type:** VOCABULARY_PRECISION
- **Original:** "machen"
- **Better:** "erstellen"
- **Explanation:** "erstellen" ist präziser für technische/digitale Objekte. "machen" ist umgangssprachlicher.

**Verb Hierarchy:**
- "machen" = general (make)
- "erstellen" = create (especially digital/documents)
- "erzeugen" = generate/produce
- "aufsetzen" = set up (infrastructure)

### Grammar Frame Focus
**GrammarFrame: WORD_ORDER_SUBORDINATE_CLAUSES**

Nebensätze mit Subjunktionen: **Verb am Ende**

| Subjunktion | Falsch | Richtig |
|-------------|--------|---------|
| weil | weil kann ich | weil ich ... **kann** |
| dass | dass habe ich | dass ich ... **habe** |
| sodass | sodass kann ich | sodass ich ... **kann** |
| damit | damit kann ich | damit ich ... **kann** |
| obwohl | obwohl bin ich | obwohl ich ... **bin** |

**Merksatz:** Nach "weil, dass, sodass, damit, obwohl" → Verb am Ende!

### Vocabulary Additions
- **der Endpunkt** (Plural: die Endpunkte) = endpoint (technical term)
- **der Tunnel** (Plural: die Tunnel) = tunnel (network)
- **erstellen** (Verb) = to create, to generate
- **herunterladen** (Verb, trennbar) = to download
- **sodass** (Subjunktion) = so that (consequence)

### Additional Notes
- Technical context: ngrok creates secure tunnels to localhost
- User wants mobile access to generated PDF report
- Shows good understanding of remote access needs

## Session Metadata
- Date: 2026-10-14
- Time: Morgen (~06:00 Uhr)
- Task: ngrok-Endpunkt Anfrage
- Context: After PDF report generation, needs mobile download
- Input Mode: Text (natural, colloquial request)
