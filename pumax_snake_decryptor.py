
#*******************************
# written by afshin zolfaghari
# 29 nov 2018
# 16:06
# ******************************

# ********************************how to use***************************
#copy this file and gold.key in root of your 
#directory that you want to decrypt files in it
#this code crawl in subdirectories and generate
#mirror of directories with only decrypted and healthy files
#in given path.
#if one file not encrypted this code just copy
#it in new place and if encrypted it copy the decrypted
#version.
# python pumax_snake_decryptor.py ./gold.key ./the_store_path(optional: if don't enter it, the files store in run path)
#************************************************************************

import sys
import shutil
import os

key = bytearray(open(sys.argv[1], 'rb').read())
outputPathFromInput = "./"
if len(sys.argv) > 2:
    outputPathFromInput = sys.argv[2]

inputFiles = []
for(dirpath, dirnames, filenames) in os.walk("./"):
    os.mkdir(outputPathFromInput+"decrypted_files/"+dirpath[2:],0777)
    outputPath = outputPathFromInput+"decrypted_files/"+dirpath[2:]
    if outputPath.endswith("/") is False:
        outputPath = outputPath + "/"

    print "dir path: %s"%dirpath
    print "file names: %s\n"%filenames
    for f in filenames:
    	if f.endswith(".pumax"):
            print "decrypting %s  ..."%f
            inputFile = ""
            if dirpath.endswith("/\n"):
                filePath = dirpath+f
            else:
                filePath = dirpath+"/"+f

            inputFile = open(filePath,"rb")
            outputFile = open(outputPath+f[:-6], 'wb')
            inputFileArray = bytearray(inputFile.read(500000000))

            if len(key) < len(inputFileArray):
                size = len(key)
            else:
                size = len(inputFileArray)

            for i in range(size):
                inputFileArray[i] = inputFileArray[i] ^ key[i]

            outputFile.write(inputFileArray)

            inputFileArray = bytearray(inputFile.read(500000000))
            while len(inputFileArray) != 0:
                outputFile.write(inputFileArray)
                inputFileArray = bytearray(inputFile.read(500000000))

            inputFile.close()
            outputFile.close()
            print "[*] decrypted \033[1;33m%s\033[1;m saved to \033[1;33m%s\033[1;m\n"%(f, (outputPath+f[:-6]))
        elif f.endswith("gold.key"):
            print "its key! ignore it!"
        elif f.endswith("decryptor.py"):
            print "its me! ignore it!"
        else:
            print "copy %s  ..."%f
            inputFile = ""
            if dirpath.endswith("/\n"):
                filePath = dirpath+f
            else:
                filePath = dirpath+"/"+f
            shutil.copyfile(src=filePath,dst=(outputPath+f))
