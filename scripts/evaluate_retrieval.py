"""
Offline evaluation harness for retrieval quality (Applied AI).

Runs labeled tourism queries against the TF-IDF retriever and reports hit-rate.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from chatbot.retriever import KnowledgeRetriever

# query -> expected knowledge key substring
GOLD = [
    ("visa requirements for travel", "visa"),
    ("metro transport tips", "metro"),
    ("budget planning for a trip", "budget"),
    ("places to visit museums", "place"),
    ("packing list essentials", "packing"),
    ("hotel booking advice", "hotel"),
]


def main() -> None:
    r = KnowledgeRetriever()
    hits = 0
    rows = []
    for query, expected in GOLD:
        chunks = r.retrieve(query, top_k=3)
        keys = [c.key for c in chunks]
        ok = any(expected in k for k in keys) or any(expected in c.text.lower() for c in chunks)
        hits += int(ok)
        rows.append(
            {
                "query": query,
                "expected": expected,
                "top_keys": keys,
                "hit": ok,
                "top_score": round(chunks[0].score, 4) if chunks else 0.0,
            }
        )

    report = {
        "n": len(GOLD),
        "hits": hits,
        "hit_rate": round(hits / len(GOLD), 3),
        "cases": rows,
    }
    out = ROOT / "data" / "outputs"
    out.mkdir(parents=True, exist_ok=True)
    path = out / "retrieval_eval.json"
    path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
