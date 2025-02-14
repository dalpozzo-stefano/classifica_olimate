from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/classifica")
def get_classifica():
    if not os.path.exists("classifica.json"):
        return jsonify({"errore": "Nessun dato disponibile"}), 500
    
    with open("classifica.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
