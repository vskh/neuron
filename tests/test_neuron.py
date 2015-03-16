__author__ = 'Vadym S. Khondar'

import unittest

from neuron import Neuron


class Test(unittest.TestCase):
    def test_neuron_excite(self):
        n = Neuron()
        n.excite()
        self.assertTrue(n.is_excited(), "Neuron should be excited")

    def test_neuron_inhibit(self):
        n = Neuron()
        n.inhibit()
        self.assertFalse(n.is_excited(), "Neuron should not be excited")

    def test_neuron_reacts_to_inputs(self):
        n = Neuron()

        class NeuronMock:
            def is_excited(self):
                return True

            def activate(self):
                n.notify()

        m1 = NeuronMock()
        n.connect_dendrite(m1)

        m2 = NeuronMock()
        n.connect_dendrite(m2)

        m1.activate()

        self.assertTrue(n.is_excited(), "Neuron should be excited")

    def test_neuron_dendrite_weight(self):
        n = Neuron()
        with self.assertRaises(
                LookupError):  # , "Neuron should raise error for not existing dendrite"):
            n.set_dendrite_weight_by_idx(0, 0)
        n2 = Neuron()
        n.connect_dendrite(n2)
        n.set_dendrite_weight_by_idx(0, 0.5)


if __name__ == "__main__":
    unittest.main()
