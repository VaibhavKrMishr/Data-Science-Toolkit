import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=a
print(a)
print(id(a))
c=a.copy()#Deep Copy
c[0][0]=88
print(a)
print(c)
d=a.view()#Shallow Copy
d[0][0]=99
print(id(d))
print(a)
print(d)