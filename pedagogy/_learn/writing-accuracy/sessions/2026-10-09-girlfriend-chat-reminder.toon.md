schema: writing-accuracy/session
date: 2026-10-09
primaryLang: de
context: reminder-note-for-girlfriend-chat-continuity

## Raw

Das ist meine Notiz für meine Freundin, ich bin ihrer Freund, sie hat zur Gewohnheit gegangen, jedes Mal ein neuer Chatsitzung zu starten, deshalb bekommt sie keine "the way the product is designed to be working", so bitte notieren Sie sie nächstes Mal ja. Nebenbei, du sollst Korrigiertes Satz geben und die Fokus geben bei der Korrigierung.

## Minimal rewrite

Das ist eine Notiz für meine Freundin. Ich bin ihr Freund. Sie hat die Gewohnheit, jedes Mal eine neue Chat-Sitzung zu starten, deshalb bekommt sie nicht die optimale Funktionsweise des Produkts. Bitte erinnere sie beim nächsten Mal daran. Nebenbei sollst du den korrigierten Satz geben und den Fokus bei der Korrektur angeben.

## Errors

### E1: Possessivpronomen Kasus/Genus [POSSESSIVE_CASE_GENDER]
- Raw: `ich bin ihrer Freund`
- Fix: `ich bin ihr Freund`
- Frame: Possessiv "ihr" (= belonging to her) + maskulin Nominativ → keine Endung
- Note: "ihrer" ist Genitiv/Dativ feminin oder Genitiv Plural, nicht maskulin Nominativ

**Deklination "ihr" (= her):**
| Kasus | maskulin | feminin | neutrum |
|-------|----------|---------|---------|
| Nom | ihr Freund | ihre Freundin | ihr Kind |
| Akk | ihren Freund | ihre Freundin | ihr Kind |
| Dat | ihrem Freund | ihrer Freundin | ihrem Kind |
| Gen | ihres Freundes | ihrer Freundin | ihres Kindes |

### E2: Idiom "Gewohnheit haben" [IDIOM_CONSTRUCTION]
- Raw: `sie hat zur Gewohnheit gegangen`
- Fix: `sie hat die Gewohnheit`
- Frame: Feste Wendung: **jemand hat die Gewohnheit, etwas zu tun**
- Alternative: "sie ist es gewohnt" oder "sie pflegt zu..."
- Note: "zur Gewohnheit gegangen" ist kein korrektes deutsches Idiom

### E3: Artikel + Adjektiv + Genus [ARTICLE_ADJECTIVE_GENDER]
- Raw: `ein neuer Chatsitzung`
- Fix: `eine neue Chat-Sitzung`
- Frame: "die Sitzung" ist feminin → unbestimmter Artikel **eine** + Adjektiv **neue** (nicht **ein neuer**)
- Note: maskulin wäre "ein neuer Chat", aber "eine neue Sitzung"

**Adjektivdeklination nach unbestimmtem Artikel:**
| Kasus | maskulin | feminin | neutrum |
|-------|----------|---------|---------|
| Nom | ein neuer | eine neue | ein neues |
| Akk | einen neuen | eine neue | ein neues |

### E4: Artikel bei substantiviertem Adjektiv [ARTICLE_NOMINALIZED_ADJECTIVE]
- Raw: `du sollst Korrigiertes Satz geben`
- Fix: `du sollst den korrigierten Satz geben`
- Frame: Adjektiv + Nomen braucht Artikel; "korrigiert" muss dekliniert werden (schwache Deklination nach bestimmtem Artikel)
- Note: **den** (Akkusativ maskulin) + **korrigierten** (schwache Endung -en)

### E5: Genus des Nomens [NOUN_GENDER]
- Raw: `die Fokus`
- Fix: `den Fokus`
- Frame: **der Fokus** (maskulin) → Akkusativ **den** Fokus (nicht **die**)
- Note: Viele auf -us endende Wörter aus dem Latein sind maskulin (der Kasus, der Zirkus, der Bonus)

### E6: Verbalternative "erinnern" vs "notieren" [LEXIS_VERB_CHOICE]
- Raw: `bitte notieren Sie sie nächstes Mal ja`
- Fix: `bitte erinnere sie beim nächsten Mal daran`
- Frame: "jemanden an etwas **erinnern**" = remind someone; "notieren" = write down/note
- Note: "notieren Sie sie" wäre "write her down" (nonsensical); richtig ist "erinnern Sie sie daran" = remind her of it

### E7: Satzstruktur - zu lang [SENTENCE_CHUNKING]
- Raw: Ein Satz mit 5+ Nebensätzen/Infos
- Fix: In mehrere Sätze aufgeteilt (3 Hauptsätze)
- Note: Deutsche Sätze sollten fokussiert bleiben; zu viele Infos → schwer lesbar

## GrammarFrame focus

**Possessivpronomen-Deklination nach Genus des Bezugsnomens**

"ihr" = her (possessive) richtet sich nach dem **Nomen**, das folgt:

| Bezugsnomen | Beispiel | Warum |
|-------------|----------|-------|
| der Freund (mask.) | **ihr** Freund | Nominativ maskulin = keine Endung |
| den Freund (mask. Akk.) | **ihren** Freund | Akkusativ maskulin = -en |
| die Freundin (fem.) | **ihre** Freundin | feminin = -e |
| das Kind (neut.) | **ihr** Kind | neutrum = keine Endung (Nom/Akk) |

**Nicht verwechseln:**
- "**ihr** Freund" = her friend (mask. Nominativ)
- "**ihrer** Freundin" = to her friend (fem. Dativ) oder "of her friend" (Genitiv)

### Merksatz
**Possessivpronomen deklinieren nach Genus + Kasus des Bezugsnomens, nicht nach dem Besitzer**

## Context
User asked to save a reminder note for his girlfriend: she starts a new chat session every time, missing the benefit of continuous conversation. He also requested corrected sentences with correction focus. Multiple errors in possessives, idioms, gender agreement, and article usage.
