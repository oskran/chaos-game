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

    def _generate_ngon(self):
        """Generates the ngon for a given number of sides
        """
        theta = np.linspace(0, (np.pi * 2), self.n + 1)

        c = []

        for i in range(self.n):
            c1 = np.sin(theta[i])
            c2 = np.cos(theta[i])

            c.append([c1, c2])

        self.corners = c

    def plot_ngon(self):
        """Plots the ngon
        """
        plt.scatter(*zip(*self.corners))

        plt.axis("equal")
        plt.show()


game = ChaosGame(5, 0.5)

game.plot_ngon()
