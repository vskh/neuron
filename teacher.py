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
                    for weight in neuron:
                        genotype.append(random())
            subpop.append(genotype)
        return subpop

    def __gen_population(self):
        items = self.__gen_subpopulation(self.__pop_size)
        self.__current_pop = self.__calc_fitness(items)

    def __sort_population(self):
        self.__current_pop.sort(key=lambda i: i[0], reverse=True)

    @staticmethod
    def __cvt_vector_to_conf(vector, shape):
        conf = []
        pos = 0
        for layer in shape:
            layer_neuron_weights = []
            for neuron in layer:
                neuron_weights = vector[pos:pos+len(neuron)]
                pos += len(neuron)
                layer_neuron_weights.append(neuron_weights)
            conf.append(layer_neuron_weights)
        return conf

    def __fitness(self, item):
        net = self.__neuralnet
        shape = net.get_configuration()

        conf = self.__cvt_vector_to_conf(item, shape)

        net.configure(conf)

        def test(inputs, outputs):
            net.set_inputs(inputs)
            print("Expected outputs: ")
            print(outputs)
            print("Real outputs: ")
            print(net.get_outputs())
            print("Network state: ")
            print(net.get_state())
            return net.get_outputs() == outputs

        fitness = 0
        for inputs, outputs in self.__training_set:
            # print("Fitness: {}".format(fitness))
            fitness += test(inputs, outputs)

        print("Fitness: {}".format(fitness))
        return fitness

    def __calc_fitness(self, items):
        return [(self.__fitness(item), item) for item in items]

    def __retire(self):
        num_retired = int(uniform(0, self.__retirement_factor))
        self.__current_pop = self.__current_pop[0:self.__pop_size - num_retired]

    @staticmethod
    def __crossover_once(item1, item2, cross_point=None):
        assert len(item1) == len(item2)

        cross_point = cross_point or uniform(1, len(item1))
        child1 = list(item1)
        child2 = list(item2)

        sz = len(item1)

        tmp = child1[cross_point:sz]
        child1[cross_point:sz] = child2[cross_point:sz]
        child2[cross_point:sz] = tmp

        return child1, child2

    def __crossover(self):
        sz = len(self.__current_pop)
        num_crossovers = self.__pop_size - sz

        for i in range(0, num_crossovers):
            idx1 = int(uniform(0, sz))
            idx2 = int(uniform(0, sz))
            children = self.__crossover_once(self.__current_pop[idx1][1],
                                             self.__current_pop[idx2][1])
            self.__current_pop.extend(self.__calc_fitness(children))

    def __mutate(self):
        sz = len(self.__current_pop)
        mutation_space = sz * len(self.__current_pop[0][1])
        num_mutations = int(mutation_space * self.__mutation_factor)
        for i in range(0, num_mutations):
            item = self.__current_pop[int(uniform(0, sz))][1]
            idx1 = int(uniform(0, len(item)))
            idx2 = int(uniform(0, len(item)))
            item[idx1], item[idx2] = item[idx2], item[idx1]

        extension_pop_size = int(max(self.__pop_size - sz, sz * self.__mutation_factor))
        extension_pop = self.__gen_subpopulation(extension_pop_size)
        self.__current_pop.extend(self.__calc_fitness(extension_pop))

    def teach(self, num_iterations=100, continue_teaching=True):
        if not self.__current_pop or not continue_teaching:
            self.__gen_population()

        for i in range(1, num_iterations):
            self.__sort_population()
            self.__retire()
            self.__crossover()
            self.__mutate()
            print("Best specimen (fitness {}): ".format(self.__current_pop[0][0]))
            print(", ".join(str(w) for w in self.__current_pop[0][1]))
            if self.__current_pop[0][0] == len(self.__training_set):
                print("Found solution fits all training samples. Stopping search")
                break

    def get_best_specimen(self):
        fitness = self.__current_pop[0][0]
        conf = self.__cvt_vector_to_conf(self.__current_pop[0][1],
                                         self.__neuralnet.get_configuration())
        return (fitness, conf)
