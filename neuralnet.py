__author__ = 'Vadym S. Khondar'

from neuron import InputTerminal, Neuron


class ConnectedNeuralnet:

    def __init__(self, num_inputs, num_outputs, layers_config=None):
        if num_inputs <= 0 or num_outputs <= 0:
            raise ValueError("Inputs and outputs number should be positive integer")

        self.inputs = []
        self.neurons = []

        layers_config = layers_config or [1, 1]

        # create inputs
        [self.inputs.append(InputTerminal()) for i in range(0, num_inputs)]

        # create and connect neurons
        prev_layer = self.inputs
        for layer_size in layers_config:
            curr_layer = []
            for i in range(0, layer_size):
                neuron = Neuron()
                curr_layer.append(neuron)
                [neuron.connect(prev_layer[i]) for i in range(0, len(prev_layer))]
            self.neurons.append(curr_layer)
            prev_layer = curr_layer

        # create and connect output layer
        outer_layer = []
        for i in range(0, num_outputs):
            neuron = Neuron()
            outer_layer.append(neuron)
            [neuron.connect(prev_layer[i]) for i in range(0, len(prev_layer))]
        self.neurons.append(outer_layer)

    def get_num_inputs(self):
        return len(self.inputs)

    def get_num_outputs(self):
        return len(self.neurons[len(self.neurons) - 1])

    def set_inputs(self, input_values):
        for i in range(0, len(self.inputs)):
            if input_values[i]:
                self.inputs[i].excite()
            else:
                self.inputs[i].inhibit()

    def get_num_layers(self):
        return len(self.neurons)

    def get_outputs(self):
        outputs = []
        [outputs.append(neuron.get_value()) for neuron in self.neurons[len(self.neurons) - 1]]
        return outputs

    def _get_layer(self, layer_num):
        return self.neurons[layer_num]
