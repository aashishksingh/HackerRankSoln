m,n=tuple(map(int,input().split()))
dp=[]
def minsquares(i,j):
    
    if i==j:
        return 1
    if dp[i][j]:
        return dp[i][j]
    minhorizontal=9999
    minvertical=9999
    for length in range(1,i//2+1):
        minhorizontal=min(minhorizontal,minsquares(length,j)+minsquares(i-length,j))
                    
    for width in range(1,j//2+1):
        minvertical=min(minvertical,minsquares(i,width)+minsquares(i,j-width))
        
        
    dp[i][j]=min(minhorizontal,minvertical)
    return dp[i][j]
    
dp=[[0 for i in range(n+1)]for j in range(m+1)]
print(minsquares(m,n))    
                        
