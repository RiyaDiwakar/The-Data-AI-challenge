# Candidate Ranker – The Data & AI Challenge

## AI-Powered Candidate Ranking System

An intelligent candidate ranking system designed to identify the most relevant candidates for a job description using semantic understanding, recruiter signals, and hybrid scoring.

Instead of relying solely on keyword matching, the system evaluates candidate relevance using career history, experience, profile information, recruiter activity, interview signals, GitHub engagement, and semantic similarity.

---

## Challenge Objective

Traditional recruitment systems often miss strong candidates because they depend heavily on exact keyword matching.

This project aims to replicate how an experienced recruiter evaluates talent by:

* Understanding job requirements semantically
* Evaluating complete candidate profiles
* Considering multiple hiring signals
* Ranking candidates based on overall fit
* Providing explainable recommendations

---

## Key Results

| Metric                     | Value            |
| -------------------------- | ---------------- |
| Total Candidates Processed | 100,000          |
| Retrieved Candidates       | 1,179            |
| Final Recommendations      | Top 100          |
| Embedding Model            | all-MiniLM-L6-v2 |
| Ranking Strategy           | Hybrid Scoring   |
| Execution Time             | ~106 seconds     |

---

## Solution Architecture

```text
┌─────────────────────┐
│ Job Description     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Candidate Retrieval │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Semantic Matching   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Feature Engineering │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Hybrid Scoring      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Reasoning Engine    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Top Candidate List  │
└─────────────────────┘
```

---

## Dataset Overview

The provided dataset contains approximately 100,000 candidate profiles.

Available information includes:

* Candidate Profiles
* Professional Summaries
* Career History
* Skills
* Recruiter Activity Signals
* Interview Signals
* GitHub Signals
* Open-to-Work Indicators

**Note:** Dataset files are excluded from this repository due to GitHub file size limitations.

Place all provided challenge datasets inside the `data/` directory before running the project.

---

## Candidate Retrieval Layer

To improve efficiency, an initial retrieval stage filters candidates using domain-specific recruitment keywords.

Examples include:

* Machine Learning
* AI Engineer
* Recommendation Systems
* Search Relevance
* Retrieval Systems
* Embeddings
* Ranking Models
* Information Retrieval
* Production ML

This reduces the search space from:

```text
100,000 Candidates
        ↓
1,179 Retrieved Candidates
```

allowing semantic ranking to operate on a focused candidate pool.

---

## Semantic Matching

The system uses Sentence Transformers to understand semantic similarity between the job description and candidate profiles.

### Model

```text
all-MiniLM-L6-v2
```

### Process

1. Encode Job Description
2. Encode Candidate Profile
3. Generate Dense Embeddings
4. Compute Cosine Similarity
5. Use Similarity Score as Ranking Signal

This enables matching based on meaning rather than exact keywords.

---

## Feature Engineering

The ranking engine combines multiple candidate signals.

### Semantic Score (35%)

Measures semantic similarity between candidate profile and job description.

### Career Relevance Score (25%)

Evaluates relevance of professional experience.

### Skill Relevance Score (15%)

Measures alignment between candidate expertise and role requirements.

### Title Relevance Score (10%)

Compares candidate title against target role.

### Experience Score (5%)

Rewards depth and maturity of experience.

### GitHub Score (4%)

Captures technical engagement and contribution signals.

### Recruiter Score (3%)

Incorporates recruiter interaction indicators.

### Interview Score (2%)

Uses interview-related activity signals.

### Open-to-Work Score (1%)

Reflects candidate availability.

---

## Hybrid Scoring Formula

```text
Final Score =

0.35 × Semantic Score
+ 0.25 × Career Relevance
+ 0.15 × Skill Relevance
+ 0.10 × Title Relevance
+ 0.05 × Experience
+ 0.04 × GitHub
+ 0.03 × Recruiter Signals
+ 0.02 × Interview Signals
+ 0.01 × Open-to-Work Signals
```

---

## Explainable Reasoning

Each recommended candidate includes a recruiter-style explanation describing why the candidate is relevant.

Example:

> Senior Machine Learning Engineer demonstrates strong alignment with the role through experience in retrieval systems, ranking models, search relevance, and embedding-based search. The profile highlights relevant production AI/ML work and capabilities closely matching the job requirements.

This improves transparency and recruiter trust.

---

## Example Results

| Rank | Candidate ID | Score |
| ---- | ------------ | ----- |
| 1    | CAND_0018499 | 59.61 |
| 2    | CAND_0002025 | 59.34 |
| 3    | CAND_0039754 | 58.91 |
| 4    | CAND_0049538 | 58.20 |
| 5    | CAND_0088025 | 57.08 |

---

## Challenge Requirement Coverage

This solution satisfies all core challenge objectives:

- Understands job descriptions semantically

- Evaluates complete candidate profiles

- Uses semantic search and ranking

- Combines recruiter and behavioral signals

- Produces explainable recommendations

- Generates a recruiter-ready ranked shortlist

---

## Repository Structure

```text
candidate-ranker/

├── data/
├── docs/
├── notebooks/
├── outputs/
│   ├── final_rankings.csv
│   └── final_submission.csv
├── src/
│   ├── retrieval.py
│   ├── semantic_matching.py
│   ├── feature_engineering.py
│   ├── scoring.py
│   ├── reasoning.py
│   ├── rank_candidates.py
│   └── generate_submission.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

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

Output:

```text
outputs/final_submission.csv
```

---

## Future Improvements

* FAISS Vector Retrieval
* Hybrid BM25 + Dense Retrieval
* Cross-Encoder Re-ranking
* Learning-to-Rank Models
* LLM-Based Candidate Explanations
* Personalized Recruiter Preferences
* Real-Time Candidate Recommendations

---

## Author

**Riya Diwakar**

Submission for **The Data & AI Challenge**
