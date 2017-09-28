m,n=tuple(map(int,input().split()))
grid=[list(map(int,input().split())) for i in range(m)]

s=[[0 for j in range(n)] for i in range(m)]

#Bottom-up DP
for i in range(n):
    if grid[0][i]:
        break
    s[0][i]=1
    
for i in range(m):
    if grid[i][0]:
        break
    s[i][0]=1
    
for i in range(1,m):
    for j in range(1,n):
        if not grid[i][j]:
            s[i][j]=s[i-1][j]+s[i][j-1]
            
print(s[m-1][n-1])                    
