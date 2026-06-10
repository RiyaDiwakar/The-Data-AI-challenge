from feature_engineering import (
    title_relevance_score,
    experience_score,
    open_to_work_score,
    recruiter_score,
    github_score,
    interview_score,
    career_relevance_score,
    skill_relevance_score,
    
)
from semantic_matching import semantic_score
def calculate_score(candidate):

    score = (
        semantic_score(candidate) * 0.35
        + career_relevance_score(candidate) * 0.25
        + skill_relevance_score(candidate) * 0.15
        + title_relevance_score(candidate) * 0.10
        + experience_score(candidate) * 0.05
        + github_score(candidate) * 0.04
        + recruiter_score(candidate) * 0.03
        + interview_score(candidate) * 0.02
        + open_to_work_score(candidate) * 0.01
    )

    return round(score, 2)