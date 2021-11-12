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

        # TODO: imports is empty
        # TODO: n_cluster
        # TODO: eps duplicate

        # count miu_i and eps_ij
        miu = [0] * self.n_cluster
        eps = [[0 for _ in range(self.n_cluster)]
               for _ in range(self.n_cluster)]
        n = [0] * self.n_cluster

        for key in dep_graph.keys():
            key_cluster = self.genes[list(dep_graph).index(key)]
            n[key_cluster - 1] += 1
            for outgoing_edge in dep_graph[key]['imports']:
                outgoing_cluster = self.genes[list(
                    dep_graph).index(outgoing_edge)]
                if key_cluster == outgoing_cluster:
                    miu[key_cluster - 1] += 1
                else:
                    eps[key_cluster - 1][outgoing_cluster - 1] += 1
                    eps[outgoing_cluster - 1][key_cluster - 1] += 1

        # count A_i
        cum_A = 0
        for k in range(self.n_cluster):
            if n[k] != 0:  # TODO: n_cluster
                cum_A += (miu[k] / (n[k] * n[k]))

        # count E_ij
        cum_E = 0
        for i in range(self.n_cluster):
            for j in range(self.n_cluster):
                if n[i] != 0 & n[j] != 0:  # TODO: n_cluster
                    cum_E += (eps[i][j] / (2 * n[i] * n[j]))

        # calculate MQ
        if self.n_cluster == 1:
            self.fitness = cum_A
        else:
            ave_A = cum_A / self.n_cluster
            ave_E = cum_E / (self.n_cluster * (self.n_cluster - 1) / 2)
            self.fitness = ave_A - ave_E

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
