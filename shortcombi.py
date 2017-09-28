a=input().strip()
b=input().strip()
lena=len(a)
lenb=len(b)
result=[]
c=[[0 for i in range(lenb)] for j in range(lena)]
def LCS(a,b,i,j):
    global c
    if i<0 or j<0:
        return 0 
    else:
        
        if a[i]==b[j]:
            #result.append(a[i])
            c[i][j]=1+LCS(a,b,i-1,j-1)
        else:
            #if j>i:
            #result.append(b[j]);result.append(a[i])
                
            c[i][j]=1+min(LCS(a,b,i-1,j),LCS(a,b,i,j-1))
        
        return c[i][j]
LCS(a,b,lena-1,lenb-1)
lcs=[]
i=lena-1
j=lenb-1
while i>0 and j>0:
    if a[i]==b[j]:
        lcs.append(a[i])
        i-=1
        j-=1
    else:
        if c[i-1][j]>c[i][j-1]:
            lcs.append(b[j-1])
            j-=1
        else:
            lcs.append(a[i-1])
            i-=1
while i>0:
    lcs.append(a[i])
    i-=1
while j>0:
    lcs.append(b[j])
    j-=1

print("".join(result[::-1]))                            
        
