#!/usr/bin/env python3
"""Find existing Growee Skills from natural-language task aliases."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALIAS_PATH = ROOT / "catalog" / "task-aliases.json"


def normalize(value: str) -> str:
    return " ".join(re.findall(r"[\w]+", value.casefold(), flags=re.UNICODE))


def score(query: str, job: dict) -> int:
    normalized_query = normalize(query)
    candidates = [
        job["id"],
        job["title_en"],
        job["title_zh"],
        *job["queries_en"],
        *job["queries_zh"],
    ]
    normalized_candidates = [normalize(candidate) for candidate in candidates]
    if normalized_query in normalized_candidates:
        return 100

    best = 0
    query_tokens = set(normalized_query.split())
    for candidate in normalized_candidates:
        if not candidate:
            continue
        if normalized_query in candidate or candidate in normalized_query:
            best = max(best, 60)
        candidate_tokens = set(candidate.split())
        overlap = len(query_tokens & candidate_tokens)
        if overlap:
            best = max(best, overlap * 10)
    return best


def find(query: str, limit: int = 5) -> list[dict]:
    catalog = json.loads(ALIAS_PATH.read_text(encoding="utf-8"))
    matches = []
    for job in catalog["jobs"]:
        match_score = score(query, job)
        if match_score >= 20:
            matches.append({"score": match_score, **job})
    matches.sort(key=lambda item: (-item["score"], item["id"]))
    return matches[:limit]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Find Growee Skills by describing the user task."
    )
    parser.add_argument("query", help="Natural-language task in English or Chinese")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    matches = find(args.query, args.limit)
    if args.as_json:
        print(json.dumps(matches, ensure_ascii=False, indent=2))
    else:
        for match in matches:
            related = ", ".join(match["related_skills"]) or "none"
            print(f'{match["primary_skill"]}\t{match["title_en"]}')
            print(f'  中文：{match["title_zh"]}')
            print(f"  Related: {related}")
    return 0 if matches else 1


if __name__ == "__main__":
    raise SystemExit(main())
