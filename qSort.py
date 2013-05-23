#!/usr/bin/env python

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
        
def main():
    numbers = [1,7,11,3,4,5,2,6,2,8,19,23,47,89]
    print numbers
    Quick_sort(numbers,0,len(numbers)-1)
    print numbers
    
if __name__ == '__main__':
    main()