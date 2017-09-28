#! usr/bin/env python3

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    arr=list(map(int,input().split()))
    j=1
    cntr=0
    while(j<n):
    
        v=arr[j]
        i=j-1
        while(arr[i]>v) and i>=0:
            arr[i+1]=arr[i]
            cntr+=1
            i-=1
        arr[i+1]=v
        j+=1
    if cntr%2==0:
        print('YES')
    else:
        print('NO')
