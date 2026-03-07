import pandas as pd

s=pd.Series([1,2,3],
index=['a','b','c'])

# print(s)
# print(s.describe())


d=pd.DataFrame(s)
print(d)
b= pd.DataFrame([2,5,6],
                index=['a','b','c'],
                columns=['No'])



print(b)
# print(b.describe())


data ={'a':0.0,'b':1.0,'c':2.0}
s1= pd.Series(data, index=['b','c','d','a'])
print(s1)
list =['g','e','e','k','s']

s2=pd.Series()
print(s2)

s3=pd.Series([1,2,3,4,5],
             index=['a','b','c','d','e'])


print(s3)


















































# df = pd.DataFrame(
# {"a" : [4, 5, 6],
# "b" : [7, 8, 9],
# "c" : [10, 11, 12]},
# index = [1, 2, 3])

# print(df)


# df2 = pd.DataFrame(
# [[4, 7, 10],
# [5, 8, 11],
# [6, 9, 12]],
# index=[1, 2, 3],
# columns=['a', 'b', 'c'])

# print(df2)


# df3 = pd.DataFrame(
# {"a" : [4 ,5, 6],
# "b" : [7, 8, 9],
# "c" : [10, 11, 12]},
# index=[1,2,3])

# print(df3)


# df4 = pd.DataFrame(
# {"a" : [4 ,5, 6, 7],
# "b" : [7, 8, 9, 10],
# "c" : [10, 11, 12, 13]},
# index = pd.MultiIndex.from_tuples(
# [('e', 1), ('e', 2),
# ('f', 1),('f',2)], names=['n', 'v']))

# print(df4)
# print(df4.describe())