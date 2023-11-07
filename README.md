# Extractive Summarization with TF-IDF

This project provides a basic extractive summarizing service based on the Term Frequency-Inverse Document Frequency (TF-IDF) algorithm. The project includes of three primary files: `summarization.py`, `main.py`, and `requirements.txt`.

## **`requirements.txt`**

### ***Description for `requirements.txt`***

The needed Python libraries and their versions are listed in `requirements.txt`. You may use `pip` with the `-r` flag to install these dependencies.

### ***Prerequisites For This Project***

Before using this project, make sure you have Python 3.x installed, and install the required dependencies using the command provided below

### ***Installation***

```sh
pip install -r requirements.txt
```

## **`summarization.py`**

### ***Description for `summarization.py`***

The summarization.py Python package offers a method for summarizing text using the TF-IDF algorithm. The function accepts a text input and provides a summary with the amount of sentences you specify.

### ***Usage for `summarization.py`***

1. Download the relevant NLTK data and import the appropriate libraries.
2. To summarize a given input text, use the summarize_text(input_text, summary_length) function.
3. The summary is returned as a string by the summarize_text function.

### ***Example for `summarization.py`***

```py
from summarization import summarize_text

input_text = "Your long input text goes here..."
summary = summarize_text(input_text, summary_length=3)  # default is 7
print(summary)
```

## **`main.py`**

### ***Description for `main.py`***

`main.py` is an API service written in Flask that exposes the summarizing feature as a web service. It watches for HTTP POST requests with JSON data and delivers the summary result in JSON format.

### ***Usage for `main.py`***

1. Import the required libraries.
2. Make a Flask app.
3. Define a `/summarize` route that waits for POST requests.
4. Extract the input text from the request's JSON data.
5. To construct the summary, use the summarize_text function from summarization.py.
6. Return the summary in the form of a JSON response.

### ***Example for `main.py`***

To run the API service use the following command in your terminal:

```sh
python main.py
```

You can make a POST request to the /summarize endpoint with a JSON payload containing the input text to get the summarization result.

## **API Documentation**

### Endpoint

- **POST /summarize**: This endpoint accepts a JSON payload with the following structure:

  ```json
  {
    "text": "Your long input goes here..."
  }
  ```

### Response

The endpoint returns a JSON response with the summarization result:

  ```json
  {
    "summary": "The summarized text..."
  }
  ```

## **How to Use the API**

1. Start the API service by running `main.py` or using the production url `https://www.savadow.pythonanywhere.com`.
2. Send a POST request to the /summarize endpoint with a JSON payload containing the input text to be summarized.
3. Receive the summary as a JSON response.

### ***Example POST request using `curl`***

```sh
curl -X POST -H "Content-Type: application/json" -d '{"text": "Your long input text goes here..."}' http://localhost:5000/summarize
```

## Author

This project was built by [me](github.com/Uju-Chinedum) and [Khay](github.com/Khay-dev)
