#!usr/bin/env python3

n=int(input().strip())
xarr=[]
sarr=[]
helper={}
for i in range(n):
    x,s=input().split()
    if(i<n//2):
        s='-'
    x=int(x)
    if x in helper:
        helper[x].append(s)
    else:
        helper[x]=[]
        helper[x].append(s)
keys=helper.keys()
#keys.sort()
#print(keys)
#print(helper)
for i in keys:
    for v in helper[i]:
        print(v,end=' ')
