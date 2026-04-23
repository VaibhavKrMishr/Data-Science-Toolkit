import numpy as np
from scipy.stats import chi2_contingency

observed = np.array([
    [40,60],
    [30,70]
])

chi2_stat, p_val, dof, expected = chi2_contingency(observed)
print(f"Chi-Square statistic: {chi2_stat:.4f}")
print(f"Degrees of freedom:{dof}")
print(f"P-Value:{p_val:.4f}")
print("/nExpected Frequency: ")
print(expected)

alpha =0.05
if p_val < alpha:
    print("/nResult: Reject the Null hypothesis.")
else:
    print("/nResult: Fail to reject the Null hypothesis.")
    