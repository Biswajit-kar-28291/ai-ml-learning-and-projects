import pandas as pd

# 1. Load dataset
df = pd.read_csv("02-pandas\Employee_Salary_Dataset.csv")

print("Original Data:")
print(df)

# 2. Basic information
print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nInfo:")
print(df.info())

print("\nDescribe:")
print(df.describe())

# 3. Missing values
print("\nMissing values:")
print(df.isnull().sum())

# 4. Fill missing salary with average salary
avg_salary = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(avg_salary)

print("\nAfter filling missing Salary with average:")
print(df)

# 5. Remove duplicates
df = df.drop_duplicates()

print("\nAfter removing duplicates:")
print(df)

# 6. Analysis
print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nLowest Salary:")
print(df["Salary"].min())

print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())

print("\nEmployees with Salary > 55000:")
print(df[df["Salary"] > 55000])

print("\nEmployees from IT Department:")
print(df[df["Department"] == "IT"])

print("\nEmployees with Experience > 3:")
print(df[df["Experience"] > 3])

# 7. Add new column
df["Level"] = df["Experience"].apply(lambda x: "Senior" if x >= 5 else "Junior")

print("\nAfter adding Level column:")
print(df)

# 8. Sort by Salary descending
df = df.sort_values(by="Salary", ascending=False)

print("\nSorted by Salary descending:")
print(df)

# 9. Save cleaned data
df.to_csv("cleaned_employees.csv", index=False)

print("\nCleaned data saved as cleaned_employees.csv")