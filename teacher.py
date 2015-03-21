__author__ = 'Vadym S. Khondar'

from random import random, uniform


class GeneticTeacher:

    def __init__(self, neuralnet, mutation_factor, retirement_factor):
        self.__neuralnet = neuralnet
        self.__neuralnet_configuration = neuralnet.get_configuration()
        self.__mutation_factor = mutation_factor
        self.__retirement_factor = retirement_factor
        self.__current_pop = []
        self.__pop_size = 100

    def __gen_subpopulation(self, population_size):
        subpop = []
        for inst in range(0, population_size):
            genotype = []
            for layer in self.__neuralnet_configuration:
                for neuron in layer:
                    genotype.append(random())
            subpop.append(genotype)
        return subpop

    def __gen_population(self):
        self.__current_pop = self.__gen_subpopulation(self.__pop_size)

    def __retire(self):
        num_retired = int(uniform(0, self.__retirement_factor))
        self.__current_pop = self.__current_pop[0:len(self.__current_pop) - num_retired]

    def _crossover(self):
        pass

    def _select(self):
        pass

    def _mutate(self):
        pass

    def __teach_once(self):
        self._gen_population()
        self._crossover()

    def teach(self, training_set):
        pass








