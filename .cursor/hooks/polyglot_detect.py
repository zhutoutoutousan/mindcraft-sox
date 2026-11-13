#!/usr/bin/env python3
"""Shared polyglot language detection + code-switch gap heuristics."""
from __future__ import annotations

import re
from collections import Counter

# Proper nouns / tech allowlist — not treated as expression gaps.
ALLOW = {
    "todo",
    "repo",
    "api",
    "pr",
    "mcp",
    "cpu",
    "path",
    "url",
    "html",
    "pdf",
    "mp4",
    "json",
    "yaml",
    "git",
    "github",
    "cursor",
    "claude",
    "kiro",
    "aws",
    "bedrock",
    "laptop",  # borrowed noun used in DE; still allow as proper-ish tech
    "dump",
    "hook",
    "hooks",
    "skill",
    "skills",
    "agent",
    "agents",
    "prompt",
    "ontology",
    "graph",
    "vertex",
    "studio",
    "bilibili",
}

MARKERS: dict[str, set[str]] = {
    "de": {
        "der",
        "die",
        "das",
        "und",
        "ich",
        "nicht",
        "für",
        "fur",
        "auf",
        "mit",
        "ist",
        "ein",
        "eine",
        "einen",
        "einem",
        "eines",
        "lass",
        "lassen",
        "bitte",
        "aber",
        "oder",
        "auch",
        "noch",
        "schon",
        "wenn",
        "dann",
        "mir",
        "dir",
        "uns",
        "euch",
        "kein",
        "keine",
        "dieser",
        "diese",
        "dieses",
        "nach",
        "von",
        "zu",
        "im",
        "am",
        "zum",
        "zur",
        "heute",
        "jetzt",
        "projekt",
        "zustand",
        "änderung",
        "anderung",
        "gib",
        "mache",
        "mach",
        "liegt",
        "tauchen",
        "eintauchen",
        "vergessen",
        "dass",
        "daß",
        "danke",
        "hallo",
        "gut",
        "guten",
        "ja",
        "nein",
        "doch",
        "mal",
        "sehr",
        "mehr",
        "gern",
        "gerne",
        "muss",
        "kann",
        "kannst",
        "sind",
        "habe",
        "haben",
        "wird",
        "werden",
    },
    "en": {
        "the",
        "and",
        "for",
        "with",
        "please",
        "this",
        "that",
        "make",
        "give",
        "let",
        "lets",
        "don't",
        "dont",
        "not",
        "into",
        "from",
        "have",
        "has",
        "are",
        "is",
        "be",
        "do",
        "does",
        "can",
        "will",
        "would",
        "should",
        "about",
        "after",
        "before",
        "deeper",
        "update",
        "updated",
        "current",
        "state",
        "change",
        "changes",
        "today",
        "now",
        "project",
        "without",
        "but",
        "just",
        "also",
        "only",
    },
    "es": {
        "el",
        "la",
        "los",
        "las",
        "que",
        "para",
        "con",
        "una",
        "uno",
        "por",
        "como",
        "más",
        "mas",
        "está",
        "esta",
        "hay",
        "también",
        "tambien",
        "hoy",
        "ahora",
        "proyecto",
        "dame",
        "haz",
        "sin",
        "pero",
        "gracias",
        "necesito",
        "necesitas",
        "quiero",
        "puedes",
        "podría",
        "podrias",
        "fichero",
        "archivo",
        "trabajo",
        "hacer",
        "favor",
        "vale",
        "bueno",
        "muy",
        "tengo",
        "estoy",
        "todo",
        "aquí",
        "cosa",
    },
    "fr": {
        "le",
        "la",
        "les",
        "des",
        "un",
        "une",
        "et",
        "pour",
        "avec",
        "pas",
        "que",
        "qui",
        "dans",
        "sur",
        "est",
        "sont",
        "aujourd",
        "projet",
        "mais",
        "aussi",
    },
    # Distinctive function words only. Shared items (que, la, para) stay on
    # the language that already owned them so one overlap cannot flip primary.
    "it": {
        "non",
        "sono",
        "oggi",
        "anche",
        "questo",
        "questa",
        "perché",
        "perche",
        "io",
    },
    "pt": {
        "não",
        "nao",
        "você",
        "voce",
        "obrigado",
        "isso",
        "estou",
    },
    "fi": {
        "että",
        "etta",
        "minä",
        "mina",
        "tämä",
        "tama",
        "tänään",
        "tanaan",
        "mutta",
        "koska",
        "olen",
    },
    "vi": {
        "không",
        "khong",
        "tôi",
        "toi",
        "bạn",
        "ban",
        "này",
        "nay",
        "được",
        "duoc",
    },
    "ru": {
        "привет",
        "здравствуйте",
        "пожалуйста",
        "это",
        "что",
        "мне",
        "меня",
        "вы",
        "ты",
        "как",
        "сегодня",
        "сейчас",
        "не",
    },
}

# Roster learning languages. en / zh / wuu stay native and are not samples.
NONLATIN = ("ru", "el", "ar", "hi", "ja", "ko")
LATIN_LEARNING = ("de", "fr", "es", "it", "pt", "fi", "vi")
LEARNING = LATIN_LEARNING + NONLATIN

# Human 2026-11-09: these three are always a sample, one marker is enough.
# Other learning languages stay on the two-marker threshold and count only on demand.
ALWAYS_ACTIVE = ("es", "de", "ru")

# Latin, Cyrillic, Greek, Arabic, Devanagari, Kana, Hangul, CJK, or 内化-ed.
TOKEN_RE = re.compile(
    r"[A-Za-zÀ-ÿÄÖÜäöüß]+"
    r"|[\u0400-\u04FF]+"
    r"|[\u0370-\u03FF\u1F00-\u1FFF]+"
    r"|[\u0600-\u06FF]+"
    r"|[\u0900-\u097F]+"
    r"|[\u3040-\u30FF]+"
    r"|[\uAC00-\uD7AF]+"
    r"|[\u4e00-\u9fff]+(?:-[A-Za-z]+)?",
    re.UNICODE,
)

_SCRIPT_RX: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("ru", re.compile(r"[\u0400-\u04FF]")),
    ("el", re.compile(r"[\u0370-\u03FF\u1F00-\u1FFF]")),
    ("ar", re.compile(r"[\u0600-\u06FF]")),
    ("hi", re.compile(r"[\u0900-\u097F]")),
    ("ja", re.compile(r"[\u3040-\u30FF]")),
    ("ko", re.compile(r"[\uAC00-\uD7AF]")),
    ("zh", re.compile(r"[\u4e00-\u9fff]")),
)


def extract_prompt(data: object) -> str:
    """Pull user text from Cursor beforeSubmitPrompt JSON (prompt, nested content, parts)."""
    if isinstance(data, str):
        return data.strip()
    if not isinstance(data, dict):
        return ""
    for key in ("prompt", "text", "content", "user_prompt", "message", "query"):
        val = data.get(key)
        if isinstance(val, str) and val.strip():
            return val.strip()
        if isinstance(val, dict):
            inner = extract_prompt(val)
            if inner:
                return inner
        if isinstance(val, list):
            parts: list[str] = []
            for item in val:
                if isinstance(item, str) and item.strip():
                    parts.append(item.strip())
                elif isinstance(item, dict):
                    t = item.get("text") or item.get("content") or ""
                    if isinstance(t, str) and t.strip():
                        parts.append(t.strip())
            joined = "\n".join(parts).strip()
            if joined:
                return joined
    nested = data.get("input") or data.get("payload")
    if nested and nested is not data:
        inner = extract_prompt(nested)
        if inner:
            return inner
    msgs = data.get("messages")
    if isinstance(msgs, list) and msgs:
        last = msgs[-1]
        if isinstance(last, dict):
            inner = extract_prompt(last)
            if inner:
                return inner
        elif isinstance(last, str) and last.strip():
            return last.strip()
    return ""


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text or "")


def script_of(token: str) -> str | None:
    for lang, rx in _SCRIPT_RX:
        if rx.search(token):
            return lang
    return None


def score_langs(tokens: list[str]) -> Counter:
    scores: Counter = Counter()
    lower = [t.lower() for t in tokens]
    for lang, words in MARKERS.items():
        for t in lower:
            if t in words:
                scores[lang] += 1
    for raw in tokens:
        script = script_of(raw)
        if script:
            # Per token, not per character — a ZH stretch must not drown markers.
            scores[script] += 1
        elif re.search(r"[ÄÖÜäöüß]", raw):
            scores["de"] += 2
    return scores


def primary_lang(text: str, target: str = "de", default: str = "en") -> tuple[str, Counter]:
    tokens = tokenize(text)
    if not tokens:
        return default, Counter()
    scores = score_langs(tokens)
    if not scores:
        return default, Counter()
    # Highest learning-language score wins. A tie prefers the parked target,
    # then Russian and the other non-Latin roster languages, so they are not
    # dropped behind German, French, or Spanish.
    cands = [lang for lang in LEARNING if scores.get(lang, 0) >= 2]
    if cands:
        best = max(scores[lang] for lang in cands)
        top = [lang for lang in cands if scores[lang] == best]
        if target in top:
            return target, scores
        for lang in NONLATIN:
            if lang in top:
                return lang, scores
        return top[0], scores
    return scores.most_common(1)[0][0], scores


def also_langs(scores: Counter, primary: str) -> list[str]:
    """Other roster languages actually in the turn. Non-Latin first."""
    out: list[str] = []
    for lang in NONLATIN + LATIN_LEARNING:
        if lang == primary:
            continue
        need = 1 if lang in NONLATIN else 2
        if scores.get(lang, 0) >= need:
            out.append(lang)
    return out


def foreign_islands(
    text: str,
    primary: str,
    target: str,
    scores: Counter | None = None,
) -> list[dict]:
    """Sparse non-target tokens → expression gaps when the utterance attempts targetLang."""
    tokens = tokenize(text)
    lower = [t.lower() for t in tokens]
    scores = scores or Counter()
    target_score = scores.get(target, 0)
    primary_score = scores.get(primary, 0) or 1
    attempting_target = (
        primary == target
        or target_score >= 2
        or (target_score / primary_score) >= 0.35
    )
    if not attempting_target:
        return []

    gaps: list[dict] = []
    seen: set[str] = set()

    en_content = {
        "deeper",
        "update",
        "updated",
        "current",
        "state",
        "change",
        "changes",
        "please",
        "without",
        "after",
        "before",
        "today",
        "project",
        "make",
        "give",
        "lets",
        "don't",
        "dont",
        "dive",
        "diving",
        "forget",
        "remember",
        "list",
    }

    for raw, low in zip(tokens, lower):
        if low in ALLOW or (raw.isupper() and len(raw) <= 6):
            continue
        src = None
        script = script_of(raw)
        if script in NONLATIN:
            # A Russian (or el/ar/hi/ja/ko) word is its own sample, not a
            # missing French or German form.
            continue
        if script == "zh" or re.search(r"[\u4e00-\u9fff]", raw):
            src = "zh"
        else:
            for lang, words in MARKERS.items():
                if low in words and lang != target:
                    src = lang
                    break
            if src is None and low in en_content and target != "en":
                src = "en"
        if src is None or src == target:
            continue
        key = f"{src}:{low}"
        if key in seen:
            continue
        seen.add(key)
        gaps.append(
            {
                "surface": raw,
                "fromLang": src,
                "targetLang": target,
                "kind": "code_switch_gap",
                "meaning": "unknown-how-to-say-in-target",
            }
        )
    return gaps[:20]


def analyze(text: str, target: str = "de") -> dict:
    primary, scores = primary_lang(text, target=target, default="en")
    # Prefer the parked target only when the turn is otherwise native (en/zh).
    # Do not relabel a Russian or German sample as French because targetLang is fr.
    if (
        target in scores
        and primary in {"en", "zh"}
        and primary != target
        and (scores[target] >= 2 or scores[target] >= scores[primary] * 0.8)
    ):
        primary = target
    others = also_langs(scores, primary)
    gaps = foreign_islands(text, primary, target, scores)
    n = len(tokenize(text))
    method_hit = bool(n) and (
        any(scores.get(lang, 0) >= 1 for lang in ALWAYS_ACTIVE)
        or scores.get(target, 0) >= 2
        or any(scores.get(lang, 0) >= 2 for lang in LEARNING)
        or any(scores.get(lang, 0) >= 1 for lang in NONLATIN)
    )
    return {
        "primaryLang": primary,
        "targetLang": target,
        "alsoLangs": others,
        "scores": dict(scores),
        "gaps": gaps,
        "tokenCount": n,
        "mix": bool(gaps) or bool(others),
        "methodHit": method_hit,
    }
