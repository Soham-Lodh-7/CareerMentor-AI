from flask import Flask, request, jsonify
from flask_cors import CORS
import utils

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend_career():
    data = request.get_json()
    name = data.get("name")
    skills = data.get("skills", "")
    interests = data.get("interests", "")
    dream = data.get("dream", "")
    recommendations = utils.get_recommendations(skills, interests, dream)
    return jsonify({"career": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
