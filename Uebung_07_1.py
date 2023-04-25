import matplotlib.pyplot as plt
import random

farben = []
x = []
y = []
for i in range(1000):
    x.append(random.randint(-100,100))
    y.append(random.randint(-100,100))
    farben.append((random.random(), random.random(), random.random()))

plt.scatter(x, y, c=farben)
plt.xlabel("x-Achse")
plt.ylabel("y-Achse")
plt.grid(True)
plt.axis('equal')
plt.show()



