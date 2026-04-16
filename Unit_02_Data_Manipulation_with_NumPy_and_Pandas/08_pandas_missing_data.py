import pandas as pd
import numpy as np

data = {
    'ID':[1,2,3,4,5],
    'Name':["Alice",'Bob', np.nan ,'David','Eve'],
    'Age':[25, np.nan, 30, np.nan, 40],
    'City':['New York', 'Los Angeles','Chicago',np.nan,'Hosuton'],
    'Salary':[50000,60000,np.nan,90000,80000]
}
df=pd.DataFrame(data)
print("Original DataFrame With Missing Values: ")
print(df)   
print("\nMissing Values in each column:")
print(df.isnull().sum())


#Dropping rows with missing values
df_dropped_rows =df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped_rows)

#Dropping cols with missing values
df_dropped_cols=df.dropna(axis=1)
print("\nDataFrame after dropping cols with missing values:")
print(df_dropped_cols)


#Filling missing values with specific values
df_filled =df.fillna({
    'Age':df['Age'].mean(),
    'City':"New York",
    'Salary': df['Salary'].mean()
})
print("\nDataFrame After filling missing values:")
print(df_filled)


#Fowrward Fill (upgrade to avoid Future Warning)
df_Ffill = df.ffill()
print("\nDataFrame after Forward filling:")
print(df_Ffill)

#Backward Fill (upgrade to avoid Future Warning)
df_Bfill = df.bfill()
print("\nDataFrame after Backward filling:")
print(df_Bfill)



#23 FEB

#Interpolating Missing Values(Updated to avoid Future Warning)
df_numeric =df.select_dtypes(include =[np.number])
df_interpolated = df_numeric.interpolate()

#Merge back non-numric columns
df_final=df.copy()
df_final[df_numeric.columns]=df_interpolated
print("\nDataFrame after Interpolation: ")
print(df_final)

#Saving Cleared DAta
df_final.to_csv("./ABC.csv",index=False)
print(f"Cleaned data saved to:{"ABC.csv"}")