import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("data/experiment_data.csv")

# -----------------------------
# Day 5: Basic statistics
# -----------------------------

group_means = df.groupby("model_version")["quality_score"].mean()

print("Average quality:")
print(group_means)

difference = group_means["B"] - group_means["A"]

print("\nDifference in quality:", difference)

std = df.groupby("model_version")["quality_score"].std()

print("\nStandard deviation:")
print(std)

summary = df.groupby("model_version")["quality_score"].agg(
    ["mean", "std", "count"]
)

print("\nQuality summary:")
print(summary)


# -----------------------------
# Day 6: Hypothesis testing
# -----------------------------

quality_a = df[
    df["model_version"] == "A"
]["quality_score"]

quality_b = df[
    df["model_version"] == "B"
]["quality_score"]


# Welch's t-test
t_stat, p_value = ttest_ind(
    quality_a,
    quality_b,
    equal_var=False
)

print("\nT-statistic:", t_stat)
print("P-value:", p_value)


# Statistical decision
alpha = 0.05

print("\nStatistical conclusion:")

if p_value < alpha:
    print("The difference is statistically significant.")
else:
    print("The difference is not statistically significant.")

percentage_improvement = (
    (group_means["B"] - group_means["A"])
    / group_means["A"]
) * 100

print("\nPercentage improvement in quality:", percentage_improvement, "%")