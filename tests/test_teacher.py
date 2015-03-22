__author__ = 'Vadym S. Khondar'

import unittest

from teacher import GeneticTeacher
from neuralnet import ConnectedNeuralnet


class Test(unittest.TestCase):
    def setUp(self):
        net = ConnectedNeuralnet(1, 1)
        self.teacher = GeneticTeacher(net, [], 10, 50)

    def test_gen_subpopulation(self):
        subpop = self.teacher._GeneticTeacher__gen_subpopulation(10)
        self.assertEqual(len(subpop), 10, "Generated population should have 10 items")

    def test_retire(self):
        self.teacher._GeneticTeacher__gen_population()
        self.assertEqual(len(self.teacher._GeneticTeacher__current_pop), 100, "Default generated "
                                                                              "population should "
                                                                              "have 100 items")
        self.teacher._GeneticTeacher__retire()
        self.assertLess(len(self.teacher._GeneticTeacher__current_pop), 100, "After retirement "
                                                                             "population should "
                                                                             "be less than 100")
        self.assertGreater(len(self.teacher._GeneticTeacher__current_pop), 50, "After retirement "
                                                                               "population should "
                                                                               "be greater than 50")

    def test_crossover_once(self):
        children = GeneticTeacher._GeneticTeacher__crossover_once([0.1, 0.2, 0.3, 0.4],
                                                                  [0.5, 0.6, 0.7, 0.8], 1)

        self.assertEqual(children,
                         ([0.1, 0.6, 0.7, 0.8], [0.5, 0.2, 0.3, 0.4]),
                         "Invalid crossover")

if __name__ == "__main__":
    unittest.main()
