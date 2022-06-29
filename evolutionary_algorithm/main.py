import numpy as np
import matplotlib.pyplot as plt
from cec2017.functions import f4
from evol import evol
from math import sqrt

POPULATION_SIZE = 100
ELITE_NUMBER = 10
MUTATION_COEF = 2
TEST_ITERATIONS_NUMBER = 30
BOUND = 100


def make_table(param, param_name, results):
    table = []
    table.append(f'|    parameter    |{" "*10}min{" "*10}|{" "*10}max{" "*10}|{" "*10}avg{" "*10}|{" "*10}std{" "*10}|')
    for cur_param, cur_result in zip(param, results):
        res_max = max(cur_result)
        res_min = min(cur_result)
        avg = sum(cur_result) / len(cur_result)

        tmp = [(res - avg) ** 2 for res in cur_result]
        std = sqrt(sum(tmp) / len(cur_result))

        str = f'{param_name}={cur_param}'
        table.append(f'|{str:^17}|{res_min:^23}|{res_max:^23}|{avg:^23}|{std:^23}|')
    return table

def print_table(table):
    for str in table:
        print(str)

def save_table(table, file_name):
    try:
        f = open(f'{file_name}.txt', "w")
        for str in table:
            f.write(f'{str}\n')
    finally:
        f.close()


# test_values = [0.01, 0.02, 0.03, 0.05, 0.08, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5]
# test_values = [20,30,50,100,150,200,300,500,1000,1500,2000,3000,5000]
test_values = [1, 2, 3, 5, 7, 10, 15, 20, 25, 50]

res_population = []
for test_value in test_values:
    tmp = []
    for _ in range(TEST_ITERATIONS_NUMBER):
        tmp.append(f4(evol(f4, POPULATION_SIZE, test_value, BOUND, MUTATION_COEF)))
    res_population.append(tmp)

table = make_table(test_values, 'elite', res_population)
save_table(table, 'elite')
print_table(table)

# Zwiększenie każdego z 3 parametrów (siła mutacji, rozmiaru elity, liczba osobników w populacji) polepsza wynik,
#     ale w pewnym momencie wynik pogorsza się, czyli każdy z parametrów wymaga dopasowania

# W porównaniu z algorytmem gradient descent, algorytm ewolucyjny jest bardziej precyzyjny, ale bardziej złożony
#     objiczeniowo. Implementacja algorytmu evolucyjnego jest trudniejsza od implementacji, ale nadal nie jest
#     zbyt trudna, czyli raszej prosta. Oba algorytmu wymagają dopasowania. Istotną wadą jest szybki wzrost czasu
#     wykonania algorytmu wraz ze zwiększeniem liczby wymiarów. W sumie, algorytm ewolucyjny jest dość przydatny,
#     jeśli budżet czasowy na to pozwala.
