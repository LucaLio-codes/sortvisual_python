import math
import random
import sys
from sorters.sorter import Sorter


class QuickSort(Sorter):

    def __init__(self, data):
        super(QuickSort, self).__init__(data)

    def algo(self):
        self.quick(0, len(self.data)-1)

    def quick(self, lo, hi):
        if hi - lo >= 1:
            if lo < hi:
                p = self.partition(lo, hi)
                self.quick(lo, p-1)
                self.quick(p+1, hi)

    def partition(self, lo, hi):

        pivot = self.data[hi]
        i = lo-1

        for j in range(lo,hi):
            if self.data[j] <= pivot:
                i = i+1
                self.swap(i, j)
        self.swap(i+1, hi)
        return i + 1


if __name__ == '__main__':
    data = [i for i in range(10)]
    random.shuffle(data)
    print(data)
    dut = QuickSort(data)
    print(data)