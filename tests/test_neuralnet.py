__author__ = 'Vadym S. Khondar'

import unittest

from neuralnet import ConnectedNeuralnet


class ConnectedNeuralnetTest(unittest.TestCase):
    def test_neuralnet_construct_with_zero_inputs(self):
        with self.assertRaises(
                ValueError):  # , "Neuronet with zero inputs should not be possible"):
            ConnectedNeuralnet(0, 2)

    def test_neuralnet_construct_with_zero_outputs(self):
        with self.assertRaises(
                ValueError):  # , "Neuronet with zero outputs should not be possible"):
            ConnectedNeuralnet(1, 0)

    def test_neuralnet_construct_with_defaults_layers_conf(self):
        neuralnet = ConnectedNeuralnet(1, 1)
        self.assertEqual(neuralnet.get_num_layers(), 3, "Default neuralnet should contain 3 layers")
        self.assertEqual(
            len(neuralnet._ConnectedNeuralnet__get_layer(0)), 1, "Default neuralnet should have 1 "
                                                                 "input neuron")
        self.assertEqual(
            len(neuralnet._ConnectedNeuralnet__get_layer(2)), 1, "Default neuralnet should have 1 "
                                                                 "output neuron")

    def test_neuralnet_configure_on_construct(self):
        neuralnet = ConnectedNeuralnet(2, 2,
                                       [[(0.1, 0.2), (0.3, 0.4)],
                                        [(0.5, 0.6), (0.7, 0.8)],
                                        [(0.9, 1.0), (2.0, 3.0)]])

        layer1 = neuralnet._ConnectedNeuralnet__get_layer(0)
        self.assertEquals(layer1[0].get_dendrite_weight_by_idx(0), 0.1, "Weight should be 0.1")
        self.assertEquals(layer1[0].get_dendrite_weight_by_idx(1), 0.2, "Weight should be 0.2")
        self.assertEquals(layer1[1].get_dendrite_weight_by_idx(0), 0.3, "Weight should be 0.3")
        self.assertEquals(layer1[1].get_dendrite_weight_by_idx(1), 0.4, "Weight should be 0.4")
        layer2 = neuralnet._ConnectedNeuralnet__get_layer(1)
        self.assertEquals(layer2[0].get_dendrite_weight_by_idx(0), 0.5, "Weight should be 0.5")
        self.assertEquals(layer2[0].get_dendrite_weight_by_idx(1), 0.6, "Weight should be 0.6")
        self.assertEquals(layer2[1].get_dendrite_weight_by_idx(0), 0.7, "Weight should be 0.7")
        self.assertEquals(layer2[1].get_dendrite_weight_by_idx(1), 0.8, "Weight should be 0.8")
        layer3 = neuralnet._ConnectedNeuralnet__get_layer(2)
        self.assertEquals(layer3[0].get_dendrite_weight_by_idx(0), 0.9, "Weight should be 0.9")
        self.assertEquals(layer3[0].get_dendrite_weight_by_idx(1), 1.0, "Weight should be 1.0")
        self.assertEquals(layer3[1].get_dendrite_weight_by_idx(0), 2.0, "Weight should be 2.0")
        self.assertEquals(layer3[1].get_dendrite_weight_by_idx(1), 3.0, "Weight should be 3.0")

    def test_neuralnet_configure(self):
        neuralnet = ConnectedNeuralnet(2, 2, [[(3.0, 2.0), (1.0, 0.9)],
                                              [(0.8, 0.7), (0.6, 0.5)],
                                              [(0.4, 0.3), (0.2, 0.1)]])

        neuralnet.configure([[(0.1, 0.2), (0.3, 0.4)],
                             [(0.5, 0.6), (0.7, 0.8)],
                             [(0.9, 1.0), (2.0, 3.0)]])

        layer1 = neuralnet._ConnectedNeuralnet__get_layer(0)
        self.assertEquals(layer1[0].get_dendrite_weight_by_idx(0), 0.1, "Weight should be 0.1")
        self.assertEquals(layer1[0].get_dendrite_weight_by_idx(1), 0.2, "Weight should be 0.2")
        self.assertEquals(layer1[1].get_dendrite_weight_by_idx(0), 0.3, "Weight should be 0.3")
        self.assertEquals(layer1[1].get_dendrite_weight_by_idx(1), 0.4, "Weight should be 0.4")
        layer2 = neuralnet._ConnectedNeuralnet__get_layer(1)
        self.assertEquals(layer2[0].get_dendrite_weight_by_idx(0), 0.5, "Weight should be 0.5")
        self.assertEquals(layer2[0].get_dendrite_weight_by_idx(1), 0.6, "Weight should be 0.6")
        self.assertEquals(layer2[1].get_dendrite_weight_by_idx(0), 0.7, "Weight should be 0.7")
        self.assertEquals(layer2[1].get_dendrite_weight_by_idx(1), 0.8, "Weight should be 0.8")
        layer3 = neuralnet._ConnectedNeuralnet__get_layer(2)
        self.assertEquals(layer3[0].get_dendrite_weight_by_idx(0), 0.9, "Weight should be 0.9")
        self.assertEquals(layer3[0].get_dendrite_weight_by_idx(1), 1.0, "Weight should be 1.0")
        self.assertEquals(layer3[1].get_dendrite_weight_by_idx(0), 2.0, "Weight should be 2.0")
        self.assertEquals(layer3[1].get_dendrite_weight_by_idx(1), 3.0, "Weight should be 3.0")

    def test_get_configuration(self):
        neuralnet = ConnectedNeuralnet(1, 1)
        self.assertEqual(neuralnet.get_configuration(),
                         [[(1,)], [(1,)], [(1,)]], "Unexpected default configuration of net")

        neuralnet = ConnectedNeuralnet(4, 1)
        self.assertEqual(neuralnet.get_configuration(),
                         [[(1, 1, 1, 1)], [(1,)], [(1,)]],
                         "Unexpected default configuration of net")


if __name__ == "__main__":
    unittest.main()
