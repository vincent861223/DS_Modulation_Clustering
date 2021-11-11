import random
import string


class Individual:
    """
        Individual in the population
    """

    def __init__(self, size):
        self.fitness = 0
        self.genes = self.generate_random_genes(size)

    # Fitness function: returns a floating points of "correct" characters
    def calc_fitness(self, target):
        score = 0
        index = 0
        
        for gene in self.genes: 
            if gene == target[index]:
                score += 1
            index += 1

        # insert your code to calculate the individual fitness here

        self.fitness = score / len(target)

    def __repr__(self):
        return ''.join(self.genes) + " -> fitness: " + str(self.fitness)

    @staticmethod
    def generate_random_genes(size):
        genes = []

        for i in range(size):
            genes.append(random.choice(string.printable))

        return genes

    # The crossover function selects pairs of individuals to be mated, generating a third individual (child)
    def crossover(self, partner):
        # Crossover suggestion: child with half genes from one parent and half from the other parent
        ind_len = len(self.genes)
        child = Individual(ind_len)

        midpoint = random.randint(0, ind_len)

        child.genes = self.genes[:midpoint] + partner.genes[midpoint:]

        return child

    # Mutation: based on a mutation probability, the function picks a new random character and replace a gene with it
    def mutate(self, mutation_rate):
        # code to mutate the individual here
        for i, gene in enumerate(self.genes):
            if random.uniform(0, 1) < mutation_rate: 
                self.genes[i] = random.choice(string.printable)



