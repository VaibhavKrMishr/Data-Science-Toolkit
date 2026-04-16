import pandas as pd
df=pd.read_excel("../Datasets/tips.xlsx")
# print(df)
#Read CSV

print("Data Loaded Successfylly!\n")

#Display first 10 rows
print("First 10 rows:\n",df.head(10))
print()
# Display last 5 rows
print("Last 5 rows;\n",df.tail(5))
print()
#Dataframe Summary
print("DataFrame Info:")
df.info()
print()

# Descriptive Statics
print("Descriptive Statistics:\n",df.describe(),"\n")

#Shape of DataFrame
print("Shape of Datframe:",df.shape,"\n")

#Column Names
print("Columns Names:\n",df.columns,"\n")

#Checking Missing Values
print("Missing Values:\n",df.isnull().sum(),"\n")

#Drop Rows
df_clear=df.dropna()
print("Data after dropping missing values;\n", df_clear.head(),"\n")

#Fill Missing Values
df_filled=df.fillna(0)
print("Data after filling missing values:\n",df_filled,"\n")

#Group by a column and aggregate
grouped_data=df.groupby('day')['total_bill'].sum()
print("Total Bills:\n",grouped_data,"\n")

#Sort values by total bills in descending order
sorted_df=df.sort_values(by='total_bill',ascending=False)
print("Top 5 Tolal bill Records;\n",sorted_df.head(),"\n")

#Apply function to transform total bill columns
df['total_bill_in_hundreds']=df['total_bill'].apply(lambda x:x/100)
print("Transformed Total bills data:\n",df[['total_bill','total_bill_in_hundreds']].head(),"\n")
