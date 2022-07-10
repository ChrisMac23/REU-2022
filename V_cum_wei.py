import os
import numpy as np  
voltages = []
cum_freq=[]
weibull=[]

bd_path = input("Path to sorted breakdown: ")
with open(bd_path,'r') as file:
    file_lines = file.readlines()

for line in file_lines:
    voltages.append(float(line))

rel_freq = 1/len(voltages)
for x in range(len(voltages)):
    cum_freq.append((x+1)*rel_freq)
for x in range(len(voltages)):
    if cum_freq[x]==1:
        weibull.append(np.log(-np.log(1-.99999999999999)))
    else:
        weibull.append(np.log(-np.log(1-cum_freq[x])))

with open(os.path.dirname(bd_path)+"\\bdV-cum-wei.txt",'w') as file:
    for x in range(len(voltages)):
        file.write(f"{voltages[x]} {cum_freq[x]} {weibull[x]}")
        file.write('\n')