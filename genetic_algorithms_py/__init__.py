'''
@authors: Scott Smith, Josh Teeter, Steven Gao, Irfan Lakha
'''

from genetic_algorithms_py import reproduction
from genetic_algorithms_py import mutation
from genetic_algorithms_py import objectiveFunction


def __init__():

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
        printList(matingPool)


    return 0



def printList(list1):
    size = len(list1)

    for i in range(0, size):
        print(list1[i])


'run'
result = __init__()
