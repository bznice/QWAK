import networkx as nx
from matplotlib import pyplot as plt

from qwak.GraphicalQWAK import GraphicalQWAK

if __name__ == "__main__":

    staticN = 100
    dynamicN = staticN
    t = 12
    initState = [staticN // 2, (staticN // 2) + 1]
    graph = nx.complete_graph(staticN)
    timeList = [0, 12]
    initStateList = [[staticN // 2, (staticN // 2) + 1]]

    gQwak = GraphicalQWAK(
        staticN,
        dynamicN,
        graph,
        graph,
        initState,
        initStateList,
        t,
        timeList)

    print(gQwak.runMultipleWalks()[1])
