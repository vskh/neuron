__author__ = 'Vadym S. Khondar'


class InputTerminal(object):
    def __init__(self):
        self.value = 0
        self.synapses = []

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def connect_synapse(self, neuron):
        self.synapses.append(neuron)

    def disconnect_synapse(self, neuron):
        self.synapses.remove(neuron)

    def _value(self, value=None):
        if value is None:
            return self.value
        elif self.value != value:
            self.value = value
            self._propagate()

    def _propagate(self):
        [n.notify() for n in self.synapses]


# Multi input extension of InputTerminal
class Neuron (InputTerminal):
    def __init__(self):
        super(Neuron, self).__init__()
        self.dendrites = []

    def excite(self):
        self.set_value(1)

    def inhibit(self):
        self.set_value(0)

    def is_excited(self):
        return self.get_value() == 1

    def notify(self):
        inputs = [(neuron.is_excited(), weight) for neuron, weight in self.dendrites]
        weighted_sum = 0
        for (v, w) in inputs:
            weighted_sum += v * w

        if weighted_sum > 0.5:
            self.excite()
        else:
            self.inhibit()

    def connect_dendrite(self, neuron, weight=0.5):
        self.dendrites.append((neuron, weight))

    def set_dendrite_weight(self, neuron, weight):
        for p in self.dendrites:
            if p[0] == neuron:
                p[1] = weight
                break

    def disconnect_dendrite(self, neuron):
        self.dendrites = [(n, w) for n, w in self.dendrites if n != neuron]

    def connect(self, input_terminal, weight=0.5):
        input_terminal.connect_synapse(self)
        self.connect_dendrite(input_terminal, weight)
