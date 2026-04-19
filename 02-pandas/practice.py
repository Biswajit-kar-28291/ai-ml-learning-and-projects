import pandas as pd

# -------------------------------
# 1. Create Series
# -------------------------------
s = pd.Series([10, 20, 30, 40])
print("Series:\n", s)

# -------------------------------
# 2. Create DataFrame
# -------------------------------
data = {
    "Name": ["Amit", "Riya", "John"],
    "Age": [21, 22, 20]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# -------------------------------
# 3. Select Column
# -------------------------------
print("\nSelect Name column:\n", df["Name"])

# -------------------------------
# 4. Filter Data
# -------------------------------
print("\nFilter Age > 21:\n", df[df["Age"] > 21])

# -------------------------------
# 5. Add Column
# -------------------------------
df["Salary"] = [50000, 60000, 55000]
print("\nAfter Adding Salary:\n", df)

# -------------------------------
# 6. Apply Function
# -------------------------------
df["Level"] = df["Salary"].apply(lambda x: "High" if x > 55000 else "Low")
print("\nAfter Apply:\n", df)

# -------------------------------
# 7. Sorting
# -------------------------------
print("\nSorted by Salary:\n", df.sort_values(by="Salary", ascending=False))

# -------------------------------
# 8. GroupBy
# -------------------------------
group = df.groupby("Level")["Salary"].mean()
print("\nGroupBy Level:\n", group)

# -------------------------------
# 9. Missing Values
# -------------------------------
df2 = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Salary": [50000, None, 60000]
})
print("\nMissing Data:\n", df2)

df2["Salary"].fillna(0, inplace=True)
print("\nAfter Fill Missing:\n", df2)

# -------------------------------
# 10. Merge
# -------------------------------
df1 = pd.DataFrame({"ID": [1, 2], "Name": ["Amit", "Riya"]})
df3 = pd.DataFrame({"ID": [1, 2], "Salary": [50000, 45000]})

merged = pd.merge(df1, df3, on="ID")
print("\nMerged Data:\n", merged)

# -------------------------------
# 11. Datetime
# -------------------------------
df4 = pd.DataFrame({"Date": ["2025-01-01", "2025-02-01"]})
df4["Date"] = pd.to_datetime(df4["Date"])
print("\nMonth Extracted:\n", df4["Date"].dt.month)

# -------------------------------
# 12. Pivot Table
# -------------------------------
data2 = {
    "Dept": ["IT", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 40000, 45000]
}
df5 = pd.DataFrame(data2)

pivot = pd.pivot_table(df5, values="Salary", index="Dept", aggfunc="mean")
print("\nPivot Table:\n", pivot)