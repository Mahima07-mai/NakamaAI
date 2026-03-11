import os
import pickle
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import preprocess_data

DATA_PATH = "data/anime.csv"
MODEL_PATH = "model/similarity.pkl"


def train():

    df = preprocess_data(DATA_PATH)

    print("Total anime:", len(df))

    # TF-IDF
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(df["features"])

    # Cosine similarity
    similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Save model
    os.makedirs("model", exist_ok=True)

    with open(MODEL_PATH, "wb") as f:
        pickle.dump((similarity, df), f)

    print("Model trained and saved.")


if __name__ == "__main__":
    train()