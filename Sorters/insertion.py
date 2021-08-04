from Sorters.sorter import Sorter


class InsertionSort(Sorter):

    def __init__(self, data):
        super(InsertionSort, self).__init__(data)
        self.i = 1
        self.j = 0

    def reset(self):
        self.i = 1
        self.j = 0

    def step(self):
        if self.i >= len(self.data):
            pass
        else:
            if self.j == 0:
                self.j = self.i
            elif self.j > 0 and self.data[self.j-1] > self.data[self.j]:

                self.data[self.j], self.data[self.j-1] = self.data[self.j-1], self.data[self.j]
                self.j -= 1
            else:

                self.i += 1
                self.j = 0

    def isFinished(self):
        return self.i >= len(self.data)
