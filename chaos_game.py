import numpy as np
import matplotlib.pyplot as plt


class ChaosGame:
    def __init__(self, n, r):
        """A chaos game object
        
        Parameters
        ----------
        n : int
            Number of sides
        r : float
            Ratio between two points 
        """
        assert isinstance(n, int), "n must be of type int"
        assert isinstance(r, float), "r must be of type float"

        assert n >= 3, "n must be larger or equal to 3"
        assert r > 0 and r < 1, "r must be between 0 and 1"

        self.n = n
        self.r = r

        self._generate_ngon()
        self.st_point = self._starting_point()

    def _generate_ngon(self):
        """Generates the ngon for a given number of sides
        """
        theta = np.linspace(0, (np.pi * 2), self.n + 1)

        c = np.zeros(shape=(self.n, 2))

        for i in range(self.n):
            c1 = np.sin(theta[i])
            c2 = np.cos(theta[i])

            c[i] = [c1, c2]

        self.corners = c

    def plot_ngon(self):
        """Plots the ngon
        """
        plt.scatter(*zip(*self.corners))

        plt.axis("equal")
        plt.show()

    def _starting_point(self):
        w = np.zeros(self.n)

        for i in range(w.size):
            w[i] = np.random.random()

        # Divide all weigths by the sum of the weigths so that they sum to one
        w = w / np.sum(w)

        point = np.zeros(2)

        for i, c in enumerate(self.corners):
            point[0] = point[0] + c[0] * w[i]
            point[1] = point[1] + c[1] * w[i]

        return point

    def iterate(self, steps, discard=5):
        random_corner = np.random.randint(self.n)

        midway_point = (
            self.r * self.st_point + (1 - self.r) * self.corners[random_corner]
        )

        points = np.zeros(shape=(steps, 2))
        points[0] = midway_point

        for i in range(1, steps):
            random_corner = np.random.randint(self.n)

            points[i] = (
                self.r * points[i - 1] + (1 - self.r) * self.corners[random_corner]
            )

        return points[discard:]


game = ChaosGame(3, 0.5)

points = game.iterate(1000)

plt.scatter(*zip(*points))

plt.axis("equal")
plt.show()
