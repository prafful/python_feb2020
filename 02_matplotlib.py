import matplotlib.pyplot as plt

fb_views = [400, 500, 600, 800, 200]
yt_views =  [800, 600, 900, 1200, 2000]
tw_views =  [200, 300, 400, 900, 3000]

days = range(1, 6)

plt.plot(days, fb_views, label="Facebook Views", color='r', marker='D')
plt.plot(days, yt_views, label="Youtube Views", color='g', marker='s')
plt.plot(days, tw_views, label="Twitter Views", color='b', marker='o')

plt.xlabel("Days")
plt.ylabel("Views")

plt.legend(loc = "upper left")

plt.title("Channel Views")
plt.grid(color='y', linestyle=":")
plt.savefig("Channel_Views.png", dpi=400)


plt.show()