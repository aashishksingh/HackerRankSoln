#!usr/bin/env python3
import re

len_s=int(input().strip())
s=str(input().strip())


def main():
    
    mx=0
    uniq=set(s)
    lst=list(uniq)
    #print(lst)
    mx_lst=[]
    for i in range(len(lst)):
        
        for j in range(i+1,len(lst)):
            temp=s
            flag=0
            
            #print('i',i,'j',j)
            for k in temp:
                if not (k==lst[j]) and not (k==lst[i]):
                    temp=re.sub(k,"",temp)
                    #print('j',lst[j],temp)
                       
            #print(temp)
            l=len(temp)
            if(l%2==0):
                a=temp[0]
                b=temp[1]
                for k in range(0,l-1):
                    if(a==temp[k])and(b==temp[k+1]):
                        continue
                    else:
                        flag=1
            else:
                for i in range(0,l//2):
                    if(temp[i]==temp[l-(i+1)]) and not(temp[i]==temp[i+1]):
                        continue
                    else:
                        flag=1
                        break
            if(flag==0):
                mx_lst.append(l)
    
    print(max(mx_lst))                   
main()                

