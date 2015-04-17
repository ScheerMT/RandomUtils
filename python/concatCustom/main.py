# -*- coding: utf-8 -*-
import os
import pprint

pp = pprint.PrettyPrinter(indent=4)

FILES_FOLDER_NAME = 'files/'

def ReturnTestFiles():
    """
    Returns a list of the test files found within the TESTBENCHFOLDER
    """
    data = []

    for fn in os.listdir('./' + FILES_FOLDER_NAME):
        # curFile = './' + FILES_FOLDER_NAME + fn
        if not os.path.isdir(fn):
            data.append('./' + FILES_FOLDER_NAME + fn)
    data.sort()
    return data

finalData = dict()

for fileLoc in ReturnTestFiles():
    with open(fileLoc, 'rb') as f:
        curFileLineList = list(f)
        curFileTotalLine = len(curFileLineList)

        for n in range(0, curFileTotalLine, 2):
            if curFileLineList[n] in finalData:
                finalData[curFileLineList[n]] = finalData[curFileLineList[n]] + curFileLineList[n+1].strip()
            else:
                finalData[curFileLineList[n]] = curFileLineList[n+1].strip()

print "RAW DICTIONARY:"
pp.pprint(finalData)


with open("OUTPUT.txt", 'w') as f:
    for key,value in finalData.items():
        f.write(key)
        f.write(value)
        f.write('\n')
