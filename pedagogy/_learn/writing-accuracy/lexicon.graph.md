graph: writing-accuracy/lexicon
engine: gremlin-lite


# ingest-session 2026-11-13T12:24:38Z sprachkorrektur-sync lang=de
V Session_sprachkorrektur_sync kind=session date=2026-11-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-11-13-sprachkorrektur-sync.toon.md
V Sent_sprachkorrektur_sync_raw kind=sentence date=2026-11-13 lang=de role=raw
V Sent_sprachkorrektur_sync_fix kind=sentence date=2026-11-13 lang=de role=corrected
E Sent_sprachkorrektur_sync_fix FIXES Sent_sprachkorrektur_sync_raw
E Sent_sprachkorrektur_sync_raw FROM_SESSION Session_sprachkorrektur_sync
E Sent_sprachkorrektur_sync_fix FROM_SESSION Session_sprachkorrektur_sync
