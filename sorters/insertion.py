from sorters.sorter import Sorter


class InsertionSort(Sorter):

    def __init__(self, data):
        super(InsertionSort, self).__init__(data)

    def algo(self):
        for i in range(len(self.data)):
            j = i
            while j > 0 and self.data[j-1] > self.data[j]:
                self.swap(j, j-1)
                j -= 1
            i += 1