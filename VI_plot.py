import os
import matplotlib.pyplot as plt
import random
experiment_path = input("Path: ")
path_contents = os.listdir(experiment_path)
voltage=[]
current =[]
all_voltages=[]
all_currents=[]
for x in path_contents:
    with open(experiment_path+"\\"+x) as file:
        file_lines = file.readlines()

    for line in file_lines:
        if len(line.split())==0 or line.split()[1] == 'V2':
            continue
        voltage.append(float(line.split()[1]))
        current.append(float(line.split()[2]))
    
    all_voltages.append(voltage)
    all_currents.append(current)
    voltage=[]
    current=[]


fig, ax = plt.subplots(num="IV_Plot")

#plots line graph for each experiment
#weibull v breakdown graph
for x in range(len(all_voltages)):
    randcolor=(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))

    ax.plot(all_voltages[x], all_currents[x], color=randcolor,
            label=os.path.basename(path_contents[x]))

# ax.plot(voltages,weibull)
#ax.hlines(0, 0, 20, colors="red", linewidth=1, linestyle='--')
ax.set_xlabel("Voltage")
ax.set_ylabel("Current")
plt.yscale('log')
plt.title(os.path.basename(os.path.dirname(experiment_path)))
#plt.legend()
plt.show()