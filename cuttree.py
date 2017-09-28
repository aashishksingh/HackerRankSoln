#!usr/bin/env python3

n=int(input().strip())
a=list(map(int,input().split()))
a.insert(0,0)

visit=[0]*(n+1)
st=[1]
q=[]
edges=[]
adj=dict()
nodes=set()
def getnodelist(v):
    q.insert(0,v)
    visit[v]=1
    lst=set()
    while len(q):
        t=q[0]
        
        lst.add(t)
        del q[0]
        l=len(q)
        #k=0
        if t in adj:
            q.extend(adj[t])
            lst.update(adj[t])
    return lst             

edges=[]
adj=dict()
nodes=set()

for _ in range(n-1):
    u,v=input().split()
    u,v=int(u),int(v)
    edges.append((u,v))
    if(len(nodes)==0):
        t=[]
        t.append(v)
        adj[u]=t
        nodes.add(u)
        nodes.add(v)
    elif u in nodes:
        if u in adj:
            adj[u].append(v)
        else:
            t=[]
            t.append(v)
            adj[u]=t
        nodes.add(u)
        nodes.add(v)
    elif v in nodes:
        if v in adj:
            adj[v].append(u)
        else:
            t=[]
            t.append(u)
            adj[v]=t
        nodes.add(u)
        nodes.add(v)

def parent(i,j):
    if i in adj:
        if j in adj[i]:
            return i
    return j
#del nodes

def sumlist(lst):
    s=0
    for i in lst:
        s+=a[i]
    return s
#print(a)

root_always=1
mini=999999
total=sumlist([1,2,3,4,5,6])
print(total)
print(adj)
for i,j in edges:
    k=parent(i,j)
    if(k==i):
        lst=getnodelist(j)
        t1=sumlist(lst)
        t2=total-t1
        if abs(t1-t2)<=mini:
            mini=abs(t1-t2)
    else:
        lst=getnodelist(i)
        t1=sumlist(lst)
        t2=total-t1
        if abs(t1-t2)<=mini:
            mini=abs(t1-t2)
print(mini)        

