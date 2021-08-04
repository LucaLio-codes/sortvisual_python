from abc import ABC, abstractmethod


class Sorter(ABC):

    def __init__(self, data):
        self.data = data

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def isFinished(self):
        return False

    @abstractmethod
    def step(self):
        pass