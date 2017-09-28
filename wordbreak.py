words=[]
flag=False
#Backtracking
def compute(string,wordset):
    global flag
    global words
    #Destination reached
    if len(string)==0:
        
        for w in words:
            print(w,end=' ')
        print()
        flag=True    
        return True
        
    if len(string)==1 and string in wordset:
        words.append(string)
        for w in words:
            print(w,end=' ')
        print()
        flag=True    
        return True
        
    for i in range(1,len(string)+1):
        word=string[:i]
        if word in wordset:
            #print(word,'yes')
            words.append(word)
            if compute(string[i:],wordset):
                words.pop()
            else:
                words.pop() #backtrack
    #print(words)            
    return False            

T=int(input().strip())
for _ in range(T):
    n=int(input().strip())
    wordset=set(map(str,input().split(' ')))
    print(wordset)
    string=input().strip()
    words=[]
    flag=False
    #print()
    compute(string,wordset)
    
    if not flag:    
        print('Empty')
    
