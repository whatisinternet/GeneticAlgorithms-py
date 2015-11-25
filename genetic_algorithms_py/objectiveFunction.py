'''
@authors: Scott Smith, Josh Teeter, Steven Gao, Irfan Lakha
'''


def OFSimple( bitStringList, targetBitStr):
    '''
    Inputs a list of strings of bits, outputs a list of values between 0 and 1 to measure a percentage
    that the string meets the objective function's requirements. ie. 0.99 is equivalent to the string
    being %99 similar to what the objective function is optimizing.
    '''
    resultList = [ ]
    convertedList = [ ]

    targetNum = int(targetBitStr,2)                         #convert target bit string to integer

    for str1 in bitStringList:

        bitStrConvertedToInt = int(str1,2)                    #convert to base 10 from base 2
        convertedList.append( bitStrConvertedToInt )          #append converted bit string to use later


    theMax = max(convertedList)
    theMin = min(convertedList)
    rangeSize = theMax - theMin

    #have maximum and minimum range, now go through converted values to compare % that it is close to target number compared to range possible

    for convertedBitStr in convertedList:

        distanceToGoal = abs(targetNum - convertedBitStr )

        percentResult = abs( 1 - (distanceToGoal / rangeSize) )          #Percentage (values between 0 to 1)
        #0 is furthest extrema (minimum or maximum), 1 is goal

        resultList.append(  percentResult  )


    return resultList








