schema: writing-accuracy/session
date: 2026-10-03
lang: de
focus: modal_passiv_verb_position_2
primaryLang: de

## Original

> **ist Plastiktüten in Supermarkt verboten sollen**
> **haben viele Beitragen für das Thema diskutieren**
> **produzieren die Plastiktüten viel unnötig Müll, der umweltschonender stark verschmutzt**
> **konnten Menschen eigene Taschen mitbringen**
> **finde ich die Plastiktüten verboten ist sinnvoll**

## Rewrite

> **sollten Plastiktüten in Supermärkten verboten werden**
> **diskutieren viele über dieses Thema**
> **produzieren Plastiktüten viel unnötigen Müll, der die Umwelt stark verschmutzt**
> **können Menschen ihre eigenen Taschen mitbringen**
> **finde ich, dass ein Verbot von Plastiktüten sinnvoll ist**

## Errors

1. **ist...sollen** → **sollten...werden** (Verbposition: Verb an Position 2; Modalverb + Passiv mit "werden")
2. **in Supermarkt** → **in Supermärkten** (Plural nach Präposition ohne Artikel)
3. **haben...Beitragen...diskutieren** → **diskutieren viele** (Struktur: einfacher Hauptsatz; "Beiträge" Nominativ Plural nicht "Beitragen")
4. **die Plastiktüten** → **Plastiktüten** (Artikel: unnötig im generischen Satz)
5. **viel unnötig Müll** → **viel unnötigen Müll** (Adjektivdeklination: stark Akkusativ maskulin -en nach "viel")
6. **umweltschonender** → **die Umwelt** (Nomen statt Adjektiv)
7. **konnten** → **können** (Tempus: Präsens, nicht Präteritum)
8. **eigene Taschen** → **ihre eigenen Taschen** (Possessivpronomen fehlt)
9. **die Plastiktüten verboten ist** → **dass ein Verbot von Plastiktüten...ist** (Nebensatz mit "dass"; Nominalisierung "Verbot")

## GrammarFrame Focus

**Modal_Passiv_Position_2**

- Pattern: Modalverb (Position 2) + Subjekt + Partizip II + werden (Satzende)
- Example: sollten Plastiktüten verboten werden
- Anti: ist...sollen; sollen verbieten (Aktiv); Verb nicht Position 2
- Concept: modal-passive-main-clause-word-order
- Repeated error: user consistently puts verb in wrong position and forgets passive "werden"

**Adjektiv_nach_viel_Akk_mask**

- Pattern: viel + Adjektiv(-en stark) + N_m (Akk)
- Example: viel unnötigen Müll
- Anti: viel unnötig Müll (keine Endung)
- Concept: strong adjective declension after quantifier

**dass_Satz_nach_finde_ich**

- Pattern: finde ich, dass + Nebensatz
- Example: finde ich, dass ein Verbot sinnvoll ist
- Anti: finde ich Verbot ist sinnvoll
- Concept: subordinate clause after opinion verb

## Notes

Second attempt at plastic bag ban text. Same systematic errors repeated: verb position, modal passive construction, adjective declension after "viel", missing "dass" subordinate clause. User needs drill on main clause word order (V2) and modal+passive structure.
