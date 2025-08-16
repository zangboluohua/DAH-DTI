# -*- coding:utf-8 -*-
'''
Filename : GenerateData.py
'''

from src.process.triples import csvToStandard, jsonToStandard, \
                                generateDict, splitData

if __name__ == "__main__":
    trainFile = "F:/Trans-Implementation-master/data/DPG-targets/train.txt"
    validFile = "F:/Trans-Implementation-master/data/DPG-targets/valid.txt"
    testFile = "F:/Trans-Implementation-master/data/DPG-targets/test.txt"
    saveDir = "F:/Trans-Implementation-master/data/DPG-3/"
    dictDir = "F:/Trans-Implementation-master/source/dict/DPG"
    # Step1: Transform raw data to standard format
    csvToStandard(rawPath=trainFile,
                  savePath="F:/Trans-Implementation-master/data/DPG-targets/train1.txt",
                  names=["head", "relation", "tail"],
                  header=None,
                  sep="\t",
                  encoding="utf-8")
    csvToStandard(rawPath=validFile,
                  savePath="F:/Trans-Implementation-master/data/DPG-targets/valid1.txt",
                  names=["head", "relation", "tail"],
                  header=None,
                  sep="\t",
                  encoding="utf-8")
    csvToStandard(rawPath=testFile,
                  savePath="F:/Trans-Implementation-master/data/DPG-targets/test1.txt",
                  names=["head", "relation", "tail"],
                  header=None,
                  sep="\t",
                  encoding="utf-8")

    # Step2: Generate dict
    generateDict(dataPath=[trainFile, validFile, testFile],
                 dictSaveDir=dictDir)

    # Step3: Split data
    pass