import random


def make_population(size: int):
    pop =[]
    for x in range(0,size):
        individual = []
        for y in range(0, len(items)):
            individual.append(random.randint(0,1))
        pop.append(individual)
    return pop


def making_new_pop(pop):
    wheel = roullette_wheel(pop)
    mating_pool = []
    new_pop = []
    for x in range(0, pop_size):
        mating_pool.append(wheel[random.randint(0, len(wheel)-1)])
    while len(mating_pool) > 0:
        if len(mating_pool)==2:
            p1 = mating_pool.pop(1)
            p2 = mating_pool.pop(0)
        else:
            p1 = mating_pool.pop(random.randint(0, len(mating_pool)-1))
            p2 = mating_pool.pop(random.randint(0, len(mating_pool)-1))
        cross_prob = random.random()
        mut_prob_1 = random.random()
        mut_prob_2 = random.random()
        if cross_prob > 0.5:
            child1, child2 = crossover_individual(p1,p2)
        else:
            child1 = p1
            child2 = p2
        if mut_prob_1 > 0.8:
            mutate(child1)
        if mut_prob_2 > 0.8:
            mutate(child2)

        new_pop.append(child1)
        new_pop.append(child2)

    return new_pop


def crossover_individual(mom, dad):
    child1 = mom[0:3] + dad[3:5]
    child2 = dad[0:3] + mom[3:5]
    return child1, child2


def mutate(individual):
    for x in range(0, len(individual)):
        if individual[x] == 0:
            individual[x] == 1
        else:
            individual[x] == 0
    return individual


def roullette_wheel(pop):
    wheel = []
    fit_list = fitness(pop)
    for x in range(0, len(fit_list)):
        for y in range(0, fit_list[x]):
            wheel.append(pop[x])
    return wheel


def fitness(pop):
    fitness_list = []
    for ind in pop:
        fit_weight = 0
        fit_value = 0
        for x in range(0, len(ind)):
            fit_weight += ind[x] * items[x][0]
            fit_value += ind[x] * items[x][1]
        if fit_weight > max_weight:
            fitness_list.append(0)
        else:
            fitness_list.append(fit_value)
    return fitness_list


def find_best(pop, iteration):
    for x in range(0, iteration):
        new_pop = making_new_pop(pop)
    best_fitness = fitness(new_pop)
    index = best_fitness.index(max(best_fitness))
    best = new_pop[index]
    print(new_pop)
    return best, best_fitness


if __name__ == "__main__":
    items = [[5, 7], [6, 12], [1, 8], [5, 14], [2, 8]]
    max_weight = 12
    pop_size = 10
    population = make_population(pop_size)
    best, fitnes = find_best(population, 100)
    print(best)

