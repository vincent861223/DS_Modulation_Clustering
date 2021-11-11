from population import Population
import argparse
import time

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=str, default="To be or not to be.")
    parser.add_argument("--pop", type=int, default=200)
    parser.add_argument("--mut", type=float, default=0.01)
    parser.add_argument("--cro", type=float, default=1)
    parser.add_argument("--repeat", type=int, default=1)
    parser.add_argument("--printInterval", type=int, default=100)

    return parser

def main(args):
    pop_size = args.pop
    target = args.target 
    mutation_rate = args.mut 
    crossover_rate = args.cro

    # you don't need to call this function when the ones right bellow are fully implemented

    """
    Uncomment these lines bellow when you implement all the functions
    """

    generations = []
    execTime = []

    for i in range(args.repeat):
        pop = Population(target, pop_size, mutation_rate, crossover_rate)
        start = time.time()
        while not pop.finished:
            pop.natural_selection()
            pop.generate_new_population()
            pop.evaluate()
            if pop.generations % args.printInterval == 0:
                pop.print_population_status()
        end = time.time()
        generations.append(pop.generations)
        execTime.append(end-start)

    print("Generations: ", generations)
    print("Average: ", sum(generations)/len(generations))
    print("execTime: ", execTime)
    print("Average: ", sum(execTime)/len(execTime))


if __name__ == "__main__":
    parser = argparser()
    args = parser.parse_args()
    main(args)
