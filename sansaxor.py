t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    arr=list(map(int,input().split()))
    residues=[]
    for i in range(n):
        total= 2 if 0<i<n-1 else 1
        left=i if i>=0 else 0
        right=n-1-(i) if n-1>=i else 0
        total+=left+right
        if total%2:
            residues.append(arr[i])
    #print(residues)
    if n%2:
        result=0
        for i in range(0,n,2):
            result=result^arr[i]
        print(result)
    else:
        print(0)
        

