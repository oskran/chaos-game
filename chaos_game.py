import numpy as np
import matplotlib.pyplot as plt


class ChaosGame:
    """A chaos game object.

        Attributes
        ----------
        n : int
            Number of sides
        r : float
            Ratio between two points
        st_point : ndarray (2, ) of int
            Coordinates for the random starting point
        corners : ndarray (n, 2) of int
            Coordinates for the ngon corners
        corner_list : ndarray (dicard:n, )
            List of the randomly picked corner indexes
        points : ndarray (discard:n, 2)
            Coordinates for the randomly picked points
        ----------
        n : int
            Number of sides
        r : float
            Ratio between two points
    """

    def __init__(self, n, r):
        assert isinstance(n, int), "n must be of type int"
        assert isinstance(r, float), "r must be of type float"

        # assert n >= 3, "n must be larger or equal to 3"
        # assert r > 0 and r < 1, "r must be between 0 and 1"
        if not n >= 3:
            raise ValueError("n must be larger or equal to 3")
        if not 0 < r < 1:
            raise ValueError("r must be between 0 and 1")

        self.n = n
        self.r = r

        self._generate_ngon()
        self.st_point = self._starting_point()

    def _generate_ngon(self):
        """Generates the corners of a ngon, for a given number of sides."""
        theta = np.linspace(0, (np.pi * 2), self.n + 1)

        corners = np.zeros(shape=(self.n, 2))

        for i in range(self.n):
            c1 = np.sin(theta[i])
            c2 = np.cos(theta[i])

            corners[i] = [c1, c2]

        self.corners = corners

    def plot_ngon(self):
        """Plots the ngon."""
        plt.scatter(*zip(*self.corners))

        plt.axis("equal")
        plt.show()

    def _starting_point(self):
        """Returns a random starting point inside the ngon.

        Finds a random point inside the ngon by taking the coordinates 
        of the corners and multiplying them with random weights.

        Returns
        -------
        point : ndarray (2, )
            Random starting point
        """
        w = np.zeros(self.n)

        for i in range(w.size):
            w[i] = np.random.random()

        # Divide all weights by the sum of the weights so that they sum to one
        w = w / np.sum(w)

        point = np.zeros(2)

        for i, c in enumerate(self.corners):
            point[0] = point[0] + c[0] * w[i]
            point[1] = point[1] + c[1] * w[i]

        return point

    def iterate(self, steps, discard=5):
        """Generates points by picking a corner randomly.

        Generated the first point based on the starting point. Iterates step
        number of times, and discards the first generated points.

        Parameters
        ----------
        steps : int
            Number of iterations / points to be generated
        discard : int, optional
            Number of first points to be discarded, by default 5
        """

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
        self.colors = self._compute_color()
        self.points = points[discard:]

    def plot(self, color=False, cmap="jet"):
        """Creates a plot of the generated points.

        Parameters
        ----------
        color : bool, optional
            Uses a color gradient if True, and keeps the points black if False
            , by default False
        cmap : str, optional
            [description], by default "jet"
        """

        if color == True:
            colors = self.colors
        else:
            colors = "black"

        plt.scatter(*zip(*self.points), s=1, c=colors, cmap=cmap)

        plt.axis("equal")

    def show(self, color=False, cmap="jet"):
        """Creates a plot of the generated points and shows it.

        Parameters
        ----------
        color : bool, optional
            Uses a color gradient if True, and keeps the points black if False
            , by default False
        cmap : str, optional
            [description], by default "jet"
        """

        self.plot(color=color, cmap=cmap)
        plt.show()
        plt.close()

    def _compute_color(self):
        """Computes the points to be used as the color gradient when plotting.

        Returns
        -------
        color : ndarray
            [description]
        """

        color = np.zeros(shape=(self.corner_list.shape[0],))

        for i, corner in enumerate(self.corner_list):
            color[i] = (color[i - 1] + self.corner_list[i]) / 2

        return color

    def savepng(self, outfile, color=False, cmap="jet"):
        """Creates a plot and saves it as a png file.

        Parameters
        ----------
        outfile : String
            Name of the output file, must be .png or have no file extension.
        color : bool, optional
            Uses a color gradient if True, and keeps the points black if False
            , by default False
        cmap : str, optional
            [description], by default "jet"
        """

        outfile = outfile.split(".")

        if len(outfile) != 1:
            assert outfile[1] == "png", "Output file format must be .png"

        self.plot(color=color, cmap=cmap)

        plt.savefig("figures/" + outfile[0] + ".png", dpi=300)
        plt.close()


if __name__ == "__main__":

    figure_list = [[3, 1 / 2], [4, 1 / 3], [5, 1 / 3], [5, 3 / 8], [6, 1 / 3]]

    for i, figure in enumerate(figure_list):
        game = ChaosGame(figure[0], figure[1])

        game.iterate(10000)
        game.show(color=True)
        game.savepng(f"chaos{i}.png", color=True)
