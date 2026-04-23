import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from scipy.stats import ttest_ind

data = pd.read_excel("Datasets/SALES.xlsx")

print("EDA\n")
print("Data Description\n", data.describe())
print("\nData Info\n", data.info())
print("\nIs Null\n", data.isnull().sum())
print("\nData Head\n", data.head())
print("\nData Tail\n", data.tail())

plt.figure()
plt.hist(data['Sales_Cost'], bins=10)
plt.title("Sales Cost Distribution")
plt.xlabel("Sales Cost")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.scatter(data['Sales_Amt'], data['Sales_Cost'])
plt.title("Sales Amount vs Sales Cost")
plt.xlabel("Sales Amount")
plt.ylabel("Sales Cost")
plt.show()



X = data[['Sales_Amt', 'Sales_Qty']]
y = data['Sales_Cost']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

y_pred = model.predict(X_test)

result = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(result.head())


group1 = data[data['PayType'] == 'Debit']['Sales_Cost']
group2 = data[data['PayType'] == 'Credit']['Sales_Cost']

t_stat, p_value = ttest_ind(group1, group2)

print("T-statistic:", t_stat)
print("P-value:", p_value)


if p_value < 0.05:
    print("Reject Null Hypothesis → Significant association")
else:
    print("Fail to Reject Null → No significant association")
    