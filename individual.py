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

    def generate_random_genes(self, n_nodes):
        # genes = [0] * n_nodes
        genes = []

        for i in range(n_nodes):
            genes.append(random.randint(0, self.n_cluster - 1))

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
            n[key_cluster] += 1
            # for outgoing_edge in dep_graph[key]['imports']:
            for outgoing_edge in dep_graph[key].get('imports', []):
                outgoing_cluster = self.genes[list(
                    dep_graph).index(outgoing_edge)]
                if self.n_cluster == outgoing_cluster:
                    print(self.genes)
                if key_cluster == outgoing_cluster:
                    miu[key_cluster] += 1
                else:
                    eps[key_cluster][outgoing_cluster] += 1
                    eps[outgoing_cluster][key_cluster] += 1

        # count A_i
        cum_A = 0
        for k in range(self.n_cluster):
            if n[k] != 0:  # TODO: n_cluster
                cum_A += (miu[k] / (n[k] * n[k]))

        # count E_ij
        cum_E = 0
        for i in range(self.n_cluster):
            for j in range(self.n_cluster):
                if n[i] != 0 and n[j] != 0:  # TODO: n_cluster
                # print("in\n")
                    cum_E += (eps[i][j] / (2 * n[i] * n[j]))
                # print("out\n")

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
        # child.n_cluster = max(self.n_cluster, partner.n_cluster)
        child.n_cluster = max(child.genes) + 1

        return child

    # Mutation: based on a mutation probability, the function picks a new random character and replace a gene with it
    def mutate(self, mutation_rate, n_cluster_mutation_rate):
        # code to mutate the individual here
        for i, gene in enumerate(self.genes):
            if random.uniform(0, 1) < mutation_rate:
                self.genes[i] += 1
        self.genes = self.resetClusterIndex(self.genes) 


        self.n_cluster = max(self.genes) + 1

    def resetClusterIndex(self, cluster):
        indexes = set(cluster)
        idxMap = { k:i for i, k in enumerate(indexes)}
        newCluster = []
        for c in cluster:
            newCluster.append(idxMap[c])
        return newCluster

    def appearMoreThanOnce(self, cluster):
        count = 0
        for gene in self.genes:
            if gene == cluster:
                count += 1

        if count == 1:
            return False
        elif(count <= 0):
            print("not possible")
            return False
        else:
            return True
