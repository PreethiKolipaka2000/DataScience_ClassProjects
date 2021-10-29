import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
sns.set(color_codes=True)

# Reading DataFrame From CSV FILE 
df = pd.read_csv("zomato.csv")

# STEP 1 : DATA PREPROCESSING 

# Dropping Unnecessary Columns
df=df.drop(['url','dish_liked','phone'],axis=1)
print(df.columns)

#Converting "votes" and "approx_cost_for_2_people" into numeric(int)
df.rename({'approx_cost(for two people)': 'approx_cost_for_2_people',
                  'listed_in(type)':'listed_in_type',
                  'listed_in(city)':'listed_in_city'
                 }, axis=1, inplace=True)

# Removing comma and changing approx_cost_for_two_people as int 
remove_comma_lambda = lambda x: int(x.replace(',', '')) if type(x) == np.str and x != np.nan else x 
df.votes = df.votes.astype('int')
df['approx_cost_for_2_people'] = df['approx_cost_for_2_people'].apply(remove_comma_lambda)

# Removing Restaurant datas where rate = 'NEW'
df = df.loc[df.rate !='NEW']
df = df.loc[df.rate !='-'].reset_index(drop=True)

# Removing '/5' in rate column
remove_slash = lambda x: x.replace('/5', '') if type(x) == np.str else x
df.rate = df.rate.apply(remove_slash).str.strip().astype('float')

df['rate'] = df['rate'].replace('NEW',np.NaN)
df['rate'] = df['rate'].replace('-',np.NaN)
df.dropna(how = 'any', inplace = True)
df['rate'] = df.loc[:,'rate'].replace('[ ]','',regex = True)

# STEP 2 : REGRESSION ANALYSIS 
def Encode(df):
    for column in df.columns[~df.columns.isin(['rate', 'cost', 'votes'])]:
        df[column] = df[column].factorize()[0]
    return df

df = Encode(df.copy()) 

# CORRELATION BETWEEN DIFFERENT VARIABLES 

corr = df.corr(method='kendall')
plt.figure(figsize=(15,8))
sns.heatmap(corr, annot=True)
plt.tight_layout()
plt.show()

x = df.iloc[:,[2,3,5,6,7,8,9,11]]
y = df['rate']

# Getting Test and Training Set
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.1,random_state=353)

# LINEAR REGRESSION 

from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(x_train,y_train)
y_pred=reg.predict(x_test)
from sklearn.metrics import r2_score
print("R- Square Value : ",r2_score(y_test,y_pred))

# PREDICTION OF RATING USING DECISION TREE REGRESSION

from sklearn.tree import DecisionTreeRegressor
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.1,random_state=105)
Dtree=DecisionTreeRegressor(min_samples_leaf=.0001)
Dtree.fit(x_train,y_train)
y_predict=Dtree.predict(x_test)

from sklearn.metrics import r2_score
print("R-Square Value   :  ",r2_score(y_test,y_predict))
print("Accuracy score for DTREE :",r2_score(y_test,y_predict)*100)
decision_pred =pd.DataFrame({ "Actual Rating": y_test, "Predicted Rating": y_predict })
decision_pred.to_csv('Rating_Predicted_DTree.csv')


plt.figure()
plt.scatter(x,y, s=20, edgecolor="black", c="darkorange", label="data")
plt.plot(x_test, y_predict, color="cornflowerblue", label="max_depth=2", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()

# PREDICTION OF RATING USING  RANDOM FOREST REGRESSION

from sklearn.ensemble import RandomForestRegressor
Rforest=RandomForestRegressor(n_estimators=500,random_state=329,min_samples_leaf=.0001)
Rforest.fit(x_train,y_train)
y_predict=Rforest.predict(x_test)
from sklearn.metrics import r2_score
print("R-Square Value   :  ",r2_score(y_test,y_predict))
print("Accuracy score for RANDOM:",r2_score(y_test,y_predict)*100)
Randpred =pd.DataFrame({ "Actual Rating": y_test, "Predicted Rating": y_predict })
Randpred.to_csv('Rating_Predicted_Rforest.csv')


