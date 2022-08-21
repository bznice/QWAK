import networkx as nx
import numpy as np

from qwak.qwak import StochasticQWAK
from StochasticQWAKTestStub import StochasticQWAKTestStub

from testVariables import (
    stochasticProbDistSingleNodeCycleNoise,
    stochasticProbDistSingleNodeCycleNoNoise,
)

import pytest


class TestStochasticQWAK(object):
    def test_StochasticProbDistSingleNodeCycleNoNoise(self):
        n = 50
        t = 6
        qwak = StochasticQWAKTestStub()
        np.testing.assert_almost_equal(
            qwak.getProbVec(),
            np.zeros(n),
            err_msg="Probability distribution before running should be 0.",
        )
        qwak.buildWalk(t)
        np.testing.assert_almost_equal(
            qwak.getProbVec(),
            stochasticProbDistSingleNodeCycleNoNoise,
            err_msg=f"Probability Distribution does not match expected for n = {n} and t = {t}",
        )

    def test_StochasticProbDistSingleNodeCycleNoise(self):
        n = 50
        t = 20
        self.t = t
        noiseParam = 0.15
        sinkNode = 10
        sinkRate = 1.0
        graph = nx.cycle_graph(n)
        initStateList = [n // 2]
        qwak = StochasticQWAKTestStub(
            StochasticQWAK(
                graph,
                initStateList=initStateList,
                customStateList=None,
                noiseParam=noiseParam,
                sinkNode=sinkNode,
                sinkRate=sinkRate,
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
            stochasticProbDistSingleNodeCycleNoise,
            err_msg=f"Probability Distribution does not match expected for n = {n} and t = {t}",
        )
