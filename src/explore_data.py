import pandas as pd

df = pd.read_csv("data/sample_experiments.csv")

model_a = df[df["model_version"] == "A"]
model_b = df[df["model_version"] == "B"]


print(df.groupby("query_type")["quality_score"].mean())
print(
    df.groupby(
        ["model_version", "query_type"]
    )["quality_score"].mean()
)