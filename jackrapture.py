n,e=tuple(map(int,input().split()))
adj={i:{j:99999 for j in range(n+1)} for i in range(n+1)}
adjSet={i:[] for i in range(n+1)}
for _ in range(e):
    u,v,c=tuple(map(int,input().split()))
    adj[u][v]=c
    adj[v][u]=c
    adjSet[u].append(v)
    adjSet[v].append(u)
    
flag=[0]*(n+1)
distance=[99999]*(n+1)
flag[1]=1
distance[1]=0
for w in adj[1]:
    distance[w]=adj[1][w]
    
iteration=0


while iteration<n-1:
    mini=99999
    target=0
        
    for w in range(1,n+1):
        if distance[w]<mini and flag[w]==0:
            mini=distance[w]
            target=w
    #print(target)    
    flag[target]=1
    #print(target)
        
    for w in adjSet[target]:
        if flag[w]==0:
            distance[w]=max(distance[target],adj[target][w])
    iteration+=1        
    
if distance[n]<99999:
    print(distance[n])
else:
    print('NO PATH EXISTS')
