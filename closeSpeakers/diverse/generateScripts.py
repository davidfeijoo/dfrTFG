
import numpy as np

testSpeakers = np.loadtxt('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/testSpeakersList.txt')

header = ['#!/bin/bash',
'',
'#PBS -l ncpus=1',
'#PBS -l mem=42GB',
'#PBS -q normal',
'#PBS -P wa66',
'#PBS -l walltime=01:59:00',
'#PBS -l wd',
'',
'module load python3/3.10.4',
'cd /home/561/dr2845/closeSpeakers/Intento\ 3']  

pc = 35

for testSpeaker in testSpeakers:
    testSpeaker = int(testSpeaker)
    f = open(f"/Users/davidfeijoo/bussoImplementation/Close speakers selection/Intento 3/ScriptsSH/{pc}pc/List_testSpeaker_"+str(testSpeaker)+".sh",'w')
    f.writelines(line + '\n' for line in header)
    f.write('\n')
    f.write(f'python3 closeSpeakersList.py --testSpeaker {str(testSpeaker)} --pc {str(pc)} --gadi > /home/561/dr2845/closeSpeakers/logs/diverse/KLDs_{str(pc)}pc/closeSpeakersList_{str(testSpeaker)}.txt')
    f.write('\n')