import math
import random

import numpy as np
from matplotlib import pyplot as plt

import population as p


def f(x: int) -> int:
    if 0 <= x <= 255:
        return 0.2 * pow(x, 0.5) + 2 * math.sin(2 * math.pi * 0.02 * x) + 5
    else:
        print(x)


x_axis = [x for x in np.linspace(0, 255, 100000)]
y_axis = [f(x1) for x1 in x_axis]


def plot_f():
    plt.plot(x_axis, y_axis, label="Plot of a function for values between 0 to 255")
    print("FUNCTION MAXIMUM: " + str(max(y_axis)))
    plt.show()


def fitness_function(arg):
    objective = max(y_axis)
    return f(arg) / objective


def print_fitness(population_chromosomes: p.Population, fitness_of_chromosomes: list):
    for i, (fit, pop) in enumerate(zip(fitness_of_chromosomes, population_chromosomes.get_population())):
        print(str(i + 1) + ". " + str(fit * 100) + " value for chromosome: " + format(pop.get_chromosome(), '08b'))


def roulette_selection(fitness_list: list, my_population: p.Population):
    sum_of_fitness = sum(fitness_list)
    pick = random.uniform(0, sum_of_fitness)
    current = 0
    for chromosome in my_population.get_population():
        current += fitness_function(chromosome.get_chromosome())
        if current > pick:
            return chromosome


def mutation(mutation_probability, my_population: p.Population):
    should_mutate = random.randrange(0, 1000, 1) / 1000
    if should_mutate < mutation_probability:
        chromosome = random.choice(my_population.get_population())
        bits_to_toggle = [x for x in range(8) if random.uniform(0, 1) < mutation_probability]
        for bit in bits_to_toggle:
            chromosome.toggle_binary(bit)


def crossover(crossover_probability, my_population: p.Population):
    should_cross = random.randrange(0, 1000, 1) / 1000
    if should_cross < crossover_probability:
        chromosome1 = random.choice(my_population.get_population())
        chromosome2 = random.choice(my_population.get_population())
        locus = random.randint(1, 6)
        chromosome1.locus_swap(locus, chromosome2)


def select_the_strongest(from_population: p.Population):
    maximum = []
    for x in from_population.get_population():
        maximum.append(f(x.get_chromosome()))
    return max(maximum)


def basic_genetic_algorithm(number_of_generations: int, number_of_units: int, crossover_probability: float,
                            mutation_probability: float):
    population = None
    result_plot = []

    for i in range(number_of_generations):
        population = p.Population(number_of_units)

        fitness = [fitness_function(x.get_chromosome()) for x in population.get_population()]

        mating_pool = [roulette_selection(fitness, population) for x in range(population.get_number_of_chromosomes())]
        population.set_population(mating_pool)

        [mutation(mutation_probability, population) for x in range(population.get_number_of_chromosomes())]
        [crossover(crossover_probability, population) for x in range(population.get_number_of_chromosomes())]

        result_plot.append(select_the_strongest(population))

    return population, result_plot


def plot_results(res):
    plt.plot([i for i in range(len(res))], res)
    plt.show()


if __name__ == '__main__':

    response = input("Show function plot?(yes/no)")
    if response == "yes":
        plot_f()

    ret, for_plot = basic_genetic_algorithm(50, 50, 0.5, 0.01)
    print("THE STRONGEST UNIT : ")
    print(max(for_plot))
    plot_results(for_plot)
