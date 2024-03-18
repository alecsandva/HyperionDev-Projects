# capstone pls work

import spacy
import pandas as pd
import numpy as np
from spacytextblob.spacytextblob import SpacyTextBlob

# Load SpaCy model and add TextBlob pipeline
nlp = spacy.load("en_core_web_md")
nlp.add_pipe('spacytextblob')

# Load amazon reviews
# This filepath works for my laptop, I tried multiple ways but I kept having an error that the file was not found, please adjust for your device
amazon_reviews = pd.read_csv(r'Desktop\capstoneproject\amazon_product_reviews.csv', low_memory=False)

# Extract review text column
reviews = amazon_reviews[['reviews.text']].copy()

# Drop rows with missing review text
clean_data = reviews.dropna(subset=['reviews.text'])

# Define preprocessing function
def preprocess(review):
    if not isinstance(review, str):
        return review
    doc = nlp(review.lower().strip())
    processed = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    processed_text = ' '.join(processed)
    return processed_text

# Preprocess review text
clean_data['processed_text'] = clean_data['reviews.text'].apply(preprocess)

# Define sentiment analysis function
def sentiment_analysis(review):
    doc = nlp(review)
    sentiment_score = doc._.blob.polarity
    if sentiment_score >= 0.5:
        sentiment = 'Positive'
    elif sentiment_score <= -0.5:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    return sentiment

# Perform sentiment analysis on sample reviews
def sentiment_model(cleaned, num_samples=3):
    sample_indices = np.random.choice(cleaned.index, size=num_samples, replace=False)
    sample_reviews = cleaned.loc[sample_indices, 'processed_text']
    print("\n--- Testing on Sample Reviews ---")
    for review in sample_reviews:
        sentiment = sentiment_analysis(review)
        print(f"Review: {review}")
        print(f"Sentiment: {sentiment}")

# Call the sentiment model function
sentiment_model(clean_data)