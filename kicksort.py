fo=open("A-large.in",'r')
go=open("output3.txt",'w')
status=set()
def kicksort(arr):
    global status
    n=len(arr)
    if n<=1:
        return arr
    pivot=arr[(n-1)//2]
    B=[]
    C=[]
    for i in range(n):
        if i==(n-1)//2:
            continue
        if arr[i]<=pivot:
            B.append(arr[i])
        else:
            C.append(arr[i])
    if len(B)==n-1 or len(C)==n-1:
        status.add('True')
    else:
        status.add('False')
                    
    return kicksort(B)+[pivot]+kicksort(C)                     
    
t=int(fo.readline())
for _ in range(t):
    n=int(fo.readline())
    arr=list(map(int,fo.readline().split()))
    status=set()
    kicksort(arr)
    if 'False' in status:
        go.write("Case #"+str(_+1)+": NO"+"\n")
    else:
        go.write("Case #"+str(_+1)+": YES"+"\n")
    
    
