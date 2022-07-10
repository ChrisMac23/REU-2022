from turtle import width
import matplotlib.pyplot as plt
import numpy as np
import os
import random

colors = ['b', 'g', 'y', 'r', 'c']
max_voltage=0
file_lines = []  # temp variable for reading files

# temp array for holding each array of voltages, cumulative frequencies, and weibull distribuition for one file
voltages = []
cum_freq = []
weibull = []

# arrays for holding each array of voltages, cumulative frequencies, and weibull distribuition of all files
all_voltages = []
all_cum = []
all_weibull = []


experiment_path = input("Path: ")
path_contents = os.listdir(experiment_path)

# retrieves folders with experiment data
path_folders = []
for x in path_contents:
    if os.path.isdir(experiment_path+'\\'+x):
        path_folders.append(experiment_path+'\\'+x)

# reads specified data and calculates cumulative frequency and weibull distribuition from each file
for x in path_folders:

    with open(x+'\\IV_raw-breakdown-sorted.txt', 'r') as file:
        file_lines = file.readlines()

    for line in file_lines:
        voltages.append(float(line))
        if float(line)> max_voltage:
            max_voltage= float(line)

    rel_freq = 1/len(voltages)
    for x in range(len(voltages)-1):
        cum_freq.append((x+1)*rel_freq)
    for x in range(len(voltages)-1):
        if cum_freq[x]==1:
            weibull.append(np.log(-np.log(1-.99999999999999)))
        else:
            weibull.append(np.log(-np.log(1-cum_freq[x])))

    # saves data for each file to list
    voltages = voltages[:-1]
    all_voltages.append(voltages)
    all_cum.append(cum_freq)
    all_weibull.append(weibull)
    voltages = []
    cum_freq = []
    weibull = []

#creating plot
fig, ax = plt.subplots()

#plots line graph for each experiment
#weibull v breakdown graph
for x in range(len(all_voltages)):
    randcolor=(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
    ax.plot(all_voltages[x], all_weibull[x], color=randcolor,
            label=os.path.basename(path_folders[x]))

# ax.plot(voltages,weibull)
ax.hlines(0, 0, max_voltage, colors="red", linewidth=1, linestyle='--')
ax.set_xlabel("Voltage")
ax.set_ylabel("Weibull")
plt.xscale('log')
plt.legend()
plt.show()
