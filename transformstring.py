a=input().strip()
b=input().strip()
chars=set([c for c in a])
if chars!=set([c for c in b]):
    print(-1)
        
else:

    flag=False
    for c in chars:
    if a.count(c)<b.count(c):
        print(-1)
        flag=True
        break
    
    if not flag:
        
            

        
