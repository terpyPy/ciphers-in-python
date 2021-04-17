
#
#  Author:      Cameron Kerley
#  Date:        23 Feb 2020
#  Description: password tool run file
import allTheFuctions
import sys
from random import randrange
from math import sqrt

mode = ''

while True:
    keyDivisor = randrange(1,94)
    mode = (input('[encrypt/decrypt?]: ', ))
    scram = ''
    unScram = ''
    userOption = ((mode[0][0]).lower())
    if userOption == 'e':  # step1 check first char input
        password = (input('[Enter a phrase you want to use]: ' ))
        key = len(password)  # 1.1 get variable key
    #
    #
    # math.sqrt() is a better logic for block encrypted strings
        while key >= keyDivisor:
            key = round(sqrt(key)) 
        print('e key', key,'\n')
       
    #
    # layer one calculated key string, store the block encrypted txt string
        
    #entlilllnk nohIf cnb
    #Tfoccth  t fsnltamn 

    # scrambles the txt given the key previous, this is point of cipher origan for symbols in LETTERS
        scram += (allTheFuctions.ceaser(key,password))
        '''TODO: I wanna add a function that removes the most commen element in list
        and then removes or changes them, and somehow adds that info to the string 
        in such away that i know what position to add them back'''

        encryptedPhrase = (allTheFuctions.encryptMessage(key, scram))
        print('[hash]:--- ', encryptedPhrase, '|end', '\n')
#
#
# decrypt button check
    elif userOption == 'd':
        encryptPass = input('[phrase used?]: ',)  # encrypted phrase
        key = len(encryptPass)  # get the legnth of the keystring

        while key >= keyDivisor:
            key = round(sqrt(key)) 
        print('key calculated!', key,'\n')
        # with the given key decode the string position
        # decrypt block cipher, store the still block encrypted txt string
        unScram += allTheFuctions.ceaserUndo(key, encryptPass)
        unScram = allTheFuctions.decryptMessage(key, unScram)
        
        print('[removed sudo hash]:---- ', unScram)
    elif userOption == 'q':
        print('closing tool')
        sys.exit()
    else:
        continue
