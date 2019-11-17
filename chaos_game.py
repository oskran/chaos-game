import numpy as np


class ChaosGame:
    def __init__(self, n, r):
        assert isinstance(n, int), "n must be of type int"
        assert isinstance(r, float), "r must be of type float"

        assert n >= 3, "n must be larger or equal to 3"
        assert r > 0 and r < 1, "r must be between 0 and 1"

        self.n = n
        self.r = r

    def _generate_ngon(self):

        theta = np.linspace(0, np.pi * 2, self.n)


game = ChaosGame(3, 0.5)

