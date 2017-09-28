#!/bin/python3

import sys,math


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    lst=[]
    for i in range(1,n+1):
        if i-k>0:
            if not i-k in lst:
                lst.append(i-k)
            else:
                lst.append(i+k)
        else:
            lst.append(i+k)
    #print('lst',lst)
    a=set(lst)
    flag=0
    #print(a)
    for i in range(1,n+1):
        if not i in lst:
            flag=1
    if flag:
        print(-1)
    else:
        cntr=1
        arr=[0]*(n+1)
        #print(arr)
        for i in range(len(lst)):
            arr[lst[i]]=cntr
            cntr+=1
        for i in range(1,len(arr)):
            print(arr[i],end=' ')
        print()    

        
        
 
