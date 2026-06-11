def generate_reasoning(candidate):

    title = candidate["profile"].get(
        "current_title",
        "Professional"
    )

    summary = candidate["profile"].get(
        "summary",
        ""
    )

    experience = candidate.get(
        "total_experience_years",
        "multiple"
    )

    reasoning = (
        f"{title} demonstrates strong alignment with the role through "
        f"{experience} years of experience and relevant expertise in "
        f"AI, machine learning, retrieval, ranking, and production ML systems. "
        f"The candidate's profile highlights practical experience building "
        f"search, recommendation, or data-driven solutions that closely match "
        f"the requirements of the target position."
    )

    return reasoning