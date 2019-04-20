#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time   : 2019/1/10 8:34
#@Author : Yun
#@File   : fast-sort.py
def quick_sort(alist, first, last):
    '''快速排序'''
    if first >= last:
        return
    n = len(alist)
    mid_value = alist[first]
    low = first
    high = last

    while low < high:
        while low < high and  alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        #low += 1
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
        #high -= 1
    #从循环退出时 low = high
    alist[low] = mid_value

    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)

if __name__ == "__main__":
    alist = [12,6,3,89,45,25]
    print(alist)
    quick_sort(alist, 0 ,len(alist)-1)
    print(alist)

