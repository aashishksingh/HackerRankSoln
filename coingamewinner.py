n,x,y=tuple(map(int,input().split()))

dp=[False]*(n)
dp[1]=True
for i in range(2,n):
    if i-1>=0 and not dp[i-1]:
        dp[i]=True
    if i-x>=0 and not dp[i-x]:
        dp[i]=True
    if i-y>=0 and not dp[i-y]:
        dp[i]=True


if dp[n-1]:

    print("A")

else:
    
    print("B")            
