"""
 Created by qujl on 2018-05-10
"""
__author__ = 'qujl'

from random import randint

# quick_sort
L = [randint(0,5) for i in range(5)]
print(L)
def quick_sort(L, left, right):
    i = left
    j = right
    if i >= j:
        return
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1
        L[i] = L[j]
        while i < j  and L[i] <= key:
            i = i+1
        L[j] = L[i]
    L[i] = key
    quick_sort(L,left,i-1)
    quick_sort(L,j+1,right)
    return L

dd = quick_sort(L,0,len(L)-1)
print(dd)