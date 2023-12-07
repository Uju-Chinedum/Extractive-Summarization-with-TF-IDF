# Imports
from flask import Flask, request, jsonify
from summarization import extractive_summarization, abstractive_summarization
import os

# Variable Declaration
app = Flask(__name__)

# Function Definition


@app.route("/")
def hello():
    return "Hello, Welcome to this Summarizer"

@app.route("/summarize", methods=["POST"])
def run_summarization():
    data = request.json
    
    text = data["text"]
    sentences = data["sentences"]
    max_length = data["max_length"]
    min_length = data["min_length"]
    
    extractive = extractive_summarization(input_text=text, sentence_length=sentences)
    abstractive = abstractive_summarization(input_text=text, max_length=max_length, min_length=min_length)
    
    return jsonify({"extractive": extractive, "abstractive": abstractive})


# Body
if __name__ == "__main__":
    app.run(debug=True)
