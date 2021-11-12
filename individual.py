import random
import string


class Individual:
    """
        Individual in the population
    """

    """
        size: number of nodes
    """
    def __init__(self, n_nodes):
        self.fitness = 0
        self.n_cluster = 1
        self.max_n_cluster = 10
        self.genes = self.generate_random_genes(n_nodes)

    @staticmethod
    def generate_random_genes(n_nodes):
        genes = [1] * n_nodes

        return genes


    # Fitness function: returns a floating points of "correct" characters
    def calc_fitness(self, dep_graph):
        self.fitness = 0.1


        # score = 0
        # index = 0
        
        # for gene in self.genes: 
        #     if gene == target[index]:
        #         score += 1
        #     index += 1

        # # insert your code to calculate the individual fitness here

        # self.fitness = score / len(target)

    def __repr__(self):
        return str(self.genes) + " -> fitness: " + str(self.fitness)

    # The crossover function selects pairs of individuals to be mated, generating a third individual (child)
    def crossover(self, partner):
        # Crossover suggestion: child with half genes from one parent and half from the other parent
        ind_len = len(self.genes)
        child = Individual(ind_len)

        midpoint = random.randint(0, ind_len)

        child.genes = self.genes[:midpoint] + partner.genes[midpoint:]
        child.n_cluster = max(self.n_cluster, partner.n_cluster)

        return child

    # Mutation: based on a mutation probability, the function picks a new random character and replace a gene with it
    def mutate(self, mutation_rate, n_cluster_mutation_rate):
        # code to mutate the individual here
        for i, gene in enumerate(self.genes):
            if random.uniform(0, 1) < mutation_rate: 
                self.genes[i] = random.randint(0, self.n_cluster)

        # Mutatate n_cluster
        if self.n_cluster < self.max_n_cluster and random.uniform(0, 1) < n_cluster_mutation_rate: 
            self.n_cluster += 1 
