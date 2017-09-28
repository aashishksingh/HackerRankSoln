#!/bin/python3

import sys


s = input().strip()
n = int(input().strip())

sorted(s)

a_set = set()
prev = ''

count = 0
for c in s:
    if c != prev:
        count = 1
        prev = c
    else:
        count +=1
    a_set.add(count * (ord(c) - 96))

for a0 in range(n):
    x = int(input().strip())
    print("Yes" if x in a_set else "No")
