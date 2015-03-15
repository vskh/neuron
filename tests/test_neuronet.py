__author__ = 'Vadym S. Khondar'

import unittest

from neuronet import ConnectedNeuronet


class ConnectedNeuronetTest(unittest.TestCase):
    def test_neuronet_construct_with_zero_inputs(self):
        with self.assertRaises(ValueError): #, "Neuronet with zero inputs should not be possible"):
            ConnectedNeuronet(0, 2)

    def test_neuronet_construct_with_zero_outputs(self):
        with self.assertRaises(ValueError): #, "Neuronet with zero outputs should not be possible"):
            ConnectedNeuronet(1, 0)

    def test_neuronet_construct_with_defaults_layers_conf(self):
        neuronet = ConnectedNeuronet(1, 1)
        self.assertEqual(neuronet.get_num_layers(), 3, "Default neuronet should contain 3 layers")
        self.assertEqual(len(neuronet._get_layer(0)), 1, "Default neuronet should have 1 "
                                                         "input neuron")
        self.assertEqual(len(neuronet._get_layer(2)), 1, "Default neuronet should have 1 "
                                                         "output neuron")
