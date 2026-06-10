from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

JD_TEXT = """
Senior AI Engineer

Candidate Matching
Candidate Ranking
Recommendation Systems
Retrieval Systems
Search Relevance
Embeddings
Vector Search
Behavioral Signals
Ranking Models
Information Retrieval
Machine Learning
Feature Engineering
Production ML
"""

# Encode JD only once
JD_EMBEDDING = model.encode(JD_TEXT)


def build_candidate_text(candidate):

    text = ""

    text += candidate["profile"].get(
        "headline", ""
    )

    text += " "

    text += candidate["profile"].get(
        "summary", ""
    )

    for role in candidate["career_history"]:

        text += " "

        text += role.get(
            "description", ""
        )

    return text


def semantic_score(candidate):

    candidate_text = build_candidate_text(
        candidate
    )

    candidate_embedding = model.encode(
        candidate_text
    )

    score = cosine_similarity(
        [JD_EMBEDDING],
        [candidate_embedding]
    )[0][0]

    return score * 100