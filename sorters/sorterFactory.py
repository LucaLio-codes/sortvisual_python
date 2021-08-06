from sorters.bubble import BubbleSort
from sorters.insertion import InsertionSort
from sorters.merge import MergeSort
from sorters.quick import QuickSort
from util.sorttype import SortType


def getSorter(enum, data):

    if enum == SortType.INSERTION:
        return InsertionSort(data)
    if enum == SortType.BUBBLE:
        return BubbleSort(data)
    if enum == SortType.QUICK:
        return QuickSort(data)
    if enum == SortType.MERGE:
        return MergeSort(data)




