# Python3 program for the above approach
import math


# Calculating next gap
def nextGap(gap):
    if gap <= 1:
        return 0

    return int(math.ceil(gap / 2))


# Function for swapping
def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


# Merging the subarrays using shell sorting
# Time Complexity: O(nlog n)
# Space Complexity: O(1)
def inPlaceMerge(nums, start, end):
    gap = end - start + 1
    gap = nextGap(gap)

    while gap > 0:
        i = start
        while (i + gap) <= end:
            j = i + gap

            if nums[i] > nums[j]:
                swap(nums, i, j)

            i += 1

        gap = nextGap(gap)


# merge sort makes log n recursive calls
# and each time calls merge()
# which takes nlog n steps
# Time Complexity: O(n*log n + 2((n/2)*log(n/2)) +
# 4((n/4)*log(n/4)) +.....+ 1)
# Time Complexity: O(logn*(n*log n))
# i.e. O(n*(logn)^2)
# Space Complexity: O(1)
def mergeSort(nums, s, e):
    if s == e:
        return

    # Calculating mid to slice the
    # array in two halves
    mid = (s + e) // 2

    # Recursive calls to sort left
    # and right subarrays
    mergeSort(nums, s, mid)
    mergeSort(nums, mid + 1, e)

    inPlaceMerge(nums, s, e)


# UTILITY FUNCTIONS
# Function to pran array
def printArray(A, size):
    for i in range(size):
        print(A[i], end=" ")

    print()


# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    arr_size = len(arr)

    mergeSort(arr, 0, arr_size - 1)
    printArray(arr, arr_size)

# This code is contributed by adityapande88