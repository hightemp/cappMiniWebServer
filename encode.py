
import base64
import os
from os.path import *

aDirectories = ['templates', 'assets']
sCurrentDir = os.path.dirname(os.path.abspath(__file__))
sTempDir = join(sCurrentDir, 'temporary')

def fnEcodeFilesInDir(in_sCurrentPath, in_sTempPath):
    for sFileName in os.listdir(in_sCurrentPath):
        sAbsolutePath = join(in_sCurrentPath, sFileName)
        sAbsoluteTempPath = join(in_sTempPath, sFileName)

        print(sAbsolutePath)
        if isdir(sAbsolutePath):
            if not isdir(sAbsoluteTempPath):
                os.makedirs(sAbsoluteTempPath)
            fnEcodeFilesInDir(sAbsolutePath, sAbsoluteTempPath)

    for sFileName in os.listdir(in_sCurrentPath):
        sAbsolutePath = join(in_sCurrentPath, sFileName)
        sAbsoluteTempPath = join(in_sTempPath, sFileName)

        print(sAbsolutePath)
        if isfile(sAbsolutePath):
            try:
                objReadFileHandler = file(sAbsolutePath, "r")
                sBase64Encoded = base64.b64encode(objReadFileHandler.read())
                objWriteFileHandler = file(sAbsoluteTempPath + ".base64", "w")
                objWriteFileHandler.write(sBase64Encoded)
                objWriteFileHandler.close()
                objReadFileHandler.close()
            except Exception as objException:
                print(objException)

for sDirectory in aDirectories:
    sAbsolutePath = join(sCurrentDir, sDirectory)
    sAbsoluteTempPath = join(sTempDir, sDirectory)

    if isdir(sAbsolutePath):
        if not isdir(sAbsoluteTempPath):
            os.makedirs(sAbsoluteTempPath)
        fnEcodeFilesInDir(sAbsolutePath, sAbsoluteTempPath)