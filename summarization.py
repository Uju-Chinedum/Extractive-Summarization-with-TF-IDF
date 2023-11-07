# Imports
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

# Download NLTK data for tokenization and stopwords
nltk.download('punkt')
nltk.download('stopwords')

# Function Definition
def summarize_text(input_text, summary_length=7):
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
        axis=0)[-summary_length:][::-1].flatten().tolist()[0]
    summary_sentences = [sentences[i] for i in summary_indices]

    # Join the summary sentences to create the final summary
    summary = " ".join(summary_sentences)

    return summary

# Body
if __name__ == "__main__":
    text = input()
    summary = summarize_text(text)
    print(summary)