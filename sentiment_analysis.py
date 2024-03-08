import spacy
import pandas as pd
import numpy as np

# Loaded medium pack for improved accuracy.
nlp = spacy.load("en_core_web_md")

# Loading my CSV file.
amazon = pd.read_csv('Datafiniti_Amazon_Consumer_reviews_of_Amazon_Products.csv')
low_memory=False

# Cleaning two rows of data, checking for null values and removing them from my analysis.
cleaned = amazon[['reviews.text', 'reviews.title']]
cleaned.isnull().sum()
cleaned.dropna(inplace=True, axis=0)
cleaned.isnull().sum()
# Isolating review text for further processing.
text = cleaned['reviews.text']


# Process review text, converts to lower case, eliminates trailing spaces.
# Transform words to base form, remove stop words and punctuation.
def preprocess(review):
    if not isinstance(text, str): 
        return text
    doc =nlp(text.lower().strip())
    processed = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(processed)

# Convert the column to a list
reviews = amazon["reviews.text"].tolist()

# Import libraries for wordcloud generation.
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import defaultdict
from textblob import TextBlob

# Dictionaries to store positive and negative word counts.
positive_words = defaultdict(int)
negative_words = defaultdict(int)

# Set function for basic sentiment analysis output.
for sentence in cleaned['processed.text']:
    doc = nlp(sentence)
    tokens = [token.lemma_.lower().strip() for token in doc if not token.is_stop and token.is_alpha]
    for token in tokens:
        blob = TextBlob(str(token))
        polarity = blob.sentiment.polarity

        if polarity > 0:
            positive_words[token.lower()] += 1
        elif polarity < 0:
            negative_words[token.lower()] += 1

# Calculates sentiment by iterating through each review in column.
def sentiment_analysis(cleaned):
    for review in cleaned['reviews.text']: 
        doc = nlp(review)
        sentiment = doc._.sentiment
        print(f"\nReview: {review}")
        print(f"Sentiment: {sentiment}")

# Test sentiment analysis on random reviews.   
def test_sentiment_model(cleaned, num_samples=3):
    sample_indices = np.random.choice(cleaned.index, size=num_samples, replace=False)
    sample_reviews = cleaned.loc[sample_indices, 'reviews.text']

    print("\n--- Testing on Sample Reviews ---")
    sentiment_analysis(sample_reviews)

