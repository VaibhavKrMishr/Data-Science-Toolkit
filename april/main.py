import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

x= np.array([1,2,3,4,5])
y= np.array([3,4,2,4,5])
x=x.reshape(-1,1)

model = LinearRegression()
model.fit(x,y)
y_pred = model.predict(x)

mse =mean_squared_error(y,y_pred)
r_sq=r2_score(y,y_pred)
print(mse,r_sq)