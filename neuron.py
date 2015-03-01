__author__ = 'Vadym S. Khondar'


class Neuron:
    def __init__(self, *args):
        self.state = 0
        self.dendrites = []
        self.synapses = []

    def excite(self):
        self._state(1)

    def inhibit(self):
        self._state(0)

    def is_excited(self):
        return self._state()

    def notify(self):
        input = [(neuron.is_excited(), weight) for neuron, weight in self.dendrites]
        weighted_sum = 0
        for (v, w) in input:
            weighted_sum += v * w

        if weighted_sum > 0.5:
            self.excite()
        else:
            self.inhibit()

    def connect_dendrite(self, neuron):
        self.dendrites.append((neuron, 0.5))

    def disconnect_dendrite(self, neuron):
        self.dendrites = [(n, w) for n, w in self.dendrites if n != neuron]

    def connect_synapse(self, neuron):
        self.synapses.append(neuron)

    def disconnect_synapse(self, neuron):
        self.synapses.remove(neuron)

    def _state(self, state=None):
        if state is None:
            return self.state
        elif self.state != state:
            self.state = state
            self._propagate()

    def _propagate(self):
        [n.excite() for n in self.synapses]
