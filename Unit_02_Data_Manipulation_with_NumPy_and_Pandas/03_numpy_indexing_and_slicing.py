import numpy as np

# a=np.arange(12).reshape(3,4)
# print("A\n",a)
# print()
# print("a[1][1]:",a[1][1])
# print()
# print('a[1]:',a[1])
# print()
# print("a[1:3,0:2]:",a[1:3,0:2])
# print()
# print('a[-1][-1]',a[-1][-1])
# print()
# print('a[-1]',a[-1])
# print()
# print('a[-1,-1]',a[-1,-1])
# print()
# print(a[:1,-3:][0])


a=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print("Via array-like input: \n",a)
print('Max',np.max(a))
print("Min",np.min(a))
print("Sum",np.sum(a))
print("Sort",np.sort(a))
print("ABS",np.abs(a))
print("Cummulative sum coloumn wise",a.cumsum(axis=0))
print("Cummulative sum row wise",a.cumsum(axis=1))
print("Flatten funtion",a.flatten())
print("Transpose fumction",a.transpose())

l=[]
for i in range(13,22):
    l.append(i)
a=np.array(l)
a.shape=(3,-1)
print(a)