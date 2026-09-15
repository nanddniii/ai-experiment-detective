import pandas as pd

df = pd.read_csv("data/experiment_data.csv")

summary = df.groupby("model_version")[
    ["quality_score", "latency_ms", "cost"]
].mean()

quality_a = summary.loc["A", "quality_score"]
quality_b = summary.loc["B", "quality_score"]

latency_a = summary.loc["A", "latency_ms"]
latency_b = summary.loc["B", "latency_ms"]

cost_a = summary.loc["A", "cost"]
cost_b = summary.loc["B", "cost"]

quality_change = (
    (quality_b - quality_a) / quality_a
) * 100

latency_change = (
    (latency_b - latency_a) / latency_a
) * 100

cost_change = (
    (cost_b - cost_a) / cost_a
) * 100

print("=== Experiment Summary ===")

print(f"Quality change: {quality_change:.2f}%")
print(f"Latency change: {latency_change:.2f}%")
print(f"Cost change: {cost_change:.2f}%")

if quality_change > 0 and latency_change <= 10 and cost_change <= 10:
    verdict = "RECOMMEND MODEL B"

elif quality_change > 0:
    verdict = "TRADE-OFF - REVIEW BEFORE ADOPTION"

else:
    verdict = "DO NOT RECOMMEND MODEL B"

print("\n=== Experiment Verdict ===")
print(verdict)

print("\nReason:")

if verdict == "RECOMMEND MODEL B":
    print(
        "Model B improves quality without exceeding "
        "the allowed latency and cost thresholds."
    )

elif verdict == "TRADE-OFF - REVIEW BEFORE ADOPTION":
    print(
        "Model B improves quality, but the increases "
        "in latency and/or cost require further review."
    )

else:
    print(
        "Model B does not provide sufficient quality "
        "improvement to justify adoption."
    )