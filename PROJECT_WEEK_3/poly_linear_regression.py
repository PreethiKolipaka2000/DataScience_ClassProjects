# PROGRAM        : PERFORMING LINEAR AND PLOYNOMIAL REGRESSION ANALYSIS
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
def multiple_reg(file,x1,x2,y1):
    data=pd.read_csv(file)
    x_data=data[[x1,x2]] #independent var
    y_data=data[y1] #dependant var
    reg_obj=linear_model.LinearRegression()
    reg_obj.fit(x_data,y_data) # coefficient of reg
    # Predict the values afor 10000 males annd 10000 Females 
    literacy_predict=reg_obj.predict([[10000,10000]])
    return literacy_predict # ....
def cov_mulreg(file,x1,x2,y1):
    data=pd.read_csv(file)
    x_data=data[[x1,x2]] #independent var
    y_data=data[y1] #dependant var
    reg_obj=linear_model.LinearRegression()
    reg_obj.fit(x_data,y_data) # coefficient of 
    return reg_obj.coef_

# ......Polynomial Regression.......

def polynomial_regression(x,y,xlab,ylab):
    poly=PolynomialFeatures(degree=3)
    x_poly=poly.fit_transform(x.reshape(-1,1))
    poly_model=LinearRegression()
    poly_model.fit(x_poly,y.reshape(-1,1))
    y_pred=poly_model.predict(x_poly)

    poly=np.poly1d(np.polyfit(x,y,3))
    print("r2_score of ",xlab,'Vs',ylab,"is",r2_score(y,poly(x)))

    plt.scatter(x,y,c='green')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(xlab+" Vs "+ylab)
    plt.plot(x,y_pred,c='red')
    plt.ticklabel_format(style='plain')
    plt.gcf().set_size_inches(7,7)
    #plt.xticks(rotation=90)
    plt.savefig("./static/"+"poly_"+xlab+" Vs"+ ylab+".png",format="png")
    plt.show()

# ... Linear Regression.....
def linear_reg(x,y,xlab,ylab):
    m=((len(x)*sum(x*y))-(sum(x)*sum(y)))/((len(x)*sum(x*x))-sum(x)*2)
    c=(sum(y)-m*sum(x))/len(x)
    print("m and c of",xlab,'Vs',ylab,"is",m,c)

    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(xlab+" Vs "+ylab)
    plt.scatter(x,y)
    plt.plot(x,m*x+c,color="red")
    plt.ticklabel_format(style='plain')
    plt.gcf().set_size_inches(5,5)
    #plt.xticks(rotation=90)
    plt.savefig("./static/"+xlab+" Vs"+ ylab+".png",format="png")
    plt.show()


# Reading Csv FIle
df1=pd.read_csv("data_2.csv")

# Considering Only World DataFrame 
df=df1[df1['Entity']=='World']

# Applying Linear and polynomial  Regression Over Certain Attributes 
high_sodium=np.array(df['Diet high in sodium'])
blood_pressure=np.array(df['High systolic blood pressure'])
polynomial_regression(high_sodium,blood_pressure,'Diet High in sodium','Blood pressure')

smoking=np.array(df['Smoking'])
sec_smoke=np.array(df['Secondhand smoke'])
polynomial_regression(smoking,sec_smoke,'Smoking','SecondHand Smoke')

alc=np.array(df['Alcohol use'])
iron_def=np.array(df['Iron deficiency'])
polynomial_regression(alc,iron_def,'Alcohol use','Iron deficiency')

