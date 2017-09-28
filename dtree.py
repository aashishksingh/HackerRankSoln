#!usr/bin/env python3

#Diameter of a tree [ONLY APPROXIMATION IS OBTAINED BY BFS, for exact diameter check dtree2.py]

def main():
        t=int(input())  #test cases
        for i in range(t):
                n=int(input())  #number of nodes
                edges=[]
                q=[]
                level=0
                bfs_list=[]
                visited=[]
                #Getting edges
                for j in range(1,n):
                        s=input().split(' ')
                        u,v=int(s[0]),int(s[1])
                        edges.append((u,v))
                visited.append(0)        
                for j in range(1,n+1):
                        visited.append(0)
                        
                        
                q.insert(0,edges[0][0]) #enqued
                visited[edges[0][0]]=1
                bfs_list.insert(level,[q[0]])
                level=level+1
                print(visited)
                while not len(q)==0:
                        v=q[0]
                        visited[v]=2    #dequed
                        print('level',level,len(q))
                        print(q)
                        
                        del q[0]
                        level=level+1
                        
                        
                        temp=[]
                        t=len(q)
                        for x,y in edges:
                                if(x==v) and (visited[y]==0):
                                        q.insert(t,y)
                                        visited[y]=1
                                        t=t+1
                                        temp.append(y)
                        if len(temp)>0:                                                  
                                bfs_list.insert(level,temp)
                        
                        temp=[]
                print(bfs_list)
                a=0;b=0
                
                for lst in bfs_list:
                        if len(lst)==2        

main();                                
