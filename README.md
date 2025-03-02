# Sentiment-Analysis-FastAPI
A lightweight sentiment analysis web application built with FastAPI, utilizing a Random Forest model trained on the IMDb dataset. This project includes a frontend interface to analyze text sentiment (positive or negative) and demonstrates the integration of machine learning with a RESTful API.

Welcome to the **Sentiment Analysis with FastAPI** project! This repository contains a web application that performs sentiment analysis on text input using a Random Forest machine learning model trained on the IMDb dataset. The backend is built with FastAPI, and the frontend provides a simple interface to interact with the API.

## Overview

This project demonstrates:
- Building a RESTful API with FastAPI.
- Integrating a pre-trained machine learning model for sentiment classification.
- Creating a responsive frontend with HTML, CSS, and JavaScript.
- Deploying a sentiment analysis tool accessible via a web browser.

## Features
- Analyze text sentiment (Positive or Negative).
- Preprocessing of text data (tokenization, lemmatization, stopword removal).
- TF-IDF vectorization for feature extraction.
- Real-time sentiment prediction using a Random Forest classifier.

## Project Structure

```
Sentiment-Analysis-FastAPI/
│
├── __pycache__/            # Python bytecode cache
├── __init__.py
├── index
├── main.py
├── script.js
├── styles.css
├── app/                    # Directory containing backend and model files
│   ├── __pycache__/
│   ├── Execution.ipynb     # Jupyter notebook for model training
│   ├── modelTrainingNLP.ipynb  # Jupyter notebook for model training
│   ├── random_forest_imdb.pkl in zip # Trained Random Forest model (unzip first)
│   ├── service.py          # FastAPI router and sentiment analysis logic
│   └── tfidf_vectorizer.pkl    # TF-IDF vectorizer
├── README.md               # This file
├── requirements.txt        # Python dependencies
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Code-with-pranav/Sentiment-Analysis-FastAPI.git
   cd Sentiment-Analysis-FastAPI
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   Create a `requirements.txt` file with the following content and install:
   ```
   fastapi
   uvicorn
   joblib
   nltk
   scikit-learn
   pydantic
   python-multipart
   ```
   Install them using:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data:**
   Run the following in Python to download required NLTK resources:
   ```python
   import nltk
   nltk.download('all')
   ```

5. **Run the application:**
   Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   Open your browser and navigate to `http://localhost:8000` to see the welcome message, or use the frontend at `http://localhost:8000/index`.

## Usage

1. Open the frontend interface at `http://localhost:8000/index`.
2. Enter a text sentence in the textarea.
3. Click "Analyze Sentiment" to get the sentiment classification (Positive or Negative).
4. The result will be displayed with color-coded feedback.

## API Endpoints

- **POST `/api/sentiment-analyser/post/`**
  - **Request Body:** `{ "sentence": "your text here" }`
  - **Response:** `{ "sentiment": "Positive" }` or `{ "sentiment": "Negative" }` (or an error message if applicable)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](LICENSE) (or choose your preferred license). Feel free to add a `LICENSE` file with the appropriate content.

## Acknowledgments

- The IMDb dataset for training the sentiment analysis model.
- The FastAPI framework for building the API.
- NLTK and scikit-learn for natural language processing and machine learning.

## Contact

For questions or feedback, please open an issue or contact [thisispranavroy@gmail.com](mailto:thisispranavroy@gmail.com).

```
