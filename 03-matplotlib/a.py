# import matplotlib.pyplot as plt

# x=[1,2,3,4,5,6]
# y=[1,2,3,4,5,6]
# y1 = [10, 20, 30, 40,50,60]
# y2 = [15, 25, 35, 45,55,65]
# plt.title("for testing char")
# plt.xlabel("hi")
# plt.ylabel("hello")
# plt.plot(x,y, color='red', linestyle="--",marker="o", linewidth=1)
# # plt.bar(x,y)
# # plt.scatter(x,y)
# # plt.pie(x,y)
# # plt.hist(x,bins=5)
# # plt.boxplot(x)
# # plt.fill_between(x,y)

# # plt.plot(x, y1, label="Product A")
# # plt.plot(x, y2, label="Product B")
# # plt.legend()
# # plt.figure(figsize=(8, 5))
# plt.grid(True)

# plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [10, 20, 15]

plt.plot(x, y, marker='o')
plt.annotate("Highest", xy=(2, 20), xytext=(2.2, 22),
             arrowprops=dict(facecolor='black'))
plt.show()