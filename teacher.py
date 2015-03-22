__author__ = 'Vadym S. Khondar'

from random import random, uniform


class GeneticTeacher:
    def __init__(self, neuralnet, training_set, mutation_factor, retirement_factor):
        self.__neuralnet = neuralnet
        self.__neuralnet_configuration = neuralnet.get_configuration()
        self.__training_set = training_set
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
        items = self.__gen_subpopulation(self.__pop_size)
        for item in items:
            self.__current_pop.append((self.__fitness(item), item))

    def __sort_population(self):
        self.__current_pop.sort(key=lambda i: i[0])

    def __fitness(self, item):
        net = self.__neuralnet
        shape = net.get_configuration()

        conf = []
        pos = 0
        for layer in shape:
            layer_neuron_weights = []
            for neuron in layer:
                neuron_weights = item[pos:pos+len(neuron)]
                pos += len(neuron)
                layer_neuron_weights.append(neuron_weights)
            conf.append(layer_neuron_weights)

        net.configure(conf)

        def test(inputs, outputs):
            net.set_inputs(inputs)
            return net.get_outputs() == outputs

        fitness = 0
        for inputs, outputs in self.__training_set:
            fitness += test(inputs, outputs)

        return fitness

    def __retire(self):
        num_retired = int(uniform(0, self.__retirement_factor))
        self.__current_pop = self.__current_pop[0:len(self.__current_pop) - num_retired]

    def __crossover_once(self, idx1, idx2, cross_point=None):
        item1 = self.__current_pop[idx1][1]
        item2 = self.__current_pop[idx2][1]

        assert len(item1) == len(item2)
        cross_point = cross_point or uniform(1, len(item1))

        sz = len(item1)

        tmp = item1[cross_point:sz]
        item1[cross_point:sz] = item2[cross_point:sz]
        item2[cross_point:sz] = tmp

    def __crossover(self):
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
