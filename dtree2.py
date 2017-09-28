#!usr/bin/env python3

#Diameter of a tree

edges=[]
visited=[]

mx=0
                
def dfs(v,l):
        global edges
        global visited
        level=l
        global mx
        
        
        visited[v]=1
        level=level+1
        print(v,mx,level)
        if level>mx:
                mx=level
        for x,y in edges:
                if x==v and visited[y]==0:
                        dfs(y,level)
                                
def main():
        global edges
        global visited
        global mx
        
        t=int(input())  #test cases
        for i in range(t):
                n=int(input())  #number of nodes
                #Getting edges
                
                for j in range(1,n):
                        s=input().split(' ')
                        u,v=int(s[0]),int(s[1])
                        edges.append((u,v))
                visited.append(0)        
                for j in range(1,n+1):
                        visited.append(0)
                visited[edges[0][0]]=1
                v=edges[0][0]
                depth_lst=[]
                for x,y in edges:
                        if x==v and visited[y]==0:
                                mx=0
                                
                                dfs(y,0)
                                depth_lst.append(mx)
                
                m=0
                n=0
                for y in depth_lst:
                        if m<=y:
                                n=m
                                m=y
                diameter=m+n
                
                print(diameter)                         
                visited=[]
                edges=[]                 
main();                                
