import numpy as np
import pandas as pd

math_score =np.array([85,90,78,92,88])
science_score=np.array([80,85,88,92,86])
df = pd.DataFrame({'Maths':math_score,'Science':science_score})
print(df.describe())
cov_matrix=df.cov()
print("Convariance Matrix:\n",cov_matrix)
corr_matrix=df.corr()
print("\nCorrelation Matrix",corr_matrix)
print(df.describe())