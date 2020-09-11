import numpy as np
import matplotlib.pyplot as plt


class Triangle:
    def __init__(self):
        """Triangle object.

        Attributes
        ----------
        corners : ndarray of int (3, 2)
            Coordinates of the triangles corners.
        points : ndarray of int
            Coordinates of generated points within the triangle.
        iteration : String
            Description of which iteration method was used.
        color : ndarray
            Color values for each point to be used in the plotting method.
        """
        self.corners = self.create_triangle()

    def create_triangle(self):
        """Returns coordinates for the three corners of the triangle.

        Takes the coordinates of the first two corners as given, an calculates
        the coordinates of the last triangle so that it is equilateral.
        By definition, given v1=(x1, y1), v2=(x2, y2), and v3=(x3, y3),
        v3 = ((x1 + x2 + Sqrt[3]*(y1 - y2))/2, (y1 + y2 + Sqrt[3]*(x2 - x1))/2) 

        Returns
        -------
        List of floats (3, 2)
            Coordinates of the three corners of the equilateral triangle
        """
        c0 = np.array([0, 0])
        c1 = np.array([1, 0])

        c2 = [
            ((c0[0] + c1[0] + np.sqrt(3) * (c0[1] - c1[1])) / 2),
            ((c0[1] + c1[1] + np.sqrt(3) * (c1[0] - c0[0])) / 2),
        ]

        return [c0, c1, c2]

    def random_starting_point(self):
        """Returns a random point inside the triangle

        finds a random point inside the triangle by taking the coordinates 
        of the three corners and giving multiplying them with random weights.

        Returns
        -------
        point: ndarray of floats
            Coordinates of random point inside the triangle
        """
        c0, c1, c2 = self.corners[0], self.corners[1], self.corners[2]

        w = np.zeros(3)  # Array to store weights

        for i in range(w.size):
            w[i] = np.random.random()

        # Divide all weights by the sum of the weights so that they sum to one
        w = w / np.sum(w)

        point = np.array(
            [
                c0[0] * w[0] + c1[0] * w[1] + c2[0] * w[2],
                c0[1] * w[0] + c1[1] * w[1] + c2[1] * w[2],
            ]
        )

        return point

    def iterate(self, n):
        """Generates points withing the triangle iteratively.

        Starts at a random point within the triangle and finds the point
        that is halfway between the current point and a randomly picked corner.
        Also sets the iteration parameter to be "black".

        Parameters
        ----------
        n : int
            Number of iterations
        """
        random_corner = np.random.randint(3)
        points = np.zeros(shape=(n, 2))
        points[0] = (self.random_starting_point() + self.corners[random_corner]) / 2

        for i in range(1, n):
            random_corner = np.random.randint(3)
            points[i] = (points[i - 1] + self.corners[random_corner]) / 2

        self.points = points
        self.iteration = "black"

    def iterate_color(self, n):
        """Generates points and saves the randomly picked corners in an array.

        Does the same thing as iterate(), but also stores the randomly picked
        corners in an ndarray named color. Sets the iteration parameter to be
        "color".

        Parameters
        ----------
        n : int
            Number of iterations
        """

        color = np.zeros(shape=(n,))  # Array to store randomly picked corners
        random_corner = np.random.randint(3)
        color[0] = random_corner

        points = np.zeros(shape=(n, 2))
        points[0] = (self.random_starting_point() + self.corners[random_corner]) / 2

        for i in range(1, n):
            random_corner = np.random.randint(3)
            color[i] = random_corner
            points[i] = (points[i - 1] + self.corners[random_corner]) / 2

        self.points = points
        self.color = color
        self.iteration = "color"

    def iterate_gradient(self, n):
        """Generates points and assigns them a RGB color value

        Does the same thing as iterate(), but also assigns a RGB color value
        to each point by having each corner corespond to an RBG value, and 
        for each point calculating:
        (previous points RGB value + current corners RGB value) / 2
        so that the triangle has a continuous color gradient.

        Parameters
        ----------
        n : int
            Number of iterations
        """
        color = np.zeros(shape=(n, 3))

        random_corner = np.random.randint(3)

        # RGB values coresponding to each corner index
        if random_corner == 0:
            color[0] = [1, 0, 0]

        if random_corner == 1:
            color[0] = [0, 1, 0]

        if random_corner == 2:
            color[0] = [0, 0, 1]

        points = np.zeros(shape=(n, 2))
        points[0] = (self.random_starting_point() + self.corners[random_corner]) / 2

        for i in range(1, n):
            random_corner = np.random.randint(3)

            if random_corner == 0:
                r = [1, 0, 0]

            if random_corner == 1:
                r = [0, 1, 0]

            if random_corner == 2:
                r = [0, 0, 1]

            color[i] = (color[i - 1] + r) / 2

            points[i] = (points[i - 1] + self.corners[random_corner]) / 2

        self.points = points
        self.color = color
        self.iteration = "gradient"

    def plot(self):
        """Plots the triangle.

        Checks which iteration function was last called on, and plots the
        coresponding colors accordingly.
        """
        if self.iteration == "color":
            red = self.points[self.color == 0]
            green = self.points[self.color == 1]
            blue = self.points[self.color == 2]

            plt.scatter(*zip(*red[5:]), s=0.1, color="red")
            plt.scatter(*zip(*green[5:]), s=0.1, color="green")
            plt.scatter(*zip(*blue[5:]), s=0.1, color="blue")

        if self.iteration == "gradient":
            plt.scatter(*zip(*self.points[5:]), s=0.1, color=self.color[5:])

        if self.iteration == "black":
            plt.scatter(*zip(*self.points[5:]), s=0.1, color="black")

        plt.axis("equal")
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    figure = Triangle()
    figure.iterate(10000)
    figure.plot()
    figure.iterate_color(10000)
    figure.plot()
    figure.iterate_gradient(10000)
    figure.plot()
