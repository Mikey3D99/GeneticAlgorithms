import chromosome as c


class Population:
    def __init__(self, n_chromosomes):
        self.number = n_chromosomes
        self.population = [c.Chromosome() for x in range(n_chromosomes)]

    def get_population(self):
        return self.population

    def get_number_of_chromosomes(self):
        return self.number

    def set_population(self, new_population):
        self.population = new_population

    def print_population_binary(self):
        for i, chromosome in enumerate(self.population):
            print(str(i + 1) + ". " + format(chromosome.get_chromosome(), '08b'))
