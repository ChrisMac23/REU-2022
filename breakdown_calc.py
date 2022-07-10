# exact same code as C++
import sys
import os

raw_data_path = sys.argv[1]
file_counter = 1
vol = []
curr = []

file_lines = []
breakdown_voltages = []

output= os.path.basename(raw_data_path)
output += "-breakdown"

while True:
    inputfile = raw_data_path+f"\\device-{file_counter:02}-meas-01.txt"
    if not os.path.exists(inputfile):
        print(f"Couldn't open file {inputfile}")
        break

    print(inputfile)
     
    with open(inputfile,'r') as file:
        file_lines = file.readlines()
    
    for line in file_lines:
        intarr = line.split()
        if(len(intarr)==0 or intarr[0]=="Index"):
            continue
        
        vol.append(float(intarr[1]))
        curr.append(float(intarr[2]))

    for x in reversed(range(len(vol)-1)):
        num = curr[x+1]
        if curr[x]*10 < num:
            print(f"Forming Voltage: {vol[x]}")
            breakdown_voltages.append(vol[x])
            break
    
    file_counter +=1
    curr.clear()
    vol.clear()

   
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