import timeit

import numpy as np


class StateTest:
    """[summary]
    """

    def __init__(self, n, stateList=None):
        """[summary]

        Args:
            n ([type]): [description]
            stateList ([type], optional): [description]. Defaults to None.
        """
        self._n = n
        self._stateList = stateList
        self._stateVec = np.zeros((self._n, 1))
        self.stateExecutionTime = 0

    def __mul__(self, other):
        """[summary]

        Args:
            other ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self._stateVec * other

    def __rmul__(self, other):
        """[summary]

        Args:
            other ([type]): [description]

        Returns:
            [type]: [description]
        """
        return other * self._stateVec

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return '%s' % self._stateVec

    def buildState(self):
        """[summary]
        """
        if self._stateList is not None:
            for state in self._stateList:
                self._stateVec[state] = 1 / np.sqrt(len(self._stateList))

    def timedBuildState(self):
        """[summary]
        """
        startTimeState = timeit.default_timer()
        self.buildState()
        endTimeState = timeit.default_timer()
        self.stateExecutionTime = (endTimeState - startTimeState)

    def setDim(self, newN):
        """[summary]

        Args:
            newN ([type]): [description]
        """
        self._n = newN

    def getDim(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self._n

    # TODO: This might not be needed.
    def setStateList(self, newState):
        """[summary]

        Args:
            newState ([type]): [description]
        """
        self._stateList = newState

    def getStateList(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self._stateList

    def setStateVec(self, newVec):
        """[summary]

        Args:
            newVec ([type]): [description]
        """
        self._stateVec = newVec

    def getStateVec(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self._stateVec

    def setState(self, newState):
        """[summary]

        Args:
            newState ([type]): [description]
        """
        self._n = newState.getDim()
        self._stateList = newState.getNodeList()
        self._stateVec = newState.getState()
