#!usr/bin/env python3

#Returns the index after which k appears in a sorted array

n=int(input().strip())
a=list(map(int,input().split()))

def binarys(a,l,r,k):
    if r<l:
        return -1
    if l==len(a)-1:
        return l    
    mid=(l+r)//2
    if k==a[mid]:
        return mid
    if mid+1<n:
        if a[mid]<k<a[mid+1]:
            return mid
    if k>a[mid]:
        return binarys(a,mid+1,r,k)
    if k<a[mid]:
        return binarys(a,l,mid-1,k)
k=int(input().strip())        
print(binarys(a,0,n-1,k))                         
