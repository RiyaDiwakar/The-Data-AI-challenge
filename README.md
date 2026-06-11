# Candidate Ranker - The Data & AI Challenge

## Overview

This project was built for **The Data & AI Challenge**.

The goal is to rank candidates for a given job description by understanding semantic relevance, career history, skills, experience, and behavioral signals rather than relying solely on keyword matching.

The system combines:

* Candidate Retrieval
* Semantic Matching using Sentence Transformers
* Feature Engineering
* Hybrid Weighted Scoring
* Recruiter-style Reasoning Generation

The final output is a ranked shortlist of candidates that closely match the target role.

---

## Problem Statement

Traditional keyword-based candidate filtering often misses highly relevant candidates because it cannot understand context, experience, or semantic meaning.

This project addresses that challenge by:

1. Understanding the job description semantically.
2. Retrieving relevant candidates from a large dataset.
3. Computing semantic similarity between candidates and the job description.
4. Combining multiple recruiter-relevant signals into a final ranking score.
5. Generating explainable reasoning for every recommended candidate.

---

## Dataset

The provided dataset contains:

* Candidate Profiles
* Career History
* Skills
* Recruiter Activity Signals
* GitHub Signals
* Interview Signals
* Open-to-Work Signals

Dataset size:

* ~100,000 candidates

Note: The dataset is not included in this repository due to GitHub file size limitations.

Place the provided dataset files inside the `data/` folder before running the project.

---

## Project Architecture

Job Description
↓
Candidate Retrieval
↓
Semantic Matching
↓
Feature Engineering
↓
Hybrid Scoring
↓
Candidate Ranking
↓
Reasoning Generation
↓
Final Submission

---

## Retrieval Layer

The retrieval stage filters the candidate pool using domain-relevant keywords.

Example keywords:

* AI
* ML
* Machine Learning
* Recommendation
* Search
* Retrieval
* Ranking
* NLP
* Embeddings

This step reduces the search space and improves ranking efficiency.

Results:

* Total Candidates: 100,000
* Retrieved Candidates: 1,179

---

## Semantic Matching

The system uses:

Sentence Transformer:

`all-MiniLM-L6-v2`

Process:

1. Convert Job Description into an embedding.
2. Convert Candidate Profile into an embedding.
3. Compute cosine similarity.
4. Use similarity score as a ranking signal.

This allows the system to identify relevant candidates even when exact keywords do not match.

---

## Feature Engineering

The final ranking combines multiple signals:

### Semantic Score

Measures semantic similarity between candidate and job description.

### Career Relevance Score

Evaluates relevance of past work experience.

### Skill Relevance Score

Measures overlap between candidate expertise and role requirements.

### Title Relevance Score

Compares current title against target role.

### Experience Score

Evaluates years and depth of experience.

### GitHub Score

Rewards technical engagement and public contributions.

### Recruiter Score

Incorporates recruiter activity signals.

### Interview Score

Uses interview-related indicators.

### Open-to-Work Score

Considers candidate availability.

---

## Scoring Formula

Final Score =

* Semantic Score × 0.35
* Career Relevance × 0.25
* Skill Relevance × 0.15
* Title Relevance × 0.10
* Experience × 0.05
* GitHub × 0.04
* Recruiter × 0.03
* Interview × 0.02
* Open-to-Work × 0.01

---

## Results

Pipeline Performance:

* Total Candidates: 100,000
* Retrieved Candidates: 1,179
* Final Ranked Candidates: Top 100

Execution Time:

* Approximately 106 seconds

Example Top Results:

| Rank | Candidate ID | Score |
| ---- | ------------ | ----- |
| 1    | CAND_0018499 | 59.61 |
| 2    | CAND_0002025 | 59.34 |
| 3    | CAND_0039754 | 58.91 |
| 4    | CAND_0049538 | 58.20 |
| 5    | CAND_0088025 | 57.08 |

---

## Repository Structure

candidate-ranker/

├── data/

├── docs/

├── notebooks/

├── outputs/

│ ├── final_rankings.csv

│ └── final_submission.csv

├── src/

│ ├── retrieval.py

│ ├── semantic_matching.py

│ ├── feature_engineering.py

│ ├── scoring.py

│ ├── reasoning.py

│ ├── rank_candidates.py

│ └── generate_submission.py

├── README.md

├── requirements.txt

└── .gitignore

---

## Installation

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Generate rankings:

```bash
python src/rank_candidates.py
```

Generate final submission:

```bash
python src/generate_submission.py
```

Output file:

```text
outputs/final_submission.csv
```

---

## Future Improvements

* Dense Vector Retrieval using FAISS
* Hybrid BM25 + Embedding Search
* Cross-Encoder Re-ranking
* LLM-based Candidate Reasoning
* Learning-to-Rank Models
* Personalized Recruiter Preferences
* Real-time Candidate Recommendations

---

## Author

Riya Diwakar

Project Submission for The Data & AI Challenge
