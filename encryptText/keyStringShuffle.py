def keyStringShuffle(inputStr, key):
    # revInt will hold the output for our new string
    alph1 = ''
    index = len(inputStr)
    while index > key:
        alph1 += inputStr[index - 1]
        index = index - 1
    alpha2 = inputStr[:index]
    newStr = alph1 + alpha2 
    return newStr

if __name__ =='__main__':
    LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    keyStringShuffle(LETTERS,45)