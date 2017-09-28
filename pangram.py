#!/bin/python3

import sys


s=str(input().strip().lower())
letters='abcdefghijklmnopqrstuvwxyz'
d=[]
for c in letters:
    d.append([c,-1])
for i in range(len(d)):
    if d[i][0] in s:
        d[i][1]=s.index(d[i][0])
cntr=0
for i in range(len(d)):
    if(d[i][1]>=0):
        cntr=cntr+1
print(d)        
if (cntr>=26):
    print('pangram')
else:
    print('not pangram')
