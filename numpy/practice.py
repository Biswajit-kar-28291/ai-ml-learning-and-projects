import numpy as np

print("===== NUMPY COMPLETE GUIDE =====")

# -----------------------------------
# 1. ARRAY CREATION
# -----------------------------------
a = np.array([1, 2, 3, 4])
b = np.zeros((2, 3))
c = np.ones((2, 2))
d = np.arange(0, 10, 2)
e = np.linspace(0, 1, 5)
f = np.random.rand(3, 3)

print("\nArray:", a)
print("Zeros:\n", b)
print("Ones:\n", c)
print("Arange:", d)
print("Linspace:", e)
print("Random:\n", f)

# -----------------------------------
# 2. INDEXING & SLICING
# -----------------------------------
print("\nIndexing:", a[0])
print("Slicing:", a[1:3])

matrix = np.array([[1,2,3],[4,5,6]])
print("2D Index:", matrix[0,1])

# -----------------------------------
# 3. VECTORIZATION (NO LOOPS)
# -----------------------------------
x = np.array([1,2,3])
y = np.array([4,5,6])

print("\nAddition:", x + y)
print("Multiplication:", x * y)

# -----------------------------------
# 4. MATHEMATICAL FUNCTIONS
# -----------------------------------
print("\nSum:", np.sum(a))
print("Mean:", np.mean(a))
print("Std:", np.std(a))
print("Max:", np.max(a))
print("Min:", np.min(a))

# -----------------------------------
# 5. RESHAPING
# -----------------------------------
r = np.arange(6)
r2 = r.reshape(2,3)
print("\nReshape:\n", r2)

# -----------------------------------
# 6. BROADCASTING
# -----------------------------------
print("\nBroadcasting:", x * 2)

# -----------------------------------
# 7. MATRIX OPERATIONS
# -----------------------------------
m1 = np.array([[1,2],[3,4]])
m2 = np.array([[5,6],[7,8]])

print("\nDot Product:\n", np.dot(m1, m2))

# -----------------------------------
# 8. BOOLEAN MASKING
# -----------------------------------
arr = np.array([1,2,3,4,5])
print("\nFiltered (>2):", arr[arr > 2])

# -----------------------------------
# 9. RANDOM MODULE
# -----------------------------------
np.random.seed(42)
print("\nRandom numbers:", np.random.randint(1, 10, 5))

# -----------------------------------
# 10. AXIS CONCEPT
# -----------------------------------
data = np.array([[1,2,3],[4,5,6]])
print("\nColumn sum:", data.sum(axis=0))
print("Row sum:", data.sum(axis=1))

# -----------------------------------
# 11. LINEAR ALGEBRA
# -----------------------------------
print("\nDeterminant:", np.linalg.det(m1))
print("Inverse:\n", np.linalg.inv(m1))

# -----------------------------------
# 12. REAL-WORLD EXAMPLE
# -----------------------------------
salary = np.array([2000, 3000, 4000, 2500, 5000])

print("\n===== REAL WORLD ANALYSIS =====")
print("Average Salary:", np.mean(salary))
print("Highest Salary:", np.max(salary))
print("Employees >3000:", salary[salary > 3000])

print("\n===== END =====")