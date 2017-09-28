m,n=tuple(map(int,input().split()))

total=0
multiplier=1

i=n
while(i>0):
    total+=m//multiplier-2**(i-1)
    multiplier*=2
    i-=1
print(total)    
