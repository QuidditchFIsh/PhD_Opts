#Testing file#

import numpy as np

frequencies = []
Capaticance = []
Josephson_Energy = []
Strength = []

opt_freq = []
opt_str = []
temp = []

with open('Frequency_Data.txt') as f:
    for line in f:
        line = line.strip().split()
        frequencies.append(float(line[2]))
        Capaticance.append(float(line[1]))
        Josephson_Energy.append(float(line[0]))
        Strength.append(float(line[3]))
with open('Optimization_Output.dat') as f:
    for line in f:
        line = line.strip().split()
        temp.append(float(line[0]))
        temp.append(float(line[1]))
        temp.append(float(line[2]))
        temp.append(float(line[3]))
        opt_freq.append(temp)
        temp = []
        opt_str.append(float(line[4]))


Index0 = [i for i, _ in enumerate(frequencies) if np.isclose(_, opt_freq[0][0],0.001)]
Index1 = [i for i, _ in enumerate(frequencies) if np.isclose(_, opt_freq[0][1],0.001)]
Index2 = [i for i, _ in enumerate(frequencies) if np.isclose(_, opt_freq[0][2],0.001)]
Index3 = [i for i, _ in enumerate(frequencies) if np.isclose(_, opt_freq[0][3],0.001)]

for i in range(0,10):
    print(str(Capaticance[Index0[i]]) + " " + str(Josephson_Energy[Index0[i]]) + " " + str(frequencies[Index0[i]]) + "\n")
