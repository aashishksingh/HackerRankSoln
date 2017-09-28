#!usr/bin/env python3
n,k=list(map(int,input().split(' ')))
rq,cq=list(map(int,input().split(' ')))
rq,cq=[rq-1,cq-1]
obs=set()
for _ in range(k):
    robs,cobs=list(map(int,input().split(' ')))
    obs.add((robs-1,cobs-1))

#diagonals search(all 4)
def safe(i,j,n):
    if 0<=i<n and 0<=j<n:
        return True
    return False    

total=0
for k in range(1,n):
    if safe(rq+k,cq+k,n):
        if (rq+k,cq+k) in obs:
            break
        total+=1
    else:
        break    
        
for k in range(1,n):
    if safe(rq+k,cq-k,n):
        if (rq+k,cq-k) in obs:
            break
        total+=1
    else:
        break    
for k in range(1,n):
    if safe(rq-k,cq+k,n):
        if (rq-k,cq+k) in obs:
            break
        total+=1
    else:
        break    
        
for k in range(1,n):
    if safe(rq-k,cq-k,n):
        if (rq-k,cq-k) in obs:
            break
        total+=1        
    else:
        break    

#Other 4directions
for k in range(1,n):
    if safe(rq+k,cq,n):
        if (rq+k,cq) in obs:
            break
        total+=1        
    else:
        break    
        
for k in range(1,n):
    if safe(rq-k,cq,n):
        if (rq-k,cq) in obs:
            break
        total+=1        
    else:
        break

for k in range(1,n):
    if safe(rq,cq+k,n):
        if (rq,cq+k) in obs:
            break
        total+=1        
    else:
        break    
        
for k in range(1,n):
    if safe(rq,cq-k,n):
        if (rq,cq-k) in obs:
            break
        total+=1        
    else:
        break    

print(total)
