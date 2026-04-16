import numpy as np
import pandas as pd
from scipy import stats

data = pd.DataFrame({"values": [12, 15, 16, 10, 13, 15, 14, 16, 14, 13]})
mu = 12

mean = data["values"].mean()
std_dev = data["values"].std(ddof=1)

n = len(data)

t_stat, p_value = stats.ttest_1samp(data["values"], mu)

df = n - 1

alpha = 0.05
t_critical = stats.t.ppf(1 - alpha / 2, df)

print(f"Sample Mean:{mean:.3f}")
print(f"Sample Standard Deviation:{std_dev:.3f}")
# print(f"Sample Mean:{mean:.3f}")
# print(f"Sample Mean:{mean:.3f}")
# print(f"Sample Mean:{mean:.3f}")
# print(f"Sample Mean:{mean:.3f}")
# print(f"Sample Mean:{mean:.3f}")
