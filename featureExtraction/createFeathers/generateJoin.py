import numpy as np

numero = 1000 #tiene que ser divisible entre 100

header = ['import numpy as np',
'import pandas as pd',
'from datetime import datetime',
]  
f = open('/Users/davidfeijoo/bussoImplementation/models/joinFeatures1000.py','w')
f.writelines(line + '\n' for line in header)
f.write('\n')
f.write(f'def joinFeatures(dictsList,audioNameList):\n\n\tnumero = {numero}\n\n')
f.write('\tnow = datetime.now()\n\tcurrent_time = now.strftime("%H:%M:%S")\n\tprint(f"Joining features...:  {current_time}")\n\n')
f.write('\tlength = len(dictsList)\n')
f.write('\tglobalFM = np.empty((0,6381))\n\n')

for i in range(numero):
    f.write(f'\tglobalFM{i} = np.empty((0,6381))\n')

f.write('\n\tM = 0\n\n')

for i in range(numero):
    if i != numero-1:
        f.write(f'\tfor dict in dictsList[{i}*int(length/numero):{i+1}*int(length/numero)]:\n')
        f.write(f'\t\tdataArray = []\n')
        f.write(f'\t\tdataArray.append(audioNameList[M])\n')
        f.write(f'\t\tdataArray.extend(dict.values())\n')
        f.write(f'\t\tglobalFM{i} = np.row_stack((globalFM{i},dataArray))\n')
        f.write(f'\t\tM += 1\n')
        f.write(f'\tprint(M)\n\n')
    else:
        f.write(f'\tfor dict in dictsList[{i}*int(length/numero):]:\n')
        f.write(f'\t\tdataArray = []\n')
        f.write(f'\t\tdataArray.append(audioNameList[M])\n')
        f.write(f'\t\tdataArray.extend(dict.values())\n')
        f.write(f'\t\tglobalFM{i} = np.row_stack((globalFM{i},dataArray))\n')
        f.write(f'\t\tM += 1\n')
        f.write(f'\tprint(M)\n\n')

for n in range(int(10)):

    f.write(f'\tglobalFMx{n} = np.row_stack((')

    for i in range(int(numero/10)):

        f.write(f'globalFM{int(i+int(numero/10)*n)},')

    f.write('))\n')

f.write('\tglobalFM = np.row_stack((')
for n in range(int(10)):#10
    f.write(f'globalFMx{n},')
f.write('))\n')



f.write('\tnow = datetime.now()\n\tcurrent_time = now.strftime("%H:%M:%S")\n\tprint(f"Features joined!:  {current_time}")\n')
f.write('\tprint("Global fm", globalFM)\n\tprint("M", M)\n\tprint("Number of utterances in global fm",globalFM.shape[0])\n\n\n')
f.write('\treturn globalFM')

