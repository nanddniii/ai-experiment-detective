import numpy as np
import pandas as pd
np.random.seed(123)
query_types = np.random.choice(
    ["technical", "billing", "account"],
    10
)

device_types = np.random.choice(
    ["mobile", "desktop"],
    10
)

models = np.array(["A"] * 5 + ["B"] * 5)

quality_scores = np.where(
    models == "A",
    np.random.normal(0.89, 0.05, 10),
    np.random.normal(0.94, 0.05, 10)
)

latency = np.where(
    models == "A",
    np.random.normal(1200, 150, 10),
    np.random.normal(1500, 150, 10)
)

cost = np.where(
    models == "A",
    np.random.normal(0.40, 0.05, 10),
    np.random.normal(0.65, 0.08, 10)
)
df = pd.DataFrame({
    "model_version": models,
    "query_type": query_types,
    "device_type": device_types,
    "quality_score": quality_scores,
    "latency_ms": latency,
    "cost": cost
})
print(df)
df.to_csv("data/experiment_data.csv", index=False)