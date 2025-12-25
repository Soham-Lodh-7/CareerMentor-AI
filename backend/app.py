from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from google.genai.errors import ClientError
import os
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise Exception(
        "No API key found! Make sure GEMINI_API_KEY is set in .env or environment variables."
    )

client = genai.Client(api_key=API_KEY)

app = Flask(__name__)
CORS(app, resources={r"/recommend": {"origins": "*"}})


def get_ai_recommendations(skills, interests, dream):
    prompt = f"""
    The user's details:
    Skills: {skills}
    Interests: {interests}
    Dream Career: {dream}

    Generate EXACTLY 5 career recommendations in JSON format like this:
    [
      {{
        "title": "...",
        "reason": "...",
        "future_scope": "...",
        "difficulty": "Easy/Medium/Hard"
      }}
    ]
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt]
        )

        ai_text = response.candidates[0].content.parts[0].text

        ai_text = ai_text.strip()
        if ai_text.startswith("```json"):
            ai_text = ai_text[len("```json"):].strip()
        if ai_text.endswith("```"):
            ai_text = ai_text[:-3].strip()

        return json.loads(ai_text)

    except ClientError as e:
        print("Gemini API Error:", e)
        return []
    except json.JSONDecodeError:
        print("AI returned invalid JSON:")
        print(ai_text)
        return []


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    name = data.get("name")
    skills = data.get("skills")
    interests = data.get("interests")
    dream = data.get("dream")

    result = get_ai_recommendations(skills, interests, dream)

    return jsonify({"name": name, "recommendations": result})


if __name__ == "__main__":
    app.run(debug=True)
