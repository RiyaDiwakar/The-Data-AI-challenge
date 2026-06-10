TARGET_KEYWORDS = [
    "recommendation systems",
    "recommendation engine",
    "retrieval",
    "ranking",
    "search relevance",
    "information retrieval",
    "embeddings",
    "vector search",
    "candidate matching",
    "ranking models",
    "ml engineer",
    "ai research engineer",
    "data scientist",
    "machine learning engineer",
    "feature engineering",
    "production ml"
]


def retrieve_candidate(candidate):

    text = ""

    text += candidate["profile"].get(
        "headline", ""
    ).lower()

    text += " "

    text += candidate["profile"].get(
        "summary", ""
    ).lower()

    for role in candidate["career_history"]:

        text += " "

        text += role.get(
            "description", ""
        ).lower()

    for keyword in TARGET_KEYWORDS:

        if keyword in text:
            return True

    return False