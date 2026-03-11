import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



print("1-1")
df = pd.read_csv("CA1/employees.csv")
print(df.head(10))


print("1-2")
print("Columns Names:\n",df.columns)
print("Data Type:\n",type(df))
print("Shape:\n",df.shape)

print("1-3")
print(df.isnull().sum())

print("1-4")
avg_sal = df.groupby("Team")["Salary"].mean()
print(avg_sal)


print("1-5")

team_counts = df['Team'].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(team_counts.index, team_counts.values)

plt.title('Distribution of Employees by Team')
plt.xlabel('Department / Team')
plt.ylabel('Number of Employees')

plt.tight_layout()
plt.show()