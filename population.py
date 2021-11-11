from individual import Individual
import random


class Population:
    """
        A class that describes a population of virtual individuals
    """

    def __init__(self, target, size, mutation_rate, crossover_rate):
        self.population = []
        self.generations = 0
        self.target = target
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.best_ind = None
        self.finished = False
        self.perfect_score = 1.0
        self.max_fitness = 0.0
        self.average_fitness = 0.0
        self.mating_pool = []

        for i in range(size):
            ind = Individual(len(target))
            ind.calc_fitness(target)

            if ind.fitness > self.max_fitness:
                self.max_fitness = ind.fitness

            self.average_fitness += ind.fitness
            self.population.append(ind)

        self.average_fitness /= size

    def print_population_status(self):
        print("\nPopulation " + str(self.generations))
        print("Average fitness: " + str(self.average_fitness))
        print("Best individual: " + str(self.best_ind))

    # Generate a mating pool according to the probability of each individual
    def natural_selection(self):
        # Implementation suggestion based on Lab 3:
        # Based on fitness, each member will get added to the mating pool a certain number of times
        # a higher fitness = more entries to mating pool = more likely to be picked as a parent
        # a lower fitness = fewer entries to mating pool = less likely to be picked as a parent
        self.mating_pool = []
        

        for i, ind in enumerate(self.population):
            prob = int(round(ind.fitness * 100))
            self.mating_pool.extend([i for j in range(prob)])

    # Generate the new population based on the natural selection function
    def generate_new_population(self):
        population_len = len(self.population)
        mating_pool_len = len(self.mating_pool)
        new_population = []
        self.average_fitness = 0.0

        for i in range(population_len):
            i_partner_a = random.randint(0, mating_pool_len - 1)
            i_partner_b = random.randint(0, mating_pool_len - 1)

            i_partner_a = self.mating_pool[i_partner_a]
            i_partner_b = self.mating_pool[i_partner_b]

            partner_a = self.population[i_partner_a]
            partner_b = self.population[i_partner_b]

            if random.uniform(0, 1) < self.crossover_rate:
                child = partner_a.crossover(partner_b)
            else: 
                child = partner_a
            child.mutate(self.mutation_rate)
            child.calc_fitness(self.target)

            self.average_fitness += child.fitness
            new_population.append(child)

        self.population = new_population
        self.generations += 1
        self.average_fitness /= len(new_population)
    # Compute/Identify the current "most fit" individual within the population
    def evaluate(self):
        best_fitness = 0.0

        for ind in self.population:
            if ind.fitness > best_fitness: 
                best_fitness = ind.fitness
                self.best_ind = ind

        if best_fitness == self.perfect_score:
            self.finished = True