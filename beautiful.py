#!usr/bin/env python3

def main():
        s=str(input().strip())
        if(s[0]=='0'):
                print('NO')
                return
        
        j=1
        n=len(s)
        while j<n/2:
                ini=int(s[:j])
                k=0
                temp=1
                while(k<=n-j):
                        
                        print('k,j',k,j)
                        num=int(s[k:k+j])
                        if(len(str(num+1))==len(str(num))+1):
                                print('hi')
                                temp=j
                                j=j+1
                        k=k+temp
                        temp=j
                        print('k,n',k,n-j)
                        print(num)
                j=j+1
main()                                        
