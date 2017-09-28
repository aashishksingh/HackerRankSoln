t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    chocos=list(map(int,input().split()))
    mini=min(chocos)
    case=mini
    case_cntr=0
    min_steps=999999999
    while case_cntr<=4:
        
        steps=0
        for i in range(n):
            d=chocos[i]-case
            a=d//5
            b=(d%5)//2
            c=((d%5)%2)//1
            steps+=(a+b+c)
        if steps<min_steps:
            min_steps=steps
        case-=1
        case_cntr+=1    
    print(min_steps)        
