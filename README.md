# ciphers-in-python
different "encryption tools" based on transposition and Ceaser ciphers in python
the og ciphers are unchaged in the encryption folder
# passtool.py is a bad sudo hashing algorithm
-this uses allTheFuctions.py model, 
-the key is calculated intead of static, 
-uses a diffrent cipher alphebet with no whitspace symbols,
-total block size is determened by the key calculation instead of white spaces.
# problems
-cipher alphebet is in a static order, need to shuffle in some way for new starting pos in the alphebet, needs to be based on the key
-i dont know any fancy enough math to make a true key calculation, that can be someway derived from the encrypted message for decryption
-the closer you get to the GFC for the length of SYMBOLS string the more likely it is to produce 1 as the key 
