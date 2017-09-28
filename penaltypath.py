import heapq
n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
    
adj=dict()
adj={i:dict() for i in range(n+1)}
for a1 in range(m):
    x,y,r = input().strip().split(' ')
    x,y,r = [int(x),int(y),int(r)]
    if y not in adj[x]:
        adj[x][y]=r
    elif y in adj[x]:
        if r<adj[x][y]:
            adj[x][y]=r
    if x not in adj[y]:
        adj[y][x]=r
    elif x in adj[y]:
        if r<adj[y][x]:
            adj[y][x]=r
        
a,b=tuple(map(int,input().split()))

def BFS(u):
    que=[]
    visited=[-1]*(n+1)
    
    que.append(u)
    visited[u]=0
    while que:
        v=que.pop(0)
        for w in adj[v]:
            visited[w]=visited[v]+1
            que.append(w)
    return visited


def djisktra(s):
    flag=[0]*(n+1)
    distance=[99999]*(n+1)
    flag[s]=1
    distance[s]=0
    for w in adj[s]:
        distance[w]=adj[s][w]
    
    iteration=0
    currentNode=s
    
    while iteration<n-1:
        mini=99999
        target=0
        
        for w in range(1,n+1):
            if distance[w]<mini and flag[w]==0:
                mini=distance[w]
                target=w
        
        flag[target]=1
        #print(target)
        
        for w in adj[target]:
            if flag[w]==0 and distance[w]>distance[target] | adj[target][w]:
                
                distance[w]=distance[target] | adj[target][w]
        iteration+=1        
    
    return distance

#print(adj)

dist=djisktra(a)
#print(dist)

if dist[b]==9999:
    print(-1)
else:
    print(dist[b])

