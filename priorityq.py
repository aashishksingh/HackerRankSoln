from heapq import heappush, heappop, heapify


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
adj={i:[] for i in range(n+1)}

for a1 in range(m):
    x,y,r = input().strip().split(' ')
    x,y,r = [int(x),int(y),int(r)]
    adj[x].append((y,r))
    adj[y].append((x,r))
    
a,b=tuple(map(int,input().split()))

#print(adj)
paths=[[False for i in range(1024)] for j in range(n+1)]
bfs=[]
que=[]
bfs.append(a)
que.append(0)

while bfs:
    u=bfs.pop()
    c=que.pop()
    
    for w in adj[u]:
        
        if not paths[w[0]][c | w[1]]:
            paths[w[0]][c | w[1]]=True
            bfs.append(w[0])
            que.append(c | w[1])

found=False            
for i in range(1024):
    if paths[b][i]:
        print(i)
        found=True
        break
if not found:
    print(-1)
