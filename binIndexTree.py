#!usr/bin/env python3

n=int(input().strip())
arr=list(map(int,input().split()))
temp=[i for i in arr]   #copy of the original list
arr=[0]+arr #BIT works for 1-based arrays, not 0-based 

def initialize(array):  #adding to the binary index tree i.e. forming the Binary Indexed Tree for the 'array'
    for idx in range(1, len(array)):
        idx2 = idx + (idx & -idx)
        if idx2 < len(array):
            array[idx2] += array[idx]

def sum_arr(bit_arr,idx):
    result=0
    while idx:
        result+=bit_arr[idx]
        idx-=idx & -idx
    return result
    
initialize(arr)
print(sum_arr(arr,2))
print(temp)                     
