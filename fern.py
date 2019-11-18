import numpy as np
import matplotlib.pyplot as plt


class AffineTransform:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self, x, y):
        return np.array([[self.a, self.b], [self.c, self.d]]) @ np.array(
            [x, y]
        ) + np.array([self.e, self.f])


func1 = AffineTransform(0, 0, 0, 0.16, 0, 0)
func2 = AffineTransform(0.85, 0.04, -0.04, 0.85, 0, 1.60)
func3 = AffineTransform(0.20, -0.26, 0.23, 0.22, 0, 1.60)
func4 = AffineTransform(-0.15, 0.28, 0.26, 0.24, 0, 0.44)

functions = [func1, func2, func3, func4]

prob = [0.01, 0.85, 0.07, 0.07]
prob_cumulative = np.cumsum(prob)


def choose_function():
    r = np.random.random()
    for j, p in enumerate(prob_cumulative):
        if r < p:
            return functions[j]


n = 50000

points = np.zeros(shape=(n, 2))
points[0] = [0, 0]

for i in range(1, n):
    func = choose_function()
    points[i] = func(points[i - 1][0], points[i - 1][1])

plt.scatter(*zip(*points), s=1, c="green")
plt.axis("equal")
plt.show()
