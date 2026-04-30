import pandas as pd
from sklearn.linear_model import LogisticRegression

data=pd.read_csv("07-Logistic-Regression\data\student_pass_data.csv")

x=data[["hours"]]
y=data['result']

model=LogisticRegression()
model.fit(x,y)
a=model.predict([[2]])

if a>=0.5:
    print(1)
else:
    print(0)


