#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    lst=list(s)
    # your code goes here
    word='hackerrank'
    d=[]
    flag=False
    for c in word:
        d.append([c,-1])
   # print(d)
    #print(s.index('a'))
    j=-1
    for i in range(len(d)):
        if d[i][0] in lst[j+1:]:
            d[i][1]=lst[j+1:].index(d[i][0])+j+1
            j=d[i][1]
    print(d)        
    for i in range(len(d)-1):
        if (d[i][1]>=d[i+1][1]) and (d[i][1]>0):
            flag=True
    if not (flag):
        print("YES")
    else:
        print("NO")
