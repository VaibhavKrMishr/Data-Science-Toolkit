#linear regression
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.stats.outliers_influence import variance_inflation_factor


x=np.array([1,2,3,4,5])
y=np.array([3,4,2,4,5])
x=x.reshape(-1,1)
model=LinearRegression()
model.fit(x,y)
y_pred=model.predict(x)
mse=mean_squared_error(y,y_pred)
r_sq=r2_score(y,y_pred)
print(mse,r_sq)

#
x = np.array([[500],[750],[1000],[1250],[1500],[1750],[2000],[2250],[2500]])
y = np.array([150,200,250,275,300,325,350,375,400])
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
#model
model = LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
#error
mse = mean_squared_error(y_test, y_pred)
r2= r2_score(y_test,y_pred)
#plotting result
plt.scatter(x,y,color='blue',label='Actual Data')
plt.plot(x,model.predict(x),color='red',linewidth=2,label='regression line')
plt.xlabel("house size (sq ft)")
plt.ylabel("price ($1000)")
plt.title("linear regression: house size vs. price")
plt.legend()
plt.grid(True)
plt.show()
#used to predict a value using a trained machine learning model.
a = np.array([[3500]])
predicted_price = model.predict(a)
print(predicted_price)

X_df = pd.DataFrame(x, columns=["House_Size"])
vif_data =pd.DataFrame()
vif_data['Feature'] =X_df.columns
vif_data['VIF']=[variance_inflation_factor(X_df.values,i)for i in range(X_df.shape[1])]

print("/nVarience Inflation Factor(VIF):")
print(vif_data)