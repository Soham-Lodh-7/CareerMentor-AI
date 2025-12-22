def generate_recommendations(interests, skills, dream):
    recommendations = []
    interests = interests.lower()
    skills = skills.lower()
    dream = dream.lower()

    career_map = {
        "Software Engineer": ["technology", "coding", "programming", "developer"],
        "UI/UX Designer": ["design", "creative", "ui", "ux", "art"],
        "Data Scientist": ["data", "analytics", "machine learning", "python"],
        "Business Analyst": ["business", "management", "strategy", "analytics"],
        "Marketing / Content Strategist": ["communication", "marketing", "content", "public speaking"],
        "Researcher / Scientist": ["research", "science", "laboratory", "analysis"],
        "Entrepreneur / Startup": ["startup", "entrepreneur", "innovation", "business"]
    }

    for career, keywords in career_map.items():
        score = 0
        for kw in keywords:
            if kw in interests or kw in skills or kw in dream:
                score += 1
        if score > 0:
            recommendations.append({
                "title": career,
                "reason": f"Matched {score} keywords from your profile indicating suitability for {career}."
            })

    if len(recommendations) == 0:
        recommendations.append({
            "title": "Career Counselor Consultation Recommended",
            "reason": "Your profile suggests multiple possibilities; consider personalized guidance."
        })
    return recommendations
