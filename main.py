import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from pathlib import Path
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "reviews.csv" / "reviews.csv"   # FIXED PATH

if not csv_path.exists():
    raise FileNotFoundError(f"File not found: {csv_path}")

print(f"Loading data from: {csv_path}")

df = pd.read_csv(csv_path)

print("Columns in dataset:", df.columns)

possible_text_cols = ["review", "content", "review_text", "text"]
review_col = next((col for col in possible_text_cols if col in df.columns), None)

if review_col is None:
    raise KeyError("No valid review column found!")

print(f"Using column: {review_col}")

reviews = df[review_col].dropna().head(50).tolist()
aspects = {
    "UI": ["ui", "design", "interface", "layout"],
    "Performance": ["slow", "fast", "lag", "crash", "loading"],
    "Features": ["feature", "option", "tool", "function"]
}


def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


def analyze_aspects(review_text, aspects_dict):
    results = {}
    review_lower = review_text.lower()

    for aspect, keywords in aspects_dict.items():
        found_sentiment = None

        for keyword in keywords:
            if keyword in review_lower:
                sentences = TextBlob(review_text).sentences

                for sentence in sentences:
                    if keyword in sentence.raw.lower():
                        found_sentiment = get_sentiment(str(sentence))
                        break

                if found_sentiment:
                    break

        results[aspect] = found_sentiment if found_sentiment else "N/A"

    return results

results_list = []

for review in reviews:
    aspect_sentiments = analyze_aspects(review, aspects)
    
    row = {"Review": review}
    row.update(aspect_sentiments)
    
    results_list.append(row)

results_df = pd.DataFrame(results_list)

print("\nFinal Output Table:\n")
print(results_df)


results_df.to_csv("output_results.csv", index=False)
print("\nSaved as output_results.csv")

aspect_counts = {
    "UI": {"Positive": 0, "Negative": 0, "Neutral": 0},
    "Performance": {"Positive": 0, "Negative": 0, "Neutral": 0},
    "Features": {"Positive": 0, "Negative": 0, "Neutral": 0}
}

for _, row in results_df.iterrows():
    for aspect in ["UI", "Performance", "Features"]:
        sentiment = row[aspect]
        if sentiment in ["Positive", "Negative", "Neutral"]:
            aspect_counts[aspect][sentiment] += 1

graph_df = pd.DataFrame(aspect_counts)

graph_df.plot(kind='bar')

plt.title("Aspect-Based Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.show()
