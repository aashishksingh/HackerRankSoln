n=int(input().strip())
a=list(map(int,input().split()))

s=[1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if abs(a[j]-a[i])<=1:
            s[i]=s[j]+1 if s[i]<s[j]+1 else s[i]

print(max(s))            
        
