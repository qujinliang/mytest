
from random import randint

# L = [randint(0,5) for i in range(5)]
L= [0,3,1,4,2]
print(L)

def quick_sort(L,low,hight):
    i = low
    j = hight
    if low > hight:
        return
    # L[i]==L[0] 赋值给key 作为标记位
    key = L[i]
    while i < j:
        # 日过i<j,也就是起始下标必须小于结束下标值
        # 并且L[j]的值大于标记key，那么 j 就-1
        while i < j and L[j] >= key:
            j = j-1
        # 如果L[j]>=key的话就是 L[j-1]的值给L[i],否则就直接把L[j]的值给L[i]
        L[i] = L[j]
        print(L[i])
        # 如果L[i]位置的值小于key，那么i+1，第一次循环必然L[i]==key，所以i+1
        while i < j and L[i] <= key:
            i = i + 1
        # 如果L[i]<=key的话就是 L[j]=L[i+1],否则直接L[j]=L[i]
        L[j] = L[i]
        print('L[j]: %s' % L[j])
    # 把key的值放到L[i]的位置
    L[i] = key
    print('key:%s' %key)
    # 开始递归quick_sort 先从前半段0 -- i-1开始排序
    quick_sort(L,low,i-1)
    # 然后再次 递归quick_sort 再从后半段 j+1 -- hight 结束排序
    quick_sort(L,j+1,hight)
    return L

print(quick_sort(L,0,len(L)-1))
