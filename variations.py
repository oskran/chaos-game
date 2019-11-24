import numpy as np
import matplotlib.pyplot as plt
from chaos_game import ChaosGame
from fern import Fern


class Variations:
    """Transforms a set of coordinates using a fractal flame algorithm."""

    # Exercise 4a) Implementing the variations

    def __init__(self, x, y, colors="black"):
        self.colors = colors
        self.x = x
        self.y = y
        self.r = np.sqrt(np.power(x, 2) + np.power(y, 2))
        self.theta = np.arctan2(x, y)
        self.phi = np.arctan2(y, x)
        self.collection = {
            "linear": self.linear,
            "swirl": self.swirl,
            "handkerchief": self.handkerchief,
            "disc": self.disc,
        }

    def __call__(self, coefficients, variations):
        """Returns coordinates transformed by a linear combination of variations.

        Takes a list of variations and a list weights, and creates a linear 
        combination of variations. Then takes the list of x and y coordinates
        and transforms them using the combined variation.

        Parameters
        ----------
        coefficients : List of float
            The weight given to each variation
        variations : List of str
            Names of the variations

        Returns
        -------
        u, v : ndarray
            Transformed coordinates
        """

        coefficients = coefficients / np.sum(coefficients)
        u_temp = np.zeros(shape=(self.x.size))
        v_temp = np.zeros(shape=(self.y.size))

        for i, coef in enumerate(coefficients):
            self.collection[variations[i]]()

            u_temp = u_temp + (coef * self.u)
            v_temp = v_temp + (coef * self.v)

        self.u = u_temp
        self.v = v_temp

        return u_temp, v_temp

    def linear(self):
        self.u = self.x
        self.v = self.y

    def handkerchief(self):
        self.u = self.r * np.sin(self.theta + self.r)
        self.v = self.r * np.cos(self.theta - self.r)

    def swirl(self):
        self.u = self.x * np.sin(np.power(self.r, 2)) - self.y * np.cos(
            np.power(self.r, 2)
        )
        self.v = self.x * np.cos(np.power(self.r, 2)) + self.y * np.sin(
            np.power(self.r, 2)
        )

    def disc(self):
        self.u = (self.theta / np.pi) * np.sin(np.pi * self.r)
        self.v = (self.theta / np.pi) * np.cos(np.pi * self.r)

    # Exercise 4b) Testing the implementation

    def plot(self, cmap):
        """Generates a plot of the transformed coordinates.

        Parameters
        ----------
        cmap : str
            The color specification
        """
        plt.scatter(self.u, -self.v, c=self.colors, cmap=cmap, s=0.1)
        plt.axis("off")


# Exercise 4c) Plotting variations
# Exercise 4c) Linear combinations of variations
if __name__ == "__main__":

    def plot_grid():
        plt.plot([-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1], color="grey")
        plt.plot([-1, 1], [0, 0], color="grey")
        plt.plot([0, 0], [-1, 1], color="grey")

    variations = ["linear", "handkerchief", "swirl", "disc"]

    def grid():
        N = 60
        grid_values = np.linspace(-1, 1, N)
        x_values = np.ones(N * N)
        y_values = np.ones(N * N)
        for i in range(N):
            index = i * N
            x_values[index : index + N] *= grid_values[i]
            y_values[index : index + N] *= grid_values

        coords_varia = Variations(x_values, y_values)

        plt.figure(10, figsize=(9, 9))

        for i, variation in enumerate(variations):
            plt.subplot(221 + i)
            plot_grid()
            coords_varia.collection[variation]()
            coords_varia.plot("jet")
            plt.title(variation)

        plt.show()
        plt.close()

    def triangle_variations():
        triangle = ChaosGame(4, 1 / 3)
        triangle.iterate(10000)
        tri_variations = Variations(
            triangle.points[:, 0], -triangle.points[:, 1], colors=triangle.colors
        )

        plt.figure(10, figsize=(9, 9))

        for i, variation in enumerate(variations):
            plt.subplot(221 + i)
            plot_grid()
            tri_variations.collection[variation]()
            tri_variations.plot("jet")
            plt.title(variation)

        plt.show()
        plt.close()

    def fern_variations():
        fern = Fern()
        fern.iterate(50000)
        points = fern.points

        # Normalize between -1 and 1
        points[:, 0] = np.interp(
            points[:, 0], (points[:, 0].min(), points[:, 0].max()), (-1, +1)
        )
        points[:, 1] = np.interp(
            points[:, 1], (points[:, 1].min(), points[:, 1].max()), (-1, +1)
        )

        fern_vars = Variations(points[:, 0], -points[:, 1], colors="green")

        plt.figure(10, figsize=(9, 9))

        for i, variation in enumerate(variations):
            plt.subplot(221 + i)
            plot_grid()
            fern_vars.collection[variation]()
            fern_vars.plot("jet")
            plt.title(variation)

        plt.show()

    # Exercise 4d) Plotting linear combinations of variations
    def linear_combinations_fern():
        random_coefficients = []
        for i in range(4):
            random_coefficients.append(np.random.random())

        fern = Fern()
        fern.iterate(50000)
        points = fern.points

        # Normalize between -1 and 1
        points[:, 0] = np.interp(
            points[:, 0], (points[:, 0].min(), points[:, 0].max()), (-1, +1)
        )
        points[:, 1] = np.interp(
            points[:, 1], (points[:, 1].min(), points[:, 1].max()), (-1, +1)
        )

        fern_vars = Variations(points[:, 0], -points[:, 1], colors="green")

        plt.figure(10, figsize=(9, 9))

        for i, variation in enumerate(random_coefficients):
            plt.subplot(221 + i)
            plot_grid()
            fern_vars(
                [random_coefficients[i], 1 - random_coefficients[i]],
                ["swirl", "linear"],
            )
            fern_vars.plot("jet")
            plt.title(random_coefficients[i])

        plt.show()
        plt.close()

    def linear_combinations_ngon():
        random_coefficients = []
        for i in range(4):
            random_coefficients.append(np.random.random())

        triangle = ChaosGame(4, 1 / 3)
        triangle.iterate(10000)
        tri_variations = Variations(
            triangle.points[:, 0], -triangle.points[:, 1], colors=triangle.colors
        )

        plt.figure(10, figsize=(9, 9))

        for i, variation in enumerate(variations):
            plt.subplot(221 + i)
            plot_grid()
            tri_variations(
                [random_coefficients[i], 1 - random_coefficients[i]],
                ["handkerchief", "disc"],
            )
            tri_variations.plot("jet")
            plt.title(random_coefficients[i])

        plt.show()
        plt.close()

    grid()
    triangle_variations()
    fern_variations()
    linear_combinations_fern()
    linear_combinations_ngon()
