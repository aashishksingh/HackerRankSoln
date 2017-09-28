q=int(input().strip())
for _ in range(q): 
    m,n=list(map(int,input().split())) 
    y=list(map(int,input().split())) 
    x=list(map(int,input().split()))
    cost=0 
    n_vert=1 
    n_hori=1 
    flag='' 
    for i in range(m+n-2): 
        max1=0 
        max2=0 
        if y: 
            max1=max(y) #Col max 
        if x: 
            max2=max(x) #Row max 
        if max1>max2: 
            cost=(cost+(n_hori)*max1)%(10**9+7) 
            if max1 in set(y): 
                del y[y.index(max1)] 
            n_vert+=1 
        elif max2>=max1: 
            cost=(cost+(n_vert)*max2)%(10**9+7) 
            if max2 in set(x): 
                del x[x.index(max2)] 
            n_hori+=1 
     
    print(cost)
