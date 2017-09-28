t=int(input().strip())
for _ in range(t):
    n,g=tuple(map(int,input().split()))
    time=list(map(int,input().split()))
    status=False
    for i in time:
        if i>g:
            print('NO')
            status=True
            break
    if status:
        continue
    
    #Wrong !! since there is no order ! s=[0]*n  #Minimum time taken by 'i' robbers
    time.sort()
    
    
    small=0
    big=n-1
    timeTaken=0
    smallTime=0
    while small<big:
        if smallTime<=time[big]:
            smallTime+=time[small]
            small+=1
            
        elif smallTime>time[big]:
            timeTaken+=time[big]
            big-=1
            smallTime=0
    
    print(timeTaken)
