class ChaosGame:
    def __init__(self, n, r):
        assert isinstance(n, int), "n must be of type int"
        assert isinstance(r, float), "r must be of type float"

        assert n >= 3, "n must be larger or equal to 3"
        assert r > 0 and r < 1, "r must be between 0 and 1"


game = ChaosGame(3, 0.5)
