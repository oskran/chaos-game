import numpy as np
import matplotlib.pyplot as plt


class AffineTransform:
    """Affine transformation function.

    Takes a pair of coordinates, transforms them, and returns them.

    Parameters
    ----------
    a : float
        Parameter of the transformation function
    b : float
        Parameter of the transformation function
    c : float
        Parameter of the transformation function
    d : float
        Parameter of the transformation function
    e : float
        Parameter of the transformation function
    f : float
        Parameter of the transformation function
    Returns
    -------
    ndarray of float
        The transformed coordinates
    """

    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
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


class Fern:
    """Uses AffineTransform to create Barnsley Fern.

    Returns
    -------
    [type]
        [description]
    """

    def __init__(self):
        func1 = AffineTransform(0, 0, 0, 0.16, 0, 0)
        func2 = AffineTransform(0.85, 0.04, -0.04, 0.85, 0, 1.60)
        func3 = AffineTransform(0.20, -0.26, 0.23, 0.22, 0, 1.60)
        func4 = AffineTransform(-0.15, 0.28, 0.26, 0.24, 0, 0.44)
        self.functions = [func1, func2, func3, func4]

        probabilities = [0.01, 0.85, 0.07, 0.07]
        self.prob_cumulative = np.cumsum(probabilities)

    def choose_function(self):
        """Chooses a transformation function at random.

        Chooses based on a list of probabilities.

        Returns
        -------
        AffineTransform
            A randomly chosen transformation function
        """
        r = np.random.random()
        for j, p in enumerate(self.prob_cumulative):
            if r < p:
                return self.functions[j]

    def iterate(self, n):
        """Generates points iteratively by using affine transformations

        Parameters
        ----------
        n : int
            Number of iterations
        """
        self.n = n

        points = np.zeros(shape=(self.n, 2))
        points[0] = [0, 0]

        for i in range(1, self.n):
            func = self.choose_function()
            points[i] = func(points[i - 1][0], points[i - 1][1])

        self.points = points

    def plot(self, s=1, c="green"):
        """Plots the fern.

        Parameters
        ----------
        s : int, optional
            Size of the points, by default 1
        c : str, optional
            Color of the fern, by default "green"
        """
        plt.scatter(*zip(*self.points), s=s, c=c)
        plt.axis("equal")
        plt.savefig("figures/barnsley_fern.png", dpi=300)
        plt.show()


if __name__ == "__main__":
    fern = Fern()
    fern.iterate(50000)
    fern.plot(s=0.1)
