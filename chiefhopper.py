n=int(input().strip())
a=list(map(int,input().split()))
start=a[0]
energy=start
for i in range(n):
    if a[i]>energy:
        energy-=(a[i]-energy)
    else:
        energy+=(energy-a[i])
    
    if energy<0:
        start+=1
        energy=0
        
print(start)        
