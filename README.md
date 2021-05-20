# ciphers-in-python
different "encryption tools" based on transposition and Ceaser ciphers in python

encrypted:

https://user-images.githubusercontent.com/66324329/118921484-3f6d4480-b906-11eb-869f-1b3339760810.mp4

[demoEcrypted.txt](https://github.com/terpyPy/ciphers-in-python/files/6512984/demoEcrypted.txt)

decrypted:

https://user-images.githubusercontent.com/66324329/118921539-557b0500-b906-11eb-9fde-6491afe8b8ff.mp4

[demoDecrypted.txt](https://github.com/terpyPy/ciphers-in-python/files/6512991/demoDecrypted.txt)




# fileEcryption.py & encrypt text
- this uses encryptText, a module i wrote with simpile file manuipulation  
- the key is asked for by the user, 
- uses a diffrent cipher alphebet order for each key,
- total block size is determened by the key.
# problems
- only 94 key strings possible
- i dont know any fancy enough math to make a true key calculation, that can be someway derived from the encrypted message for decryption
