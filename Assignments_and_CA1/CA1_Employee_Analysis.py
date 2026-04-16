import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../Datasets/melb_data.csv")

print(df.head())

print(df.shape)

print(df[df["Price"]>1000000])

tips=sns.load_dataset("tips")
print(tips)
avg_tips = tips.groupby("day")["tip"].mean()
print(avg_tips)