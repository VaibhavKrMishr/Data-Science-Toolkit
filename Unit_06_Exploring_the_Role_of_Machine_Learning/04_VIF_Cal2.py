import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

x = pd.DataFrame({
    'House_size':[500 ,750, 1000 ,1250 ,1500 ,1750 ,2000, 2250, 2500],
    'Bedrooms':[1,2,2,3,3,4,4,4,5]
})

vif_data=pd.DataFrame()
vif_data["Feature"]=x.columns
vif_data=[variance_inflation_factor(x.values,i)for i in range(x.shape[1])]

print(vif_data)