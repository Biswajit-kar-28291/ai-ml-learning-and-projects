from collections import Counter
import numpy as np
class Node:
    def __init__(self, threshold=None,left=None,right=None,value=None):
        self.threshold=threshold
        self.left=left
        self.right=right
        self.value=value
class decisiontree:
    def __init__(self, max_depth=3):
        self.max_depth = max_depth
        self.root = None
    def gini(self,y):
        value=Counter(y)
        p=0
        for i in value.values():
            p+=(i/len(y))**2
        return 1-p
    
    def best_split(self,x,y):
        best_gini=float("inf")
        thresholds=np.unique(x)
        threshold=None

        for i in thresholds:
            left_part= x<=i
            right_part= x>i

            if sum(left_part)==0 or sum(right_part)==0:
                continue
            left=y[left_part]
            right=y[right_part]

            gini_total=((len(left)/len(y))*self.gini(left))+((len(right)/len(y))*self.gini(right))

            if gini_total<best_gini:
                best_gini=gini_total
                threshold=i
        return threshold
    
    def build_tree(self, x, y):
        if len(set(y))==1:
            return Node(value=y[0])
        
        threshold=self.best_split(x,y)

        if threshold is None:
            return Node(value=Counter(y).most_common(1)[0][0])
        
        left_part= x<=threshold
        right_part= x>threshold

        left=self.build_tree(x[left_part],y[left_part])
        right=self.build_tree(x[right_part],y[right_part])

        return Node(threshold,left,right)
    def fit(self,x,y):
        self.root=self.build_tree(x,y)

    def travarse(self,x,node):
        if node.value is not None:
            return node.value
        if x>node.threshold:
            return self.travarse(x,node.right)
        else:
            return self.travarse(x,node.left)
    def predict(self,X):
        return np.array([self.travarse(x,self.root) for x in X])

class randomforest:
    def __init__(self, n_trees=5,max_depth=3):
        self.n_trees=n_trees
        self.max_depth=max_depth
        self.trees=[]

    def bootstrap(self, x, y):
        n=len(y)
        tree=np.random.choice(
                n, size=n,replace=True
            )
        return x[tree],y[tree]
    def fit(self,x,y):
        self.trees=[]
        for i in range(self.n_trees):
            x_sample,y_sample=self.bootstrap(x,y)

            tree=decisiontree(max_depth=self.max_depth)
            tree.fit(x_sample,y_sample)
            self.trees.append(tree)
    def majority(self,prediction):
        count=Counter(prediction)
        return count.most_common(1)[0][0]
    def predict(self,x):
        all_tree_predictions=[]

        for i in self.trees:
            pred=i.predict(x)
            all_tree_predictions.append(pred)

        all_tree_predictions = np.array(all_tree_predictions)

        final_predictions = []

        for col in all_tree_predictions.T:
            final_predictions.append(self.majority(col))

        return np.array(final_predictions)



X = np.array([20, 25, 30, 35, 40, 45])
y = np.array([0, 0, 1, 1, 1, 0])

model = randomforest(n_trees=5, max_depth=3)
model.fit(X, y)

test_data = np.array([28, 42])

predictions = model.predict(test_data)

print("Predictions:", predictions)