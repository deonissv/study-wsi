import numpy as np
from autograd import grad

DIMENSIONALITY = 2
ITERATIONS = 10000

def booth(x):
    return (x[0] + 2 * x[1] - 7) ** 2 + (2 * x[0] + x[1] - 5) ** 2

def steepestDescent(func, step, max_x, point=()):
    if isinstance(point, (list, tuple)):
        point = np.random.uniform(-max_x, max_x, size=DIMENSIONALITY)
    arr = [(point[0], point[1])]
    for _ in range(ITERATIONS):
        grad_fct = grad(func)
        d = grad_fct(point)

        point[0] -= step * d[0]
        point[1] -= step * d[1]
        arr.append((point[0], point[1]))
    return arr
