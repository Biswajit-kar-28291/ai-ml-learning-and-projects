import pandas as pd 
import numpy as np

data=pd.read_csv("06-Linear-Regression\data\salary_data.csv")

x=np.array(data["experience"])
y=np.array(data["experience"])

weight=0
bais=0

learning_rate = 0.1
epochs = 100
n = len(x)

for i in range(epochs):
    y_pred=weight*x+ bais

    error=y-y_pred

    dw=(-2/n)*sum(x*error)
    db=(-2/n)*sum(error)

    weight=weight-(learning_rate*dw)
    bais=bais-(learning_rate*dw)


print("Final Weight:",weight)
print("Final Bias:",bais)