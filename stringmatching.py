s=input().strip()
a=list(map(str,input().split()))

l=len(a)
a=set(a)

count=0

def compute(a,s,i,j):
    
    global count
    
    if i>j:
        return 0
    
    else:
        current=0
        b=set(c for c in s[i:j+1])
        #print(b)
        if a.issubset(b):
            current=1
            
        count= current + compute(a,s,i+1,j) + compute(a,s,i,j-1)
        
        return count

print(compute(a,s,0,len(s)-1))        
            
        
        
