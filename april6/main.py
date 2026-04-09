from unicodedata import numeric

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.core.dtypes.inference import Number
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_excel("sample_superstore_excel_dataset.xlsx", sheet_name="Orders")

print("EDA\n")
print("Data Description\n", data.describe())
print("\nData Info\n", data.info())
print("\nIs Null\n", data.isnull().sum())
print("\nData Head\n", data.head())
print("\nData Tail\n", data.tail())

print("\nCorr()")
a=data.corr(numeric_only=True)
# a = data.select_dtypes(include=Number)
print(a)

plt.figure()
sns.heatmap(a, annot=True)
# plt.table("Correlation Heat Map")
plt.show()


x=data[["Sales"]]
y=data["Profit"]
# x=x.reshape(-1,1)

model = LinearRegression()
model.fit(x,y)
y_pred = model.predict(x)

mse =mean_squared_error(y,y_pred)
r_sq=r2_score(y,y_pred)
print(mse,r_sq)