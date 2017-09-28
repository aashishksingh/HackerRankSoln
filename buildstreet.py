n=int(input().strip())

s=[[0 for i in range(2)]for j in range(n+1)]
s[1][0]=1
s[1][1]=2
for i in range(2,n+1):
    s[i][0]=s[i-1][0]+s[i-1][1]
    s[i][1]=s[i-1][0]*2 + s[i-1][1]
    
print(s[n][0]+s[n][1])    
