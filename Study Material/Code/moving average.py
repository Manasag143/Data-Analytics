# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.metrics import mean_squared_error
#from sklearn.metrics import mean_absolute_error
#from sklearn.metrics import mean_absolute_percentage_error


df=pd.read_excel("D:\\advanced analytics\Data_Files\Tablet Computer Sales.xlsx", skiprows=2)
print(df)
#n=3
df["ma_3"]=df["Units Sold"].rolling(window=3).mean().shift(1)
#n=4
df["ma_4"]=df["Units Sold"].rolling(window=4).mean().shift(1)
print(df)
plt.plot(df[df.columns[0]],df[df.columns[1]])
plt.plot(df[df.columns[0]],df[df.columns[2]])
plt.xlabel("Week")
plt.ylabel("Units Sold")
plt.title("Moving Average n=3")
plt.show()
#df=df.dropna(how='any') 
#print(mean_absolute_percentage_error(df["Units Sold"], df["ma_4"])) #MAPE
#print(mean_squared_error(df["Units Sold"], df["ma_4"], squared=False)) #RMSE
#print(mean_squared_error(df["Units Sold"], df["ma_4"], squared=True)) #MSE
#print("n is 3",mean_absolute_error(df["Units Sold"], df["ma_3"])) #MAD

#print("n is 4",mean_absolute_error(df["Units Sold"], df["ma_4"])) #MAD


