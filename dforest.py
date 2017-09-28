#!usr/bin/env python3

#Diameter of a tree

edges=[]


mx=0
                
def dfs(v,l):
        global edges
        
        level=l
        global mx
        level=level+1
        #print(v,mx,level)
        if level>mx:
                mx=level
        for x,y in edges:
                if x==v:
                        dfs(y,level)
                                
def main():
        global edges
        global mx
        
        t=int(input())  #test cases
        for i in range(t):
                n=int(input())  #number of nodes
                #Getting edges
                
                for j in range(1,n):
                        s=input().split(' ')
                        u,v=int(s[0]),int(s[1])
                        edges.append((u,v))
                
                roots=[]
                diams=[]
                final=[]
                #Removing each node one by one
                for i in range(1,n+1):
                        if not i==1:
                                roots.append(1)
                        for j,k in edges:
                                if j==i:
                                        roots.append(k)
                        #print('roots',roots)
                        
                        for j in roots:
                                depth_lst=[]
                                for x,t in edges:
                                        if x==j and not t==i:
                                                #print('at j=',j,'t=',t)
                                                mx=0
                                                dfs(t,0)
                                                depth_lst.append(mx)
                                #print('At j=',j,'dlst=',depth_lst)                
                                m=0
                                n=0
                                for y in depth_lst:
                                        if m<=y:
                                                n=m
                                                m=y
                                diameter=m+n
                                #print('at i=',i,' and root=',j,'d=',diameter)
                                diams.append(diameter)
                                m=0
                        
                        for y in diams:
                                if m<=y:
                                        m=y                                           
                        final.append(m)                                                                                    
                        roots=[]
                        diams=[] 
                print(final)        
                edges=[]                 
main();                                
