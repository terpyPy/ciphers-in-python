
#
#  Author:      Cameron Kerley
#  Date:        23 Feb 2020
#  Description: password tool run file
import allTheFuctions
import sys
from random import randrange

mode = ''

while True:
    keyDivisor = randrange(0,92)
    mode = (input('[encrypt/decrypt?]: ', ))
    cipherText = None
    unScram = None
    userOption = ((mode[0][0]).lower())
    if userOption == 'e':  # step1 check first char input
        password = (input('[Enter a phrase you want to use]: ' ))
        key = len(password)  # 1.1 get variable key
    #
    #
    # math.sqrt() is a better logic for block encrypted strings
        while key >= keyDivisor:
            key = key // keyDivisor 
        print('e key', key,'\n')
    #
    # layer one calculated key string, store the block encrypted txt string
        
    #entlilllnk nohIf cnb
    #Tfoccth  t fsnltamn 

    # scrambles the txt given the key previous, this is point of cipher origan for symbols in LETTERS
        

        # change the most commen element from cipher text to white space, as it can be used for the block encryption
        # add it to the end of the string so its encrypted by transposition encrypt
        mostFreqEleRomove = allTheFuctions.removeElement(list(password), ' ')
        strList,  totEleRemoved, eleRemoved, removedIndLst = mostFreqEleRomove
        print(strList, eleRemoved, totEleRemoved, removedIndLst)
        # add the identifyer at the end
        moddedCipherText = ''.join(strList) + ''.join(str(removedIndLst)) + str(eleRemoved) + str(totEleRemoved)
        cipherText = (allTheFuctions.ceaser(key, moddedCipherText))
        encryptedPhrase = (allTheFuctions.encryptMessage(key, cipherText))

        print('[hash]:--- ', encryptedPhrase, '- \___end__', '\n')
#
#
# decrypt button check
    elif userOption == 'd':
        encryptPass = input('[phrase used?]: ',)  # encrypted phrase
        key = len(encryptPass)  # get the legnth of the keystring

        while key >= keyDivisor:
            print(key)
            key = key // keyDivisor
        print('key calculated!', key,'\n')

        # decrypt block cipher, 
        unScram = allTheFuctions.ceaserUndo(key, encryptPass)
        # store the cipher text to be broken as a list
        unscramList = list(unScram)
        # grab the commenEle identifyer phrase
        listPhrase = unscramList[-2:]
        EleToAdd, totalToAdd = listPhrase[0], listPhrase[1]
        # with the phrase extract the index list by reading it in reverse excluding the identifyer phrase
        DecodedIndexes = unscramList[slice(-3, totalToAdd, -1)]
        print(EleToAdd, totalToAdd, DecodedIndexes)
        # add the missing element back now that there positions are useable
        for pos, replace in enumerate(unscramList):
            if pos in DecodedIndexes and replace == ' ':
                unscramList.insert(pos, EleToAdd)
                unscramList.pop(pos+1)
        cipherText = ''.join(unscramList)
        print()
        plainText = allTheFuctions.decryptMessage(key, cipherText)
        
        # with the given key decode the string position
        print('[removed sudo hash]:---- ', plainText)
    elif userOption == 'q':
        print('closing tool')
        sys.exit()
    else:
        continue
