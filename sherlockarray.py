#!usr/bin/env python3

import sys

def initialize(array):  #adding to the binary index tree i.e. forming the Binary Indexed Tree for the 'array'
    array=[0]+array
    for idx in range(1, len(array)):
        idx2 = idx + (idx & -idx)
        if idx2 < len(array):
            array[idx2] += array[idx]
    return array        

def sum_arr(bit_arr,idx):
    result=0
    while idx:
        result+=bit_arr[idx]
        idx-=idx & -idx
    return result


def solve(a,n,total):
    # Complete this function
    if(n==1):
        return 'YES'
    left=0
    for i in range(1,n-1):
        left+=a[i-1]
        
        if(left==(total-left-a[i])):
            #print(i)
            return 'YES'
    return 'NO'    

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    #a = initialize(a)   #my edit
    #print(a)
    ar=initialize(a)
    total=sum_arr(ar,n)
    result = solve(a,n,total)
    print(result)
