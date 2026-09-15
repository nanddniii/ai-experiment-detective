import pandas as pd

df = pd.read_csv("data/experiment_data.csv")
q1 = df["latency_ms"].quantile(0.25)
q3 = df["latency_ms"].quantile(0.75)

print("Q1:", q1)
print("Q3:", q3)
iqr = q3 - q1

print("IQR:", iqr)
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)

anomalies = df[
    (df["latency_ms"] < lower_bound) |
    (df["latency_ms"] > upper_bound)
]
print("\nNumber of latency anomalies:", len(anomalies))

print("\nAnomalous observations:")

print(
    anomalies[
        [
            "model_version",
            "query_type",
            "device_type",
            "latency_ms",
            "quality_score",
            "cost"
        ]
    ]
)

print("\nAnomalies by model:")

print(
    anomalies["model_version"].value_counts()
)