schema: writing-accuracy/session
date: 2026-10-09
primaryLang: de
context: requesting-communication-channel-system

## Raw

Also als iherer Freund hätte ich gerne, dass es gibt ein Kommunikationskanal von mich zu sie, also wenn jemand ohne solche "Ich bin ihrer Freund" Erklärung wahrscheinlich ist die Sprachler meiner Freundin ja. Wann meine Freundin, die Inhalber von dieser projekt mindcraft-sox ist, etwas zu dir fragt, danach kriegt sie Benarichtigungen von mir ja

## Minimal rewrite

Also als ihr Freund hätte ich gerne, dass es einen Kommunikationskanal von mir zu ihr gibt. Wenn jemand ohne eine solche "Ich bin ihr Freund"-Erklärung schreibt, ist das wahrscheinlich der Sprachlerner meiner Freundin. Wenn meine Freundin, die Inhaberin von diesem Projekt mindcraft-sox, etwas zu dir fragt, bekommt sie danach Benachrichtigungen von mir.

## Errors

### E1: Possessivpronomen maskulin Nominativ (WIEDERKEHREND) [POSSESSIVE_CASE_GENDER]
- Raw: `als iherer Freund`
- Fix: `als ihr Freund`
- Frame: Possessiv "ihr" (= her) + maskulin Nominativ → **keine Endung**
- Note: **ZWEITES MAL in dieser Session!** Gleicher Fehler wie in vorheriger Nachricht
- Escalation: Dieser Fehler kehrt zurück → sofortige Übung + wiederholende Übungen (+1/+3/+7 Tage)

**Deklination "ihr" (= her) wiederholt:**
| Kasus | maskulin | feminin | neutrum |
|-------|----------|---------|---------|
| Nom | ihr Freund | ihre Freundin | ihr Kind |
| Akk | ihren Freund | ihre Freundin | ihr Kind |
| Dat | ihrem Freund | ihrer Freundin | ihrem Kind |

### E2: Personalpronomen im Dativ [PERSONAL_PRONOUN_CASE]
- Raw: `von mich zu sie`
- Fix: `von mir zu ihr`
- Frame: Präpositionen "von" und "zu" verlangen **Dativ**
- Note: ich → **mir** (nicht "mich"); sie → **ihr** (nicht "sie")

**Personalpronomen Dativ:**
| Nominativ | Akkusativ | Dativ |
|-----------|-----------|-------|
| ich | mich | mir |
| du | dich | dir |
| er | ihn | ihm |
| sie | sie | ihr |
| wir | uns | uns |
| ihr | euch | euch |
| sie | sie | ihnen |

### E3: Wortstellung bei "es gibt" [WORD_ORDER_EXPLETIVE]
- Raw: `dass es gibt ein Kommunikationskanal`
- Fix: `dass es einen Kommunikationskanal gibt`
- Frame: In Nebensatz mit "dass" → Verb am Ende; "es gibt" + **Akkusativ**
- Note: "gibt" steht am Ende des Nebensatzes; "ein" → "einen" (Akkusativ maskulin)

**Struktur:**
- Hauptsatz: Es gibt einen Kanal.
- Nebensatz: ..., **dass** es einen Kanal **gibt**.

### E4: Demonstrativpronomen + Genus [DEMONSTRATIVE_GENDER_CASE]
- Raw: `ohne solche ... Erklärung` (ok) aber `von dieser projekt`
- Fix: `von diesem Projekt`
- Frame: **das** Projekt (neutrum) + Dativ → **diesem** Projekt
- Note: "dieser" ist feminin/Dativ oder maskulin/feminin/Genitiv; nicht neutrum Dativ

**Demonstrativ "dieser" im Dativ:**
| Genus | Dativ |
|-------|-------|
| maskulin | diesem Mann |
| feminin | dieser Frau |
| neutrum | diesem Projekt |

### E5: Genus des Nomens [NOUN_GENDER]
- Raw: `die Sprachler` (mask. als feminin behandelt)
- Fix: `der Sprachlerner`
- Frame: **der** Lerner (maskulin), nicht "die Lerner" (die wäre Plural oder feminin Singular)
- Note: -er Endung oft maskulin (der Lehrer, der Arbeiter, der Lerner)

### E6: Genus des Nomens + Genuskongruenz [NOUN_GENDER]
- Raw: `die Inhalber`
- Fix: `die Inhaberin`
- Frame: Für Frauen: **die Inhaberin** (feminin mit -in Suffix), nicht "die Inhalber"
- Note: "der Inhaber" (Mann), "die Inhaberin" (Frau)

### E7: Temporale Konjunktion "wenn" vs "wann" [CONJUNCTION_CHOICE]
- Raw: `Wann meine Freundin ... fragt`
- Fix: `Wenn meine Freundin ... fragt`
- Frame: **"Wenn"** = conditional/whenever; **"Wann"** = when (question)
- Note: "Wann kommst du?" (Frage); "Wenn du kommst, ..." (Bedingung)

### E8: Verb-Wahl Register [LEXIS_VERB_REGISTER]
- Raw: `kriegt sie Benarichtigungen` (+ Rechtschreibfehler)
- Fix: `bekommt sie Benachrichtigungen` oder `erhält sie Benachrichtigungen`
- Frame: "kriegen" ist umgangssprachlich; "bekommen" oder "erhalten" formeller/passender
- Note: "Benachrichtigungen" (nicht "Benarichtigungen")

### E9: Partikel "ja" am Satzende [PARTICLE_USAGE]
- Raw: `von mir ja` (am Ende)
- Fix: kein "ja" nötig, oder "von mir."
- Frame: "ja" als Bestätigungspartikel mitten im Satz OK, aber am Ende eines Aussagesatzes ungewöhnlich
- Note: "ja" hier nicht falsch, aber stilistisch überflüssig

## GrammarFrame focus

**Personalpronomen: Nominativ vs. Akkusativ vs. Dativ**

Präpositionen verlangen bestimmte Fälle. "von" und "zu" verlangen **immer Dativ**.

**Häufige Präpositionen mit Dativ:**
| Präposition | Beispiel | Warum |
|-------------|----------|-------|
| von | von **mir** | ich → mir |
| zu | zu **dir** | du → dir |
| mit | mit **ihm** | er → ihm |
| bei | bei **ihr** | sie → ihr |
| nach | nach **uns** | wir → uns |
| aus | aus **ihnen** | sie (Plural) → ihnen |

**Nicht verwechseln:**
- **Akkusativ (für/gegen/ohne):** für **mich**, ohne **dich**, gegen **ihn**
- **Dativ (von/zu/mit/bei):** von **mir**, zu **dir**, mit **ihm**

### Merksatz
**"von" und "zu" = Dativ → mir/dir/ihm/ihr/uns/euch/ihnen**

## Context
User (boyfriend) wants to set up a communication channel to his girlfriend (project owner of mindcraft-sox) so he doesn't need to explain his identity every time. He wants her to receive notifications from him when she chats. Multiple recurring errors: possessive pronouns (second time!), personal pronouns in dative, word order, and noun gender.

## Error Escalation

**Recurring error detected:** `ihrer Freund` → `ihr Freund`

This is the **second occurrence** in today's sessions (also appeared in 2026-10-09-girlfriend-chat-reminder.toon.md).

**Action required per method.toon.md errorEscalation:**
1. Sofortige Übung heute (immediate drill)
2. Wiederholende Übungen: +1 Tag, +3 Tage, +7 Tage (spaced repetition)
3. Lesen: Frame + lexicon Form review
4. Video + Probe: spoken back-and-forth until vollständiges Verständnis
5. Exit only when learner confirms mastery

**Agent must NOT:**
- Mark this as resolved automatically
- Invent ANSWER or mastery claim
- Skip the escalation loop
