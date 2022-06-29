import numpy as np
from random import sample

DIMENSION = 2
COMPRASONS = 10000

def evol(func, population_size, elite_number, bound, mutation_coef, comparisons=COMPRASONS):
    population = [np.random.uniform(-bound, bound, DIMENSION) for _ in range(population_size)]

    for _ in range(comparisons // population_size):
        new_generation = sorted(population, key=lambda coords: func(coords))[:elite_number]
        for _ in range(population_size):
            participants = sample(population,2)
            new_generation.append(tournament(func, *participants))
        tmp = mutation(new_generation, mutation_coef)
        population = sorted(tmp, key=lambda coords: func(coords))[:-elite_number]
    return min(population, key=lambda elem: func(elem))


def compare(subj1, subj2, func):
    if func(subj1) < func(subj2):
        return subj1
    return subj2

def mutation(population, mutation_coef):
    mutated = []
    for subject in population:
        mutated_subject = subject + mutation_coef * np.random.normal(0, 1, 2)
        mutated.append(mutated_subject)
    return mutated


def tournament(func, point1, point2):
    if func(point1) < func(point2):
        return point1
    return point2