import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required resources (only first time)
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("punkt_tab")

class TextPreprocessor:

    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def clean_text(self, text):

        # Convert to lowercase
        text = text.lower()

        # Remove punctuation and numbers
        text = re.sub(r'[^a-zA-Z\s]', ' ', text)

        # Tokenize
        tokens = word_tokenize(text)

        # Remove stopwords and lemmatize
        cleaned_tokens = []

        for token in tokens:
            if token not in self.stop_words:
                cleaned_tokens.append(
                    self.lemmatizer.lemmatize(token)
                )

        return cleaned_tokens