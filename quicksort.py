#!usr/bin/env python3

n=int(input().strip())
ar=list(map(int,input().split()))

def partition(A, lo, hi):
    pivot = A[hi]
    i = lo - 1    
    for j in  range(lo,hi):
        if A[j] <= pivot:
            i = i + 1
            if not i == j:
                A[i],A[j]=A[j],A[i]
    A[i+1]A[hi]=A[hi],A[i+1]
    return i + 1
    
def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p - 1)
        quicksort(A, p + 1, hi)

quicksort(ar,0,len(ar)-1)
