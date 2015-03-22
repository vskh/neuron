__author__ = 'Vadym S. Khondar'

from neuron import InputTerminal, Neuron


class ConnectedNeuralnet:

    def __init__(self, num_inputs, num_outputs, layers_config=None):
        if num_inputs <= 0 or num_outputs <= 0:
            raise ValueError("Inputs and outputs number should be positive integer")

        self.__inputs = []
        self.__neurons = []

        layers_config = layers_config or [[tuple(1 for i in range(0, num_inputs))], [(1,)], [(1,)]]

        # create inputs
        self.__inputs = [InputTerminal() for i in range(0, num_inputs)]

        # create and connect neurons
        prev_layer = self.__inputs
        for layer_config in layers_config[0:-1]:
            layer_size = len(layer_config)
            curr_layer = []
            for i in range(0, layer_size):
                neuron = Neuron()
                curr_layer.append(neuron)
                for j in range(0, len(prev_layer)):
                    neuron.connect(prev_layer[j], layer_config[i][j])

            self.__neurons.append(curr_layer)
            prev_layer = curr_layer

        # create and connect output layer
        outer_layer = []
        layer_config = layers_config[-1]
        for i in range(0, num_outputs):
            neuron = Neuron()
            outer_layer.append(neuron)
            [neuron.connect(prev_layer[j], layer_config[i][j]) for j in range(0, len(prev_layer))]
        self.__neurons.append(outer_layer)

    def get_num_inputs(self):
        return len(self.__inputs)

    def get_num_outputs(self):
        return len(self.__neurons[len(self.__neurons) - 1])

    def set_inputs(self, input_values):
        for i, value in enumerate(input_values):
            self.__inputs[i].set_value(value)

    def get_num_layers(self):
        return len(self.__neurons)

    def get_state(self):
        state = []
        for layer in self.__neurons:
            layer_state = []
            for neuron in layer:
                layer_state.append(neuron.get_value())
            state.append(layer_state)
        return state

    def get_outputs(self):
        return [int(neuron.is_excited()) for neuron in self.__neurons[len(self.__neurons) - 1]]

    def configure(self, layers_config):
        for layer_num, layer_config in enumerate(layers_config):
            layer = self.__get_layer(layer_num)
            if len(layer_config) != len(layer):
                raise ValueError("Incorrect layer size for layer {}".format(layer_num))

            for neuron_num, neuron in enumerate(layer):
                if len(layer_config[neuron_num]) != neuron.get_num_dendrites():
                    raise ValueError("Incorrect number of inputs for neuron {0} in layer {1}".
                                     format(neuron_num, layer_num))
                for dendrite_num, dendrite_weight in enumerate(layer_config[neuron_num]):
                    neuron.set_dendrite_weight_by_idx(dendrite_num, dendrite_weight)

    def get_configuration(self):
        conf = []
        for layer in self.__neurons:
            layer_neuron_weights = []
            for neuron in layer:
                layer_neuron_weights.append(neuron.get_dendrite_weights())
            conf.append(layer_neuron_weights)
        return conf

    def __get_layer(self, layer_num):
        return self.__neurons[layer_num]
