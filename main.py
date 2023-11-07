# Imports
from flask import Flask, request, jsonify
from summarization import summarize_text
import os

# Variable Declaration
app = Flask(__name__)
host = os.environ.get("")

# Function Definition


@app.route("/summarize", methods=["POST"])
def run_summarization():
    data = request.json
    text = data["text"]
    summary = summarize_text(text)
    return jsonify({"summary": summary})


# Body
if __name__ == "__main__":
    app.run(debug=True)
