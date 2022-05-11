import networkx as nx
import numpy as np

from Tools.Profiler import profile
from qwak.qwak import QWAK, StochasticQWAK

from Tools.testVariables import (
    probDistUniformSuperpositionCycle,
    probDistUniformSuperpositionComplete,
    orientedGraph,
    probDistUniformSuperpositionCycleOriented,
    probDistUniformSuperpositionPath,
    stochasticProbDistSingleNodeCycleNoise,
    stochasticProbDistSingleNodeCycleNoNoise,
)

probDistUniformSuperpositionCycle = np.asarray(
    probDistUniformSuperpositionCycle
).flatten()
probDistUniformSuperpositionComplete = np.asarray(
    probDistUniformSuperpositionComplete
).flatten()
probDistUniformSuperpositionCycle = np.asarray(
    probDistUniformSuperpositionCycle
).flatten()
probDistUniformSuperpositionCycleOriented = np.asarray(
    probDistUniformSuperpositionCycleOriented
).flatten()
probDistUniformSuperpositionPath = np.asarray(
    probDistUniformSuperpositionPath
).flatten()

import unittest


class QWAKTest(unittest.TestCase):
    def test_ProbDistUniformSuperpositionCycle(self):
        n = 100
        t = 12
        qwak = QWAKTestStub()
        np.testing.assert_almost_equal(
            qwak.getProbVec(),
            np.zeros(n),
            err_msg="Probability distribution before running should be 0.",
        )
        qwak.buildWalk()
        np.testing.assert_almost_equal(
            qwak.getProbVec(),
            probDistUniformSuperpositionCycle,
            err_msg=f"Probability Distribution does not match expected for n = {n} and t = {t}",
        )

    def test_ProbDistUniformSuperpositionComplete(self):
        n = 100
        t = 12
        self.t = t
        graph = nx.complete_graph(n)
        initStateList = [n // 2, n // 2 + 1]
        laplacian = False
        markedSearch = None
        qwak = QWAKTestStub(
            QWAK(
                graph,
                initStateList=initStateList,
                customStateList=None,
                laplacian=laplacian,
                markedSearch=markedSearch,
            )
        )
        np.testing.assert_almost_equal(
            qwak.getProbVec(),
            np.zeros(n),
            err_msg="Probability distribution before running should be 0.",
        )
        qwak.buildWalk(t)
        np.testing.assert_almost_equal(
            qwak.getProbVec(),
            probDistUniformSuperpositionComplete,
            err_msg=f"Probability Distribution does not match expected for n = {n} and t = {t}",
        )

    def test_ProbDistUniformSuperpositionCycleOriented(self):
        n = 100
        t = 12
        self.t = t
        graph = orientedGraph
        initStateList = [n // 2, n // 2 + 1]
        laplacian = False
        markedSearch = None
        qwak = QWAKTestStub(
            QWAK(
                graph,
                initStateList=initStateList,
                customStateList=None,
                laplacian=laplacian,
                markedSearch=markedSearch,
            )
        )
        np.testing.assert_almost_equal(
            qwak.getProbVec(),
            np.zeros(n),
            err_msg="Probability distribution before running should be 0.",
        )
        qwak.buildWalk(t)
        np.testing.assert_almost_equal(
            qwak.getProbVec(),
            probDistUniformSuperpositionCycleOriented,
            err_msg=f"Probability Distribution does not match expected for n = {n} and t = {t}",
        )

    def test_ProbDistUniformSuperpositionPath(self):
        n = 100
        t = 12
        self.t = t
        graph = nx.path_graph(n)
        initStateList = [n // 2, n // 2 + 1]
        laplacian = True
        markedSearch = None
        qwak = QWAKTestStub(
            QWAK(
                graph,
                initStateList=initStateList,
                customStateList=None,
                laplacian=laplacian,
                markedSearch=markedSearch,
            )
        )
        np.testing.assert_almost_equal(
            qwak.getProbVec(),
            np.zeros(n),
            err_msg="Probability distribution before running should be 0.",
        )
        qwak.buildWalk(t)
        np.testing.assert_almost_equal(
            qwak.getProbVec(),
            probDistUniformSuperpositionPath,
            err_msg=f"Probability Distribution does not match expected for n = {n} and t = {t}",
        )


class QWAKTestStub:
    def __init__(self, testQwak=None):
        n = 100
        self.t = 12
        graph = nx.cycle_graph(n)
        initStateList = [n // 2, n // 2 + 1]
        laplacian = False
        markedSearch = None
        if testQwak is None:
            self.qwak = QWAK(
                graph,
                initStateList=initStateList,
                customStateList=None,
                laplacian=laplacian,
                markedSearch=markedSearch,
            )
        else:
            self.qwak = testQwak

    def buildWalk(self,t=None):
        if t is not None:
            self.t = t
        self.qwak.runWalk(time = self.t)

    def getProbVec(self):
        return self.qwak.getProbVec()
