import numpy as np
from scipy import stats

mu = 70
sample_mean = 73
sigma = 10
n = 50

alpha = 0.05

z_stat = (sample_mean - mu) / (sigma / np.sqrt(n))

z_critical = stats.norm.ppf(1 - alpha)

p_value = 1 - stats.norm.cdf(z_stat)

# print(f"Sample Mean (x): {sample_mean}")
# print(f"Population Mean (mu): {mu}")
# print(f"Standard Deviation (sigma): {sigma}")
# print(f"Sample Size (n): {n}")
print(f"Z-statistic: {z_stat:.3f}")
print(f"P-value: {p_value:.4f}")
print(f"Critical Z-value (one-tailed, a=0.05): {z_critical:.3f}")

if p_value < alpha:
    print("Conclusion: Reject the null hypothesis. The new method increases the average score.\n")
else:
    print("Conclusion: Fail to reject the null hypothesis.\n")