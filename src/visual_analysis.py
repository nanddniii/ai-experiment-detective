import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/experiment_data.csv")
quality = df.groupby("model_version")["quality_score"].mean()

print("Average quality:")
print(quality)
quality.plot(kind="bar")

plt.title("Average Quality: Model A vs Model B")
plt.xlabel("Model")
plt.ylabel("Quality Score")

plt.show()

latency = df.groupby("model_version")["latency_ms"].mean()

print("\nAverage latency:")
print(latency)

latency.plot(kind="bar")

plt.title("Average Latency: Model A vs Model B")
plt.xlabel("Model")
plt.ylabel("Latency (ms)")

plt.show()

cost = df.groupby("model_version")["cost"].mean()

print("\nAverage cost:")
print(cost)

cost.plot(kind="bar")

plt.title("Average Cost: Model A vs Model B")
plt.xlabel("Model")
plt.ylabel("Cost")

plt.show()

segment_quality = df.groupby(
    ["query_type", "model_version"]
)["quality_score"].mean().unstack()

segment_quality["difference"] = (
    segment_quality["B"] - segment_quality["A"]
)

print("\nSegment improvement:")
print(segment_quality["difference"])
segment_quality["difference"].plot(kind="bar")

plt.title("Quality Improvement by Query Type")
plt.xlabel("Query Type")
plt.ylabel("Quality Improvement")

plt.show()