t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    a=list(map(int,input().split()))
    hashmap=dict()
    for i in a:
        if i not in hashmap:
            hashmap[i]=1
        else:
            hashmap[i]+=1
            
    freqList=[]
    for i in hashmap:
        freqList.append([i,hashmap[i]])
    
    freqList.sort(reverse=True,key=lambda x: x[1])
    
    result=[]
    for i in freqList:
        result.extend([i[0]]*i[1])
    
    for i in result:
        print(i,end=' ')
    print()        
