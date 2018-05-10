"""
 Created by qujl on 2018-05-09
"""
__author__ = 'qujl'

from random import randint
num = [randint(0,20) for _ in range(30)]


def QuickSort(arr, firstIndex, lastIndex):
    if firstIndex < lastIndex:
        divIndex = Partition(arr, firstIndex, lastIndex)

        QuickSort(arr, firstIndex, divIndex)
        QuickSort(arr, divIndex + 1, lastIndex)
    else:
        return

def Partition(arr, firstIndex, lastIndex):
    i = firstIndex - 1
    for j in range(firstIndex, lastIndex):
        if arr[j] <= arr[lastIndex]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[lastIndex] = arr[lastIndex], arr[i + 1]
    return i


QuickSort(num,0,len(num)-1)

print(num)


