n=int(input().strip())
a=list(map(int,input().split()))
k=int(input().strip())
s=[[1,[a[i]]] for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[j]<a[i] and s[i][0]<s[j][0]+1:
            s[i][0]=s[j][0]+1
            s[i][1]=s[j][1]+s[i][1]
            
minsum=9999
for k in range(n):
    
    if s[i][0]==k:
        
        minsum=sum(s[i][1]) if sum(s[i][1])<minsum else minsum
        
print(minsum)
