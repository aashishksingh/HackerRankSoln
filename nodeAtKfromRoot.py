n,m=list(map(int,input().split()))
adj={i:[] for i in range(n+1)}

#Building the tree
for edge in range(m):
    u,v=list(map(int,input().split()))
    if v not in adj[u]:
        adj[u].append(v)
    if u not in adj[v]:
        adj[v].append(u)
                                  


def BFS(u):
    global adj
    que=[]*(n)
    level=[-1]*(n+1)
    
    que.append(u)
    level[u]=0
    
    while que:
        v=que.pop(0)
        if v in adj:
            for w in adj[v]:
                if level[w]==-1:
                    que.append(w)
                    level[w]=level[v]+1
    
    return level
    
def findLevel():
    level=BFS(1)
    
    for l in range(n+1):
        if level[l]==2:
            print(l)

findLevel()    
