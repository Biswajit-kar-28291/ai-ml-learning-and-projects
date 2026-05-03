import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Data
X = np.array([[20], [25], [30], [35], [40], [45]])
y = np.array([0, 0, 1, 1, 1, 0])

# Model
model = RandomForestClassifier(
    n_estimators=5,   # number of trees
    max_depth=3,      # depth of each tree
    random_state=42   # fix randomness
)

# Train
model.fit(X, y)

# Test data
X_test = np.array([[28], [42]])

# Predict
predictions = model.predict(X_test)

print("Predictions:", predictions)