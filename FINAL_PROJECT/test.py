import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)

df = pd.read_csv("zomato.csv")
print(df.info())


# EXPLORATORY DATA ANALYSIS


# 1.  MOST POPULAR TOP 20 RESTAURANTS 

# We have 8972 unique restaurants in our dataset that are registered on Zomato.
# Out of these Cafe Coffee Day and Onesta are the most popular ones on Zomato

plt.figure(figsize=(5,5))
top_20_res=df['name'].value_counts()[:20]
ax=sns.barplot(x=top_20_res,y=top_20_res.index,palette='deep')
plt.title("Most Famous Top 20 Restaurants in Banglore",weight='bold')
plt.xlabel("No of Restaurants",fontsize=12)
plt.tight_layout()
plt.savefig("images/Top_20_Res.png")
plt.show()


print(top_20_res)


# print(len(df['name'].unique())) totakl unique count of restaurant names 

# Observation :
#By the above graph here we can see that **Cafe Coffee Day** has the most popular restaurant chains 
#and Onesta has almost 90 popular chains in Bangalore.
#They have almost 100 restaurants in Bangalore. 

# 2. Restaurants Accepting Online Orders 

plt.figure(figsize=(7,7))
online_ord=df['online_order'].value_counts()
ax=sns.barplot(y=online_ord,x=online_ord.index,palette='deep')
plt.title("No of Restaurants Accepting Online Orders",weight='bold')
plt.xlabel('Online Orders ( Yes / No ) ')
plt.ylabel('Counts')
plt.savefig("images/Online_Order.png")
plt.show()

print(df['online_order'].value_counts())

# Observation :
# We Can Say that Majority of the Restaurants has online Order facility i.e 30444 restaurants has Online Order Facility.


# 3. Restaurants Having Book Table Facility  

plt.figure(figsize=(7,7))
book_tab=df['book_table'].value_counts()
ax=sns.barplot(y=book_tab,x=book_tab.index,palette='Set2')
plt.title("No of Restaurants having Booking Table Facility",weight='bold')
plt.xlabel('Book Table Facility ')
plt.ylabel('Count')
plt.savefig("images/Book_table.png")
plt.show()

print(df['book_table'].value_counts())

# Observation :
# We Can Say that Majority of the Restaurants Doesn't have book table  facility 
# i.e 6449 restaurants has Book Table Facility.


# 4. Most Popular Restaurant Types in Banglore 

plt.figure(figsize=(8,8))
rest=df['rest_type'].value_counts()[:15]
ax=sns.barplot(x=rest,y=rest.index)
plt.title("Restaurant types")
plt.xlabel("Count")
plt.tight_layout()
plt.savefig("images/pop_rest_types.png")
plt.show()


# Observation :
# We can Observe that Quick Bytes , Casual dining and Cafe are some Popular Restaurant Types 


# 4. Most Popular Cuisines in Banglore 

plt.figure(figsize=(7,7))
cuisines=df['cuisines'].value_counts()[:10]
ax=sns.barplot(x=cuisines,y=cuisines.index,palette='deep')
plt.xlabel('Count')
plt.title("Most popular cuisines of Bangalore")
plt.tight_layout()
plt.savefig("images/pop_rest_cuisines.png")
plt.show()



# 5. Foodie Areas In Banglore 

plt.figure(figsize=(7,7))
Rest_locations=df['location'].value_counts()[:20]
ax=sns.barplot(Rest_locations,Rest_locations.index,palette="rocket")
plt.tight_layout()
plt.savefig("images/foodie_area.png")
plt.show()




# 6. Percentage of Restaurants in Foodie Areas In Banglore 

plt.figure(figsize = (7,7))
names = df['location'].value_counts()[:10].index
values = df['location'].value_counts()[:10].values
colors = ['gold', 'red', 'lightcoral', 'lightskyblue','blue','green','silver']
explode = (0.1, 0.1, 0, 0,0,0,0,0,0,0)  # explode 1st , 2nd slice

plt.pie(values, explode=explode, labels=names, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title("Percentage of restaurants present in that location", weight = 'bold')
plt.tight_layout()
plt.savefig("images/per_res_foodie_area.png")
plt.show()


# Observation :
# BTM Has Around 3000 Restaurants 


# 7. Approx Cost For Two People 

plt.figure(figsize = (8,8))
df['approx_cost(for two people)'].value_counts()[:20].plot(kind = 'pie')
plt.title('Approx Cost for 2 people', fontsize =20, weight = 'bold')
plt.tight_layout()
plt.savefig("images/avg_cost.png")
plt.show()


# Observation :
# There is 17.86 percentage chances that for two persons the approx cost will be 400 and 
# 17.04 % chance that the cost will be 300 and so on.



# 8. Average Rating Per Restaurant in Banglore 

df['rate'] = df['rate'].replace('NEW',np.NaN)
df['rate'] = df['rate'].replace('-',np.NaN)
df.dropna(how = 'any', inplace = True)
df['rate'] = df.loc[:,'rate'].replace('[ ]','',regex = True)

# Extracting Exact rate value 
df['rate'] = df['rate'].astype(str)
df['rate'] = df['rate'].apply(lambda r: r.replace('/5',''))
df['rate'] = df['rate'].apply(lambda r: float(r))


df.rate.hist(color='c')
plt.axvline(x= df.rate.mean(),ls='--',color='black')
plt.title('Average Rating for Bangalore Restaurants',weight='bold')
plt.xlabel('Rating')
plt.ylabel('No of Restaurants')
plt.savefig("images/avg_rating_rest.png")
plt.show()

print(df.rate.mean())

# Observation :
# The Average Rating for Banglore Restaurants is 3.9 approx.




# 9. Type Of Restaurants and Percentage in Banglore 

plt.figure(figsize=(7,7))
values=df['rest_type'].value_counts()[:10]
labels=df['rest_type'].value_counts()[:10].index
plt.pie(values,labels=labels,autopct="%.2f")
plt.title("Type of Restaurant in Banglore with Percent ( % )")
plt.tight_layout()
plt.savefig("images/rest_type_per.png")
plt.show()



# 10. Type Of Restaurants and Count in Banglore 

plt.figure(figsize=(7,7))
ax=df['rest_type'].value_counts()[:10].plot(kind='bar',color = ['red', 'yellow', 'black', 'blue', 'orange','pink','violet','green','brown'])
plt.title("Type of Restaurant vs Count ",weight='bold')
plt.xlabel('Restaurant Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("images/rest_type_count.png")
plt.show()






# 11. Ratio Between Rating and Restaurant Type in Banglore 

f,ax=plt.subplots(figsize=(20,10))
g = sns.pointplot(x=df["rest_type"], y=df["rate"], df=df)
g.set_xticklabels(g.get_xticklabels(), rotation=90)
plt.title('Rating vs Restaurant type', fontsize =20, weight = 'bold')
plt.tight_layout()
plt.show()


plt.figure(figsize = (14,8))
g=sns.boxplot(x = 'rest_type', y = 'rate', data = df, palette = 'inferno')
g.set_xticklabels(g.get_xticklabels(), rotation=90)
plt.tight_layout()
plt.savefig("images/rating_rest_type.png")
plt.show()







