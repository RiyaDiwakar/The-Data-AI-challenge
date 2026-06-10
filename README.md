# Candidate Ranking System

## Objective
Rank candidates for a Senior AI Engineer role from 100,000 profiles.

## Approach

### Retrieval Stage
- Keyword-based filtering
- Reduced pool from 100,000 to 1,179 candidates

### Semantic Matching
- Model: all-MiniLM-L6-v2
- Cosine similarity between JD and candidate profile

### Feature Engineering
- Semantic Similarity: 35%
- Career Relevance: 25%
- Skill Relevance: 15%
- Title Relevance: 10%
- Experience: 5%
- GitHub Activity: 4%
- Recruiter Signals: 3%
- Interview Signals: 2%
- Open-to-Work Signal: 1%

### Final Ranking
Candidates sorted by weighted score.