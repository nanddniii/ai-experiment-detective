import pandas as pd
from scipy import stats
import numpy as np

# Load experiment data
df = pd.read_csv("data/experiment_data.csv")

# Separate quality scores for Model A and Model B
quality_a = df[df["model_version"] == "A"]["quality_score"]
quality_b = df[df["model_version"] == "B"]["quality_score"]

# Calculate the mean quality of each model
mean_a = quality_a.mean()
mean_b = quality_b.mean()

# Calculate the observed difference
difference = mean_b - mean_a

print("Model A average quality:", mean_a)
print("Model B average quality:", mean_b)
print("Difference (B - A):", difference)


# --------------------------------------------------
# 95% Confidence Interval
# --------------------------------------------------

# Standard error of the difference between two independent means
se_difference = np.sqrt(
    (quality_a.var(ddof=1) / len(quality_a)) +
    (quality_b.var(ddof=1) / len(quality_b))
)

# Degrees of freedom for Welch's method
df_welch = (
    (
        quality_a.var(ddof=1) / len(quality_a)
        + quality_b.var(ddof=1) / len(quality_b)
    ) ** 2
    /
    (
        (
            quality_a.var(ddof=1) / len(quality_a)
        ) ** 2
        / (len(quality_a) - 1)
        +
        (
            quality_b.var(ddof=1) / len(quality_b)
        ) ** 2
        / (len(quality_b) - 1)
    )
)

# Critical t-value for a 95% confidence interval
t_critical = stats.t.ppf(0.975, df_welch)

# Calculate confidence interval
margin_of_error = t_critical * se_difference

lower = difference - margin_of_error
upper = difference + margin_of_error

print("\n95% Confidence Interval:")
print("Lower:", lower)
print("Upper:", upper)


# --------------------------------------------------
# Cohen's d — Effect Size
# --------------------------------------------------

# Standard deviations
std_a = quality_a.std()
std_b = quality_b.std()

# Pooled standard deviation
pooled_std = np.sqrt(
    (
        (len(quality_a) - 1) * std_a**2
        + (len(quality_b) - 1) * std_b**2
    )
    /
    (
        len(quality_a) + len(quality_b) - 2
    )
)

# Cohen's d
cohens_d = difference / pooled_std

print("\nCohen's d:", cohens_d)


# --------------------------------------------------
# Interpretation
# --------------------------------------------------

print("\nInterpretation:")

print(f"Model B improves quality by {difference * 100:.2f}% points.")

print(
    f"The 95% confidence interval for the difference is "
    f"{lower:.4f} to {upper:.4f}."
)

print(f"Cohen's d = {cohens_d:.2f}")

if abs(cohens_d) < 0.2:
    print("Effect size: Very small")
elif abs(cohens_d) < 0.5:
    print("Effect size: Small")
elif abs(cohens_d) < 0.8:
    print("Effect size: Medium")
else:
    print("Effect size: Large")