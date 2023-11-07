# Imports
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download NLTK data for tokenization and stopwords
nltk.download('punkt')
nltk.download('stopwords')

# Text for summarization
text = input()

# Tokenize the text into sentences
sentences = sent_tokenize(text)

# Tokenize and preprocess the text
def preprocess(text):
    tokens = word_tokenize(text)
    tokens = [token.lower() for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token not in stopwords.words('english')]
    return " ".join(tokens)

# Preprocess each sentence
preprocessed_sentences = [preprocess(sentence) for sentence in sentences]

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(preprocessed_sentences)

# Calculate the TF-IDF scores for each sentence
sentence_scores = tfidf_matrix.sum(axis=1)

# Define the number of sentences to include in the summary
N = 7  # You can adjust this to control the summary length

# Get the top N sentences with the highest TF-IDF scores as the summary
summary_indices = sentence_scores.argsort(axis=0)[-N:][::-1].flatten().tolist()[0]
summary_sentences = [sentences[i] for i in summary_indices]

# Join the summary sentences to create the final summary
summary = " ".join(summary_sentences)

# Print the summary
print(summary)
