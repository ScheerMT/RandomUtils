# -*- coding: utf-8 -*-
import os
import pprint

pp = pprint.PrettyPrinter(indent=4)

FILES_FOLDER_NAME = 'files/'


def ReturnTestFiles():
    '''
    Grabs a list of files contained within FILES_FOLDER_NAME and outputs a
    list of those names (with folder appended to front).
    '''
    data = []

    for fn in os.listdir('./' + FILES_FOLDER_NAME):
        # curFile = './' + FILES_FOLDER_NAME + fn
        if not os.path.isdir(fn):
            data.append('./' + FILES_FOLDER_NAME + fn)
    data.sort()
    return data

# Construct for file output
finalData = dict()


for fileLoc in ReturnTestFiles():
    with open(fileLoc, 'rb') as f:
        curFileLineList = list(f)
        curFileTotalLine = len(curFileLineList)

        # Every other line contains a key whereas data to be appended to key
        #  is in the other line (even = key, odd = value)
        #  if the key already exists then add it to the end.
        for n in range(0, curFileTotalLine, 2):
            if curFileLineList[n] in finalData:
                finalData[curFileLineList[n]] = finalData[curFileLineList[n]] + curFileLineList[n+1].strip()
            else:
                finalData[curFileLineList[n]] = curFileLineList[n+1].strip()

# Test printing
print "RAW DICTIONARY:"
pp.pprint(finalData)


with open("OUTPUT.txt", 'w') as f:
    for key, value in finalData.items():
        f.write(key)
        f.write(value)
        f.write('\n')
