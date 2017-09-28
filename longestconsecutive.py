arr=list(map(int,input().split(' ')))

maximum=0
for i in arr:
    if i>maximum:
        maximum=i

presence={i:0 for i in range(-1,maximum+2)}

for i in arr:
    presence[i]=1+presence[i-1]+presence[i+1]


length=0    

for i in arr:
    
        if presence[i]>length:
            length=presence[i]
            
print(length)            
            
