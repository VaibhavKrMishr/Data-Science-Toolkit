import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=np.array([1,2,2,2,3,3,4,5,5,5,6,6,6,6,7,8,8,9,27])
data1= pd.DataFrame(data)

print(data1.describe())

#IQR Methord
Q1= np.percentile(data, 25)
Q3= np.percentile(data, 75)
IQR=Q3-Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 - 1.5 * IQR
outliers_iqr = data[(data< lower_bound)| (data>upper_bound)]
print(outliers_iqr)

#2. Z-Score Methord(Using sample standard deviation)
mean = np.mean(data)
std_dev = np.std(data,ddof=1)
z_score =(data - mean)/ std_dev
outliers_z = data[np.abs(z_score)>3]
print(outliers_z)

#3. Box Plot Visualization
plt.figure(figsize=(6,4))
plt.boxplot(data,vert=False)
plt.xlabel("Values")
plt.title("Box Plot for Outliers Detection")
plt.show()