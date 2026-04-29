import pandas as pd 
import numpy as np 


class linearreg:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate=learning_rate
        self.epochs=epochs
        self.weight=0
        self.bias=0

    def fit(self, x,y):
        n=len(x)

        for i in range(self.epochs):
            y_pred=self.weight*x+self.bias

            eror=y-y_pred

            dw=(-2/n)*sum(x*eror)
            dd=(-2/n)*sum(eror)

            self.weight=self.weight-self.learning_rate*dw
            self.bias=self.bias-self.learning_rate*dd

    def predict(slef,x):
        return slef.weight*x+slef.bias
    
df = pd.read_csv("06-Linear-Regression\data\salary_data.csv")

X = df["experience"].values
y = df["salary"].values

model=linearreg()
model.fit(X,y)
a=model.predict(10)
print(a)




































data=pd.read_csv("06-Linear-Regression\data\salary_data.csv")

x=np.array("experience")
y=np.array("salary")

