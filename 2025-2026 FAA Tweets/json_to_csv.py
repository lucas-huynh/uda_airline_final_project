import json
import pandas as pd

with open("tweets.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.json_normalize(data)
df.to_csv("tweets_2025.csv", index=False)