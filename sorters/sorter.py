from abc import ABC, abstractmethod
from util.fifo import Fifo
import time


class Sorter(ABC):

    def __init__(self, data):
        self.data = data
        self.stack = Fifo()
        self.comparisons = 0
        self.opperations = 0
        start = time.time()
        self.algo()
        end = time.time()
        self.timeElapsed = end-start

    def __str__(self):
        return self.__class__.__name__

    @abstractmethod
    def algo(self):
        pass

    def swap(self, i, j):
        self.stack.push(i)
        self.stack.push(j)
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.opperations += 1

    def getStack(self):
        return self.stack

    def getTimeMs(self):
        return self.timeElapsed

    def getComparisons(self):
        return self.comparisons

    def getOperations(self):
        return self.opperations


