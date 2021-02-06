#!/usr/bin/python3
#
#  Author:      Richard Barton
#  Date:        12 April 2018
#  Description: Tell me what you think this program is doing.
#

import random

#
#  The following constant is used to size the lists.
#  It should be no less than 10.
#
listSize = 10

##################################################################
#  DON'T MODIFY ANYTHING FROM HERE UNTIL YOU'RE TOLD OTHERWISE.  #
##################################################################
def populateIntList(list):
    #
    #  Pick a number of entries to put into the list.
    #
    i = len(list) // 2
    maxIndex = i + random.randrange(i) + 1

    #
    #  Given the number of entries, figure out an upper
    #  bound so that the sum is still positive in an integer.
    #
    upperBound = 0x40000000 // maxIndex

    #
    #  Put that number of random numbers into the list.
    #
    for i in range(maxIndex):
        list[i] = random.randrange(upperBound)


    #
    #  Tell the caller how many entries we put into the
    #  list.
    #
    return(i + 1)

#########################################
#  MAKE YOUR MODIFICATIONS BELOW HERE.  #
#########################################

#
#  Declare the averageIntList() function as returning an integer
#  and taking two arguments:  an integer list argument and integer
#  count of the number of entries in the list.  The return
#  value is calculated by summing all the entries in the list
#  and dividing that sum by the number of entries in the list.
#
def averageIntList(numList, index):
    return (sum(numList)) // index


#
#  Declare the maximumIntList() function as returning an integer
#  and taking two arguments:  an integer list argument and integer
#  count of the number of entries in the list.  The return
#  value is determined by finding the largest value in the list.
#
def maximumIntList(numList, index):
    return (max(numList))
    
    
#
#  Declare the minimumIntList() function as returning an integer
#  and taking two arguments:  an integer list argument and integer
#  count of the number of entries in the list.  The return
#  value is determined by finding the smallest value in the
#  list.
#
def minimumIntList(numList, index):
    return (min(numList))

#  Size the list.
#
numList = []
for x in range(listSize):
    (numList.insert(0, x)) 
#   

#
#  Put numbers into the list by passing the
#  populateIntList() function the list and saving its
#  return value.
#
populateIntList(numList)
#print(numList)
#print(minimumIntList(numList, listSize))

#
#  Find the average of the numbers in the list by
#  passing the averageIntList() method the list and
#  count and saving its return value.
#
avg = averageIntList(numList, listSize)
#
#  Find the maximum of the numbers in the list by
#  passing the maximumIntList() method the list and
#  count and saving its return value.
#  Display the number of entries and contents of the
#  list in the form:
#    numberCount: 7
#    number[0]: 1798475702
#    number[1]: 1704122948
#       ...
#
maxi = maximumIntList(numList, listSize)
mini = minimumIntList(numList, listSize)

print("numberCount: ", listSize)
for e, i in enumerate(numList):
    
    print("number[{0}]: {1}".format(e, i))

#  Display the statistics in the form:
#    Average: 38233531
#    Maximum: 1798475702
#    Minimum: 353528483
#
print('Average:', avg)
print('Maximum:', maxi)
print('Minimum:', mini)
