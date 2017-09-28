#!usr/bin/env python3

#!/bin/python3

import sys

q = int(input().strip())
    
for a0 in range(q):
    n, m, x, y = input().strip().split(' ')
    n, m, x, y = [int(n), int(m), int(x), int(y)]
    adj=dict()
    for a1 in range(m):
        city_1, city_2 = input().strip().split(' ')
        city_1, city_2 = [int(city_1), int(city_2)]
        if not city_1 in adj:
            t=[]
            t.append(city_2)
            adj[city_1]=t
            del t
        else:
            adj[city_1].append(city_2)
        if not city_2 in adj:
            t=[]
            t.append(city_1)
            adj[city_2]=t
            del t
        else:
            adj[city_2].append(city_1)    
        
        
    for i in range(1,n+1):
        if not i in adj:
            t=[]
            adj[i]=t
    if y>=x:
        print(x*n)
        continue
    elif m>0:
        visit=[0]*(n+1)
        visit[0]=-1
        complst=[0]*(n+1)
        complst[0]=-1
        comp=1
        while(complst.count(0)>0):
            st=[]
            st.append(complst.index(0))
            while st:   #DFS
                v=st.pop()
                visit[v]=1
                complst[v]=comp
                for i in adj[v]:
                    if visit[i]==0:
                        st.append(i)
            comp+=1
        del complst[0]
        #print(adj)
        #print(complst)
        comps=set(complst)
        bill=0
        for i in comps:
            bill+=(complst.count(i)-1)*y + x
        print(bill)    
    elif m==0:
        print(n*x)
