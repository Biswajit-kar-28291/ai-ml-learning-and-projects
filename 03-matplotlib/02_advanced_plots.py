import matplotlib.pyplot as plt
import numpy as np

# -------------------------------
# 1. Multiple Lines in One Graph
# -------------------------------
months = [1, 2, 3, 4, 5]
product_a = [10, 20, 30, 40, 50]
product_b = [15, 25, 35, 30, 45]

plt.figure(figsize=(8, 5))
plt.plot(months, product_a, marker='o', label='Product A')
plt.plot(months, product_b, marker='s', label='Product B')
plt.title("Multiple Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()


# -------------------------------
# 2. Area Plot
# -------------------------------
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]

plt.figure(figsize=(8, 5))
plt.fill_between(x, y)
plt.title("Area Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()


# -------------------------------
# 3. Subplots
# -------------------------------
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Left subplot
ax[0].plot([1, 2, 3, 4], [10, 20, 15, 25], marker='o')
ax[0].set_title("Line Plot")
ax[0].set_xlabel("X")
ax[0].set_ylabel("Y")
ax[0].grid(True)

# Right subplot
ax[1].bar(['A', 'B', 'C'], [5, 7, 3])
ax[1].set_title("Bar Plot")
ax[1].set_xlabel("Category")
ax[1].set_ylabel("Value")

plt.tight_layout()
plt.show()


# -------------------------------
# 4. Annotation Example
# -------------------------------
x = [1, 2, 3]
y = [10, 20, 15]

plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o')
plt.annotate("Highest Point", xy=(2, 20), xytext=(2.2, 22),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.title("Annotation Example")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()


# -------------------------------
# 5. Style Example
# -------------------------------
plt.style.use('ggplot')

x = [1, 2, 3, 4, 5]
y = [3, 7, 5, 9, 6]

plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o')
plt.title("Styled Plot Example")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# -------------------------------
# 6. Axis Limit and Tick Example
# -------------------------------
x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]

plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o')
plt.title("Axis Limit and Tick Example")
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(0, 6)
plt.ylim(0, 35)
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([0, 10, 20, 30])
plt.grid(True)
plt.show()


# -------------------------------
# 7. Saving Plot
# -------------------------------
x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 15, 25])

plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o')
plt.title("Save Figure Example")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.savefig("saved_plot.png")
plt.show()


# -------------------------------
# 8. ML Example - Loss Curve
# -------------------------------
epochs = [1, 2, 3, 4, 5]
loss = [0.9, 0.7, 0.5, 0.4, 0.3]

plt.figure(figsize=(8, 5))
plt.plot(epochs, loss, marker='o')
plt.title("Training Loss Curve")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()


# -------------------------------
# 9. ML Example - Accuracy Curve
# -------------------------------
accuracy = [60, 68, 75, 82, 88]

plt.figure(figsize=(8, 5))
plt.plot(epochs, accuracy, marker='o')
plt.title("Training Accuracy Curve")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.grid(True)
plt.show()