import sys
from collections import defaultdict
import heapq
n,e = list(map(int,input().split()))
graph=defaultdict(list)
heap=[]
weight=0
for _ in range(e):
    u,v,w = list(map(int,input().split()))
    graph[u].append((v,w))
    graph[v].append((u,w))
'''defaultdict(<type 'list'>, {1: [(2, 3), (3, 4)], 2: [(1, 3), (4, 6), (5, 2), (3, 5)], 3: [(1, 4), (2, 5), (5, 7)], 4: [(2, 6)], 5: [(2, 2), (3, 7)]})'''

startnode = int(input().strip())
mstset = [False]*(n)
heapq.heappush(heap,(0,1))
heapq.heapify(heap)
while heap:
    vertex  = heapq.heappop(heap)
    if mstset[vertex[1]-1] == False:
        mstset[vertex[1]-1] = True
        weight+=vertex[0]
        for v in graph[vertex[1]]:
            heapq.heappush(heap,(v[1],v[0]))
        '''[(3, 2), (4, 3)]
[(2, 5), (3, 1), (6, 4), (4, 3), (5, 3)]
[(2, 2), (3, 1), (6, 4), (5, 3), (4, 3), (7, 3)]
[(4, 1), (5, 2), (6, 4), (7, 3), (5, 3), (7, 5)]
[(6, 2), (7, 5), (7, 3)]
'''
print(weight)
