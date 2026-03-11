import pandas as pd

def preprocess_data(path):

    df = pd.read_csv(path)

    # Remove rows without genre or type
    df = df.dropna(subset=["genre", "type"])

    # Convert episodes to numeric
    df["episodes"] = pd.to_numeric(df["episodes"], errors="coerce")

    # Fill missing ratings
    df["rating"] = df["rating"].fillna(df["rating"].mean())

    # Fill missing members
    df["members"] = df["members"].fillna(0)

    # Clean text columns
    df["genre"] = df["genre"].astype(str)
    df["type"] = df["type"].astype(str)

    # Create feature column
    df["features"] = df["genre"].str.replace(",", " ") + " " + df["type"]

    # Final safety: remove any remaining NaN
    df = df.dropna(subset=["features"])

    return df