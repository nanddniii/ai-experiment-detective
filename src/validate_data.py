import pandas as pd

df = pd.read_csv("data/experiment_data.csv")

print(df.head())
required_columns = [
    "model_version",
    "query_type",
    "device_type",
    "quality_score",
    "latency_ms",
    "cost"
]
missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]

print("Missing columns:", missing_columns)
print("\nMissing values:")
print(df.isnull().sum())
invalid_quality = df[
    (df["quality_score"] < 0) |
    (df["quality_score"] > 1)
]

print("\nInvalid quality scores:", len(invalid_quality))
invalid_latency = df[
    df["latency_ms"] < 0
]

print("Invalid latency values:", len(invalid_latency))
invalid_cost = df[
    df["cost"] < 0
]

print("Invalid cost values:", len(invalid_cost))
print("\nModels:")
print(df["model_version"].value_counts())
print("\n--- Validation Summary ---")

if not missing_columns:
    print("Required columns: PASS")
else:
    print("Required columns: FAIL")

if df.isnull().sum().sum() == 0:
    print("Missing values: PASS")
else:
    print("Missing values: FAIL")

if len(invalid_quality) == 0:
    print("Quality scores: PASS")
else:
    print("Quality scores: FAIL")

if len(invalid_latency) == 0:
    print("Latency values: PASS")
else:
    print("Latency values: FAIL")

if len(invalid_cost) == 0:
    print("Cost values: PASS")
else:
    print("Cost values: FAIL")

if set(df["model_version"]) == {"A", "B"}:
    print("Control/Treatment groups: PASS")
else:
    print("Control/Treatment groups: FAIL")
print("\nInvalid quality rows:")
print(
    invalid_quality[
        ["model_version", "quality_score"]
    ].head()
)
validation_passed = (
    len(missing_columns) == 0
    and df.isnull().sum().sum() == 0
    and len(invalid_quality) == 0
    and len(invalid_latency) == 0
    and len(invalid_cost) == 0
    and set(df["model_version"]) == {"A", "B"}
)

print("\nOverall validation status:")

if validation_passed:
    print("PASS - Data is ready for analysis.")
else:
    print("FAIL - Data requires attention before analysis.")

print(f"Invalid quality score count: {len(invalid_quality)}")