#!usr/bin/env python3
prime=[]

def SieveOfEratosthenes(n):
     
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    global prime = [True for i in range(n+1)]
    p=2
    while(p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p+=1
     
SieveOfEratosthenes(8191)#Prepare the Seive

q=int(input().strip())
MAX=999999
for _ in range(q):
    n=int(input().strip())
    arr=list(map(int,input().split(' ')))
    limit=dict()
    for i in arr:
        if i not in limit:
            limit[i]=arr.count(i)
    
    arr=list(set(arr))
    
    s={i:0 for i in range(8192)} #possible xor sums are in [0,8191]
    
    s[0]=0
    
    track=[[0 for i in range(len(arr))] for j in range(len(s))]
    
    for j in range(len(arr)):
        
        track[0][j]=limit[arr[j]]    
    
    #Coin-Change problem with limited number of coins    
    for j in range(1,8192):
        s[j]=MAX
        for i in range(len(arr)):
            if (arr[i]<=j and s[j-arr[i]]<MAX) and track[j-arr[i]][i]>0:
                if s[j]>s[j-arr[i]]:
                    s[j]=s[j-arr[i]]+1
                    track[j][i]=track[j-arr[i]][i]-1
                else:
                    track[j][i]=track[j-arr[i]][i]
            elif arr[i]>j:
                track[j][i]=track[0][i]            
    #print(limit)
    #print(s)               
    
    counter=0
    for j in s:
        if not s[j]<MAX and prime[s[j]]:
            counter=(counter+1)%(10**9+7)
    
    print(counter        
