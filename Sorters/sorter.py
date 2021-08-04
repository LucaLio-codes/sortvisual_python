from abc import ABC, abstractmethod
import math


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


class BubbleSort(Sorter):

    def __init__(self, data):
        super().__init__(data)
        self.n = len(self.data)
        self.i = 1
        self.swapped = False
        self.finished = False
        self.first = True

    def isFinished(self):
        return self.finished

    def reset(self):
        self.i = 1
        self.finished = False
        self.n = len(self.data)
        self.first = True

    def step(self):
        if self.i <= self.n - 1:
            self.swapped = False
            if self.data[self.i-1] > self.data[self.i]:
                self.data[self.i - 1], self.data[self.i] = self.data[self.i], self.data[self.i - 1]
                self.swapped = True
            self.i += 1
        elif not self.swapped and not self.first :
            self.finished = True
        else:
            self.n -= 1
            self.first = False
            self.i = 1


class QuickSort(Sorter):

    def __init__(self, data):
        super().__init__(data)
        self.isInAlgo = False
        self.lo = 0
        self.hi = len(self.data)
        self.j = 0
        self.i = 0
        self.x = 0
        self.first_partition = True
        self.first = True
        self.retvalue = -1
        self.size = self.hi - self.lo + 1
        self.stack = [0] * self.size
        self.top = -1
        self.top += 1
        self.stack[self.top] = self.lo
        self.top += 1
        self.stack[self.top] = self.hi
        self.finished = False


    def reset(self):
        self.isInAlgo = False
        self.lo = 0
        self.hi = len(self.data) -1
        self.j = 0
        self.i = 0
        self.x = 0
        self.first_partition = True
        self.first = True
        self.retvalue = -1
        self.size = self.hi - self.lo + 1
        self.stack = [0] * self.size
        self.top = 0
        self.top += 1
        self.stack[self.top] = self.lo
        self.top += 1
        self.stack[self.top] = self.hi
        self.finished = False




    def isFinished(self):
        return self.finished


    def step(self):
        if self.top < 0 and not self.isInAlgo:
            self.finished = True
        elif self.isInAlgo:
            self.partition()
        elif self.retvalue != -1:
            if self.retvalue - 1 > self.lo:
                self.top += 1
                self.stack[self.top] = self.lo
                self.top += 1
                self.stack[self.top] = self.retvalue - 1
            if self.retvalue + 1 < self.hi:
                self.top += 1
                self.stack[self.top] = self.retvalue + 1
                self.top += 1
                self.stack[self.top] = self.hi
            self.retvalue = -1
        else:
            self.hi = self.stack[self.top]
            self.top -= 1
            self.lo = self.stack[self.top]
            self.top -= 1

            self.isInAlgo = True
            self.first_partition = True
            self.retvalue = -1
            self.j = self.lo


    def partition(self):
       l = self.lo
       h = self.hi
       if self.first_partition:
           self.i = l-1
           mid = math.floor((l+h)/2.)
           if self.data[mid] < self.data[l]:
               self.data[mid], self.data[l] = self.data[l], self.data[mid]
           if self.data[h] < self.data[l]:
               self.data[h], self.data[l] = self.data[l], self.data[h]
           if self.data[mid] < self.data[h]:
               self.data[mid], self.data[h] = self.data[h], self.data[mid]
           self.x = self.data[h]
           self.first_partition = False

       if self.j in range(l,h):
           if self.data[self.j] <= self.x:
               self.i += 1
               self.data[self.i], self.data[self.j] = self.data[self.j], self.data[self.i]
           self.j += 1
       else:
           self.data[self.i +1], self.data[h] = self.data[h], self.data[self.i +1]
           self.retvalue = self.i+1
           self.isInAlgo = False

