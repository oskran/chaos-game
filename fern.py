import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


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


function1 = AffineTransform(0, 0, 0, 0.16, 0, 0)
function2 = AffineTransform(0.85, 0.04, -0.04, 0.85, 0, 1.60)
function3 = AffineTransform(0.20, -0.26, 0.23, 0.22, 0, 1.60)
function4 = AffineTransform(-0.15, 0.28, 0.26, 0.24, 0, 0.44)
