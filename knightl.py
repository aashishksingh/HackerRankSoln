#!usr/bin/env python3

cntr=0
n=int(input().strip())
tree=dict()

def buildTree(x,y,a,b):
    
    global cntr
    a_set=list()
    global n
    global tree
    
    if x-a>0:
        if y-b>0:
            a_set.append((x-a,y-b))
        if y+b<n:
            a_set.append((x-a,y+b))
    if x+a<n:
        if y-b>0:   
            a_set.append((x+a,y-b))
        if y+b<n:
            a_set.append((x+a,y+b))   
    if x-b>0:
        if y-a>0:
            a_set.append((x-b,y-a))
        if y+a<n:
            a_set.append((x-b,y+a))
    if x+b<n:
        if y-a>0:
            a_set.append((x+b,y-a))
        if y+a<n:
            a_set.append((x+b,y+a))
    
    s=set(a_set)
    lst=list(s)
    print(lst)
    tree[(x,y)]=lst
    if(len(lst)<1):
        return
    else:
        for i,j in lst:
            buildTree(i,j,a,b)        
            

buildTree(2,2,1,1)
print(tree)                      
                
