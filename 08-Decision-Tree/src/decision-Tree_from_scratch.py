import pandas as pd
import numpy as np 
from collections import Counter

# data=pd.read_csv("07-Logistic-Regression\data\student_pass_data.csv")

# x=np.array(data["hours"])
# y=np.array(data['result'])

class Node:
    def __init__(self,threshold=None,left=None,right=None,value=None):
        self.threshold=threshold
        self.left=left
        self.right=right
        self.value=value

class DecisionTree:
    def __init__(self):
        self.root=None 
    
    def fit(self,x,y):
        self.root=self.build_tree(x,y)

    def _entorpy(self,y):
        count=Counter(y)
        n=len(y)
        entorpy=0

        for i in count.values():
            p=i/n
            entorpy+=-p*np.log2(p)
        return entorpy
    def information_gain(self,y,left_y,right_y):
        parrent_entropy=self._entorpy(y)
        gain=parrent_entropy-((len(left_y)/len(y))*self._entorpy(left_y)+(len(right_y)/len(y))*self._entorpy(right_y))
        return gain
    def _split(self,x,y):
        heighst_gain=-1
        threshold=None
        thresholds=np.unique(x)
        for i in thresholds:
            left_part= x<=i
            right_part=x>i

            if sum(left_part)==0 or sum(right_part)==0:
                continue

            gain=self.information_gain(y,y[left_part],y[right_part])

            if gain>heighst_gain:
                heighst_gain=gain
                threshold=i
        return threshold
    def build_tree(self,x,y):
        if len(set(y))==1:
            return Node(value=y[0])
        threshold=self._split(x,y)
        if threshold is None:
            return Node(value=Counter(y).most_common(1)[0][0])
        
        left_sub_part= x<=threshold
        right_sub_part=x>threshold

        left_part=self.build_tree(x[left_sub_part],y[left_sub_part])
        right_part=self.build_tree(x[right_sub_part],y[right_sub_part])

        return Node(threshold,left_part,right_part)
    def travarse(self,x,node):
        if node.value is not None:
            return node.value
        if x<=node.threshold:
            return self.travarse(x,node.left)
        else:
            return self.travarse(x,node.right)
    def predict(self, x):
            return np.array([self.travarse(i,self.root) for i in x ])

X = np.array([20, 25, 30, 35, 40, 45])
y = np.array([0, 0, 1, 1, 1, 0])

model = DecisionTree()
model.fit(X, y)

pred = model.predict(np.array([28, 42]))
print(pred)