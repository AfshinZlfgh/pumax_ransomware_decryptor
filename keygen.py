
#this code write by Afshin Zolfaghari
#https://github.com/AfshinZlfgh/
#24 nov 2018
#21:07 (Tehran time)

import sys

encryptedFile = bytearray(open(sys.argv[1], 'rb').read())
unEncryptedFile = bytearray(open(sys.argv[2], 'rb').read())

if len(encryptedFile) == len(unEncryptedFile):
    if len(encryptedFile) < 153600:
        print "the input files are small, may it cause broken key."

    size = len(encryptedFile)
    key = bytearray(size)
    size = len(encryptedFile)

    for i in range(size):
        key[i] = encryptedFile[i] ^ unEncryptedFile[i]

    
    keySize = 0
    keyEnd = 0
    for i in key:
        keyEnd = keyEnd + 1
        if i!=0:
            keySize = keyEnd


    key = key[:keySize]
    open("./gold.key", 'wb').write(key)
    print "[*] key succesfully stored in \033[1;33m%s\033[1;m\n"%"gold.key"

else:
    print "mismatch inputs!\ncan't generate key file!"
