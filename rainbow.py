t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    a=list(map(int,input().split()))
    
    i=0
    j=n-1
    t=1
    while(i<=j):
        if a[i]==a[j] and (a[i]==t or a[i]==t+1) and a[i]<=7:
            if a[i]==t+1:
                t+=1
            i+=1
            j-=1
        else:
            break
            
    if i>j:
        print('YES')
    else:
        print('NO')                      
