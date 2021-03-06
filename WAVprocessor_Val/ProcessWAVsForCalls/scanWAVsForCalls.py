#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
from datetime import datetime
import time

import searchForCalls as sff
import importlib
importlib.reload(sff)
"""

"""
dirWAVs = "/home/val/WAVs"           # folder with wav files
dirOutput = "/home/val/WAVs/Calls"   # folder where output is placed

if dirWAVs.split('/') != '':   #Make sure directory has a final /
    dirWAVs += "/"
    
theWAVs = glob.glob(dirWAVs+"*.wav")
theWAVs = theWAVs + glob.glob(dirWAVs+"*.WAV")

 # setup output file 
 
dirOutput = "/home/val/WAVs/Calls"
if dirOutput.split('/') != '':   #Make sure directory has a final /
    dirOutput += "/"

timeNow = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
outputFile = dirOutput + 'callList_'+timeNow+'.txt'
callOutput = open(outputFile, 'w')  
callOutput.write("fileName\tstartidx\tstopidx\tlencall\tf0\tsigma_f0\tpeak\tsigma_peak\n")  
cnt = 0
start = time.time()
for wav in theWAVs:
    sff.searchForCalls(wav,callOutput, dirOutput)
    cnt += 1
#    if cnt == 3:
#        break
stop = time.time()    
print("Processed ", cnt, " WAV files in", np.round(stop-start), " seconds.")
callOutput.close()