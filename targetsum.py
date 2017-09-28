#! usr/bin/env python3

t=int(input().strip())
for i in range(t):
    m=int(input().strip())
    n=int(input().strip())
    arr=list(map(int,input().split()))
    temp=[i for i in arr]
    indexdict=dict()
    for i in range(len(arr)):
        if not arr[i] in indexdict:
            a=[]
            a.append(i)
            indexdict[arr[i]]=a
            del a
        else:
            indexdict[arr[i]].append(i)
    arr.sort()
    i=0
    j=len(arr)-1
    while(i<=j):
        s=arr[i]+arr[j]
        #print(s,m)
        if(s==m):
            #print(arr[i],arr[j])
            if(arr[i]==arr[j]):
                for i in indexdict[arr[i]]:
                    print(i+1,end=' ')
            else:
                if(indexdict[arr[i]][0]+1<indexdict[arr[j]][0]+1):
                    print(indexdict[arr[i]][0]+1,indexdict[arr[j]][0]+1)
                else:
                    print(indexdict[arr[j]][0]+1,indexdict[arr[i]][0]+1)
            break
        elif s<m:
            i+=1
        else:
            j-=1
            
            
