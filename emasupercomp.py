#!usr/bin/env python3

arr=list(map(int,input().split()))
n,m=arr[0],arr[1]
del arr
size=[]
cur=1
grid=[]
prevSize=0
for i in range(n):
    lst=list(input().strip())
    grid.append(lst)

#print(grid)
def neighbours(i,j,cur):
    global n
    global m
    a=set()
    limit=(cur)//2
    for k in range(1,limit+1):
        if(i-k>=0) and grid[i-k][j]=='G':
            a.add((i-k,j))
        if(i+k<n) and grid[i+k][j]=='G':
            a.add((i+k,j))
        if(j-k>=0) and grid[i][j-k]=='G':
            a.add((i,j-k))
        if(j+k<m) and grid[i][j+k]=='G':
            a.add((i,j+k))
    return a

lookUp=dict()
for i in range(n):
    for j in range(m):
        if grid[i][j]=='G':
            if not cur in lookUp:
                t=[]
                t.append((i,j))
                lookUp[cur]=t
            else:
                lookUp[cur].append((i,j))
#print(lookUp)
t=len(lookUp)
while(True):

    size.append(cur)
    prevSize=len(lookUp)
    
    for i in lookUp:
        if i==cur:
            final=set()
            #print('final',final)
            for j,k in lookUp[i]:
                #print('j,k',j,k)
                a=neighbours(j,k,cur+2)
                #print('j,k',j,k,'a',a,'len',len(a),((cur+2)//2)*4)
                if(len(a)==4*((cur+2)//2)):
                    #print(j,k)
                    final.add((j,k))
                    #print('final',final)
    cur+=2
    if (len(final)):
        lookUp[cur]=list(final)
        t=t+1
    if not t>prevSize:    
        break
print(lookUp)

def distance(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

cntr=0
done=[]
for i in size[::-1]:
    for j in range(len(lookUp[i])):
        for k in range(j,len(lookUp[i])):
            dist=distance(lookUp[i][j],lookUp[i][k])
            if dist>=i:
                done.append(lookUp[i][j])
                done.append(lookUp[i][k])
    if len(done)>1:
        print((2*i-1)**2)
        break
    else:
        if i>1:
            leftouts=set(lookUp[i-2])-set(lookUp[i])
            for j in leftouts()
        break
        
        
                
                
                
    
