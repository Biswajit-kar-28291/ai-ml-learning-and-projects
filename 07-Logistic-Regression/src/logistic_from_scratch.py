import pandas as pd
import numpy as np 

data=pd.read_csv("07-Logistic-Regression\data\student_pass_data.csv")

x=data["hours"]
y=data['result']

w=0
b=0
epochs=100
learning_rate=0.01
n=len(x)

def sigmoid(z):
    return 1/(1+np.exp(-z))

for i in range(epochs):
    z=w*x+b
    y_pred=sigmoid(z)

    error=y_pred-y

    dw=(1/n)*sum(error*x)
    db=(1/n)*sum(error)

    w=w-learning_rate*dw
    b=b-learning_rate*db

def predict(x):
    predict_value=sigmoid(w*x+b)
    return 0 if predict_value<0.5 else 1

print("Final Weight:", w)
print("Final Bias:", b)
print("Prediction for 3 hours:", predict(25))