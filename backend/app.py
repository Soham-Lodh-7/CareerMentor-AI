from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app, resources={r"/recommend": {"origins": "http://127.0.0.1:3000"}})

from ml.model import generate_recommendations

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    name = data.get("name", "")
    interests = data.get("interests", "")
    skills = data.get("skills", "")
    dream = data.get("dream", "")
    results = generate_recommendations(interests, skills, dream)
    return jsonify({
        "status": "success",
        "name": name,
        "recommendations": results
    })

if __name__ == "__main__":
    app.run(debug=True)
