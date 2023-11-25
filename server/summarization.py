# Imports
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Download NLTK data for tokenization and stopwords
nltk.download('punkt')
nltk.download('stopwords')

# Function Definition


def extractive_summarization(input_text, sentence_length=7):
    # Tokenize the text into sentences
    sentences = sent_tokenize(input_text)

    # Tokenize and preprocess the text
    def preprocess(text):
        tokens = word_tokenize(text)
        tokens = [token.lower() for token in tokens if token.isalpha()]
        tokens = [
            token for token in tokens if token not in stopwords.words('english')]
        return " ".join(tokens)

    # Preprocess each sentence
    preprocessed_sentences = [preprocess(sentence) for sentence in sentences]

    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(preprocessed_sentences)

    # Calculate the TF-IDF scores for each sentence
    sentence_scores = tfidf_matrix.sum(axis=1)

    # Get the top N sentences with the highest TF-IDF scores as the summary
    summary_indices = sentence_scores.argsort(
        axis=0)[-sentence_length:][::-1].flatten().tolist()[0]
    summary_sentences = [sentences[i] for i in summary_indices]

    # Join the summary sentences to create the final summary
    summary = " ".join(summary_sentences)

    return summary


def abstractive_summarization(input_text, max_length=150, min_length=50):
    # Load pre-trained T5 model and tokenizer
    model = T5ForConditionalGeneration.from_pretrained("t5-small")
    tokenizer = T5Tokenizer.from_pretrained("t5-small")

    # Tokenize and format the input text
    input_ids = tokenizer.encode(
        "summarize: " + input_text, return_tensors="pt", max_length=512, truncation=True)

    # Generate summary using the T5 model
    summary_ids = model.generate(input_ids, max_length=max_length, min_length=min_length,
                                 length_penalty=2.0, num_beams=4, early_stopping=True)

    # Decode the generated summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary


# Body
if __name__ == "__main__":
    text = input()
    extractive = extractive_summarization(text)
    abstractive = abstractive_summarization(text)
    print({"extractive": extractive, "abstractive": abstractive})
