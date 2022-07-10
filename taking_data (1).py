import os

device = int(input("Starting device: "))
meas = 1
devices = int(input("How many devices: "))
path = input("Path to data: ")
print(path)
if os.path.isdir(path):
    while device <devices:
        filepath = path+f"\\device-{device:02}-meas-{meas:02}.txt"
        os.system("C:\\Users\\guest1234\\vim\\vim82\\gvim.exe "+'"'+filepath+'"')
        device += 1 

else:
    print("Not a path")
