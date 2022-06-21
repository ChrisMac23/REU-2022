import os

device = 1
meas = 1

path = input("Path to data: ")

if os.path.isdir(path):
    while True:
        filepath = path+f"\\device-{device:02}-meas-{meas:02}.txt"
        os.system("notepad "+filepath)
        meas = 1 if (meas == 2) else 2
        device += 1 if (meas == 1)else 0

else:
    print("Not a path")
