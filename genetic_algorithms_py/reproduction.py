'''
Created on Nov 18, 2015

@authors: Scott Smith, Josh Teeter, Steven Gao, Irfan Lakha

'''
import random

        
def createRandomPool( poolSize, strLength):
    '''
    Creates a random pool of strings of binary digits for specified string length and pool size
    '''
  
    poolList = [ ]
    
  
    for i in range(0,poolSize):       #traverse all bit strings in list
        curString = ''                  #init next new string
        
        
        for j in range(0, strLength): #traverse all bits in a string
            
            randBit = random.randint(0,1)
    
            curString+= str(randBit)         #append random bit
    
        poolList.append(curString)         #random string complete, add to list


    return poolList 



def reproduce( objectiveFunction, PoolListIn, poolOutSize, targetBitStr):
    '''
    Inputs a list of bit strings (input pool) and uses the objective function (OF)
    to produce a new pool. The OF outputs a list of probabilities that the string should
    appear in the output pool (size can be chosen). The string is either chosen
    or not in its entirety 0 or multiple times, chosen by a weighted randomized selection 
    (ie. probability based choice).
    
    objectiveFunction must have parameters(List PoolListIn, String targetBitStr)  

    '''
    poolOut = [ ]

    poolInSize = len(PoolListIn)      #same size as OFResultList  (pool values correspond to OF results)
  
    print('pool size: '+str(poolInSize))
    #OF outputs a list of percentages corresponding to probabitlity that string should be chosen
    OFResultList = objectiveFunction(PoolListIn, targetBitStr) 
    
    print('')
    print('OF listlength: ')
    print( len(OFResultList) )
    print('OF list:')
    printList(OFResultList) 
    print('')

    #percentages are given as values between 0 and 1
    maxPercentage = poolInSize * 1      #total maximum percentage possible of OF output, %100 is 1

    #search for choice (weighted random selection - probability)
    for i in range(0, poolOutSize):
        
        
        found = False
        
        
        
        while not found:
        #choice may still lie between added percentages and max percent, produce a new choice if in this range
        # (ie. if probability is %99, this is the %1 that nothing is found)
        
            choice = random.uniform(0,maxPercentage)        #choose percentage between 0 and added values
            currentTotal = 0       #init/reset

         #search for where choice falls
            for j in range(0,poolInSize):

                if choice >= currentTotal and choice <= currentTotal + OFResultList[j]:
                
                    stringIndexChosen = j
                    found = True
                    break       #found, end search (current loop)

                currentTotal += OFResultList[j]      #add actual percentage values to create weight distribution

        
        #found, record and choose next string for output list
        print('string chosen: ' + PoolListIn[stringIndexChosen] + ', chose #: ' + str(stringIndexChosen+1) +', time:' +str(i+1)) 
        poolOut.append(PoolListIn[stringIndexChosen])


    return poolOut





def printList(list1):
    size = len(list1)

    for i in range(0, size):
        print(list1[i])
     

