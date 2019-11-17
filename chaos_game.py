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

        corners = np.zeros(shape=(self.n, 2))

        for i in range(self.n):
            c1 = np.sin(theta[i])
            c2 = np.cos(theta[i])

            corners[i] = [c1, c2]

        self.corners = corners

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
        corner_list = np.zeros(shape=(steps,))
        random_corner = np.random.randint(self.n)
        corner_list[0] = random_corner

        midway_point = (
            self.r * self.st_point + (1 - self.r) * self.corners[random_corner]
        )

        points = np.zeros(shape=(steps, 2))
        points[0] = midway_point

        for i in range(1, steps):
            random_corner = np.random.randint(self.n)
            corner_list[i] = random_corner

            points[i] = (
                self.r * points[i - 1] + (1 - self.r) * self.corners[random_corner]
            )

        self.corner_list = corner_list[discard:]
        self.points = points[discard:]

    def plot(self, color=False, cmap="jet"):
        if color == True:
            colors = self.corner_list
        else:
            colors = "black"

        plt.scatter(*zip(*self.points), s=1, c=colors, cmap=cmap)

        plt.axis("equal")

    def show(self, color=False, cmap="jet"):
        self.plot(color=color, cmap=cmap)
        plt.show()

    def savepng(self, outfile, color=False, cmap="jet"):

        outfile = outfile.split(".")

        if len(outfile) != 1:
            assert outfile[1] == "png", "Output file format must be .png"

        self.plot(color=color, cmap=cmap)

        plt.savefig(outfile[0] + ".png", dpi=300)


game = ChaosGame(3, 0.5)

game.iterate(10000)

game.show(color=True)
game.savepng("output.png", color=True)
