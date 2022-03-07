import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
import timeit
import sympy as sp
from sympy.abc import pi
from math import sqrt, ceil, pow
from qwak.qwak import QWAK
from qwak.operator import Operator

if __name__ == '__main__':
    n = 100
    t = 0
    # gamma = 1 / (2 * np.sqrt(2))
    graph = nx.cycle_graph(n)
    # graph = nx.complete_bipartite_graph(20,20)
    # graph = nx.hypercube_graph(3)

    # marked = [int(n / 2)]
    marked = [50,51]
    # marked = range(n)
    # marked = range(int(n))
    # qwController = QWAK(graph, laplacian=True,markedSearch=[(0,1j)])
    qwController = QWAK(graph, laplacian=False)
    # sp.pprint(f"PST {qwController.checkPST(0,2)}")
    qwController.runWalk(t, marked)

    # qwOperator = Operator(graph=graph)
    # qwOperator.buildDiagonalOperator(1)
    # print(qwOperator.getAdjacencyMatrix())
    # print(f"{qwOperator}\n")
    # qwOperator.setAdjacencyMatrix(nx.adjacency_matrix(nx.complete_graph(n)).todense())
    # print(qwOperator.getAdjacencyMatrix())
    # qwOperator.buildDiagonalOperator(1)
    # print(qwOperator)

    print(f"Mean: {qwController.getProbDist().mean()}\t "
          f"Moment 1: {qwController.getProbDist().moment(1)}\n"
          f"Moment 2: {qwController.getProbDist().moment(2)}\n"
          f"Stdev: {qwController.getProbDist().stDev()}\n"
          f"Survival Probability: {qwController.getProbDist().survivalProb(0,0)}\n"
          f"Inverse Part. Ratio: {qwController.getWalk().invPartRatio()}\n")
    #       f"PST {qwController.checkPST(0,2)}")

    # G = nx.Graph()
    # for i in range(0,100):
    #     G.add_edge(f"{i}",f"{i+1}",weight=2)
    #     # print(f" {i} ---- {i+1}")
    # G.add_edge("100","101", weight=2)
    # G.add_edge("100","a", weight=2)
    # G.add_edge("100","b", weight=2)
    # G.add_edge("100","c", weight=2)
    # for i in range(101, 199):
    #     G.add_edge(f"{i}", f"{i + 1}", weight=2)
    #     # print(f" {i} ---- {i+1}")
    # G.add_edge("199", "0", weight=2)
    #
    # # print(nx.adjacency_matrix(G))
    #
    # # graph=G
    # qwController = QWAK(graph, laplacian=True)
    # qwController.runWalk(t, gamma, [100])
    #
    # qwProbabilities = qwController.getProbDist()
    # qwProbVec = qwProbabilities.getProbVec()
    #
    # m = 0
    # std = 0
    # pos = np.arange(0,len(qwProbVec))
    # for x in range(len(qwProbVec)):
    #     m += pos[x] * qwProbVec[x]
    #
    # for x in range(len(qwProbVec)):
    #     std += (qwProbVec[x] * (pos[x] - m)**2)/(t**2)
    #
    # # print(G)
    # print(qwProbabilities.mean())
    # print(qwProbabilities.stdev())
    # # print(std)
    # nx.draw(G)
    # plt.show()
    # plt.plot(qwProbVec)
    # plt.show()

    # print(qwProbabilities.mean())
    # print(m)
    # print(qwProbabilities.std())