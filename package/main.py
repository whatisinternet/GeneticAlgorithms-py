'''
Created on Nov 22, 2015

@authors: Scott Smith, Josh Teeter, Steven Gao, Irfan Lakha
'''

from package import reproduction
from package import mutation
from package import objectiveFunction


def main():

    randomPoolSize = 20
    strLength = 10
    matingPoolSize = 20
    timesToReproduce = 10
    
    targetBitStr = '0000011111'

    randomPool = reproduction.createRandomPool(randomPoolSize, strLength)
    print("initial random pool:")
    printList(randomPool)
    print
    
    for i in range(0, timesToReproduce):

        matingPool = reproduction.reproduce(objectiveFunction.OFSimple, randomPool, matingPoolSize, targetBitStr)

        print('Pool after ' + str(i+1) + ' reproductions:')
        print('')
        printList(matingPool)
        print('')
        print('')


    return 0



def printList(list1):
    size = len(list1)

    for i in range(0, size):
        print(list1[i])
     

'run'
result = main()
