from datetime import datetime


def experience_score(candidate):

    years = candidate["profile"]["years_of_experience"]

    if 5 <= years <= 9:
        return 100

    elif 3 <= years < 5:
        return 75

    elif 9 < years <= 12:
        return 75

    return 40


def open_to_work_score(candidate):

    return (
        100
        if candidate["redrob_signals"]["open_to_work_flag"]
        else 0
    )


def recruiter_score(candidate):

    return (
        candidate["redrob_signals"][
            "recruiter_response_rate"
        ]
        * 100
    )


def github_score(candidate):

    return candidate["redrob_signals"][
        "github_activity_score"
    ]


def interview_score(candidate):

    return (
        candidate["redrob_signals"][
            "interview_completion_rate"
        ]
        * 100
    )

RELEVANT_TERMS = [
    "retrieval",
    "ranking",
    "recommendation",
    "matching",
    "relevance",
    "vector",
    "embedding",
    "search",
    "personalization",
    "llm",
    "fine-tuning",
]

def career_relevance_score(candidate):

    text = ""

    text += (
        candidate["profile"]
        .get("headline", "")
        .lower()
    )

    text += " "

    text += (
        candidate["profile"]
        .get("summary", "")
        .lower()
    )

    for role in candidate["career_history"]:

        text += " "

        text += (
            role.get("description", "")
            .lower()
        )

    matches = 0

    for term in RELEVANT_TERMS:

        if term in text:
            matches += 1

    return (
        matches
        / len(RELEVANT_TERMS)
    ) * 100

AI_SKILLS = [
    "NLP",
    "Fine-tuning LLMs",
    "LoRA",
    "Milvus",
    "Vector Search",
    "Embeddings",
    "Information Retrieval",
    "Recommendation Systems",
    "Ranking",
    "Search",
    "PyTorch",
    "TensorFlow",
    "Transformers",
    "LLMs",
    "RAG",
]
def skill_relevance_score(candidate):

    skills = [
        skill["name"].lower()
        for skill in candidate["skills"]
    ]

    matches = 0

    for target in AI_SKILLS:

        if target.lower() in skills:
            matches += 1

    return (
        matches / len(AI_SKILLS)
    ) * 100
def notice_period_score(candidate):

    days = candidate["redrob_signals"][
        "notice_period_days"
    ]

    if days <= 30:
        return 100

    elif days <= 60:
        return 70

    return 40

TARGET_ROLES = [
    "recommendation",
    "search",
    "retrieval",
    "ranking",
    "ml engineer",
    "machine learning",
    "applied ai",
    "ai engineer",
    "nlp engineer",
]
def title_relevance_score(candidate):

    headline = (
        candidate["profile"]
        .get("headline", "")
        .lower()
    )

    matches = 0

    for role in TARGET_ROLES:

        if role in headline:
            matches += 1

    return (
        matches / len(TARGET_ROLES)
    ) * 100
HIGH_VALUE_ROLES = [
    "recommendation",
    "search engineer",
    "ml engineer",
    "machine learning",
    "ai research",
    "applied ml",
    "data scientist",
    "nlp engineer",
]

MEDIUM_VALUE_ROLES = [
    "data engineer",
    "backend engineer",
    "software engineer",
    "cloud engineer",
]

LOW_VALUE_ROLES = [
    "project manager",
    "business analyst",
]
def role_score(candidate):

    headline = (
        candidate["profile"]
        .get("headline", "")
        .lower()
    )

    for role in HIGH_VALUE_ROLES:
        if role in headline:
            return 100

    for role in MEDIUM_VALUE_ROLES:
        if role in headline:
            return 70

    for role in LOW_VALUE_ROLES:
        if role in headline:
            return 40

    return 10