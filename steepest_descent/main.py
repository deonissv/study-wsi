import numpy as np
from funcs import *
import matplotlib.pyplot as plt
from cec2017.functions import f1, f2, f3

def savePlot(func, step, max_x,):
    x_arr = np.arange(-max_x, max_x, max_x * 1e-2)
    y_arr = np.arange(-max_x, max_x, max_x * 1e-2)
    z_arr = np.empty((len(x_arr), len(y_arr)))

    for i in range(len(x_arr)):
        for j in range(len(y_arr)):
            z_arr[i, j] = func(np.array([x_arr[i], y_arr[j]]))

    plt.contour(x_arr, y_arr, z_arr)

    coords = steepestDescent(func, step, max_x)
    for i, coord in enumerate(coords[:-1]):
        plt.arrow(*coord, coords[i+1][0] - coord[0], coords[i+1][1] - coord[1], head_width=1, head_length=1)
    plt.title(f'{func.__name__}')
    plt.savefig(f'{func.__name__}.png', dpi=300)


savePlot(booth, 1e-1, 100)
savePlot(f1, 2e-8, 100)
savePlot(f2, 5e-1, 3000)
savePlot(f3, 1e-4, 100)


# Jak wartość parametru beta wpływa na szybkość dojścia do optimum i zachowanie algorytmu?
# 	zwiększenie parametru beta przyspiesza działanie algorytmu, ale w pewnym momencie może spowodować

# Zalety/wady algorytmu?

# 	+ stosunkowo szybki
# 	+ proswy w implementacji

# 	- wymaga dobranie parametru beta indywidualnie dla każdego problemu
# 	- wpada w oscylacje
# 	- "wpada" w minima lokalne

# Wnioski
# 	Algorytm może być przydatny w przypadku braku czasu na rozwiązanie problemu (lub małej mocy obliczeniowej).
# 	Oprócz tego jest praktyczny, jeśli beta i punkt początkowy są znane