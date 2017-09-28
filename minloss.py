#!usr/bin/env python3

n=int(input().strip())
arr=list(map(int,input().split()))
temp=list(arr)
arr.sort()
mini=99999999
for i in range(1,len(arr)):
    if(mini>temp[i]-temp[i-1]) and (arr.index(temp[i])<arr.index(temp[i-1])) :
        mini=temp[i]-temp[i-1]

print(mini)        
