#kth smallest element: O(n)

#!usr/bin/env python3


import random


n=int(input().strip())
arr=list(map(int,input().split()))

def partition(a,left,right,pivot):
    p=a[pivot]
    a[pivot],a[right]=a[right],a[pivot]
    store=left
    for i in range(left,right):
        if(a[i]<p):
            a[i],a[store]=a[store],a[i]
            store+=1
    a[right],a[store]=a[store],a[right]
    return store
            
def select(a,left,right,k):
    if(left==right):
        return a[left]
    pivot=left+int(random.random()*100%(right-left+1))
    pivot=partition(a,left,right,pivot)
    if k==pivot:
        return a[k]
    elif k<pivot:
        return select(a,left,pivot-1,k)
    else:
        return select(a,pivot+1,right,k)

print(select(arr,0,n-1,n//2))
#Call for kth element                    
