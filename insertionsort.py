#!usr/bin/env python3

n=int(input().strip())
arr=list(map(int,input().split()))
l=len(arr)

def insertionSort(arr):
    j=l-1

    v=arr[j]
    while(arr[j-1]>v) and j>0:
        arr[j]=arr[j-1]
        for i in arr:
            print(i,end=' ')
        print()
        j=j-1
    arr[j]=v    
    for i in arr:
        print(i,end=' ')

insertionSort(arr)        
