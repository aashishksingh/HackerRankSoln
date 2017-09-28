#!usr/bin/env python3

arr=list(map(int,input().split()))
n,m,k=arr[0],arr[1],arr[2]
index=dict()
for i in range(k):
        arr=list(map(int,input().split()))
        if arr[0] in index:
                if(arr[1]<=max(index[arr[0]])):
                        index[arr[0]].remove(max(index[i+1])
                        index[arr[0]].append(arr[2])
                else:
                        index[arr[0]].append(arr[1])
                        index[arr[0]].append(arr[2])        
        else:
                a=[]
                a.append(arr[1])
                a.append(arr[2])
                index[arr[0]]=a
                del a
                
cntr=0
for i in range(n):
        if i+1 in index:
                for j in range(1,len(index[i+1],2):
                        cntr+=index[i+1][j]-index[i+1][j-1]

print(n*m-cntr)                                       
