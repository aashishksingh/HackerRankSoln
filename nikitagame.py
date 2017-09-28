#!usr/bin/env

def partitionScore(a,left,right):
    if right<=left:
        return 0
    else:
        total=sum(a[left:right+1])
        s=0
        pivot=-1
        for i in range(left,right+1):
            s+=a[i]
            if s==total-s:
                pivot=i
                break
        #print(a[left:right+1],'l',left,'r',right,'p',pivot)        
        if left<=pivot<right:
            
            return 1+max([partitionScore(a,left,i),partitionScore(a,i+1,right)])
        else:
            return 0
t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    arr=list(map(int,input().split()))
    print(partitionScore(arr,0,len(arr)-1))        
