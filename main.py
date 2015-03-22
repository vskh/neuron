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

training_set2 = [((i / 100,), (int(i / 100 < 0.5),)) for i in range(0, 100, 1)]
# training_set2 = [
# ((1,), (0,)),
# ((0.95,), (0,)),
# ((0.9,), (0,)),
#     ((0.85,), (0,)),
#     ((0.75,), (0,)),
#     ((0.6,), (0,)),
#     ((0.55,), (0,)),
#     ((0.5,), (0,)),
#     ((0.45,), (1,)),
#     ((0.4,), (1,)),
#     ((0.35,), (1,)),
#     ((0.25,), (1,)),
#     ((0.2,), (1,)),
#     ((0.15,), (1,)),
#     ((0.1,), (1,)),
#     ((0.05,), (1,)),
#     ((0,), (1,))
# ]

net1 = ConnectedNeuralnet(3, 3, [
    [(1, 1, 1), (1, 1, 1), (1, 1, 1)],
    [(1, 1, 1), (1, 1, 1), (1, 1, 1)],
    [(1, 1, 1), (1, 1, 1), (1, 1, 1)]
])

net2 = ConnectedNeuralnet(1, 1, [
    [(1,)],
    [(1,), (1,)],
    # [(1, 1), (1, 1)],
    [(1, 1)]
])

teacher1 = GeneticTeacher(net1, training_set1, 0.05, 0.1)
teacher2 = GeneticTeacher(net2, training_set2, 0.1, 0.2)

teacher2.teach(1000)
specimen = teacher2.get_best_specimen()
print("Success rate of specimen found is {}".format(specimen[0] / len(training_set2)))

print(specimen)
net2.configure(specimen[1])

net2.set_inputs([0])
print(net2.get_outputs())

net2.set_inputs([1])
print(net2.get_outputs())
