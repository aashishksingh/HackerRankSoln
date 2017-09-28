#!usr/bin/env python3
a=[5,3,4,8,6,7]
s=[1]*6
for i in range(6):
    for j in range(i):
        if a[i]>=a[j]:
            s[i]=s[j]+1
print(s[5])        
