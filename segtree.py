#Segment tree for range queries of the minimum

n=int(input().strip())
arr=list(map(int,input().split()))
segtree=[0]*(2*n)

#Building the segment tree
for i in range(n,2*n):
    segtree[i]=arr[i-n]
for i in range(n-1,0,-1):
    segtree[i]=min([segtree[2*i],segtree[2*i+1]])


def update(idx,value):
    idx+=n
    segtree[idx]=value
    
    while idx>1:
        idx=idx//2
        segtree[idx]=min((segtree[2*idx],segtree[2*idx+1]))

def queryMin(left,right):
    left+=n
    right+=n
    minimum=9999999999999
    while left<right:
        if left%2:
            minimum=min((minimum,segtree[left]))
            left+=1
        if right%2:
            minimum=min((minimum,segtree[right]))
            right-=1
        left=left//2
        right=right//2
    return minimum         
    
print(segtree)
print(queryMin(2,n-1))                                
