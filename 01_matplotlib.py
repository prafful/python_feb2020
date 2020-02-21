import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y  = [22,245, 78, 88,56, 33, 54,45,99]

plt.plot(x, y, label="Day Score", color='r', marker="D" )


plt.xlabel("Day Number")
plt.ylabel("Score")
plt.legend(loc="upper left")
plt.title("Score on Each Day")
plt.show()