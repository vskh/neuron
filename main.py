__author__ = 'Vadym S. Khondar'

from neuralnet import ConnectedNeuralnet
from teacher import GeneticTeacher

training_set1 = [
    ((0, 0, 0), (1, 1, 1)),
    ((0, 0, 1), (1, 1, 0)),
    ((0, 1, 0), (1, 0, 1)),
    ((0, 1, 1), (1, 0, 0)),
    ((1, 0, 0), (0, 1, 1)),
    ((1, 0, 1), (0, 1, 0)),
    ((1, 1, 0), (0, 0, 1)),
    ((1, 1, 1), (0, 0, 0)),
]

training_set2 = [
    ((1,), (0,)),
    ((0,), (1,))
]

net1 = ConnectedNeuralnet(3, 3, [
    [(1, 1, 1), (1, 1, 1), (1, 1, 1)],
    [(1, 1, 1), (1, 1, 1), (1, 1, 1)],
    [(1, 1, 1), (1, 1, 1), (1, 1, 1)]
])

net2 = ConnectedNeuralnet(1, 1)

teacher1 = GeneticTeacher(net1, training_set1, 0.05, 0.1)
teacher2 = GeneticTeacher(net2, training_set2, 0.05, 0.1)

teacher2.teach()
