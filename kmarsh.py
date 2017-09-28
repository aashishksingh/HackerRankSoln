#!usr/bin/env python3

m,n=tuple(input().split())

field=[[input().strip() for i in range(n)]for _ in range(m)] 

c=[[]
def maxPeri(field,m,n):
    
    i=-1
    j=-1
    for k in range(m):
        if field[k]=='X':
            i=k
            break
    if i==-1:
        i=m
    
    for k in range(m):
        if field[k]=='X':
            j=k
            break
    if j==-1:
        j=n
        
    c    
