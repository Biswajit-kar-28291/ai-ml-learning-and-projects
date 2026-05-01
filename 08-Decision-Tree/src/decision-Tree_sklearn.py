import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Create sample data
data = pd.DataFrame({
    "Age": [20, 25, 30, 35, 40, 45],
    "Label": [0, 0, 1, 1, 1, 0]
})

# 2. Split input and output
X = data[["Age"]]
y = data["Label"]

# 3. Create model
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

# 4. Train model
model.fit(X, y)

# 5. Predict
y_pred = model.predict(X)

# 6. Evaluate
print("Accuracy:", accuracy_score(y, y_pred))
print("\nClassification Report:")
print(classification_report(y, y_pred))

# 7. New prediction
new_age = [[28]]
prediction = model.predict(new_age)

print("Prediction for Age 28:", prediction[0])