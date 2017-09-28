t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    s=[False]*(n+1)
    #s[0]=False
    for i in range(1,n+1):
        
        if i-2>=0 and s[i-2]==False:
            s[i]=True
        elif i-3>=0 and s[i-3]==False:
            s[i]=True
        elif i-5>=0 and s[i-5]==False:
            s[i]=True
    
    if s[n]:
        print("First")
    else:
        print("Second")
    
        
