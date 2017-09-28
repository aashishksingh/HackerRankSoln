#!usr/bin/env python3

def solve(n,arr):
    if n<2:
        return 'yes'
    flag=0
    #Already sorted
    #print(arr)
    for i in range(1,n):
        if(arr[i]-arr[i-1]<0):
            flag=1
    if not flag:
        return 'yes'
    #swap pair
    #print('swap',arr)
    lst=[]
    for i in range(1,n):
        if(arr[i]-arr[i-1]<0):
            t=[]
            t.append(i-1)
            t.append(i)
            lst.append(t)
            del t
    if n>2:
        if len(lst)==2:
            arr[lst[0][0]],arr[lst[1][1]]=arr[lst[1][1]],arr[lst[0][0]]
        flag=0
        for i in range(1,n):
            if(arr[i]-arr[i-1]<0):
                flag=1
        if not flag:
            return 'yes'+'\n'+'swap '+str(lst[0][0]+1)+' '+str(lst[1][1]+1)
        
    if n==2:
        return 'yes'+'\n'+'swap '+str(lst[0][0]+1)+' '+str(lst[0][1]+1)
    del lst
    #reverse a segment
    #print('reverse',arr)
    flag=0
    lst=[]
    cntr=0
    for i in range(1,n):
        if arr[i]-arr[i-1]<0 and not flag:
            t=[]
            #t.append(i-1)
            #t.append(i)
            lst.append(i-1)
            #del t
            flag=1
            cntr+=1
        elif arr[i]-arr[i-1]>=0 and flag:
            t=[]
            #t.append(i-1)
            lst.append(i-1)
            flag=0
    #print('list',lst)        
    if cntr==1:
        if n>2:
            if(lst[1]-lst[0]==1):
                arr[lst[1]],arr[lst[0]]=arr[lst[0]],arr[lst[1]]
                flag=0
                for i in range(1,n):
                    if(arr[i]-arr[i-1]<0):
                        flag=1
                if not flag:
                    return 'yes'+'\n'+'swap '+str(lst[0]+1)+' '+str(lst[1]+1)
                else:
                    arr[lst[1]],arr[lst[0]]=arr[lst[0]],arr[lst[1]]
            flag1='A'
            if lst[0]-1>=0:
                if arr[lst[1]]>arr[lst[0]-1]:
                    flag1='L'
                else:
                    flag1='N'
            else:
                flag1='L'
            flag2='A'    
            if lst[1]+1<n:
                if arr[lst[0]]<arr[lst[1]+1]:
                    flag2='R'
                else:
                    flag2='N'
            else:
                flag2='R'
            if flag1=='L' and flag2=='R':    
                return 'yes'+'\n'+'reverse '+str(lst[0]+1)+' '+str(lst[1]+1)
    #Nothing can be done
    
    return 'no'
            
    

n=int(input().strip())
arr=list(map(int,input().split()))
result=solve(n,arr)
print("".join(result))
