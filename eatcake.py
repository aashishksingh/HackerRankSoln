fo=open("D-large.in",'r')
go=open("output2.txt",'w')
t=int(fo.readline())
for _ in range(t):
    n=int(fo.readline())
    cakes=[]
    i=1
    
    while(i**2<=n):
        cakes.append(i**2)
        i+=1
        
    s=[100000]*(n+1)
    s[0]=0 #no length i.e. one way
    
        
    for i in range(1,n+1):
        for j in cakes:
            if j<=i:
                temp=1+s[i-j]
                s[i]=min(s[i],temp)
    #print(cakes)
                    
    go.write("Case #"+str(_+1)+": "+str(s[n])+"\n")            
