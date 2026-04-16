import numpy as np
from scipy.stats import chi2_contingency

observed = np.array([
    [35,52.5,12.5],
    [28.1,42.1,9.8],
    [6.9,10.4,2.7]
])

chi2_stat, p_val, dof, expected = chi2_contingency(observed)
print(f"Chi-Square statistic: {chi2_stat:.4f}")
print(f"Degrees of freedom:{dof}")
print(f"P-Value:{p_val:.4f}")