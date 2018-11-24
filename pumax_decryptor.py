#this code write by Afshin Zolfaghari
#https://github.com/AfshinZlfgh/
#24 nov 2018
#19:35 (Tehran time)

import sys

import os

key = bytearray(open(sys.argv[1], 'rb').read())
outputPath = sys.argv[2]

inputFiles = []
for(dirpath, dirnames, filenames) in os.walk("./"):
    inputFiles.extend(filenames)
    break


for f in inputFiles:
	if f.endswith(".pumax"):
		print "decrypting %s  ..."%f

		inputFile = bytearray(open(("./"+f), 'rb').read())

		if len(key) < len(inputFile):
			size = len(key)
		else:
			size = len(inputFile)

		print "file size is: %d"%len(inputFile)

		for i in range(size):
			inputFile[i] = inputFile[i] ^ key[i]

		open(outputPath+f[:-6], 'wb').write(inputFile)
		print "[*] decrypted \033[1;33m%s\033[1;m saved to \033[1;33m%s\033[1;m\n"%(f, (outputPath+f[:-6]))
