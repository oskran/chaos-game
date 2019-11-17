import numpy as np
import matplotlib.pyplot as plt

# Creates list of coordinates in a equilateral triangle
def create_triangle():
    c0 = np.array([0, 0], dtype="float")
    c1 = np.array([0, 1], dtype="float")

    c2 = [
        -((c0[0] + c1[0] + np.sqrt(3) * (c0[1] - c1[1])) / 2),
        ((c0[1] + c1[1] + np.sqrt(3) * (c1[0] - c0[0])) / 2),
    ]

    return [c0, c1, c2]


# Create list of random weigths for a given triangle
def random_point(corners):

    c0, c1, c2 = corners[0], corners[1], corners[2]

    w = np.zeros(3)

    for i in range(w.size):
        w[i] = np.random.random()

    # Divide all weigths by the sum of the weigths so that they sum to one
    w = w / np.sum(w)

    point = [
        c0[0] * w[0] + c1[0] * w[1] + c2[0] * w[2],
        c0[1] * w[0] + c1[1] * w[1] + c2[1] * w[2],
    ]

    return point


def random_corner_point(point, corners):

    random_corner = np.random.randint(3)

    halfway_point = (point + corners[random_corner]) / 2

    return halfway_point


corners = create_triangle()
points = [random_point(corners)]

for i in range(1, 10000):
    points.append(random_corner_point(points[i - 1], corners))


plt.scatter(*zip(*points[5:]))

plt.axis("equal")
plt.show()
