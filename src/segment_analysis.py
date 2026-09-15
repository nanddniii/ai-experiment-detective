import pandas as pd

df = pd.read_csv("data/experiment_data.csv")

segment_quality = df.groupby(
    ["query_type", "model_version"]
)["quality_score"].mean()

print(segment_quality)
segment_quality = df.groupby(
    ["query_type", "model_version"]
)["quality_score"].mean().unstack()

segment_quality["difference"] = (
    segment_quality["B"] - segment_quality["A"]
)

print(segment_quality)
device_quality = df.groupby(
    ["device_type", "model_version"]
)["quality_score"].mean().unstack()

device_quality["difference"] = (
    device_quality["B"] - device_quality["A"]
)

print("\nQuality by device:")
print(device_quality)
combined_quality = df.groupby(
    ["query_type", "device_type", "model_version"]
)["quality_score"].mean().unstack()

combined_quality["difference"] = (
    combined_quality["B"] - combined_quality["A"]
)

print("\nQuality by query type and device:")
print(combined_quality)
best_segment = combined_quality["difference"].idxmax()
worst_segment = combined_quality["difference"].idxmin()

print("\nBest segment:")
print(best_segment)
print("Improvement:", combined_quality.loc[best_segment, "difference"])

print("\nWorst segment:")
print(worst_segment)
print("Improvement:", combined_quality.loc[worst_segment, "difference"])

sorted_segments = combined_quality.sort_values(
    "difference",
    ascending=False
)

print("\nSegments ranked by improvement:")
print(sorted_segments)