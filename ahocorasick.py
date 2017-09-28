#!/bin/python3

import sys,re


n = int(input().strip())
genes = input().strip().split(' ')
health = list(map(int, input().strip().split(' ')))
s = int(input().strip())
#print(health)
table=(genes[i],health[i]) for i in range(len(genes))
#print(table)
lst=[]

for a0 in range(s):
    first,last,d = input().strip().split(' ')
    first,last,d = [int(first),int(last),str(d)]
    # your code goes here
    result=0
    for g in table[first:last+1]:
        occur=len([i for i in range(len(d)) if d.startswith(g[0], i)])
        result=result+occur*g[1]
    lst.append(result)
print(min(lst),max(lst))    

