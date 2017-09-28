fo=open("B-small-attempt1.in",'r')
go=open("output4.txt",'w')
t=int(fo.readline())
for _ in range(t):
    e,n=tuple(map(int,fo.readline().split()))
    s=list(map(int,fo.readline().split()))
    hnr=0
    
    i=0
    j=n-1
    s.sort()
    while(i<=j):
        
        if(s[i]<e):
            e-=s[i]
            hnr+=1
            i+=1
            
        elif(hnr>=1 and i!=j):
            hnr-=1
            j-=1
            e+=s[j]
            
        else:
            break
            
    go.write("Case #"+str(_+1)+": "+str(hnr)+"\n")            
