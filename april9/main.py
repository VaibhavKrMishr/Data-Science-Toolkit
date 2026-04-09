import math
from scipy.stats import norm

sample_mean =169.5
population_mean = 168
population_std_dev=3.9
sample_size=36
alpha=0.05
tail="two"

standard_error = population_std_dev/math.sqrt(sample_size)

z_score =(sample_mean - population_mean)/standard_error

if tail =="two":
    p_value = 2*(1 - norm.cdf(abs(z_score)))
    print(norm.cdf(abs(z_score)))
elif tail =="left":
    p_value = norm.cdf(z_score)
    print(norm.cdf(z_score))
elif tail=="right":
    p_value =1- norm.cdf(z_score)
else:
    raise ValueError("tail must be 'two','right','left'")
    
if p_value <alpha:
    conclusion = "Reject the Null Hypothesis"
else:
    conclusion = "Fail to reject the Null Hypothesis"
print(f"Z-Score: {z_score:.4f}")
print(f"P-Score: {p_value:.4f}")
print(f"Conclusion: {conclusion}")
    
