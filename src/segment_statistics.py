import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("data/experiment_data.csv")
query_types = df["query_type"].unique()

for query_type in query_types:

    segment = df[df["query_type"] == query_type]

    quality_a = segment[
        segment["model_version"] == "A"
    ]["quality_score"]

    quality_b = segment[
        segment["model_version"] == "B"
    ]["quality_score"]

    t_stat, p_value = ttest_ind(
        quality_a,
        quality_b,
        equal_var=False
    )

    difference = quality_b.mean() - quality_a.mean()

    print("\nQuery type:", query_type)
    print("A mean:", quality_a.mean())
    print("B mean:", quality_b.mean())
    print("Difference:", difference)
    print("P-value:", p_value)
    if p_value < 0.05:
        print("Conclusion: Significant improvement")
    else:
        print("Conclusion: Not statistically significant")