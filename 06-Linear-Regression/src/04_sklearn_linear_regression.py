import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data=pd.read_csv("06-Linear-Regression\data\salary_data.csv")

x=data[['experience']]
y=data['salary']

# X_train,,y_train

model=LinearRegression()
model.fit(x,y)

a=model.predict([[12]])
print(a)

