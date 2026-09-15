import pandas as pd

df = pd.read_csv("data/experiment_data.csv")
summary = df.groupby("model_version")[
    ["quality_score", "latency_ms", "cost"]
].mean()

print("Average metrics:")
print(summary)
quality_change = (
    (summary.loc["B", "quality_score"]
     - summary.loc["A", "quality_score"])
    / summary.loc["A", "quality_score"]
) * 100

latency_change = (
    (summary.loc["B", "latency_ms"]
     - summary.loc["A", "latency_ms"])
    / summary.loc["A", "latency_ms"]
) * 100

cost_change = (
    (summary.loc["B", "cost"]
     - summary.loc["A", "cost"])
    / summary.loc["A", "cost"]
) * 100
print("\nPercentage changes:")
print("Quality:", quality_change, "%")
print("Latency:", latency_change, "%")
print("Cost:", cost_change, "%")

print("\nTrade-off assessment:")

if quality_change > 0 and latency_change > 0 and cost_change > 0:
    print("Quality improved, but latency and cost also increased.")