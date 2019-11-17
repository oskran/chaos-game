import numpy as np
import matplotlib.pyplot as plt

c0 = np.array([0, 0], dtype="float")
c1 = np.array([0, 1], dtype="float")

c2 = [
    -((c0[0] + c1[0] + np.sqrt(3) * (c0[1] - c1[1])) / 2),
    ((c0[1] + c1[1] + np.sqrt(3) * (c1[0] - c0[0])) / 2),
]

print(c2)

corners = [c0, c1, c2]

plt.scatter(*zip(*corners))

axes = plt.axes()

plt.show()
