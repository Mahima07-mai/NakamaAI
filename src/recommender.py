import pickle
from rapidfuzz import process

MODEL_PATH = "model/similarity.pkl"

with open(MODEL_PATH, "rb") as f:
    similarity, df = pickle.load(f)


def recommend(anime_name, top_n=5):

    match = process.extractOne(anime_name, df["name"])

    if match is None or match[1] < 60:
        return None

    best_match = match[0]

    idx = df[df["name"] == best_match].index[0]

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    results = [df["name"].iloc[i] for i, _ in scores]

    return results