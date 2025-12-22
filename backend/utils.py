def get_recommendations(skills, interests, dream):
    skills = skills.lower()
    interests = interests.lower()
    dream = dream.lower()
    results = []

    if "python" in skills or "coding" in interests:
        results.append("Software Developer")
    if "analysis" in interests or "excel" in skills:
        results.append("Data Analyst")
    if "design" in interests:
        results.append("UI/UX designer")
    if "machine learning" in interests and "artificial intelligence" in interests:
        results.append("AI/ML Engineer")
    if dream:
        results.append(f"Path to become a {dream.title()}")
    if not results:
        results = ["Explore different fields through internships"]
    return results
