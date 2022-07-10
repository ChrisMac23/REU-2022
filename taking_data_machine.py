import string
import pyvisa as visa
import os
import matplotlib.pyplot as plt
import random
import time
data = []
os.add_dll_directory("C:/Program Files/Keysight/IO Libraries Suite/bin")
os.add_dll_directory("C:/Program Files (x86)/Keysight/IO Libraries Suite/bin")
rm = visa.ResourceManager("C:/Windows/System32/visa32.dll")

resources = rm.list_resources()
if 'GPIB1::17::INSTR' in resources:
    print("Found SPA")
spa = rm.open_resource('GPIB1::17::INSTR')

spa.write('*RST')
print(spa.query('*IDN?', delay=.1))
spa.write(':SYST:LANG COMP')
time.sleep(3)
spa.write('DE',)
spa.write("CH1")
spa.write("CH2 , 'V2','I2',1,1")
spa.write("CH3 , 'V3','I3',3,3")
spa.write("CH4")

spa.write("SS;")
spa.write("VR1, 0 , 20,.1,.0000005")
spa.write("IT 1;")
spa.write("SM;")
spa.write("XN 'V2', 1,0,20;")
spa.write("YA 'I2', ,1E-13,1E-2;")
spa.write('MD;')
spa.write('ME 1;')
while spa.stb != 1:
    pass
print("done")
# spa.write(''.join(['CH ', '1', ',', "''", "V1", "''", ',', "''", "I1", "''", ',', "1", ',', "2", ';']))
#spa.write('MD 1;')
dummy:string = spa.query("DO 'V2';")
print(dummy)
dummy = dummy.replace('N', '')
dummy = dummy.replace('C', '')
#dummy = dummy.replace(' ', '')
print(dummy)
str_v_list=dummy.split(',')
print(str_v_list)
v_list=[float(i)for i in str_v_list]
print(v_list)


done = False
dummy:string = spa.query("DO 'I2';")
print(dummy)
dummy = dummy.replace('N', '')
dummy = dummy.replace('C', '')
#dummy = dummy.replace(' ', '')
print(dummy)
str_i_list=dummy.split(',')
print(str_i_list)
i_list=[float(i)for i in str_i_list]
print(i_list)
spa.close()

fig, ax = plt.subplots(num="IV_Plot")

#plots line graph for each experiment
#weibull v breakdown graph

randcolor=(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))

ax.plot(v_list, i_list, color=randcolor)

# ax.plot(voltages,weibull)
#ax.hlines(0, 0, 20, colors="red", linewidth=1, linestyle='--')
ax.set_xlabel("Voltage")
ax.set_ylabel("Current")
plt.yscale('log')
plt.title("VI")
#plt.legend()
plt.show()