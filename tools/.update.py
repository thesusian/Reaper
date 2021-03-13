import os
import sys
from sys import platform
path = os.getcwd()
parent = os.path.abspath(os.path.join(path, os.pardir))
os.chdir(parent)
print(os.getcwd())
xd = input("Would you like to update? (Y/N): ")
if xd == "Y":
    os.system("rm -rf Reaper ; git clone https://github.com/krisishere/Reaper ; cp -r .info " + parent + "/Reaper/tools/ ; touch Reaper/.info/tos_agree.py")
    os.chdir(parent + "/Reaper")
    os.system("python3 main.py")
    sys.exit()
if xd == "y":
    os.system("rm -rf Reaper ; git clone https://github.com/krisishere/Reaper ; cp -r .info " + parent + "/Reaper/tools/ ; touch Reaper/.info/tos_agree.py")
    os.chdir(parent + "/Reaper")
    os.system("python3 main.py")
    sys.exit()
else:
    print("ok")
    sys.exit()
