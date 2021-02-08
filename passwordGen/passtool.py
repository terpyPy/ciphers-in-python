#!/usr/bin/python3
#
#  Author:      Cameron Kerley
#  Date:        27 July 2019
#  Description: password tool run file
import allTheFuctions
import random
import sys
mode = ''
while True:
    key = random.randrange(1, 94)
    mode = (input('encrypt/decrypt?: ', ))
    scram = ''
    if mode == "encrypt":
        password = (input('Enter a phrase you want to use: ', ))
        scram = (allTheFuctions.encryptMessage(key, password))
        scram = (allTheFuctions.ceaser(key, scram, mode))
        print('hash: ', scram, '\n', 'key: ', key)

    # i need to create a thingUndo function decryption work with the reversing
    # and take multi key input to undo the 2 current layers i.e. key1 and key2
    # d1B17po7T1Id4E1
    elif mode == 'decrypt':
        key = int(input('key used?: '))
        encryptPass = input('phrase used?: ')
        unScram = allTheFuctions.ceaserUndo(key, encryptPass, mode)
        unScram = allTheFuctions.decryptMessage(key, unScram)
        print('removed sudo hash:', unScram)
    elif mode == 'q' or 'quit':
        print('closing tool')
        sys.exit()
    else:
        continue
