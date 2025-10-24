# -*- coding: utf-8 -*-

import torch
from src.utils.utils import CheckPath

class Config():
    def __init__(self):
        # Data arguments
        self.pospath = "F:/Trans-Implementation-master/data/DPG-targets/train.txt"
        self.validpath = "F:/Trans-Implementation-master/data/DPG-targets/valid.txt"
        self.entpath = "F:/Trans-Implementation-master/source/dict/DPG/entityDict.json"
        self.relpath = "F:/Trans-Implementation-master/source/dict/DPG/relationDict.json"
        self.embedpath = "F:/Trans-Implementation-master/source/embed/"
        self.logpath = "F:/Trans-Implementation-master/source/log/"
        self.savetype = "pkl"

        # Dataloader arguments
        self.batchsize = 40
        self.shuffle = True
        self.numworkers = 0
        self.droplast = False
        self.repproba = 0.5
        self.exproba = 0.5

        # Model and training general arguments
        self.TransE = {"EmbeddingDim": 100,
                       "Margin":       1.0,
                       "L":            2}
        self.TransH = {"EmbeddingDim": 100,
                       "Margin":       1.0,
                       "L":            2,
                       "C":            0.1,
                       "Eps":          0.01}
        self.TransD = {"EntityDim":    100,
                       "RelationDim":  100,
                       "Margin":       2.0,
                       "L":            2}
        self.TransA = {"EmbeddingDim": 100,
                       "Margin":       3.2,
                       "L":            2,
                       "Lamb":         0.1,
                       "C":            0.2}
        self.KG2E   = {"EmbeddingDim": 100,
                       "Margin":       4.0,
                       "Sim":          "EL",
                       "Vmin":         0.03,
                       "Vmax":         3.0}
        self.usegpu = torch.cuda.is_available()
        self.gpunum = 0
        self.modelname = "TransA"
        self.weightdecay = 0
        self.epochs = 5
        self.evalepoch = 1
        self.learningrate = 0.01
        self.lrdecay = 0.96
        self.lrdecayepoch = 1
        # 只支持Adam优化
        self.optimizer = "Adam"
        self.evalmethod = "MR"
        self.simmeasure = "L2"
        self.modelsave = "param"
        self.modelpath = "F:/Trans-Implementation-master/source/model/"
        self.loadembed = False
        self.entityfile = "F:/Trans-Implementation-master/source/embed/entityEmbedding.txt"
        self.relationfile = "F:/Trans-Implementation-master/source/embed/relationEmbedding.txt"
        self.premodel = "F:/Trans-Implementation-master/source/model/TransE_ent128_rel128.param"

        # Other arguments
        self.summarydir = "F:/Trans-Implementation-master/source/summary/TransA/"

        # Check Path
        self.CheckPath()

        # self.usePaperConfig()

    def usePaperConfig(self):
        # Paper best params
        if self.modelname == "TransE":
            self.embeddingdim = 50
            self.learningrate = 0.01
            self.margin = 1.0
            self.distance = 1
            self.simmeasure = "L1"
        elif self.modelname == "TransH":
            self.batchsize =32
            self.embeddingdim = 50
            self.learningrate = 0.1
            self.margin = 0.5
            self.C = 0.015625
        elif self.modelname == "TransD":
            self.batchsize =32
            self.entitydim = 100
            self.relationdim = 100
            self.margin = 2.0


    def CheckPath(self):
        # Check files
        CheckPath(self.pospath)
        CheckPath(self.validpath)

        # Check dirs
        CheckPath(self.modelpath, raise_error=False)
        CheckPath(self.summarydir, raise_error=False)
        CheckPath(self.logpath, raise_error=False)
        CheckPath(self.embedpath, raise_error=False)


