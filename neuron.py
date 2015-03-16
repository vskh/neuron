__author__ = 'Vadym S. Khondar'

from collections import OrderedDict


class InputTerminal(object):
    def __init__(self):
        self.__value = 0
        self.__synapses = []

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def connect_synapse(self, neuron):
        self.__synapses.append(neuron)

    def disconnect_synapse(self, neuron):
        self.__synapses.remove(neuron)

    def get_num_synapses(self):
        return len(self.__synapses)

    def __value(self, value=None):
        if value is None:
            return self.__value
        elif self.__value != value:
            self.__value = value
            self.__propagate()

    def __propagate(self):
        [n.notify() for n in self.__synapses]


# Multi input extension of InputTerminal
class Neuron(InputTerminal):
    def __init__(self):
        super(Neuron, self).__init__()
        self.__dendrites = OrderedDict()

    def excite(self):
        self.set_value(1)

    def inhibit(self):
        self.set_value(0)

    def is_excited(self):
        return self.get_value() == 1

    def notify(self):
        inputs = [(neuron.is_excited(), weight) for neuron, weight in self.__dendrites.items()]
        weighted_sum = 0
        for (v, w) in inputs:
            weighted_sum += v * w

        if weighted_sum > 0.5:
            self.excite()
        else:
            self.inhibit()

    def connect_dendrite(self, neuron, weight=0.5):
        self.__dendrites[neuron] = weight

    def get_dendrite_weight_by_idx(self, idx):
        return self.__dendrites[list(self.__dendrites.keys())[idx]]

    def get_dendrite_weight(self, neuron):
        return self.__dendrites[neuron]

    def set_dendrite_weight_by_idx(self, idx, weight):
        self.__dendrites[list(self.__dendrites.keys())[idx]] = weight

    def set_dendrite_weight(self, neuron, weight):
        if neuron in self.__dendrites:
            self.__dendrites[neuron] = weight
        else:
            raise LookupError("Neuron {} not found".format(neuron))

    def disconnect_dendrite(self, neuron):
        self.__dendrites = [(n, w) for n, w in self.__dendrites if n != neuron]

    def get_num_dendrites(self):
        return len(self.__dendrites)

    def connect(self, input_terminal, weight=0.5):
        input_terminal.connect_synapse(self)
        self.connect_dendrite(input_terminal, weight)
