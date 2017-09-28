#!usr/bin/env python3

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    a=list(map(int,input().split()))
    ns=[0]*n
    ns[0]=(a[0])
    s=[0]*n
    s[0]=a[0]
    '''
    Note: For ns[i]=max sum for any sub sequence made up of elements before a[i] i.e. it may or may not include a[i]
          For s[i]=max sum of subarray with last element as a[i] i.e. any subarray has to include a[i] at the end
    '''
    for i in range(1,n):
        ns[i]=(max([ns[i-1],ns[i-1]+a[i],a[i]]))
        s[i]=max([s[i-1]+a[i],a[i]])
    print(max(s),ns[n-1])    
