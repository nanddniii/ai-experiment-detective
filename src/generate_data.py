import numpy as np
import pandas as pd

# Make the generated data reproducible
np.random.seed(42)

# Number of AI interactions
n = 1000

# Generate query types
query_types = np.random.choice(
    ["technical", "billing", "account"],
    n
)

# Generate device types
device_types = np.random.choice(
    ["mobile", "desktop"],
    n
)

# Define Control (A) and Treatment (B)
models = np.array(
    ["A"] * (n // 2) +
    ["B"] * (n // 2)
)

# Generate quality scores
quality_scores = np.where(
    models == "A",
    np.random.normal(0.89, 0.05, n),
    np.random.normal(0.94, 0.05, n)
)

# Generate latency
latency = np.where(
    models == "A",
    np.random.normal(1200, 150, n),
    np.random.normal(1500, 150, n)
)

# Generate cost
cost = np.where(
    models == "A",
    np.random.normal(0.40, 0.05, n),
    np.random.normal(0.65, 0.08, n)
)

# Create DataFrame
df = pd.DataFrame({
    "model_version": models,
    "query_type": query_types,
    "device_type": device_types,
    "quality_score": quality_scores,
    "latency_ms": latency,
    "cost": cost
})

# Show first 5 rows
print(df.head())

# Show dataset size
print("\nShape:", df.shape)

# Compare average metrics between Model A and Model B
print("\nAverage metrics by model:")
print(
    df.groupby("model_version")[
        ["quality_score", "latency_ms", "cost"]
    ].mean()
)

# Save the generated dataset
df.to_csv("data/experiment_data.csv", index=False)

print("\nDataset saved to data/experiment_data.csv")