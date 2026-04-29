import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("data\salary_data.csv")

x=data["experience"]
y=data["salary"]

x_mean=x.mean()
y_mean=y.mean()

nu=((x-x_mean)*(y-y_mean)).sum()
du=((x-x_mean)**2).sum()
# formula of slope is sum((y-ybar)*(x-xbar)) devided by sum(x-xbar)**2
slope=nu/du

intershape=y_mean-slope*x_mean

pred_value=int(input("Enter Your Predict Value:"))
# this is the exact linear regression formmula 
pred_value=slope*pred_value+intershape


y_pred=slope*x+intershape

# print(y_pred)

plt.scatter(x,y, label="Actual Data")
plt.plot(x,y_pred, label="Predict Data")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Basic linear regression usign fromula")
plt.legend()
plt.show()