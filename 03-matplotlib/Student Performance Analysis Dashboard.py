import os
import pandas as pd
import matplotlib.pyplot as plt

# Create charts folder if not exists
os.makedirs("charts", exist_ok=True)

# Load data
df = pd.read_csv("data/students.csv")

# Create new columns
df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# Print basic information
print("Student Data:\n")
print(df)

print("\nTopper:")
topper = df.loc[df["Total"].idxmax()]
print(topper[["Name", "Total", "Average"]])

print("\nAverage marks of all students:")
print(df["Average"].mean())

# -------------------------------
# 1. Bar Chart - Total marks
# -------------------------------
plt.figure(figsize=(10, 5))
plt.bar(df["Name"], df["Total"])
plt.title("Total Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/total_marks_bar.png")
plt.show()

# -------------------------------
# 2. Line Chart - Average marks
# -------------------------------
plt.figure(figsize=(10, 5))
plt.plot(df["Name"], df["Average"], marker='o')
plt.title("Average Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/average_marks_line.png")
plt.show()

# -------------------------------
# 3. Scatter Plot - Study Hours vs Average Marks
# -------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(df["StudyHours"], df["Average"])
plt.title("Study Hours vs Average Marks")
plt.xlabel("Study Hours")
plt.ylabel("Average Marks")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/studyhours_vs_marks_scatter.png")
plt.show()

# -------------------------------
# 4. Histogram - Total marks distribution
# -------------------------------
plt.figure(figsize=(8, 5))
plt.hist(df["Total"], bins=5, edgecolor="black")
plt.title("Distribution of Total Marks")
plt.xlabel("Total Marks")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("charts/total_marks_histogram.png")
plt.show()

# -------------------------------
# 5. Pie Chart - Pass/Fail
# -------------------------------
result_counts = df["Result"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(result_counts, labels=result_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Pass vs Fail")
plt.tight_layout()
plt.savefig("charts/pass_fail_pie.png")
plt.show()

# -------------------------------
# 6. Box Plot - Marks distribution
# -------------------------------
plt.figure(figsize=(8, 5))
plt.boxplot([df["Math"], df["Science"], df["English"]], labels=["Math", "Science", "English"])
plt.title("Subject-wise Marks Distribution")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("charts/subject_boxplot.png")
plt.show()