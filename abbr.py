#!usr/bin/env python3

def wayExists(a,i,b,j):
    if i<0 and not j<0:
        return False
    elif j<0 and a[:i+1].lower()==a[:i+1]:
        return True
    elif i<0 and j<0:
        return True
    elif 65<=ord(a[i])<=90 and a[i]==b[j]:
        return wayExists(a,i-1,b,j-1)
    elif 65<=ord(a[i])<=90 and not a[i]==b[j]:
        return False
    elif a[i]==b[j].lower():
        return wayExists(a,i-1,b,j-1) or wayExists(a,i-1,b,j)
    elif not a[i]==b[j].lower():
        return wayExists(a,i-1,b,j)

q=int(input().strip())
for _ in range(q):
    a=input().strip()
    b=input().strip()
    if wayExists(a,len(a)-1,b,len(b)-1):
        print('YES')
    else:
        print('NO')
