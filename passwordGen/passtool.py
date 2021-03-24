#!/usr/bin/python3
#
#  Author:      Cameron Kerley
#  Date:        23 Feb 2020
#  Description: password tool run file
import allTheFuctions
import math
import sys
mode = ''
keyDivisor = 91
while True:

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
            key = round(math.sqrt(key))
        print('e key', key,'\n')
    #
    # layer one calculated key string, store the block encrypted txt string
        
    #entlilllnk nohIf cnb
    #Tfoccth  t fsnltamn 
    # scrambles the txt given the key previous, this is point of cipher origan for symbols in LETTERS
        scram = (allTheFuctions.ceaser(key,password ))
        scram = (allTheFuctions.encryptMessage(key, scram))
        print('[hash]:--- ', scram, '\n', '\n')
#
#
# decrypt button check
    elif userOption == 'd':
        encryptPass = input('[phrase used?]: ',)  # encrypted phrase
        key = len(encryptPass)  # get the legnth of the keystring

        while key >= keyDivisor:
            key = round(math.sqrt(key))
        print('key calculated!', key,'\n')

        # decrypt layer one calculated key string, store the still block encrypted txt string
        unScram += allTheFuctions.ceaserUndo(key, encryptPass)
        # with the given key decode the string position
        unScram = allTheFuctions.decryptMessage(key, unScram)
        print('[removed sudo hash]:---- ', unScram)
    elif userOption == 'q':
        print('closing tool')
        sys.exit()
    else:
        continue
