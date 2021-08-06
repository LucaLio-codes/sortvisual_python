from sorters.sorter import Sorter


class BubbleSort(Sorter):

    def __init__(self, data):
        super().__init__(data)


    def algo(self):
        n = len(self.data)
        swapped = True
        while swapped:
            swapped = False
            for i in range(n-1):
                if self.data[i] > self.data[i + 1]:
                    self.swap(i, i+1)
                    swapped = True
            n -= 1


if __name__ == '__main__':
    dut = BubbleSort([1,2,3])
    print(str(dut))