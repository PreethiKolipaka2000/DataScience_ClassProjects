# PROGRAM        : PERFORMING MULTIPLE REGRESSION ANALYSIS
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in 
# DATE           : 22-OCT-2021
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None 
import numpy as np 
import pandas as pd
import  matplotlib.pyplot as plt 
from sklearn import linear_model 
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# ......Multi variate regression......
def multiple_reg(data,x1,x2,y1):
    x_data=data[[x1,x2]] #independent var
    y_data=data[y1] #dependant var
    reg_obj=linear_model.LinearRegression()
    reg_obj.fit(x_data,y_data) # coefficient of reg
    # Predict the values afor 10000 males annd 10000 Females 
    literacy_predict=reg_obj.predict([[10000,10000]])
    return literacy_predict 
def cov_mulreg(data,x1,x2,y1):
    x_data=data[[x1,x2]] #independent var
    y_data=data[y1] #dependant var
    reg_obj=linear_model.LinearRegression()
    reg_obj.fit(x_data,y_data) # coefficient of 
    return reg_obj.coef_

# Reading Csv FIle
df1=pd.read_csv("data_2.csv")
# Considering Only World DataFrame 
df=df1[df1['Entity']=='World']

# Child Stunting
print("----------------------Child Stunting --------------------")
print(multiple_reg(df,'Low bone mineral density','Diet low in nuts and seeds','Child stunting'))
print(cov_mulreg(df,'Low bone mineral density','Diet low in nuts and seeds','Child stunting'))

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter(df['Low bone mineral density'],df['Diet low in nuts and seeds'],df['Child stunting'],c='red',marker='o',alpha=0.5)
ax.set_xlabel('Low bone mineral density')
ax.set_ylabel('Diet low in nuts and seeds')
ax.set_zlabel('Child stunting')
plt.show()

print("-----------------Air Pollution-----------------------------------------------------------")
print(multiple_reg(df,'Household air pollution from solid fuels','Outdoor air pollution','Air pollution'))
print(cov_mulreg(df,'Household air pollution from solid fuels','Outdoor air pollution','Air pollution'))


fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter(df['Household air pollution from solid fuels'],df['Outdoor air pollution'],df['Air pollution'],c='green',marker='o',alpha=0.5)
ax.set_xlabel('Household air pollution from solid fuels')
ax.set_ylabel('Outdoor air pollution')
ax.set_zlabel('Air pollution')
plt.show()


print("-----------------No Access to Handwashing Facility-----------------------------------------------------------")

print(multiple_reg(df,"Unsafe water source","Unsafe sanitation","No access to handwashing facility"))
print(cov_mulreg(df,"Unsafe water source","Unsafe sanitation","No access to handwashing facility"))

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter(df['Unsafe water source'],df['Unsafe sanitation'],df['No access to handwashing facility'],c='blue',marker='o',alpha=0.5)
ax.set_xlabel('Unsafe water source')
ax.set_ylabel('Unsafe sanitation')
ax.set_zlabel('No access to handwashing facility')
plt.show()

print("------------------------Alcohol-----------------------------------------------------------")

print(multiple_reg(df,"High systolic blood pressure","High fasting plasma glucose","Alcohol use"))
print(cov_mulreg(df,"High systolic blood pressure","High fasting plasma glucose","Alcohol use"))

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter(df['High systolic blood pressure'],df['High fasting plasma glucose'],df['Alcohol use'],c='black',marker='o',alpha=0.5)
ax.set_xlabel('High systolic blood pressure')
ax.set_ylabel('High fasting plasma glucose')
ax.set_zlabel('Alcohol use')
plt.show()