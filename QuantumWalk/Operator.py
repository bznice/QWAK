import networkx as nx
import numpy as np
from scipy import linalg

import QuantumWalk.Graph
from QuantumWalk.graphs import Graph

class Operator:
    def __init__(self,graph,n,time=0,gamma=1):
        self._graph = graph
        self._adjacencyMatrix = nx.adjacency_matrix(graph).todense()
        self._time = time
        self._gamma = gamma
        self._n = n
        self._operator = np.zeros((self._n,self._n))

    def __mul__(self,other):
        return self._operator*other

    def __rmul__(self,other):
        return other*self._operator

    def buildOperator(self):
        self._operator = linalg.expm(-1j * self._gamma * self._adjacencyMatrix * self._time)

    def setTime(self,newTime):
        self._time = newTime

    def getTime(self):
        return self._time

    def setGamma(self, newGamma):
        self._gamma = newGamma

    def getGamma(self):
        return self._gamma

    def setDim(self,newDim):
        self._n = newDim

    def getDim(self):
        return self._n

    def setOperator(self,newOperator):
        self._n = newOperator.getDim()
        self._gamma = newOperator.getGamma()
        self._time = newOperator.getTime()
        self._operator = newOperator.getOperator()

    def getOperator(self):
        return self._operator

    def getAdjacencyMatrix(self):
        return self._adjacencyMatrix