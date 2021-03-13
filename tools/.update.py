import os
import sys
from sys import platform
path = os.getcwd()
parent = os.path.abspath(os.path.join(path, os.pardir))
os.chdir(parent)
print(os.getcwd())
Print("Reaper update tool made by KrisIsHere | ver. 1.1")
xd = input("Would you like to update? (Y/N): ")
if xd == "Y":
    os.system("rm -rf Reaper ; git clone https://github.com/krisishere/Reaper ; cp -r .info " + parent + "/Reaper/tools/ ;")
    os.chdir(parent + "/Reaper")
    os.system("python3 main.py")
    sys.exit()
if xd == "y":
    os.system("rm -rf Reaper ; git clone https://github.com/krisishere/Reaper ; cp -r .info " + parent + "/Reaper/tools/")
    os.chdir(parent + "/Reaper")
    os.system("python3 main.py")
    sys.exit()
else:
    print("ok")
    sys.exit()
