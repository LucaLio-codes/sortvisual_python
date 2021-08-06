from sorters.sorter import Sorter
import math


class MergeSort(Sorter):

    def __init__(self, data):
        super(MergeSort, self).__init__(data)

    def algo(self):
        self.mergeSort(0, len(self.data) -1)

    def mergeSort(self, s, e):
        if s >= e:
            return
        m = (s + e) // 2
        self.mergeSort(s, m)
        self.mergeSort(m + 1, e)
        self.merge(s, e)

    def merge(self, start, end):
        gap = end - start + 1
        gap = self.nextGap(gap)

        while gap > 0:
            i = start
            while i + gap <= end:
                j = i + gap
                if self.data[i] > self.data[j]:
                    self.swap(i, j)
                i += 1
            gap = self.nextGap(gap)

    @staticmethod
    def nextGap(gap):
        if gap <= 1:
            return 0
        return int(math.ceil(gap/2))

if __name__ == '__main__':
    dut = MergeSort([5, 4, 3, 2, 1])