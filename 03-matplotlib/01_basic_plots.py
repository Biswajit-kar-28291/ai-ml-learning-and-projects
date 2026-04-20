import matplotlib.pyplot as plt

# -------------------------------
# 1. Line Plot
# -------------------------------
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o', linestyle='--', linewidth=2, label='Sales')
plt.title("Line Plot Example")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()


# -------------------------------
# 2. Bar Chart
# -------------------------------
students = ['A', 'B', 'C', 'D']
marks = [85, 90, 78, 88]

plt.figure(figsize=(8, 5))
plt.bar(students, marks)
plt.title("Bar Chart Example")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(axis='y')
plt.show()


# -------------------------------
# 3. Horizontal Bar Chart
# -------------------------------
plt.figure(figsize=(8, 5))
plt.barh(students, marks)
plt.title("Horizontal Bar Chart")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.show()


# -------------------------------
# 4. Scatter Plot
# -------------------------------
height = [150, 155, 160, 165, 170]
weight = [50, 55, 58, 65, 70]

plt.figure(figsize=(8, 5))
plt.scatter(height, weight)
plt.title("Scatter Plot Example")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.grid(True)
plt.show()


# -------------------------------
# 5. Histogram
# -------------------------------
ages = [18, 19, 20, 21, 22, 18, 19, 20, 21, 22, 23, 24, 20, 21]

plt.figure(figsize=(8, 5))
plt.hist(ages, bins=5, edgecolor='black')
plt.title("Histogram Example")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# -------------------------------
# 6. Pie Chart
# -------------------------------
languages = ['Python', 'Java', 'C++', 'JavaScript']
popularity = [40, 25, 20, 15]

plt.figure(figsize=(8, 5))
plt.pie(popularity, labels=languages, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart Example")
plt.show()


# -------------------------------
# 7. Box Plot
# -------------------------------
data = [10, 12, 14, 15, 18, 20, 21, 22, 100]

plt.figure(figsize=(8, 5))
plt.boxplot(data)
plt.title("Box Plot Example")
plt.ylabel("Values")
plt.show()