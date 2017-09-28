'''
Solution Code:
Strategy: Sorting + Hashing
Input Format: 
    First Line: target sum, an integer
    Second Line: space seperated list of integers: array
Output Format:
    space seperated triplets in 'array', having sum 'target sum'    
    In case of multiple triplets, the first one found is printed.
'''


class TripletTarget():
    def __init__(self,targetSum,array):
        self.targetSum=targetSum
        self.array=array
        self.array.sort() #Python in-built sort method [Uses Timsort algo: O(nlogn)]
        self.arrayLength=len(array)

    '''
        Function to return a pair of numbers with sum=target
        uses hashing, ASSUMPTION: RANGE OF ELEMENTS OF THE ARRAY IS KNOWN[NEGATIVE INTEGERS ARE ALSO HANDLED]
        This case: assumed maximum value of array[i] is 10^5
    '''
    @staticmethod
    
    def pairIsThere(array,hashMap,targetSum):
        
        
        for element in (array):  #Avoiding useless iterations for duplicate elements in the array
            
            pairElement = targetSum - element   
            if pairElement>=0 and hashMap[pairElement]: #Found a pair
                return (element,pairElement)
            hashMap[element]=1
        return False #No possible pair        
                
            
    '''
    Preprocessing: Building HashMap
    handling negative elements seperately, making them postive
    '''
    @staticmethod
    def preprocessing(array,targetSum):
        mostNegative=0
        for index in range(len(array)):
            
            if array[index]<0 and array[index]<mostNegative:
                mostNegative=array[index]

        targetSum -= 3*mostNegative #targetSum also gets scaled up accordingly
        
        for index in range(len(array)):
            
            array[index] -= mostNegative                    
        
        return array,targetSum,mostNegative
    
    '''
        Utility function to get results through other functions
    '''
    #@staticmethod        
    def mainFunction(self,targetSum,array):    

        newArray=[i for i in array] #Creating duplicate
        target=targetSum
        newArray,newTarget,adjustment = TripletTarget.preprocessing(newArray,target) #so that HashMap has all positive elements

        hashMap=[0]*10**5
        resultTriplet=[] #Later to be used by the testcases
        for firstElement in range(0,len(array)-2):
            
            newTargetSumForPair = newTarget - newArray[firstElement]
            pairObtained = TripletTarget.pairIsThere(newArray[firstElement+1:],hashMap,newTargetSumForPair)
            
            if pairObtained :
                resultTriplet.append(array[firstElement])
                resultTriplet.append(pairObtained[0]+adjustment)
                resultTriplet.append(pairObtained[1]+adjustment) 
                #print (self.array[firstElement],pairObtained[0]+adjustment,pairObtained[1]+adjustment)
                break
                

        #Uncomment if Auxilliary memory is not a constraint
        '''
        hashMap=[0 for value in range(-10**5,10**5)] #Preprocessing not done assuming bigger auxilliary memory, hence hashMap for both -ve and +ve
                
        for firstElement in range(0,arrayLength-2):
            
            newTargetSumForPair = targetSum - array[firstElement]
            pairObtained = pairIsThere(array[firstElement+1:],hashMap,newTargetSumForPair)
            
            if pairObtained :
                #print (newArray[firstElement],pairObtained[0],pairObtained[1])
                print (array[firstElement],pairObtained[0],pairObtained[1])
                break
        '''
        return (resultTriplet)

    
targetSum=int(input().strip())  #User input target sum 
array=list(map(int,input().split()))    #User input array of integers
    
ttObject=TripletTarget(targetSum,array)
resultTriplet=list(ttObject.mainFunction(targetSum,array))
print(resultTriplet)
                          
