#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())

for c in s:
    if('a'<=c<='z'):
        new=97+(ord(c)-97+k)%26
        s=s.replace(c,chr(new))
    if('A'<=c<='Z'):
        new=65+(ord(c)-65+k)%26
        s=s.replace(c,chr(new))
print(s)
