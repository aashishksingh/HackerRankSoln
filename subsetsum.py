status=False
def found(array,target,current,n,partial=[]):
    global status    
    if sum(partial)>target:
        return False
    
    if sum(partial)==target:
        status=True
        return True
    
    for i in range(current,n):
        partial=partial+[array[i]]
        if found(array,target,i+1,n,partial):
           return True
        partial.pop()
        

n=int(input().strip())
array=list(map(int,input().split()))
target=int(input().strip())
found(array,target,0,n)
if status:
    print("TRUE")
else:
    print("FALSE")                        
