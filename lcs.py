a=input().strip()
b=input().strip()
l=len(a)
dp=[[0]*l]*l

for i in range(l):
    for j in range(l):
        if i==0 or j==0:
            dp[i][j]=0
        
        elif a[i]==b[j]:
            dp[i][j]=1+dp[i-1][j-1]
        
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])


print(dp[l-1][l-1])                    
