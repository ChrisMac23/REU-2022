# exact same code as C++
import sys
import os
import pdb

raw_data_path = sys.argv[1]
file_counter = 1
vol = []
curr = []

file_lines = []
breakdown_voltages = []

output= os.path.basename(raw_data_path)
output += "-breakdown"
# list to hold data sets
data = []

#inputfile = raw_data_path+f"\\device-{file_counter:02}-meas-01.txt"
inputfile = raw_data_path+"\\data.txt"
if not os.path.exists(inputfile):
    print(f"Couldn't open file {inputfile}")

print(inputfile)
 
with open(inputfile,'r') as file:
    file_lines = file.readlines()

device_num_previous = 1
for line in file_lines:
    intarr = line.split()
    # skip heading
    if intarr[0]=="Index":
        continue
    
    # get current device number
    device_num_current = int(intarr[0].split('/')[0])
    
    if device_num_current > device_num_previous: # at next device
        
        # extract breakdown voltage
        for x in reversed(range(len(vol)-1)):
            num = curr[x+1]

            if curr[x]*10 < num:
                print(f"Forming Voltage: {vol[x]}")
                breakdown_voltages.append(vol[x])       
                curr.clear()
                vol.clear()
                device_num_previous = device_num_current
                break
                
               
    else:
        vol.append(float(intarr[1]))
        curr.append(float(intarr[2]))
  

   
with open(os.path.dirname(raw_data_path)+"\\"+ output+".txt",'w') as file:
    for line in breakdown_voltages:
        file.write(str(line))
        file.write('\n')
    
breakdown_voltages.sort()
with open(os.path.dirname(raw_data_path)+"\\"+output+"-sorted.txt",'w') as file:
    for line in breakdown_voltages:
        file.write(str(line))
        file.write('\n')
    

print(f"Saved to {output}")