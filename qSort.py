#!/usr/bin/env python
import numpy as np


def partition(toSort = [], idx_1 = None, idx_2 = None):
    x = toSort[idx_2]
    i = idx_1 - 1
    for j in range(idx_1, idx_2):
        if(toSort[j] <= x) :
            i+=1
            tmp = toSort[i]
            toSort[i] = toSort[j]
            toSort[j] = tmp
    tmp = toSort[i+1]
    toSort[i+1] = toSort[idx_2]
    toSort[idx_2] = tmp
    print toSort
    return i+1
    

def Quick_sort(toSort, idx_1, idx_2):
    if(idx_1 < idx_2):
        q = partition(toSort,idx_1,  idx_2)
        Quick_sort(toSort,idx_1, q-1)
        Quick_sort(toSort,q+1, idx_2)
        
        
        
def ran_partition(toSort = [], idx_1 = None, idx_2 = None):
    # Choose a random pivot point
    i = int(np.random.uniform(low = idx_1,high = idx_2,size = 1))
    tmp = toSort[idx_2]
    toSort[idx_2] = toSort[i]
    toSort[i] = tmp
    return( partition(toSort,idx_1,  idx_2))
    
def ran_Qsort(toSort, idx_1, idx_2):
    if(idx_1 < idx_2):
        q = ran_partition(toSort,idx_1,  idx_2)
        ran_Qsort(toSort,idx_1, q-1)
        ran_Qsort(toSort,q+1, idx_2)

        
def main():
    numbers = np.random.random_integers(low = 0, high = 1000, size = 20 )	
    print numbers
    ran_Qsort(numbers,0,len(numbers)-1)
    print numbers
    
if __name__ == '__main__':
    main()