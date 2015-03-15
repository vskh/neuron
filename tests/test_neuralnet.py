__author__ = 'Vadym S. Khondar'

import unittest

from neuralnet import ConnectedNeuralnet


class ConnectedNeuralnetTest(unittest.TestCase):
    def test_neuralnet_construct_with_zero_inputs(self):
        with self.assertRaises(ValueError): #, "Neuronet with zero inputs should not be possible"):
            ConnectedNeuralnet(0, 2)

    def test_neuralnet_construct_with_zero_outputs(self):
        with self.assertRaises(ValueError): #, "Neuronet with zero outputs should not be possible"):
            ConnectedNeuralnet(1, 0)

    def test_neuralnet_construct_with_defaults_layers_conf(self):
        neuralnet = ConnectedNeuralnet(1, 1)
        self.assertEqual(neuralnet.get_num_layers(), 3, "Default neuralnet should contain 3 layers")
        self.assertEqual(len(neuralnet._get_layer(0)), 1, "Default neuralnet should have 1 "
                                                         "input neuron")
        self.assertEqual(len(neuralnet._get_layer(2)), 1, "Default neuralnet should have 1 "
                                                         "output neuron")
