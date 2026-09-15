import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("data/experiment_data.csv")

quality_a = df[df["model_version"] == "A"]["quality_score"]
quality_b = df[df["model_version"] == "B"]["quality_score"]

t_stat, p_value = ttest_ind(
    quality_a,
    quality_b,
    equal_var=False
)

print("Model A average:", quality_a.mean())
print("Model B average:", quality_b.mean())

print("\nT-statistic:", t_stat)
print("P-value:", p_value)

alpha = 0.05

print("\nConclusion:")

if p_value < alpha:
    print("The difference is statistically significant.")
else:
    print("The difference is not statistically significant.")