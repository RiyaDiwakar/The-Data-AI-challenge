import json

from retrieval import retrieve_candidate
from scoring import calculate_score


def rank_candidates():

    ranked = []

    with open(
        "../data/candidates.jsonl",
        "r",
        encoding="utf-8"
    ) as f:

        for line in f:

            candidate = json.loads(line)

            if not retrieve_candidate(candidate):
                continue

            score = calculate_score(candidate)

            ranked.append({
                "candidate_id": candidate["candidate_id"],
                "score": score,
                "title": candidate["profile"]["current_title"]
            })

    ranked = sorted(
        ranked,
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked