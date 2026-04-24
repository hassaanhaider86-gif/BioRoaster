from flask import Flask, request, jsonify, render_template_string
import random

app = Flask(__name__)

ROAST_TEMPLATES = [
    "Wow, '%s' — sounds like you invented being average.",
    "'%s'... LinkedIn called, they want their buzzwords back.",
    "Ah yes, '%s' — the universal sign of someone who loves saying a lot without saying anything.",
    "'%s' — impressive, if this were 2012.",
    "Reading '%s' feels like eating plain toast with no butter.",
    "'%s' — did ChatGPT write this or did you?",
    "'%s' — bold of you to assume this stands out.",
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Bio Roaster 🔥</title>
    <style>
        body { font-family: Arial; max-width: 600px; margin: 50px auto; }
        textarea { width: 100%; height: 100px; }
        button { padding: 10px 20px; margin-top: 10px; }
        .result { margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <h1>🔥 LinkedIn Bio Roaster</h1>
    <form method="post">
        <textarea name="bio" placeholder="Paste your bio here..."></textarea><br>
        <button type="submit">Roast Me</button>
    </form>
    {% if roast %}
        <div class="result">{{ roast }}</div>
    {% endif %}
</body>
</html>
"""

def generate_roast(bio):
    template = random.choice(ROAST_TEMPLATES)
    return template % bio

@app.route("/", methods=["GET", "POST"])
def home():
    roast = None
    if request.method == "POST":
        bio = request.form.get("bio", "")
        if bio:
            roast = generate_roast(bio)
    return render_template_string(HTML_TEMPLATE, roast=roast)

@app.route("/api/roast", methods=["POST"])
def api_roast():
    data = request.json
    bio = data.get("bio", "")
    if not bio:
        return jsonify({"error": "No bio provided"}), 400

    roast = generate_roast(bio)
    return jsonify({"roast": roast})

if __name__ == "__main__":
    app.run(debug=True)
