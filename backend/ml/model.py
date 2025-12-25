import google.generativeai as genai

def generate_recommendations(interests, skills, dream):
    prompt = f"""
    You are an expert career advisor.
    The user has given:

    Interests: {interests}
    Skills: {skills}
    Dream Career Area: {dream}

    Give 4 highly relevant and realistic career recommendations.
    For each recommendation give:

    1. Job Title
    2. Why it fits the user
    3. What skills they need to improve

    Output in clean JSON format:
    [
      {{
        "title": "...",
        "reason": "...",
        "improvements": "..."
      }}
    ]
    """

    try:
        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
        return response.text
    except Exception as e:
        return {"error": str(e)}
