import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", palette="deep")

df = sns.load_dataset("tips")

print(df.head())

# 1 Histogram
sns.histplot(data=df, x="total_bill", kde=True)
plt.title("Histogram + KDE")
plt.show()

# 2 KDE
sns.kdeplot(data=df, x="total_bill", fill=True)
plt.title("KDE Plot")
plt.show()

# 3 ECDF
sns.ecdfplot(data=df, x="total_bill")
plt.title("ECDF Plot")
plt.show()

# 4 Scatter
sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex")
plt.title("Scatter Plot")
plt.show()

# 5 Line
sns.lineplot(data=df, x="size", y="total_bill", hue="sex")
plt.title("Line Plot")
plt.show()

# 6 Bar
sns.barplot(data=df, x="day", y="total_bill", hue="sex")
plt.title("Bar Plot")
plt.show()

# 7 Count
sns.countplot(data=df, x="day", hue="sex")
plt.title("Count Plot")
plt.show()

# 8 Box
sns.boxplot(data=df, x="day", y="total_bill")
plt.title("Box Plot")
plt.show()

# 9 Violin
sns.violinplot(data=df, x="day", y="total_bill")
plt.title("Violin Plot")
plt.show()

# 10 Strip
sns.stripplot(data=df, x="day", y="total_bill")
plt.title("Strip Plot")
plt.show()

# 11 Swarm
sns.swarmplot(data=df, x="day", y="total_bill")
plt.title("Swarm Plot")
plt.show()

# 12 Point
sns.pointplot(data=df, x="day", y="total_bill")
plt.title("Point Plot")
plt.show()

# 13 Regression
sns.regplot(data=df, x="total_bill", y="tip")
plt.title("Regression Plot")
plt.show()

# 14 Heatmap
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Heatmap")
plt.show()

# 15 Relplot
sns.relplot(data=df, x="total_bill", y="tip", hue="sex", kind="scatter")
plt.show()

# 16 Catplot
sns.catplot(data=df, x="day", y="total_bill", kind="box")
plt.show()

# 17 Displot
sns.displot(data=df, x="total_bill", kde=True)
plt.show()

# 18 Jointplot
sns.jointplot(data=df, x="total_bill", y="tip", kind="scatter")
plt.show()

# 19 Pairplot
iris = sns.load_dataset("iris")
sns.pairplot(iris, hue="species")
plt.show()