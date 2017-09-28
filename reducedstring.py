#!usr/bin/env python3

def main():
    s=str(input().strip())
    nochange=False
    temp=list(s)
    while not (nochange):
        l=len(temp)
        for i in range(l-1):
            if(i+1<len(temp)) and (temp[i]==temp[i+1]):
                temp=[temp[j] for j in range(l) if not (j==i) and not (j==i+1)]
                #print(str("".join(temp)))
                break
        i=i+1
        if(len(temp)==l):
           	nochange=True
    if(len(temp)==0):
    	print("Empty String")
    else:	        
    	print(str("".join(temp)))
main()            
