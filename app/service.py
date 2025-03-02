from fastapi import APIRouter
from pydantic import BaseModel
import joblib
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Load trained model and vectorizer
model = joblib.load("app/random_forest_imdb.pkl")
vectorizer = joblib.load("app/tfidf_vectorizer.pkl")


# Define input schema
class SentimentAnalyser(BaseModel):
    sentence: str

router = APIRouter()
import nltk
nltk.download('all')
nltk.download('stopwords')
nltk.download('wordnet')

# Preprocessing function (same as used in training)
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)  # Remove URLs
    text = re.sub(r'\W+', ' ', text)  # Remove punctuation
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    stop_words.remove('not')
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return " ".join(words)

@router.post("/sentiment-analyser/post/")
async def analyze_sentiment(analyser: SentimentAnalyser):  
    try:
        # Preprocess input sentence
        processed_text = preprocess_text(analyser.sentence)

        # Convert text to TF-IDF features
        transformed_text = vectorizer.transform([processed_text])

        # Predict sentiment (1 = positive, 0 = negative)
        prediction = model.predict(transformed_text)[0]
        sentiment_label = "Positive" if prediction == 1 else "Negative"

        return {"sentiment": sentiment_label}

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
