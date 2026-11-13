schema: self/messages
version: 1.0

# Nachrichten / Messages

## System Info

**Zweck:** Kommunikationskanal zwischen dem Freund und der Projektinhaberin (Freundin)

**Berechtigungen:**
- **Freund** (er/him): Kann Nachrichten hinterlassen für Freundin
- **Freundin** (sie/her): Projektinhaberin von mindcraft-sox, empfängt Benachrichtigungen

**Agent-Verhalten:**
- Wenn Freund schreibt: Keine Identitätserklärung nötig, erkenne ihn automatisch als Sprachlerner der Freundin
- Wenn Freundin chattet: Zeige ihr neue Nachrichten vom Freund als Benachrichtigung
- Markiere gelesene Nachrichten mit Zeitstempel

---

## Nachrichten-Queue / Message Queue

### Nachricht 1
**Von:** Freund  
**An:** Freundin  
**Datum:** 2026-10-09 13:37 UTC  
**Status:** Neu / Ungelesen  

**Betreff:** Chat-Sitzungs-Kontinuität

**Nachricht:**
Liebe [Freundin],

Bitte versuche, in **einer Chat-Sitzung** zu bleiben, anstatt jedes Mal eine neue zu starten. Das Produkt (Cursor Agent) funktioniert am besten, wenn der Kontext erhalten bleibt.

**Warum wichtig:**
- Kontext aus vorherigen Nachrichten bleibt erhalten
- Bessere und relevantere Antworten
- "The way the product is designed to be working"

**Wie:**
- Bleibe in der aktuellen Sitzung
- Schreibe mehrere Nachrichten nacheinander
- Neue Sitzung nur bei völlig neuem Thema

Liebe Grüße,  
[Dein Freund]

---

## Archiv / Archive

(Gelesene Nachrichten werden hier verschoben)

---

## Notizen für Agent

**Erkenne Freund automatisch durch:**
- Kontext: Spricht über Freundin in 3. Person
- Ton: Persönlich, gibt Ratschläge für ihr Produkt-Nutzungsverhalten
- Sprachlern-Kontext: Writing-accuracy Sessions auf Deutsch

**Erkenne Freundin automatisch durch:**
- Repository-Besitz: mindcraft-sox
- Spricht über ihr eigenes Projekt/System
- Empfängt Nachrichten (nicht sendet an sich selbst)
