import re

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

def extract_jd_requirements(jd_text=JD_TEXT):

    lines = [
        line.strip()
        for line in jd_text.split("\n")
        if line.strip()
    ]

    role = lines[0]

    skills = lines[1:]

    return {
        "role": role,
        "skills": skills
    }


if __name__ == "__main__":

    result = extract_jd_requirements()

    print("Role:", result["role"])

    print("\nSkills:")

    for skill in result["skills"]:
        print("-", skill)