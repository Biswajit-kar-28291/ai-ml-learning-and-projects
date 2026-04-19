import numpy as np

print("===== NUMPY MINI PROJECT: SALARY ANALYSIS =====")

# -----------------------------------
# DATA (Simulated Company Data)
# -----------------------------------
employee_ids = np.arange(1, 11)
salaries = np.array([25000, 30000, 28000, 35000, 40000, 27000, 32000, 45000, 50000, 29000])
experience = np.array([1, 3, 2, 5, 7, 2, 4, 8, 10, 3])

# -----------------------------------
# BASIC ANALYSIS
# -----------------------------------
print("\n--- Basic Statistics ---")
print("Average Salary:", np.mean(salaries))
print("Highest Salary:", np.max(salaries))
print("Lowest Salary:", np.min(salaries))

# -----------------------------------
# FILTERING (Important Real Use)
# -----------------------------------
print("\n--- Employees with Salary > 30000 ---")
high_salary = salaries[salaries > 30000]
print(high_salary)

# -----------------------------------
# EXPERIENCE BASED ANALYSIS
# -----------------------------------
print("\n--- Experienced Employees (>5 years) ---")
experienced = salaries[experience > 5]
print(experienced)

# -----------------------------------
# SALARY INCREMENT (10%)
# -----------------------------------
print("\n--- Salary After 10% Increment ---")
incremented_salary = salaries * 1.10
print(incremented_salary.astype(int))

# -----------------------------------
# PERFORMANCE BONUS (CONDITION)
# -----------------------------------
print("\n--- Bonus (Salary > 40000 gets 5000 bonus) ---")
bonus = np.where(salaries > 40000, salaries + 5000, salaries)
print(bonus)

# -----------------------------------
# SORTING DATA
# -----------------------------------
print("\n--- Sorted Salaries ---")
print(np.sort(salaries))

# -----------------------------------
# CORRELATION (Experience vs Salary)
# -----------------------------------
correlation = np.corrcoef(experience, salaries)
print("\n--- Correlation Matrix ---")
print(correlation)

# -----------------------------------
# FINAL SUMMARY
# -----------------------------------
print("\n===== FINAL INSIGHTS =====")
print("Total Employees:", len(employee_ids))
print("Employees earning >30000:", len(high_salary))
print("Employees with >5 yrs experience:", len(experienced))
print("Average Salary After Increment:", int(np.mean(incremented_salary)))

print("\n===== END OF PROJECT =====")